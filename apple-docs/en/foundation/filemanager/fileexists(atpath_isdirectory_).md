---
title: 'fileExists(atPath:isDirectory:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/fileexists(atpath:isdirectory:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/fileexists(atpath:isdirectory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/fileexists%28atpath%3Aisdirectory%3A%29.json'
content_hash: 'sha256:7480408053ff7af2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# fileExists(atPath:isDirectory:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a file or directory exists at a specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fileExists(atPath path: String, isDirectory: UnsafeMutablePointer<ObjCBool>?) -> Bool
```

## Parameters

- `path` — The path of a file or directory. If `path` begins with a tilde (`~`), it must first be expanded with [stringByExpandingTildeInPath](../nsstring/expandingtildeinpath.md), or this method will return [false](../../swift/false.md).

- `isDirectory` — Upon return, contains [true](../../swift/true.md) if `path` is a directory or if the final path element is a symbolic link that points to a directory; otherwise, contains [false](../../swift/false.md). If `path` doesn’t exist, this value is undefined upon return. Pass `NULL` if you do not need this information.

## Return Value

[true](../../swift/true.md) if a file at the specified path exists, or [false](../../swift/false.md) if the file’s does not exist or its existence could not be determined.

## Discussion

If the file at `path` is inaccessible to your app, perhaps because one or more parent directories are inaccessible, this method returns [false](../../swift/false.md). If the final element in `path` specifies a symbolic link, this method traverses the link and returns [true](../../swift/true.md) or [false](../../swift/false.md) based on the existence of the file at the link destination.

If you need to further determine whether `path` is a package, use the [isFilePackage(atPath:)](<../../appkit/nsworkspace/isfilepackage(atpath_).md>) method of [NSWorkspace](../../appkit/nsworkspace.md).

The following example code gets an array that identifies the fonts in the user’s fonts directory:

```objc
NSArray *subpaths;
BOOL isDir;
 
NSArray *paths = NSSearchPathForDirectoriesInDomains
                     (NSLibraryDirectory, NSUserDomainMask, YES);
 
if ([paths count] == 1) {
 
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSString *fontPath = [[paths objectAtIndex:0] stringByAppendingPathComponent:@"Fonts"];
 
    if ([fileManager fileExistsAtPath:fontPath isDirectory:&isDir] && isDir) {
        subpaths = [fileManager subpathsAtPath:fontPath];
// ...
```

> [!note] Note
> Attempting to predicate behavior based on the current state of the file system or a particular file on the file system is not recommended. Doing so can cause odd behavior or race conditions. It’s far better to attempt an operation (such as loading a file or creating a directory), check for errors, and handle those errors gracefully than it is to try to figure out ahead of time whether the operation will succeed. For more information on file-system race conditions, see [Race Conditions and Secure File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## See Also

### Related Documentation

- [- checkResourceIsReachableAndReturnError:](<../nsurl/checkresourceisreachableandreturnerror(__).md>) — Returns whether the resource pointed to by a file URL can be reached.

### Determining access to files

- [- fileExistsAtPath:](<fileexists(atpath_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- isReadableFileAtPath:](<isreadablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to read a specified file.
- [- isWritableFileAtPath:](<iswritablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to write to a specified file.
- [- isExecutableFileAtPath:](<isexecutablefile(atpath_).md>) — Returns a Boolean value that indicates whether the operating system appears able to execute a specified file.
- [- isDeletableFileAtPath:](<isdeletablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to delete a specified file.
