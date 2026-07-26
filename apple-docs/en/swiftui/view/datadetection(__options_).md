---
title: 'dataDetection(_:options:)'
framework: DataDetection
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/datadetection(_:options:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/datadetection(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/datadetection%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:ddb7d325f9c9a30c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# dataDetection(_:options:)

<sub>Instance Method</sub>

Asynchronously detects data in the view’s content and styles them to indicate they are clickable.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
nonisolated func dataDetection(_ types: DataDetector.MatchType = .all, options: DataDetector.Options = .init()) -> some View

```

## Parameters

- `types` — The data detector match types

- `options` — Data detector options

## Return Value

A view with modified text attributes when matches are detected
