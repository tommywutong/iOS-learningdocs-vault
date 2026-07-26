---
title: SearchToolbarBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchtoolbarbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/searchtoolbarbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchtoolbarbehavior.json'
content_hash: 'sha256:e2059d27fb19e1f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SearchToolbarBehavior

<sub>Structure</sub>

The behavior of a search field in a toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SearchToolbarBehavior
```

## Overview

Use this type in combination with the [searchToolbarBehavior(_:)](<view/searchtoolbarbehavior(__).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [automatic](searchtoolbarbehavior/automatic.md) — The automatic behavior.
- [minimize](searchtoolbarbehavior/minimize.md) — A search toolbar behavior that prefers rendering a search field as a button-like control.

## See Also

### Populating a customizable toolbar

- [toolbar(id:content:)](<view/toolbar(id_content_).md>) — Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [toolbarItemHidden(_:)](<view/toolbaritemhidden(__).md>) — Hides an individual view within a control group toolbar item.
- [CustomizableToolbarContent](customizabletoolbarcontent.md) — Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md) — The customization behavior of customizable toolbar content.
- [ToolbarCustomizationOptions](toolbarcustomizationoptions.md) — Options that influence the default customization behavior of customizable toolbar content.
