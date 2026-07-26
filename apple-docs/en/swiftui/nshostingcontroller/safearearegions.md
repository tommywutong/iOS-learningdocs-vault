---
title: safeAreaRegions
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.3+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingcontroller/safearearegions
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingcontroller/safearearegions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingcontroller/safearearegions.json'
content_hash: 'sha256:5d5075068cdd487f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingController](../nshostingcontroller.md)

# safeAreaRegions

<sub>Instance Property</sub>

The safe area regions that this view controller adds to its view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency var safeAreaRegions: SafeAreaRegions { get set }
```

## Discussion

The default value is `SafeAreaRegions.all`.

## See Also

### Configuring the controller

- [sizeThatFits(in:)](<sizethatfits(in_).md>) — Calculates and returns the most appropriate size for the current view.
- [preferredContentSize](preferredcontentsize.md)
- [sizingOptions](sizingoptions.md) — The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [sceneBridgingOptions](scenebridgingoptions.md) — The options for which aspects of the window will be managed by this controller’s hosting view.
