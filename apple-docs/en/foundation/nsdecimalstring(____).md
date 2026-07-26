---
title: 'NSDecimalString(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalstring(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalstring(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalstring%28_%3A_%3A%29.json'
content_hash: 'sha256:207f7761072be74a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalString(_:_:)

<sub>Function</sub>

Returns a string representation of the decimal value appropriate for the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSDecimalString(_ dcm: UnsafePointer<Decimal>, _ locale: Any?) -> String
```

## Parameters

- `dcm` — The decimal value to represent.

- `locale` — Either an instance of [NSLocale](nslocale.md) or a dictionary with a string value corresponding to the [NSLocaleDecimalSeparator](nslocale/key/decimalseparator.md) key.
