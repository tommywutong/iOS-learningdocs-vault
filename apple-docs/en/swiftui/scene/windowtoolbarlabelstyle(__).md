---
title: 'windowToolbarLabelStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowtoolbarlabelstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowtoolbarlabelstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowtoolbarlabelstyle%28_%3A%29.json'
content_hash: 'sha256:79eff689e72693d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowToolbarLabelStyle(_:)

<sub>Instance Method</sub>

Sets the label style of items in a toolbar and enables user customization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func windowToolbarLabelStyle(_ toolbarLabelStyle: Binding<ToolbarLabelStyle>) -> some Scene

```

## Parameters

- `toolbarLabelStyle` — The label style to apply.

## Discussion

Use this modifier to bind a [ToolbarLabelStyle](../toolbarlabelstyle.md) to [AppStorage](../appstorage.md). The toolbar will default to the label style specified but will also be user configurable.

```swift
    @main
    struct MyApp: App {
        @AppStorage("ToolbarLabelStyle")
        private var labelStyle: ToolbarLabelStyle = .iconOnly

        var body: some Scene {
            WindowGroup {
                ContentView()
                    .toolbar(id: "browserToolbar") {
                        ...
                    }
            }
            .windowToolbarLabelStyle($labelStyle)
        }
    }
```

## See Also

### Styling the associated toolbar

- [windowToolbarStyle(_:)](<windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [windowToolbarLabelStyle(fixed:)](<windowtoolbarlabelstyle(fixed_).md>) — Sets the label style of items in a toolbar.
- [WindowToolbarStyle](../windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
