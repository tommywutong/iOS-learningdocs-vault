---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOObserverProxy.html
archived_at: '2026-07-18T01:28:37.080496Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOObserverCenter-2.md)
[!](EOOrQualifier-2.md)

---

# EOObserverProxy

__Inherits From:__
EODelayedObserver : NSObject

__Conforms To:__ EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__ EOControl/EOObserver.h

The EOObserverProxy class is a part of EOControl's change tracking mechanism. It provides a means for objects that can't inherit from EODelayedObserver to handle [__subjectChanged__](EODelayedObserver-3.md)messages. For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework-2.md) in the introduction to the EOControl Framework.

An EOObserverProxy has a target object on whose behalf it observes objects. EOObserverProxy overrides [__subjectChanged__](EODelayedObserver-3.md)to send an action message to its target object, allowing the target to act as though it had received [__subjectChanged__](EODelayedObserver-3.md)directly from an EODelayedObserverQueue. See the [EOObserverCenter](EOObserverCenter-2.md) and [EODelayedObserverQueue](EODelayedObserverQueue-3.md) class specifications for more information.

---

#### initWithTarget:action:priority:

- (id)__initWithTarget:__ (id)_anObject___action:__ (SEL)_anAction___priority:__ (EOObserverPriority)_priority_

Initializes a new EOObserverProxy to send _anAction_ to _anObject_ upon receiving a [__subjectChanged__](EODelayedObserver-3.md)message. _anAction_ should be a selector for a typical action method, taking one __id__ argument and returning __void__ . _priority_ indicates when the receiver is sent this message from EODelayedObserverQueue's [__notifyObserversUpToPriority:__](EODelayedObserverQueue-3.md)method. This is the designated initializer for the EOObserverProxy class. Returns __self__ .

---

[!](EOObserverCenter-2.md)
[!](EOOrQualifier-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
