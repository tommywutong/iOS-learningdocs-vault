---
title: 'urlSession(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/backgroundtask/urlsession(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/backgroundtask/urlsession(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/backgroundtask/urlsession%28_%3A%29.json'
content_hash: 'sha256:b35754fa4c3615b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BackgroundTask](../backgroundtask.md)

# urlSession(_:)

<sub>Type Method</sub>

A task that responds to background URL sessions matching the given identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func urlSession(_ identifier: String) -> BackgroundTask<Void, Void>
```

## Parameters

- `identifier` — The identifier to match.

## Return Value

A background task that you can handle with your app or extension.

## See Also

### Responding to URL sessions

- [urlSession](urlsession.md) — A task that responds to background URL sessions.
- [urlSession(matching:)](<urlsession(matching_).md>) — A task that responds to background URL sessions matching the given predicate.
