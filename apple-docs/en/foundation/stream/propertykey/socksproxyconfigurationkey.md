---
title: socksProxyConfigurationKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stream/propertykey/socksproxyconfigurationkey
source_url: 'https://developer.apple.com/documentation/foundation/stream/propertykey/socksproxyconfigurationkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stream/propertykey/socksproxyconfigurationkey.json'
content_hash: 'sha256:d28ab432f8d90db8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Stream](../../stream.md) · [PropertyKey](../propertykey.md)

# socksProxyConfigurationKey

<sub>Type Property</sub>

Value is an `NSDictionary` object containing SOCKS proxy configuration information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let socksProxyConfigurationKey: Stream.PropertyKey
```

## Discussion

The dictionary returned from the System Configuration framework for SOCKS proxies usually suffices.

## See Also

### Type Properties

- [NSStreamDataWrittenToMemoryStreamKey](datawrittentomemorystreamkey.md) — Value is an `NSData` instance containing the data written to a memory stream.
- [NSStreamFileCurrentOffsetKey](filecurrentoffsetkey.md) — Value is an `NSNumber` object containing the current absolute offset of the stream.
- [NSStreamNetworkServiceType](networkservicetype.md) — The type of service for the stream. Providing the service type allows the system to properly handle certain attributes of the stream, including routing and suspension behavior. Most streams do not need to set this property. See `Stream Service Types` for a list of possible values.
- [NSStreamSocketSecurityLevelKey](socketsecuritylevelkey.md)
