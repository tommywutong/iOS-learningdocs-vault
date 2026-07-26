---
title: progressMarkNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsanimation/progressmarknotification
source_url: 'https://developer.apple.com/documentation/appkit/nsanimation/progressmarknotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsanimation/progressmarknotification.json'
content_hash: 'sha256:b1b90f85c1bd73bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSAnimation](../nsanimation.md)

# progressMarkNotification

<sub>Type Property</sub>

Posted when the current progress of a running animation reaches one of its progress marks.

<sub>macOS</sub>

```swift
class let progressMarkNotification: NSNotification.Name
```

## Discussion

The notification object is a running `NSAnimation` object. The `userInfo` dictionary contains the current progress mark, accessed via the key `NSAnimationProgressMark`.

## See Also

### Related Documentation

- [- animation:didReachProgressMark:](<../nsanimationdelegate/animation(__didreachprogressmark_).md>) — Sent to the delegate when an animation reaches a specific progress mark.
