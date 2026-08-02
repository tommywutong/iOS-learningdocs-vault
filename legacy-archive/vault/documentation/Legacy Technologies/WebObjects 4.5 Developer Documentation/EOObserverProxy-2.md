---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObserverProxy.html
archived_at: '2026-07-15T08:11:39.952475Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOObserverProxy

> **__Inherits
> from:__**
> : [EODelayedObserver](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5cgk3dbpfswit3consxe5tfoi) : NSObject

> **__Conforms to:__**
> : [EOObserving](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOObserving.html#//apple_ref/occ/intf/EOObserving)
> : (EODelayedObserver)
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOObserver.h

---

## Class Description

---

The EOObserverProxy class is a part of EOControl's change
tracking mechanism. It provides a means for objects that can't
inherit from EODelayedObserver to handle [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) messages. For an overview
of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework-2.md#apple-ijeucrchivauo) in the introduction to
the EOControl Framework.

An EOObserverProxy has a target object on whose behalf it
observes objects. EOObserverProxy overrides [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) to send an action
message to its target object, allowing the target to act as though
it had received [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) directly from an EODelayedObserverQueue.
See the [EOObserverCenter](EOObserverCenter-2.md#apple-ivhu6yttmvzhmzlsinsw45dfoi) and [EODelayedObserverQueue](EODelayedObserverQueue-3.md#apple-ivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovsq) class
specifications for more information.

## Instance Methods

---

### initWithTarget:action:priority:

`- (id)initWithTarget:(id)anObject
action:(SEL)anAction
priority:(EOObserverPriority)priority`

Initializes a new EOObserverProxy to send anAction
to _anObject_ upon receiving a [subjectChanged](EODelayedObserver-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4rpon2we2tfmn2eg2dbnztwkza) message. _anAction_ should
be a selector for a typical action method, taking one `id` argument
and returning `void`. _priority_ indicates
when the receiver is sent this message from EODelayedObserverQueue's [notifyObserversUpToPriority:](EODelayedObserverQueue-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emvwgc6lfmrhwe43foj3gk4srovsxkzjpnzxxi2lgpfhwe43foj3gk4ttkvyfi32qojuw64tjor4tu) method.
This is the designated initializer for the EOObserverProxy class.
Returns `self`.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
