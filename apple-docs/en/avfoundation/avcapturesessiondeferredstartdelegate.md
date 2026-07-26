---
title: AVCaptureSessionDeferredStartDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesessiondeferredstartdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesessiondeferredstartdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesessiondeferredstartdelegate.json'
content_hash: 'sha256:5830a0e93625a57e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSessionDeferredStartDelegate

<sub>Protocol</sub>

A protocol that defines the interface to respond to events about a capture session’s deferred start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVCaptureSessionDeferredStartDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to deferred start events

- [- sessionDidRunDeferredStart:](<avcapturesessiondeferredstartdelegate/sessiondidrundeferredstart(__).md>) — This method gets called by the session when deferred start has finished running.
- [- sessionWillRunDeferredStart:](<avcapturesessiondeferredstartdelegate/sessionwillrundeferredstart(__).md>) — This method gets called by the session when deferred start is about to run.

## See Also

### Configuring deferred start

- [manualDeferredStartSupported](avcapturesession/ismanualdeferredstartsupported.md) — A `BOOL` value that indicates whether the session supports manually running deferred start.
- [automaticallyRunsDeferredStart](avcapturesession/automaticallyrunsdeferredstart.md) — A Boolean value that indicates whether deferred start runs automatically.
- [- runDeferredStartWhenNeeded](<avcapturesession/rundeferredstartwhenneeded().md>) — Tells the session to run deferred start when appropriate.
- [deferredStartDelegate](avcapturesession/deferredstartdelegate.md) — A delegate object that observes events about deferred start.
- [deferredStartDelegateCallbackQueue](avcapturesession/deferredstartdelegatecallbackqueue.md) — The dispatch queue on which the session calls deferred start delegate methods.
- [- setDeferredStartDelegate:deferredStartDelegateCallbackQueue:](<avcapturesession/setdeferredstartdelegate(__deferredstartdelegatecallbackqueue_).md>) — Sets a delegate object for the session to call when performing deferred start.
