---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses22.html
archived_at: '2026-07-15T08:06:18.683838Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses21.md)

## Subcomponents and Component References

A "node" in a template's object graph can represent a _subcomponent_ (also called a reusable component) as well as a dynamic or static HTML element. A dynamic element called a _component reference_ represents all occurrences of the subcomponent in the parent component. At run-time, the component reference binds itself to the separate instances. [Figure 30](#apple-ge2to) is an example of an object graph for a page with a subcomponent.

A subcomponent can fire actions against its parent component (using __performParentAction:__), and if the parent's state changes, its state is synchronized accordingly. In other words, its state is updated to reflect changes according to its bindings with the parent.
An element ID is assigned to each instance of a subcomponent. When a request-handling message traverses an object graph and reaches the component reference, it resolves references to its instances according to the element ID of each instance.

!

Figure 30. An Object Graph for a Page With a Subcomponent

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](Creating%20Reusable%20Components.md)
