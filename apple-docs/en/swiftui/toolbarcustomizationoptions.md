---
title: ToolbarCustomizationOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarcustomizationoptions
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcustomizationoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcustomizationoptions.json'
content_hash: 'sha256:d2f6e7a75d3b155f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ToolbarCustomizationOptions

<sub>Structure</sub>

Options that influence the default customization behavior of customizable toolbar content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ToolbarCustomizationOptions
```

## Overview

Use this type in conjunction with the [defaultCustomization(_:options:)](<customizabletoolbarcontent/defaultcustomization(__options_).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting customization options

- [alwaysAvailable](toolbarcustomizationoptions/alwaysavailable.md) — Configures default customizable toolbar content to always be present in the toolbar.

## See Also

### Populating a customizable toolbar

- [toolbar(id:content:)](<view/toolbar(id_content_).md>) — Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [toolbarItemHidden(_:)](<view/toolbaritemhidden(__).md>) — Hides an individual view within a control group toolbar item.
- [CustomizableToolbarContent](customizabletoolbarcontent.md) — Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md) — The customization behavior of customizable toolbar content.
- [SearchToolbarBehavior](searchtoolbarbehavior.md) — The behavior of a search field in a toolbar.
