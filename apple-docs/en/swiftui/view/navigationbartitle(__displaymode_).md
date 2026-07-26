---
title: 'navigationBarTitle(_:displayMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/navigationbartitle(_:displaymode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:displaymode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationbartitle%28_%3Adisplaymode%3A%29.json'
content_hash: 'sha256:3f06c12dc8e357f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationBarTitle(_:displayMode:)

<sub>Instance Method</sub>

Sets the title and display mode in the navigation bar for this view.

> [!warning] Deprecated
> Use [navigationTitle(_:)](<navigationtitle(__)-5di1u.md>) with [navigationBarTitleDisplayMode(_:)](<navigationbartitledisplaymode(__).md>).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated func navigationBarTitle(_ title: Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View

```

## Parameters

- `title` — A title for this view to display in the navigation bar.

- `displayMode` — The style to use for displaying the navigation bar title.

## Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation bar for this view and specify a display mode for the title from one of the [TitleDisplayMode](../navigationbaritem/titledisplaymode.md) styles. This modifier only takes effect when this view is inside of and visible within a [NavigationView](../navigationview.md).

In the example below, text for the navigation bar title is provided using a [Text](../text.md) view. The navigation bar title’s [TitleDisplayMode](../navigationbaritem/titledisplaymode.md) is set to `.inline` which places the navigation bar title in the bounds of the navigation bar.

```swift
struct FlavorView: View {
   let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                "Pistachio"]
   var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle(Text("Today's Flavors", displayMode: .inline))
        }
    }
}
```

## See Also

### Auxiliary view modifiers

- [navigationBarTitle(_:)](<navigationbartitle(__).md>) — Sets the title in the navigation bar for this view. _(deprecated)_
- [navigationBarItems(leading:)](<navigationbaritems(leading_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(leading:trailing:)](<navigationbaritems(leading_trailing_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(trailing:)](<navigationbaritems(trailing_).md>) — Configures the navigation bar items for this view. _(deprecated)_
- [navigationBarHidden(_:)](<navigationbarhidden(__).md>) — Hides the navigation bar for this view. _(deprecated)_
- [statusBar(hidden:)](<statusbar(hidden_).md>) — Sets the visibility of the status bar. _(deprecated)_
- [contextMenu(_:)](<contextmenu(__).md>) — Adds a context menu to the view. _(deprecated)_
