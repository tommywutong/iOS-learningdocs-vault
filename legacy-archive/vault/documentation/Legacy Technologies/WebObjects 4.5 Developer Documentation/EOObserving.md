---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOObserving.html
archived_at: '2026-07-15T08:11:38.975827Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOObserving

> __Implemented by:__ : [EODelayedObserver](EODelayedObserver.md#apple-ivhuizlmmf4wkzcpmjzwk4twmvza)
> : EOEditingContext

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The EOObserving interface, a part of EOControl's change
tracking mechanism, declares the [objectWillChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpj5rhgzlsozuw4zzpn5rguzldorlws3dminugc3thmu) method,
used by observers to receive notifications that an object has changed.
This message is sent by EOObserverCenter to all observers registered
using its [addObserver](EOObserverCenter.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6t3consxe5tfojbwk3tumvzc6ylemrhwe43foj3gk4q) method.
For an overview of the general change tracking mechanism, see ["Tracking Enterprise Objects Changes"](The%20EOControl%20Framework.md#apple-ijeucrchivauo) in
the introduction to the EOControl Framework.

## Instance Methods

---

### objectWillChange

`public abstract void objectWillChange(Object anObject)`

Informs the receiver that _anObject_'s
state is about to change. The receiver can record _anObject_'s
state, mark or record it as changed, and examine it later (such
as at the end of the run loop) to see how it's changed.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
