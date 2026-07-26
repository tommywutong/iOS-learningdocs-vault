---
title: 'setAttributes(_:ofItemAtPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/setattributes(_:ofitematpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/setattributes(_:ofitematpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/setattributes%28_%3Aofitematpath%3A%29.json'
content_hash: 'sha256:77b93d73948b59a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# setAttributes(_:ofItemAtPath:)

<sub>Instance Method</sub>

Sets the attributes of the specified file or directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setAttributes(_ attributes: [FileAttributeKey : Any], ofItemAtPath path: String) throws
```

## Parameters

- `attributes` — A dictionary containing as keys the attributes to set for `path` and as values the corresponding value for the attribute. You can set the following attributes: [NSFileBusy](../fileattributekey/busy.md), [NSFileCreationDate](../fileattributekey/creationdate.md), [NSFileExtensionHidden](../fileattributekey/extensionhidden.md), [NSFileGroupOwnerAccountID](../fileattributekey/groupowneraccountid.md), [NSFileGroupOwnerAccountName](../fileattributekey/groupowneraccountname.md), [NSFileHFSCreatorCode](../fileattributekey/hfscreatorcode.md), [NSFileHFSTypeCode](../fileattributekey/hfstypecode.md), [NSFileImmutable](../fileattributekey/immutable.md), [NSFileModificationDate](../fileattributekey/modificationdate.md), [NSFileOwnerAccountID](../fileattributekey/owneraccountid.md), [NSFileOwnerAccountName](../fileattributekey/owneraccountname.md), [NSFilePosixPermissions](../fileattributekey/posixpermissions.md). You can change single attributes or any combination of attributes; you need not specify keys for all attributes.

- `path` — The path of a file or directory.

## Discussion

As in the POSIX standard, the app either must own the file or directory or must be running as superuser for attribute changes to take effect. The method attempts to make all changes specified in attributes and ignores any rejection of an attempted modification. If the last component of the path is a symbolic link, the system traverses it.

You must initialize the [NSFilePosixPermissions](../fileattributekey/posixpermissions.md) value with the code representing the POSIX file-permissions bit pattern. The system sets [NSFileHFSCreatorCode](../fileattributekey/hfscreatorcode.md) and [NSFileHFSTypeCode](../fileattributekey/hfstypecode.md) only when `path` specifies a file.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Getting and setting attributes

- [- componentsToDisplayForPath:](<componentstodisplay(forpath_).md>) — Returns an array of strings representing the user-visible components of a given path.
- [- displayNameAtPath:](<displayname(atpath_).md>) — Returns the display name of the file or directory at a specified path.
- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- attributesOfFileSystemForPath:error:](<attributesoffilesystem(forpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides.
