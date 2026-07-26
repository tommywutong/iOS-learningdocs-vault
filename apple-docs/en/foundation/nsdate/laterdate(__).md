---
title: 'laterDate(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/laterdate(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/laterdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/laterdate%28_%3A%29.json'
content_hash: 'sha256:68e96e86a82746ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# laterDate(_:)

<sub>Instance Method</sub>

Returns the later of the receiver and another given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func laterDate(_ anotherDate: Date) -> Date
```

## Parameters

- `anotherDate` — The date with which to compare the receiver.

## Return Value

The later of the receiver and `anotherDate`, determined using [- timeIntervalSinceDate:](<timeintervalsince(__).md>). If the receiver and `anotherDate` represent the same date, returns the receiver.

## See Also

### Related Documentation

- [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.

### Comparing Dates

- [- isEqualToDate:](<isequal(to_).md>) — Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.
- [- earlierDate:](<earlierdate(__).md>) — Returns the earlier of the receiver and another given date.
- [- compare:](<compare(__).md>) — Indicates the temporal ordering of the receiver and another given date.
