---
title: 'setPrivacyContext(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparameters/setprivacycontext(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparameters/setprivacycontext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/setprivacycontext%28_%3A%29.json'
content_hash: 'sha256:884dfb5d52b187c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# setPrivacyContext(_:)

<sub>Instance Method</sub>

Associates a privacy context with any connections or listeners that use the parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func setPrivacyContext(_ privacyContext: NWParameters.PrivacyContext)
```

## Discussion

The privacy context allows using separate caches for different sets of connections, as well as restricting how connection-specific information is logged and shared on the network.

## See Also

### Configuring Privacy Settings

- [PrivacyContext](privacycontext.md) — An object that defines the privacy requirements for a set of connections.
