---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bytecountformatter/string(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/string(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/string%28from%3A%29.json'
content_hash: 'sha256:ddc43eb60279217e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# string(from:)

<sub>Instance Method</sub>

Formats the value of the given measurement using the receiver’s `countStyle`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from measurement: Measurement<UnitInformationStorage>) -> String
```

## Discussion

Converts the measurement to the units allowed by the receiver’s `allowedUnits` before formatting; depending on the value of the measurement, this may result in a string which implies an approximate value (e.g. if the measurement is too large to represent in `allowedUnits`, like `1e20 YB` expressed in `NSByteCountFormatterUseBytes`).

Throws an exception if the given measurement’s unit does not belong to the `NSUnitInformationStorage` dimension.
