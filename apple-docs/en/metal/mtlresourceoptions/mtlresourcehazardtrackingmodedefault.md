---
title: MTLResourceHazardTrackingModeDefault
framework: Metal
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceoptions/mtlresourcehazardtrackingmodedefault
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcehazardtrackingmodedefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceoptions/mtlresourcehazardtrackingmodedefault.json'
content_hash: 'sha256:26d6f47019fd1441'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceOptions](../mtlresourceoptions.md)

# MTLResourceHazardTrackingModeDefault

<sub>Enumeration Case</sub>

An option specifying that the default tracking mode should be used.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
MTLResourceHazardTrackingModeDefault
```

## Discussion

For more information, see [MTLHazardTrackingModeDefault](../mtlhazardtrackingmode/default.md).

## See Also

### Specifying hazard tracking

- [MTLResourceHazardTrackingModeTracked](hazardtrackingmodetracked.md) — An option that instructs Metal to apply safeguards for a resource at runtime to avoid memory hazards for the applicable commands.
- [MTLResourceHazardTrackingModeUntracked](hazardtrackingmodeuntracked.md) — A resource option that instructs Metal to ignore memory hazards for a resource at runtime.
