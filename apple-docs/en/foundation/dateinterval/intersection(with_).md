---
title: 'intersection(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dateinterval/intersection(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateinterval/intersection(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateinterval/intersection%28with%3A%29.json'
content_hash: 'sha256:def5de79ad073065'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateInterval](../dateinterval.md)

# intersection(with:)

<sub>Instance Method</sub>

Returns an interval that represents the interval where the given date interval and the current instance intersect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersection(with dateInterval: DateInterval) -> DateInterval?
```

## Discussion

In the event that there is no intersection, the method returns nil.

## See Also

### Determining Intersections

- [intersects(_:)](<intersects(__).md>) — Indicates whether this interval intersects the specified interval.
