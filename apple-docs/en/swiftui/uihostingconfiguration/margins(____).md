---
title: 'margins(_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingconfiguration/margins(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingconfiguration/margins(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingconfiguration/margins%28_%3A_%3A%29.json'
content_hash: 'sha256:ca7604636c03d3ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingConfiguration](../uihostingconfiguration.md)

# margins(_:_:)

<sub>Instance Method</sub>

Sets the margins around the content of the configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func margins(_ edges: Edge.Set = .all, _ insets: EdgeInsets) -> UIHostingConfiguration<Content, Background>
```

## Parameters

- `edges` — The edges to apply the insets. Any edges not specified will use the system default values. The default value is [all](../edge/set/all.md).

- `insets` — The insets to apply.

## Discussion

Use this modifier to replace the default margins applied to the root of the configuration. The following example creates 10 points of space between the content and the background on the leading edge and 20 points of space on the trailing edge:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.margins(.horizontal, 20.0)
```
