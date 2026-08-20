---
title: File-System Performance Guidelines
apple_id: 10000161i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/FileSystem/Articles/MacOSXAndFiles.html
archived_at: '2026-07-18T01:48:43.072798Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File-System Performance Guidelines](Introduction%20to%20File-System%20Performance%20Guidelines.md)


[Next](Examining%20File-System%20Usage.md)[Previous](File-System%20Performance%20Tips.md)

# Overview of OS X File Systems

The following sections discuss the file systems supported by OS X and the impact they can have on application performance.

OS X supports a variety of file systems and volume formats, including those listed in Table 1. Although the primary volume format is HFS Plus, OS X can also boot from a disk formatted with the UFS file system. Future versions of OS X may be bootable with other volume formats as well.

__Table 1__  File systems supported by OS X

| File System | Description |
| HFS | Mac OS Standard file system. Standard Macintosh file system for older versions of Mac OS. |
| HFS Plus | Mac OS Extended file system. Standard Macintosh file system for OS X. |
| UFS | Unix File System. A variant of the BSD “Fast File System.” |
| WebDAV | Used for directly accessing files on the web. For example, iDisk uses WebDAV for accessing files. |
| UDF | Universal Disk Format. The standard file system for all forms of DVD media (video, ROM, RAM and RW) and some writable CD formats. |
| FAT | The MS-DOS file system, with 16- and 32-bit variants. |
| SMB/CIFS | Used for sharing files with Microsoft Windows SMB file servers. |
| AFP | AppleTalk Filing Protocol. The primary network file system for all versions of Mac OS. |
| NFS | Network File System. A commonly-used BSD file sharing standard. OS X supports NFSv2 and NFSv3 over TCP and UDP. |
| FTP | A file system wrapper for the standard Internet File Transfer Protocol. |

Every file system stores _metadata_ about the files in the file system. This metadata describes the file but is not part of the file itself. The metadata for a file can include attributes such as Mac OS file type information, BSD-style file access permissions, and creation and modification dates. Because of the differences in how file systems store this data, accessing metadata can be a potentially expensive operation on some file systems.

It’s important to realize that if a piece of data is not immediately present in the file system, that information might have to be calculated. Retrieving file-system information is a time-consuming operation as it is, but if the information must be calculated or read separately from disk, it becomes even more time-consuming. The valence of a directory—the number of items in that directory—is a typical example of information that must be calculated on most file systems.

When calling file-system routines, you should always carefully consider what information you actually need and request only that information. For example, a single call to `PBGetCatInfoSync` returns Finder file type information from a file or folder. On HFS and HFS Plus file systems, the penalty for retrieving this metadata is minimal because it is stored in the file’s catalog node and read into memory along with the file name. However, on other file systems, this data may have to be read separately, incurring another read operation. Instead of `PBGetCatInfoSync`, you should have used `FSGetCatalogInfo` or `PBGetCatalogInfoSync` and specified exactly which pieces of information you wanted.

[Next](Examining%20File-System%20Usage.md)[Previous](File-System%20Performance%20Tips.md)

