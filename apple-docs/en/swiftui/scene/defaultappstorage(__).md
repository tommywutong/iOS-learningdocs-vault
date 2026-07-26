---
title: 'defaultAppStorage(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/defaultappstorage(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/defaultappstorage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/defaultappstorage%28_%3A%29.json'
content_hash: 'sha256:4905e71a19be6e81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# defaultAppStorage(_:)

<sub>Instance Method</sub>

The default store used by `AppStorage` contained within the scene and its view content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func defaultAppStorage(_ store: UserDefaults) -> some Scene

```

## Parameters

- `store` — The user defaults to use as the default store for `AppStorage`.

## Discussion

If unspecified, the default store for a view hierarchy is `UserDefaults.standard`, but can be set a to a custom one. For example, sharing defaults between an app and an extension can override the default store to one created with `UserDefaults.init(suiteName:_)`.
