---
title: contentTypesForRecentDocuments
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/contenttypesforrecentdocuments
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/contenttypesforrecentdocuments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/contenttypesforrecentdocuments.json'
content_hash: 'sha256:ed8d44b25862085f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# contentTypesForRecentDocuments

<sub>Instance Property</sub>

Content types for browsing recent documents.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var contentTypesForRecentDocuments: [UTType] { get }
```

## Discussion

The default list is the same as the list of content types you provide to the initializer, or the types you define in [CFBundleDocumentTypes](../../bundleresources/information-property-list/cfbundledocumenttypes.md) in the app’s `Info.plist` file.

You can define a subset of these types using the `UIDocumentBrowserRecentDocumentContentTypes` key in the app’s `Info.plist` file.

## See Also

### Configuring a document browser

- [allowsDocumentCreation](allowsdocumentcreation.md) — A Boolean value that determines whether the document browser can create new documents.
- [allowsPickingMultipleItems](allowspickingmultipleitems.md) — A Boolean value that determines whether the user can select and open more than one document at a time.
- [- revealDocumentAtURL:importIfNeeded:completion:](<revealdocument(at_importifneeded_completion_).md>) — Reveals, and optionally imports, the document at the provided URL.
