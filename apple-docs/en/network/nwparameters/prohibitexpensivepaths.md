---
title: prohibitExpensivePaths
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/prohibitexpensivepaths
source_url: 'https://developer.apple.com/documentation/network/nwparameters/prohibitexpensivepaths'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/prohibitexpensivepaths.json'
content_hash: 'sha256:186ffb2614583ab2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# prohibitExpensivePaths

<sub>Instance Property</sub>

A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var prohibitExpensivePaths: Bool { get set }
```

## Discussion

To test the behavior of this property, you can override the device’s current values for cellular and Wi-Fi cost in Settings \> Developer \> Network Override.

> [!tip] Tip
> Prefer basing your app’s policy logic around the [prohibitConstrainedPaths](prohibitconstrainedpaths.md) property rather than this one. People using your app can use the “Low Data Mode” setting to set the constrained status, and thereby choose to use a potentially expensive network.

## See Also

### Selecting Paths

- [requiredInterfaceType](requiredinterfacetype.md) — An interface type to require on connections and listeners.
- [requiredInterface](requiredinterface.md) — A specific interface to require on connections, listeners, and browsers.
- [requiredLocalEndpoint](requiredlocalendpoint.md) — A specific local IP address and port to use for connections and listeners.
- [prohibitConstrainedPaths](prohibitconstrainedpaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [prohibitedInterfaceTypes](prohibitedinterfacetypes.md) — A list of interface types that connections, listeners, and browsers will not use.
- [prohibitedInterfaces](prohibitedinterfaces.md) — A list of specific interfaces that connections and listeners will not use.
