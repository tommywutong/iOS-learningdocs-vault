---
title: 'subscript(_:)'
framework: WidgetKit
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/timelineprovidercontext/environmentvariants-swift.struct/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineprovidercontext/environmentvariants-swift.struct/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineprovidercontext/environmentvariants-swift.struct/subscript%28_%3A%29.json'
content_hash: 'sha256:12f7bc8a22ac1f69'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [WidgetKit](../../../widgetkit.md) · [TimelineProviderContext](../../timelineprovidercontext.md) · [EnvironmentVariants](../environmentvariants-swift.struct.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the widget environment variants for a key path to an environment values instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
subscript<T>(keyPath: WritableKeyPath<EnvironmentValues, T>) -> [T]? { get }
```
