---
title: AVPictureInPictureControllerDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontrollerdelegate
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontrollerdelegate.json'
content_hash: 'sha256:e6624317317d5d6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPictureInPictureControllerDelegate

<sub>Protocol</sub>

A protocol to adopt to respond to Picture in Picture events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVPictureInPictureControllerDelegate : NSObjectProtocol
```

## Overview

Adopt this protocol in a custom object, and assign the object as the [delegate](avpictureinpicturecontroller/delegate.md) of your [AVPictureInPictureController](avpictureinpicturecontroller.md) instance.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Restoring the User Interface

- [- pictureInPictureController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate to restore the user interface before Picture in Picture stops.

### Responding to Picture in Picture Lifecycle Events

- [- pictureInPictureControllerWillStartPictureInPicture:](<avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(__).md>) — Tells the delegate that Picture in Picture is about to start.
- [- pictureInPictureControllerDidStartPictureInPicture:](<avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(__).md>) — Tells the delegate that Picture in Picture started.
- [- pictureInPictureController:failedToStartPictureInPictureWithError:](<avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture failed to start.
- [- pictureInPictureControllerWillStopPictureInPicture:](<avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(__).md>) — Tells the delegate that Picture in Picture is about to stop.
- [- pictureInPictureControllerDidStopPictureInPicture:](<avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(__).md>) — Tells the delegate that Picture in Picture stopped.

## See Also

### Accessing the Delegate Object

- [delegate](avpictureinpicturecontroller/delegate.md) — A delegate object for a Picture in Picture controller.
