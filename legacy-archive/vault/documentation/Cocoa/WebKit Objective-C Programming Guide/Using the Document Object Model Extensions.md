---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/DOMExtensions.html
archived_at: '2026-07-15T07:14:49.758875Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Using%20JavaScript%20From%20Objective-C.md)[Previous](Using%20the%20Document%20Object%20Model%20from%20Objective-C.md)

# Using the Document Object Model Extensions

WebKit provides extensions to the Document Object Model (DOM) that provide additional functionality not specified by the W3C recommendations. The DOM extensions are part of the DOM Objective-C API but are not part of the W3C DOM specification (and not implemented in JavaScript).

The extensions currently provide additions to `DOMHTMLElement`, `DOMDocument`, and `DOMRGBColor`. An additional `DOMHTMLElement` subclass, `DOMHTMLEmbedElement`, provides an Objective-C DOM class for HTML `embed` elements.

Among the useful features of the extensions are the inner/outer HTML and text accessor methods. Given an element block of HTML (a `DOMHTMLElement`), you can dynamically get and set the HTML and text from that block using these methods: `innerText` gets the inner content of the block without its HTML tags; `innerHTML` gets the inner content of the block (with its HTML tags, but not its enclosing tags);  `outerHTML` gets the entire content of the block. For example, given this HTML block:

```
<DIV id=”paras”>
    <P>Paragraph 1</P>
    <P>Paragraph 2</P>
</DIV>
```

The `innerHTML` method will return (as an `NSString`):

```
<P>Paragraph 1</P>
<P>Paragraph 2</P>
```

The `innerText` method will return (as an `NSString`):

```
Paragraph 1
Paragraph 2
```

And the `outerHTML` method will return (as an `NSString`):

```
<DIV id=”paras”>
    <P>Paragraph 1</P>
    <P>Paragraph 2</P>
</DIV>
```

Each of those methods has a corresponding set method (`setInnerHTML`, `setInnerText`, `setOuterHTML`) and can be used on any element cast as a `DOMHTMLElement` or any subclass of it.

The addition to the `DOMRGBColor` interface is also very useful, as it allows you to use the DOM to access the CSS Level 3 alpha channel of an RGB(A) color, even though the DOM Level 2 specification does not include it.

For a complete list of extensions provided by the Objective-C DOM API, see the `DOMExtensions.h` header file.

[Next](Using%20JavaScript%20From%20Objective-C.md)[Previous](Using%20the%20Document%20Object%20Model%20from%20Objective-C.md)

