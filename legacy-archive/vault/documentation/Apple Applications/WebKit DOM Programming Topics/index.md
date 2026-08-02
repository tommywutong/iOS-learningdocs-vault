---
title: WebKit DOM Programming Topics
apple_id: TP40001483
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: WebKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html
archived_at: '2026-07-15T05:18:15.860269Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## About JavaScript and the DOM

JavaScript is a powerful interpreted scripting language designed to be embedded into web-based applications. You can use the JavaScript Document Object Model (DOM) in Safari and the WebKit framework to help provide dynamic content to your users, whether you are designing web content, Dashboard widgets, or Cocoa applications. Features such as dynamic typing, event handling, and JavaScript’s interface with a webpage’s Document Object Model (DOM) make JavaScript a very useful extension to HTML.

### JavaScript

JavaScript is not a compiled language; rather, it is interpreted during the parsing of an HTML page by a web client—it is not interpreted on the server side. Despite their similar names, JavaScript has no functional equivalence to the Java language; however, technologies like LiveConnect create interoperability between the two.

Scripts can be placed anywhere within an HTML file, but most commonly are placed in the `<head>` section, where the page’s title and stylesheet definitions usually reside:

1. `<head>`
2. `<title>My Page</title>`
3. `<!-- a script in another file -->`
4. `<script language="JavaScript" TYPE="text/javascript"`
5. `src="myscript.js"></script>`
7. `<!-- a script inline -->`
8. `<script language="JavaScript" TYPE="text/javascript"><!--`
10. `function myFunction() {`
11. `...`
12. `}`
13. `// -->`
14. `</script>`
15. `</head>`

The script’s content is enclosed in an HTML comment by convention. The `<script>` tag is notably the only tag in HTML whose contents are not supposed to be treated as content to display. Putting comments around these inline scripts ensures that older browsers (and non-browser tools) that do not understand the `<script>` tag do not mistake that content for ordinary text.

> [!WARNING]
> 

Apple’s WebKit framework, and the Safari web browser based on it, both support the latest versions of JavaScript. Since the support is built into the framework, you can use all the features of JavaScript within anything that uses WebKit, including Safari, Dashboard, and any WebKit-based OS X application.

### The Document Object Model (DOM)

The Document Object Model (DOM) is a standardized software interface that allows code written in JavaScript and other languages to interact with the contents of an HTML document. The Document Object Model consists of a series of classes that represent HTML elements, events, and so on, each of which contains methods that operate on those elements or events.

With the Document Object Model, you can manipulate the contents of an HTML document in any number of ways, including adding, removing, and changing content, reading and altering the contents of a form, changing CSS styles (to hide or show content, for example), and so on.

By taking advantage of the Document Object Model, you can create much more dynamic websites that adapt as the user takes actions, such as showing certain form fields depending on selections in other fields, organizing your content based on what pages the viewer has recently visited, adding dynamic navigation features such as pull-down menus, and so on.

[Using the Document Object Model](DOM.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztolkciffeosskifea)
