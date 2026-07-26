---
title: allowsAutomaticMirroring
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand/allowsautomaticmirroring
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/allowsautomaticmirroring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/allowsautomaticmirroring.json'
content_hash: 'sha256:58cee4648bc2d5ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# allowsAutomaticMirroring

<sub>Instance Property</sub>

A Boolean value that determines whether the system automatically swaps input strings for some keyboard shortcuts when the interface direction changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsAutomaticMirroring: Bool { get set }
```

## Discussion

When a key command represents a direction-related action, it’s common to specify an input string that conveys that direction. For example, Safari uses Command-[ to go back to the previous page, and Command-] to go forward to the next page. Because directions are different in left-to-right and right-to-left interfaces, this property lets the system swap some input strings to match the current language direction.

When the value of this property is [true](../../swift/true.md), iOS 15 and later automatically swaps input strings that contain brackets `[]`, braces `{}`, parenthesis `()`, angle brackets `<>`, or arrow keys when the interface directionality changes. This behavior eliminates the need for you to create different key commands for left-to-right and right-to-left interfaces. Set this property to [false](../../swift/false.md) if you already change this item’s shortcut to support both left-to-right and right-to-left interfaces. You might also set it to [false](../../swift/false.md) to keep the same shortcut regardless of the interface’s directionality.

The default value of this property is [true](../../swift/true.md). However, if you set the [allowsAutomaticLocalization](allowsautomaticlocalization.md) property to [false](../../swift/false.md), the system disables this feature regardless of the property’s value.

## See Also

### Localizing keyboard shortcuts

- [allowsAutomaticLocalization](allowsautomaticlocalization.md) — A Boolean value that determines whether the system automatically remaps keyboard shortcuts based on the keyboard layout.
