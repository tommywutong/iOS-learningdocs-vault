---
title: AXChartDescriptorRepresentable
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/axchartdescriptorrepresentable
source_url: 'https://developer.apple.com/documentation/swiftui/axchartdescriptorrepresentable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/axchartdescriptorrepresentable.json'
content_hash: 'sha256:64ac1e41fc99081b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AXChartDescriptorRepresentable

<sub>Protocol</sub>

A type to generate an `AXChartDescriptor` object that you use to provide information about a chart and its data for an accessible experience in VoiceOver or other assistive technologies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AXChartDescriptorRepresentable
```

## Overview

Note that you may use the `@Environment` property wrapper inside the implementation of your `AXChartDescriptorRepresentable`, in which case you should implement `updateChartDescriptor`, which will be called when the `Environment` changes.

For example, to provide accessibility for a view that represents a chart, you would first declare your chart descriptor representable type:

```swift
struct MyChartDescriptorRepresentable: AXChartDescriptorRepresentable {
    func makeChartDescriptor() -> AXChartDescriptor {
        // Build and return your `AXChartDescriptor` here.
    }

    func updateChartDescriptor(_ descriptor: AXChartDescriptor) {
        // Update your chart descriptor with any new values.
    }
}
```

Then, provide an instance of your `AXChartDescriptorRepresentable` type to your view using the `accessibilityChartDescriptor` modifier:

```swift
var body: some View {
    MyChartView()
        .accessibilityChartDescriptor(MyChartDescriptorRepresentable())
}
```

## Topics

### Managing a descriptor

- [makeChartDescriptor()](<axchartdescriptorrepresentable/makechartdescriptor().md>) — Create the `AXChartDescriptor` for this view, and return it.
- [updateChartDescriptor(_:)](<axchartdescriptorrepresentable/updatechartdescriptor(__).md>) — Update the existing `AXChartDescriptor` for your view, based on changes in your view or in the `Environment`.

## See Also

### Describing charts

- [accessibilityChartDescriptor(_:)](<view/accessibilitychartdescriptor(__).md>) — Adds a descriptor to a View that represents a chart to make the chart’s contents accessible to all users.
