---
title: systemPrefersReducedResourceUsageDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiapplication/systemprefersreducedresourceusagedidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/systemprefersreducedresourceusagedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/systemprefersreducedresourceusagedidchangenotification.json'
content_hash: 'sha256:81e4cf5a482d468e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# systemPrefersReducedResourceUsageDidChangeNotification

<sub>Type Property</sub>

A notification that posts when [systemPrefersReducedResourceUsage](systemprefersreducedresourceusage.md) changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let systemPrefersReducedResourceUsageDidChangeNotification: NSNotification.Name
```

## Discussion

The object of the notification is the `UIApplication` object. The `userInfo` dictionary is empty. Re-read `systemPrefersReducedResourceUsage` to get the new value.

Use this notification to re-read the value and adjust the scheduling of future work, the same way the property is read proactively. Avoid performing or scheduling expensive work directly in the handler, as this could worsen resource usage.
