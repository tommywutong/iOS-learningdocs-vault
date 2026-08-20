---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSDisposable.html
archived_at: '2026-07-15T08:13:56.798515Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSDisposable

> __Implemented by:__ : NSDisposableRegistry: NSUndoManager

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The NSDisposable interface declares one method, [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstiruxg4dponqwe3dff5sgs43qn5zwk), in which an object prepares for destruction. In __dispose__, an object should clear all references that other objects have to it. For example, if an NSDisposable object has assigned itself as another object's delegate, the NSDisposable object should set the other object's delegate to `null` in __dispose__, thus clearing the other object's reference to the NSDisposable object. You should implement this interface if your object is a delegate for another object.

NSDisposable is needed to clean up references to objects that ought to be destroyed. As an example, consider NSNotificationCenter. When an object registers for notifications, the notification center creates a reference to that object so that it can perform the notification at the appropriate time. Unless the object removes itself as an observer of the notification, the NSNotificationCenter's reference to the object prevents the object from being garbage collected.

By implementing NSDisposable, objects are given a chance to remove references that other objects have to them. This allows other objects to send __dispose__ messages to NSDisposable objects when the NSDisposable objects are no longer needed. As an example, Direct to Java Client disposes of controllers when they're no longer needed, and subsequently, the NSDisposable controllers are garbage collected.

## Guidelines

You should implement NSDisposable if your object is a delegate for another object. If you do implement NSDisposable, you should be sure that your [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstiruxg4dponqwe3dff5sgs43qn5zwk) method will be invoked. If it won't be invoked automatically, you can add yourself to an appropriate [NSDisposableRegistry](NSDisposableRegistry.md#apple-incumq2eifdek). Known registries are provided by the com.webobjects.eoapplication classes EOController and EOArchive.

## Instance Methods

---

### dispose

`public void dispose()`

Invoked when the receiver should prepare itself for destruction. Implementations of this method should break connections that other objects have to the receiver, including unregistering for notifications, resigning as other objects' delegates, and so on.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
