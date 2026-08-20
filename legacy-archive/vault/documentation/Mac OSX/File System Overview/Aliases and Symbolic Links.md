---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/Aliases.html
archived_at: '2026-07-15T08:15:22.822580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](File%20System%20Comparisons.md)

# Aliases and Symbolic Links

Aliases and symbolic links are lightweight references to files and folders. Aliases are associated with Mac OS Standard (HFS) and Mac OS Extended (HFS+) volume formats. Symbolic links are a feature of HFS+ and UFS file systems. Both aliases and symbolic links allow multiple references to files and folders without requiring multiple copies of these items. Prior to Mac OS X v10.2, aliases and symbolic links behaved very differently when a referenced file or folder moved or changed.

On HFS and HFS+ file systems, each file and folder has a unique, persistent identity. Aliases use this identity along with pathname information to find files and folders on the same volume.

In versions of Mac OS X before 10.2, aliases located a file or folder using its unique identity first and its pathname second. Beginning with Mac OS X 10.2, aliases reversed this search order by using the pathname first and unique identity second. This means that if you move a file and replace it with an identically named file, aliases to the original file now point to the new file. Similarly, if you move a file on the same volume (without replacing it), aliases use the unique identity information to locate the file.

When a file or folder moves, the alias may update either its path information or unique identity information to account for the change. If a file moves somewhere on the same volume, the alias updates its internal record with the new path information for the file. Similarly, if the original file is replaced by a file with the same name, but a different unique identity, the alias updates its internal record with the unique identity of the new file.

Because aliases use a file system path to resolve a file’s location initially, they now offer a similar behavior to symbolic links. Symbolic links rely exclusively on path information to locate a file. If you move a file somewhere on the same volume without replacing it, symbolic links to the file break while aliases do not. The only way to fix a symbolic link is to delete it and create a new one.

The Finder and other system applications now use aliases with this pathname-first behavior. However, applications can still resolve aliases by unique identity first using the methods of the Alias Manager.

If your application supports versions of Mac OS X prior to Mac OS X v10.2, you should follow certain guidelines when modifying files. First, when editing a file, modify the existing file. Second, if you need to replace a file transparently with a new version, use `FSExchangeObjects` to swap the new file for the old one. The NSDocument class already uses similar techniques to update the document file, thus maintaining aliases whenever possible.

[Next](Document%20Revision%20History.md)[Previous](File%20System%20Comparisons.md)

