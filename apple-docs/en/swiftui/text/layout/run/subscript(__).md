---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/layout/run/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/layout/run/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/layout/run/subscript%28_%3A%29.json'
content_hash: 'sha256:03df55c188e6a4f5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftUI](../../../../swiftui.md) · [Text](../../../text.md) · [Layout](../../layout.md) · [Run](../run.md)

# subscript(_:)

<sub>Instance Subscript</sub>

The custom attribute of type `T` associated with the run of glyphs, or nil. If no run contains the custom attribute we also check its attachment’s runs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(key: T.Type) -> T? where T : TextAttribute { get }
```
