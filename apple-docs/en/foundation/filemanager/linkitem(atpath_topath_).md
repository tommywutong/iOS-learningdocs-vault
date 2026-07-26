---
title: 'linkItem(atPath:toPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/linkitem(atpath:topath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/linkitem(atpath:topath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/linkitem%28atpath%3Atopath%3A%29.json'
content_hash: 'sha256:e65507d9da2b07af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# linkItem(atPath:toPath:)

<sub>Instance Method</sub>

Creates a hard link between the items at the specified paths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func linkItem(atPath srcPath: String, toPath dstPath: String) throws
```

## Parameters

- `srcPath` — The path that specifies the item you wish to link to. The value in this parameter must not be `nil`.

- `dstPath` — The path that identifies the location where the link will be created. The value in this parameter must not be `nil`.

## Discussion

Use this method to create hard links between files in the current file system. If `srcPath` is a directory, this method creates a new directory at `dstPath` and then creates hard links for the items in that directory. If `srcPath` is (or contains) a symbolic link, the symbolic link is copied to the new location and not converted to a hard link.

Prior to linking each item, the file manager asks its delegate if it should actually create the link. It does this by calling the [- fileManager:shouldLinkItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldlinkitemat_to_).md>) method; if that method is not implemented it calls the [- fileManager:shouldLinkItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldlinkitematpath_topath_).md>) method instead. If the delegate method returns [true](../../swift/true.md), or if the delegate does not implement the appropriate methods, the file manager creates the hard link. If there is an error linking one out of several items, the file manager may also call the delegate’s [- fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_linkingitemat_to_).md>) or [- fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_linkingitematpath_topath_).md>) method to determine how to proceed.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Creating symbolic and hard links

- [- createSymbolicLinkAtURL:withDestinationURL:error:](<createsymboliclink(at_withdestinationurl_).md>) — Creates a symbolic link at the specified URL that points to an item at the given URL.
- [- createSymbolicLinkAtPath:withDestinationPath:error:](<createsymboliclink(atpath_withdestinationpath_).md>) — Creates a symbolic link that points to the specified destination.
- [- linkItemAtURL:toURL:error:](<linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) — Returns the path of the item pointed to by a symbolic link.
