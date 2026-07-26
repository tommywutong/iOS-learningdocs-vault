---
title: extendedLimits
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureusage/extendedlimits
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/extendedlimits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureusage/extendedlimits.json'
content_hash: 'sha256:f55cea63d67e4183'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUsage](../mtlaccelerationstructureusage.md)

# extendedLimits

<sub>Type Property</sub>

An option that increases an acceleration structure’s storage capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var extendedLimits: MTLAccelerationStructureUsage { get }
```

## Discussion

The acceleration structures you build with this option can affect their performance because they support more data complexity.

|  | Standard limits | Extended limits |
|---|---|---|
| Primitives in primitive acceleration structure | `2^(28)` | `2^(30)` |
| Geometries in primitive acceleration structure | `2^(24)` | `2^(30)` |
| Instances in instance acceleration structure | `2^(24)` | `2^(30)` |
| Visibility mask bits | `8` | `32` |

## See Also

### Applying options

- [MTLAccelerationStructureUsageRefit](refit.md) — An option that lets you update an acceleration structure after creating it.
- [MTLAccelerationStructureUsagePreferFastBuild](preferfastbuild.md) — An option that instructs Metal to build an acceleration structure quickly.
- [MTLAccelerationStructureUsagePreferFastIntersection](preferfastintersection.md) — An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [MTLAccelerationStructureUsageMinimizeMemory](minimizememory.md) — An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
