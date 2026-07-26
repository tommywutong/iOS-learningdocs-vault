---
title: supportsMultipleWindows
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/supportsmultiplewindows
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/supportsmultiplewindows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/supportsmultiplewindows.json'
content_hash: 'sha256:4588be6ca9e28b9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# supportsMultipleWindows

<sub>Instance Property</sub>

A Boolean value that indicates whether the current platform supports opening multiple windows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var supportsMultipleWindows: Bool { get }
```

## Discussion

Read this property from the environment to determine if your app can use the [openWindow](openwindow.md) action to open new windows:

```swift
struct NewMailViewerButton: View {
    @Environment(\.supportsMultipleWindows) private var supportsMultipleWindows
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Open New Window") {
            openWindow(id: "mail-viewer")
        }
        .disabled(!supportsMultipleWindows)
    }
}
```

The reported value depends on both the platform and how you configure your app:

- In macOS, this property returns `true` for any app that uses the SwiftUI app lifecycle.
- In iPadOS, this property returns `true` for any app that uses the SwiftUI app lifecycle and has the Information Property List key [UIApplicationSupportsMultipleScenes](../../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) set to `true`.
- For all other platforms and configurations, the value returns `false`.

If the value is false and you try to open a window, SwiftUI ignores the action and logs a runtime error.

## See Also

### Opening windows

- [Presenting windows and spaces](../../visionos/presenting-windows-and-spaces.md) — Open and close the scenes that make up your app’s interface.
- [openWindow](openwindow.md) — A window presentation action stored in a view’s environment.
- [OpenWindowAction](../openwindowaction.md) — An action that presents a window.
- [PushWindowAction](../pushwindowaction.md) — An action that opens the requested window in place of the window the action is called from.
