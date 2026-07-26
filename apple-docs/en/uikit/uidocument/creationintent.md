---
title: UIDocument.CreationIntent
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/creationintent
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/creationintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/creationintent.json'
content_hash: 'sha256:c5ed716a4648a361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# UIDocument.CreationIntent

<sub>Structure</sub>

An app intent that creates new documents for your app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct CreationIntent
```

## Overview

UIKit provides a default intent. You can extend this structure to provide additional intents for your app.

```swift
// Extend the creation intent enumeration to add custom options for document creation.
extension UIDocument.CreationIntent {
    static let template = UIDocument.CreationIntent("template")
}
```

For more information, see [Customizing a document-based app’s launch experience](../customizing-a-document-based-app-s-launch-experience.md).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accessing creation intents

- [UIDocumentCreationIntentDefault](creationintent/default.md) — The default document creation intent.

### Creating new intents

- [init(_:)](<creationintent/init(__).md>) — Create a new document creation intent using the provided string.
- [init(rawValue:)](<creationintent/init(rawvalue_).md>) — Create a new document creation intent using the provided string.
