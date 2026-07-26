---
title: addresses
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice/addresses
source_url: 'https://developer.apple.com/documentation/foundation/netservice/addresses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/addresses.json'
content_hash: 'sha256:c6974e23c8264878'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# addresses

<sub>Instance Property</sub>

A read-only array containing `NSData` objects, each of which contains a socket address for the service.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var addresses: [Data]? { get }
```

## Discussion

An array containing `NSData` objects, each of which contains a socket address for the service. Each `NSData` object in the returned array contains an appropriate `sockaddr` structure that you can use to connect to the socket. The exact type of this structure depends on the service to which you are connecting. If no addresses were resolved for the service, the returned array contains zero elements.

It is possible for a single service to resolve to more than one address or not resolve to any addresses. A service might resolve to multiple addresses if the computer publishing the service is currently multihoming.

> [!note] Backward Compatibility Note
> This became a property in OS X v10.9 and iOS 7, but the underlying getter method (`addresses`) has been available since this class was first introduced.

## See Also

### Related Documentation

- [- resolve](<resolve().md>) — Starts a resolve process for the service. _(deprecated)_

### Configuring Network Services

- [+ dataFromTXTRecordDictionary:](<data(fromtxtrecord_).md>) — Returns an `NSData` object representing a TXT record formed from a given dictionary. _(deprecated)_
- [+ dictionaryFromTXTRecordData:](<dictionary(fromtxtrecord_).md>) — Returns a dictionary representing a TXT record given as an `NSData` object. _(deprecated)_
- [domain](domain.md) — A string containing the domain for this service. _(deprecated)_
- [includesPeerToPeer](includespeertopeer.md) — Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available. _(deprecated)_
- [- getInputStream:outputStream:](<getinputstream(__outputstream_).md>) — Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully. _(deprecated)_
- [name](name.md) — A string containing the name of this service. _(deprecated)_
- [type](type.md) — The type of the published service. _(deprecated)_
- [- TXTRecordData](<txtrecorddata().md>) — Returns the TXT record for the receiver. _(deprecated)_
- [- setTXTRecordData:](<settxtrecord(__).md>) — Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful. _(deprecated)_
- [delegate](delegate.md) — The delegate for the receiver. _(deprecated)_
