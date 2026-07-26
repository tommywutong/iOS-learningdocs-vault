---
title: runDeferredStartWhenNeeded()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesession/rundeferredstartwhenneeded()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/rundeferredstartwhenneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/rundeferredstartwhenneeded%28%29.json'
content_hash: 'sha256:4e6527befc49db9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# runDeferredStartWhenNeeded()

<sub>Instance Method</sub>

Tells the session to run deferred start when appropriate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func runDeferredStartWhenNeeded()
```

## Discussion

For best perceived startup performance, call this after displaying the first frame, so that deferred start processing doesn’t interfere with other initialization operations. For example, if using a [CAMetalLayer](../../quartzcore/cametallayer.md) to draw camera frames, add a `presentHandler` (using doc://com.apple.documentation/metal/mtldrawable/addpresentedhandler) to the first drawable and call [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) from there.

If one or more outputs need to start to perform a capture operation, and [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) has not run yet, the session runs the deferred start on your app’s behalf. Only call this method once for each configuration commit - after the first call, subsequent calls to [- runDeferredStartWhenNeeded](<rundeferredstartwhenneeded().md>) have no effect. The deferred start runs asynchronously, so this method returns immediately.

> [!note] Note
> You can only call this when [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) is `false`. Otherwise, the session throws an `NSInvalidArgumentException`.

> [!important] Important
> To avoid blocking your app’s UI, don’t call this method from the application’s main actor or queue.

## See Also

### Configuring deferred start

- [manualDeferredStartSupported](ismanualdeferredstartsupported.md) — A `BOOL` value that indicates whether the session supports manually running deferred start.
- [automaticallyRunsDeferredStart](automaticallyrunsdeferredstart.md) — A Boolean value that indicates whether deferred start runs automatically.
- [deferredStartDelegate](deferredstartdelegate.md) — A delegate object that observes events about deferred start.
- [deferredStartDelegateCallbackQueue](deferredstartdelegatecallbackqueue.md) — The dispatch queue on which the session calls deferred start delegate methods.
- [- setDeferredStartDelegate:deferredStartDelegateCallbackQueue:](<setdeferredstartdelegate(__deferredstartdelegatecallbackqueue_).md>) — Sets a delegate object for the session to call when performing deferred start.
- [AVCaptureSessionDeferredStartDelegate](../avcapturesessiondeferredstartdelegate.md) — A protocol that defines the interface to respond to events about a capture session’s deferred start.
