---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOObserving.html
archived_at: '2026-07-18T01:28:33.123212Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOEditingContext.MessageHandler.md)
[!](EOQualifier.Comparison.md)

---

# EOObserving

__Implemented By:__
[EODelayedObserver](EODelayedObserver.md)
EOEditingContext

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Protocol Description

The EOObserving interface,a part of EOControl's change tracking mechanism, declares the __objectWillChange__ method, used by observers to receive notifications that an object has changed. This message is sent by EOObserverCenter to all observers registered using its [__addObserver__](EOObserverCenter.md)method. For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md) in the introduction to the EOControl Framework. The EOObserving interface

## Instance Methods

---

#### objectWillChange

public abstract void __objectWillChange__ (java.lang.Object _anObject_)

Informs the receiver that _anObject_'s state is about to change. The receiver can record _anObject_'s state, mark or record it as changed, and examine it later (such as at the end of the run loop) to see how it's changed.

---

[!](EOEditingContext.MessageHandler.md)
[!](EOQualifier.Comparison.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
