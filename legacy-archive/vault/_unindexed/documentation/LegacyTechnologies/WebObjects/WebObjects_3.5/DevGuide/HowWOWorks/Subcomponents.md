---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/Subcomponents.html
archived_at: '2026-07-15T07:51:55.297352Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](ClientSideAssociations.md)

## Subcomponents and Component References

A "node" in a template's object graph can represent a _subcomponent_ (also called a reusable component) as well as a dynamic or static HTML element. A dynamic element called a _component reference_ represents all occurrences of the subcomponent in the parent component. At runtime, the component reference binds itself to the separate instances. [Figure 26](#apple-ge2to) is an example of an object graph for a page with a subcomponent.

A subcomponent can fire actions against its parent component (using __performParentAction:__), and if the parent's state changes, its state is synchronized accordingly. In other words, its state is updated to reflect changes according to its bindings with the parent.
An element ID is assigned to each instance of a subcomponent. When the chain of request-handling messages traverses an object graph and reaches the component reference, it resolves references to its instances according to the element ID of each instance. Components keep track of all their subcomponents by storing them in an internal dictionary using element IDs as keys.!Figure 26. An Object Graph for a Page With a Subcomponent

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
