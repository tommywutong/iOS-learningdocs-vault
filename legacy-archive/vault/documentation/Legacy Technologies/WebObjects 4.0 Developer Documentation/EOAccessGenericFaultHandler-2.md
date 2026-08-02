---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOAccessGenericFaultHndlr.html
archived_at: '2026-07-18T01:28:15.195150Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOAccessFaultHandler-2.md)
[!](EOAdaptor-2.md)

---

# EOAccessGenericFaultHandler

__Inherits From:__
EOFaultHandler (EOControl) : NSObject

__Declared in:__
EOAccess/EOAccessFault.h

---

## Class Description

EOAccessGenericFaultHandler is an abstract class that helps an EOAccessFault to fire by fetching data using an EODatabaseContext. Don't use EOAcceessGenericFaultHandler directly; instead, use its subclasses [EOAccessFaultHandler](EOAccessFaultHandler-2.md) and [EOAccessArrayFaultHandler](EOAccessArrayFaultHandler-2.md).

EOAccessGenericFaultHandler lets you chain together all the fault handlers in the access layer, so the batch faulting mechanism can find other faults related to the one that triggered the batch. Use [`linkAfter:usingGeneration:`](#apple-guztmmy) to link one fault after another. Use [`next`](#apple-g43tsoi) and [`previous`](#apple-g43tinq) to traverse the chain.

---

## Instance Methods

---

### generation

- (unsigned int)`generation`

Returns the the receiver's generation, a number that represents when the fault handler was built.

---

### linkAfter:usingGeneration:

- (void)`linkAfter:`(EOAccessGenericFaultHandler \*)_faultHandler_
`usingGeneration:`(unsigned int)_generation_

Adds the receiver to a chain of fault handlers, after _faultHandler_. _generation_ is a number that represents when the handler was built. All faults in an access layer can be chained together, so the batch faulting mechanism can find other faults related to the one that triggered the batch.

__See also:__
[- `next`](#apple-g43tsoi), [- `previous`](#apple-g43tinq)

---

### next

- (EOAccessGenericFaultHandler \*)`next`

Returns the next fault in the chain.

---

### previous

public EOAccessGenericFaultHandler `previous`()

- (EOAccessGenericFaultHandler \*)`previous`

Returns the previous fault in the chain.

---

[!](EOAccessFaultHandler-2.md)
[!](EOAdaptor-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
