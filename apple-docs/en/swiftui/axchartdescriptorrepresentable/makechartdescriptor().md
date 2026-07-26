---
title: makeChartDescriptor()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/axchartdescriptorrepresentable/makechartdescriptor()
source_url: 'https://developer.apple.com/documentation/swiftui/axchartdescriptorrepresentable/makechartdescriptor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/axchartdescriptorrepresentable/makechartdescriptor%28%29.json'
content_hash: 'sha256:0582721f3e7e566a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AXChartDescriptorRepresentable](../axchartdescriptorrepresentable.md)

# makeChartDescriptor()

<sub>Instance Method</sub>

Create the `AXChartDescriptor` for this view, and return it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeChartDescriptor() -> AXChartDescriptor
```

## Discussion

This will be called once per identity of your `View`. It will not be run again unless the identity of your `View` changes. If you need to update the `AXChartDescriptor` based on changes in your `View`, or in the `Environment`, implement `updateChartDescriptor`. This method will only be called if / when accessibility needs the `AXChartDescriptor` of your view, for VoiceOver.

## See Also

### Managing a descriptor

- [updateChartDescriptor(_:)](<updatechartdescriptor(__).md>) — Update the existing `AXChartDescriptor` for your view, based on changes in your view or in the `Environment`.
