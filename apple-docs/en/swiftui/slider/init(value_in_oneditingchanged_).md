---
title: 'init(value:in:onEditingChanged:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/slider/init(value:in:oneditingchanged:)'
source_url: 'https://developer.apple.com/documentation/swiftui/slider/init(value:in:oneditingchanged:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/slider/init%28value%3Ain%3Aoneditingchanged%3A%29.json'
content_hash: 'sha256:6955ca881622e4af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Slider](../slider.md)

# init(value:in:onEditingChanged:)

<sub>Initializer</sub>

Creates a slider to select a value from a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init<V>(value: Binding<V>, in bounds: ClosedRange<V> = 0...1, onEditingChanged: @escaping (Bool) -> Void = { _ in }) where V : BinaryFloatingPoint, V.Stride : BinaryFloatingPoint
```

## Parameters

- `value` — The selected value within `bounds`.

- `bounds` — The range of the valid values. Defaults to `0...1`.

- `onEditingChanged` — A callback for when editing begins and ends.

## Discussion

The `value` of the created instance is equal to the position of the given value within `bounds`, mapped into `0...1`.

The slider calls `onEditingChanged` when editing begins and ends. For example, on iOS, editing begins when the user starts to drag the thumb along the slider’s track.

## See Also

### Creating a slider

- [init(value:in:step:onEditingChanged:)](<init(value_in_step_oneditingchanged_).md>) — Creates a slider to select a value from a given range, subject to a step increment.
