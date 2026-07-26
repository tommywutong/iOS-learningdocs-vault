---
title: 'init(windowID:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowvisibilitytoggle/init(windowid:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowvisibilitytoggle/init(windowid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowvisibilitytoggle/init%28windowid%3A%29.json'
content_hash: 'sha256:f89d3e2dc65031a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowVisibilityToggle](../windowvisibilitytoggle.md)

# init(windowID:)

<sub>Initializer</sub>

Create a window visibility toggle to alter the visibility of a specific window.

<sub>macOS</sub>

```swift
nonisolated init(windowID: String) where Label == DefaultWindowVisibilityToggleLabel
```

## Parameters

- `windowID` — The `id` of the singleton window type that should be toggled. If this is not a valid id, the toggle will be disabled and non-functional.
