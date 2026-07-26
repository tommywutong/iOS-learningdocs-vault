---
title: 'attributesOfFileSystem(forPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/attributesoffilesystem(forpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/attributesoffilesystem(forpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/attributesoffilesystem%28forpath%3A%29.json'
content_hash: 'sha256:df3a3b1fe8607bdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# attributesOfFileSystem(forPath:)

<sub>Instance Method</sub>

Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attributesOfFileSystem(forPath path: String) throws -> [FileAttributeKey : Any]
```

## Parameters

- `path` — Any pathname within the mounted file system.

## Return Value

A dictionary object that describes the attributes of the mounted file system on which `path` resides. See `File-System Attribute Keys` for a description of the keys available in the dictionary.

## Discussion

This method does not traverse a terminal symbolic link.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Getting and setting attributes

- [- componentsToDisplayForPath:](<componentstodisplay(forpath_).md>) — Returns an array of strings representing the user-visible components of a given path.
- [- displayNameAtPath:](<displayname(atpath_).md>) — Returns the display name of the file or directory at a specified path.
- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.
