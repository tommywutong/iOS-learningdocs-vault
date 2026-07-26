---
title: 'registerObject(forStateRestoration:restorationIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/registerobject(forstaterestoration:restorationidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/registerobject(forstaterestoration:restorationidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/registerobject%28forstaterestoration%3Arestorationidentifier%3A%29.json'
content_hash: 'sha256:d7700d4c708b4974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# registerObject(forStateRestoration:restorationIdentifier:)

<sub>Type Method</sub>

Registers a custom object for use with the state restoration system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func registerObject(forStateRestoration object: any UIStateRestoring, restorationIdentifier: String)
```

## Parameters

- `object` — The object to be registered with the restoration archive. The object must adopt the [UIStateRestoring](../uistaterestoring.md) protocol. This parameter must not be `nil`.

- `restorationIdentifier` — The restoration identifier for the object. UIKit uses this parameter to distinguish the object from other objects in the archive. This parameter must not be `nil`.

## Discussion

You use this method to register objects that you want to save as part of the overall state restoration process. Registering the object makes it available for inclusion in the restoration archive but does not automatically include it. To include the object, refer to it from one of your other interface objects. For example, you might write out a reference to the object from the [- encodeRestorableStateWithCoder:](<../uiviewcontroller/encoderestorablestate(with_).md>) method of one of your view controllers.

## See Also

### Managing state restoration

- [- extendStateRestoration](<extendstaterestoration().md>) — Tells the app that your code is restoring state asynchronously.
- [- completeStateRestoration](<completestaterestoration().md>) — Tells the app that your code has finished any asynchronous state restoration.
- [- ignoreSnapshotOnNextApplicationLaunch](<ignoresnapshotonnextapplicationlaunch().md>) — Prevents the app from using the recent snapshot image during the next launch cycle.
