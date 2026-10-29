"""Assemble the complete audit manuscript without modifying scientific inputs."""
from pathlib import Path
import os
import re
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PAPER=ROOT/'paper'
def section(filename,title):
    text=(PAPER/filename).read_text(encoding='utf-8').strip()
    lines=text.splitlines()
    if not lines or not lines[0].startswith('## '):
        raise ValueError('Expected a level-two component heading: '+filename)
    lines[0]='## '+title
    return '\n'.join(lines)

opening=(PAPER/'opening.md').read_text(encoding='utf-8').strip()
source=section('source-provenance.md','3. Source provenance and released particle data')
methods=section('methods-results.md','4. First-passage attribution and recorded region histories')
measured=section('released-batch-results.md','5. Matched attribution on the released particle batches')
diagnostics=(PAPER/'resampling-validation.md').read_text(encoding='utf-8').strip()
assert diagnostics.startswith('### ')
measured += '\n\n'+diagnostics
ancillary=section('ancillary-checks.md','Appendix B. Ancillary source and diagnostic checks')
proxy=section('proxy-validation.md','Appendix C. Positive checks and inferred display reconstruction')
upstream=section('audited-function.md','Appendix D. Deposited first-passage routine')
protocol=section('reanalysis-protocol.md','6. Extending the comparison to the historical population')
theory=section('theory-and-estimands.md','Appendix A. Estimator identities and sampling limits')
closing=(PAPER/'closing.md').read_text(encoding='utf-8')
assert closing.count('## References\n')==1
conclusion,refs=closing.split('## References\n',1)
text='\n\n'.join([opening,source,methods,measured,protocol,conclusion.strip(),theory,ancillary,proxy,upstream,'## References\n'+refs.strip()])+'\n'
assert text.count('## Abstract\n')==1
headings=re.findall(r'^## (\d+)\. ',text,re.M)
assert headings==[str(i) for i in range(1,9)],headings
(PAPER/'manuscript.md').write_text(text,encoding='utf-8',newline='\n')
pandoc=os.environ.get('PANDOC') or shutil.which('pandoc')
if not pandoc:
    raise RuntimeError('Pandoc is required for manuscript assembly; install it on PATH or set PANDOC to its executable.')
subprocess.run([pandoc,str(PAPER/'manuscript.md'),'-f','markdown+tex_math_dollars+raw_tex+autolink_bare_uris',
    '-t','latex','--no-highlight','-o',str(PAPER/'latex/body.tex')],check=True)
body=(PAPER/'latex/body.tex').read_text(encoding='utf-8').replace('../figures/','images/')
def code_span(match):
    if ' ' in match[1]:return match[0]
    return r'\nolinkurl{'+match[1].replace(r'\_','_')+'}'
body=re.sub(r'\\texttt\{([^{}]*)\}',code_span,body)
body,listing_count=re.subn(r'\\begin\{verbatim\}\n(def get_energy_by_region_w_bands.*?)(?:\n)\\end\{verbatim\}',
    lambda m:r'\begin{lstlisting}[firstnumber=344]'+'\n'+m[1]+'\n'+r'\end{lstlisting}',body,flags=re.S)
assert listing_count==1,listing_count
# Portable reproduction commands can exceed one printed line. Preserve their
# literal contents while allowing TeX to wrap them without adding line numbers.
body=re.sub(r'\\begin\{verbatim\}\n(.*?)\n\\end\{verbatim\}',
    lambda m:r'\begin{lstlisting}[numbers=none]'+'\n'+m[1]+'\n'+r'\end{lstlisting}',body,flags=re.S)
def keep_small_table(match):
    # Both manuscript tables have four rows. Keep each together so a float
    # cannot strand a repeated longtable header on the following page.
    table=match[0].replace(r'\begin{longtable}[]',r'\begin{tabular}')
    table=table.replace('\\endhead\n\\bottomrule\\noalign{}\n\\endlastfoot\n','')
    table=table.replace(r'\end{longtable}',r'\bottomrule\noalign{}'+'\n'+r'\end{tabular}')
    font=r'\small' if 'Conditional' in table and 'percentile' in table else ''
    return r'\par\noindent\begin{minipage}{\linewidth}'+font+'\n'+table+'\n'+r'\end{minipage}\par'
body,table_count=re.subn(r'\\begin\{longtable\}.*?\\end\{longtable\}',keep_small_table,body,flags=re.S)
assert table_count>=2,table_count
body=re.sub(r'^(\\subsection\{[45678]\. )',r'\\FloatBarrier\n\1',body,flags=re.M)
heading=r'\subsection{References}\label{references}'
assert body.count(heading)==1
prefix,reference_body=body.split(heading,1)
paragraphs=[x for x in reference_body.strip().split('\n\n') if x.strip()]
reference_body='\n\n'.join(r'\begin{samepage}'+'\n'+x+'\n'+r'\end{samepage}' for x in paragraphs)
body=prefix+r'\clearpage'+'\n'+heading+'\n\n'+r'\begingroup\small'+'\n'+reference_body+'\n'+r'\endgroup'+'\n'
(PAPER/'latex/body.tex').write_text(body,encoding='utf-8',newline='\n')
(PAPER/'latex/images').mkdir(exist_ok=True)
for image in (ROOT/'figures').glob('*.png'):
    shutil.copy2(image,PAPER/'latex/images'/image.name)
print({'words_regex':len(re.findall(r'\b[\w-]+\b',text)),'characters':len(text),'numbered_sections':len(headings)})
