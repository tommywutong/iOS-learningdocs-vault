---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOObserverProxy.html
archived_at: '2026-07-15T08:11:37.868859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOObserverProxy

> **__Inherits
> from:__**
> : [(com.apple.client.eocontrol) EODelayedObserver](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuizlmmf4wkzcpmjzwk4twmvza) : Object
> (com.apple.yellow.eocontrol) EODelayedObserver : NSObject

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

The EOObserverProxy class is a part of EOControl's change
tracking mechanism. It provides a means for objects that can't
inherit from EODelayedObserver to handle [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) messages. For an overview
of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md#apple-ijeucrchivauo) in the introduction
to the EOControl Framework.

An EOObserverProxy has a target object on whose behalf it
observes objects. EOObserverProxy overrides [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) to send an action
message to its target object, allowing the target to act as though
it had received [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) directly from an EODelayedObserverQueue.
See the [EOObserverCenter](EOObserverCenter.md#apple-ivhu6yttmvzhmzlsinsw45dfoi) and [EODelayedObserverQueue](EODelayedObserverQueue.md#apple-ivhuizlmmf4wkzcpmjzwk4twmvzfc5lfovsq) class
specifications for more information.

## Constructors

---

### EOObserverProxy

`public EOObserverProxy(
Object anObject,
NSSelector anAction,
int priority)`

Creates a new EOObserverProxy to send _anAction_ to _anObject_ upon
receiving a [subjectChanged](EODelayedObserver.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlsf5zxkytkmvrxiq3imfxgozle) message. _anAction_ should
be a selector for a typical action method, taking one java.util.Object
argument and returning `void`. _priority_ indicates
when the receiver is sent this message from EODelayedObserverQueue's [notifyObserversUpToPriority](EODelayedObserverQueue.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpirswyylzmvse6yttmvzhmzlskf2wk5lff5xg65djmz4u6yttmvzhmzlsonkxavdpkbzgs33snf2hs) method.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
