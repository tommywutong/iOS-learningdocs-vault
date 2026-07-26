---
title: stateRestorationUserInterfaceIdiomKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/staterestorationuserinterfaceidiomkey
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/staterestorationuserinterfaceidiomkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/staterestorationuserinterfaceidiomkey.json'
content_hash: 'sha256:f5872328a2c28a63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# stateRestorationUserInterfaceIdiomKey

<sub>Type Property</sub>

The user interface idiom that was in effect when your app created the restoration archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let stateRestorationUserInterfaceIdiomKey: String
```

## Discussion

The value of this key is an [NSNumber](../../foundation/nsnumber.md) object containing one of the values for the [UIUserInterfaceIdiom](../uiuserinterfaceidiom.md) enum. This value reflects whether the interface that was saved was targeting the iPad or iPhone idiom.

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
- [UIStateRestorationViewControllerStoryboardKey](staterestorationviewcontrollerstoryboardkey.md) — A reference to the storyboard that contains the view controller.
