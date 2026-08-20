---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EONullValue.html
archived_at: '2026-07-18T01:28:26.683686Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EONotQualifier.md)
[!](EOObjectStore.md)

---

# EONullValue

__Inherits From:__
Object (Java Client)
NSObject (Yellow Box)

__Implements:__
NSCoding (Java Client only)
EOSortOrderingComparison (Java Client only)
java.lang.Cloneable (Java Client only)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

The EONullValue class defines a unique object used to represent null values in collection objects (which don't allow __null__ values). For example, NSDictionaries fetched by an EOAdaptorChannel contain an EONullValue instance for such values. EONullValue is automatically translated to __null__ in enterprise objects, however, so most applications should rarely need to account for this class.

EONullValue has exactly one instance, returned by the __nullValue__ class method. t You can safely cache this instance and use the == operator to test for the presence of a null value:

> ```
> EONullValue myNull = EONullValue.nullValue();
> /* ... */
> if (value == myNull) {
>     /* ... */
> }
> ```

## Interfaces Implemented

**NSCoding (Java Client only)**

**- classForCoder

**- encodeWithCoder****

**EOSortOrderingComparison**

**[- compareAscending](EOSortOrdering.Comparison.md)

**[- compareCaseInsensitiveAscending](EOSortOrdering.Comparison.md)

**[- compareCaseInsensitiveDescending](EOSortOrdering.Comparison.md)

**[- compareDescending](EOSortOrdering.Comparison.md)********

**java.lang.Cloneable (Java Client only)**

## Constructors

---

#### EONullValue

public __EONullValue__ ()

Returns the unique instance of EONullValue.

## Static Methods

---

#### nullValue

public static EONullValue __nullValue__ ()

Returns the unique instance of EONullValue.

---

[!](EONotQualifier.md)
[!](EOObjectStore.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
