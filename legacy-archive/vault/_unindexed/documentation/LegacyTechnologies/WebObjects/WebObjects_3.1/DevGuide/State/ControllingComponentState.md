---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/ControllingComponentState.html
archived_at: '2026-07-15T07:47:41.424231Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](SessionAwake.md)

# Controlling Component State

As mentioned previously, a WOComponent can represent a portion of a page (as with reusable components) or a complete page. State associated with the component is generally stored in the component object's instance variables and so persists for the life of the object. Component objects exist within a particular session and are stored along with the session object between each cycle of the request-response loop. Since a user can visit many pages during a session, managing component state can be crucial to reducing your application's storage requirements.

[!Table of Contents](ManagingState.book.md)
[!Next Section](CreatingComponentState.md)
