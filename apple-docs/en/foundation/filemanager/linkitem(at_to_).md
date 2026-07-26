---
title: 'linkItem(at:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/linkitem(at:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/linkitem(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/linkitem%28at%3Ato%3A%29.json'
content_hash: 'sha256:e4224c78df01c614'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# linkItem(at:to:)

<sub>Instance Method</sub>

Creates a hard link between the items at the specified URLs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func linkItem(at srcURL: URL, to dstURL: URL) throws
```

## Parameters

- `srcURL` — The file URL that identifies the source of the link. The URL in this parameter must not be a file reference URL; it must specify the actual path to the item. The value in this parameter must not be `nil`.

- `dstURL` — The file URL that specifies where you want to create the hard link. The URL in this parameter must not be a file reference URL; it must specify the actual path to the item. The value in this parameter must not be `nil`.

## Discussion

Use this method to create hard links between files in the current file system. If `srcURL` is a directory, this method creates a new directory at `dstURL` and then creates hard links for the items in that directory. If `srcURL` is (or contains) a symbolic link, the symbolic link is copied and not converted to a hard link at `dstURL`.

Prior to linking each item, the file manager asks its delegate if it should actually create the link. It does this by calling the [- fileManager:shouldLinkItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldlinkitemat_to_).md>) method; if that method is not implemented it calls the [- fileManager:shouldLinkItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldlinkitematpath_topath_).md>) method instead. If the delegate method returns [true](../../swift/true.md), or if the delegate does not implement the appropriate methods, the file manager creates the hard link. If there is an error linking one out of several items, the file manager may also call the delegate’s [- fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_linkingitemat_to_).md>) or [- fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_linkingitematpath_topath_).md>) method to determine how to proceed.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Creating symbolic and hard links

- [- createSymbolicLinkAtURL:withDestinationURL:error:](<createsymboliclink(at_withdestinationurl_).md>) — Creates a symbolic link at the specified URL that points to an item at the given URL.
- [- createSymbolicLinkAtPath:withDestinationPath:error:](<createsymboliclink(atpath_withdestinationpath_).md>) — Creates a symbolic link that points to the specified destination.
- [- linkItemAtPath:toPath:error:](<linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.
- [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) — Returns the path of the item pointed to by a symbolic link.
