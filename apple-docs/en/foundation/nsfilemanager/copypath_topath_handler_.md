---
title: 'copyPath:toPath:handler:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.5 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsfilemanager/copypath:topath:handler:'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilemanager/copypath:topath:handler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilemanager/copypath%3Atopath%3Ahandler%3A.json'
content_hash: 'sha256:e93098f93a7ddd37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# copyPath:toPath:handler:

<sub>Instance Method</sub>

Copies the directory or file specified in a given path to a different location in the file system identified by another path.

> [!warning] Deprecated
> Use [- copyItemAtURL:toURL:error:](<../filemanager/copyitem(at_to_).md>) instead.

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) copyPath:(NSString *) src toPath:(NSString *) dest handler:(id) handler;
```

## Parameters

- `src` — The location of the source file.

- `dest` — The location to which to copy the file specified by `source`.

- `handler` — An object that responds to the callback messages [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) and [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>). You can specify `nil` for `handler`; if you do so and an error occurs, the method automatically returns [false](../../swift/false.md).

## Return Value

[true](../../swift/true.md) if the copy operation is successful. If the operation is not successful, but the callback handler of [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) returns [true](../../swift/true.md), [copyPath:toPath:handler:](copypath_topath_handler_.md) also returns [true](../../swift/true.md). Otherwise this method returns [false](../../swift/false.md). The method also attempts to make the attributes of the directory or file at `destination` identical to `source`, but ignores any failure at this attempt.

## Discussion

If `source` is a file, the method creates a file at `destination` that holds the exact contents of the original file (this includes BSD special files). If `source` is a directory, the method creates a new directory at `destination` and recursively populates it with duplicates of the files and directories contained in `source`, preserving all links. The file specified in `source` must exist, while `destination` must not exist prior to the operation. When a file is being copied, the destination path must end in a filename—there is no implicit adoption of the source filename. Symbolic links are not traversed but are themselves copied. File or directory attributes—that is, metadata such as owner and group numbers, file permissions, and modification date—are also copied.

The handler callback mechanism is similar to delegation. `NSFileManager` sends [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) when it begins a copy, move, remove, or link operation. It sends [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) when it encounters any error in processing.

### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- copyItemAtURL:toURL:error:](<../filemanager/copyitem(at_to_).md>) instead.

## See Also

### Related Documentation

- [- linkItemAtURL:toURL:error:](<../filemanager/linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- copyItemAtPath:toPath:error:](<../filemanager/copyitem(atpath_topath_).md>) — Copies the item at the specified path to a new location synchronously.
- [- removeItemAtPath:error:](<../filemanager/removeitem(atpath_).md>) — Removes the file or directory at the specified path.

### Deprecated Methods

- [movePath:toPath:handler:](movepath_topath_handler_.md) — Moves the directory or file specified by a given path to a different location in the file system identified by another path. _(deprecated)_
- [removeFileAtPath:handler:](removefileatpath_handler_.md) — Deletes the file, link, or directory (including, recursively, all subdirectories, files, and links in the directory) identified by a given path. _(deprecated)_
- [- changeFileAttributes:atPath:](<../filemanager/changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileAttributesAtPath:traverseLink:](<../filemanager/fileattributes(atpath_traverselink_).md>) — Returns a dictionary that describes the POSIX attributes of the file specified at a given. _(deprecated)_
- [- fileSystemAttributesAtPath:](<../filemanager/filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- directoryContentsAtPath:](<../filemanager/directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<../filemanager/createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<../filemanager/createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<../filemanager/pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [linkPath:toPath:handler:](linkpath_topath_handler_.md) — Creates a link from a source to a destination. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
