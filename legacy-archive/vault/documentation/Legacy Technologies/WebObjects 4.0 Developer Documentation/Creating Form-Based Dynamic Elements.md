---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements10.html
archived_at: '2026-07-18T01:25:28.186934Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Binding%20Elements-2.md)

# Creating Form-Based Dynamic Elements

In HTML, a form is a container element (one that can contain other elements). Typically, forms contain input elements (such as text fields, radio buttons and checkboxes) to capture user information, a button or active image to submit the form data, as well as display elements such as text and images.
In WebObjects Builder, you create form elements by clicking one of the buttons in the Form Elements portion of the switchable toolbar (or using their menu equivalents).

!

All the form elements you create in the toolbar are dynamic equivalents of standard HTML elements.You can convert any dynamic form element to its static equivalent (and vice versa) by using the Inspector (see ["Dynamic and Static Inspectors"](Dynamic%20and%20Static%20Inspectors.md#apple-he4tooa)).

Most form elements have a __value__ attribute that represents the information entered by the user. You bind this attribute to a variable so that your application can work with it. Others, such as WOSubmitButton, WOImageButton, or WOForm itself, don't receive information but have an __action__ attribute representing an action to be taken when the form is submitted. You bind form-based elements by the process described in ["Binding Elements"](Binding%20Elements-2.md#apple-gy2tioi).

Usually you create a WOForm element to contain other form elements, including buttons. The submit and reset buttons will apply to all other elements inside the same form.
By default, only one submit button is allowed in a single form. If you want multiple submit buttons, use the WOForm Inspector to set the __multipleSubmit__ attribute to __YES__.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Dynamic%20and%20Static%20Inspectors.md)
