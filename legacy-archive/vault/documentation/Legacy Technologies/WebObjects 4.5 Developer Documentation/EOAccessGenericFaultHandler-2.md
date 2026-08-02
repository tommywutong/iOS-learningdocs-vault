---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOAccessGenericFltHndlr.html
archived_at: '2026-07-15T08:11:33.306060Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOAccessGenericFaultHandler

> __Inherits
> from:__  EOFaultHandler (EOControl) : NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOAccessFault.h

---

## Class Description

---

EOAccessGenericFaultHandler is an abstract class that helps
an EOAccessFault to fire by fetching data using an EODatabaseContext.
Don't use EOAccessGenericFaultHandler directly; instead, use its subclasses [EOAccessFaultHandler](EOAccessFaultHandler-2.md#apple-ivhucy3dmvzxgrtbovwhisdbnzsgyzls) and [EOAccessArrayFaultHandler](EOAccessArrayFaultHandler-2.md#apple-ivhucy3dmvzxgqlsojqxsrtbovwhisdbnzsgyzls).

EOAccessGenericFaultHandler lets you chain together all the
fault handlers in the access layer, so the batch faulting mechanism
can find other faults related to the one that triggered the batch.
Use [linkAfter:usingGeneration:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmnrwk43ti5sw4zlsnfrumylvnr2eqylomrwgk4rpnruw422bmz2gk4r2ovzws3thi5sw4zlsmf2gs33ohi) to
link one fault after another. Use [next](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmnrwk43ti5sw4zlsnfrumylvnr2eqylomrwgk4rpnzsxq5a) and [previous](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmnrwk43ti5sw4zlsnfrumylvnr2eqylomrwgk4rpobzgk5tjn52xg) to traverse the chain.

## Instance Methods

---

### faultWillFire:

`- (void)faultWillFire:(id)aFault`

Informs the receiver that _aFault_ is
about to be reverted to its original state. EOAccessGenericFaultHandler's
implementation removes the receiver from the chain of fault handlers.
This method is invoked by EOFault's __clearFault:__ method.

---

### generation

`- (unsigned int)generation`

Returns the receiver's generation, a number
that represents when the fault handler was built.

---

### linkAfter:usingGeneration:

`- (void)linkAfter:(EOAccessGenericFaultHandler
*)faultHandler
usingGeneration:(unsigned int)generation`

Adds the receiver to a chain of fault handlers,
after _faultHandler_. _generation_ is
a number that represents when the handler was built. All faults
in an access layer can be chained together, so the batch faulting
mechanism can find other faults related to the one that triggered
the batch.

__See Also:__  [- next](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmnrwk43ti5sw4zlsnfrumylvnr2eqylomrwgk4rpnzsxq5a), [- previous](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmnrwk43ti5sw4zlsnfrumylvnr2eqylomrwgk4rpobzgk5tjn52xg)

---

### next

`- (EOAccessGenericFaultHandler *)next`

Returns the next fault in the chain.

---

### previous

`- (EOAccessGenericFaultHandler *)previous`

Returns the previous fault in the chain.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
