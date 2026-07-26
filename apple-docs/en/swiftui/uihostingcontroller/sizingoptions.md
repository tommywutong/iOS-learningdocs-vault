---
title: sizingOptions
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingcontroller/sizingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/sizingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/sizingoptions.json'
content_hash: 'sha256:507dd9d317b498da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# sizingOptions

<sub>Instance Property</sub>

The options for how the hosting controller tracks changes to the size of its SwiftUI content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var sizingOptions: UIHostingControllerSizingOptions { get set }
```

## Discussion

The default value is the empty set.

## See Also

### Managing the size

- [preferredContentSizeDidChange(forChildContentContainer:)](<preferredcontentsizedidchange(forchildcontentcontainer_).md>)
- [sizeThatFits(in:)](<sizethatfits(in_).md>) — Calculates and returns the most appropriate size for the current view.
- [safeAreaRegions](safearearegions.md) — The safe area regions that this view controller adds to its view.
