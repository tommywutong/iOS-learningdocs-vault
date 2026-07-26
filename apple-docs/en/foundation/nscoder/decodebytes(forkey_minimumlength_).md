---
title: 'decodeBytes(forKey:minimumLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/decodebytes(forkey:minimumlength:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/decodebytes(forkey:minimumlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/decodebytes%28forkey%3Aminimumlength%3A%29.json'
content_hash: 'sha256:a19646c36a5a07d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# decodeBytes(forKey:minimumLength:)

<sub>Instance Method</sub>

Decode bytes from the decoder for a given key. The length of the bytes must be greater than or equal to the `length` parameter. If the result exists, but is of insufficient length, then the decoder uses `failWithError` to fail the entire decode operation. The result of that is configurable on a per-NSCoder basis using `NSDecodingFailurePolicy`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeBytes(forKey key: String, minimumLength length: Int) -> UnsafePointer<UInt8>?
```
