---
title: isLuminanceReduced
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isluminancereduced
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isluminancereduced'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isluminancereduced.json'
content_hash: 'sha256:fce4be83904b854d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isLuminanceReduced

<sub>Instance Property</sub>

A Boolean value that indicates whether the display or environment currently requires reduced luminance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLuminanceReduced: Bool { get set }
```

## Discussion

When you detect this condition, lower the overall brightness of your view. For example, you can change large, filled shapes to be stroked, and choose less bright colors:

```swift
@Environment(\.isLuminanceReduced) var isLuminanceReduced

var body: some View {
    if isLuminanceReduced {
        Circle()
            .stroke(Color.gray, lineWidth: 10)
    } else {
        Circle()
            .fill(Color.white)
    }
}
```

In addition to the changes that you make, the system could also dim the display to achieve a suitable brightness. By reacting to `isLuminanceReduced`, you can preserve contrast and readability while helping to satisfy the reduced brightness requirement.

> [!note] Note
> On watchOS, the system typically sets this value to `true` when the user lowers their wrist, but the display remains on. Starting in watchOS 8, the system keeps your view visible on wrist down by default. If you want the system to blur the screen instead, as it did in earlier versions of watchOS, set the value for the [WKSupportsAlwaysOnDisplay](../../bundleresources/information-property-list/wksupportsalwaysondisplay.md) key in your app’s [Information Property List](../../bundleresources/information-property-list.md) file to `false`.

## See Also

### Reacting to interface characteristics

- [displayScale](displayscale.md) — The display scale of this environment.
- [pixelLength](pixellength.md) — The size of a pixel on the screen.
- [horizontalSizeClass](horizontalsizeclass.md) — The horizontal size class of this environment.
- [verticalSizeClass](verticalsizeclass.md) — The vertical size class of this environment.
- [UserInterfaceSizeClass](../userinterfacesizeclass.md) — A set of values that indicate the visual size available to the view.
