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
doc_path: /documentation/swiftui/nshostingview/scenebridgingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/scenebridgingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/scenebridgingoptions.json'
content_hash: 'sha256:7c08f2acc3d5a7b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

# sceneBridgingOptions

<sub>Instance Property</sub>

The options for which aspects of the window will be managed by this hosting view.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }
```

## Discussion

`NSHostingView` will populate certain aspects of its associated window, depending on which options are specified.

For example, a hosting view can manage its window’s toolbar by including the `.toolbars` option:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                MyToolbarContent()
            }
    }
}

let view = NSHostingView(rootView: RootView())
view.sceneBridgingOptions = [.toolbars]
```

When this hosting view is set as the `contentView` for a window, the default value for this property will be `.all`, which includes the options for `.toolbars` and `.title`. Otherwise, the default value is `[]`.
