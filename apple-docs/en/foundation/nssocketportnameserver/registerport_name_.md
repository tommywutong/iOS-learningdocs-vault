---
title: 'registerPort:name:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nssocketportnameserver/registerport:name:'
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver/registerport:name:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver/registerport%3Aname%3A.json'
content_hash: 'sha256:1c18f2ba92b330f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSocketPortNameServer](../nssocketportnameserver.md)

# registerPort:name:

<sub>Instance Method</sub>

Registers a given port as a network service with the specified name in the local domain.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>macOS</sub>

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name;
```

## Parameters

- `port` — The port to make available.

- `name` — The name for the port.

## Return Value

[true](../../swift/true.md) if successful, [false](../../swift/false.md) otherwise.

## Discussion

Invokes [registerPort:name:nameServerPortNumber:](registerport_name_nameserverportnumber_.md) with 0 as the name server port number.

## See Also

### Registering and Removing Ports

- [registerPort:name:nameServerPortNumber:](registerport_name_nameserverportnumber_.md) — Registers a given port as a network service with the specified name in the local domain. _(deprecated)_
- [removePortForName:](removeportforname_.md) — Unregisters the port for a given name on the local host. _(deprecated)_
