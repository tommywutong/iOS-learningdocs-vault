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
doc_path: '/documentation/foundation/nsmessageportnameserver/portforname:host:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmessageportnameserver/portforname:host:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmessageportnameserver/portforname%3Ahost%3A.json'
content_hash: 'sha256:477ce7fcadab2def'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMessagePortNameServer](../nsmessageportnameserver.md)

# portForName:host:

<sub>Instance Method</sub>

Returns the `NSPort` object registered under a given name on the local host.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name host:(NSString *) host;
```

## Parameters

- `name` — The port name.

- `host` — The host name. Because `NSMessagePortNameServer` is a local-only server, `host` must be the empty string or `nil`.

## Return Value

The `NSPort` object registered under a given name on the local host. Returns `nil` if a port named `name` does not exist.

## See Also

### Getting Ports By Name

- [portForName:](portforname_.md) — Returns the `NSPort` object registered under a given name on the local host. _(deprecated)_
