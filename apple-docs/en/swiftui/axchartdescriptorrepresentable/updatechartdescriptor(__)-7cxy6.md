---
title: 'updateChartDescriptor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/axchartdescriptorrepresentable/updatechartdescriptor(_:)-7cxy6'
source_url: 'https://developer.apple.com/documentation/swiftui/axchartdescriptorrepresentable/updatechartdescriptor(_:)-7cxy6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/axchartdescriptorrepresentable/updatechartdescriptor%28_%3A%29-7cxy6.json'
content_hash: 'sha256:50ad0ac032213330'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AXChartDescriptorRepresentable](../axchartdescriptorrepresentable.md)

# updateChartDescriptor(_:)

<sub>Instance Method</sub>

Update the existing `AXChartDescriptor` for your view, based on changes in your view or in the `Environment`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func updateChartDescriptor(_ descriptor: AXChartDescriptor)
```

## Discussion

This will be called as needed, when accessibility needs your `AXChartDescriptor` for VoiceOver. It will only be called if the inputs to your views, or a relevant part of the `Environment`, have changed.
