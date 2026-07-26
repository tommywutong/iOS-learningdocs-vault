---
title: 'decodeXPCObject(ofType:forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsxpccoder/decodexpcobject(oftype:forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsxpccoder/decodexpcobject(oftype:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpccoder/decodexpcobject%28oftype%3Aforkey%3A%29.json'
content_hash: 'sha256:f96ed346b677e495'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSXPCCoder](../nsxpccoder.md)

# decodeXPCObject(ofType:forKey:)

<sub>Instance Method</sub>

Decodes an object and validates that its type matches the type a service provides over XPC.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decodeXPCObject(ofType type: xpc_type_t, forKey key: String) -> xpc_object_t?
```

## Parameters

- `type` — An opaque pointer to an encoded XPC object.

- `key` — A string that your app uses to reference the decoded object.

## Return Value

An object that XPC can encode.

## Discussion

The [- decodeXPCObjectOfType:forKey:](<decodexpcobject(oftype_forkey_).md>) method validates that the type of the decoded object matches the type of the encoded object. If they don’t match, the [NSXPCCoder](../nsxpccoder.md) throws an exception in support of [NSSecureCoding](../nssecurecoding.md).

Be sure to check the result against [null](../nsnull/null.md) if you call an [XPC](../../xpc.md) function because calling an [XPC](../../xpc.md) function on a [null](../nsnull/null.md) object results in a crash.

## See Also

### Encoding and Decoding

- [- encodeXPCObject:forKey:](<encodexpcobject(__forkey_).md>) — Encodes an object to send over an XPC connection.
