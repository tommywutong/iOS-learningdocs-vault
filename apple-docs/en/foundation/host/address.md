---
title: address
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/host/address
source_url: 'https://developer.apple.com/documentation/foundation/host/address'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/address.json'
content_hash: 'sha256:29d233ee8fba0f9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# address

<sub>Instance Property</sub>

Returns one of the network addresses of the receiver.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
var address: String? { get }
```

## Return Value

One of the network address for the receiver. For example, `"192.42.172.1"` or `"fe80::1"`.

## See Also

### Getting Host Information

- [addresses](addresses.md) — Returns all the network addresses of the receiver. _(deprecated)_
- [name](name.md) — Returns one of the hostnames of the receiver. _(deprecated)_
- [localizedName](localizedname.md) — Returns the name used as by default when publishing `NSNetServices`. _(deprecated)_
- [names](names.md) — Returns all the hostnames of the receiver. _(deprecated)_
