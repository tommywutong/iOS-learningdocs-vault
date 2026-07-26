---
title: 'application(_:shouldSaveSecureApplicationState:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.2+, iPadOS 13.2+, Mac Catalyst 13.2+, tvOS 13.2+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldsavesecureapplicationstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ashouldsavesecureapplicationstate%3A%29.json'
content_hash: 'sha256:a1977aede8e1fb2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:shouldSaveSecureApplicationState:)

<sub>Instance Method</sub>

Asks the delegate whether to securely preserve the app’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, shouldSaveSecureApplicationState coder: NSCoder) -> Bool
```

## Parameters

- `application` — The singleton app object.

- `coder` — A keyed archiver where you can store high-level state information. The coder’s [requiresSecureCoding](../../foundation/nscoder/requiressecurecoding.md) property is set to [true](../../swift/true.md), and any objects you encode must adopt [NSSecureCoding](../../foundation/nssecurecoding.md).

## Return Value

[true](../../swift/true.md) to securely preserve the app’s state; otherwise, [false](../../swift/false.md).

## Discussion

Apps must implement both this method and [- application:shouldRestoreSecureApplicationState:](<application(__shouldrestoresecureapplicationstate_).md>) for state preservation to occur.

Your implementation of this method should return [true](../../swift/true.md) each time UIKit attempts to preserve the state of your app. You can temporarily disable state preservation by returning [false](../../swift/false.md), which you may want to do during testing, for example.

You can add version information or any other contextual data to the provided coder as necessary. During restoration, you can use that information to determine whether to proceed with restoring your app to its previous state. Any objects you add to the coder must adopt the [NSSecureCoding](../../foundation/nssecurecoding.md) protocol.

This method supersedes [- application:shouldSaveApplicationState:](<application(__shouldsaveapplicationstate_).md>). If your delegate implements both methods, the system only calls this one.

## See Also

### Managing app state restoration

- [- application:shouldRestoreSecureApplicationState:](<application(__shouldrestoresecureapplicationstate_).md>) — Asks the delegate whether to restore the app’s saved state.
- [- application:viewControllerWithRestorationIdentifierPath:coder:](<application(__viewcontrollerwithrestorationidentifierpath_coder_).md>) — Asks the delegate to provide the specified view controller.
- [- application:willEncodeRestorableStateWithCoder:](<application(__willencoderestorablestatewith_).md>) — Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [- application:didDecodeRestorableStateWithCoder:](<application(__diddecoderestorablestatewith_).md>) — Tells your delegate to restore any high-level state information as part of the state restoration process.
- [UIApplicationStateRestorationBundleVersionKey](../uiapplication/staterestorationbundleversionkey.md) — The version of your app responsible for creating the restoration archive.
- [UIApplicationStateRestorationSystemVersionKey](../uiapplication/staterestorationsystemversionkey.md) — The version of the system on which your app created the restoration archive.
- [UIApplicationStateRestorationTimestampKey](../uiapplication/staterestorationtimestampkey.md) — The time your app created the restoration archive.
- [UIApplicationStateRestorationUserInterfaceIdiomKey](../uiapplication/staterestorationuserinterfaceidiomkey.md) — The user interface idiom that was in effect when your app created the restoration archive.
- [UIStateRestorationViewControllerStoryboardKey](../uiapplication/staterestorationviewcontrollerstoryboardkey.md) — A reference to the storyboard that contains the view controller.
