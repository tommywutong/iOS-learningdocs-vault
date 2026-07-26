---
title: 'addingTimeInterval(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/addingtimeinterval(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/addingtimeinterval(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/addingtimeinterval%28_%3A%29.json'
content_hash: 'sha256:f644e8d69b10c8a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# addingTimeInterval(_:)

<sub>Instance Method</sub>

Returns a new date object that is set to a given number of seconds relative to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addingTimeInterval(_ ti: TimeInterval) -> Self
```

## Parameters

- `ti` — The number of seconds to add to the receiver. Use a negative value for seconds to have the returned object specify a date before the receiver.

## Return Value

A new `NSDate` object that is set to `seconds` seconds relative to the receiver. The date returned might have a representation different from the receiver’s.

## See Also

### Related Documentation

- [- timeIntervalSinceDate:](<timeintervalsince(__).md>) — Returns the interval between the receiver and another given date.
