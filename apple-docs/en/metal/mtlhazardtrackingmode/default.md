---
title: MTLHazardTrackingMode.default
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlhazardtrackingmode/default
source_url: 'https://developer.apple.com/documentation/metal/mtlhazardtrackingmode/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlhazardtrackingmode/default.json'
content_hash: 'sha256:049222fa652cf37d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHazardTrackingMode](../mtlhazardtrackingmode.md)

# MTLHazardTrackingMode.default

<sub>Case</sub>

An option that applies the default tracking behavior in Metal based on the resource or heap type you’re creating.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case `default`
```

## Discussion

When you choose the [MTLHazardTrackingModeDefault](default.md) option, Metal assigns a tracking mode based on the type you’re creating:

- The default tracking mode for an [MTLHeap](../mtlheap.md) is [MTLHazardTrackingModeUntracked](untracked.md) because heaps typically contain many resources that you manage manually.
- The default tracking mode for a type that inherits [MTLResource](../mtlresource.md) is [MTLHazardTrackingModeTracked](tracked.md) because individual resources benefit from automatic hazard tracking.

For example, Metal tracks hazards for [MTLBuffer](../mtlbuffer.md) and [MTLTexture](../mtltexture.md) instances when you create them with [MTLHazardTrackingModeDefault](default.md).

For more information, see [MTLHazardTrackingMode](../mtlhazardtrackingmode.md).

## See Also

### Selecting the tracking mode

- [MTLHazardTrackingModeUntracked](untracked.md) — An option that disables automatic memory hazard tracking in Metal for a resource at runtime.
- [MTLHazardTrackingModeTracked](tracked.md) — An option that directs Metal to apply runtime safeguards that prevent memory hazards when commands access a resource.
