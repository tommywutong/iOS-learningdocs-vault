---
title: ToolbarCustomizationBehavior
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarcustomizationbehavior
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcustomizationbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcustomizationbehavior.json'
content_hash: 'sha256:11c41d5cbe9f79c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarCustomizationBehavior

<sub>Structure</sub>

The customization behavior of customizable toolbar content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarCustomizationBehavior
```

## Overview

Customizable toolbar content support different types of customization behaviors. For example, some customizable content may not be removed by the user. Some content may be placed in a toolbar that supports customization overall, but not for that particular content.

Use this type in conjunction with the [customizationBehavior(_:)](<customizabletoolbarcontent/customizationbehavior(__).md>) modifier.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting customization behaviors

- [default](toolbarcustomizationbehavior/default.md) — The default customization behavior.
- [disabled](toolbarcustomizationbehavior/disabled.md) — The disabled customization behavior.
- [reorderable](toolbarcustomizationbehavior/reorderable.md) — The reorderable customization behavior.

## See Also

### Populating a customizable toolbar

- [toolbar(id:content:)](<view/toolbar(id_content_).md>) — Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [toolbarItemHidden(_:)](<view/toolbaritemhidden(__).md>) — Hides an individual view within a control group toolbar item.
- [CustomizableToolbarContent](customizabletoolbarcontent.md) — Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [ToolbarCustomizationOptions](toolbarcustomizationoptions.md) — Options that influence the default customization behavior of customizable toolbar content.
- [SearchToolbarBehavior](searchtoolbarbehavior.md) — The behavior of a search field in a toolbar.
