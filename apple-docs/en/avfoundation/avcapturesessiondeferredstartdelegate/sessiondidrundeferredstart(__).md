---
title: 'sessionDidRunDeferredStart(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart%28_%3A%29.json'
content_hash: 'sha256:ecb109d7aeed9c64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md)

# sessionDidRunDeferredStart(_:)

<sub>Instance Method</sub>

This method gets called by the session when deferred start has finished running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func sessionDidRunDeferredStart(_ session: AVCaptureSession)
```

## Parameters

- `session` — The [AVCaptureSession](../avcapturesession.md) instance that runs the deferred start.

## See Also

### Responding to deferred start events

- [- sessionWillRunDeferredStart:](<sessionwillrundeferredstart(__).md>) — This method gets called by the session when deferred start is about to run.
