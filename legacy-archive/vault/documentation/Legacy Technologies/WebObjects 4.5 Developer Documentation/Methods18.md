---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods18.html
archived_at: '2026-07-15T08:05:54.115536Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods17.md)

## Invoking an Action

The second phase of the component action request-response loop involves __invokeActionForRequest:inContext:__. WebObjects forwards this method from object to object until it is handled by the dynamic element associated with the user action (typically, a submit button, a hyperlink, and active image, or a form).
You rarely need to override __invokeActionForRequest:inContext:__. One reason you might do so is if you want to return a page other than the one requested. This scenario might occur if the user requests a page that has a dependency on another page that the user must fill out first. The user might, for example, finish ordering items from a catalog application and want to go to a fulfillment page but first have to supply credit card information.

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods19.md)
