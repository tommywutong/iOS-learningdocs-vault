---
title: 'init(value:in:onEditingChanged:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/slider/init(value:in:oneditingchanged:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slider/init(value:in:oneditingchanged:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slider/init%28value%3Ain%3Aoneditingchanged%3Alabel%3A%29.json'
content_hash: 'sha256:34a7c40c61325eed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Slider](../slider.md)

# init(value:in:onEditingChanged:label:)

<sub>Initializer</sub>

Creates a slider to select a value from a given range, which displays the provided label.

> [!warning] Deprecated
> Use [init(value:in:label:onEditingChanged:)](<init(value_in_label_oneditingchanged_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<V>(value: Binding<V>, in bounds: ClosedRange<V> = 0...1, onEditingChanged: @escaping (Bool) -> Void = { _ in }, @ContentBuilder label: () -> Label) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

## Parameters

- `value` — The selected value within `bounds`.

- `bounds` — The range of the valid values. Defaults to `0...1`.

- `onEditingChanged` — A callback for when editing begins and ends.

- `label` — A `View` that describes the purpose of the instance. Not all slider styles show the label, but even in those cases, SwiftUI uses the label for accessibility. For example, VoiceOver uses the label to identify the purpose of the slider.

## Discussion

The `value` of the created instance is equal to the position of the given value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example, on iOS, editing begins when the user starts to drag the thumb along the slider’s track.

## See Also

### Deprecated initializers

- [init(value:in:step:onEditingChanged:label:)](<init(value_in_step_oneditingchanged_label_).md>) — Creates a slider to select a value from a given range, subject to a step increment, which displays the provided label. _(deprecated)_
- [init(value:in:onEditingChanged:minimumValueLabel:maximumValueLabel:label:)](<init(value_in_oneditingchanged_minimumvaluelabel_maximumvaluelabel_label_).md>) — Creates a slider to select a value from a given range, which displays the provided labels. _(deprecated)_
- [init(value:in:step:onEditingChanged:minimumValueLabel:maximumValueLabel:label:)](<init(value_in_step_oneditingchanged_minimumvaluelabel_maximumvaluelabel_label_).md>) — Creates a slider to select a value from a given range, subject to a step increment, which displays the provided labels. _(deprecated)_
