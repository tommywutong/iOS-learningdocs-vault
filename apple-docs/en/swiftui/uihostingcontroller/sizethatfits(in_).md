---
title: 'sizeThatFits(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingcontroller/sizethatfits(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/sizethatfits(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/sizethatfits%28in%3A%29.json'
content_hash: 'sha256:c850058cf2df16cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# sizeThatFits(in:)

<sub>Instance Method</sub>

Calculates and returns the most appropriate size for the current view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func sizeThatFits(in size: CGSize) -> CGSize
```

## Parameters

- `size` — The proposed new size for the view.

## Return Value

The size that offers the best fit for the root view and its contents.

## See Also

### Managing the size

- [sizingOptions](sizingoptions.md) — The options for how the hosting controller tracks changes to the size of its SwiftUI content.
- [preferredContentSizeDidChange(forChildContentContainer:)](<preferredcontentsizedidchange(forchildcontentcontainer_).md>)
- [safeAreaRegions](safearearegions.md) — The safe area regions that this view controller adds to its view.
