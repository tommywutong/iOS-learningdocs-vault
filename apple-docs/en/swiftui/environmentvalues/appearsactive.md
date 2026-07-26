---
title: appearsActive
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 10.15+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/appearsactive
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/appearsactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/appearsactive.json'
content_hash: 'sha256:1f1c43ffb94fcace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# appearsActive

<sub>Instance Property</sub>

Whether views and styles in this environment should prefer an active appearance over an inactive appearance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 15.0)
var appearsActive: Bool { get set }
```

## Discussion

On macOS, views in the focused window (also referred to as the “key” window) should appear active. Some contexts also appear active in other circumstances, such as the contents of a window toolbar appearing active when the window is not focused but is the main window.

Typical adjustments made when a view does not appear active include:

- Uses of `Color.accentColor` should generally be removed or replaced with a desaturated style.
- Text and image content in sidebars should appear dimmer.
- Buttons with destructive actions should appear disabled.
- `ShapeStyle.selection` and selection in list and tables will automatically become a grey color

Custom views, styles, and shape styles can use this to adjust their own appearance:

```swift
struct ProminentPillButtonStyle: ButtonStyle {
    @Environment(\.appearsActive) private var appearsActive

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .lineLimit(1)
            .padding(.horizontal, 8)
            .padding(.vertical, 2)
            .frame(minHeight: 20)
            .overlay(Capsule().strokeBorder(.tertiary))
            .background(appearsActive ? Color.accentColor : .clear, in: .capsule)
            .contentShape(.capsule)
    }
}
```

On all other platforms, this value is always `true`.

This is bridged with `UITraitCollection.activeAppearance` for UIKit hosted content.

## See Also

### Display characteristics

- [colorScheme](colorscheme.md) — The color scheme of this environment.
- [colorSchemeContrast](colorschemecontrast.md) — The contrast associated with the color scheme of this environment.
- [displayScale](displayscale.md) — The display scale of this environment.
- [horizontalSizeClass](horizontalsizeclass.md) — The horizontal size class of this environment.
- [imageScale](imagescale.md) — The image scale for this environment.
- [pixelLength](pixellength.md) — The size of a pixel on the screen.
- [sidebarRowSize](sidebarrowsize.md) — The current size of sidebar rows.
- [verticalSizeClass](verticalsizeclass.md) — The vertical size class of this environment.
- [immersiveSpaceDisplacement](immersivespacedisplacement.md) — The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [labelsVisibility](labelsvisibility.md) — The labels visibility set by [labelsVisibility(_:)](<../view/labelsvisibility(__).md>).
- [materialActiveAppearance](materialactiveappearance.md) — The behavior materials should use for their active state, defaulting to `automatic`.
- [TabBarPlacement](../tabbarplacement.md) — A placement for tabs in a tab view.
- [toolbarLabelStyle](toolbarlabelstyle.md) — The label style to apply to controls within a toolbar.
