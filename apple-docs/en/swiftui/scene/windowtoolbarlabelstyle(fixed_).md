---
title: 'windowToolbarLabelStyle(fixed:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/windowtoolbarlabelstyle(fixed:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/windowtoolbarlabelstyle(fixed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/windowtoolbarlabelstyle%28fixed%3A%29.json'
content_hash: 'sha256:90bde1f786dd44c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# windowToolbarLabelStyle(fixed:)

<sub>Instance Method</sub>

Sets the label style of items in a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func windowToolbarLabelStyle(fixed: ToolbarLabelStyle) -> some Scene

```

## Parameters

- `fixed` — The toolbar label style to apply.

## Discussion

Use this modifier to set a static [ToolbarLabelStyle](../toolbarlabelstyle.md) the toolbar should use. The style will not be configurable by the user.

```swift
    @main
    struct MyApp: App {
        var body: some Scene {
            WindowGroup {
                ContentView()
                    .toolbar(id: "browserToolbar") {
                        ...
                    }
            }
            .windowToolbarLabelStyle(fixed: .iconOnly)
        }
    }
```

## See Also

### Styling the associated toolbar

- [windowToolbarStyle(_:)](<windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [windowToolbarLabelStyle(_:)](<windowtoolbarlabelstyle(__).md>) — Sets the label style of items in a toolbar and enables user customization.
- [WindowToolbarStyle](../windowtoolbarstyle.md) — A specification for the appearance and behavior of a window’s toolbar.
