---
title: requiredInterface
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/requiredinterface
source_url: 'https://developer.apple.com/documentation/network/nwparameters/requiredinterface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/requiredinterface.json'
content_hash: 'sha256:263239c434d6a1c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# requiredInterface

<sub>Instance Property</sub>

A specific interface to require on connections, listeners, and browsers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var requiredInterface: NWInterface? { get set }
```

## See Also

### Selecting Paths

- [requiredInterfaceType](requiredinterfacetype.md) — An interface type to require on connections and listeners.
- [requiredLocalEndpoint](requiredlocalendpoint.md) — A specific local IP address and port to use for connections and listeners.
- [prohibitConstrainedPaths](prohibitconstrainedpaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [prohibitExpensivePaths](prohibitexpensivepaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.
- [prohibitedInterfaceTypes](prohibitedinterfacetypes.md) — A list of interface types that connections, listeners, and browsers will not use.
- [prohibitedInterfaces](prohibitedinterfaces.md) — A list of specific interfaces that connections and listeners will not use.
