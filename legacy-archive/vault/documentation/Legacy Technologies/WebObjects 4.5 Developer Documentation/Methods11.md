---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods11.html
archived_at: '2026-07-15T08:05:50.666517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods10.md)

## WODirectAction Initialization

Unlike applications, components, and sessions, WODirectAction objects do not persist between cycles of the request-response loop. A WODirectAction object is initialized at the beginning of a direct action request-response loop cycle and is released or marked for garbage collection at the end of the cycle. The designated initializer for WODirectAction is __initWithRequest:__. In Java, the constructor must take a WORequest argument, for example:

```
public DirectAction(WORequest) { ... }
```


In the __initWithRequest:__ method (or constructor), you perform anything that should happen before the WODirectAction performs any of the actions that it declares.

[!Table of Contents](Common%20Methods.md) [!Next Section](Component%20Action%20Request-Handling%20Methods.md)
