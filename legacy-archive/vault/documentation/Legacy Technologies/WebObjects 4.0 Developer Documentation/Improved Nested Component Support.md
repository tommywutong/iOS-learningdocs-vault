---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.032.html
archived_at: '2026-07-15T07:58:41.067169Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.031.md)

# Improved Nested Component Support

In WebObjects 4.0, support for nested, reusable components has been improved in these ways:

- Template parsing improvements make HTML generation for components faster. Thus, you'll see only a small performance loss by using a component instead of a dynamic element.
- You can now create a nested component that serves as an HTML container element, one that wraps other HTML and text inside of it (similar to the way a WORepetition wraps other HTML elements).
- You can turn off component synchronization, in which values are pulled from the parent component and pushed to the parent component before and after each phase of the request-response loop, and perform synchronization manually. When you perform synchronization manually, components are more predictable and behave more like dynamic elements.
- It's now easier to use components to mimic and customize the behavior of dynamic elements. Because of the performance improvements and the ability to define non-synchronized components, you shouldn't find it necessary to have to write a subclass of WODynamicElement.
- WOComponent now has a __parent__ method that returns the receiver's parent WOComponent.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.033.md)
