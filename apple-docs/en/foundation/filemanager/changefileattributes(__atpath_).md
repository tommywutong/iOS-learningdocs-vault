---
title: 'changeFileAttributes(_:atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filemanager/changefileattributes(_:atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/changefileattributes(_:atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/changefileattributes%28_%3Aatpath%3A%29.json'
content_hash: 'sha256:21e524f67ca0e134'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# changeFileAttributes(_:atPath:)

<sub>Instance Method</sub>

Changes the attributes of a given file or directory.

> [!warning] Deprecated
> Use [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func changeFileAttributes(_ attributes: [AnyHashable : Any] = [:], atPath path: String) -> Bool
```

## Parameters

- `attributes` — A dictionary containing as keys the attributes to set for `path` and as values the corresponding value for the attribute. You can set following: `NSFileBusy`, `NSFileCreationDate`, `NSFileExtensionHidden`, `NSFileGroupOwnerAccountID`, `NSFileGroupOwnerAccountName`, `NSFileHFSCreatorCode`, `NSFileHFSTypeCode`, `NSFileImmutable`, `NSFileModificationDate`, `NSFileOwnerAccountID`, `NSFileOwnerAccountName`, `NSFilePosixPermissions`. You can change single attributes or any combination of attributes; you need not specify keys for all attributes. For the `NSFilePosixPermissions` value, specify a file mode from the OR’d permission bit masks defined in `sys/stat.h`. See the man page for the `chmod` function (`man 2 chmod`) for an explanation.

- `path` — A path to a file or directory.

## Return Value

[true](../../swift/true.md) if _all_ changes succeed. If any change fails, returns [false](../../swift/false.md), but it is undefined whether any changes actually occurred.

## Discussion

As in the POSIX standard, the app either must own the file or directory or must be running as superuser for attribute changes to take effect. The method attempts to make all changes specified in attributes and ignores any rejection of an attempted modification.

The `NSFilePosixPermissions` value must be initialized with the code representing the POSIX file-permissions bit pattern. `NSFileHFSCreatorCode` and `NSFileHFSTypeCode` will only be heeded when `path` specifies a file.

### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) instead.

## See Also

### Related Documentation

- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.

### Deprecated Methods

- [- fileAttributesAtPath:traverseLink:](<fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- fileSystemAttributesAtPath:](<filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- directoryContentsAtPath:](<directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_
