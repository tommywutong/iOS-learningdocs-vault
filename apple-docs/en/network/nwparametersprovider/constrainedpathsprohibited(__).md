---
title: 'constrainedPathsProhibited(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/constrainedpathsprohibited(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/constrainedpathsprohibited(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/constrainedpathsprohibited%28_%3A%29.json'
content_hash: 'sha256:050d5b4932bcffa7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# constrainedPathsProhibited(_:)

<sub>Instance Method</sub>

Prohibit using constrained paths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func constrainedPathsProhibited(_ prohibited: Bool) -> Self
```

## Parameters

- `prohibited` — True if constrained paths are prohibited, false otherwise.

## Discussion

Prohibit connections and listeners from using a network interface that is considered constrained by the system, for example an interface in Low Data Mode.

## Default Implementations

### NWParametersProvider Implementations

- [constrainedPathsProhibited(_:)](<constrainedpathsprohibited(__)-5anfr.md>) — Prohibit using constrained paths.
