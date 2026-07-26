---
title: 'getBytes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuuid/getbytes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuuid/getbytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuuid/getbytes%28_%3A%29.json'
content_hash: 'sha256:00e750c037c1ee76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUUID](../nsuuid.md)

# getBytes(_:)

<sub>Instance Method</sub>

Returns the UUID as bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getBytes(_ uuid: UnsafeMutablePointer<UInt8>)
```

## Parameters

- `uuid` — The value of uuid represented as raw bytes.

## See Also

### Get UUID Values

- [UUIDString](uuidstring.md) — The UUID as a string.
