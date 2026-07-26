---
title: stateRestorationBundleVersionKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/staterestorationbundleversionkey
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/staterestorationbundleversionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/staterestorationbundleversionkey.json'
content_hash: 'sha256:5d6a3f74986ae239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# stateRestorationBundleVersionKey

<sub>Type Property</sub>

The version of your app responsible for creating the restoration archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let stateRestorationBundleVersionKey: String
```

## Discussion

The value of this key is an [NSString](../../foundation/nsstring.md) object that identifies the version of your app (as obtained from the `CFBundleVersion` key of your app’s `Info.plist` file) that was present when the state information was saved. You can use the value of this key to help make choices about how to proceed during state restoration. For example, if the key indicates that the state is associated with an older version of your app, you might want to avoid restoring the previous state altogether or modify the restoration process more significantly.

## See Also

### Managing app state restoration

- [- application:shouldSaveSecureApplicationState:](<../uiapplicationdelegate/application(__shouldsavesecureapplicationstate_).md>) — Asks the delegate whether to securely preserve the app’s state.
- [- application:shouldRestoreSecureApplicationState:](<../uiapplicationdelegate/application(__shouldrestoresecureapplicationstate_).md>) — Asks the delegate whether to restore the app’s saved state.
- [- application:viewControllerWithRestorationIdentifierPath:coder:](<../uiapplicationdelegate/application(__viewcontrollerwithrestorationidentifierpath_coder_).md>) — Asks the delegate to provide the specified view controller.
- [- application:willEncodeRestorableStateWithCoder:](<../uiapplicationdelegate/application(__willencoderestorablestatewith_).md>) — Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [- application:didDecodeRestorableStateWithCoder:](<../uiapplicationdelegate/application(__diddecoderestorablestatewith_).md>) — Tells your delegate to restore any high-level state information as part of the state restoration process.
- [UIApplicationStateRestorationSystemVersionKey](staterestorationsystemversionkey.md) — The version of the system on which your app created the restoration archive.
- [UIApplicationStateRestorationTimestampKey](staterestorationtimestampkey.md) — The time your app created the restoration archive.
- [UIApplicationStateRestorationUserInterfaceIdiomKey](staterestorationuserinterfaceidiomkey.md) — The user interface idiom that was in effect when your app created the restoration archive.
- [UIStateRestorationViewControllerStoryboardKey](staterestorationviewcontrollerstoryboardkey.md) — A reference to the storyboard that contains the view controller.
