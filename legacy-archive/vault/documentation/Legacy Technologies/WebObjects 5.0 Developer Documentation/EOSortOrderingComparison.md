---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOSortOrderingComparison.html
archived_at: '2026-07-15T08:13:48.222727Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOSortOrderingComparison

> __(informal interface)__

> __Implemented by:__ : EONullValue

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The [EOSortOrderingComparison](#apple-mnxw24dbojsuizltmnsw4zdjnztv6) interface defines methods for comparing values. These methods are used for sorting value objects.

Support for these methods is provided for String, Number, and Date using EOSortOrdering.ComparisonSupport. EONullValue implements the interface directly. You should implement this interface for any value classes you write that you want to be properly sorted by EOSortOrdering instances.

## Instance Methods

---

### compareAscending

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered after the receiver, `NSComparator.OrderedDescending` if it's naturally ordered before the receiver, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

### compareCaseInsensitiveAscending

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered-ignoring case-after the receiver, `NSComparator.OrderedDescending` if it's naturally ordered before the receiver, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

### compareCaseInsensitiveDescending

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered-ignoring case-_before_ the receiver, `NSComparator.OrderedDescending` if it's naturally ordered _after_ the receiver, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

### compareDescending

Returns `NSComparator.OrderedAscending` if _anObject_ is naturally ordered before the receiver, `NSComparator.OrderedDescending` if it's naturally ordered _after_ the receiver, and `NSComparator.OrderedSame` if they're equivalent for ordering purposes.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
