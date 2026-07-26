---
title: deferredStartDelegateCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/deferredstartdelegatecallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/deferredstartdelegatecallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/deferredstartdelegatecallbackqueue.json'
content_hash: 'sha256:283e086c0df10f4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# deferredStartDelegateCallbackQueue

<sub>Instance Property</sub>

The dispatch queue on which the session calls deferred start delegate methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var deferredStartDelegateCallbackQueue: dispatch_queue_t? { get }
```

## Discussion

Call the [- setDeferredStartDelegate:deferredStartDelegateCallbackQueue:](<setdeferredstartdelegate(__deferredstartdelegatecallbackqueue_).md>) method to specify the dispatch queue on which to call the deferred start delegate methods.

## See Also

### Configuring deferred start

- [manualDeferredStartSupported](ismanualdeferredstartsupported.md) — A `BOOL` value that indicates whether the session supports manually running deferred start.
- [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) — A Boolean value that indicates whether deferred start runs automatically.
- [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) — Tells the session to run deferred start when appropriate.
- [deferredStartDelegate](deferredstartdelegate.md) — A delegate object that observes events about deferred start.
- [- setDeferredStartDelegate:deferredStartDelegateCallbackQueue:](<setdeferredstartdelegate(__deferredstartdelegatecallbackqueue_).md>) — Sets a delegate object for the session to call when performing deferred start.
- [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md) — A protocol that defines the interface to respond to events about a capture session’s deferred start.
