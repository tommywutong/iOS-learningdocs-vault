---
title: sidebarRowSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/sidebarrowsize
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/sidebarrowsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/sidebarrowsize.json'
content_hash: 'sha256:62d2d6a7235f3389'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# sidebarRowSize

<sub>Instance Property</sub>

The current size of sidebar rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sidebarRowSize: SidebarRowSize { get set }
```

## Discussion

On macOS, reflects the value of the “Sidebar icon size” in System Settings’ Appearance settings.

This can be used to update the content shown in the sidebar in response to this size. And it can be overridden to force a sidebar to a particularly size, regardless of the user preference.

On other platforms, the value is always `.medium` and setting a different value has no effect.

SwiftUI views like `Label` automatically adapt to the sidebar row size.

## See Also

### Configuring the sidebar

- [SidebarRowSize](../sidebarrowsize.md) — The standard sizes of sidebar rows.
