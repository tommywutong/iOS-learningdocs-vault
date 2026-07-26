---
title: 'contains(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdateinterval/contains(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdateinterval/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateinterval/contains%28_%3A%29.json'
content_hash: 'sha256:055eeedfbd064bee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateInterval](../nsdateinterval.md)

# contains(_:)

<sub>Instance Method</sub>

Indicates whether the receiver contains the specified date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ date: Date) -> Bool
```

## Parameters

- `date` — The date for which to test membership of the date interval.

## Return Value

[true](../../swift/true.md) if the receiver contains `date`. Otherwise, [false](../../swift/false.md).
