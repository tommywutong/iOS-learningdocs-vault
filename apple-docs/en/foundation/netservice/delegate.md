---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice/delegate
source_url: 'https://developer.apple.com/documentation/foundation/netservice/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/delegate.json'
content_hash: 'sha256:257fe8925544bb1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# delegate

<sub>Instance Property</sub>

The delegate for the receiver.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
unowned(unsafe) var delegate: (any NetServiceDelegate)? { get set }
```

## Discussion

The delegate must conform to the [NetServiceDelegate](../netservicedelegate.md) protocol, and is not retained.

> [!note] Backward Compatibility Note
> This became a property in OS X v10.9 and iOS 7, but the underlying getter and setter methods (`delegate` and `setDelegate`) have been available since this class was first introduced.

## See Also

### Configuring Network Services

- [+ dataFromTXTRecordDictionary:](<data(fromtxtrecord_).md>) — Returns an `NSData` object representing a TXT record formed from a given dictionary. _(deprecated)_
- [+ dictionaryFromTXTRecordData:](<dictionary(fromtxtrecord_).md>) — Returns a dictionary representing a TXT record given as an `NSData` object. _(deprecated)_
- [addresses](addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_
- [domain](domain.md) — A string containing the domain for this service. _(deprecated)_
- [includesPeerToPeer](includespeertopeer.md) — Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available. _(deprecated)_
- [- getInputStream:outputStream:](<getinputstream(__outputstream_).md>) — Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully. _(deprecated)_
- [name](name.md) — A string containing the name of this service. _(deprecated)_
- [type](type.md) — The type of the published service. _(deprecated)_
- [- TXTRecordData](<txtrecorddata().md>) — Returns the TXT record for the receiver. _(deprecated)_
- [- setTXTRecordData:](<settxtrecord(__).md>) — Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful. _(deprecated)_
