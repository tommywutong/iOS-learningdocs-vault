---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.048.html
archived_at: '2026-07-15T07:58:52.030149Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.047.md)

# Dynamic Elements Changes

- All dynamic elements now define an __otherTagString__ attribute. Use this attribute to include a string directly in the element's HTML tag. Some HTML elements contain parameters that are not key-value pairs. If you wish to include one of these parameters in your element, you can send it using this attribute.
- Every element which supports the __displayString__ binding now has an __escapeHTML__ attribute. For the following elements, __escapeHTML__ defaults to YES:

WOBrowser
WOPopUpButton

For these following elements, __escapeHTML__ defaults to YES if you use the __displayString__ binding, and NO if you use the (now deprecated) __value__ binding:

WOCheckBoxList
WORadioButtonList
WONestedList

- Two new dynamic elements have been added to the WebObjects framework to better support JavaScript. They are called WOActionURL, which is similar to WOHyperlink; and WOResourceURL, which is similar to WOImage.
- WOPopUpButton and WOBrowser have a new __selectedValues__ attribute which passes the selected objects to a popup or browser via a list of selected values rather than a list of selected objects. The selected values come directly from the form values of the request.
- The first item in a WOPopUpButton can now be an empty selection. Bind the __noSelectionString__ attribute to a string that, if chosen, represents an empty selection. If the user leaves the WOPopUpButton at this item, then the __selection__ attribute is set to __null__ or __nil__.
- WOTextField and WOString have a new attribute, __formatter__, which should be bound to an NSFormatter instance. In the event a user enters a value that cannot be formatted, these elements will pass the invalid value through, allowing you to send back an error page that shows the invalid value. Note that the prior behavior in this case was to pass back a blank value for the field.
- The behavior of WORadioButton and WOCheckBox changed slightly so that they now push NSNumber objects with a value of 1 or 0 rather than @"1" or __nil__ (__null__ in Java) to indicate the state of the button or check box. The old behavior still applies if WebObjects 3.5 request handling is enabled (see [Troubleshooting WebObjects 4.0 Request Handling](NewInWO4.05.md#apple-giytaobr)).

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.049.md)
