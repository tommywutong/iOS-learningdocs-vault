---
title: 'registerPort:name:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmachbootstrapserver/registerport:name:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachbootstrapserver/registerport:name:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachbootstrapserver/registerport%3Aname%3A.json'
content_hash: 'sha256:02bc46c855557c8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachBootstrapServer](../nsmachbootstrapserver.md)

# registerPort:name:

<sub>Instance Method</sub>

Registers a port with a specified name.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) registerPort:(NSPort *) port name:(NSString *) name;
```

## Parameters

- `port` — The port object to register with the bootstrap server.

- `name` — The name to associate with `port`.

## Return Value

[true](../../swift/true.md) if the registration succeeded, [false](../../swift/false.md) otherwise.

## Discussion

Once registered, a port cannot be unregistered; instead, you need to invalidate the port.
