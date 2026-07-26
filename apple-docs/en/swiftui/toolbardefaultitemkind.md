---
title: ToolbarDefaultItemKind
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbardefaultitemkind
source_url: 'https://developer.apple.com/documentation/swiftui/toolbardefaultitemkind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbardefaultitemkind.json'
content_hash: 'sha256:424653ff43785613'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarDefaultItemKind

<sub>Structure</sub>

A kind of toolbar item a `View` adds by default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarDefaultItemKind
```

## Overview

`View`s can add toolbar items clients may wish to remove or customize. A default item kind can be passed to the [toolbar(removing:)](<view/toolbar(removing_).md>) modifier to remove the item. Documentation on the `View` placing the default item should reference the `ToolbarDefaultItemKind` used to remove the item.

## Topics

### Getting the default item types

- [sidebarToggle](toolbardefaultitemkind/sidebartoggle.md) — The sidebar toggle toolbar item a `NavigationSplitView` adds by default.

### Type Properties

- [search](toolbardefaultitemkind/search.md) — The search item added by a `View/searchable(text:isPresented:placement:prompt)` modifier.
- [title](toolbardefaultitemkind/title.md) — The title and subtitle shown in title bar / navigation bar.

## See Also

### Removing default items

- [toolbar(removing:)](<view/toolbar(removing_).md>) — Remove a toolbar item present by default
