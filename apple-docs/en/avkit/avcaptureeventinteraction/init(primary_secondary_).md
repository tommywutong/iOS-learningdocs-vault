---
title: 'init(primary:secondary:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcaptureeventinteraction/init(primary:secondary:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/init(primary:secondary:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureeventinteraction/init%28primary%3Asecondary%3A%29.json'
content_hash: 'sha256:b9ffb331a143f84d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureEventInteraction](../avcaptureeventinteraction.md)

# init(primary:secondary:)

<sub>Initializer</sub>

Creates a capture event interaction with handlers that respond independently to presses of hardware buttons.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(primary primaryHandler: @escaping (AVCaptureEvent) -> Void, secondary secondaryHandler: @escaping (AVCaptureEvent) -> Void)
```

## Parameters

- `primaryHandler` — An event handler the system calls when a person performs a primary capture event.

- `secondaryHandler` — An event handler the system calls when a person performs a secondary capture event.

## See Also

### Creating an interaction

- [- initWithEventHandler:](<init(handler_).md>) — Creates a capture event interaction with a handler that responds to presses of hardware buttons.
