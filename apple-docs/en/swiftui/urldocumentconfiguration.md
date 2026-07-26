---
title: URLDocumentConfiguration
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/urldocumentconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/urldocumentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/urldocumentconfiguration.json'
content_hash: 'sha256:60efceff883eef29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# URLDocumentConfiguration

<sub>Class</sub>

The configuration of an open document that stores its file URL, last modification date, and related metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor final class URLDocumentConfiguration
```

## Overview

SwiftUI passes a `URLDocumentConfiguration` to the `makeDocument` closure of [DocumentGroup](documentgroup.md). This class is `@Observable` — views and other observers can track changes to [fileURL](urldocumentconfiguration/fileurl.md) and other properties.

Use [makeFileCoordinator()](<urldocumentconfiguration/makefilecoordinator().md>) to perform coordinated reads or writes outside the normal [DocumentReader](documentreader.md)/[DocumentWriter](documentwriter.md) flow — for example, to read a single sub-file of a package document on demand:

```swift
let coordinator = configuration.makeFileCoordinator()
var error: NSError?
coordinator.coordinate(
    readingItemAt: pageURL, options: [], error: &error
) { url in
    let data = try? Data(contentsOf: url)
    // ...
}
```

> [!important] Important
> Inside [read(from:progress:)](<documentreader/read(from_progress_).md>) and `DocumentWriter/write(content:to:previous:progress:)`, use the `source` / `destination` URL parameter — not [fileURL](urldocumentconfiguration/fileurl.md). The configuration’s URL reflects current state and may differ from the operation’s URL after a Save As or rename.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing document properties

- [fileURL](urldocumentconfiguration/fileurl.md) — A URL of the open document if it is saved to disk. _(beta)_
- [lastContentModificationDate](urldocumentconfiguration/lastcontentmodificationdate.md) — The date on which the contents of the document were last modified, if available. _(beta)_
- [creationSource](urldocumentconfiguration/creationsource.md) — The source associated with the button that created this document. _(beta)_

### Coordinating file access

- [makeFileCoordinator()](<urldocumentconfiguration/makefilecoordinator().md>) — Creates a file coordinator for coordinated disk access outside the normal read/write flow. _(beta)_

## See Also

### Storing document data in a reference type instance

- [Document](document.md) — A document that supports both reading and writing. _(beta)_
- [ReadableDocument](readabledocument.md) — A document type that supports reading from file. _(beta)_
- [WritableDocument](writabledocument.md) — A document type that supports writing to file. _(beta)_
- [DocumentCreationContext](documentcreationcontext.md) — Context about how a document was created. _(beta)_
- [DocumentBaseBox](documentbasebox.md) — A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.
