---
title: 'compare(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/compare(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/compare(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/compare%28_%3A%29.json'
content_hash: 'sha256:9700f71168ead64f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# compare(_:)

<sub>Instance Method</sub>

Indicates the temporal ordering of the receiver and another given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ other: Date) -> ComparisonResult
```

## Parameters

- `other` — The date with which to compare the receiver. This value must not be `nil`. If the value is `nil`, the behavior is undefined and may change in future versions of macOS.

## Return Value

If:

- The receiver and `anotherDate` are exactly equal to each other, [NSOrderedSame](../comparisonresult/orderedsame.md)
- The receiver is later in time than `anotherDate`, [NSOrderedDescending](../comparisonresult/ordereddescending.md)
- The receiver is earlier in time than `anotherDate`, [NSOrderedAscending](../comparisonresult/orderedascending.md).

## Discussion

This method detects sub-second differences between dates. If you want to compare dates with a less fine granularity, use [- timeIntervalSinceDate:](<timeintervalsince(__).md>) to compare the two dates.

## See Also

### Related Documentation

- [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.

### Comparing Dates

- [- isEqualToDate:](<isequal(to_).md>) — Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.
- [- earlierDate:](<earlierdate(__).md>) — Returns the earlier of the receiver and another given date.
- [- laterDate:](<laterdate(__).md>) — Returns the later of the receiver and another given date.
