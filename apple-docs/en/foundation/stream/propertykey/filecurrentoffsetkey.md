---
title: fileCurrentOffsetKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/propertykey/filecurrentoffsetkey
source_url: 'https://developer.apple.com/documentation/foundation/stream/propertykey/filecurrentoffsetkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/propertykey/filecurrentoffsetkey.json'
content_hash: 'sha256:a83423dd5da23a7c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Stream](../../stream.md) · [PropertyKey](../propertykey.md)

# fileCurrentOffsetKey

<sub>Type Property</sub>

Value is an `NSNumber` object containing the current absolute offset of the stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let fileCurrentOffsetKey: Stream.PropertyKey
```

## See Also

### Type Properties

- [NSStreamDataWrittenToMemoryStreamKey](datawrittentomemorystreamkey.md) — Value is an `NSData` instance containing the data written to a memory stream.
- [NSStreamNetworkServiceType](networkservicetype.md) — The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.
- [NSStreamSocketSecurityLevelKey](socketsecuritylevelkey.md)
- [NSStreamSOCKSProxyConfigurationKey](socksproxyconfigurationkey.md) — Value is an `NSDictionary` object containing SOCKS proxy configuration information.
