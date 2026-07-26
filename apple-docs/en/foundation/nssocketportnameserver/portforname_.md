---
title: 'portForName:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nssocketportnameserver/portforname:'
source_url: 'https://developer.apple.com/documentation/foundation/nssocketportnameserver/portforname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssocketportnameserver/portforname%3A.json'
content_hash: 'sha256:829e2928dc8b6465'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSocketPortNameServer](../nssocketportnameserver.md)

# portForName:

<sub>Instance Method</sub>

Looks up and returns the port registered under the specified name on the local host.

> [!warning] Deprecated
> Apple discourages the use of this symbol.

<sub>macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name;
```

## Parameters

- `name` — The name of the desired port.

## Return Value

The port associated with `portName` on the local host. Returns `nil` if no such port exists.

## Discussion

Invokes [portForName:host:nameServerPortNumber:](portforname_host_nameserverportnumber_.md) with `nil` as the host name and 0 as the name server port number.

## See Also

### Looking up Ports

- [portForName:host:](portforname_host_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_
- [portForName:host:nameServerPortNumber:](portforname_host_nameserverportnumber_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_
