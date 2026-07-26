---
title: colorScheme
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/colorscheme
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/colorscheme'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/colorscheme.json'
content_hash: 'sha256:1d671768dffa339f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# colorScheme

<sub>Instance Property</sub>

The color scheme of this environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var colorScheme: ColorScheme { get set }
```

## Discussion

Read this environment value from within a view to find out if SwiftUI is currently displaying the view using the [ColorScheme.light](../colorscheme/light.md) or [ColorScheme.dark](../colorscheme/dark.md) appearance. The value that you receive depends on whether the user has enabled Dark Mode, possibly superseded by the configuration of the current presentation’s view hierarchy.

```swift
@Environment(\.colorScheme) private var colorScheme

var body: some View {
    Text(colorScheme == .dark ? "Dark" : "Light")
}
```

You can set the `colorScheme` environment value directly, but that usually isn’t what you want. Doing so changes the color scheme of the given view and its child views but _not_ the views above it in the view hierarchy. Instead, set a color scheme using the [preferredColorScheme(_:)](<../view/preferredcolorscheme(__).md>) modifier, which also propagates the value up through the view hierarchy to the enclosing presentation, like a sheet or a window.

When adjusting your app’s user interface to match the color scheme, consider also checking the [colorSchemeContrast](colorschemecontrast.md) property, which reflects a system-wide contrast setting that the user controls. For information, see [Accessibility](../../design/human-interface-guidelines/accessibility.md#Color-and-effects) in the Human Interface Guidelines.

> [!note] Note
> If you only need to provide different colors or images for different color scheme and contrast settings, do that in your app’s Asset Catalog. See [Asset management](../../xcode/asset-management.md).

## See Also

### Detecting and requesting the light or dark appearance

- [preferredColorScheme(_:)](<../view/preferredcolorscheme(__).md>) — Sets the preferred color scheme for this presentation.
- [ColorScheme](../colorscheme.md) — The possible color schemes, corresponding to the light and dark appearances.
