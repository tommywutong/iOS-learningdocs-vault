---
title: 'asyncImageURLSession(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/asyncimageurlsession(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/asyncimageurlsession(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/asyncimageurlsession%28_%3A%29.json'
content_hash: 'sha256:ab2f2703c6ac4ae1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# asyncImageURLSession(_:)

<sub>Instance Method</sub>

A modifier that adds a URL session for asynchronous images contained in the view to use when fetching image data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func asyncImageURLSession(_ urlSession: URLSession) -> some View

```

## Parameters

- `urlSession` — An instance of [URLSession](../../foundation/urlsession.md) for [AsyncImage](../asyncimage.md) instances to use for image download data tasks.
