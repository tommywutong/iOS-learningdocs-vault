---
title: Application File Management
apple_id: 10000056i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppFileMgmt/Tasks/WorkingWithDirWrappers.html
archived_at: '2026-07-15T05:25:39.441197Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application File Management](Introduction%20to%20Application%20File%20Management.md)


[Next](Using%20a%20Save%20Panel.md)[Previous](Working%20With%20File%20Wrappers.md)

# Working With Directory Wrappers

A directory wrapper contains other file wrappers (of any type), and allows you to access them by keys derived from their preferred filenames. You can add any type of file wrapper to a directory wrapper with `addFileWrapper:` or `addFileWithPath:`, and remove it with `removeFileWrapper:`. The convenience methods `addRegularFileWithContents:preferredFilename:` and `addSymbolicLinkWithDestination:preferredFilename:` allow you to add regular file and link wrappers while also setting their preferred names.

A directory wrapper stores its contents in an NSDictionary, which you can retrieve using the `fileWrappers` method. The keys of this dictionary are based on the preferred filenames of each file wrapper contained in the directory wrapper. There exist, then, three identifiers for a file wrapper within a directory wrapper:

- Preferred filename. This doesn’t uniquely identify the file wrapper, but the following identifiers are always based on it.
- Dictionary key. This is always equal to the preferred name when there are no other file wrappers of the same preferred name in the same directory wrapper. Otherwise, it’s a string made by adding a unique prefix to the preferred filename (note that the same file wrapper can have a different dictionary key for each directory wrapper that contains it). You use the dictionary key to retrieve the file wrapper object in memory, in order to get its contents or its filename (to update it from disk). You can get a file wrapper’s dictionary key by sending a `keyForFileWrapper:` message to the directory wrapper that contains it.
- Filename. This is usually based on the preferred filename, but isn’t necessarily the same as it or the dictionary key. You use the filename to update a single file wrapper relative to the path of the directory wrapper that contains it. Note that the filename may change whenever you save a directory wrapper containing the file wrapper (particularly if the file wrapper has been added to several different directory wrappers); thus, you should always retrieve the filename from the file wrapper itself each time you need it rather than caching it.

When working with the contents of a directory wrapper, you can use a dictionary enumerator to retrieve each file wrapper and perform whatever operation you need. Note that with the exceptions of saving and updating, a directory file wrapper defines no recursive operations for its contents. To set the file attributes for all contained file wrappers, or to perform any other such operation, you must define a recursive method that examines the type of each file wrapper and invokes itself anew for any directory wrapper it encounters.

[Next](Using%20a%20Save%20Panel.md)[Previous](Working%20With%20File%20Wrappers.md)

