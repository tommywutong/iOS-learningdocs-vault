---
title: 'init(handler:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcaptureeventinteraction/init(handler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/init(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureeventinteraction/init%28handler%3A%29.json'
content_hash: 'sha256:41b98e06f5861a71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureEventInteraction](../avcaptureeventinteraction.md)

# init(handler:)

<sub>Initializer</sub>

Creates a capture event interaction with a handler that responds to presses of hardware buttons.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(handler: @escaping (AVCaptureEvent) -> Void)
```

## Parameters

- `handler` — An event handler the system calls when a person performs a primary or secondary capture event.

## See Also

### Creating an interaction

- [- initWithPrimaryEventHandler:secondaryEventHandler:](<init(primary_secondary_).md>) — Creates a capture event interaction with handlers that respond independently to presses of hardware buttons.
