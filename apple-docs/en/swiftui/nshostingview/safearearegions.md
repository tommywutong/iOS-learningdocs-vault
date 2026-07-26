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
doc_path: /documentation/swiftui/nshostingview/safearearegions
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/safearearegions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/safearearegions.json'
content_hash: 'sha256:f87909ef93d2f6cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

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

### Configuring the view layout behavior

- [requiresConstraintBasedLayout](requiresconstraintbasedlayout.md)
- [userInterfaceLayoutDirection](userinterfacelayoutdirection.md)
- [isFlipped](isflipped.md)
- [layerContentsRedrawPolicy](layercontentsredrawpolicy.md)
- [updateConstraints()](<updateconstraints().md>)
- [layout()](<layout().md>)
