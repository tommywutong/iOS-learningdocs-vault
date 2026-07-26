---
title: AVCaptureView
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureview
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureview.json'
content_hash: 'sha256:0bff5aafb201e66e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVCaptureView

<sub>Class</sub>

A view that displays standard user interface controls for capturing media data.

<sub>macOS</sub>

```swift
class AVCaptureView
```

## Relationships

- **Inherits From**: [NSView](../appkit/nsview.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md), [NSAppearanceCustomization](../appkit/nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](../appkit/nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the Capture Session

- [session](avcaptureview/session.md) — The view’s associated capture session.
- [- setSession:showVideoPreview:showAudioPreview:](<avcaptureview/setsession(__showvideopreview_showaudiopreview_).md>) — Sets the view’s capture session.

### Customizing the View

- [controlsStyle](avcaptureview/controlsstyle.md) — The style of the capture controls presented by the view.
- [AVCaptureViewControlsStyle](avcaptureviewcontrolsstyle.md) — Constants that describe the capture view’s supported controls styles.
- [videoGravity](avcaptureview/videogravity.md) — A string value that defines how the capture view displays video within its bounds.

### Configuring the Delegate

- [delegate](avcaptureview/delegate.md) — The capture view’s delegate object.
- [AVCaptureViewDelegate](avcaptureviewdelegate.md) — The protocol that defines the methods you can implement to respond to capture view events.

### Recording Media

- [fileOutput](avcaptureview/fileoutput.md) — The capture file output used to record media data.

## See Also

### macOS playback and capture

- [Implementing Trimming in a macOS Player](implementing-trimming-in-a-macos-player.md) — Provide a QuickTime media-trimming experience in your macOS app.
- [AVPlayerView](avplayerview.md) — A view that displays content from a player and presents a native user interface to control playback.
