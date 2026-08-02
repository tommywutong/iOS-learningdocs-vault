---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EODeferredFaulting.html
archived_at: '2026-07-15T08:11:38.831530Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EODeferredFaulting

> __Implemented by:__ : EOEnterpriseObject
> : EOCustomObject
> : EOGenericRecord

> **__Implements:__**
> : EOFaulting

> **__Package:__**
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The [EODeferredFaulting](#apple-ijcuiskdirbuc) interface defines
the method enterprise objects use to manage deferred faulting.

|  |
| --- |
| __Note:__  The deferred faulting mechanism isn't available in Java Client. Although [EODeferredFaulting](#apple-ijcuiskdirbuc) is defined in com.apple.client.eocontrol, it's methods are never invoked by the Framework. |

EOF uses __faults__ as stand-ins for objects
whose data has not yet been fetched. Although fault creation is much
faster than fetching, fault instantiation still takes time. To further
improve performance, enterprise objects can use __deferred
faults__ (which are more efficient).

In an object whose class enables deferred faulting, the object's
relationships are initially set to deferred faults. For a particular
relationship, a single deferred fault is shared between all instances
of an enterprise object class. This sharing of deferred faults can
significantly reduce the number of faults that need to be created,
and usually reduces the overhead of fault creation during a fetch.

For example, consider a Movie class with a `studio` relationship.
Without deferred faulting, during a fetch of twenty Movie objects,
twenty faults are created for the `studio` relationship-one
fault for each movie. With deferred faulting, only one fault is
created-a deferred fault that is shared by all the movies.

## Instance Methods

---

### willReadRelationship

`public abstract Object willReadRelationship(Object object)`

Enterprise object instances
that use deferred faulting invoke this method before accessing a
relationship to ensure that the relationship isn't a deferred
fault. EOCustomObject and EOGenericRecord's implementations check if _object_ is
a deferred fault, and create and return a regular fault if it is.

For example, suppose a Movie enterprise object uses deferred
faulting. Then the accessors for its relationships-`studio`,
for example-should invoke `willReadRelationship` before
returning the object:

> ```
> public Studio studio() {
>     return this.willReadRelationship(studio);
> }
> ```

__See Also:__
[createFaultForDeferredFault](EOFaultHandler.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizqxk3dujbqw4zdmmvzc6y3smvqxizkgmf2wy5cgn5zeizlgmvzhezleizqxk3du) ( [EOFaultHandler](EOFaultHandler.md#apple-ivhumylvnr2eqylomrwgk4q))

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
