---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOJoin.html
archived_at: '2026-07-18T01:28:16.660759Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOGenericRecord%20Additions.md)
[!](EOLoginPanel-2.md)

---

# EOJoin

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EOJoin.h

---

## Class Description

An EOJoin describes one source-destination attribute pair for an EORelationship. See the [EORelationship](EORelationship-2.md) class specification for more information and for examples.

---

## Method Types

**Initializing new instances**

**[- initWithSourceAttribute:destinationAttribute:](#apple-guzdsmi)**

**Querying the join**

**[- destinationAttribute](#apple-ha2q)

**[- isReciprocalToJoin:](#apple-he2a)

**[- sourceAttribute](#apple-he4a)******

---

## Instance Methods

---

### destinationAttribute

- (EOAttribute \*)`destinationAttribute`

Returns the destination ("right") attribute used by the join.

__See also:__
- `destinationAttributes` (EORelationship)

---

### initWithSourceAttribute:destinationAttribute:

- `initWithSourceAttribute:`(EOAttribute \*)_source_ `destinationAttribute:`(EOAttribute \*)_destination_

Initializes a newly allocated EOJoin with the given source and destination attributes. This is the designated initializer for the EOJoin class. Returns `self`.

See the [EORelationship](EORelationship-2.md) class specification for an example of creating a relationship using EOJoins.

__See also:__
[- `addJoin:`](EORelationship.md#apple-gm4dkoa) (EORelationship)

---

### isReciprocalToJoin:

- (BOOL)`isReciprocalToJoin:`(EOJoin \*)_otherJoin_

Returns YES if this join's source attribute is equal to _otherJoin_'s destination attribute and _otherJoin_'s source attribute is equal to this join's destination attribute. This is known as a back-referencing join.

__See also:__
[- `inverseRelationship`](EORelationship.md#apple-guzdm) (EORelationship)

---

### sourceAttribute

- (EOAttribute \*)`sourceAttribute`

Returns the source ("left") attribute used by the join.

__See also:__
[- `sourceAttributes`](EORelationship.md#apple-gyzds) (EORelationship)

---

[!](EOGenericRecord%20Additions.md)
[!](EOLoginPanel-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
