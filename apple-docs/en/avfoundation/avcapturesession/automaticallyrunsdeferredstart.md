---
title: automaticallyRunsDeferredStart
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/automaticallyrunsdeferredstart
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/automaticallyrunsdeferredstart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/automaticallyrunsdeferredstart.json'
content_hash: 'sha256:75797407a56e7bc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# automaticallyRunsDeferredStart

<sub>Instance Property</sub>

A Boolean value that indicates whether deferred start runs automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var automaticallyRunsDeferredStart: Bool { get set }
```

## Discussion

Deferred Start is a feature that allows you to control, on a per-output basis, whether output objects start when or after the session is started. The session defers starting an output when its [deferredStartEnabled](../avcaptureoutput/isdeferredstartenabled.md) property is set to `true`, and starts it after the session is started.

When this value is `true`, [AVCaptureSession](../avcapturesession.md) automatically runs deferred start. If only [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md) objects have [deferredStartEnabled](../avcapturevideopreviewlayer/isdeferredstartenabled.md) set to `false`, the session runs deferred start a short time after displaying the first frame. If there are [AVCaptureOutput](../avcaptureoutput.md) objects that have [deferredStartEnabled](../avcaptureoutput/isdeferredstartenabled.md) set to `false`, then the session waits until each output that provides streaming data to your app sends its first frame.

If you set this value to `false`, call [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) to indicate when to run deferred start.

By default, for apps that are linked on or after iOS 26, this value is `true`.

If [manualDeferredStartSupported](ismanualdeferredstartsupported.md) is `false`, setting this property value to false results in the session throwing an invalid argument exception.

## See Also

### Configuring deferred start

- [manualDeferredStartSupported](ismanualdeferredstartsupported.md) — A `BOOL` value that indicates whether the session supports manually running deferred start.
- [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) — Tells the session to run deferred start when appropriate.
- [deferredStartDelegate](deferredstartdelegate.md) — A delegate object that observes events about deferred start.
- [deferredStartDelegateCallbackQueue](deferredstartdelegatecallbackqueue.md) — The dispatch queue on which the session calls deferred start delegate methods.
- [- setDeferredStartDelegate:deferredStartDelegateCallbackQueue:](<setdeferredstartdelegate(__deferredstartdelegatecallbackqueue_).md>) — Sets a delegate object for the session to call when performing deferred start.
- [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md) — A protocol that defines the interface to respond to events about a capture session’s deferred start.
