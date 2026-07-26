---
title: stateRestorationViewControllerStoryboardKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/staterestorationviewcontrollerstoryboardkey
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/staterestorationviewcontrollerstoryboardkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/staterestorationviewcontrollerstoryboardkey.json'
content_hash: 'sha256:19407f32b43e5877'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# stateRestorationViewControllerStoryboardKey

<sub>Type Property</sub>

A reference to the storyboard that contains the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let stateRestorationViewControllerStoryboardKey: String
```

## Discussion

The value of this key is a [UIStoryboard](../uistoryboard.md) object representing the storyboard from which a view controller was initially obtained. You don’t need to write this key to the coder yourself. Each [UIViewController](../uiviewcontroller.md) class automatically writes this key to the coder during the state preservation process.

## See Also

### Managing app state restoration

- [- application:shouldSaveSecureApplicationState:](<../uiapplicationdelegate/application(__shouldsavesecureapplicationstate_).md>) — Asks the delegate whether to securely preserve the app’s state.
- [- application:shouldRestoreSecureApplicationState:](<../uiapplicationdelegate/application(__shouldrestoresecureapplicationstate_).md>) — Asks the delegate whether to restore the app’s saved state.
- [- application:viewControllerWithRestorationIdentifierPath:coder:](<../uiapplicationdelegate/application(__viewcontrollerwithrestorationidentifierpath_coder_).md>) — Asks the delegate to provide the specified view controller.
- [- application:willEncodeRestorableStateWithCoder:](<../uiapplicationdelegate/application(__willencoderestorablestatewith_).md>) — Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [- application:didDecodeRestorableStateWithCoder:](<../uiapplicationdelegate/application(__diddecoderestorablestatewith_).md>) — Tells your delegate to restore any high-level state information as part of the state restoration process.
- [UIApplicationStateRestorationBundleVersionKey](staterestorationbundleversionkey.md) — The version of your app responsible for creating the restoration archive.
- [UIApplicationStateRestorationSystemVersionKey](staterestorationsystemversionkey.md) — The version of the system on which your app created the restoration archive.
- [UIApplicationStateRestorationTimestampKey](staterestorationtimestampkey.md) — The time your app created the restoration archive.
- [UIApplicationStateRestorationUserInterfaceIdiomKey](staterestorationuserinterfaceidiomkey.md) — The user interface idiom that was in effect when your app created the restoration archive.
