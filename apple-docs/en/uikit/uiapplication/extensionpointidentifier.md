---
title: UIApplication.ExtensionPointIdentifier
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/extensionpointidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/extensionpointidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/extensionpointidentifier.json'
content_hash: 'sha256:0a46b8785b62dc46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# UIApplication.ExtensionPointIdentifier

<sub>Structure</sub>

A structure that identifies types of extensions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct ExtensionPointIdentifier
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIApplicationKeyboardExtensionPointIdentifier](extensionpointidentifier/keyboard.md) — The identifier for custom keyboards.

### Initializers

- [init(rawValue:)](<extensionpointidentifier/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

## See Also

### Disallowing specified app extension types

- [- application:shouldAllowExtensionPointIdentifier:](<../uiapplicationdelegate/application(__shouldallowextensionpointidentifier_).md>) — Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [UIApplicationKeyboardExtensionPointIdentifier](extensionpointidentifier/keyboard.md) — The identifier for custom keyboards.
