---
title: Apple File System Guide
apple_id: TP40016999
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/Features/Features.html
archived_at: '2026-07-15T07:31:54.635488Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple File System Guide](Introduction.md)


[Next](Frequently%20Asked%20Questions.md)[Previous](Introduction.md)

# Features

Apple File System is a 64-bit file system supporting over 9 quintillion files on a single volume. This state-of-the-art file system features cloning for files and directories, snapshots, space sharing, fast directory sizing, atomic safe-save primitives, and improved filesystem fundamentals, as well as a unique copy-on-write design that uses I/O coalescing to deliver maximum performance while ensuring data reliability.

Security and privacy are fundamental in the design of Apple File System. That's why Apple File System implements strong full-disk encryption, encrypting files and all sensitive metadata.

Which encryption methods are available depends on hardware and operating system support, and can vary for Mac, iPhone, iPad, Apple TV, and Apple Watch.

Apple File System supports the following encryption models for each volume in a container:

- No encryption
- Single-key encryption
- Multi-key encryption with per-file keys for file data and a separate key for sensitive metadata

Multi-key encryption ensures the integrity of user data. Even if someone were to compromise the physical security of the device and gain access to the device key, they still couldn't decrypt the user's files.

Apple File System uses AES-XTS or AES-CBC encryption modes, depending on hardware.

Apple File System uses a novel copy-on-write metadata scheme to ensure that updates to the file system are crash protected, without the write-twice overhead of journaling.

Fast directory sizing allows Apple File System to quickly compute the total space used by a directory hierarchy, and update it as the hierarchy evolves.

Fast directory sizing works by precomputing the size of directory as content is added and removed. Therefore, it is most appropriate for directories that contain many files and have relatively little churn. For example, a user’s Documents folder is a good candidate for fast directory sizing, whereas the `/tmp` directory would not.

The file system can enable fast directory sizing on empty directories. You cannot enable Fast Directory Sizing on directories containing files or other directories directly; you must instead first create a new directory, enable fast directory sizing on it, and then move the contents of the existing directory to the new directory.

Apple File System introduces a new Atomic Safe-Save primitive for bundles and directories. Atomic Safe-Save performs renames in a single transaction such that, from the user’s perspective, the operation either is completed or does not happen at all.

[Next](Frequently%20Asked%20Questions.md)[Previous](Introduction.md)

