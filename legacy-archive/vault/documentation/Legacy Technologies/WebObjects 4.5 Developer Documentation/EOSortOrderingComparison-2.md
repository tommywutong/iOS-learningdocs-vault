---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOSortOrderingCmprsn.html
archived_at: '2026-07-15T08:11:43.574148Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOSortOrderingComparison

> __(informal protocol)__

> __Declared in:__ : EOControl/EOSortOrdering.h

---

## Protocol Description

---

The [EOSortOrderingComparison](#apple-mnxw24dbojsuizltmnsw4zdjnztv6) informal
protocol defines methods for comparing values. These methods are
used for sorting value objects.

|  |
| --- |
| __Note:__  This interface doesn't exist in the Yellow Box package, com.apple.yellow.eocontrol |

Though declared for NSObject, most of these methods work properly
only with value classes: NSString, NSDate, NSNumber, NSDecimalNumber,
and EONull.

## Instance Methods

---

### compareAscending

Returns `NSOrderedAscending` if _anObject_ is
naturally ordered after the receiver, `NSOrderedDescending` if it's
naturally ordered before the receiver, and `NSOrderedSame` if
they're equivalent for ordering purposes. NSObject's implementation
of this method simply invokes __compare:__.

---

### compareCaseInsensitiveAscending

Returns `NSOrderedAscending` if _anObject_ is
naturally ordered-ignoring case-after the receiver, `NSOrderedDescending` if
it's naturally ordered before the receiver, and `NSOrderedSame` if
they're equivalent for ordering purposes. NSObject's implementation
of this method invokes __compare:__, while NSString's
invokes __caseInsensitiveCompare:__.

---

### compareCaseInsensitiveDescending

Returns `NSOrderedAscending` if _anObject_ is
naturally ordered-ignoring case-_before_ the
receiver, `NSOrderedDescending` if
it's naturally ordered _after_ the
receiver, and `NSOrderedSame` if
they're equivalent for ordering purposes. NSObject's implementation
of this method invokes __compare:__ and inverts
the result, while NSString's invokes __caseInsensitiveCompare:__ and
inverts the result.

---

### compareDescending

Returns `NSOrderedAscending` if _anObject_ is
naturally ordered _before_ the receiver, `NSOrderedDescending` if it's
naturally ordered _after_ the receiver,
and `NSOrderedSame` if
they're equivalent for ordering purposes. NSObject's implementation
of this method simply invokes __compare:__ and
inverts the result.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
