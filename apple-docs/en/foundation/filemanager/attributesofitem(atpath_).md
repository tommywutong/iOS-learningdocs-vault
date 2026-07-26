---
title: 'attributesOfItem(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/attributesofitem(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/attributesofitem(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/attributesofitem%28atpath%3A%29.json'
content_hash: 'sha256:5cfda6f387e377ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# attributesOfItem(atPath:)

<sub>Instance Method</sub>

Returns the attributes of the item at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attributesOfItem(atPath path: String) throws -> [FileAttributeKey : Any]
```

## Parameters

- `path` — The path of a file or directory.

## Return Value

A dictionary object that describes the attributes (file, directory, symlink, and so on) of the file specified by `path` (or `nil` if an error occurred in Objective-C). The keys in the dictionary are described in `File Attribute Keys`.

## Discussion

If the item at the path is a symbolic link—that is, the value of the [NSFileType](../fileattributekey/type.md) key in the attributes dictionary is [NSFileTypeSymbolicLink](../fileattributetype/typesymboliclink.md)—you can use the [- destinationOfSymbolicLinkAtPath:error:](<destinationofsymboliclink(atpath_).md>) method to retrieve the path of the item pointed to by the link. You can also use the [stringByResolvingSymlinksInPath](../nsstring/resolvingsymlinksinpath.md) method of [NSString](../nsstring.md) to resolve links in the path before retrieving the item’s attributes.

As a convenience, [NSDictionary](../nsdictionary.md) provides a set of methods (declared as a category on [NSDictionary](../nsdictionary.md)) for quickly and efficiently obtaining attribute information from the returned dictionary: [- fileGroupOwnerAccountName](<../nsdictionary/filegroupowneraccountname().md>), [- fileModificationDate](<../nsdictionary/filemodificationdate().md>), [- fileOwnerAccountName](<../nsdictionary/fileowneraccountname().md>), [- filePosixPermissions](<../nsdictionary/fileposixpermissions().md>), [- fileSize](<../nsdictionary/filesize().md>), [- fileSystemFileNumber](<../nsdictionary/filesystemfilenumber().md>), [- fileSystemNumber](<../nsdictionary/filesystemnumber().md>), and [- fileType](<../nsdictionary/filetype().md>).

### Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Getting and setting attributes

- [- componentsToDisplayForPath:](<componentstodisplay(forpath_).md>) — Returns an array of strings representing the user-visible components of a given path.
- [- displayNameAtPath:](<displayname(atpath_).md>) — Returns the display name of the file or directory at a specified path.
- [- attributesOfFileSystemForPath:error:](<attributesoffilesystem(forpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.
