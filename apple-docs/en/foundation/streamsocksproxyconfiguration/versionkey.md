---
title: versionKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/streamsocksproxyconfiguration/versionkey
source_url: 'https://developer.apple.com/documentation/foundation/streamsocksproxyconfiguration/versionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/streamsocksproxyconfiguration/versionkey.json'
content_hash: 'sha256:9e3b809debe8b849'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StreamSOCKSProxyConfiguration](../streamsocksproxyconfiguration.md)

# versionKey

<sub>Type Property</sub>

Value is either `NSStreamSOCKSProxyVersion4` or `NSStreamSOCKSProxyVersion5`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let versionKey: StreamSOCKSProxyConfiguration
```

## Discussion

If this key is not present, `NSStreamSOCKSProxyVersion5` is used by default.

## See Also

### Type Properties

- [NSStreamSOCKSProxyHostKey](hostkey.md) — Value is an `NSString` object that represents the SOCKS proxy host.
- [NSStreamSOCKSProxyPasswordKey](passwordkey.md) — Value is an `NSString` object containing the user’s password.
- [NSStreamSOCKSProxyPortKey](portkey.md) — Value is an `NSNumber` object containing an integer that represents the port on which the proxy listens.
- [NSStreamSOCKSProxyUserKey](userkey.md) — Value is an `NSString` object containing the user’s name.
