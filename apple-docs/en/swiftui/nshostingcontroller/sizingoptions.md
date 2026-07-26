---
title: sizingOptions
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingcontroller/sizingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingcontroller/sizingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingcontroller/sizingoptions.json'
content_hash: 'sha256:c0685de58ad2c865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingController](../nshostingcontroller.md)

# sizingOptions

<sub>Instance Property</sub>

The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency var sizingOptions: NSHostingSizingOptions { get set }
```

## Discussion

NSHostingController can create minimum, maximum, and ideal (content size) constraints that are derived from its SwiftUI view content. These constraints are only created when Auto Layout constraints are otherwise being used in the containing window.

If the NSHostingController is set as the `contentViewController` of an `NSWindow`, it will also update the window’s `contentMinSize` and `contentMaxSize` based on the minimum and maximum size of its SwiftUI content.

`sizingOptions` defaults to `.standardBounds` (which includes `minSize`, `intrinsicContentSize`, and `maxSize`), but can be set to an explicit value to control this behavior. For instance, setting a value of `.minSize` will only create the constraints necessary to maintain the minimum size of the SwiftUI content, or setting a value of `[]` will create no constraints at all.

If a use case can make assumptions about the size of the `NSHostingController` relative to its displayed content, such as the always being displayed in a fixed frame, setting this to a value with fewer options can improve performance as it reduces the amount of layout measurements that need to be performed. If an `NSHostingController` has a `frame` that is smaller or larger than that required to display its SwiftUI content, the content will be centered within that frame.

## See Also

### Configuring the controller

- [sizeThatFits(in:)](<sizethatfits(in_).md>) — Calculates and returns the most appropriate size for the current view.
- [preferredContentSize](preferredcontentsize.md)
- [safeAreaRegions](safearearegions.md) — The safe area regions that this view controller adds to its view.
- [sceneBridgingOptions](scenebridgingoptions.md) — The options for which aspects of the window will be managed by this controller’s hosting view.
