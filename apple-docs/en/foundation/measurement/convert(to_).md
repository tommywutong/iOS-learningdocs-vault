---
title: 'convert(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/convert(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/convert(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/convert%28to%3A%29.json'
content_hash: 'sha256:f63cb70e617372f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# convert(to:)

<sub>Instance Method</sub>

Converts the measurement to the specified unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func convert(to otherUnit: UnitType)
```

## Parameters

- `otherUnit` — A unit of the same `Dimension`.

## See Also

### Converting to Other Units

- [converted(to:)](<converted(to_).md>) — Returns a new measurement created by converting to the specified unit.
