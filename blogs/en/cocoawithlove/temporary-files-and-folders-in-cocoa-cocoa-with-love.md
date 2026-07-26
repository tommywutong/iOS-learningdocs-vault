---
title: 'Temporary files and folders in Cocoa | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/07/temporary-files-and-folders-in-cocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:7761c8883fd23f28'
translated: false
---

> 原文：[Temporary files and folders in Cocoa | Cocoa with Love](https://www.cocoawithlove.com/2009/07/temporary-files-and-folders-in-cocoa.html)　·　Cocoa with Love (Matt Gallagher)

If you need to use temporary files in your application and you search the Cocoa documentation for "temporary file", you're unlikely to find anything that explains how to create one. Since temporary files and folders are subject to a number of security issues and race conditions when done wrong, it is important to know the correct way to create them. I'll show you some code that you can copy and paste into your applications to create temporary files and folders safely.

## Introduction

With large amounts of RAM on modern computers and alternatives such as the cache directories and application support directories, genuine temporary files are not needed in most Cocoa applications. Even when they are needed, for atomic write operations or for Core Data databases, Cocoa libraries often create them automatically.

Eventually though, you're likely to encounter a situation where you need to create a temporary file yourself. You need to be careful when creating temporary files because:

- Predictable temporary file locations can be a security hole in your applications.
- On Mac OS X, multiple users on the computer may have their own copies of your application open, so the creation must be atomic (safe when concurrent).

In addition to this, you must be able to find the correct directories to place your files, be aware of the lifetime of files in these locations and manage cleanup correctly when you are done.

## Required steps

### Choosing the right enclosing directory

The directory for temporary files needs to be writeable by the current user. This means that the directory will need to be user-specific.

The correct directory is almost always the one returned by the Foundation function `NSTemporaryDirectory`. This directory is unique for each user (so each user has write permissions to it).

If you choose this directory though, it is important to know that it is cleaned out automatically every 3 days but otherwise persists between application launches and reboots. This directory is in a hashed location (not predictable in advance) and is therefore safe against security issues associated with predicatable locations.

If you need a location that can persist longer than 3 days, you probably want to use the Application Support directory or a Cache directory instead. Both of these locations are permanent (until your application deletes the contents) but Application Support is considered "important data" and backed up by Time Machine, whereas Cache is considered "user deletable at any time" and is not backed up. The backup point is important: don't store large amounts of temporary data in a location that will fill someone's backup drive.

These alternate directories are obtained using the Foundation function `NSSearchPathForDirectoriesInDomains` with a first parameter of `NSApplicationSupportDirectory` or `NSCachesDirectory`, a second parameter of `NSUserDomainMask` (occasionally a different value if you need a directory shared between users on the system or network — but this is uncommon). This function returns an array but you'll normally get just one result if you use `NSUserDomainMask` and you'll need to append your bundle identifier to get a location unique to your application.

```objc
// an alternative to the NSTemporaryDirectory
NSString *path = nil;
NSArray *paths = NSSearchPathForDirectoriesInDomains(
    NSCachesDirectory, NSUserDomainMask, YES);
if ([paths count])
{
    NSString *bundleName =
        [[[NSBundle mainBundle] infoDictionary] objectForKey:@"CFBundleIdentifier"];
    path = [[paths objectAtIndex:0] stringByAppendingPathComponent:bundleName];
}
```

This `path` value can be used instead of the `NSTemporaryDirectory()` invocations in the code samples below.

### Creating and opening a file or subdirectory

To avoid concurrency issues (race conditions), you need to choose a name for any file or directory placed directly in the temporary directory that is unique but which also can't be stolen by another process between choosing the name and creating/opening the file or directory. Even though `NSTemporaryDirectory()` is unique for each user, you still must avoid potential conflicts within the user's account.

To do this, we use the POSIX function `mkstemp` for files and `mkdtemp` for directories. The former will return an already open file descriptor for the file and the latter will have already created the directory for us.

We could simply generate a universally unique identifier (UUID) and use that for the filename but these IDs are guessable which can create security problems in obscure cases where we don't also check for a name conflict — better to use something that looks for a collision, in the extremely unlikely case that it occurs. If you must use a UUID filename instead of `mkstemp` for some reason, be certain that it is for non-critical data.

#### Creating a temporary file:

```objc
NSString *tempFileTemplate =
    [NSTemporaryDirectory() stringByAppendingPathComponent:@"myapptempfile.XXXXXX"];
const char *tempFileTemplateCString =
    [tempFileTemplate fileSystemRepresentation];
char *tempFileNameCString = (char *)malloc(strlen(tempFileTemplateCString) + 1);
strcpy(tempFileNameCString, tempFileTemplateCString);
int fileDescriptor = mkstemp(tempFileNameCString);

if (fileDescriptor == -1)
{
   // handle file creation failure
}

// This is the file name if you need to access the file by name, otherwise you can remove
// this line.
tempFileName =
    [[NSFileManager defaultManager]
        stringWithFileSystemRepresentation:tempFileNameCString
        length:strlen(tempFileNameCString)];

free(tempFileNameCString);
tempFileHandle =
    [[NSFileHandle alloc]
        initWithFileDescriptor:fileDescriptor
        closeOnDealloc:NO];
```

It is important to handle all reading and writing from the temporary file using this `fileDescriptor` or something created directly from the `fileDescriptor` like the `NSFileHandle` in this example. This guarantees the operation remains safe for concurrency — if the `fileDescriptor` is closed before use, a race condition could occur.

The "X"s in the file name are replaced by the unique hash for the file's name. You'll probably want to replace the "`myapptempfile`" name with something appropriate, although it isn't required (the file is guaranteed unique regardless).

Also notice the use of `fileSystemRepresentation` and `stringWithFileSystemRepresentation:length:` to convert to and from the C strings — this is helpful to handle weird path quirks on different filesystems.

#### Creating a temporary folder:

```objc
NSString *tempDirectoryTemplate =
    [NSTemporaryDirectory() stringByAppendingPathComponent:@"myapptempdirectory.XXXXXX"];
const char *tempDirectoryTemplateCString =
    [tempDirectoryTemplate fileSystemRepresentation];
char *tempDirectoryNameCString =
    (char *)malloc(strlen(tempDirectoryTemplateCString) + 1);
strcpy(tempDirectoryNameCString, tempDirectoryTemplateCString);

char *result = mkdtemp(tempDirectoryNameCString);
if (!result)
{
    // handle directory creation failure
}

NSString *tempDirectoryPath =
    [[NSFileManager defaultManager]
        stringWithFileSystemRepresentation:tempDirectoryNameCString
        length:strlen(result)];
free(tempDirectoryNameCString);
```

You can now use the `tempDirectoryPath` as the container for any files. As with the previous example, you probably want to replace "`myapptempdirectory`" with something appropriate to your application and usage.

## Conclusion

You could simply create a file in the `/tmp` directory but this approach is filled with many problems — write permissions, concurrency issues, security issues and duration or persistence issues.

Fortunately, the code to create a temporary file or temporary directory is consistent — you can normally use these code samples without modification. The only choices you need to make is whether to use an alternative directory (like the Application Support directory or the Caches directory).
