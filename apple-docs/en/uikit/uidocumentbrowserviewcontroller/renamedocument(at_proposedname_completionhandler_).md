---
title: 'renameDocument(at:proposedName:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentbrowserviewcontroller/renamedocument(at:proposedname:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/renamedocument(at:proposedname:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentbrowserviewcontroller/renamedocument%28at%3Aproposedname%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3690b191dfd526b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)

# renameDocument(at:proposedName:completionHandler:)

<sub>Instance Method</sub>

Renames a document at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func renameDocument(at documentURL: URL, proposedName: String, completionHandler: @escaping (URL?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func renameDocument(at documentURL: URL, proposedName: String) async throws -> URL
```

## Parameters

- `documentURL` — The URL specifying the location of the document.

- `proposedName` — The proposed new name to rename the document to. If `proposedName` is already taken, the system might alter the proposed name and confirm the new suggestion with the user. The final name that the system chooses appears in the `finalURL` parameter of `completionHandler`.

- `completionHandler` — A completion handler to execute after the renaming operation occurs. The final URL and error information are available in the completion handler. - **`finalURL`** — The URL of the newly renamed document, or `nil` if an error occurs. - **`error`** — An object that describes the error, if one occurs; otherwise, `nil`.
