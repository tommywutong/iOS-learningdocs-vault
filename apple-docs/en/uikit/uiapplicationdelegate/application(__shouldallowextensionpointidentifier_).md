---
title: 'application(_:shouldAllowExtensionPointIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:shouldallowextensionpointidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:shouldallowextensionpointidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Ashouldallowextensionpointidentifier%3A%29.json'
content_hash: 'sha256:4f910785fdf95e26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:shouldAllowExtensionPointIdentifier:)

<sub>Instance Method</sub>

Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func application(_ application: UIApplication, shouldAllowExtensionPointIdentifier extensionPointIdentifier: UIApplication.ExtensionPointIdentifier) -> Bool
```

## Parameters

- `application` — Your shared app object.

- `extensionPointIdentifier` — A constant identifying an extension point.

## Return Value

[false](../../swift/false.md) to disallow use of a specified app extension type, or [true](../../swift/true.md) to allow use of the type.

## Discussion

You can implement this method to reject a specified type of app extension, based on its extension point identifier, from use in your app. See Extension Point Identifier Constants in [UIApplication](../uiapplication.md).

If you do not implement this method, all app extension types are available for use in your app.

In iOS 8.0, the only type of app extension you can reject is the custom keyboard. For information on app extensions, see [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## See Also

### Disallowing specified app extension types

- [ExtensionPointIdentifier](../uiapplication/extensionpointidentifier.md) — A structure that identifies types of extensions.
- [UIApplicationKeyboardExtensionPointIdentifier](../uiapplication/extensionpointidentifier/keyboard.md) — The identifier for custom keyboards.
