---
title: ignoreSnapshotOnNextApplicationLaunch()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/ignoresnapshotonnextapplicationlaunch()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/ignoresnapshotonnextapplicationlaunch()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/ignoresnapshotonnextapplicationlaunch%28%29.json'
content_hash: 'sha256:01b7caff29c03770'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# ignoreSnapshotOnNextApplicationLaunch()

<sub>Instance Method</sub>

Prevents the app from using the recent snapshot image during the next launch cycle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func ignoreSnapshotOnNextApplicationLaunch()
```

## Discussion

As part of the state preservation process, UIKit captures your app’s user interface and stores it in an image file. When your app is relaunched, the system displays this snapshot image in place of your app’s default launch image to preserve the notion that your app was still running. If you feel that the snapshot cannot correctly reflect your app’s user interface when your app is relaunched, call this method to let UIKit know that it should use your app’s default launch image instead of the snapshot.

You must call this method from within the code you use to preserve your app’s state.

## See Also

### Managing state restoration

- [- extendStateRestoration](<extendstaterestoration().md>) — Tells the app that your code is restoring state asynchronously.
- [- completeStateRestoration](<completestaterestoration().md>) — Tells the app that your code has finished any asynchronous state restoration.
- [+ registerObjectForStateRestoration:restorationIdentifier:](<registerobject(forstaterestoration_restorationidentifier_).md>) — Registers a custom object for use with the state restoration system.
