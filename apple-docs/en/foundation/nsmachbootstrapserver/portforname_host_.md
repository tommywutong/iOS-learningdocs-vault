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
doc_path: '/documentation/foundation/nsmachbootstrapserver/portforname:host:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachbootstrapserver/portforname:host:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachbootstrapserver/portforname%3Ahost%3A.json'
content_hash: 'sha256:be388ecc284f4b5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachBootstrapServer](../nsmachbootstrapserver.md)

# portForName:host:

<sub>Instance Method</sub>

Looks up and returns the port registered under the specified name.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host;
```

## Parameters

- `name` — The name of the desired port.

- `host` — Because `NSMachBootstrapServer` is a local-only server; `hostName` must be the empty string or `nil`.

## Return Value

The port associated with `portName` on the local host. Returns `nil` if no such port exists.

## See Also

### Looking up Ports

- [portForName:](portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
- [servicePortWithName:](serviceportwithname_.md) — Looks up and returns the port for the vended service that is registered under the specified name. _(deprecated)_
