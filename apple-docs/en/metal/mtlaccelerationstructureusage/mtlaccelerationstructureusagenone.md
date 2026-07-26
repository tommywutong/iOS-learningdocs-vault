---
title: MTLAccelerationStructureUsageNone
framework: Metal
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlaccelerationstructureusage/mtlaccelerationstructureusagenone
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage/mtlaccelerationstructureusagenone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructureusage/mtlaccelerationstructureusagenone.json'
content_hash: 'sha256:7287037e82ecaffe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureUsage](../mtlaccelerationstructureusage.md)

# MTLAccelerationStructureUsageNone

<sub>Enumeration Case</sub>

A sentinel value the represents an empty set of options, which is the default behavior for building new acceleration structures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
MTLAccelerationStructureUsageNone
```

## See Also

### Applying options

- [MTLAccelerationStructureUsageRefit](refit.md) — An option that lets you update an acceleration structure after creating it.
- [MTLAccelerationStructureUsagePreferFastBuild](preferfastbuild.md) — An option that instructs Metal to build an acceleration structure quickly.
- [MTLAccelerationStructureUsagePreferFastIntersection](preferfastintersection.md) — An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [MTLAccelerationStructureUsageMinimizeMemory](minimizememory.md) — An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [MTLAccelerationStructureUsageExtendedLimits](extendedlimits.md) — An option that increases an acceleration structure’s storage capacity.
