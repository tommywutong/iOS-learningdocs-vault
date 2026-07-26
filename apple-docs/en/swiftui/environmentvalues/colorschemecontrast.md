---
title: colorSchemeContrast
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/colorschemecontrast
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/colorschemecontrast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/colorschemecontrast.json'
content_hash: 'sha256:2aa328c92d26d95d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# colorSchemeContrast

<sub>Instance Property</sub>

The contrast associated with the color scheme of this environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var colorSchemeContrast: ColorSchemeContrast { get }
```

## Discussion

Read this environment value from within a view to find out if SwiftUI is currently displaying the view using [ColorSchemeContrast.standard](../colorschemecontrast/standard.md) or [ColorSchemeContrast.increased](../colorschemecontrast/increased.md) contrast. The value that you read depends entirely on user settings, and you can’t change it.

```swift
@Environment(\.colorSchemeContrast) private var colorSchemeContrast

var body: some View {
    Text(colorSchemeContrast == .standard ? "Standard" : "Increased")
}
```

When adjusting your app’s user interface to match the contrast, consider also checking the [colorScheme](colorscheme.md) property to find out if SwiftUI is displaying the view with a light or dark appearance. For information, see [Accessibility](../../design/human-interface-guidelines/accessibility.md#Color-and-effects) in the Human Interface Guidelines.

> [!note] Note
> If you only need to provide different colors or images for different color scheme and contrast settings, do that in your app’s Asset Catalog. See [Asset management](../../xcode/asset-management.md).

## See Also

### Getting the color scheme contrast

- [ColorSchemeContrast](../colorschemecontrast.md) — The contrast between the app’s foreground and background colors.
