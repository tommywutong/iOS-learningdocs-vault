---
title: menuIndicatorVisibility
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/menuindicatorvisibility
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/menuindicatorvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/menuindicatorvisibility.json'
content_hash: 'sha256:b73b0b648354f0cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# menuIndicatorVisibility

<sub>Instance Property</sub>

The menu indicator visibility to apply to controls within a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var menuIndicatorVisibility: Visibility { get set }
```

## Discussion

> [!note] Note
> On tvOS, the standard button styles do not include a menu indicator, so this modifier will have no effect when using a built-in button style. You can implement an indicator in your own [ButtonStyle](../buttonstyle.md) implementation by checking the value of this environment value.

## See Also

### Showing a menu indicator

- [menuIndicator(_:)](<../view/menuindicator(__).md>) — Sets the menu indicator visibility for controls within this view.
