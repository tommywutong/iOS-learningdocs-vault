---
title: 'application(_:willEncodeRestorableStateWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:willencoderestorablestatewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:willencoderestorablestatewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Awillencoderestorablestatewith%3A%29.json'
content_hash: 'sha256:e0a34e23daec9212'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:willEncodeRestorableStateWith:)

<sub>Instance Method</sub>

Tells your delegate to save any high-level state information at the beginning of the state preservation process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, willEncodeRestorableStateWith coder: NSCoder)
```

## Parameters

- `application` — Your singleton app object.

- `coder` — The keyed archiver in which to write any state information.

## Discussion

The state preservation system calls this method at the beginning of the preservation process. This is your opportunity to add any app-level information to state information. For example, you might use this method to write version information or the high-level configuration of your app.

> [!important] Important
> This method is not a substitute for saving your app’s data structures persistently to disk. You should continue to save your app’s actual data to iCloud or the local file system using existing techniques. This method is intended only for saving configuration state or other information related to your app’s user interface. You should consider the data in the coder as purgeable and be prepared for it to be unavailable during subsequent launches.

Your implementation of this method can encode restorable view and view controller objects that it needs to reference. Encoding a restorable view or view controller writes that object’s restoration identifier to the coder. (That identifier is used during the decode process to locate the new version of the object.) If the view or view controller defines a [- encodeRestorableStateWithCoder:](<../uiviewcontroller/encoderestorablestate(with_).md>) method, that method is also called at some point so that the object can encode its own state.

Apart from views and view controllers, other objects follow the normal serialization process and must adopt the [NSCoding](../../foundation/nscoding.md) protocol before they can be encoded. Encoding such objects embeds the object’s contents in the archive directly. During the decode process, a new object is created and initialized with the data from the archive.

## See Also

### Managing app state restoration

- [- application:shouldSaveSecureApplicationState:](<application(__shouldsavesecureapplicationstate_).md>) — Asks the delegate whether to securely preserve the app’s state.
- [- application:shouldRestoreSecureApplicationState:](<application(__shouldrestoresecureapplicationstate_).md>) — Asks the delegate whether to restore the app’s saved state.
- [- application:viewControllerWithRestorationIdentifierPath:coder:](<application(__viewcontrollerwithrestorationidentifierpath_coder_).md>) — Asks the delegate to provide the specified view controller.
- [- application:didDecodeRestorableStateWithCoder:](<application(__diddecoderestorablestatewith_).md>) — Tells your delegate to restore any high-level state information as part of the state restoration process.
- [UIApplicationStateRestorationBundleVersionKey](../uiapplication/staterestorationbundleversionkey.md) — The version of your app responsible for creating the restoration archive.
- [UIApplicationStateRestorationSystemVersionKey](../uiapplication/staterestorationsystemversionkey.md) — The version of the system on which your app created the restoration archive.
- [UIApplicationStateRestorationTimestampKey](../uiapplication/staterestorationtimestampkey.md) — The time your app created the restoration archive.
- [UIApplicationStateRestorationUserInterfaceIdiomKey](../uiapplication/staterestorationuserinterfaceidiomkey.md) — The user interface idiom that was in effect when your app created the restoration archive.
- [UIStateRestorationViewControllerStoryboardKey](../uiapplication/staterestorationviewcontrollerstoryboardkey.md) — A reference to the storyboard that contains the view controller.
