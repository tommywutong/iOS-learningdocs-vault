---
title: KeyPress.Result
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keypress/result
source_url: 'https://developer.apple.com/documentation/swiftui/keypress/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keypress/result.json'
content_hash: 'sha256:d45da5034436ce23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyPress](../keypress.md)

# KeyPress.Result

<sub>Enumeration</sub>

A result value returned from a key-press action that indicates whether the action consumed the event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Result
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the result

- [KeyPress.Result.handled](result/handled.md) — The action consumed the event, preventing dispatch from continuing.
- [KeyPress.Result.ignored](result/ignored.md) — The action ignored the event, allowing dispatch to continue.
