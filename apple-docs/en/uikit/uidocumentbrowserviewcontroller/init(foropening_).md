---
title: 'init(forOpening:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontroller/init(foropening:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/init(foropening:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/init%28foropening%3A%29.json'
content_hash: 'sha256:25ee15aedd93a013'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# init(forOpening:)

<sub>Initializer</sub>

Initializes and returns a document browser view controller that can open the specified file types.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(forOpening contentTypes: [UTType]?)
```

## Parameters

- `contentTypes` — An array of uniform type identifiers. If `nil`, the browser uses the document types that the [CFBundleDocumentTypes](../../bundleresources/information-property-list/cfbundledocumenttypes.md) key specifies in the app’s `Info.plist` file. For detailed instructions about setting the `CFBundleDocumentTypes` key, see [Setting up a document browser app](../setting-up-a-document-browser-app.md). For more information about type identifiers, see [Uniform Type Identifiers](../../uniformtypeidentifiers.md).

## See Also

### Creating a document browser

- [Adding a document browser to your app](../adding-a-document-browser-to-your-app.md) — Give people access to their local or remote documents from within your app.
