---
title: ToolbarTitleDisplayMode
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbartitledisplaymode
source_url: 'https://developer.apple.com/documentation/swiftui/toolbartitledisplaymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbartitledisplaymode.json'
content_hash: 'sha256:b6883db84b33b078'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarTitleDisplayMode

<sub>Structure</sub>

A type that defines the behavior of title of a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarTitleDisplayMode
```

## Overview

Use the [toolbarTitleDisplayMode(_:)](<view/toolbartitledisplaymode(__).md>) modifier to configure the title display behavior of your toolbar:

```swift
NavigationStack {
    ContentView()
        .toolbarTitleDisplayMode(.inlineLarge)
}
```

## Topics

### Getting display modes

- [automatic](toolbartitledisplaymode/automatic.md) — The automatic mode.
- [inline](toolbartitledisplaymode/inline.md) — The inline mode.
- [inlineLarge](toolbartitledisplaymode/inlinelarge.md) — The inline large mode.
- [large](toolbartitledisplaymode/large.md) — The large mode.

## See Also

### Configuring the toolbar title display mode

- [toolbarTitleDisplayMode(_:)](<view/toolbartitledisplaymode(__).md>) — Configures the toolbar title display mode for this view.
