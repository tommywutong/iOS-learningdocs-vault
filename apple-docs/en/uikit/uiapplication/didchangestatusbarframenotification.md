---
title: didChangeStatusBarFrameNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/didchangestatusbarframenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/didchangestatusbarframenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/didchangestatusbarframenotification.json'
content_hash: 'sha256:5186ffef4dfd1391'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# didChangeStatusBarFrameNotification

<sub>Type Property</sub>

Posted when the frame of the status bar changes.

> [!warning] Deprecated
> Use [- viewWillTransitionToSize:withTransitionCoordinator:](<../uicontentcontainer/viewwilltransition(to_with_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated class let didChangeStatusBarFrameNotification: NSNotification.Name
```

## Discussion

The `userInfo` dictionary contains an [NSValue](../../foundation/nsvalue.md) object that encapsulates a [CGRect](../../corefoundation/cgrect.md) structure expressing the location and size of the new status bar frame. Use [UIApplicationStatusBarFrameUserInfoKey](statusbarframeuserinfokey.md) to access this value.

## See Also

### Deprecated notifications

- [UIApplicationWillChangeStatusBarFrameNotification](willchangestatusbarframenotification.md) — Posted when the app is about to change the frame of the status bar. _(deprecated)_
- [UIApplicationWillChangeStatusBarOrientationNotification](willchangestatusbarorientationnotification.md) — Posted when the app is about to change the orientation of its interface. _(deprecated)_
- [UIApplicationDidChangeStatusBarOrientationNotification](didchangestatusbarorientationnotification.md) — Posted when the orientation of the app’s user interface changes. _(deprecated)_
