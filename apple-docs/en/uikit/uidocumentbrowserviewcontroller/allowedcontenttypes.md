---
title: allowedContentTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（14.0 起废弃）, iPadOS 11.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentbrowserviewcontroller/allowedcontenttypes
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowedcontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/allowedcontenttypes.json'
content_hash: 'sha256:c5811672971322bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# allowedContentTypes

<sub>Instance Property</sub>

The document types that the browser can open.

> [!warning] Deprecated
> Use [- initForOpeningContentTypes:](<init(foropening_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowedContentTypes: [String] { get }
```

## Discussion

This property contains an array of uniform type identifiers (UTIs). The document browser can open only documents of the types specified by these UTIs.

The list of UTIs is set when the document browser is first created. This list cannot be changed.If you programmatically create a document browser, this list is set to the value passed to the [- initForOpeningFilesWithContentTypes:](<init(foropeningfileswithcontenttypes_).md>) method’s `allowedContentTypes` parameter.

If you add a document browser to your project using a storyboard or Interface Builder, this property is calculated based on the the `CFBundleDocumentTypes` key in your app’s `Info.plist` file. For details, see [Set the supported document types](../setting-up-a-document-browser-app.md#Set-the-supported-document-types).

For more about UTIs, see [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257).

## See Also

### Deprecated symbols

- [- initForOpeningFilesWithContentTypes:](<init(foropeningfileswithcontenttypes_).md>) — Initializes and returns a document browser view controller that can open the specified file types. _(deprecated)_
- [recentDocumentsContentTypes](recentdocumentscontenttypes.md) — Content types for browsing recent documents. _(deprecated)_
- [- transitionControllerForDocumentURL:](<transitioncontroller(fordocumenturl_).md>) — Creates a transition controller that provides the standard system-loading and segue animations for the document browser. _(deprecated)_
