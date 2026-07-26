---
title: name
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/host/name
source_url: 'https://developer.apple.com/documentation/foundation/host/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/host/name.json'
content_hash: 'sha256:137ed8e9d145ca02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Host](../host.md)

# name

<sub>Instance Property</sub>

Returns one of the hostnames of the receiver.

> [!warning] Deprecated
> Use Network framework instead, see deprecation notice in \<Foundation/NSHost.h\>

<sub>macOS</sub>

```swift
var name: String? { get }
```

## Return Value

One of the hostnames of the receiver. Can be either a simple hostname, such as `"sales"`, or a fully qualified domain name, such as `"sales.anycorp.com"`.

## See Also

### Getting Host Information

- [address](address.md) — Returns one of the network addresses of the receiver. _(deprecated)_
- [addresses](addresses.md) — Returns all the network addresses of the receiver. _(deprecated)_
- [localizedName](localizedname.md) — Returns the name used as by default when publishing `NSNetServices`. _(deprecated)_
- [names](names.md) — Returns all the hostnames of the receiver. _(deprecated)_
