---
title: 'portForName:host:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsportnameserver/portforname:host:'
source_url: 'https://developer.apple.com/documentation/foundation/nsportnameserver/portforname:host:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportnameserver/portforname%3Ahost%3A.json'
content_hash: 'sha256:67d31584d66a8963'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortNameServer](../nsportnameserver.md)

# portForName:host:

<sub>Instance Method</sub>

Looks up and returns the port registered under the specified name on a specified host.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host;
```

## Parameters

- `name` — The name of the desired port.

- `host` — The name of the host. `host` is an Internet domain name (for example, “`sales.anycorp.com`”). If `host` is `nil` or empty, the local host is checked.

## Return Value

The port associated with `name` on the host `host`. Returns `nil` if no such port exists.

## See Also

### Looking up Ports

- [portForName:](portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
