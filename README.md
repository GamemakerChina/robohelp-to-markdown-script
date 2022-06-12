# robohelp-to-markdown-script
Convert RoboHelp Manual to Markdown script. (semi-automatic, manual adjustment is required after use)

将 RoboHelp 制作的文档转换为 Markdown（脚本为半自动，使用后需手动调整部分文件）

## Requirement

 - Python >= 3.8
    - lxml
    - BeautifulSoup (bs4)
    - Pandoc
    - jsbeautifier

 - Node.js 

## Manual by yourself

 - Replace "\&amp;lt;" to "<"
 - Replace "\&amp;gt;" to ">"
 - Replace ".htm" to ""(empty)
