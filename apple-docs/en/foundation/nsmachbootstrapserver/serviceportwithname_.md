---
title: 'servicePortWithName:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmachbootstrapserver/serviceportwithname:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmachbootstrapserver/serviceportwithname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmachbootstrapserver/serviceportwithname%3A.json'
content_hash: 'sha256:ac32fe2007fadb49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMachBootstrapServer](../nsmachbootstrapserver.md)

# servicePortWithName:

<sub>Instance Method</sub>

Looks up and returns the port for the vended service that is registered under the specified name.

<sub>Mac Catalyst, macOS</sub>

```objc
- (NSPort *) servicePortWithName:(NSString *) name;
```

## Parameters

- `name` — The name of the vended service.

## Return Value

The port associated with `name`. Returns `nil` if no such port exists.

## See Also

### Looking up Ports

- [portForName:](portforname_.md) — Looks up and returns the port registered under the specified name on the local host. _(deprecated)_
- [portForName:host:](portforname_host_.md) — Looks up and returns the port registered under the specified name. _(deprecated)_
