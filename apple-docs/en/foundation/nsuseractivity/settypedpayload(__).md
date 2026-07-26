---
title: 'setTypedPayload(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsuseractivity/settypedpayload(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/settypedpayload(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/settypedpayload%28_%3A%29.json'
content_hash: 'sha256:0453fa2b45254070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# setTypedPayload(_:)

<sub>Instance Method</sub>

Encodes the specified payload into the user activity’s user info dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setTypedPayload<T>(_ payload: T) throws where T : Decodable, T : Encodable
```

## Parameters

- `payload` — The instance to convert to [userInfo](userinfo.md). The type of the `payload` instance must conform to [Codable](../../swift/codable.md).

## Discussion

> [!important] Important
> This method applies only to SwiftUI apps.

Use this method to set the user activity’s [userInfo](userinfo.md) dictionary in a type-safe manner. After you set the [userInfo](userinfo.md) dictionary using this approach, the keys in the [userInfo](userinfo.md) dictionary match the coding keys from the [Codable](../../swift/codable.md) type you provide as the `payload`.

If the type can’t be encoded into the [userInfo](userinfo.md) dictionary, this method throws [NSUserActivity.TypedPayloadError.encodingError](typedpayloaderror/encodingerror.md).

## See Also

### Managing type-safe access to user info

- [typedPayload(_:)](<typedpayload(__).md>) — Decodes the user activity’s user info dictionary as an instance of the specified type.
- [TypedPayloadError](typedpayloaderror.md) — An enumeration that describes the error types for getting and setting a typed payload.
