---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOJoin.html
archived_at: '2026-07-15T08:11:31.839038Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOJoin

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

An EOJoin describes one source-destination attribute pair
for an EORelationship. See the [EORelationship](EORelationship.md#apple-ijdegrchi5auo) class specification
for more information and for examples.

## Method Types

---

> **Constructors**
> : [EOJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rpivhuu33jny)
>
> **Querying the join**
> : [destinationAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rpmrsxg5djnzqxi2lpnzaxi5dsnfrhk5df)
> : [isReciprocalToJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rpnfzvezldnfyhe33dmfwfi32kn5uw4)
> : [sourceAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rponxxk4tdmvaxi5dsnfrhk5df)

## Constructors

---

### EOJoin

`public EOJoin(
EOAttribute source,
EOAttribute destination)`

Creates and returns a new EOJoin with the given
source and destination attributes. See the [EORelationship](EORelationship.md#apple-ijdegrchi5auo) class specification
for an example of creating a relationship using EOJoins.

__See
Also:__  [addJoin](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6ylemrfg62lo) (EORelationship)

---

## Instance Methods

---

### destinationAttribute

`public EOAttribute destinationAttribute()`

Returns the destination ("right") attribute
used by the join.

__See Also:__  [destinationAttributes](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfon2gs3tboruw63sbor2he2lcov2gk4y) ( [EORelationship](EORelationship.md#apple-ijdegrchi5auo))

---

### isReciprocalToJoin

`public boolean isReciprocalToJoin(EOJoin otherJoin)`

Returns true if this join's source attribute
is equal to _otherJoin_'s destination
attribute and _otherJoin_'s source
attribute is equal to this join's destination attribute. This
is known as a back-referencing join.

__See Also:__  [inverseRelationship](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc62loozsxe43fkjswyylunfxw443infya) ( [EORelationship](EORelationship.md#apple-ijdegrchi5auo))

---

### sourceAttribute

`public EOAttribute sourceAttribute()`

Returns the source ("left") attribute used
by the join.

__See Also:__  [sourceAttributes](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc643povzggzkbor2he2lcov2gk4y) ( [EORelationship](EORelationship.md#apple-ijdegrchi5auo))

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
