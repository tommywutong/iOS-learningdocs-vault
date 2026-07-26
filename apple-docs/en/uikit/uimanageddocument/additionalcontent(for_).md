---
title: 'additionalContent(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimanageddocument/additionalcontent(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimanageddocument/additionalcontent(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimanageddocument/additionalcontent%28for%3A%29.json'
content_hash: 'sha256:25158b48239ac3fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIManagedDocument](../uimanageddocument.md)

# additionalContent(for:)

<sub>Instance Method</sub>

Handles writing non-Core Data content to the additional content directory in the document’s file package.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func additionalContent(for absoluteURL: URL) throws -> Any
```

## Parameters

- `absoluteURL` — The URL for the additional content directory in the document’s file package.

## Return Value

An object that contains the additional content for the document at `absoluteURL`, or `nil` if there is a problem.

## Discussion

You override this method to perform to manage non-Core Data content to be stored in the additional content directory in the document’s file package.

If you implement this method, it’s invoked automatically by [- contentsForType:error:](<../uidocument/contents(fortype_).md>). The returned object is passed to [- writeAdditionalContent:toURL:originalContentsURL:error:](<writeadditionalcontent(__to_originalcontentsurl_).md>).

There’s no need to invoke `super`’s implementation.

> [!note] Handling Errors in Swift
> In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> When overriding this method, use the `throw` statement to throw an `NSError`, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

### Special considerations

A return value of `nil` indicates an error condition. To avoid generating an exception, you must return a value from this method. If it isn’t always the case that there will be additional content, you should return a sentinel value (for example, an [NSNull](../../foundation/nsnull.md) instance) that you check for in [- writeAdditionalContent:toURL:originalContentsURL:error:](<writeadditionalcontent(__to_originalcontentsurl_).md>).

The object returned from this method is passed to [- writeAdditionalContent:toURL:originalContentsURL:error:](<writeadditionalcontent(__to_originalcontentsurl_).md>). Because [- writeAdditionalContent:toURL:originalContentsURL:error:](<writeadditionalcontent(__to_originalcontentsurl_).md>) is executed on a different thread, you must ensure that the object you return is thread-safe. For example, you might return an [NSData](../../foundation/nsdata.md) object containing an archive of the state you want to capture.

Additional content isn’t supported on iCloud.

## See Also

### Customizing read and write operations

- [- readAdditionalContentFromURL:error:](<readadditionalcontent(from_).md>) — Handles reading non-Core Data content in the additional content directory in the document’s file package.
- [- writeAdditionalContent:toURL:originalContentsURL:error:](<writeadditionalcontent(__to_originalcontentsurl_).md>) — Handles writing non-Core Data content to the document’s file package.
