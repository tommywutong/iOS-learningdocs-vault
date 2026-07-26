---
title: 'application(_:didDecodeRestorableStateWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:diddecoderestorablestatewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:diddecoderestorablestatewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Adiddecoderestorablestatewith%3A%29.json'
content_hash: 'sha256:a458013e1f3a4fb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:didDecodeRestorableStateWith:)

<sub>Instance Method</sub>

Tells your delegate to restore any high-level state information as part of the state restoration process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, didDecodeRestorableStateWith coder: NSCoder)
```

## Parameters

- `application` — Your singleton app object.

- `coder` — The keyed archiver containing the app’s previously saved state information.

## Discussion

The state restoration system calls this method as the final step in the state restoration process. By the time this method is called, all other restorable objects will have been restored and put back into their previous state. You can use this method to read any high-level app data you saved in the [- application:willEncodeRestorableStateWithCoder:](<application(__willencoderestorablestatewith_).md>) method and apply it to your app.

## See Also

### Managing app state restoration

- [- application:shouldSaveSecureApplicationState:](<application(__shouldsavesecureapplicationstate_).md>) — Asks the delegate whether to securely preserve the app’s state.
- [- application:shouldRestoreSecureApplicationState:](<application(__shouldrestoresecureapplicationstate_).md>) — Asks the delegate whether to restore the app’s saved state.
- [- application:viewControllerWithRestorationIdentifierPath:coder:](<application(__viewcontrollerwithrestorationidentifierpath_coder_).md>) — Asks the delegate to provide the specified view controller.
- [- application:willEncodeRestorableStateWithCoder:](<application(__willencoderestorablestatewith_).md>) — Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [UIApplicationStateRestorationBundleVersionKey](../uiapplication/staterestorationbundleversionkey.md) — The version of your app responsible for creating the restoration archive.
- [UIApplicationStateRestorationSystemVersionKey](../uiapplication/staterestorationsystemversionkey.md) — The version of the system on which your app created the restoration archive.
- [UIApplicationStateRestorationTimestampKey](../uiapplication/staterestorationtimestampkey.md) — The time your app created the restoration archive.
- [UIApplicationStateRestorationUserInterfaceIdiomKey](../uiapplication/staterestorationuserinterfaceidiomkey.md) — The user interface idiom that was in effect when your app created the restoration archive.
- [UIStateRestorationViewControllerStoryboardKey](../uiapplication/staterestorationviewcontrollerstoryboardkey.md) — A reference to the storyboard that contains the view controller.
