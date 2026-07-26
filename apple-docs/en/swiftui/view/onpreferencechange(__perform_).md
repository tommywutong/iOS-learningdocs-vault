---
title: 'onPreferenceChange(_:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onpreferencechange(_:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onpreferencechange(_:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onpreferencechange%28_%3Aperform%3A%29.json'
content_hash: 'sha256:91011651e5cb60e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onPreferenceChange(_:perform:)

<sub>Instance Method</sub>

Adds an action to perform when the specified preference key’s value changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onPreferenceChange<K>(_ key: K.Type = K.self, perform action: @escaping (K.Value) -> Void) -> some View where K : PreferenceKey, K.Value : Equatable

```

## Parameters

- `key` — The key to monitor for value changes.

- `action` — The action to perform when the value for `key` changes. The `action` closure passes the new value as its parameter.

## Return Value

A view that triggers `action` when the value for `key` changes.
