---
title: prohibitedInterfaces
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/prohibitedinterfaces
source_url: 'https://developer.apple.com/documentation/network/nwparameters/prohibitedinterfaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/prohibitedinterfaces.json'
content_hash: 'sha256:f3638ba7a07944f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# prohibitedInterfaces

<sub>Instance Property</sub>

A list of specific interfaces that connections and listeners will not use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var prohibitedInterfaces: [NWInterface]? { get set }
```

## See Also

### Selecting Paths

- [requiredInterfaceType](requiredinterfacetype.md) — An interface type to require on connections and listeners.
- [requiredInterface](requiredinterface.md) — A specific interface to require on connections, listeners, and browsers.
- [requiredLocalEndpoint](requiredlocalendpoint.md) — A specific local IP address and port to use for connections and listeners.
- [prohibitConstrainedPaths](prohibitconstrainedpaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [prohibitExpensivePaths](prohibitexpensivepaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.
- [prohibitedInterfaceTypes](prohibitedinterfacetypes.md) — A list of interface types that connections, listeners, and browsers will not use.
