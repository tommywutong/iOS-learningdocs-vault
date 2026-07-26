---
title: 'createSymbolicLink(at:withDestinationURL:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/createsymboliclink(at:withdestinationurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/createsymboliclink(at:withdestinationurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/createsymboliclink%28at%3Awithdestinationurl%3A%29.json'
content_hash: 'sha256:8642d7f0d36d95be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# createSymbolicLink(at:withDestinationURL:)

<sub>Instance Method</sub>

Creates a symbolic link at the specified URL that points to an item at the given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func createSymbolicLink(at url: URL, withDestinationURL destURL: URL) throws
```

## Parameters

- `url` — The file URL at which to create the new symbolic link. The last path component of the URL issued as the name of the link.

- `destURL` — The file URL that contains the item to be pointed to by the link. In other words, this is the destination of the link.

## Discussion

This method does not traverse symbolic links contained in `destURL`, making it possible to create symbolic links to locations that do not yet exist. Also, if the final path component in `url` is a symbolic link, that link is not followed.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Creating symbolic and hard links

- [- createSymbolicLinkAtPath:withDestinationPath:error:](<createsymboliclink(atpath_withdestinationpath_).md>) — Creates a symbolic link that points to the specified destination.
- [- linkItemAtURL:toURL:error:](<linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.
- [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) — Returns the path of the item pointed to by a symbolic link.
