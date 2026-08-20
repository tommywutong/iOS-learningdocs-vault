---
title: 'Animalify: Using Safari App Extensions to modify pages and communicate with
  native code'
apple_id: TP40017383
resource_type: Sample Code
platform: macOS
topic: null
technology: SafariServices
published: '2016-11-03'
source_url: https://developer.apple.com/library/archive/samplecode/Animalify/Listings/Animalify_Extension_script_js.html
archived_at: '2026-07-18T03:01:01.336300Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Animalify: Using Safari App Extensions to modify pages and communicate with native code](Animalify-%20Using%20Safari%20App%20Extensions%20to%20modify%20pages%20and%20communicate%20with%20nati.md)


[Next](Animalify%20Extension-SafariExtensionHandler.swift.md)[Previous](README.md.md)

# Animalify Extension/script.js

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This is the content script injected into web pages. Once the DOM has loaded on the web page that this content script is injected into, it sends a message to the Safari App Extension, and gets a response with the words to replace and what to replace them with. Once it gets the response, it traverses the DOM and performs the replacements.
*/

// Wait for the DOM to load before dispatching a message to the app extension's Swift code.
document.addEventListener("DOMContentLoaded", function(event) {
    safari.extension.dispatchMessage("GetWordsAndReplacements");
});

// Listens for messages sent from the app extension's Swift code.
safari.self.addEventListener("message", messageHandler);

function messageHandler(event)
{
    if (event.name === "WordsAndReplacements") {
        // The userInfo of the call to -[SFSafariPage dispatchMessageToScriptWithName:userInfo:].
        var wordReplacementMap = event.message;
        for (var wordToReplace in wordReplacementMap) {
            replace(document.body, wordToReplace, wordReplacementMap[wordToReplace]);
        }
    }
}

function replace(node, word, replacement) {
    switch (node.nodeType)
    {
        case Node.ELEMENT_NODE:
            // We don't want to replace text in an input field or textarea.
            if (node.tagName.toLowerCase() === "input" || node.tagName.toLowerCase() === "textarea") {
                return;
            }

            // For other types of element nodes, we explicitly fall through to iterate over their children.
        case Node.DOCUMENT_NODE:
        case Node.DOCUMENT_FRAGMENT_NODE:
            // If the node is a container node, iterate over all the children and recurse into them.
            var child = node.firstChild;
            var next = undefined;
            while (child) {
                next = child.nextSibling;
                replace(child, word, replacement);
                child = next;
            }
            break;
        case Node.TEXT_NODE:
            // If the node is a text node, perform the text replacement.
            replaceTextInTextNode(node, word, replacement);
            break;
    }
}

function replaceTextInTextNode(textNode, word, replacement) {
    // Skip over nodes that aren't text nodes.
    if (textNode.nodeType !== Node.TEXT_NODE)
        return;

    // And text nodes that don't have any text.
    if (!textNode.nodeValue.length)
        return;

    // Generate a regular expression object to perform the replacement.
    var expressionForWordToReplace = new RegExp(word, "gi");
    var nodeValue = textNode.nodeValue;
    var newNodeValue = nodeValue.replace(expressionForWordToReplace, replacement);

    // Perform the replacement in the DOM if the regular expression had any effect.
    if (nodeValue !== newNodeValue) {
        textNode.nodeValue = newNodeValue;
    }
}
```

[Next](Animalify%20Extension-SafariExtensionHandler.swift.md)[Previous](README.md.md)

