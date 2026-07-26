---
title: 'displayLink(action:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiwindowscene/displaylink(action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/displaylink(action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/displaylink%28action%3A%29.json'
content_hash: 'sha256:d116dbc48303a84b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# displayLink(action:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func displayLink(action: @escaping @Sendable (CADisplayLink) -> Void) -> CADisplayLink?
```
