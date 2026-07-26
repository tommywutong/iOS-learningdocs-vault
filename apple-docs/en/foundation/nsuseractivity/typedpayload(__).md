---
title: 'typedPayload(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivity/typedpayload(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/typedpayload(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/typedpayload%28_%3A%29.json'
content_hash: 'sha256:c732926dada1dec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# typedPayload(_:)

<sub>Instance Method</sub>

Decodes the user activity’s user info dictionary as an instance of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func typedPayload<T>(_ type: T.Type) throws -> T where T : Decodable, T : Encodable
```

## Parameters

- `type` — The type to decode from [userInfo](userinfo.md). The `type` must conform to [Codable](../../swift/codable.md).

## Return Value

The type-safe instance.

## Discussion

> [!important] Important
> This method applies only to SwiftUI apps.

Use this method to retrieve information from the user activity’s [userInfo](userinfo.md) dictionary in a type-safe manner.

If the type can’t be decoded from the [userInfo](userinfo.md) dictionary, this method throws [NSUserActivity.TypedPayloadError.invalidContent](typedpayloaderror/invalidcontent.md).

## See Also

### Managing type-safe access to user info

- [setTypedPayload(_:)](<settypedpayload(__).md>) — Encodes the specified payload into the user activity’s user info dictionary.
- [TypedPayloadError](typedpayloaderror.md) — An enumeration that describes the error types for getting and setting a typed payload.
