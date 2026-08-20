---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/FileSystemGuidelines.html
archived_at: '2026-07-15T08:15:26.570793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](Filename%20Extensions.md)[Previous](Sorting%20Rules.md)

# File System Guidelines

The following sections provide guidelines on ways to improve your application’s interactions with the Mac OS X file system.

Whenever you save a document, you should make sure the file you create for that document contains the following information:

- A type code
- A creator code
- A filename extension

All files in the Mac OS X file system should have a filename extension. The Finder uses filename extensions to help identify the type of a file. More importantly, other platforms commonly use filename extensions exclusively to identify the type of a file. Some programs, such as network transfer programs, often use filename extensions to determine how to transfer files. Providing a filename extension for your application’s data files makes it easier for end users to exchange your data files with users on other platforms. By the same token, including a type code and creator code make it easier to exchange data on legacy Mac OS systems.

For more information on filename extensions, including further guidelines on supporting them, see [Filename Extensions](Filename%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tolkdjjbeqskiizda).

Display names improve the user experience in Mac OS X and should be supported by all applications. A display name is a name intended for display only to the user. You cannot use display names in your code to open files. Instead, display names make it possible to localize file and folder names dynamically and hide filename extensions without losing any identifying information about the file.

For more information on how to support display names, see [Display Names](Display%20Names.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tqlkdjjbeqskiizda).

Avoid the assumption that you can perform case-insensitive file comparisons or searches. Mac OS X supports many file systems that use case to differentiate between files. Even on file systems (such as HFS+) that support case insensitivity, there are still times when case may be used to compare filenames. For example, CFBundle and NSBundle consider case when searching [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) directories for named resources.

Try testing your software on volumes (such as UFS) that do distinguish files by case.

Performance is an important consideration when writing code that deals with the file system. It can take millions of cycles of computing time from the time you request data to the time the disk is even ready to begin reading. Plus, different file systems store data differently, so although an HFS+ volume may cache the size of a directories contents, a UFS volume may calculate that value each time it’s requested.

As you design your software, make sure that you actually use the data you get and that you actually need the data you use. Reducing file-system overhead can improve your application performance significantly.

For more information on measuring and improving the performance of your file-related code, see _[File-System Performance Guidelines](../../Performance/File-System%20Performance%20Guidelines/Introduction%20to%20File-System%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dc2i)_.

A user’s files may reside on a network volume, a mobile volume, or on a local volume. If files are on a network volume, accessing them frequently may incur a greater performance penalty. If the network volume is part of a storage area network (such as an Xsan array), you may need to take additional steps to ensure the array performs at peak performance. In particular, you should do the following:

- If you need to optimize your file handling code for maximum performance on specific file systems, use `GetVolParms` or `statfs` to get information about a file system. Use special APIs if they are available.
- Lock only what you need before accessing files and be sure to release those locks as soon as possible.
- Other than the boot volume, don’t assume that a volume will always be there. Portable drives may be removed by the user at any time. Sign up for I/O Kit notifications if you need to know if a specific volume is removed from the system.

Mac OS X uses the `\n` character by itself to represent the end of a line. Most Mac OS X methods and functions that write out line ending characters write out only this character. Your own code should do the same when writing out content. When reading content, however, your code should be prepared to handle content that contains the `\n`, `\r`, or `\r\n` line endings. Being able to read these other line endings promotes interoperability with other platforms.

[Next](Filename%20Extensions.md)[Previous](Sorting%20Rules.md)

