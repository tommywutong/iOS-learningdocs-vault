---
title: alwaysAvailable
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbarcustomizationoptions/alwaysavailable
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarcustomizationoptions/alwaysavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarcustomizationoptions/alwaysavailable.json'
content_hash: 'sha256:4ff47a53210ab24c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarCustomizationOptions](../toolbarcustomizationoptions.md)

# alwaysAvailable

<sub>Type Property</sub>

Configures default customizable toolbar content to always be present in the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var alwaysAvailable: ToolbarCustomizationOptions { get }
```

## Discussion

In iOS, default customizable toolbar content have the option of always being available in the toolbar regardless of the customization status of the user. These items will always be in the overflow menu of the toolbar. Users can customize whether the items are present as controls in the toolbar itself but will still always be able to access the item if they remove it from the toolbar itself.

Consider using this for items that users should always be able to access, but may not be important enough to always occupy space in the toolbar itself.
