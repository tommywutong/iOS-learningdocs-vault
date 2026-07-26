---
title: 'converted(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/converted(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/converted(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/converted%28to%3A%29.json'
content_hash: 'sha256:4bfab9c5aa549df3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# converted(to:)

<sub>Instance Method</sub>

Returns a new measurement created by converting to the specified unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func converted(to otherUnit: UnitType) -> Measurement<UnitType>
```

## Parameters

- `otherUnit` — A unit of the same `Dimension`.

## Return Value

A converted measurement.

## See Also

### Converting to Other Units

- [convert(to:)](<convert(to_).md>) — Converts the measurement to the specified unit.
