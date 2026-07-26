---
title: recentDocumentsContentTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（14.0 起废弃）, iPadOS 11.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/recentdocumentscontenttypes
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/recentdocumentscontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/recentdocumentscontenttypes.json'
content_hash: 'sha256:b6cae4e1923e881d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# recentDocumentsContentTypes

<sub>Instance Property</sub>

Content types for browsing recent documents.

> [!warning] Deprecated
> Use [contentTypesForRecentDocuments](contenttypesforrecentdocuments.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var recentDocumentsContentTypes: [String] { get }
```

## Discussion

The default list is the same as the list of content types provided to the initializer, or the types defined in [CFBundleDocumentTypes](../../bundleresources/information-property-list/cfbundledocumenttypes.md) in the app’s `Info.plist` file.

You can define a subset of these types using the key `UIDocumentBrowserRecentDocumentContentTypes` in the app’s `Info.plist` file.

## See Also

### Deprecated symbols

- [- initForOpeningFilesWithContentTypes:](<init(foropeningfileswithcontenttypes_).md>) — Initializes and returns a document browser view controller that can open the specified file types. _(deprecated)_
- [allowedContentTypes](allowedcontenttypes.md) — The document types that the browser can open. _(deprecated)_
- [- transitionControllerForDocumentURL:](<transitioncontroller(fordocumenturl_).md>) — Creates a transition controller that provides the standard system-loading and segue animations for the document browser. _(deprecated)_
