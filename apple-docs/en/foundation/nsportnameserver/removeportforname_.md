---
title: 'removePortForName:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.13 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsportnameserver/removeportforname:'
source_url: 'https://developer.apple.com/documentation/foundation/nsportnameserver/removeportforname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsportnameserver/removeportforname%3A.json'
content_hash: 'sha256:32b88abf90830fc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPortNameServer](../nsportnameserver.md)

# removePortForName:

<sub>Instance Method</sub>

Unregisters the port for a given name on the local host.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) removePortForName:(NSString *) name;
```

## Parameters

- `name` — The name of the port to unregister.

## Return Value

[true](../../swift/true.md) if successful, otherwise [false](../../swift/false.md).

## Discussion

If the operation is successful, the port can no longer be looked up using the name `name`. Other applications that already have a reference to the port can continue to use it until it becomes invalid.

## See Also

### Registering Ports

- [registerPort:name:](registerport_name_.md) — Makes a given port available on the network under a specified name. _(deprecated)_
