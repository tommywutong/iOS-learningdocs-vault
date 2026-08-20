---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.4b.html
archived_at: '2026-07-15T08:10:47.289132Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Other%20Binding%20Commands.md) [!](Dynamic%20and%20Static%20Inspectors.md)

---

#   Creating Form-Based Dynamic Elements

In HTML, a form is a container element (one that can contain other elements). Typically, forms contain input elements (such as text fields, radio buttons and checkboxes) to capture user information, a button or active image to submit the form data, as well as display elements such as text and images.

In WebObjects Builder, you create form elements by clicking one of the buttons in the Form Elements portion of the toolbar (or using their menu equivalents).

!

All the form elements you create in the toolbar are dynamic equivalents of standard HTML elements. You can convert any dynamic form element to its static equivalent (and vice versa) by using the Inspector (see [Dynamic and Static Inspectors](Dynamic%20and%20Static%20Inspectors.md#apple-gi3tknzu)
).

Most form elements have a __value__
attribute that represents the information entered by the user. You bind this attribute to a key so that your application can work with it. Others, such as WOSubmitButton, WOImageButton, or WOForm itself, don't receive information but have an __action__
attribute representing an action to be taken when the form is submitted. You bind form-based elements by the process described in [Binding Elements](Binding%20Elements-2.md#apple-gmztcmzq)
.

Usually you create a WOForm element to contain other form elements, including buttons. The submit and reset buttons will apply to all other elements inside the same form.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Other%20Binding%20Commands.md) [!](Dynamic%20and%20Static%20Inspectors.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
