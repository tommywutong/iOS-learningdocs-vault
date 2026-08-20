---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState17.html
archived_at: '2026-07-15T08:05:42.560279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](Controlling%20Component%20State.md)

## Managing Component Resources

Typically, page caching occurs both on the client machine and on the WebObjects application server. WOApplication provides methods to control caching on either end of a web connection. This section discusses server-side caching and the section "[Client-Side Page Caching](ManagingState20.md#apple-gy4tanq)" looks at the consequences of page caching on the client.

There are two common techniques for controlling component resources:

- Adjusting the page cache size
- Using __awake__ and __sleep__ to initialize and release resources

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState18.md)
