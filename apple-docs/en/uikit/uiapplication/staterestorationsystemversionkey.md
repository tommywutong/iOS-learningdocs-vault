---
title: stateRestorationSystemVersionKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/staterestorationsystemversionkey
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/staterestorationsystemversionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/staterestorationsystemversionkey.json'
content_hash: 'sha256:100cf2856fd9939a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# stateRestorationSystemVersionKey

<sub>Type Property</sub>

The version of the system on which your app created the restoration archive.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let stateRestorationSystemVersionKey: String
```

## Discussion

The value of this key is an [NSString](../../foundation/nsstring.md) object containing the iOS system version that was installed when the archive was saved. The format of this string matches the format of the value in the [systemVersion](../uidevice/systemversion.md) property of the [UIDevice](../uidevice.md) class.

## See Also

### Managing app state restoration

- [- application:shouldSaveSecureApplicationState:](<../uiapplicationdelegate/application(__shouldsavesecureapplicationstate_).md>) — Asks the delegate whether to securely preserve the app’s state.
- [- application:shouldRestoreSecureApplicationState:](<../uiapplicationdelegate/application(__shouldrestoresecureapplicationstate_).md>) — Asks the delegate whether to restore the app’s saved state.
- [- application:viewControllerWithRestorationIdentifierPath:coder:](<../uiapplicationdelegate/application(__viewcontrollerwithrestorationidentifierpath_coder_).md>) — Asks the delegate to provide the specified view controller.
- [- application:willEncodeRestorableStateWithCoder:](<../uiapplicationdelegate/application(__willencoderestorablestatewith_).md>) — Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [- application:didDecodeRestorableStateWithCoder:](<../uiapplicationdelegate/application(__diddecoderestorablestatewith_).md>) — Tells your delegate to restore any high-level state information as part of the state restoration process.
- [UIApplicationStateRestorationBundleVersionKey](staterestorationbundleversionkey.md) — The version of your app responsible for creating the restoration archive.
- [UIApplicationStateRestorationTimestampKey](staterestorationtimestampkey.md) — The time your app created the restoration archive.
- [UIApplicationStateRestorationUserInterfaceIdiomKey](staterestorationuserinterfaceidiomkey.md) — The user interface idiom that was in effect when your app created the restoration archive.
- [UIStateRestorationViewControllerStoryboardKey](staterestorationviewcontrollerstoryboardkey.md) — A reference to the storyboard that contains the view controller.
