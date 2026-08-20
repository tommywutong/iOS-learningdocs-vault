---
title: Application File Management
apple_id: 10000056i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppFileMgmt/Concepts/FileWrapper.html
archived_at: '2026-07-15T05:25:37.043045Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application File Management](Introduction%20to%20Application%20File%20Management.md)


[Next](Working%20With%20File%20Wrappers.md)[Previous](The%20Save%20and%20Open%20Panels.md)

# File Wrappers

An NSFileWrapper holds a file’s contents in dynamic memory. In this role it enables a document object to embed a file, treating it as a unit of data that can be displayed as an image (and possibly edited in place), saved to disk, or transmitted to another application. It can also store an icon for representing the file in a document or in a dragging operation.

Instances of this class are referred to as file wrapper objects, and when no confusion will result, merely as file wrappers. A file wrapper can be one of three specific types: a regular file wrapper, which holds the contents of a single actual file; a directory wrapper, which holds a directory and all of the files or directories within it; or a link wrapper, which simply represents a symbolic link in the file system (sometimes called a shortcut or alias).

Because the purpose of a file wrapper is to represent files in memory, it’s very loosely coupled to any disk representation. A file wrapper doesn’t record the path to the disk representation of its contents. This allows you to save the same file wrapper with different paths, but it also requires you to record those paths if you want to update the file wrapper from disk later.

[Next](Working%20With%20File%20Wrappers.md)[Previous](The%20Save%20and%20Open%20Panels.md)

