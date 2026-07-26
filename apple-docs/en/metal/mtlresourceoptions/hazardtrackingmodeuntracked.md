---
title: hazardTrackingModeUntracked
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceoptions/hazardtrackingmodeuntracked
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceoptions/hazardtrackingmodeuntracked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceoptions/hazardtrackingmodeuntracked.json'
content_hash: 'sha256:ac7a9b0e7a4ddaec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceOptions](../mtlresourceoptions.md)

# hazardTrackingModeUntracked

<sub>Type Property</sub>

A resource option that instructs Metal to ignore memory hazards for a resource at runtime.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var hazardTrackingModeUntracked: MTLResourceOptions { get }
```

## Discussion

For more information, see [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md).

## See Also

### Specifying hazard tracking

- [MTLResourceHazardTrackingModeTracked](hazardtrackingmodetracked.md) — An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.
