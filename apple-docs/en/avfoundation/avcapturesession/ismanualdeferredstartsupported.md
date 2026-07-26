---
title: isManualDeferredStartSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/ismanualdeferredstartsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/ismanualdeferredstartsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/ismanualdeferredstartsupported.json'
content_hash: 'sha256:ab34326e9ea261bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# isManualDeferredStartSupported

<sub>Instance Property</sub>

A `BOOL` value that indicates whether the session supports manually running deferred start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isManualDeferredStartSupported: Bool { get }
```

## Discussion

Deferred Start is a feature that allows you to control, on a per-output basis, whether output objects start when or after the session is started. The session defers starting an output when its `deferredStartEnabled` property is set to `true`, and starts it after the session is started.

You can only set the [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) property value to `false` if the session supports manual deferred start.

## See Also

### Configuring deferred start

- [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) — A Boolean value that indicates whether deferred start runs automatically.
- [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) — Tells the session to run deferred start when appropriate.
- [deferredStartDelegate](deferredstartdelegate.md) — A delegate object that observes events about deferred start.
- [deferredStartDelegateCallbackQueue](deferredstartdelegatecallbackqueue.md) — The dispatch queue on which the session calls deferred start delegate methods.
- [- setDeferredStartDelegate:deferredStartDelegateCallbackQueue:](<setdeferredstartdelegate(__deferredstartdelegatecallbackqueue_).md>) — Sets a delegate object for the session to call when performing deferred start.
- [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md) — A protocol that defines the interface to respond to events about a capture session’s deferred start.
