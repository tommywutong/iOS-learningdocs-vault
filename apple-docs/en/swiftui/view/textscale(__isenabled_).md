---
title: 'textScale(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/textscale(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/textscale(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/textscale%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:7eb82c2906ea4582'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# textScale(_:isEnabled:)

<sub>Instance Method</sub>

Applies a text scale to text in the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func textScale(_ scale: Text.Scale, isEnabled: Bool = true) -> some View

```

## Parameters

- `scale` — The text scale to apply.

- `isEnabled` — If true the text scale is applied; otherwise text scale is unchanged.

## Return Value

A view with the specified text scale applied.

## See Also

### Adjusting text size

- [dynamicTypeSize(_:)](<dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](../environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [DynamicTypeSize](../dynamictypesize.md) — A Dynamic Type size, which specifies how large scalable content should be.
- [ScaledMetric](../scaledmetric.md) — A dynamic property that scales a numeric value.
- [TextVariantPreference](../textvariantpreference.md) — A protocol for controlling the size variant of text views.
- [FixedTextVariant](../fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](../sizedependenttextvariant.md) — The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
