---
title: 'dictionary(fromTXTRecord:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservice/dictionary(fromtxtrecord:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/dictionary(fromtxtrecord:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/dictionary%28fromtxtrecord%3A%29.json'
content_hash: 'sha256:a973a0bb1616cb6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# dictionary(fromTXTRecord:)

<sub>Type Method</sub>

Returns a dictionary representing a TXT record given as an `NSData` object.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func dictionary(fromTXTRecord txtData: Data) -> [String : Data]
```

## Parameters

- `txtData` — A data object encoding a TXT record.

## Return Value

A dictionary representing `txtData`. The dictionary’s keys are `NSString` objects using UTF8 encoding. The values associated with all the dictionary’s keys are `NSData` objects that encapsulate strings or data. Fails an assertion if `txtData` cannot be represented as an `NSDictionary` object.

## See Also

### Configuring Network Services

- [+ dataFromTXTRecordDictionary:](<data(fromtxtrecord_).md>) — Returns an `NSData` object representing a TXT record formed from a given dictionary. _(deprecated)_
- [addresses](addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_
- [domain](domain.md) — A string containing the domain for this service. _(deprecated)_
- [includesPeerToPeer](includespeertopeer.md) — Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available. _(deprecated)_
- [- getInputStream:outputStream:](<getinputstream(__outputstream_).md>) — Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully. _(deprecated)_
- [name](name.md) — A string containing the name of this service. _(deprecated)_
- [type](type.md) — The type of the published service. _(deprecated)_
- [- TXTRecordData](<txtrecorddata().md>) — Returns the TXT record for the receiver. _(deprecated)_
- [- setTXTRecordData:](<settxtrecord(__).md>) — Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful. _(deprecated)_
- [delegate](delegate.md) — The delegate for the receiver. _(deprecated)_
