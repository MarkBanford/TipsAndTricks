import markdown
from markdown.extensions.toc import TocExtension

md_text = '[TOC]\n# Title\n**text**'
# baselevel=2 sets headings to start at `h2`
html = markdown.markdown(md_text, extensions=[TocExtension(baselevel=2, title='Contents')])
print(html)