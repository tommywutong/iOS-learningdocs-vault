---
title: 'portForName:host:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nssocketportnameserver/portforname:host:'
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver/portforname:host:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver/portforname%3Ahost%3A.json'
content_hash: 'sha256:d0c50a8e9e588ccc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSocketPortNameServer](../nssocketportnameserver.md)

# portForName:host:

<sub>Instance Method</sub>

Looks up and returns the port registered under the specified name on a specified host.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host;
```

## Parameters

- `name` — The name of the desired port.

- `host` — The name of the host. `hostName` is an Internet domain name (for example, “`sales.anycorp.com`”). If `hostName` is `nil` or empty, the local host is checked.

## Return Value

The port associated with `portName` on the host `hostName`. Returns `nil` if no such port exists.

## Discussion

Invokes [portForName:host:nameServerPortNumber:](portforname_host_nameserverportnumber_.md) with 0 as the name server port number.

## See Also

### Looking up Ports

- [portForName:](portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
- [portForName:host:nameServerPortNumber:](portforname_host_nameserverportnumber_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_
