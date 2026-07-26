---
title: completeStateRestoration()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/completestaterestoration()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/completestaterestoration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/completestaterestoration%28%29.json'
content_hash: 'sha256:6fd5ac36f8e426fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# completeStateRestoration()

<sub>Instance Method</sub>

Tells the app that your code has finished any asynchronous state restoration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func completeStateRestoration()
```

## Discussion

UIKit restores your app’s state synchronously on the main thread. If you choose to perform additional state restoration on a secondary thread, call the [- extendStateRestoration](<extendstaterestoration().md>) method to inform UIKit of that fact. Call this method after you finish with your background work to let the system know that state restoration is complete.

## See Also

### Managing state restoration

- [- extendStateRestoration](<extendstaterestoration().md>) — Tells the app that your code is restoring state asynchronously.
- [- ignoreSnapshotOnNextApplicationLaunch](<ignoresnapshotonnextapplicationlaunch().md>) — Prevents the app from using the recent snapshot image during the next launch cycle.
- [+ registerObjectForStateRestoration:restorationIdentifier:](<registerobject(forstaterestoration_restorationidentifier_).md>) — Registers a custom object for use with the state restoration system.
