---
title: activeDocumentCreationIntent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/activedocumentcreationintent
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/activedocumentcreationintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/activedocumentcreationintent.json'
content_hash: 'sha256:3e5335306e5f6a7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# activeDocumentCreationIntent

<sub>Instance Property</sub>

The current intent that defines how your app creates a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activeDocumentCreationIntent: UIDocument.CreationIntent? { get }
```

## Discussion

Use this property to access the current intent. For more information, see [Customizing a document-based app’s launch experience](../customizing-a-document-based-app-s-launch-experience.md).
