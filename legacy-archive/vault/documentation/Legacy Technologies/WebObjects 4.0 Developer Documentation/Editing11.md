---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/Editing11.html
archived_at: '2026-07-18T01:26:38.646128Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Structure%20Elements.md)

## Custom Marker

Not all legal HTML elements can be created directly using WebObjects Builder's buttons or menu commands. However, you can create any type of element using the custom tag.
To create an HTML element using a custom marker:

- Place the cursor where you want the element.
- Click !.

! appears in the component window. You can replace the text "Custom Marker" with the content of the element (if any).

- In the Inspector, enter the tag's name in the Marker field.
- If the element doesn't require an end tag, uncheck "Needs end marker."
- If the element has attributes you want to specify, click New Attribute, then enter the attribute's name and value.

!

For example, if you want to create a <DL> element, you would create a custom marker and enter DL for its name in the Inspector's Marker text field. Because "Needs end marker" is checked, the </DL> end tag is inserted for you.
You can also enter source editing mode and type the marker and its text directly.
__Tip:__To save a custom element so you can use it again, save it on a palette. See ["Palettes"](Palettes.md#apple-geytcnjv).

## Removing Elements or Text From a Container

You can remove an element or text from a containing element. For example, if you've typed some text inside a form, but you decide you want the text to be _outside_ the form:

- Select the text.
- Click ! or choose Elements !Promote Selection.

This causes the text to be removed from the form.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Working%20With%20Tables.md)
