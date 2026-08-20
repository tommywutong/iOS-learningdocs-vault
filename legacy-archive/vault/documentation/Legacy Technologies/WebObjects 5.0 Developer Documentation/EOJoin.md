---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOJoin.html
archived_at: '2026-07-15T08:13:41.593109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOJoin

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

An EOJoin describes one source-destination attribute pair for an EORelationship. See the EORelationship class specification for more information and for examples.

## Method Types

---

> **Constructors**
> : [EOJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rpivhuu33jny)
>
> **Querying the join**
> : [destinationAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rpmrsxg5djnzqxi2lpnzaxi5dsnfrhk5df): [isReciprocalToJoin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rpnfzvezldnfyhe33dmfwfi32kn5uw4): [sourceAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjjxws3rponxxk4tdmvaxi5dsnfrhk5df)

## Constructors

---

### EOJoin

`public EOJoin( EOAttribute source, EOAttribute destination)`

Creates and returns a new EOJoin with the given source and destination attributes. See the EORelationship class specification for an example of creating a relationship using EOJoins.

__See Also:__ addJoin (EORelationship)

---

## Instance Methods

---

### __clone__

`public Object clone()`

Description forthcoming.

---

### destinationAttribute

`public EOAttribute destinationAttribute()`

Returns the destination ("right") attribute used by the join.

__See Also:__ destinationAttributes (EORelationship)

---

### __equals__

`public boolean equals(Object anObject)`

Description forthcoming.

---

### isReciprocalToJoin

`public boolean isReciprocalToJoin(EOJoin otherJoin)`

Returns `true` if this join's source attribute is equal to _otherJoin_'s destination attribute and _otherJoin_'s source attribute is equal to this join's destination attribute. This is known as a back-referencing join.

__See Also:__ inverseRelationship (EORelationship)

---

### sourceAttribute

`public EOAttribute sourceAttribute()`

Returns the source ("left") attribute used by the join.

__See Also:__ sourceAttributes (EORelationship)

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
