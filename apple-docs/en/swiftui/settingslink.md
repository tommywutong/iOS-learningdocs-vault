---
title: SettingsLink
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/settingslink
source_url: 'https://developer.apple.com/documentation/swiftui/settingslink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/settingslink.json'
content_hash: 'sha256:13a8a9887f9c4860'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SettingsLink

<sub>Structure</sub>

A view that opens the Settings scene defined by an app.

<sub>macOS</sub>

```swift
nonisolated struct SettingsLink<Label> where Label : View
```

## Overview

On macOS, clicking on the link opens the window for the scene or orders it to the front if it is already open.

## Relationships

- **Conforms To**: [View](view.md)

## Topics

### Creating a settings link

- [init()](<settingslink/init().md>) — Creates a settings link with the default system label.
- [init(label:)](<settingslink/init(label_).md>) — Creates a settings link with a custom label.

### Supporting types

- [DefaultSettingsLinkLabel](defaultsettingslinklabel.md) — The default label to use for a settings link.

## See Also

### Managing a settings window

- [Settings](settings.md) — A scene that presents an interface for viewing and modifying an app’s settings.
- [OpenSettingsAction](opensettingsaction.md) — An action that presents the settings scene for an app.
- [openSettings](environmentvalues/opensettings.md) — A Settings presentation action stored in a view’s environment.
