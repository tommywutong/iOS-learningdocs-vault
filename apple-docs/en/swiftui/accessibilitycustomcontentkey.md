---
title: AccessibilityCustomContentKey
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitycustomcontentkey
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitycustomcontentkey.json'
content_hash: 'sha256:315b24989169bb98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityCustomContentKey

<sub>Structure</sub>

Key used to specify the identifier and label associated with an entry of additional accessibility information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AccessibilityCustomContentKey
```

## Overview

Use `AccessibilityCustomContentKey` and the associated modifiers taking this value as a parameter in order to simplify clearing or replacing entries of additional information that are manipulated from multiple places in your code.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Creating a key

- [init(_:)](<accessibilitycustomcontentkey/init(__).md>) — Create an `AccessibilityCustomContentKey` with the specified label.
- [init(_:id:)](<accessibilitycustomcontentkey/init(__id_).md>) — Create an `AccessibilityCustomContentKey` with the specified label and identifier.

## See Also

### Adding custom descriptions

- [accessibilityCustomContent(_:_:importance:)](<view/accessibilitycustomcontent(____importance_).md>) — Add additional accessibility information to the view.
