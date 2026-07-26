---
title: 'dynamicTypeSize(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/dynamictypesize(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/dynamictypesize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/dynamictypesize%28_%3A%29.json'
content_hash: 'sha256:39bd294ad69653aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dynamicTypeSize(_:)

<sub>Instance Method</sub>

Sets the Dynamic Type size within the view to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func dynamicTypeSize(_ size: DynamicTypeSize) -> some View

```

## Parameters

- `size` — The size to set for this view.

## Return Value

A view that sets the Dynamic Type size to the specified `size`.

## Discussion

As an example, you can set a Dynamic Type size in `ContentView` to be [DynamicTypeSize.xLarge](../dynamictypesize/xlarge.md) (this can be useful in previews to see your content at a different size) like this:

```swift
ContentView()
    .dynamicTypeSize(.xLarge)
```

If a Dynamic Type size range is applied after setting a value, the value is limited by that range:

```swift
ContentView() // Dynamic Type size will be .large
    .dynamicTypeSize(...DynamicTypeSize.large)
    .dynamicTypeSize(.xLarge)
```

When limiting the Dynamic Type size, consider if adding a large content view with [accessibilityShowsLargeContentViewer()](<accessibilityshowslargecontentviewer().md>) would be appropriate.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](<textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [dynamicTypeSize](../environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [DynamicTypeSize](../dynamictypesize.md) — A Dynamic Type size, which specifies how large scalable content should be.
- [ScaledMetric](../scaledmetric.md) — A dynamic property that scales a numeric value.
- [TextVariantPreference](../textvariantpreference.md) — A protocol for controlling the size variant of text views.
- [FixedTextVariant](../fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](../sizedependenttextvariant.md) — The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
