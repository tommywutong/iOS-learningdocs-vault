---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/FormBase.htm
archived_at: '2026-07-15T07:56:30.561946Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](Binding.md)

# Creating Form-Based Dynamic Elements

In HTML, a form is a container element (one that can contain other elements). Typically, forms contain input elements (such as text fields, radio buttons and checkboxes) to capture user information, a button or active image to submit the form data, as well as display elements such as text and images.
In WebObjects Builder, you create form elements by clicking one of the buttons in the Form Elements portion of the switchable toolbar (or using their menu equivalents).!
All the form elements you create in the toolbar are dynamic equivalents of standard HTML elements.You can convert any dynamic form element to its static equivalent (and vice versa) by using the Inspector (see ["Dynamic and Static Inspectors"](Inspctrs.md#apple-he4tooa)).

If you add form elements without creating a WOForm first (for example, if you add a text field to an empty page, or if you add form elements outside of the form) WebObjects Builder assumes you want to create a new form and places a <FORM> tag before and a </FORM> tag after the element.
Most form elements have a __value__ attribute that represents the information entered by the user. You bind this attribute to a variable so that your application can work with it. Others, such as WOSubmitButton, WOImageButton, or WOForm itself, don't receive information but contain an __action__ attribute representing an action to be taken when the form is submitted. You bind form-based elements by the process described in ["Binding Elements"](Binding.md#apple-gy2tioi).

__Tip:__HTML forms don't allow you to have multiple submit buttons in a single form, but the WebObjects WOForm element does. If you want multiple submit buttons in a form, bind the __multiplesubmit__ attribute of WOForm to the value YES (by typing it in the Inspector).

[!Table of Contents](DynElTOC.md) [!Next Section](Inspctrs.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
