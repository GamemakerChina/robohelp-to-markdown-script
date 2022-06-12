"use strict";
const fs = require("fs");
const path = require("path");

let toc = require("./workdir/whxdata/toc.new");
let sidebarTxt = '- [**首页**](/README.md)\n';
let relativePathArr;

function addNestedTOC(toc, callback) {
    for (let i = 0; i < toc.length; i++) {
        if ("url" in toc[i]) {
            // relativePathArr = toc[i].url.split('\/');
            // for (let j = 1; j < relativePathArr.length; j++) {
            //     if (toc[i].type != "book") {
            //         sidebarTxt += "  ";
            //     }
            // }
            sidebarTxt += '- [' + toc[i].name + '](/' + toc[i].url.replace(".htm", "") + ')\n';
        };
        if ("key" in toc[i]) {
            let toc2 = require("./workdir/whxdata/" + toc[i].key + ".new");
            addNestedTOC(toc2, callback);
        }
    };
};

function addFirstTOC() {
    for (let k = 0; k < toc.length; k++) {
        sidebarTxt += '- [' + toc[k].name + '](/' + toc[k].url.replace(".htm", "") + ')\n';
        if ("key" in toc[k]) {
            let toc2 = require("./workdir/whxdata/" + toc[k].key + ".new");
            addNestedTOC(toc2);
        }
    }
}
addFirstTOC();
fs.writeFile(path.resolve('./') + '/_sidebar.md', sidebarTxt, function (err) {
    if (err) {
        console.error(err);
    }
});