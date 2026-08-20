---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/Attribut.htm
archived_at: '2026-07-15T07:56:10.765249Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](DEIntro.md)

# Attributes

Every dynamic element has one or more attributes. These attributes are used for several purposes:

- Some attributes are used to determine the exact HTML to be generated when the element is displayed.

  For example, the __value__ attribute of a dynamic string element (WOString) determines what text is generated in its place. At run time, WebObjects replaces the WOString with the value of the variable or method that is bound to it.
- Other attributes are used to capture information provided by users. In particular, form elements are used for this purpose.

  For example, when the user submits a form, text typed by the user into a dynamic text area (WOText) inside the form is assigned to the variable bound to the __value__ attribute of the text area.
- Other attributes are used to specify actions to be taken when an event occurs.

For example, a dynamic hyperlink (WOHyperlink) has an __action__ attribute that specifies an _action method_ in the application that is executed when the user clicks the link.

The process of associating an attribute with a variable or method in your code is called _binding_. WebObjects Builder provides tools to make it easy for you to create bindings. Information about your bindings is stored in the declarations (__.wod__) file in your component.
Most dynamic elements have a number of attributes that you can bind. Some are required and others are optional. For complete information about WebObjects' dynamic elements and their attributes, see _[Dynamic Elements Reference.](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/Reference/DynamicElements/DynamicElementsTOC.html)_

[!Table of Contents](DynElTOC.md) [!Next Section](CreateDE.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
