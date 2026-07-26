---
title: 'registerPort:name:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsportnameserver/registerport:name:'
source_url: 'https://developer.apple.com/documentation/foundation/nsportnameserver/registerport:name:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportnameserver/registerport%3Aname%3A.json'
content_hash: 'sha256:0dffdd99206d7c34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortNameServer](../nsportnameserver.md)

# registerPort:name:

<sub>Instance Method</sub>

Makes a given port available on the network under a specified name.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name;
```

## Parameters

- `port` — The port to make available.

- `name` — The name for the port.

## Return Value

[true](../../swift/true.md) if successful, [false](../../swift/false.md) otherwise (for example, if another `NSPort` object  has already been registered under `name`).

## Discussion

A port can be registered under multiple names. If it is, it must be unregistered for each name with [removePortForName:](removeportforname_.md) to make it completely unavailable.

## See Also

### Registering Ports

- [removePortForName:](removeportforname_.md) — Unregisters the port for a given name on the local host. _(deprecated)_
