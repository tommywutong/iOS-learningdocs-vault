---
title: 'sessionWillRunDeferredStart(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart%28_%3A%29.json'
content_hash: 'sha256:5d835cc08fcc378c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md)

# sessionWillRunDeferredStart(_:)

<sub>Instance Method</sub>

This method gets called by the session when deferred start is about to run.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func sessionWillRunDeferredStart(_ session: AVCaptureSession)
```

## Parameters

- `session` — The [AVCaptureSession](../avcapturesession.md) instance that runs the deferred start.

## Discussion

Delegates receive this message when the session has finished the deferred start. This message will be sent regardless of whether the session’s [automaticallyRunsDeferredStart](../avcapturesession/automaticallyrunsdeferredstart.md) property is set. See [- setDeferredStartDelegate:deferredStartDelegateCallbackQueue:](<../avcapturesession/setdeferredstartdelegate(__deferredstartdelegatecallbackqueue_).md>) documentation for more information.

## See Also

### Responding to deferred start events

- [- sessionDidRunDeferredStart:](<sessiondidrundeferredstart(__).md>) — This method gets called by the session when deferred start has finished running.
