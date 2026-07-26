---
title: systemPrefersReducedResourceUsage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiapplication/systemprefersreducedresourceusage
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/systemprefersreducedresourceusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/systemprefersreducedresourceusage.json'
content_hash: 'sha256:066f5f6eda445fa3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# systemPrefersReducedResourceUsage

<sub>Instance Property</sub>

A Boolean value that indicates whether the system prefers that the app reduce its resource usage.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var systemPrefersReducedResourceUsage: Bool { get }
```

## Discussion

When this value is `YES`, the system has entered a state where it would prefer apps to scale back resource-intensive work.

Use this to avoid or reduce expensive work. For example:

- Gate or simplify resource-intensive UI, such as 3D or AR viewers, advanced camera modes, or live effects.
- Choose lighter-weight paths, such as lower-resolution assets or fewer simultaneous operations.
- Defer or shrink non-essential background work, such as prefetching or precomputation.

Avoid performing or scheduling expensive work in response to changes in this property, as this could worsen resource usage.

> [!tip] Tip
> For in-memory caching, consider using `NSCache` with `NSPurgeableData`, which automatically evicts entries under system memory pressure. Use `systemPrefersReducedResourceUsage` for higher-level decisions that `NSCache` cannot make on its own.

To respond to changes in views, read the `UITraitCollection/systemPrefersReducedResourceUsage` trait. From other contexts, observe [UIApplicationSystemPrefersReducedResourceUsageDidChangeNotification](systemprefersreducedresourceusagedidchangenotification.md) and re-read this property.
