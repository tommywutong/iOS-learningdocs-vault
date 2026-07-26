---
title: keyboard
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/extensionpointidentifier/keyboard
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/extensionpointidentifier/keyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/extensionpointidentifier/keyboard.json'
content_hash: 'sha256:bace004454fc706d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [ExtensionPointIdentifier](../extensionpointidentifier.md)

# keyboard

<sub>Type Property</sub>

The identifier for custom keyboards.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let keyboard: UIApplication.ExtensionPointIdentifier
```

## Discussion

To reject the use of custom keyboards in your app, specify this constant in your implementation of the [- application:shouldAllowExtensionPointIdentifier:](<../../uiapplicationdelegate/application(__shouldallowextensionpointidentifier_).md>) delegate method.

## See Also

### Disallowing specified app extension types

- [- application:shouldAllowExtensionPointIdentifier:](<../../uiapplicationdelegate/application(__shouldallowextensionpointidentifier_).md>) — Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [ExtensionPointIdentifier](../extensionpointidentifier.md) — A structure that identifies types of extensions.
