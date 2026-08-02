---
title: File System Overview
apple_id: 10000185i
resource_type: Guide
platform: macOS
topic: Data Management
technology: null
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFileSystem/Articles/ACLs.html
archived_at: '2026-07-15T08:15:22.300762Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Overview](Introduction%20to%20the%20File%20System%20Overview.md)


[Next](File%20System%20Comparisons.md)[Previous](BSD%20Permissions%20and%20Ownership.md)

# Access Control Lists

Mac OS X v10.4 introduced support for access control lists (ACLs)—a more fine-grained approach for implementing file and directory permissions. ACLs supplement the existing BSD permissions model in cases where more control is needed over who has access to a file or directory and what actions that person may perform. For example, using ACLs you can assign access rights for a file to multiple users and groups, each with its own distinct permission sets.

In addition to enhancing the ownership model for files and directories, ACLs also offer more fine-grained access to those entities. The basic BSD permissions for a file allow a user or group to read, write or execute that file. With ACLs, you could let a user write data to the file but not delete the file or change its file-system attributes. Similarly, you could let a user read the file attributes but not search the file or read its data.

ACLs are most often used in file server implementations, where fine-grained access to files and directories is crucial. Mac OS X Server v10.4 supports ACLs and the ability to configure them for share points and directories. The client version of Mac OS X v10.4 respects the presence of ACLs but does not currently use them to specify file and directory permissions.

If you are writing an application that interacts with the file system directly, you should check for the existence of ACLs and respect their presence. For example, developers of file backup software must remember to save ACL data along with the corresponding files and directories and be able to restore that data later.

For detailed information about ACL support in Mac OS X, see _[Security Overview](../../Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_ . For more information on how to read and write ACL information in your own code, see the `acl` man page.

[Next](File%20System%20Comparisons.md)[Previous](BSD%20Permissions%20and%20Ownership.md)

