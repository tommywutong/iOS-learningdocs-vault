---
title: 'applicationShouldAutomaticallyLocalizeKeyCommands(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands%28_%3A%29.json'
content_hash: 'sha256:3554698d7f705552'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationShouldAutomaticallyLocalizeKeyCommands(_:)

<sub>Instance Method</sub>

Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationShouldAutomaticallyLocalizeKeyCommands(_ application: UIApplication) -> Bool
```

## Parameters

- `application` — The singleton app object.

## Return Value

[true](../../swift/true.md) to enable automatic shortcut localization for all app-specific menus, or [false](../../swift/false.md) to handle shortcut localization yourself.

## Discussion

A keyboard shortcut you specify in one language might be difficult or impossible to reproduce on a keyboard with a different character set or layout. Localized keyboards sometimes rearrange punctuation marks or replace them altogether to make room for a language’s required characters. The new locations of those keys might make it difficult to use your current shortcuts. To ensure your shortcuts are always usable, the system can automatically remap shortcuts, as needed, to accommodate the connected keyboard.

If you don’t implement this method, or if you implement it and return [true](../../swift/true.md), the system automatically remaps all app-specific key-command shortcuts that are unreachable on the current keyboard. The system doesn’t remap shortcuts when the input keys have identical positions on both keyboards, or when a shortcut is still easily reachable on the current keyboard. The remapping is transparent to your app.

If you already localize your app’s key-command shortcuts for different languages, or if you allow someone to customize your app’s shortcuts, you can return [false](../../swift/false.md) to disable the automatic remapping behavior. When you return [false](../../swift/false.md), the system doesn’t change your app’s shortcuts. Instead, you are responsible to make any required changes to support localized keyboards.

During the final activation of your app at launch time, the app object calls this method once to record your app’s response.
