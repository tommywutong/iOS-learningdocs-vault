---
title: NSHostingController
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingcontroller
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingcontroller.json'
content_hash: 'sha256:ff4c24a7316d42cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NSHostingController

<sub>Class</sub>

An AppKit view controller that hosts SwiftUI view hierarchy.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency class NSHostingController<Content> where Content : View
```

## Overview

Create an `NSHostingController` object when you want to integrate SwiftUI views into an AppKit view hierarchy. At creation time, specify the SwiftUI view you want to use as the root view for this view controller; you can change that view later using the [rootView](nshostingcontroller/rootview.md) property. Use the hosting controller like you would any other view controller, by presenting it or embedding it as a child view controller in your interface.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)

## Topics

### Creating a hosting controller object

- [init(rootView:)](<nshostingcontroller/init(rootview_).md>) — Creates a hosting controller object that wraps the specified SwiftUI view.
- [init(coder:rootView:)](<nshostingcontroller/init(coder_rootview_).md>) — Creates a hosting controller object from an archive and the specified SwiftUI view.
- [init(coder:)](<nshostingcontroller/init(coder_).md>) — Creates a hosting controller object from the contents of the specified archive.

### Getting the root view

- [rootView](nshostingcontroller/rootview.md) — The root view of the SwiftUI view hierarchy managed by this view controller.
- [identifier](nshostingcontroller/identifier.md)

### Configuring the controller

- [sizeThatFits(in:)](<nshostingcontroller/sizethatfits(in_).md>) — Calculates and returns the most appropriate size for the current view.
- [preferredContentSize](nshostingcontroller/preferredcontentsize.md)
- [sizingOptions](nshostingcontroller/sizingoptions.md) — The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [safeAreaRegions](nshostingcontroller/safearearegions.md) — The safe area regions that this view controller adds to its view.
- [sceneBridgingOptions](nshostingcontroller/scenebridgingoptions.md) — The options for which aspects of the window will be managed by this controller’s hosting view.

## See Also

### Displaying SwiftUI views in AppKit

- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [NSHostingView](nshostingview.md) — An AppKit view that hosts a SwiftUI view hierarchy.
- [NSHostingMenu](nshostingmenu.md) — An AppKit menu with menu items that are defined by a SwiftUI View.
- [NSHostingSizingOptions](nshostingsizingoptions.md) — Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [NSHostingSceneRepresentation](nshostingscenerepresentation.md) — An AppKit type that hosts and can present SwiftUI scenes
- [NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md) — Options for how hosting views and controllers manage aspects of the associated window.
