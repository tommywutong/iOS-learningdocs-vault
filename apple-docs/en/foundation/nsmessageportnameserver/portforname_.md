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
doc_path: '/documentation/foundation/nsmessageportnameserver/portforname:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmessageportnameserver/portforname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmessageportnameserver/portforname%3A.json'
content_hash: 'sha256:5a5235b76282bfde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMessagePortNameServer](../nsmessageportnameserver.md)

# portForName:

<sub>Instance Method</sub>

Returns the `NSPort` object registered under a given name on the local host.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSPort *) portForName:(NSString *) name;
```

## Parameters

- `name` — The port name.

## Return Value

The NSPort registered under `portName` on the local host Returns `nil` if a port named `portName` does not exist.

## See Also

### Getting Ports By Name

- [portForName:host:](portforname_host_.md) — Returns the `NSPort` object registered under a given name on the local host. _(deprecated)_
