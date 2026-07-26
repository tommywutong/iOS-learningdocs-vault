---
title: ToolbarRole
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarrole
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarrole'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarrole.json'
content_hash: 'sha256:f8ddab10c8c0f0bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarRole

<sub>Structure</sub>

The purpose of content that populates the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarRole
```

## Overview

A toolbar role provides a description of the purpose of content that populates the toolbar. The purpose of the content influences how a toolbar renders its content. For example, a [browser](toolbarrole/browser.md) will automatically leading align the title of a toolbar in iPadOS.

Provide this type to the [toolbarRole(_:)](<view/toolbarrole(__).md>) modifier:

```swift
ContentView()
    .navigationTitle("Browser")
    .toolbarRole(.browser)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            AddButton()
        }
     }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Behavior-specific roles

- [browser](toolbarrole/browser.md) — The browser role.
- [editor](toolbarrole/editor.md) — The editor role.
- [navigationStack](toolbarrole/navigationstack.md) — The navigationStack role.

### Automatic roles

- [automatic](toolbarrole/automatic.md) — The automatic role.

## See Also

### Specifying the role of toolbar content

- [toolbarRole(_:)](<view/toolbarrole(__).md>) — Configures the semantic role for the content populating the toolbar.
