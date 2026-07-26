---
title: frameDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsview/framedidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsview/framedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsview/framedidchangenotification.json'
content_hash: 'sha256:57262fa622928329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSView](../nsview.md)

# frameDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the view’s frame rectangle changes to a new value.

<sub>macOS</sub>

```swift
class let frameDidChangeNotification: NSNotification.Name
```

## Discussion

This notification posts only when the view’s [postsFrameChangedNotifications](postsframechangednotifications.md) property is [true](../../swift/true.md).

The notification object is the `NSView` object whose frame rectangle has changed. This notification does not contain a `userInfo` dictionary.

The following methods can result in notification posting:

- [frame](frame.md)
- [- setFrameOrigin:](<setframeorigin(__).md>)
- [frameRotation](framerotation.md)
- [- setFrameSize:](<setframesize(__).md>)

To observe this notification using Swift concurrency, use [FrameDidChangeMessage](framedidchangemessage.md).

## See Also

### Modifying the Frame Rectangle

- [frame](frame.md) — The view’s frame rectangle, which defines its position and size in its superview’s coordinate system.
- [- setFrameOrigin:](<setframeorigin(__).md>) — Sets the origin of the view’s frame rectangle to the specified point, effectively repositioning it within its superview.
- [- setFrameSize:](<setframesize(__).md>) — Sets the size of the view’s frame rectangle to the specified dimensions, resizing it within its superview without affecting its coordinate system.
- [frameRotation](framerotation.md) — The angle of rotation, measured in degrees, applied to the view’s frame rectangle relative to its superview’s coordinate system.
- [postsFrameChangedNotifications](postsframechangednotifications.md) — A Boolean value indicating whether the view posts notifications when its frame rectangle changes.
