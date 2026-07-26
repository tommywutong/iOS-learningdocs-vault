---
title: remove()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/remove()
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/remove()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/remove%28%29.json'
content_hash: 'sha256:786ba624d1433ff7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# remove()

<sub>Instance Method</sub>

Remove this version object and its associated file from the version store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove() throws
```

## Discussion

This method removes this version object and its file from the version store, freeing up the associated storage space. You must not call this method for the current file version—that is, the version object returned by the [+ currentVersionOfItemAtURL:](<currentversionofitem(at_).md>) method.

You should always remove file versions as part of a coordinated write operation to a file. In other words, always call this method from a block passed to a file coordinator object to initiate a write operation. Doing so ensures that no other processes are operating on the file while you remove the version information.

If successful, subsequent requests for the versions of the file do not include this version object (or any object with the same information). You can use this method to free up disk space by removing versions that are no longer needed.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Replacing and Deleting Versions

- [- replaceItemAtURL:options:error:](<replaceitem(at_options_).md>) — Replace the contents of the specified file with the contents of the current version’s file.
- [+ removeOtherVersionsOfItemAtURL:error:](<removeotherversionsofitem(at_).md>) — Removes all versions of a file, except the current one, from the version store.
