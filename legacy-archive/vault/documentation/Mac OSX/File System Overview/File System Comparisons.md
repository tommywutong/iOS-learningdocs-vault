---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/Comparisons.html
archived_at: '2026-07-15T08:15:24.135753Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Aliases%20and%20Symbolic%20Links.md)[Previous](Access%20Control%20Lists.md)

# File System Comparisons

There are many significant differences between the two major file systems on Mac OS X: HFS+ and UFS. In many cases, these differences have some bearing on programs developed for Mac OS X. The following list summarizes the major differences between these file systems (many of these statements apply to HFS as well as HFS+):

- _Case sensitivity_. UFS is sensitive to case; although HFS+ is case-insensitive, it is case-preserving.
- _Multiple forks_. HFS+ supports multiple forks (and additional metadata) whereas UFS supports only a single fork. (Carbon simulates multiple forks on file systems that do not support them, such as UFS.)
- _Path separators_. HFS+ uses colons as path separators whereas UFS follows the convention of forward slashes. The system translates between these separators.
- _Modification dates_. HFS+ supports both creation and modification dates as file metadata; UFS supports modification dates but not creation dates. If you copy a file with a command that understands modification dates but not creation dates, the command might reset the modification date as it creates a new file for the copy. Because of this behavior, it is possible to have a file with a creation date later than its modification date.
- _Sparse files and zero filling_. UFS supports sparse files, which are a way for the file system to store the data in files without storing unused space allocated for those files. HFS+ does not support sparse files and, in fact, zero-fills all bytes allocated for a file until end-of-file.
- _Lightweight references to file-system items_. See [Aliases and Symbolic Links](Aliases%20and%20Symbolic%20Links.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dqlkciffeerkiizba).

In addition, the interfaces historically associated with each file system sometimes have different behaviors. For example, a program using BSD (or BSD-derived) interfaces can delete a file that is open; on the other hand, a Carbon program can delete only a file that is closed.

Table 1 provides a comparative summary of features in the UFS and HFS+ file systems.

__Table 1__  Feature comparison

| Feature | HFS+ | UFS |
| Case sensitive | No | Yes |
| Supports multiple file forks | Yes | No |
| Path separator character | “:” | “/” |
| Supports modification dates | Yes | Yes |
| Supports creation dates | Yes | No |
| Supports sparse files | No | Yes |
| Supports zero-filling of files | Yes | No |
| Supports aliases | Yes | No |
| Supports symbolic links | Yes | Yes |
| Supports ACLs | Yes | No |

[Next](Aliases%20and%20Symbolic%20Links.md)[Previous](Access%20Control%20Lists.md)

