# coding:utf-8
import sys
import jsbeautifier

js_file = sys.argv[1]

opts = jsbeautifier.default_options()
opts.indent_size = 2
opts.space_in_empty_paren = True

js_beautify = jsbeautifier.beautify_file(js_file, opts)
with open(js_file, "w+", encoding='utf-8') as beautify:
    beautify.write(js_beautify)

with open(js_file, "r", encoding='utf-8') as toc:
    lines = toc.readlines()

# Delete unwanted rows in the simplest mindless way
with open(js_file, "w", encoding='utf-8') as toc:
    for line in lines:
        if "(function() {" in line:
            continue
        if "window.rh.model.publish(rh.consts('KEY_TEMP_DATA'), toc, {" in line:
            continue
        if "sync: true" in line:
            continue
        if "});" in line:
            continue
        if "})();" in line:
            continue
        toc.write(line)

with open(js_file, "a", encoding='utf-8') as toc:
    toc.write("module.exports = toc;")