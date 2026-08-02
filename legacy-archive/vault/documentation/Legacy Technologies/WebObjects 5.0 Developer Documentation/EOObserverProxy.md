---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOObserverProxy.html
archived_at: '2026-07-15T08:13:47.176204Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOObserverProxy

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

The EOObserverProxy class is a part of EOControl's change tracking mechanism. It provides a means for objects that can't inherit from EODelayedObserver to handle subjectChanged messages. For an overview of the general change tracking mechanism, see "Tracking Enterprise Objects Changes" (page 22) in the introduction to the EOControl Framework.

An EOObserverProxy has a target object on whose behalf it observes objects. EOObserverProxy overrides subjectChanged to send an action message to its target object, allowing the target to act as though it had received subjectChanged directly from an EODelayedObserverQueue. See the EOObserverCenter and EODelayedObserverQueue class specifications for more information.

## Constructors

---

### EOObserverProxy

`public EOObserverProxy( Object anObject, NSSelector anAction, int priority)`

Creates a new EOObserverProxy to send _anAction_ to _anObject_ upon receiving a subjectChanged message. _anAction_ should be a selector for a typical action method, taking one java.util.Object argument and returning __void__. _priority_ indicates when the receiver is sent this message from EODelayedObserverQueue's notifyObserversUpToPriority method.

---

## Instance Methods

---

### priority

`public int priority()`

Description forthcoming.

---

### __subjectChanged__

`public void subjectChanged()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
