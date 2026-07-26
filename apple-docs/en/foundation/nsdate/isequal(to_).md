---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/isequal%28to%3A%29.json'
content_hash: 'sha256:72c53d065186faf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to otherDate: Date) -> Bool
```

## Parameters

- `otherDate` — The date to compare with the receiver.

## Return Value

[true](../../swift/true.md) if the `otherDate` is an [NSDate](../nsdate.md) object and is exactly equal to the receiver, otherwise [false](../../swift/false.md).

## Discussion

This method detects sub-second differences between dates. If you want to compare dates with a less fine granularity, use [- timeIntervalSinceDate:](<timeintervalsince(__).md>) to compare the two dates.

## See Also

### Related Documentation

- [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.

### Comparing Dates

- [- earlierDate:](<earlierdate(__).md>) — Returns the earlier of the receiver and another given date.
- [- laterDate:](<laterdate(__).md>) — Returns the later of the receiver and another given date.
- [- compare:](<compare(__).md>) — Indicates the temporal ordering of the receiver and another given date.
