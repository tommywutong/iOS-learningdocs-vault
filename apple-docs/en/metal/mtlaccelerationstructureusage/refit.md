---
title: refit
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureusage/refit
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/refit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureusage/refit.json'
content_hash: 'sha256:0217cca0a28d0233'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUsage](../mtlaccelerationstructureusage.md)

# refit

<sub>Type Property</sub>

An option that lets you update an acceleration structure after creating it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var refit: MTLAccelerationStructureUsage { get }
```

## Discussion

Apply this option to make a modifiable acceleration structure, which you can update over time, such as for geometry changes. By default, the framework builds immutable acceleration structures for performance. When you apply the [MTLAccelerationStructureUsageRefit](refit.md) option, the framework builds an acceleration structure more conservatively, which can reduce its intersection performance.

> [!note] Note
> Refitting an acceleration structure generally works better when the geometry changes are relatively small.

## See Also

### Applying options

- [MTLAccelerationStructureUsagePreferFastBuild](preferfastbuild.md) — An option that instructs Metal to build an acceleration structure quickly.
- [MTLAccelerationStructureUsagePreferFastIntersection](preferfastintersection.md) — An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [MTLAccelerationStructureUsageMinimizeMemory](minimizememory.md) — An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [MTLAccelerationStructureUsageExtendedLimits](extendedlimits.md) — An option that increases an acceleration structure’s storage capacity.
