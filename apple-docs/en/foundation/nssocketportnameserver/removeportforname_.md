---
title: 'removePortForName:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nssocketportnameserver/removeportforname:'
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver/removeportforname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver/removeportforname%3A.json'
content_hash: 'sha256:8d6213614c2cc88b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSocketPortNameServer](../nssocketportnameserver.md)

# removePortForName:

<sub>Instance Method</sub>

Unregisters the port for a given name on the local host.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>macOS</sub>

```objc
- (BOOL) removePortForName:(NSString *) name;
```

## Parameters

- `name` — The name of the port to unregister.

## Return Value

[true](../../swift/true.md) if successful, otherwise [false](../../swift/false.md).

## Discussion

If the operation is successful, the port can no longer be looked up using the name `portName`. Other applications that already have a reference to the port can continue to use it until it becomes invalid.

## See Also

### Registering and Removing Ports

- [registerPort:name:](registerport_name_.md) — Registers a given port as a network service with the specified name in the local domain. _(deprecated)_
- [registerPort:name:nameServerPortNumber:](registerport_name_nameserverportnumber_.md) — Registers a given port as a network service with the specified name in the local domain. _(deprecated)_
