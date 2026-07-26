---
title: 'navigationBarItems(leading:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/navigationbaritems(leading:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationbaritems(leading:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationbaritems%28leading%3A%29.json'
content_hash: 'sha256:5a52091dd0b1a32f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationBarItems(leading:)

<sub>Instance Method</sub>

Sets the navigation bar items for this view.

> [!warning] Deprecated
> Use [toolbar(content:)](<toolbar(content_)-5w0tj.md>) with [navigationBarLeading](../toolbaritemplacement/navigationbarleading.md) placement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func navigationBarItems<L>(leading: L) -> some View where L : View

```

## Parameters

- `leading` — A view that appears on the leading edge of the title.

## Discussion

Use `navigationBarItems(leading:)` to add navigation bar items to the leading edge of the navigation bar for this view.

This modifier only takes effect when this view is inside of and visible within a [NavigationView](../navigationview.md).

On iOS 14 and later, the leading item supplements a visible back button, instead of replacing it, by default. To hide the back button, use [navigationBarBackButtonHidden(_:)](<navigationbarbackbuttonhidden(__).md>).

The example below adds buttons to the leading edge of the button area of the navigation view:

```swift
struct FlavorView: View {
    var body: some View {
        NavigationView {
            List {
                Text("Chocolate")
                Text("Vanilla")
                Text("Strawberry")
            }
            .navigationBarTitle(Text("Today's Flavors"))
            .navigationBarItems(leading:
                HStack {
                    Button("Hours") {
                        print("Hours tapped!")
                    }

                    Button("Help") {
                        print("Help tapped!")
                    }
                }
            )
        }
    }
}
```

## See Also

### Auxiliary view modifiers

- [navigationBarTitle(_:)](<navigationbartitle(__).md>) — Sets the title in the navigation bar for this view. _(deprecated)_
- [navigationBarTitle(_:displayMode:)](<navigationbartitle(__displaymode_).md>) — Sets the title and display mode in the navigation bar for this view. _(deprecated)_
- [navigationBarItems(leading:trailing:)](<navigationbaritems(leading_trailing_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(trailing:)](<navigationbaritems(trailing_).md>) — Configures the navigation bar items for this view. _(deprecated)_
- [navigationBarHidden(_:)](<navigationbarhidden(__).md>) — Hides the navigation bar for this view. _(deprecated)_
- [statusBar(hidden:)](<statusbar(hidden_).md>) — Sets the visibility of the status bar. _(deprecated)_
- [contextMenu(_:)](<contextmenu(__).md>) — Adds a context menu to the view. _(deprecated)_
