---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/Subcomponents.html
archived_at: '2026-07-15T07:47:00.217375Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](Associations.md)

# __Subcomponents and Component References__

A "node" in a template's object graph can represent a subcomponent (also called "reusable component") as well as a dynamic or static HTML element. A dynamic element called a _component reference_ represents all occurrences of the subcomponent in the parent component. At run time, the component reference binds itself to the separate instances.

A subcomponent can fire actions against its parent component (using __performParentAction:__) and, if the parent's state changes, it's state is synchronized accordingly. In other words, its state is updated to reflected changes based upon its bindings with the parent.

An element ID is assigned to each instance of a subcomponent. When the chain of request-handling messages goes down an object graph and reaches the component reference, it resolves references to its instances based on the element ID of each instance. Components keep track of all their subcomponents by storing them in an internal dictionary using element IDs as keys.

!

Figure 7: An Object Graph for a Page With a Subcomponent
