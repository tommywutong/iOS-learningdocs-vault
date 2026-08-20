---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOObserving.html
archived_at: '2026-07-15T08:13:48.146978Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOObserving

> __Implemented by:__ EODelayedObserverEOEditingContext

> __Package:__ com.webobjects.eocontrol

---

## Interface Description

---

The EOObserving interface, a part of EOControl's change tracking mechanism, declares the [objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) method, used by observers to receive notifications that an object has changed. This message is sent by EOObserverCenter to all observers registered using its addObserver method. For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes" (page 22)](The%20EOControl%20Framework.md#apple-ijeucrchivauo) in the introduction to the EOControl Framework.

## Instance Methods

---

### objectWillChange

`public abstract void objectWillChange(Object anObject)`

Informs the receiver that _anObject_'s state is about to change. The receiver can record _anObject_'s state, mark or record it as changed, and examine it later (such as at the end of the run loop) to see how it's changed.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
