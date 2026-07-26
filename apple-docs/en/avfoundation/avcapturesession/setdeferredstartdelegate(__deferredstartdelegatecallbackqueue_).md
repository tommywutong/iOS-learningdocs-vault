---
title: 'setDeferredStartDelegate(_:deferredStartDelegateCallbackQueue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/setdeferredstartdelegate(_:deferredstartdelegatecallbackqueue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/setdeferredstartdelegate%28_%3Adeferredstartdelegatecallbackqueue%3A%29.json'
content_hash: 'sha256:27e99c243aa250e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# setDeferredStartDelegate(_:deferredStartDelegateCallbackQueue:)

<sub>Instance Method</sub>

Sets a delegate object for the session to call when performing deferred start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setDeferredStartDelegate(_ deferredStartDelegate: (any AVCaptureSessionDeferredStartDelegate)?, deferredStartDelegateCallbackQueue: dispatch_queue_t?)
```

## Parameters

- `deferredStartDelegate` — An object conforming to the [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md) protocol that receives events about deferred start.

- `deferredStartDelegateCallbackQueue` — A dispatch queue on which deferredStart delegate methods are called.

## Discussion

This delegate receives a call to the [- sessionWillRunDeferredStart:](<../avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(__).md>) method when deferred start is about to run. It is non-blocking, so by the time this method is called, the deferred start may already be underway. If you want your app to perform initialization (potentially) concurrently with deferred start (e.g. user-facing camera features that are not needed to display the first preview frame, but are available to the user as soon as possible) it may be done in the delegate’s [- sessionWillRunDeferredStart:](<../avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(__).md>) method. To wait until deferred start is finished to perform some remaining initialization work, use the [- sessionDidRunDeferredStart:](<../avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(__).md>) method instead.

The delegate receives a call to the [- sessionDidRunDeferredStart:](<../avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(__).md>) method when the deferred start finishes running. This allows you to run less-critical application initialization code. For example, if you’ve deferred an [AVCapturePhotoOutput](../avcapturephotooutput.md) by setting its [deferredStartEnabled](../avcaptureoutput/isdeferredstartenabled.md) property to `true`, and you’d like to do some app-specific initialization related to still capture, here might be a good place to put it.

If the delegate is non-nil, the session still calls the [- sessionWillRunDeferredStart:](<../avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(__).md>) and [- sessionDidRunDeferredStart:](<../avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(__).md>) methods regardless of the value of the session’s [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) property.

To minimize the capture session’s startup latency, defer all unnecessary work until after the session starts. This delegate provides callbacks for you to schedule deferred work without impacting session startup performance.

To perform initialization prior to deferred start but after the user interface displays, set [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) to `false`, and then run the custom initialization prior to calling [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>).

If [deferredStartDelegate](deferredstartdelegate.md) is not `NULL`, the session throws an exception if [deferredStartDelegateCallbackQueue](deferredstartdelegatecallbackqueue.md) is `nil`.

## See Also

### Configuring deferred start

- [manualDeferredStartSupported](ismanualdeferredstartsupported.md) — A `BOOL` value that indicates whether the session supports manually running deferred start.
- [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) — A Boolean value that indicates whether deferred start runs automatically.
- [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) — Tells the session to run deferred start when appropriate.
- [deferredStartDelegate](deferredstartdelegate.md) — A delegate object that observes events about deferred start.
- [deferredStartDelegateCallbackQueue](deferredstartdelegatecallbackqueue.md) — The dispatch queue on which the session calls deferred start delegate methods.
- [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md) — A protocol that defines the interface to respond to events about a capture session’s deferred start.
