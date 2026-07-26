---
title: boundsDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsview/boundsdidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsview/boundsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsview/boundsdidchangenotification.json'
content_hash: 'sha256:8ece5ff70b8d7b4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSView](../nsview.md)

# boundsDidChangeNotification

<sub>Type Property</sub>

A notification that posts when the view’s bounds rectangle changes to a new value independently of the frame rectangle.

<sub>macOS</sub>

```swift
class let boundsDidChangeNotification: NSNotification.Name
```

## Discussion

This notification posts only when the view’s [postsBoundsChangedNotifications](postsboundschangednotifications.md) property is [true](../../swift/true.md).

The notification object is the `NSView` object whose bounds rectangle has changed. This notification does not contain a `userInfo` dictionary.

The following methods can result in notification posting:

- [bounds](bounds.md)
- [- setBoundsOrigin:](<setboundsorigin(__).md>)
- [boundsRotation](boundsrotation.md)
- [- setBoundsSize:](<setboundssize(__).md>)
- [- translateOriginToPoint:](<translateorigin(to_).md>)
- [- scaleUnitSquareToSize:](<scaleunitsquare(to_).md>)
- [- rotateByAngle:](<rotate(bydegrees_).md>)

Note that the bounds rectangle resizes automatically to track the frame rectangle. However, changes to the frame rectangle do not result in this bounds-changed notification.

To observe this notification using Swift concurrency, use [BoundsDidChangeMessage](boundsdidchangemessage.md).

## See Also

### Modifying the Bounds Rectangle

- [bounds](bounds.md) — The view’s bounds rectangle, which expresses its location and size in its own coordinate system.
- [- setBoundsOrigin:](<setboundsorigin(__).md>) — Sets the origin of the view’s bounds rectangle to a specified point.
- [- setBoundsSize:](<setboundssize(__).md>) — Sets the size of the view’s bounds rectangle to specified dimensions, inversely scaling its coordinate system relative to its frame rectangle.
- [boundsRotation](boundsrotation.md) — The angle of rotation, measured in degrees, applied to the view’s bounds rectangle relative to its frame rectangle.
- [postsBoundsChangedNotifications](postsboundschangednotifications.md) — A Boolean value indicating whether the view posts notifications when its bounds rectangle changes.
