---
title: dynamicTypeSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/dynamictypesize
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/dynamictypesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/dynamictypesize.json'
content_hash: 'sha256:41ef0b7f8eb28ca7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# dynamicTypeSize

<sub>Instance Property</sub>

The current Dynamic Type size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dynamicTypeSize: DynamicTypeSize { get set }
```

## Discussion

This value changes as the user’s chosen Dynamic Type size changes. The default value is device-dependent.

When limiting the Dynamic Type size, consider if adding a large content view with [accessibilityShowsLargeContentViewer()](<../view/accessibilityshowslargecontentviewer().md>) would be appropriate.

On macOS, this value cannot be changed by users and does not affect the text size.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](<../view/textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](<../view/dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.
- [DynamicTypeSize](../dynamictypesize.md) — A Dynamic Type size, which specifies how large scalable content should be.
- [ScaledMetric](../scaledmetric.md) — A dynamic property that scales a numeric value.
- [TextVariantPreference](../textvariantpreference.md) — A protocol for controlling the size variant of text views.
- [FixedTextVariant](../fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](../sizedependenttextvariant.md) — The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
