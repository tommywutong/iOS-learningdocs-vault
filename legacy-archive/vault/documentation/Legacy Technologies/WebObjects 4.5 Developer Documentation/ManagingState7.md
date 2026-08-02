---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState7.html
archived_at: '2026-07-15T08:05:48.113678Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](State%20Storage%20Strategies.md)

## A Closer Look at Storage Strategies

In a normal WebObjects application, you should set the session storage mechanism as early as possible, usually in the application object's initialization method or constructor. You set the mechanism by sending the application object a __setSessionStore:__ message. This method takes a WOSessionStore object as an argument. WOSessionStore declares the serverSessionStore method to create server session stores.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState8.md)
