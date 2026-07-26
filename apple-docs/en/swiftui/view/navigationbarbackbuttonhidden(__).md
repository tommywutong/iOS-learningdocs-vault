---
title: 'navigationBarBackButtonHidden(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 13.0+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationbarbackbuttonhidden(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationbarbackbuttonhidden(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationbarbackbuttonhidden%28_%3A%29.json'
content_hash: 'sha256:1c8f073d477e68c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationBarBackButtonHidden(_:)

<sub>Instance Method</sub>

Hides the navigation bar back button for the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func navigationBarBackButtonHidden(_ hidesBackButton: Bool = true) -> some View

```

## Parameters

- `hidesBackButton` — A Boolean value that indicates whether to hide the back button. The default value is `true`.

## Discussion

Use `navigationBarBackButtonHidden(_:)` to hide the back button for this view.

This modifier only takes effect when this view is inside of and visible within a [NavigationStack](../navigationstack.md) or a [NavigationSplitView](../navigationsplitview.md) in narrow size classes.

The example below demonstrates how to hide the navigation back button for a view within a navigation stack:

```swift
NavigationStack {
   List {
       NavigationLink("Mint") {
           Color.mint
               .navigationBarBackButtonHidden()
       }
   }
   .navigationTitle("Colors")
}
```

## See Also

### Configuring the navigation bar

- [navigationBarTitleDisplayMode(_:)](<navigationbartitledisplaymode(__).md>) — Configures the title display mode for this view.
- [NavigationBarItem](../navigationbaritem.md) — A configuration for a navigation bar that represents a view at the top of a navigation stack.
