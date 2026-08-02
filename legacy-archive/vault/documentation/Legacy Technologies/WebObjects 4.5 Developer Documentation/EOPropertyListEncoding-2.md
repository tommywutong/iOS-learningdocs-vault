---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOPropertyListEncoding.html
archived_at: '2026-07-15T08:11:36.059280Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOPropertyListEncoding

> __Adopted by:__
> [EOAttribute](EOAttribute-3.md#apple-incuqq2ijfeue)
> [EOEntity](EOEntity-3.md#apple-irauuq2ginduu)
> [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG)
> [EOStoredProcedure](EOStoredProcedure-2.md#apple-inbuuqsdjjeei)

> __Declared in:__  EOAccess/EOModelGroup.h

## Protocol Description

---

The EOPropertyListEncoding protocol declares methods that
read and write objects to __property lists__-a
dictionary containing only property list data types (that is, NSDictionary
objects, NSStrings, NSArray objects, and NSData objects).

Classes that implement this protocol must also initialize
their instances with [initWithPropertyList:owner:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpnfxgs5cxnf2gqudsn5ygk4tupfggs43uhjxxo3tfoi5a).
Objects initialized with __initWithPropertyList:owner:__ are
initialized from the provided property list. The owner argument
is optional and should be used only by objects requiring a reference
to their owner. The newly created object isn't considered fully
functional until it receives an [awakeWithPropertyList](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpmf3wc23fk5uxi2cqojxxazlsor4uy2ltoq) message, which
finishes initializing the object. The __awakeWithPropertyList__ invocation
should be deferred until after all of the objects identified in
the property list have been created.

The method [encodeIntoPropertyList:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpmvxgg33emvew45dpkbzg64dfoj2hstdjon2du) is
responsible for encoding the receiver into a property list for later
restoration.

This protocol is used to read and write modeling objects (EOModel,
EOEntity, EOAttribute, and so on) to a model file.

## Instance Methods

---

### awakeWithPropertyList

`- (void)awakeWithPropertyList:(NSDictionary
*)propertyList`

Finishes initializing the receiver from _propertyList_,
which must have been initialized with [initWithPropertyList:owner:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2qojxxazlsor4uy2ltorcw4y3pmruw4zzpnfxgs5cxnf2gqudsn5ygk4tupfggs43uhjxxo3tfoi5a).

__awakeWithPropertyList__ is responsible
for restoring references to other objects. Consequently, it should not
be invoked until all other objects that the receiver might reference
have been initialized from _propertyList_.

---

### encodeIntoPropertyList:

`- (void)encodeIntoPropertyList:(NSMutableDictionary
*)propertyList`

Encodes the receiver as a property list.

---

### initWithPropertyList:owner:

`- initWithPropertyList:(NSDictionary
*)propertyList
owner:(id)owner`

Intializes a newly-allocated object from a property
list. _owner_ is optional, and should
be used by objects requiring a back pointer to their owner. This
method must be followed by a call to __awakeWithPropertyList__ in
order to create a fully-functional object. The call to __awakeWithPropertyList__ should
be deferred until after all other objects have been sent init messages.

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
