---
title: 'createDirectory(atPath:withIntermediateDirectories:attributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/createdirectory(atpath:withintermediatedirectories:attributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/createdirectory(atpath:withintermediatedirectories:attributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/createdirectory%28atpath%3Awithintermediatedirectories%3Aattributes%3A%29.json'
content_hash: 'sha256:8267a9e3b1c5b8f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# createDirectory(atPath:withIntermediateDirectories:attributes:)

<sub>Instance Method</sub>

Creates a directory with given attributes at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func createDirectory(atPath path: String, withIntermediateDirectories createIntermediates: Bool, attributes: [FileAttributeKey : Any]? = nil) throws
```

## Parameters

- `path` — A path string identifying the directory to create. You may specify a full path or a path that is relative to the current working directory. This parameter must not be `nil`.

- `createIntermediates` — If [true](../../swift/true.md), this method creates any nonexistent parent directories as part of creating the directory in `path`. If [false](../../swift/false.md), this method fails if any of the intermediate parent directories does not exist. This method also fails if any of the intermediate path elements corresponds to a file and not a directory.

- `attributes` — The file attributes for the new directory and any newly created intermediate directories. You can set the owner and group numbers, file permissions, and modification date. If you specify `nil` for this parameter or omit a particular value, one or more default values are used as described in the discussion. For a list of keys you can include in this dictionary, see Supporting Types. Some of the keys, such as [NSFileHFSCreatorCode](../fileattributekey/hfscreatorcode.md) and [NSFileHFSTypeCode](../fileattributekey/hfstypecode.md), do not apply to directories.

## Discussion

If you specify `nil` for the `attributes` parameter, this method uses a default set of values for the owner, group, and permissions of any newly created directories in the path. Similarly, if you omit a specific attribute, the default value is used. The default values for newly created directories are as follows:

- Permissions are set according to the umask of the current process. For more information, see umask.
- The owner ID is set to the effective user ID of the process.
- The group ID is set to that of the parent directory.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.

### Creating and deleting items

- [- createDirectoryAtURL:withIntermediateDirectories:attributes:error:](<createdirectory(at_withintermediatedirectories_attributes_).md>) — Creates a directory with the given attributes at the specified URL.
- [- createFileAtPath:contents:attributes:](<createfile(atpath_contents_attributes_).md>) — Creates a file with the specified content and attributes at the given location.
- [- removeItemAtURL:error:](<removeitem(at_).md>) — Removes the file or directory at the specified URL.
- [- removeItemAtPath:error:](<removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- trashItemAtURL:resultingItemURL:error:](<trashitem(at_resultingitemurl_).md>) — Moves an item to the trash.
