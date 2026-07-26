---
title: sceneBridgingOptions
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nshostingcontroller/scenebridgingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingcontroller/scenebridgingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingcontroller/scenebridgingoptions.json'
content_hash: 'sha256:aa18765004c2e488'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingController](../nshostingcontroller.md)

# sceneBridgingOptions

<sub>Instance Property</sub>

The options for which aspects of the window will be managed by this controller’s hosting view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }
```

## Discussion

`NSHostingController` will populate certain aspects of its associated window, depending on which options are specified.

For example, a hosting controller can manage its window’s toolbar by including the `.toolbars` option:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                MyToolbarContent()
            }
    }
}

let controller = NSHostingController(rootView: RootView())
controller.sceneBridgingOptions = [.toolbars]
```

When this hosting controller is set as the `contentViewController` for a window, the default value for this property will be `.all`, which includes the options for `.toolbars` and `.title`. Otherwise, the default value is `[]`.

## See Also

### Configuring the controller

- [sizeThatFits(in:)](<sizethatfits(in_).md>) — Calculates and returns the most appropriate size for the current view.
- [preferredContentSize](preferredcontentsize.md)
- [sizingOptions](sizingoptions.md) — The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [safeAreaRegions](safearearegions.md) — The safe area regions that this view controller adds to its view.
