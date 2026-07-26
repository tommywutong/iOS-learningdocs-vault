---
title: preferFastIntersection
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureusage/preferfastintersection
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/preferfastintersection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureusage/preferfastintersection.json'
content_hash: 'sha256:4886af266aa2ad87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUsage](../mtlaccelerationstructureusage.md)

# preferFastIntersection

<sub>Type Property</sub>

An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var preferFastIntersection: MTLAccelerationStructureUsage { get }
```

## Discussion

The acceleration structures you build with this option can increase their build times.

## See Also

### Applying options

- [MTLAccelerationStructureUsageRefit](refit.md) — An option that lets you update an acceleration structure after creating it.
- [MTLAccelerationStructureUsagePreferFastBuild](preferfastbuild.md) — An option that instructs Metal to build an acceleration structure quickly.
- [MTLAccelerationStructureUsageMinimizeMemory](minimizememory.md) — An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [MTLAccelerationStructureUsageExtendedLimits](extendedlimits.md) — An option that increases an acceleration structure’s storage capacity.
