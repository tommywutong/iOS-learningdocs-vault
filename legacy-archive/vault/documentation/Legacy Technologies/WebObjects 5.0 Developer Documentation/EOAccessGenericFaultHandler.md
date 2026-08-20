---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOAccessGenericFaultHandl.html
archived_at: '2026-07-15T08:13:41.151967Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOAccessGenericFaultHandler

> **__Inherits from:__**
> : EOFaultHandler

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

EOAccessGenericFaultHandler is an abstract class that helps an EOAccessFault to fire by fetching data using an EODatabaseContext. Don't use EOAccessGenericFaultHandler directly; instead, use its subclasses EOAccessFaultHandler and EOAccessArrayFaultHandler.

EOAccessGenericFaultHandler lets you chain together all the fault handlers in the access layer, so the batch faulting mechanism can find other faults related to the one that triggered the batch. Use [linkAfterHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5wgs3tlifthizlsjbqw4zdmmvza) to link one fault after another. Use [next](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5xgk6du) and [previous](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5yhezlwnfxxk4y) to traverse the chain.

## Constructors

---

### EOAccessGenericFaultHandler

`public EOAccessGenericFaultHandler()`

Description forthcoming.

---

## Instance Methods

---

### __completeInitialization__

`public abstract void completeInitializationOfObject(Object anObject)`

Description forthcoming.

---

### __databaseContext__

`public EODatabaseContext databaseContext()`

Description forthcoming.

---

### __editingContext__

`public com.webobjects.eocontrol.EOEditingContext editingContext()`

Description forthcoming.

---

### __faultWillFire__

`public void faultWillFire(Object anObject)`

Description forthcoming.

---

### generation

`public int generation()`

Returns the receiver's generation, a number that represents when the fault handler was built.

---

### linkAfterHandler

`public void linkAfterHandler( EOAccessGenericFaultHandler faultHandler, int generation)`

Adds the receiver to a chain of fault handlers, after _faultHandler_. _generation_ is a number that represents when the handler was built. All faults in an access layer can be chained together, so the batch faulting mechanism can find other faults related to the one that triggered the batch.

__See Also:__ [next](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5xgk6du), [previous](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5yhezlwnfxxk4y)

---

### next

`public EOAccessGenericFaultHandler next()`

Returns the next fault in the chain.

---

### previous

`public EOAccessGenericFaultHandler previous()`

Returns the previous fault in the chain.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
