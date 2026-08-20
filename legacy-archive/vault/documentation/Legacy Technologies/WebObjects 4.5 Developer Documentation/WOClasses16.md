---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WOClasses16.html
archived_at: '2026-07-15T08:06:13.711114Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses15.md)

### Request Post-Processing

After the response has been generated, but before returning the response to the adaptor, the component action request handler concludes request handling by doing the following:

- It causes the __sleep__ method-the counterpart of __awake__-to be invoked in all components involved the cycle (request, response, and subcomponents). As described in the chapter ["Managing State"](Managing%20State.md#apple-heytena), in the __sleep__ method objects can release resources that don't have to be saved between cycles.
- It requests the session object to save the response page in the page cache.
- It invokes the session object's __sleep__ method.
- It saves the session object in the session store.
- It invokes its own __sleep__ method.

When an Objective-C object is about to be destroyed, its __dealloc__ method is invoked at an undefined point in time after a cycle (indicated by the vertical ellipses in [Figure 26](WOClasses15.md#apple-gm2tqmq)). In the __dealloc__ method, the object releases any retained instance variables. In WebScript, this usually happens implicitly; you therefore usually don't need to implement the __dealloc__ method in any objects you write. In Java, objects have automatic garbage collection, so this deallocation step is unnecessary.

__Note:__  WOApplication provides two Java methods-__garbageCollectionPeriod()__ and __setGarbageCollectionPeriod()__-that allow you to get and set the amount of time between garbage collections.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](WOClasses17.md)
