---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdateinterval/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdateinterval/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateinterval/isequal%28to%3A%29.json'
content_hash: 'sha256:4438a3e26218ca01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateInterval](../nsdateinterval.md)

# isEqual(to:)

<sub>Instance Method</sub>

Indicates whether the receiver is equal to the specified date interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to dateInterval: DateInterval) -> Bool
```

## Parameters

- `dateInterval` — The date interval with which to check the receiver for equality.

## Return Value

[true](../../swift/true.md) if the [startDate](startdate.md) and [duration](duration.md) of `dateInterval` and the receiver are equal. Otherwise, [false](../../swift/false.md).

## See Also

### Comparing Date Intervals

- [- compare:](<compare(__).md>) — Compares the receiver with the specified date interval.
