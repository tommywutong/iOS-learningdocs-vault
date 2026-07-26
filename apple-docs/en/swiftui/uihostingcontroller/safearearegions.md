---
title: safeAreaRegions
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, tvOS 16.4+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingcontroller/safearearegions
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/safearearegions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/safearearegions.json'
content_hash: 'sha256:9fd4c70c853698f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# safeAreaRegions

<sub>Instance Property</sub>

The safe area regions that this view controller adds to its view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var safeAreaRegions: SafeAreaRegions { get set }
```

## Discussion

An example of when this is appropriate to use is when hosting content that you know should never be affected by the safe area, such as a custom scrollable container. Disabling a safe area region omits it from the SwiftUI layout system altogether.

The default value is `SafeAreaRegions.all`.

## See Also

### Managing the size

- [sizingOptions](sizingoptions.md) — The options for how the hosting controller tracks changes to the size of its SwiftUI content.
- [preferredContentSizeDidChange(forChildContentContainer:)](<preferredcontentsizedidchange(forchildcontentcontainer_).md>)
- [sizeThatFits(in:)](<sizethatfits(in_).md>) — Calculates and returns the most appropriate size for the current view.
