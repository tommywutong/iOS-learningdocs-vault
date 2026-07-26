---
title: 'writeAdditionalContent(_:to:originalContentsURL:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/writeadditionalcontent%28_%3Ato%3Aoriginalcontentsurl%3A%29.json'
content_hash: 'sha256:d49f38c9a4e3042e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# writeAdditionalContent(_:to:originalContentsURL:)

<sub>Instance Method</sub>

Handles writing non-Core Data content to the document’s file package.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func writeAdditionalContent(_ content: Any, to absoluteURL: URL, originalContentsURL absoluteOriginalContentsURL: URL?) throws
```

## Parameters

- `content` — An object that represents the additional content for the document. This is the object returned from [- additionalContentForURL:error:](<additionalcontent(for_).md>).

- `absoluteURL` — The URL to which to write the additional content.

- `absoluteOriginalContentsURL` — The current URL of the document that’s being saved.

## Discussion

You override this method to perform to write non-Core Data content in the additional content directory in the document’s file package. There are several issues to consider:

- You should typically implement this method only if you also implemented [- additionalContentForURL:error:](<additionalcontent(for_).md>).
- Because this method is executed asynchronously, it’s possible that the document’s state may be different from that at which the save operation was initiated. If you need to capture the document state at save time, you should do so in [- additionalContentForURL:error:](<additionalcontent(for_).md>).
- If you implement this method, it’s invoked automatically by [- writeContents:andAttributes:safelyToURL:forSaveOperation:error:](<../uidocument/writecontents(__andattributes_safelyto_for_).md>).
- There’s no need to invoke `super`’s implementation.

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

### Special considerations

Additional content isn’t supported on iCloud.

## See Also

### Customizing read and write operations

- [- readAdditionalContentFromURL:error:](<readadditionalcontent(from_).md>) — Handles reading non-Core Data content in the additional content directory in the document’s file package.
- [- additionalContentForURL:error:](<additionalcontent(for_).md>) — Handles writing non-Core Data content to the additional content directory in the document’s file package.
