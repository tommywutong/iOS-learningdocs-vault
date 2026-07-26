---
title: 'destinationOfSymbolicLink(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/destinationofsymboliclink(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/destinationofsymboliclink(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/destinationofsymboliclink%28atpath%3A%29.json'
content_hash: 'sha256:cef0d80e2316d834'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# destinationOfSymbolicLink(atPath:)

<sub>Instance Method</sub>

Returns the path of the item pointed to by a symbolic link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func destinationOfSymbolicLink(atPath path: String) throws -> String
```

## Parameters

- `path` — The path of a file or directory.

## Return Value

An [NSString](../nsstring.md) object containing the path of the directory or file to which the symbolic link `path` refers. When using Objective-C, returns `nil` upon failure. If the symbolic link is specified as a relative path, that relative path is returned.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Creating symbolic and hard links

- [- createSymbolicLinkAtURL:withDestinationURL:error:](<createsymboliclink(at_withdestinationurl_).md>) — Creates a symbolic link at the specified URL that points to an item at the given URL.
- [- createSymbolicLinkAtPath:withDestinationPath:error:](<createsymboliclink(atpath_withdestinationpath_).md>) — Creates a symbolic link that points to the specified destination.
- [- linkItemAtURL:toURL:error:](<linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.
