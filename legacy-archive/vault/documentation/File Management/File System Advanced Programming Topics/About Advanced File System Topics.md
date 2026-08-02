---
title: File System Advanced Programming Topics
apple_id: TP40010765
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemAdvancedPT/Introduction/Introduction.html
archived_at: '2026-07-15T07:31:56.759705Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



# About Advanced File System Topics

This document supplements the information in _[File System Programming Guide](../File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_ by describing procedures that are related to the file system but not central to using it.

This document describes advanced techniques for manipulating files.

### File Mapping is an Efficient Way to Read Large Files

File mapping is the process of mapping disk sectors associated with a file into the virtual memory space of a process. Mapping is most appropriate when you plan to read small portions of a large file frequently and in random order. Mapping just the portions you need into memory is much more efficient than reading or rereading those sections over and over from disk. Mapping yields little benefit for files you plan to read sequentially anyway.

### Directories Can Have Localized Names

You can provide localized names for any user-visible directories that your code creates. Localized names improve the experience for users by showing directory names in the language they understand. The Finder automatically localizes the names of many system directories but you must provide the appropriate localizations for any custom directories you create.

_[File System Programming Guide](../File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_ is a prerequisite for reading this document. If you have not yet read that document, you should at least understand the content in the first two chapters, which describe the file system organization and techniques for accessing files and directories.

