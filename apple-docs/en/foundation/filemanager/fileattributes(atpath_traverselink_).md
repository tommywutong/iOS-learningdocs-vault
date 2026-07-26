---
title: 'fileAttributes(atPath:traverseLink:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/filemanager/fileattributes(atpath:traverselink:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/fileattributes(atpath:traverselink:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/fileattributes%28atpath%3Atraverselink%3A%29.json'
content_hash: 'sha256:28a0fc6b8135ab0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# fileAttributes(atPath:traverseLink:)

<sub>Instance Method</sub>

Returns a dictionary that describes the POSIX attributes of the file specified at a given.

> [!warning] Deprecated
> Use [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
func fileAttributes(atPath path: String, traverseLink yorn: Bool) -> [AnyHashable : Any]?
```

## Parameters

- `path` — A file path.

- `yorn` — If `path` is not a symbolic link, this parameter has no effect. If `path` is a symbolic link, then: - If [true](../../swift/true.md) the attributes of the linked-to file are returned, or if the link points to a nonexistent file the method returns `nil`. - If [false](../../swift/false.md), the attributes of the symbolic link are returned.

## Return Value

An `NSDictionary` object that describes the POSIX attributes of the file specified at `path`. The keys in the dictionary are described in `File Attribute Keys`. If there is no item at `path`, returns `nil`.

## Discussion

This code example gets several attributes of a file and logs them.

```objc
NSFileManager *fileManager = [[NSFileManager alloc] init];
NSString *path = @"/tmp/List";
NSDictionary *fileAttributes = [fileManager fileAttributesAtPath:path traverseLink:YES];
 
if (fileAttributes != nil) {
    NSNumber *fileSize;
    NSString *fileOwner;
    NSDate *fileModDate;
    if (fileSize = [fileAttributes objectForKey:NSFileSize]) {
        NSLog(@"File size: %qi\n", [fileSize unsignedLongLongValue]);
    }
    if (fileOwner = [fileAttributes objectForKey:NSFileOwnerAccountName]) {
        NSLog(@"Owner: %@\n", fileOwner);
    }
    if (fileModDate = [fileAttributes objectForKey:NSFileModificationDate]) {
        NSLog(@"Modification date: %@\n", fileModDate);
    }
}
else {
    NSLog(@"Path (%@) is invalid.", path);
}
```

As a convenience, `NSDictionary` provides a set of methods (declared as a category in `NSFileManager.h`) for quickly and efficiently obtaining attribute information from the returned dictionary: [- fileGroupOwnerAccountName](<../nsdictionary/filegroupowneraccountname().md>), [- fileModificationDate](<../nsdictionary/filemodificationdate().md>), [- fileOwnerAccountName](<../nsdictionary/fileowneraccountname().md>), [- filePosixPermissions](<../nsdictionary/fileposixpermissions().md>), [- fileSize](<../nsdictionary/filesize().md>), [- fileSystemFileNumber](<../nsdictionary/filesystemfilenumber().md>), [- fileSystemNumber](<../nsdictionary/filesystemnumber().md>), and [- fileType](<../nsdictionary/filetype().md>). For example, you could rewrite the file modification statement in the code example above as:

```objc
if (fileModDate = [fileAttributes fileModificationDate])
    NSLog(@"Modification date: %@\n", fileModDate);
```

### Special Considerations

Because this method does not return error information, it has been deprecated as of OS X v10.5. Use [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) instead.

## See Also

### Related Documentation

- [- attributesOfItemAtPath:error:](<attributesofitem(atpath_).md>) — Returns the attributes of the item at a given path.
- [- setAttributes:ofItemAtPath:error:](<setattributes(__ofitematpath_).md>) — Sets the attributes of the specified file or directory.

### Deprecated Methods

- [- changeFileAttributes:atPath:](<changefileattributes(__atpath_).md>) — Changes the attributes of a given file or directory. _(deprecated)_
- [- fileSystemAttributesAtPath:](<filesystemattributes(atpath_).md>) — Returns a dictionary that describes the attributes of the mounted file system on which a given path resides. _(deprecated)_
- [- directoryContentsAtPath:](<directorycontents(atpath_).md>) — Returns the directories and files (including symbolic links) contained in a given directory. _(deprecated)_
- [- createDirectoryAtPath:attributes:](<createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_
- [- createSymbolicLinkAtPath:pathContent:](<createsymboliclink(atpath_pathcontent_).md>) — Creates a symbolic link identified by a given path that refers to a given location. _(deprecated)_
- [- pathContentOfSymbolicLinkAtPath:](<pathcontentofsymboliclink(atpath_).md>) — Returns the path of the directory or file that a symbolic link at a given path refers to. _(deprecated)_
- [fileManager(_:shouldProceedAfterError:)](<../../objectivec/nsobject-swift.class/filemanager(__shouldproceedaftererror_).md>) — An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories. _(deprecated)_
- [fileManager(_:willProcessPath:)](<../../objectivec/nsobject-swift.class/filemanager(__willprocesspath_).md>) — An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path. _(deprecated)_
- [replaceItemAtURL(originalItemURL:withItemAtURL:backupItemName:options:)](<replaceitematurl(originalitemurl_withitematurl_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs. _(deprecated)_
