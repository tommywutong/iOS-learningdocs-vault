---
title: 'registerPort:name:nameServerPortNumber:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nssocketportnameserver/registerport:name:nameserverportnumber:'
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver/registerport:name:nameserverportnumber:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver/registerport%3Aname%3Anameserverportnumber%3A.json'
content_hash: 'sha256:db1ec17d0618db06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSocketPortNameServer](../nssocketportnameserver.md)

# registerPort:name:nameServerPortNumber:

<sub>Instance Method</sub>

Registers a given port as a network service with the specified name in the local domain.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>macOS</sub>

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name nameServerPortNumber:(uint16_t) portNumber;
```

## Parameters

- `port` — The port to make available.

- `name` — The name for the port.

- `portNumber` — The `portNumber` parameter is ignored.

## Return Value

[true](../../swift/true.md) if successful, [false](../../swift/false.md) otherwise.

## Discussion

If your application has already registered a port under the name `portName`, this method replaces it with `port`.

If the local domain already has a port named `portName` registered, this method could return [true](../../swift/true.md) before the name collision is detected. To detect a potential name collision, you can invoke [portForName:host:](portforname_host_.md) with a `host` argument of `@"*"` to test if `portName` is already taken. This, however, leaves a race condition wherein another process can register a port under `portName` after [portForName:host:](portforname_host_.md) returns but before you register `port`. If this is an unacceptable risk for your application, you can also invoke [portForName:host:](portforname_host_.md) some finite time after registering your port to test if you get the same port back.

## See Also

### Related Documentation

- [portForName:host:nameServerPortNumber:](portforname_host_nameserverportnumber_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_

### Registering and Removing Ports

- [registerPort:name:](registerport_name_.md) — Registers a given port as a network service with the specified name in the local domain. _(deprecated)_
- [removePortForName:](removeportforname_.md) — Unregisters the port for a given name on the local host. _(deprecated)_
