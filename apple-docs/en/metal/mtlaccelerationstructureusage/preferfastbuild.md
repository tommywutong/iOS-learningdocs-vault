---
title: preferFastBuild
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureusage/preferfastbuild
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/preferfastbuild'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureusage/preferfastbuild.json'
content_hash: 'sha256:7aab786051004b50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUsage](../mtlaccelerationstructureusage.md)

# preferFastBuild

<sub>Type Property</sub>

An option that instructs Metal to build an acceleration structure quickly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var preferFastBuild: MTLAccelerationStructureUsage { get }
```

## Discussion

Apply this option when you need to reduce the time when creating or refitting an acceleration structure, such as from code that’s sensitive to runtime performance.

> [!note] Note
> The acceleration structures you build with this option can reduce their intersection performance.

## See Also

### Applying options

- [MTLAccelerationStructureUsageRefit](refit.md) — An option that lets you update an acceleration structure after creating it.
- [MTLAccelerationStructureUsagePreferFastIntersection](preferfastintersection.md) — An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [MTLAccelerationStructureUsageMinimizeMemory](minimizememory.md) — An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [MTLAccelerationStructureUsageExtendedLimits](extendedlimits.md) — An option that increases an acceleration structure’s storage capacity.
