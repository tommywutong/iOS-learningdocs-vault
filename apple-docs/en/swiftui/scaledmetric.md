---
title: ScaledMetric
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scaledmetric
source_url: 'https://developer.apple.com/documentation/swiftui/scaledmetric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scaledmetric.json'
content_hash: 'sha256:7a3f03507729a7a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScaledMetric

<sub>Structure</sub>

A dynamic property that scales a numeric value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@propertyWrapper struct ScaledMetric<Value> where Value : BinaryFloatingPoint
```

## Relationships

- **Conforms To**: [DynamicProperty](dynamicproperty.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating the metric

- [init(wrappedValue:)](<scaledmetric/init(wrappedvalue_).md>) — Creates the scaled metric with an unscaled value using the default scaling.
- [init(wrappedValue:relativeTo:)](<scaledmetric/init(wrappedvalue_relativeto_).md>) — Creates the scaled metric with an unscaled value and a text style to scale relative to.

### Getting the metric

- [wrappedValue](scaledmetric/wrappedvalue.md) — The value scaled based on the current environment.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [DynamicTypeSize](dynamictypesize.md) — A Dynamic Type size, which specifies how large scalable content should be.
- [TextVariantPreference](textvariantpreference.md) — A protocol for controlling the size variant of text views.
- [FixedTextVariant](fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](sizedependenttextvariant.md) — The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
