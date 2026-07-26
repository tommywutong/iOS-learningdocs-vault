---
title: NSHostingSizingOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingsizingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingsizingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingsizingoptions.json'
content_hash: 'sha256:00dd6c1b07d8e8af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSHostingSizingOptions

<sub>Structure</sub>

Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.

<sub>macOS</sub>

```swift
struct NSHostingSizingOptions
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Geting sizing options

- [intrinsicContentSize](nshostingsizingoptions/intrinsiccontentsize.md) — The hosting view creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting view’s `intrinsicContentSize`.
- [maxSize](nshostingsizingoptions/maxsize.md) — The hosting view creates and updates constraints that represent its content’s maximum size.
- [minSize](nshostingsizingoptions/minsize.md) — The hosting view creates and updates constraints that represent its content’s minimum size.
- [preferredContentSize](nshostingsizingoptions/preferredcontentsize.md) — The hosting controller creates and updates constraints that represent its content’s ideal size. These constraints in turn influence the hosting controller’s `preferredContentSize`.
- [standardBounds](nshostingsizingoptions/standardbounds.md) — The hosting view creates constraints for its minimum, ideal, and maximum sizes.

### Creating a sizing option

- [init(rawValue:)](<nshostingsizingoptions/init(rawvalue_).md>) — Creates a new options from a raw value.
- [rawValue](nshostingsizingoptions/rawvalue.md) — The raw value.

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](nshostingcontroller.md) — An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](nshostingview.md) — An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](nshostingmenu.md) — An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSceneRepresentation](nshostingscenerepresentation.md) — An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md) — Options for how hosting views and controllers manage aspects of the associated window.
