---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/DynEl/ServerSide.html
archived_at: '2026-07-15T07:51:33.161878Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](DynElTOC.md)

# Server-Side Dynamic Elements

Server-side dynamic elements are the simplest type of element to create and are supported by all web browsers. Needless to say, they are the most commonly used.
Server-side dynamic elements produce HTML at runtime. This HTML is composed of the same HTML elements you use when you're creating a static web page. Like static elements, dynamic elements display formatted text, images, forms, hyperlinks, and active images. WebObjects provides several dynamic elements. For a complete list, see the online book [_Dynamic Elements Reference_](../../Reference/DynamicElements/DynamicElementsTOC.md).

For an example of dynamic elements in action, look at the CyberWind sample application. It's located in <DocRoot>__/WebObjects/Examples/Java/CyberWindJava__, where <DocRoot> is your web server's document root. When you run CyberWind, its first page contains a list of hyperlinks, shown in [Figure 9](#apple-gqzdgmi).

!Figure 9. CyberWind Main Page
This list is not hard-coded into the page. Instead, it is produced by several dynamic elements. [Figure 10](#apple-gqzdima) shows how this same part of the page looks in WebObjects Builder.

!Figure 10. CyberWind Main Page in WebObjects Builder
The elements shown in [Figure 10](#apple-gqzdima) are a WORepetition, a WOHyperlink, and a WOString. The WORepetition element corresponds to a __for__ loop in C code. That is, it iterates through a list of items and, for each item in that list, prints its contents. In this example, the contents are a WOHyperlink and a WOString. The WOHyperlink is a hyperlink whose destination is determined at runtime, and the WOString is a string whose contents are determined at runtime.

When you run CyberWind, the WORepetition walks through an array of strings that the component's code supplies. For each item in the array, it displays a hyperlink whose text is the text of the string item in the array. In this array, there are two strings-"See surfshop information" and "Buy a new sailboard"-so the WORepetition creates two hyperlinks, each containing the appropriate text.
As the name implies, server-side dynamic elements operate entirely on the server (see [Figure 11](#apple-gmydaoa)). That is, when a server-side dynamic element is asked to draw itself, it returns HTML code that should form part of a page, the page is constructed, and then the entire page is sent from the server to the client. Later in this chapter, you'll learn about client-side components, which transport values and state from the server to the client and then draw themselves on the client machine.

!Figure 11. Server-Side Dynamic Elements

[!Table of Contents](DynElTOC.md) [!Next Section](HowServerSideWork.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
