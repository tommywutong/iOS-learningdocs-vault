---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOGenericContainer.html
archived_at: '2026-07-15T07:55:25.857753Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOFrame.md)

## WOGenericContainer

### Synopsis

__WOGenericContainer__ __{__ __elementName__ = _aConstantString___;__ ... __};__

### Description

WOGenericContainer provides a way for WebObjects to accommodate custom HTML container elements, that is, elements that affect a range of text. Since the HTML language is evolving rapidly, it's convenient to have a way to dynamically generate elements which are not explicitly supported by WebObjects.
In HTML, a container element (for example, <A ... > ... </A>) has opening and closing tags that delimit the text or graphic affected by the element. In contrast, an empty element (for example <HR> or <BR>) is represented by a single tag and so can't enclose any text or graphics. (See the related element WOGenericElement for information about the support of empty elements.)

**__elementName__**
: Name of the HTML element to generate. This name (for example "TEXTAREA") will be used to generate the container's opening and closing tags (<TEXTAREA>...</TEXTAREA>).

__elementName__ must be statically defined, that is, it must be a constant. It can't be something returned by a script method, for example. Please note that for elements with URL attributes, the URLs specified will appear as is in the HTML document.
This approach works for many elements, but has one limitation. Some HTML elements have an __href__ attribute that associates the element with a URL. In WebObjects, the corresponding dynamic element generally has two mutually exclusive attributes, __href__ and __action__, which make use of the HTML element's __href__ attribute. (See WOHyperlink for an element that can have either an __href__ or an __action__ attribute.) The dynamic element's __href__ attribute simply returns a URL, but __action__ invokes a WebObjects method, which returns a URL. This overloading of the HTML __href__ attribute is not supported by WOGenericContainer. If your custom element requires this functionality, you will have to create your own subclass of WODynamicElement.

### Examples

[Support for unknown container elements](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=GenericContainerEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOGenericElement.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
