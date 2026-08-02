---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods13.html
archived_at: '2026-07-15T08:05:51.612763Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Component%20Action%20Request-Handling%20Methods.md)

## Request Handling Initialization and Post-Processing

At the beginning of each cycle of the component action request-response loop, a method named __awake__ is sent to the WOApplication, WOSession, and WOComponent objects. Like the __init__ method or constructor, the __awake__ method performs initialization tasks, but __awake__ is invoked at a different time during an object's life than the __init__ method or constructor is. The __init__ message or constructor message is sent once, when the object is first created. In contrast, __awake__ is sent at the beginning of each cycle of the request-response loop that the object is involved in. Thus, it may be sent several times during an object's life.
Complementing __awake__ is the __sleep__ method. The __sleep__ method is invoked at the end of each cycle of the component action request-response loop (in contrast to the __dealloc__ or __finalize__ methods, which are invoked at the end of the object's life). The sleep method is rarely used, but you could use it to perform any clean-up task necessary before the next request begins.

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods14.md)
