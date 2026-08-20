---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EODeferredFaulting.html
archived_at: '2026-07-15T08:13:47.804164Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EODeferredFaulting

> __(informal interface)__

> __Implemented by:__ : EOEnterpriseObject: EOCustomObject: EOGenericRecord

> **__Implements:__**
> : EOFaulting

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The [EODeferredFaulting](#apple-ijcuiskdirbuc) interface defines the method enterprise objects use to manage deferred faulting.

EOF uses __faults__ as stand-ins for objects whose data has not yet been fetched. Although fault creation is much faster than fetching, fault instantiation still takes time. To further improve performance, enterprise objects can use __deferred faults__ (which are more efficient).

In an object whose class enables deferred faulting, the object's relationships are initially set to deferred faults. For a particular relationship, a single deferred fault is shared between all instances of an enterprise object class. This sharing of deferred faults can significantly reduce the number of faults that need to be created, and usually reduces the overhead of fault creation during a fetch.

For example, consider a Movie class with a `studio` relationship. Without deferred faulting, during a fetch of twenty Movie objects, twenty faults are created for the `studio` relationship-one fault for each movie. With deferred faulting, only one fault is created-a deferred fault that is shared by all the movies.

## Instance Methods

---

### willReadRelationship

`public abstract Object willReadRelationship(Object object)`

Enterprise object instances that use deferred faulting invoke this method before accessing a relationship to ensure that the relationship isn't a deferred fault. EOCustomObject and EOGenericRecord's implementations check if _object_ is a deferred fault, and create and return a regular fault if it is.

For example, suppose a Movie enterprise object uses deferred faulting. Then the accessors for its relationships-`studio`, for example-should invoke __willReadRelationship__ before returning the object:

> ```
> public Studio studio() {
>     return this.willReadRelationship(studio);
> }
> ```

__See Also:__ createFaultForDeferredFault (EOFaultHandler)

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
