---
title: addresses
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/host/addresses
source_url: 'https://developer.apple.com/documentation/foundation/host/addresses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/addresses.json'
content_hash: 'sha256:2411edb07596466a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# addresses

<sub>Instance Property</sub>

Returns all the network addresses of the receiver.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
var addresses: [String] { get }
```

## Return Value

All the network addresses of the receiver.

## See Also

### Getting Host Information

- [address](address.md) — Returns one of the network addresses of the receiver. _(deprecated)_
- [name](name.md) — Returns one of the hostnames of the receiver. _(deprecated)_
- [localizedName](localizedname.md) — Returns the name used as by default when publishing `NSNetServices`. _(deprecated)_
- [names](names.md) — Returns all the hostnames of the receiver. _(deprecated)_
