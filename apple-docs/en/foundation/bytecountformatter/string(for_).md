---
title: 'string(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bytecountformatter/string(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatter/string(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatter/string%28for%3A%29.json'
content_hash: 'sha256:492a276c4f60b32b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatter](../bytecountformatter.md)

# string(for:)

<sub>Instance Method</sub>

Formats `obj` as a byte count (if `obj` is an `NSNumber`) or specific byte measurement (if `obj` is an `NSMeasurement`) using the receiver’s settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(for obj: Any?) -> String?
```

## Discussion

Returns `nil` if `obj` is not of the correct class (`NSNumber` or `NSMeasurement`). Throws an exception if `obj` is an `NSMeasurement` whose unit does not belong to the `NSUnitInformationStorage` dimension.
