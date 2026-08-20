---
title: Application File Management
apple_id: 10000056i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppFileMgmt/Tasks/WorkingWithFileWrappers.html
archived_at: '2026-07-15T05:25:39.993627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application File Management](Introduction%20to%20Application%20File%20Management.md)


[Next](Working%20With%20Directory%20Wrappers.md)[Previous](File%20Wrappers.md)

# Working With File Wrappers

You can create a file wrapper from data in memory using `initWithSerializedRepresentation:` or from data on disk using `initWithPath:`. Both create the appropriate type of file wrapper based on the nature of the serialized representation or of the file on disk. Three convenience methods each create a file wrapper of a specific type: `initRegularFileWithContents:`, `initDirectoryWithFileWrappers:`, and `initSymbolicLinkWithDestination:`. Because each initialization method creates file wrappers of different types or states, they’re all designated initializers for this class—subclasses must meaningfully override them all as necessary.

Some NSFileWrapper methods apply only to a specific type, and an exception is raised if sent to a file wrapper of the wrong type. To determine the type of a file wrapper, use the `isRegularFile`, `isDirectory`, and `isSymbolicLink` methods.

A file wrapper stores file system information (such as modification time and access permissions), which it updates when reading from disk and uses when writing files to disk. The `fileAttributes` method returns this information in the format described in the NSFileManager class specification. You can also set the file attributes using the `setFileAttributes:` method.

NSFileWrapper allows you to set a preferred filename for save operations and records the last filename it was actually saved to; the `preferredFilename` and `filename` methods return these names. This feature is more important for directory wrappers, though, and so is discussed under [Working With Directory Wrappers](Working%20With%20Directory%20Wrappers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg43tmlkciffemqsbifea).

When saving a file wrapper to disk, you typically determine the directory you want to save it in, then append the preferred filename to that directory path and use `writeToFile:atomically:updateFilenames:`, which saves the file wrapper’s contents and updates the file attributes. You can save a file wrapper under a different name if you wish, but this may result in the recorded filename differing from the preferred filename, depending on how you invoke the `writeToFile:atomically:updateFilenames:` method.

Besides saving its contents to disk, a file wrapper can re-read them from disk when necessary. The `needsToBeUpdatedFromPath:` method determines whether a disk representation may have changed, based on the file attributes stored the last time the file was read or written. If the file wrapper’s modification time or access permissions are different from those of the file on disk, this method returns `YES`. You can then use `updateFromPath:` to re-read the file from disk.

Finally, to transmit a file wrapper to another process or system (for example, over a distributed objects connection or through the pasteboard), you use the `serializedRepresentation` method to get an NSData object containing the file wrapper’s contents in the `NSFileContentsPboardType` format. You can safely transmit this representation over whatever channel you desire. The recipient of the representation can then reconstitute the file wrapper using the `initWithSerializedRepresentation:` method.

[Next](Working%20With%20Directory%20Wrappers.md)[Previous](File%20Wrappers.md)

