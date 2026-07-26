---
title: 'accessibilityChartDescriptor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessibilitychartdescriptor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessibilitychartdescriptor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessibilitychartdescriptor%28_%3A%29.json'
content_hash: 'sha256:81c8f562e53a1fca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessibilityChartDescriptor(_:)

<sub>Instance Method</sub>

Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityChartDescriptor<R>(_ representable: R) -> some View where R : AXChartDescriptorRepresentable

```

## Parameters

- `representable` — The [AXChartDescriptorRepresentable](../axchartdescriptorrepresentable.md) used to describe your chart and its data.

## Discussion

Use this method to provide information about your chart view to allow VoiceOver and other assistive technology users to perceive and interact with your chart and its data.

This may be applied to any View that represents a chart, including Image and custom-rendered chart views.

The `accessibilityChartDescriptor` modifier can be applied to -any- view representing a chart, the simplest case being just an image of a chart. The implementation details of the view aren’t important, only the fact that it represents a chart, and that the provided chart descriptor accurately describes the content of the chart.

Example usage:

First define your `AXChartDescriptorRepresentable` type.

```swift
struct MyChartDescriptorRepresentable:
AXChartDescriptorRepresentable {
    func makeChartDescriptor() -> AXChartDescriptor {
        // Build and return your `AXChartDescriptor` here.
    }

    func updateChartDescriptor(_ descriptor: AXChartDescriptor) {
        // Update your chart descriptor with any new values, or
        // don't override if your chart doesn't have changing
        // values.
    }
}
```

Then use the `accessibilityChartDescriptor` modifier to provide an instance of your `AXChartDescriptorRepresentable` type to the view representing your chart:

```swift
SomeChartView()
    .accessibilityChartDescriptor(MyChartDescriptorRepresentable())
```

## See Also

### Describing charts

- [AXChartDescriptorRepresentable](../axchartdescriptorrepresentable.md) — A type to generate an `AXChartDescriptor` object that you use to provide information about a chart and its data for an accessible experience in VoiceOver or other assistive technologies.
