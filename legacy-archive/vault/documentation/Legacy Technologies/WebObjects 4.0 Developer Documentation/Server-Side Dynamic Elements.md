---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements1.html
archived_at: '2026-07-18T01:20:05.345742Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](Dynamic%20Elements.md)

# Server-Side Dynamic Elements

Server-side dynamic elements are the simplest type of element to create and are supported by all web browsers. Needless to say, they are the most commonly used.
Server-side dynamic elements produce HTML at run-time. This HTML is composed of the same HTML elements you use when you're creating a static web page. Like static elements, dynamic elements display formatted text, images, forms, hyperlinks, and active images. WebObjects provides several dynamic elements. For a complete list, see the online book [_Dynamic Elements Reference_](Dynamic%20Element%20Specifications.md).

For an example of dynamic elements in action, consider an application whose first page contains a list of user choices of actions to perform. This page is shown in [Figure 9](#apple-gqzdgmi).

!

Figure 9. Main Page

This list could be hard-coded into an HTML page, but it is more extensible if it the list is produced using dynamic elements in a component. (Because this is the first component in the application, it is called Main.) [Figure 10](#apple-gqzdima) shows how this same part of the page looks in WebObjects Builder.

!

Figure 10. Main Page in WebObjects Builder

The elements shown in [Figure 10](#apple-gqzdima) are a WORepetition, a WOHyperlink, and a WOString. The WORepetition element corresponds to a __for__ loop in C code. That is, it iterates through a list of items and, for each item in that list, prints its contents. In this example, the contents are a WOHyperlink and a WOString. The WOHyperlink is a hyperlink whose destination is determined at run-time, and the WOString is a string whose contents are determined at run-time.

When you run the application, the WORepetition walks through an array of strings that the component's code supplies. For each item in the array, it displays a hyperlink whose text is the text of the string item in the array. In this array, there are two strings-"See surfshop information" and "Buy a new sailboard"-so the WORepetition creates two hyperlinks, each containing the appropriate text.
As the name implies, server-side dynamic elements operate entirely on the server (see [Figure 11](#apple-gmydaoa)). That is, when a server-side dynamic element is asked to draw itself, it produces HTML code that should form part of a page, the page is constructed, and then the entire page is sent from the server to the client. Later in this chapter, you'll learn about client-side components, which transport values and state from the server to the client and then draw themselves on the client machine.

!

Figure 11. Server-Side Dynamic Elements

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
