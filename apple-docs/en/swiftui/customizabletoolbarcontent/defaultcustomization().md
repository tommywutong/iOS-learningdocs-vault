---
title: defaultCustomization()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（16.0 起废弃）, iPadOS 16.0+（16.0 起废弃）, Mac Catalyst 16.0+（16.0 起废弃）, macOS 13.0+（13.0 起废弃）, tvOS 16.0+（16.0 起废弃）, visionOS 1.0+, watchOS 9.0+（9.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/customizabletoolbarcontent/defaultcustomization()
source_url: 'https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/defaultcustomization()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/customizabletoolbarcontent/defaultcustomization%28%29.json'
content_hash: 'sha256:6c37467b05063bac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CustomizableToolbarContent](../customizabletoolbarcontent.md)

# defaultCustomization()

<sub>Instance Method</sub>

Configures customizable toolbar content with the default visibility and options.

> [!warning] Deprecated
> Please provide either a visibility or customization options

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func defaultCustomization() -> some CustomizableToolbarContent

```

## Discussion

Use the [defaultCustomization(_:options:)](<defaultcustomization(__options_).md>) modifier providing either a `defaultVisibility` or `options` instead.

## See Also

### Using default options

- [defaultCustomization(_:options:)](<defaultcustomization(__options_).md>) — Configures the way customizable toolbar items with the default behavior behave.
