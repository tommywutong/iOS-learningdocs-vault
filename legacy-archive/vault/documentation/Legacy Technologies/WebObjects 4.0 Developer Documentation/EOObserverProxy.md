---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOObserverProxy.html
archived_at: '2026-07-18T01:28:27.069753Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOObserverCenter.md)
[!](EOOrQualifier.md)

---

# EOObserverProxy

__Inherits From:__
EODelayedObserver : Object (Java Client)
EODelayedObserver : NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

The EOObserverProxy class is a part of EOControl's change tracking mechanism. It provides a means for objects that can't inherit from EODelayedObserver to handle [__subjectChanged__](EODelayedObserver.md)messages. For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes](The%20EOControl%20Framework.md) in the introduction to the EOControl Framework.

An EOObserverProxy has a target object on whose behalf it observes objects. EOObserverProxy overrides [__subjectChanged__](EODelayedObserver.md)to send an action message to its target object, allowing the target to act as though it had received [__subjectChanged__](EODelayedObserver.md)directly from an EODelayedObserverQueue. See the [EOObserverCenter](EOObserverCenter.md) and [EODelayedObserverQueue](EODelayedObserverQueue.md) class specifications for more information.

## Constructors

---

#### EOObserverProxy

public __EOObserverProxy__ (
java.lang.Object _anObject_,
NSSelector _anAction_,
int _priority_)

Creates a new EOObserverProxy to send _anAction_ to _anObject_ upon receiving a [__subjectChanged__](EODelayedObserver.md)message. _anAction_ should be a selector for a typical action method, taking one java.util.Object argument and returning __void__ . _priority_ indicates when the receiver is sent this message from EODelayedObserverQueue's [__notifyObserversUpToPriority__](EODelayedObserverQueue.md)method.

---

[!](EOObserverCenter.md)
[!](EOOrQualifier.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
