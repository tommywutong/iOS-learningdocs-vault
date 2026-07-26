---
title: 'intersects(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdateinterval/intersects(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdateinterval/intersects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateinterval/intersects%28_%3A%29.json'
content_hash: 'sha256:f44e6a06812f28d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDateInterval](../nsdateinterval.md)

# intersects(_:)

<sub>Instance Method</sub>

Indicates whether the receiver intersects with the specified date interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersects(_ dateInterval: DateInterval) -> Bool
```

## Parameters

- `dateInterval` — The date interval with which to check the receiver for intersection.

## Discussion

See [- intersectionWithDateInterval:](<intersection(with_).md>) for more information about determining whether two date intervals intersect.

## See Also

### Determining Intersections

- [- intersectionWithDateInterval:](<intersection(with_).md>) — Returns the intersection between the receiver and the specified date interval.
