---
title: 'readAdditionalContent(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimanageddocument/readadditionalcontent(from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/readadditionalcontent(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/readadditionalcontent%28from%3A%29.json'
content_hash: 'sha256:5aa5ea891e242301'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# readAdditionalContent(from:)

<sub>Instance Method</sub>

Handles reading non-Core Data content in the additional content directory in the document’s file package.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func readAdditionalContent(from absoluteURL: URL) throws
```

## Parameters

- `absoluteURL` — The URL for the additional content directory in the document’s file package.

## Discussion

You override this method to read non-Core Data content from the additional content directory in the document’s file package.

If you implement this method, it’s invoked automatically by [- readFromURL:error:](<../uidocument/read(from_).md>).

There’s no need to invoke `super`’s implementation.

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

### Special considerations

Additional content isn’t supported on iCloud.

## See Also

### Customizing read and write operations

- [- additionalContentForURL:error:](<additionalcontent(for_).md>) — Handles writing non-Core Data content to the additional content directory in the document’s file package.
- [- writeAdditionalContent:toURL:originalContentsURL:error:](<writeadditionalcontent(__to_originalcontentsurl_).md>) — Handles writing non-Core Data content to the document’s file package.
