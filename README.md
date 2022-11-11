# robohelp-to-markdown-script
Convert RoboHelp Manual to Markdown script. (semi-automatic, manual adjustment is required after use)

将 RoboHelp 制作的文档转换为 Markdown（脚本为半自动，使用后需手动调整部分文件）

## Usage

1. Installation Python dependencies
```bash
pip install -r requirements.txt
```
2. Download and install Pandoc from [here](https://github.com/jgm/pandoc/releases/latest) if you are using Windows.
3. Copy all files in `GMS2-Robohelp-en` to `workdir`.(The folder itself is not included, i.e. "workdir/GMS2-Robohelp-en" is invalid.)
4. Executes batches in `scripts` in the order of file names.(If the batch prompts that the file cannot be found, please copy these batches to this repo root directory.)

## Requirement

 - Python >= 3.8
 - Pandoc (command-line)
 - Node.js (for `OutputSidebar.js`, but optional)

## Manual by yourself

It is recommended to use Visual Studio Code for the following operations (all global)

 - Replace "\&amp;lt;" to "<"
 - Replace "\&amp;gt;" to ">"
 - Replace "\&amp;amp;" to "&"
 - Replace ".htm" to ""(empty)
