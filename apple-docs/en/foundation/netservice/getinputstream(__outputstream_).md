---
title: 'getInputStream(_:outputStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.2+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/netservice/getinputstream(_:outputstream:)'
source_url: 'https://developer.apple.com/documentation/foundation/netservice/getinputstream(_:outputstream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/getinputstream%28_%3Aoutputstream%3A%29.json'
content_hash: 'sha256:4b9321dbd34b3139'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# getInputStream(_:outputStream:)

<sub>Instance Method</sub>

Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully.

> [!warning] Deprecated
> Use nw_connection_t or nw_listener_t in Network framework instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func getInputStream(_ inputStream: UnsafeMutablePointer<InputStream?>?, outputStream: UnsafeMutablePointer<OutputStream?>?) -> Bool
```

## Parameters

- `inputStream` — Upon return, the input stream for the receiver. Pass `NULL` if you do not need this stream.

- `outputStream` — Upon return, the output stream for the receiver. Pass `NULL` if you do not need this stream.

## Return Value

[true](../../swift/true.md) if the streams are created successfully, otherwise [false](../../swift/false.md).

## Discussion

After this method is called, no delegate callbacks are called by the receiver.

> [!note] Note
> If automatic reference counting is not used, the input and output streams returned through the parameters are _retained_, which means that you are responsible for releasing them to avoid memory leaks.

## See Also

### Configuring Network Services

- [+ dataFromTXTRecordDictionary:](<data(fromtxtrecord_).md>) — Returns an `NSData` object representing a TXT record formed from a given dictionary. _(deprecated)_
- [+ dictionaryFromTXTRecordData:](<dictionary(fromtxtrecord_).md>) — Returns a dictionary representing a TXT record given as an `NSData` object. _(deprecated)_
- [addresses](addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_
- [domain](domain.md) — A string containing the domain for this service. _(deprecated)_
- [includesPeerToPeer](includespeertopeer.md) — Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available. _(deprecated)_
- [name](name.md) — A string containing the name of this service. _(deprecated)_
- [type](type.md) — The type of the published service. _(deprecated)_
- [- TXTRecordData](<txtrecorddata().md>) — Returns the TXT record for the receiver. _(deprecated)_
- [- setTXTRecordData:](<settxtrecord(__).md>) — Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful. _(deprecated)_
- [delegate](delegate.md) — The delegate for the receiver. _(deprecated)_
