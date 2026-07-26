---
title: allowsAutomaticLocalization
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand/allowsautomaticlocalization
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/allowsautomaticlocalization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/allowsautomaticlocalization.json'
content_hash: 'sha256:d0d7383c41012fdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# allowsAutomaticLocalization

<sub>Instance Property</sub>

A Boolean value that determines whether the system automatically remaps keyboard shortcuts based on the keyboard layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsAutomaticLocalization: Bool { get set }
```

## Discussion

A keyboard shortcut you specify in one language might be difficult or impossible to reproduce on a keyboard with a different character set or layout. Localized keyboards sometimes rearrange punctuation marks or replace them altogether to make room for a language’s required characters. The new locations of those keys might make it difficult to use your key command’s current shortcut. To ensure your shortcuts are always usable, the system can automatically remap shortcuts, as needed, to accommodate the connected keyboard.

When the value of this property is [true](../../swift/true.md), the system automatically remaps this key command’s shortcut when that shortcut is unreachable on the current keyboard. The system doesn’t remap shortcuts when the input keys have identical positions on both keyboards, or when the shortcut is still easily reachable on the current keyboard. The remapping is transparent to your app.

If you already localize your app’s shortcuts for different languages, or if you allow someone to customize your app’s shortcuts, you can set this property to [false](../../swift/false.md) to disable the automatic remapping behavior. When you set this property to [false](../../swift/false.md), the system doesn’t change the shortcut for your key commands. Instead, you’re responsible for making any required changes to support localized keyboards. Setting this property to [false](../../swift/false.md) also disables the automatic mirroring of shortcuts, as described by the [allowsAutomaticMirroring](allowsautomaticmirroring.md) property.

The default value of this property is [true](../../swift/true.md).

## See Also

### Related Documentation

- [- applicationShouldAutomaticallyLocalizeKeyCommands:](<../uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands(__).md>) — Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.

### Localizing keyboard shortcuts

- [allowsAutomaticMirroring](allowsautomaticmirroring.md) — A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.
