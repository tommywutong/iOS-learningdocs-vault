---
title: resolutions
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/establishmentreport/resolutions
source_url: 'https://developer.apple.com/documentation/network/nwconnection/establishmentreport/resolutions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/establishmentreport/resolutions.json'
content_hash: 'sha256:efebe6b607fc3779'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [EstablishmentReport](../establishmentreport.md)

# resolutions

<sub>Instance Property</sub>

The array of resolution steps performed during connection establishment, in order from first resolved to last resolved.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let resolutions: [NWConnection.EstablishmentReport.Resolution]
```

## See Also

### Inspecting Resolution

- [Resolution](resolution.md) — A description of a single DNS resolution step.
