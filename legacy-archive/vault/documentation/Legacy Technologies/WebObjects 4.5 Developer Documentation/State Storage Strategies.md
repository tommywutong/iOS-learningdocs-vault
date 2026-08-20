---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState6.html
archived_at: '2026-07-15T08:05:47.611038Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState5.md)

# State Storage Strategies

WebObjects gives you the option of storing state in a couple of different ways:

- __In the server.__ State is maintained in memory within a WebObjects application.
- __In custom stores.__ State is stored using a mechanism of your own design.

By default, WebObjects uses the first approach, storing state on the server. To determine whether you should use this default approach or try one of the other state-storage solutions, read "[A Closer Look at Storage Strategies](ManagingState7.md#apple-g4ztanq)." If you decide to use another state-storage solution, you may have to set up custom objects so that they can be archived. To learn more about this issue, read ["Storing State for Custom Objects"](Storing%20State%20for%20Custom%20Objects.md#apple-guzdqoa).

An additional option when storing the state on the server is to utilize cookies for persistently storing the client's __sessionID__ and __instanceID__. This allows the client to transparently have their session restored if they leave the application and return before their session has timed out. Methods on WOSession allow for the customization of this feature. This feature will be explained in more detail below.
You may find you need to control the amount of state that is stored. The sections ["Controlling Session State"](Controlling%20Session%20State.md#apple-gm2dona) and ["Controlling Component State"](Controlling%20Component%20State.md#apple-gy3do) tell you how to do so.

[!Table of Contents](Managing%20State.md) [!Next Section](ManagingState7.md)
