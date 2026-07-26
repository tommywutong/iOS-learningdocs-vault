---
title: ControlGroup
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlgroup
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroup.json'
content_hash: 'sha256:bcb46953144e6b54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ControlGroup

<sub>Structure</sub>

A container view that displays semantically-related controls in a visually-appropriate manner for the context

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated struct ControlGroup<Content> where Content : View
```

## Overview

You can provide an optional label to this view that describes its children. This view may be used in different ways depending on the surrounding context. For example, when you place the control group in a toolbar item, SwiftUI uses the label when the group is moved to the toolbar’s overflow menu.

```swift
ContentView()
    .toolbar(id: "items") {
        ToolbarItem(id: "media") {
            ControlGroup {
                MediaButton()
                ChartButton()
                GraphButton()
            } label: {
                Label("Plus", systemImage: "plus")
            }
        }
    }
```

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a control group

- [init(content:)](<controlgroup/init(content_).md>) — Creates a new ControlGroup with the specified children
- [init(content:label:)](<controlgroup/init(content_label_).md>) — Creates a new control group with the specified content and a label.
- [init(_:content:)](<controlgroup/init(__content_).md>) — Creates a new control group with the specified content that generates its label from a string.

### Creating a control group with an image

- [init(_:image:content:)](<controlgroup/init(__image_content_).md>) — Creates a new control group with the specified content that generates its label from a localized string resource and image resource.
- [init(_:systemImage:content:)](<controlgroup/init(__systemimage_content_).md>) — Creates a new control group with the specified content that generates its label from a string and image name.

### Creating a configured control group

- [init(_:)](<controlgroup/init(__).md>) — Creates a control group based on a style configuration.

### Supporting types

- [LabeledControlGroupContent](labeledcontrolgroupcontent.md) — A view that represents the body of a control group with a specified label.

## See Also

### Presenting a group of controls

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
