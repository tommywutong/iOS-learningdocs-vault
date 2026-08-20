---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOSortOrderingComparison.html
archived_at: '2026-07-15T08:11:39.035977Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOSortOrderingComparison

> __Implemented by:__ : EONullValue

> **__Package:__**
> : com.apple.client.eocontrol

---

## Interface Description

---

The [EOSortOrderingComparison](#apple-mnxw24dbojsuizltmnsw4zdjnztv6) interface defines
methods for comparing values. These methods are used for sorting
value objects.

|  |
| --- |
| __Note:__  This interface doesn't exist in the Yellow Box package, com.apple.yellow.eocontrol |

Support for these methods is provided for String, Number,
and Date using [EOSortOrdering.ComparisonSupport](EOSortOrdering.ComparisonSupport.md#apple-ivhuwzlzkzqwy5lfinxwi2lom4xfg5lqobxxe5a).
EONullValue implements the interface directly. You should implement
this interface for any value classes you write that you want to
be properly sorted by EOSortOrdering instances.

## Instance Methods

---

### compareAscending

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered after the receiver, `NSComparator.OrderedDescending` if
it's naturally ordered before the receiver, and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

### compareCaseInsensitiveAscending

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered-ignoring case-after the receiver, `NSComparator.OrderedDescending` if
it's naturally ordered before the receiver, and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

### compareCaseInsensitiveDescending

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered-ignoring case- _before_ the receiver, `NSComparator.OrderedDescending` if
it's naturally ordered _after_ the
receiver, and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

### compareDescending

Returns `NSComparator.OrderedAscending` if _anObject_ is
naturally ordered _before_ the receiver, `NSComparator.OrderedDescending` if
it's naturally ordered _after_ the
receiver, and `NSComparator.OrderedSame` if
they're equivalent for ordering purposes.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
