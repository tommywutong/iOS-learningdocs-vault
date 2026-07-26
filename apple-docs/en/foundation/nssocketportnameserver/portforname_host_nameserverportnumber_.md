---
title: 'portForName:host:nameServerPortNumber:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nssocketportnameserver/portforname:host:nameserverportnumber:'
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver/portforname:host:nameserverportnumber:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver/portforname%3Ahost%3Anameserverportnumber%3A.json'
content_hash: 'sha256:eb86b384d7b2d5c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSocketPortNameServer](../nssocketportnameserver.md)

# portForName:host:nameServerPortNumber:

<sub>Instance Method</sub>

Looks up and returns the port registered under the specified name on a specified host.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host nameServerPortNumber:(uint16_t) portNumber;
```

## Parameters

- `name` — The name of the desired port.

- `host` — The name of the host. `hostName` is an Internet domain name (for example, “`sales.anycorp.com`”) or IP address (IPv4 or IPv6). If `hostName` is `nil` or empty, the local host is checked. If `hostName` is `@”*”`, all hosts on the local network are checked.

- `portNumber` — The `portNumber` parameter is ignored.

## Return Value

The port associated with `portName` on the host `hostName`. Returns `nil` if no such port exists.

## See Also

### Related Documentation

- [registerPort:name:nameServerPortNumber:](registerport_name_nameserverportnumber_.md) — Registers a given port as a network service with the specified name in the local domain. _(deprecated)_

### Looking up Ports

- [portForName:](portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
- [portForName:host:](portforname_host_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_
