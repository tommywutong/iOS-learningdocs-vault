---
title: hazardTrackingModeTracked
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceoptions/hazardtrackingmodetracked
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceoptions/hazardtrackingmodetracked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceoptions/hazardtrackingmodetracked.json'
content_hash: 'sha256:f8b096d71f77bbd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceOptions](../mtlresourceoptions.md)

# hazardTrackingModeTracked

<sub>Type Property</sub>

An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var hazardTrackingModeTracked: MTLResourceOptions { get }
```

## Discussion

For more information, see [MTLHazardTrackingModeTracked](../mtlhazardtrackingmode/tracked.md).

## See Also

### Specifying hazard tracking

- [MTLResourceHazardTrackingModeUntracked](hazardtrackingmodeuntracked.md) — A resource option that instructs Metal to ignore memory hazards for a resource at runtime.
