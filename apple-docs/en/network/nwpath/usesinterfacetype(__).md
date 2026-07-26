---
title: 'usesInterfaceType(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwpath/usesinterfacetype(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwpath/usesinterfacetype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/usesinterfacetype%28_%3A%29.json'
content_hash: 'sha256:e47b9f08062a449d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# usesInterfaceType(_:)

<sub>Instance Method</sub>

Checks if connections using the path may send traffic over a specific interface type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func usesInterfaceType(_ type: NWInterface.InterfaceType) -> Bool
```

## Discussion

Paths can use interface types by directly routing over an interface, routing through a tunnel that goes over a physical interface, or being eligble to use multiple interfaces directly.

## See Also

### Inspecting Interfaces

- [availableInterfaces](availableinterfaces.md) — A list of all interfaces available to the path, in order of preference.
- [gateways](gateways.md) — A list of gateways configured on the interfaces available to a path.
