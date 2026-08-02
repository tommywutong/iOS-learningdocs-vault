---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOJoin.html
archived_at: '2026-07-15T08:11:33.682364Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOJoin

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOJoin.h

---

## Class Description

---

An EOJoin describes one source-destination attribute pair
for an EORelationship. See the [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG) class specification
for more information and for examples.

## Method Types

---

> **Initializing new instances**
> : [- initWithSourceAttribute:destinationAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2kn5uw4l3jnzuxiv3jorufg33vojrwkqluorzgsytvorstuzdfon2gs3tboruw63sbor2he2lcov2gkoq)
>
> **Querying the join**
> : [- destinationAttribute](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2kn5uw4l3emvzxi2lomf2gs33oif2hi4tjmj2xizi)
> : [- isReciprocalToJoin:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2kn5uw4l3jonjgky3jobzg6y3bnrkg6stpnfxdu)
> : [- sourceAttribute](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2kn5uw4l3tn52xey3fif2hi4tjmj2xizi)

## Instance Methods

---

### destinationAttribute

`- (EOAttribute *)destinationAttribute`

Returns the destination ("right") attribute
used by the join.

__See Also:__  [- destinationAttributes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#//apple_ref/occ/instm/EORelationship/destinationAttributes) ( [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG))

---

### initWithSourceAttribute:destinationAttribute:

`- initWithSourceAttribute:(EOAttribute
*)source destinationAttribute:(EOAttribute
*)destination`

Initializes a newly allocated EOJoin with the
given source and destination attributes. This is the designated
initializer for the EOJoin class. Returns __self__.

See
the [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG) class specification
for an example of creating a relationship using EOJoins.

__See
Also:__  [- addJoin:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#//apple_ref/occ/instm/EORelationship/addJoin:) (EORelationship)

---

### isReciprocalToJoin:

`- (BOOL)isReciprocalToJoin:(EOJoin
*)otherJoin`

Returns YES if this join's source attribute
is equal to _otherJoin_'s destination
attribute and _otherJoin_'s source
attribute is equal to this join's destination attribute. This
is known as a back-referencing join.

__See Also:__  [- inverseRelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#//apple_ref/occ/instm/EORelationship/inverseRelationship) ( [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG))

---

### sourceAttribute

`- (EOAttribute *)sourceAttribute`

Returns the source ("left") attribute used
by the join.

__See Also:__  [- sourceAttributes](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#//apple_ref/occ/instm/EORelationship/sourceAttributes) ( [EORelationship](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#BFCDGGAG))

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
