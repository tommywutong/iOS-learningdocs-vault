---
title: 'encodeXPCObject(_:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpccoder/encodexpcobject(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpccoder/encodexpcobject(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpccoder/encodexpcobject%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:7d48751f1e005b80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCCoder](../nsxpccoder.md)

# encodeXPCObject(_:forKey:)

<sub>Instance Method</sub>

Encodes an object to send over an XPC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encodeXPCObject(_ xpcObject: xpc_object_t, forKey key: String)
```

## Parameters

- `xpcObject` — An object that XPC can encode.

- `key` — A string that your app uses to reference the encoded object.

## See Also

### Encoding and Decoding

- [- decodeXPCObjectOfType:forKey:](<decodexpcobject(oftype_forkey_).md>) — Decodes an object and validates that its type matches the type a service provides over XPC.
