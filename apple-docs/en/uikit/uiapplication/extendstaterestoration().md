---
title: extendStateRestoration()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/extendstaterestoration()
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/extendstaterestoration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/extendstaterestoration%28%29.json'
content_hash: 'sha256:5b5f3b898b3a3418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# extendStateRestoration()

<sub>Instance Method</sub>

Tells the app that your code is restoring state asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func extendStateRestoration()
```

## Discussion

UIKit restores your app’s state synchronously on the main thread. If you choose to perform additional state restoration on a secondary thread, call this method to inform UIKit of that fact. You must balance each call to this method with a matching call to the [- completeStateRestoration](<completestaterestoration().md>) method.

Calling this method is a safety precaution in the event that your app crashes at launch time due to problems restoring its state. If you call this method but do not call the matching [- completeStateRestoration](<completestaterestoration().md>) method before a crash occurs, the system throws away any saved state information. Doing so prevents your app from crashing during subsequent launches because of issues caused by trying to restore your app’s state.

## See Also

### Managing state restoration

- [- completeStateRestoration](<completestaterestoration().md>) — Tells the app that your code has finished any asynchronous state restoration.
- [- ignoreSnapshotOnNextApplicationLaunch](<ignoresnapshotonnextapplicationlaunch().md>) — Prevents the app from using the recent snapshot image during the next launch cycle.
- [+ registerObjectForStateRestoration:restorationIdentifier:](<registerobject(forstaterestoration_restorationidentifier_).md>) — Registers a custom object for use with the state restoration system.
