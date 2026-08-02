---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/GuestBook/BindingInputElements.html
archived_at: '2026-07-18T01:20:44.245426Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Previous Section](CreatingVariables.md)

## Binding the Input Elements

Each dynamic element contains several _attributes__._ These attributes determine what happens when the element is displayed or when a form element is submitted. When you bind an element, you actually bind one or more of its attributes.
For example, a WOText element (which represents a multi-line text area) is defined as having two attributes:

- __value__ specifies the string the user enters in the text area.
- __name__ specifies a unique identifier for the text area.

In this tutorial, the only attribute you are concerned with is __value__, which represents the string entered by the user in the comments field. You'll bind this to the __comments__ variable. You don't need to bind the __name__ attribute in this application. In a later example, you'll bind more than one attribute of an element.

- In the object browser, make a connection by pressing the mouse button down on the __comments__ variable and dragging to the Comments text area. Then release the mouse button.

!

The Inspector panel comes to the front, displaying the bindings for the text area. The __value__ attribute is automatically selected (since that is the one that is most commonly used in bindings). If you wanted to choose a different attribute to bind (you don't at this time), you would simply select the binding of your choice.

- Click Connect on the Inspector panel.

__comments__ appears in the Binding column next to the __value__ attribute of the text area, indicating that the binding has been made. Also, the text comments appears in the text field to show that it has been bound.

__Note:__ you can also bind a variable by typing its name directly in the Binding column for the desired attribute.

- In the same way, bind the __guestName__ and __email__ variables to the two text fields.
- Save the Main component.

[!Table of Contents](Creating%20a%20Simple%20WebObjects%20Application.md) [!Next Section](ImplementActionMethod.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
