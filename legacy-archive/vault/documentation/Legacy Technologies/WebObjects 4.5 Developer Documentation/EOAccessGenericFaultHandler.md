---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOAccessGenericFltHndlr.html
archived_at: '2026-07-15T08:11:31.474082Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAccessGenericFaultHandler

> __Inherits
> from:__  EOFaultHandler (EOControl) : NSObject

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

EOAccessGenericFaultHandler is an abstract class that helps
an EOAccessFault to fire by fetching data using an EODatabaseContext.
Don't use EOAccessGenericFaultHandler directly; instead, use its subclasses [EOAccessFaultHandler](EOAccessFaultHandler.md#apple-ivhucy3dmvzxgrtbovwhisdbnzsgyzls) and [EOAccessArrayFaultHandler](EOAccessArrayFaultHandler.md#apple-ivhucy3dmvzxgqlsojqxsrtbovwhisdbnzsgyzls).

EOAccessGenericFaultHandler lets you chain together all the
fault handlers in the access layer, so the batch faulting mechanism
can find other faults related to the one that triggered the batch.
Use [linkAfterHandler](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5wgs3tlifthizlsjbqw4zdmmvza) to
link one fault after another. Use [next](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5xgk6du) and [previous](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5yhezlwnfxxk4y) to traverse the chain.

## Instance Methods

---

### generation

`public int generation()`

Returns the receiver's generation, a number
that represents when the fault handler was built.

---

### linkAfterHandler

`public void linkAfterHandler(
EOAccessGenericFaultHandler faultHandler,
int generation)`

Adds the receiver to a chain of fault handlers,
after _faultHandler_. _generation_ is
a number that represents when the handler was built. All faults
in an access layer can be chained together, so the batch faulting
mechanism can find other faults related to the one that triggered
the batch.

__See Also:__  [next](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5xgk6du), [previous](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifrwgzltondwk3tfojuwgrtbovwhisdbnzsgyzlsf5yhezlwnfxxk4y)

---

### next

`public EOAccessGenericFaultHandler next()`

Returns the next fault in the chain.

---

### previous

`public EOAccessGenericFaultHandler previous()`

Returns the previous fault in the chain.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
