---
title: 'expensivePathsProhibited(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/expensivepathsprohibited(_:)-53yp0'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/expensivepathsprohibited(_:)-53yp0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/expensivepathsprohibited%28_%3A%29-53yp0.json'
content_hash: 'sha256:ff806e1ec3c6292c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# expensivePathsProhibited(_:)

<sub>Instance Method</sub>

Prohibit using expensive paths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func expensivePathsProhibited(_ prohibited: Bool) -> Self
```

## Parameters

- `prohibited` — True if expensive paths are prohibited, false otherwise.

## Discussion

Prohibit connections and listeners from using a network interface that is considered expensive by the system, for example some cellular interfaces.
