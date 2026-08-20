---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState13.html
archived_at: '2026-07-15T08:05:40.556386Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState12.md)

# Controlling Session State

Maintaining state in memory on the server can consume considerable resources, so WebObjects provides a number of mechanisms to control how much state is stored. This section takes a closer look at how you manage sessionwide state.
Take care that your application only stores state for active sessions and stores the smallest amount of state possible. WOSession lets you control these factors by providing a time-out mechanism for inactive sessions and by providing a way to specify exactly what state to store between request-response loop cycles.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState14.md)
