---
title: alwaysByFew
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/viewalignedscrolltargetbehavior/limitbehavior/alwaysbyfew
source_url: 'https://developer.apple.com/documentation/swiftui/viewalignedscrolltargetbehavior/limitbehavior/alwaysbyfew'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/viewalignedscrolltargetbehavior/limitbehavior/alwaysbyfew.json'
content_hash: 'sha256:cb3ee13ed6d786ab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [ViewAlignedScrollTargetBehavior](../../viewalignedscrolltargetbehavior.md) · [LimitBehavior](../limitbehavior.md)

# alwaysByFew

<sub>Type Property</sub>

The always-by-few limit behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var alwaysByFew: ViewAlignedScrollTargetBehavior.LimitBehavior { get }
```

## Discussion

Limit the number of views that can be scrolled by a single interaction to a small number of views, rather than a single view at a time. The number of views is determined automatically.
