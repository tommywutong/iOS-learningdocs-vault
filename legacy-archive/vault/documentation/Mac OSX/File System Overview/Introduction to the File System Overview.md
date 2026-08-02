---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/BPFileSystem.html
archived_at: '2026-07-15T08:15:35.768352Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](File-System%20Domains.md)

# Introduction to the File System Overview

The file system is an important part of any operating system. After all, it’s where users keep their stuff. In Mac OS X, the organization of the file system plays an important role in helping the user find files. The organization also makes it easier for applications and the system itself to find the resources they need to support the user.

The file system in Mac OS X has at its core a set of directories inherited from the Berkeley Software Distribution (BSD) operating system. While most of these directories are actually hidden by the Finder, many elements of the BSD world are still apparent. The file permissions model, symbolic links, and user home directories are all concepts inherited from BSD. Mac OS X also adds many of its own concepts to provide the user with a secure and elegant environment for managing files and folders.

The Mac OS X file system was designed to provide power and flexibility while maintaining the traditional ease-of-use users expect. To this end, the file system provides users with a consistent structure that makes it clear where resources are located. (This consistency also helps developers, whose applications need to know where important resources are located.) Other file system conventions, such as aliases, extension hiding, and display names also enhance the user experience.

The Mac OS X File System contains the following articles:

- [File-System Domains](File-System%20Domains.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dclkdjjbeqskiizda) describes the high-level organization of the file system in Mac OS X.
- [The Library Directory](The%20Library%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4delkciffeqq2ijjeq) describes the standard subdirectories that are used to configure the system and user environments.
- [The Developer Directory](The%20Developer%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dglkcineuuqkhi5dq) describes the developer-specific directories that are installed with the Xcode Tools.
- [Where to Put Application Files](Where%20to%20Put%20Application%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimjrfvbecssiineeusi) provides guidelines on where applications should place non-essential configuration and support files.
- [Files and the Finder](Files%20and%20the%20Finder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dklkcineuuskhircq) describes the role of the Finder in managing the file system. It also explains some of the techniques the Finder uses to associate files with applications.
- [Sorting Rules](Sorting%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tolkcineuuskhircq) explains the rules for ordering file and directory names in Finder windows.
- [File System Guidelines](File%20System%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tmlkdjjbeqskiizda) offers tips and advice on how best to support Mac OS X file system features.
- [Filename Extensions](Filename%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tolkdjjbeqskiizda) describes the Mac OS X support for filename extensions and how to support them in your applications.
- [Display Names](Display%20Names.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4tqlkdjjbeqskiizda) explains the difference between file names in the file system and the file names that users see. It also explains when your application should use display names.
- [BSD Permissions and Ownership](BSD%20Permissions%20and%20Ownership.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dmlktk4yq) describes the principles behind file permissions and their implications for file management in Mac OS X.
- [Access Control Lists](Access%20Control%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemzqfvjvomi) provides an overview of access control lists and how they are used to supplement BSD permissions.
- [File System Comparisons](File%20System%20Comparisons.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dolkciffesr2firaq) offers a comparison of features between HFS+ and UFS volume formats.
- [Aliases and Symbolic Links](Aliases%20and%20Symbolic%20Links.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi4dqlkciffeerkiizba) describes the differences between aliases and symbolic links.

[Next](File-System%20Domains.md)

