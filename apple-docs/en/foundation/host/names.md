---
title: names
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/host/names
source_url: 'https://developer.apple.com/documentation/foundation/host/names'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/names.json'
content_hash: 'sha256:abc8127e5384d581'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# names

<sub>Instance Property</sub>

Returns all the hostnames of the receiver.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
var names: [String] { get }
```

## Return Value

All the hostnames of the receiver.

## See Also

### Getting Host Information

- [address](address.md) — Returns one of the network addresses of the receiver. _(deprecated)_
- [addresses](addresses.md) — Returns all the network addresses of the receiver. _(deprecated)_
- [name](name.md) — Returns one of the hostnames of the receiver. _(deprecated)_
- [localizedName](localizedname.md) — Returns the name used as by default when publishing `NSNetServices`. _(deprecated)_
