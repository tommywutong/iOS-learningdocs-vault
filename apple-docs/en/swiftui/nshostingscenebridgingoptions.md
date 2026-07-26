---
title: NSHostingSceneBridgingOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingscenebridgingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingscenebridgingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingscenebridgingoptions.json'
content_hash: 'sha256:1c3b4ac3a713486a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSHostingSceneBridgingOptions

<sub>Structure</sub>

Options for how hosting views and controllers manage aspects of the associated window.

<sub>macOS</sub>

```swift
struct NSHostingSceneBridgingOptions
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Geting bridging options

- [all](nshostingscenebridgingoptions/all.md) — The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.
- [title](nshostingscenebridgingoptions/title.md) — The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.
- [toolbars](nshostingscenebridgingoptions/toolbars.md) — The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.

### Creating a bridging options

- [init(rawValue:)](<nshostingscenebridgingoptions/init(rawvalue_).md>) — Creates a new set from a raw value.
- [rawValue](nshostingscenebridgingoptions/rawvalue.md) — The raw value.

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingController](nshostingcontroller.md) — An AppKit view controller that hosts SwiftUI view hierarchy.
- [NSHostingView](nshostingview.md) — An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](nshostingmenu.md) — An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](nshostingsizingoptions.md) — Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](nshostingscenerepresentation.md) — An AppKit type that hosts and can present SwiftUI scenes
