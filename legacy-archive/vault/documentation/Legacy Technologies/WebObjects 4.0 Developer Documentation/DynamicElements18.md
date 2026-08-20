---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements18.html
archived_at: '2026-07-18T01:25:47.437262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DynamicElements17.md)

## Generic WebObjects

You can use the generic WebObject element to create a dynamic version of any HTML element.
To create a dynamic version of a standard HTML element:

- Create the element (say, a heading).
- In the Inspector, click Make Dynamic.

!

If the element has no specific dynamic counterpart, it becomes a generic WebObject element.

!

To create a generic WebObject corresponding to any HTML element (even ones not supported directly by WebObjects Builder):

- Click ! in the toolbar.
- Bring up the Inspector.

!

A generic WebObject element has one required attribute, __elementName__, which specifies what type of element should be generated at run time.

For example, imagine that a future version of HTML adds a new container element, which you would like to generate dynamically in your component. You would:

- Type _container name_ between the quotes in the Binding column.
- Check "Element is container".
- Use the Add Attribute button to specify any additional properties of the element.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DynamicElements19.md)
