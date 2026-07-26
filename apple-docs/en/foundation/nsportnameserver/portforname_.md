---
title: 'portForName:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsportnameserver/portforname:'
source_url: 'https://developer.apple.com/documentation/foundation/nsportnameserver/portforname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportnameserver/portforname%3A.json'
content_hash: 'sha256:84e290b726972643'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortNameServer](../nsportnameserver.md)

# portForName:

<sub>Instance Method</sub>

Looks up and returns the port registered under the specified name on the local host.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name;
```

## Parameters

- `name` — The name of the desired port.

## Return Value

The port associated with `portName` on the local host. Returns `nil` if no such port exists.

## Discussion

Invokes [portForName:host:](portforname_host_.md) with `nil` as the host name.

## See Also

### Looking up Ports

- [portForName:host:](portforname_host_.md) — Looks up and returns the port registered under the specified name on a specified host. _(deprecated)_
