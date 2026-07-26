---
title: willChangeStatusBarOrientationNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/willchangestatusbarorientationnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/willchangestatusbarorientationnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/willchangestatusbarorientationnotification.json'
content_hash: 'sha256:a1eea6e5bc6a1afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# willChangeStatusBarOrientationNotification

<sub>Type Property</sub>

Posted when the app is about to change the orientation of its interface.

> [!warning] Deprecated
> Use [- viewWillTransitionToSize:withTransitionCoordinator:](<../uicontentcontainer/viewwilltransition(to_with_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated class let willChangeStatusBarOrientationNotification: NSNotification.Name
```

## Discussion

The userInfo dictionary contains an [NSNumber](../../foundation/nsnumber.md) that encapsulates a `UIInterfaceOrientation` value (see [UIInterfaceOrientation](../uiinterfaceorientation.md)). Use [UIApplicationStatusBarOrientationUserInfoKey](statusbarorientationuserinfokey.md) to access this value.

## See Also

### Deprecated notifications

- [UIApplicationWillChangeStatusBarFrameNotification](willchangestatusbarframenotification.md) — Posted when the app is about to change the frame of the status bar. _(deprecated)_
- [UIApplicationDidChangeStatusBarFrameNotification](didchangestatusbarframenotification.md) — Posted when the frame of the status bar changes. _(deprecated)_
- [UIApplicationDidChangeStatusBarOrientationNotification](didchangestatusbarorientationnotification.md) — Posted when the orientation of the app’s user interface changes. _(deprecated)_
