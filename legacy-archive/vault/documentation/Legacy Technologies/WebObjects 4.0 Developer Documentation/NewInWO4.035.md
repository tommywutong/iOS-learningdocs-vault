---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.035.html
archived_at: '2026-07-15T07:58:42.704743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.034.md)

## Components That Mimic Dynamic Elements

It's common to want to be able to subclass a particular dynamic element to provide behavior specific to your application. Creating a true subclass of a particular dynamic element can be a difficult task. In WebObjects 4.0, however, you can do this much more easily. Instead of subclassing the dynamic element class, you write a reusable component that mimics the behavior of the dynamic element and provides your own custom behavior.
To learn how to write components that mimic dynamic elements, see the MinimalPrimitivesTest example application. You can use this example application as a starting point for writing your own components.
The MinimalPrimitivesTest example uses some new WOGenericElement and WOGenericContainer attributes that make it easy to use these two elements to define other dynamic elements. The new attributes on WOGenericElement and WOGenericContainer are listed below:

|  WOGenericElement and WOGenericContainer Attributes |  |
|  Attribute |  Description |
|  elementName |  The name of the HTML element you want to create. This attribute isn't new, but it has some changes. It is now optional. You can now bind this attribute to a variable instead of a constant string. You can also set the value of this attribute to __nil__ or __null__, which effectively shuts this element off (that is, WebObjects doesn't generate HTML tags for this element). |
|  formValue |  Bind this attribute to a variable that should contain the component's input value. If this attribute is specified, WebObjects extracts the form value with the key matching this component's element ID from the request and assigns it to the variable bound to this attribute. If the request has no form value for this element, the variable isn't set. |
|  formValues |  Same as __formValue__, but should be bound to an array variable. Use this attribute if the element should receive more than one input value. (For example, a WOBrowser with multiple selections enabled could receive more than one input value.) |
|  invokeAction |  The action to be invoked. Use this attribute to simulate elements like WOHyperlink, WOSubmitButton, and so on, that define an action. |
|  omitTags |  If __YES__, WebObjects doesn't generate HTML tags for this element. This attribute allows you to define an element that conditionally wraps HTML in a container tag. For example, if the __elementName__ attribute is bound to the string "B" and the __omitTags__ attribute is bound to a boolean variable, you can use that boolean variable to set whether this element generates the bold tag or not. (The body contained in the element is generated regardless of this setting.) |
|  elementID |  Bind this attribute to a variable if you want to obtain programmatic access to the element ID for this element. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Improved%20Image%20Loading.md)
