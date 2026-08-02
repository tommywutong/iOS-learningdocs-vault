---
title: WebKit DOM Programming Topics
apple_id: TP40001483
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: WebKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/DOM.html
archived_at: '2026-07-15T05:18:09.816402Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit DOM Programming Topics](index.md)



## Using the Document Object Model

The JavaScript Document Object Model implements the Document Object Model specification, a platform- and language-neutral interface developed by the World Wide Web Consortium. This specification allows programs and scripts to dynamically access and change the content, structure, and style of a document —usually HTML or XML—by providing a structured set of objects that correspond to the document’s elements.

The Level 2 DOM specification in particular added the ability to create object trees from style sheets, and manipulate the style data of document elements.

The Document Object Model is already implemented in a wide variety of languages, most notably JavaScript. Each declaration in the JavaScript DOM was created using the Interface Definition Language (IDL) files from the W3C.

By taking advantage of the DOM, you can:

- Rearrange sections of a document without altering their contents
- Create and delete existing elements as discrete objects
- Search and traverse the document tree and the subtrees of any element on the tree
- Completely isolate the document’s structure from its contents

### Accessing a Document’s Structure with the DOM

The primary function of the Document Object Model is to view, access, and change the structure of an HTML document separate from the content contained within it. You can access certain HTML elements based on their `id` identifier, or allocate arrays of elements by their tag or CSS class type. All transformations are done according to the most recent HTML specification. More importantly, they happen dynamically—any transformation will happen without reloading the page.

The DOM tree is completely comprised of JavaScript objects. Some of the fundamental and most commonly-used ones are listed in Table 1-1.

__Table 1-1__Commonly used JavaScript DOM types

| DOM object | Definition |
| --- | --- |
| `document` | Returns the document object for the page. Represents the root node of the DOM tree, and actions on it will affect the entirety of the page. |
| `element` | Represents an instance of most structures and sub-structures in the DOM tree. For example, a text block can be an element, and so can the entire `body` section of an HTML document. |
| `nodeList` | A `nodeList` is equivalent to an array, but it is an array specific to storing elements. You can access items in a nodeList through common syntax like `myList[n]`, where `n` is an integer. |

There are a number of JavaScript methods specified by the DOM which allow you to access its structure. Some of the fundamental and most commonly-used ones are listed in Table 1-2.

__Table 1-2__Commonly used JavaScript DOM methods

| DOM method | Parent class(es) | Definition |
| --- | --- | --- |
| `element` `getElementById``(`_id_`)` | `document`, `element` | Returns the element uniquely identified by its `id` identifier. |
| `nodeList` `getElementsByTagName``(`_name_`)` | `document`, `element` | Returns a `nodeList` of any elements that have a given tag (such as `p` or `div`), specified by _name._ |
| `element` `createElement``(`_type_`)` | `element` | Creates an element with the type specified by _type_ (such as `p` or `div`) |
| `void` `appendChild``(`_node_`)` | `element`, `node` | Appends the node specified by _node_ onto the receiving node or element. |
| `string` `style` | `element` | Returns the style rules associated with an element, in string form. You can also use this to set the style rules, by calling something like `div.style.margin = "10px";` |
| `string` `innerHTML` | `element` | Returns the HTML that contains the current element and all the content within it. You can also use this to set the innerHTML of an element, by using something like `element.innerHTML = "<p>test</p>";` |
| `void` `setAttribute``(`_name_, _value_`)` | `element` | Adds (or changes) an attribute of the receiving element, such as its `id` or `align` attribute. |
| `string` `getAttribute``(`_name_`)` | `element` | Returns the value of the element attribute specified by _name_. |

The entire DOM reference can be found in [Other Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztoljrha3tcnrw).

### Using the Document Object Model

This section introduces some code examples to familiarize you with the Document Object Model.

To work with DOM code examples, you need to create a sample HTML file. The code below represents the HTML file you will use in the following examples:

1. `<html>`
2. `<head>`
3. `<title>My Sample HTML file</title>`
4. `<script language="javascript" type="text/javascript"><!--`
5. `// Insert JavaScript`
6. `// commands here.`
8. `// Do not delete this comment. -->`
9. `</script>`
10. `</head>`
11. `<body>`
12. `<div id="allMyParas" style="border-top: 1px #000 solid;">`
13. `<p id="firstParagraph">`
14. `This is my first paragraph.`
15. `</p>`
16. `<p id="secondParagraph">`
17. `This is my second paragraph.`
18. `</p>`
19. `</div>`
20. `</body>`
21. `</html>`

Now that you have an HTML document to work with, you’re ready to add some DOM transformations into the script area. This first example appends a paragraph to the DOM tree, following the `firstParagraph` and `secondParagraph` elements:

1. `var parasDiv = document.getElementById("allMyParas");`
2. `var thirdPara = document.createElement("p");`
3. `thirdPara.setAttribute("id", "thirdParagraph");`
4. `parasDiv.appendChild(thirdPara);`

Of course, the paragraph has no text in it right now. Using the DOM, you can even add text to that new paragraph:

1. `thirdPara.innerHTML = "This is my third paragraph.";`

You may also want to add a bottom margin to the enclosing `div` element, where there is currently only a top margin. You could do that with `setAttribute`, but you would have to copy the existing `style` attribute with `getAttribute`, append to it, and then send it back using `setAttribute`. Instead, use the `style` block:

1. `parasDiv.style.borderBottom = "1px #000 solid";`

Finally, maybe you want to change the style on all the paragraph elements within the enclosing `div` element. You can use the `nodeList`-generating `getElementsByTagName` method to get an array of the paragraph elements, and then cycle through them. In this example, we’ll add a gray background to all the paragraphs:

1. `var parasInDiv = parasDiv.getElementsByTagName("p");`
2. `for (var i = 0; i < parasInDiv.length; i++) {`
3. `parasInDiv[i].style.backgroundColor = "lightgrey";`
4. `}`

When you get done, the HTML effectively looks like this:

1. `<html>`
2. `<head>`
3. `<title>My Sample HTML file</title>`
4. `</head>`
5. `<body>`
6. `<div id="allMyParas" style="border-top: 1px #000 solid; border-bottom: 1px #000 solid;">`
7. `<p id="firstParagraph" style="backgroundColor: lightgrey">`
8. `This is my first paragraph.`
9. `</p>`
10. `<p id="secondParagraph" style="backgroundColor: lightgrey">`
11. `This is my second paragraph.`
12. `</p>`
13. `<p id="thirdParagraph" style="backgroundColor: lightgrey">`
14. `This is my third paragraph.`
15. `</p>`
16. `</div>`
17. `</body>`
18. `</html>`

> [!NOTE]
> 

The combination of the JavaScript Document Object Model with WebKit-based applications or Dashboard widgets is powerful. By tying these scripts to mouse events or button clicks, for example, you can create very dynamic and fluid content on your webpage or within your WebKit-based applications, including Dashboard widgets.

### Other Resources

Mozilla [Document Object Model Reference](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) is a comprehensive reference for the JavaScript DOM.

[About JavaScript and the DOM](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztclkciffeosskifea)

[Drawing Content](Canvas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztmlkciffeosskifea)
