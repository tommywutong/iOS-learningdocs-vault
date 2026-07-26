---
title: urlSession
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/backgroundtask/urlsession
source_url: 'https://developer.apple.com/documentation/swiftui/backgroundtask/urlsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/backgroundtask/urlsession.json'
content_hash: 'sha256:d49b868346637087'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BackgroundTask](../backgroundtask.md)

# urlSession

<sub>Type Property</sub>

A task that responds to background URL sessions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var urlSession: BackgroundTask<String, Void> { get }
```

## See Also

### Responding to URL sessions

- [urlSession(_:)](<urlsession(__).md>) — A task that responds to background URL sessions matching the given identifier.
- [urlSession(matching:)](<urlsession(matching_).md>) — A task that responds to background URL sessions matching the given predicate.
