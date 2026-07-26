---
title: 'init(forOpeningFilesWithContentTypes:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+（14.0 起废弃）, iPadOS 11.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/init%28foropeningfileswithcontenttypes%3A%29.json'
content_hash: 'sha256:ad877f8b8c2bbd23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# init(forOpeningFilesWithContentTypes:)

<sub>Initializer</sub>

Initializes and returns a document browser view controller that can open the specified file types.

> [!warning] Deprecated
> Use [- initForOpeningContentTypes:](<init(foropening_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(forOpeningFilesWithContentTypes allowedContentTypes: [String]?)
```

## Parameters

- `allowedContentTypes` — An array of uniform type identifiers (UTIs). The document browser can open only the document types that these UTIs specify.  If you pass `nil`, the browser uses the document types that the `CFBundleDocumentTypes` key specifies in the app’s `Info.plist` file. For detailed instructions about setting the `CFBundleDocumentTypes` key, see the [Set the supported document types](../setting-up-a-document-browser-app.md#Set-the-supported-document-types) section of [Setting up a document browser app](../setting-up-a-document-browser-app.md). For more information about UTIs, see [Uniform Type Identifiers](../../uniformtypeidentifiers.md).

## Return Value

Returns a newly initialized document browser view controller.

## See Also

### Deprecated symbols

- [recentDocumentsContentTypes](recentdocumentscontenttypes.md) — Content types for browsing recent documents. _(deprecated)_
- [allowedContentTypes](allowedcontenttypes.md) — The document types that the browser can open. _(deprecated)_
- [- transitionControllerForDocumentURL:](<transitioncontroller(fordocumenturl_).md>) — Creates a transition controller that provides the standard system-loading and segue animations for the document browser. _(deprecated)_
