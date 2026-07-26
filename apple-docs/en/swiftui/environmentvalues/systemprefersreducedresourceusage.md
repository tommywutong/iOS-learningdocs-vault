---
title: systemPrefersReducedResourceUsage
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/systemprefersreducedresourceusage
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/systemprefersreducedresourceusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/systemprefersreducedresourceusage.json'
content_hash: 'sha256:4c93e94efea2d06e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# systemPrefersReducedResourceUsage

<sub>Instance Property</sub>

A boolean value indicating whether the system would prefer the app to reduce its overall resource usage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var systemPrefersReducedResourceUsage: Bool { get set }
```

## Discussion

When this value is `true`, the system has entered a state where it would prefer apps to scale back resource-intensive work. The default value is `false`.

Use this to avoid or reduce expensive work. For example:

- Gate or simplify resource-intensive UI, such as 3D or AR viewers, advanced camera modes, or live effects.
- Choose lighter-weight paths, such as lower-resolution assets or fewer simultaneous operations.
- Defer or shrink non-essential background work, such as prefetching or precomputation.

Avoid performing or scheduling expensive work in response to changes in this property, as this could worsen resource usage.

> [!tip] Tip
> For in-memory caching, consider using `NSCache` with `NSPurgeableData`, which automatically evicts entries under system memory pressure. Use `systemPrefersReducedResourceUsage` for higher-level decisions that `NSCache` cannot make on its own.
