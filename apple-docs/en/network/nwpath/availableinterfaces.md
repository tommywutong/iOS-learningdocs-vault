---
title: availableInterfaces
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/availableinterfaces
source_url: 'https://developer.apple.com/documentation/network/nwpath/availableinterfaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/availableinterfaces.json'
content_hash: 'sha256:582bd3132a6a8425'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# availableInterfaces

<sub>Instance Property</sub>

A list of all interfaces available to the path, in order of preference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let availableInterfaces: [NWInterface]
```

## See Also

### Inspecting Interfaces

- [usesInterfaceType(_:)](<usesinterfacetype(__).md>) — Checks if connections using the path may send traffic over a specific interface type.
- [gateways](gateways.md) — A list of gateways configured on the interfaces available to a path.
