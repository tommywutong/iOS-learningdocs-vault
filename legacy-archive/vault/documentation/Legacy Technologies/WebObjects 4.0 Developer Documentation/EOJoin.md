---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOJoin.html
archived_at: '2026-07-18T01:28:09.989339Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOEntityClassDescription.md)
[!](EOLoginPanel.md)

---

# EOJoin

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

An EOJoin describes one source-destination attribute pair for an EORelationship. See the [EORelationship](EORelationship.md) class specification for more information and for examples.

---

## Method Types

**Constructors**

**[EOJoin](#apple-guytimy)**

**Querying the join**

**[destinationAttribute](#apple-ha2q)

**[isReciprocalToJoin](#apple-he2a)

**[sourceAttribute](#apple-he4a)******

---

## Constructors

---

### EOJoin

public `EOJoin`()

public `EOJoin`(EOAttribute _source_, EOAttribute _destination_)

Creates and returns a new EOJoin with the given source and destination attributes. See the [EORelationship](EORelationship.md) class specification for an example of creating a relationship using EOJoins.

__See also:__
[`addJoin`](EORelationship.md#apple-gm4dkoa) (EORelationship)

---

## Instance Methods

---

### destinationAttribute

public EOAttribute `destinationAttribute`()

Returns the destination ("right") attribute used by the join.

__See also:__
- `destinationAttributes` (EORelationship)

---

### isReciprocalToJoin

public boolean `isReciprocalToJoin`(EOJoin _otherJoin_)

Returns `true` if this join's source attribute is equal to _otherJoin_'s destination attribute and _otherJoin_'s source attribute is equal to this join's destination attribute. This is known as a back-referencing join.

__See also:__
[`inverseRelationship`](EORelationship.md#apple-guzdm) (EORelationship)

---

### sourceAttribute

public EOAttribute `sourceAttribute`()

Returns the source ("left") attribute used by the join.

__See also:__
[`sourceAttributes`](EORelationship.md#apple-gyzds) (EORelationship)

---

[!](EOEntityClassDescription.md)
[!](EOLoginPanel.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
