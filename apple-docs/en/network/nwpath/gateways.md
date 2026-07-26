---
title: gateways
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/gateways
source_url: 'https://developer.apple.com/documentation/network/nwpath/gateways'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/gateways.json'
content_hash: 'sha256:2c33de4918173fc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# gateways

<sub>Instance Property</sub>

A list of gateways configured on the interfaces available to a path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var gateways: [NWEndpoint] { get }
```

## See Also

### Inspecting Interfaces

- [usesInterfaceType(_:)](<usesinterfacetype(__).md>) — Checks if connections using the path may send traffic over a specific interface type.
- [availableInterfaces](availableinterfaces.md) — A list of all interfaces available to the path, in order of preference.
