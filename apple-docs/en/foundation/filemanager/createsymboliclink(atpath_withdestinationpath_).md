---
title: 'createSymbolicLink(atPath:withDestinationPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/createsymboliclink(atpath:withdestinationpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/createsymboliclink(atpath:withdestinationpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/createsymboliclink%28atpath%3Awithdestinationpath%3A%29.json'
content_hash: 'sha256:70e3116cf0ae497e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# createSymbolicLink(atPath:withDestinationPath:)

<sub>Instance Method</sub>

Creates a symbolic link that points to the specified destination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func createSymbolicLink(atPath path: String, withDestinationPath destPath: String) throws
```

## Parameters

- `path` — The path at which to create the new symbolic link. The last path component is used as the name of the link.

- `destPath` — The path that contains the item to be pointed to by the link. In other words, this is the destination of the link.

## Discussion

This method does not traverse symbolic links contained in `destPath`, making it possible to create symbolic links to locations that do not yet exist. Also, if the final path component in `path` is a symbolic link, that link is not followed.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- removeItemAtPath:error:](<removeitem(atpath_).md>) — Removes the file or directory at the specified path.

### Creating symbolic and hard links

- [- createSymbolicLinkAtURL:withDestinationURL:error:](<createsymboliclink(at_withdestinationurl_).md>) — Creates a symbolic link at the specified URL that points to an item at the given URL.
- [- linkItemAtURL:toURL:error:](<linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.
- [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) — Returns the path of the item pointed to by a symbolic link.
