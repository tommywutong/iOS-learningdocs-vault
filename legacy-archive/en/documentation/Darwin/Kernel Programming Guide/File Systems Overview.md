---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/Filesystem/Filesystem.html
archived_at: '2026-07-15T07:23:11.548359Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](Network%20Architecture.md)[Previous](BSD%20Overview.md)

# File Systems Overview

OS X provides “out-of-the-box” support for several different file systems. These include Mac OS Extended format (_HFS+_), the BSD standard file system format (_UFS_), _NFS_ (an industry standard for networked file systems), ISO 9660 (used for CD-ROM), MS-DOS, SMB (Windows file sharing standard), AFP (Mac OS file sharing), and UDF.

Support is also included for reading the older, Mac OS Standard format (_HFS_) file-system type; however, you should not plan to format new volumes using Mac OS Standard format. OS X cannot boot from these file systems, nor does the Mac OS Standard format provide some of the information required by OS X.

The Mac OS Extended format provides many of the same characteristics as Mac OS Standard format but adds additional support for modern features such as file permissions, longer filenames, Unicode, both hard and symbolic links, and larger disk sizes.

UFS provides case sensitivity and other characteristics that may be expected by BSD commands. In contrast, Mac OS Extended Format is not case-sensitive (but is case-preserving).

OS X currently can boot and “root” from an HFS+, UFS, ISO, NFS, or UDF volume. That is, OS X can boot from and mount a volume of any of these types and use it as the primary, or root, file system.

Other file systems can also be mounted, allowing users to gain access to additional volume formats and features.

NFS provides access to network servers as if they were locally mounted file systems. The Carbon application environment mimics many expected behaviors of Mac OS Extended format on top of both UFS and NFS. These include such characteristics as Finder Info, file ID access, and aliases.

By using the OS X Virtual File System (VFS) capability and writing kernel extensions, you can add support for other file systems. Examples of file systems that are not currently supported in OS X but that you may wish to add to the system include the Andrew file system (AFS) and the Reiser file system (ReiserFS). If you want to support a new volume format or networking protocol, you’ll need to write a file-system kernel extension.

In OS X, the _vnode_ structure provides the internal representation of a file or directory (folder). There is a unique vnode allocated for each active file or folder, including the root.

Within a file system, operations on specific files and directories are implemented via vnodes and _VOP_ (vnode operation) calls. VOP calls are used for operations on individual files or directories (such as open, close, read, or write). Examples include `VOP_OPEN` to open a file and `VOP_READ` to read file contents.

In contrast, file-system–wide operations are implemented using VFS calls. VFS calls are primarily used for operations on entire file systems; examples include `VFS_MOUNT` and `VFS_UNMOUNT` to mount or unmount a file system, respectively. File-system writers need to provide stubs for each of these sets of calls.

The details of the VFS subsystem in OS X are in the process of changing in order to make the VFS interface sustainable.

If you are writing a leaf file system, these changes will still affect you in many ways. Please contact Apple Developer Support for more information.

[Next](Network%20Architecture.md)[Previous](BSD%20Overview.md)

