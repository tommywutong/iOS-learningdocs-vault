---
title: prohibitedInterfaceTypes
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/prohibitedinterfacetypes
source_url: 'https://developer.apple.com/documentation/network/nwparameters/prohibitedinterfacetypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/prohibitedinterfacetypes.json'
content_hash: 'sha256:f01103f14771e440'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# prohibitedInterfaceTypes

<sub>Instance Property</sub>

A list of interface types that connections, listeners, and browsers will not use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var prohibitedInterfaceTypes: [NWInterface.InterfaceType]? { get set }
```

## See Also

### Selecting Paths

- [requiredInterfaceType](requiredinterfacetype.md) — An interface type to require on connections and listeners.
- [requiredInterface](requiredinterface.md) — A specific interface to require on connections, listeners, and browsers.
- [requiredLocalEndpoint](requiredlocalendpoint.md) — A specific local IP address and port to use for connections and listeners.
- [prohibitConstrainedPaths](prohibitconstrainedpaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [prohibitExpensivePaths](prohibitexpensivepaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.
- [prohibitedInterfaces](prohibitedinterfaces.md) — A list of specific interfaces that connections and listeners will not use.
