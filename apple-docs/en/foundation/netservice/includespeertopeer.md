---
title: includesPeerToPeer
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/netservice/includespeertopeer
source_url: 'https://developer.apple.com/documentation/foundation/netservice/includespeertopeer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/includespeertopeer.json'
content_hash: 'sha256:c4ebd68d1c6d9be5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NetService](../netservice.md)

# includesPeerToPeer

<sub>Instance Property</sub>

Specifies whether to also publish, resolve, or monitor this service over peer-to-peer Bluetooth and Wi-Fi, if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var includesPeerToPeer: Bool { get set }
```

## Discussion

This property must be set before calling [- publish](<publish().md>) or [- publishWithOptions:](<publish(options_).md>), [- resolveWithTimeout:](<resolve(withtimeout_).md>)`, or [- startMonitoring](<startmonitoring().md>) in order to take effect.

## See Also

### Configuring Network Services

- [+ dataFromTXTRecordDictionary:](<data(fromtxtrecord_).md>) — Returns an `NSData` object representing a TXT record formed from a given dictionary. _(deprecated)_
- [+ dictionaryFromTXTRecordData:](<dictionary(fromtxtrecord_).md>) — Returns a dictionary representing a TXT record given as an `NSData` object. _(deprecated)_
- [addresses](addresses.md) — A read-only array containing `NSData` objects, each of which contains a socket address for the service. _(deprecated)_
- [domain](domain.md) — A string containing the domain for this service. _(deprecated)_
- [- getInputStream:outputStream:](<getinputstream(__outputstream_).md>) — Creates a pair of input and output streams for the receiver and returns a Boolean value that indicates whether they were retrieved successfully. _(deprecated)_
- [name](name.md) — A string containing the name of this service. _(deprecated)_
- [type](type.md) — The type of the published service. _(deprecated)_
- [- TXTRecordData](<txtrecorddata().md>) — Returns the TXT record for the receiver. _(deprecated)_
- [- setTXTRecordData:](<settxtrecord(__).md>) — Sets the TXT record for the receiver, and returns a Boolean value that indicates whether the operation was successful. _(deprecated)_
- [delegate](delegate.md) — The delegate for the receiver. _(deprecated)_
