---
title: 'sizeThatFits(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingcontroller/sizethatfits(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingcontroller/sizethatfits(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingcontroller/sizethatfits%28in%3A%29.json'
content_hash: 'sha256:2d33cdf54acd67ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingController](../nshostingcontroller.md)

# sizeThatFits(in:)

<sub>Instance Method</sub>

Calculates and returns the most appropriate size for the current view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency func sizeThatFits(in size: CGSize) -> CGSize
```

## Parameters

- `size` — The proposed new size for the view.

## Return Value

The size that offers the best fit for the root view and its contents.

## See Also

### Configuring the controller

- [preferredContentSize](preferredcontentsize.md)
- [sizingOptions](sizingoptions.md) — The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [safeAreaRegions](safearearegions.md) — The safe area regions that this view controller adds to its view.
- [sceneBridgingOptions](scenebridgingoptions.md) — The options for which aspects of the window will be managed by this controller’s hosting view.
