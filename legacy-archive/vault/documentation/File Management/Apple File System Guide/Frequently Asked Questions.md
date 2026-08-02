---
title: Apple File System Guide
apple_id: TP40016999
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/FAQ/FAQ.html
archived_at: '2026-07-15T07:31:54.628167Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple File System Guide](Introduction.md)


[Next](Tools%20and%20APIs.md)[Previous](Features.md)

# Frequently Asked Questions

__Can I use Apple File System with my existing hard disk drive?__

Yes. Apple File System is optimized for Flash/SSD storage, but can also be used with traditional hard disk drives (HDD) and external, direct-attached storage.

__Can I reshare APFS-formatted volumes using a network file-sharing protocol?__

Yes, you can share APFS-formatted volumes using the SMB or NFS network file-sharing protocol.

You cannot share APFS-formatted volumes using AFP. The AFP protocol is deprecated.

__Can I use my third-party disk utilities with an APFS-formatted hard disk?__

Existing third-party utilities may need to be updated to support Apple File System. Consult the utility's documentation, or contact the vendor for compatibility information.

__Can I boot macOS High Sierra from an APFS-formatted hard disk?__

Yes. macOS High Sierra supports Apple File System for both bootable and data volumes.

__How do I upgrade to Apple File System?__

The macOS High Sierra installer offers nondestructive in-place upgrades from HFS+ to APFS for bootable volumes. You can use Disk Utility to convert external volumes from HFS+ to APFS format.

__If I convert a volume to APFS, can I later revert to HFS+?__

You can use Disk Utility to erase an APFS-formatted volume and reformat as HFS+. However, your data will not be preserved when you reformat the volume as HFS+.

__Why did Apple develop APFS?__

Apple File System is uniquely designed to meet the needs of Apple’s products and ecosystem. Apple File System provides strong encryption, ultra-low latencies and limited memory overhead. It is optimized for Flash/SSD storage and can be used on everything from an Apple Watch to a Mac Pro.

HFS+ and its predecessor HFS are more than 30 years old. These file systems were developed in an era of floppy disks and spinning hard drives, when file sizes were calculated in kilobytes or megabytes.

Today, people commonly store hundreds of gigabytes and access millions of files on high-speed, low-latency flash drives. People carry their data with them, and they demand that sensitive information be secure.

__How does Apple File System handle filenames?__

APFS accepts only valid UTF-8 encoded filenames for creation, and preserves both case and normalization of the filename on disk in all variants. APFS, like HFS+, is case-sensitive on iOS and is available in case-sensitive and case-insensitive variants on macOS, with case-insensitive being the default.

In macOS High Sierra, APFS is normalization-insensitive in both the case-insensitive and case-sensitive variants, using a hash-based native normalization scheme. In iOS 11, APFS is normalization-insensitive as well, using either a native normalization scheme (erase restores only) or runtime normalization scheme (upgrades from previous versions). Runtime normalization will also be available in iOS 10.3.3 and macOS Sierra 10.12.6. Being normalization-insensitive ensures that normalization variants of a filename cannot be created in the same directory, and that a filename can be found with any of its normalization variants. __This means that you don’t need to do any additional work to ensure correct normalization behavior in these versions of macOS and iOS.__

Some differences between how APFS and HFS+ handle filenames include the following:

- APFS implements normalization and case insensitivity according to the Unicode 9.0 standard; this enables APFS to support a wider range of languages for these features than HFS+, which is based on Unicode 3.2.
- APFS preserves the normalization of the filename and uses hashes of the normalized form of the filename to provide normalization insensitivity, whereas HFS+ stores the normalized form of the filename on disk to provide normalization insensitivity.
- Calling `readdir(2)` on a directory in APFS returns filenames in hash order, whereas HFS+ returns filenames in lexicographical order.
- While both filesystems expect filenames to be encoded in UTF-8, APFS stores filenames on disk in UTF-8 encoding, whereas HFS stores filenames on disk in UTF-16 encoding.
- APFS doesn’t allow files to be created with filenames that contain unassigned codepoints in the Unicode 9.0 standard, whereas HFS+ does.

In iOS 10.3 and in the case-sensitive variant of the developer preview of APFS in macOS Sierra, APFS is normalization-sensitive. For these versions, developers should be aware of behavior differences between normalization sensitivity and insensitivity that may arise when a device upgrades macOS or iOS and migrates the filesystem from HFS+ to APFS. For example, attempting to create a file using one normalization behavior and then opening that file using another normalization behavior may result in `ENOENT`, or “File Not Found” errors. Additionally, storing filenames externally, such as in the defaults database, Core Data, or iCloud storage may cause problems if the normalization scheme of the filename being stored is different from what exists on disk.

To avoid introducing bugs in your code with mismatched Unicode normalization (for iOS 10.3.0, 10.3.1 and 10.3.2) in filenames, do the following:

- Use high-level Foundation APIs such as [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) and [NSURL](https://developer.apple.com/documentation/foundation/nsurl) when interacting with the filesystem.
- Use the [fileSystemRepresentation](https://developer.apple.com/documentation/foundation/nsurl/1412925-filesystemrepresentation) property of [NSURL](https://developer.apple.com/documentation/foundation/nsurl) objects when creating and opening files with lower-level filesystem APIs such as POSIX `open(2)`, or when storing filenames externally from the filesystem.

__Can RAID be used with Apple File System?__

Yes. Apple File System does not directly implement software RAID; however APFS-formatted volumes can be combined with an Apple RAID volume to support Striping (RAID 0), Mirroring (RAID 1), and Concatenation (JBOD). APFS-formatted volumes can also be used with direct-attached hardware RAID solutions.

__Does Apple File System support directory hard links?__

Directory hard links are not supported by Apple File System. All directory hard links are converted to symbolic links or aliases when you convert from HFS+ to APFS volume formats on macOS.

__Does Apple File System support redundant metadata?__

With modern Flash/SSD storage, writing two blocks of data to different locations does not guarantee that the blocks will be written to separate locations. The Flash translation layer typically groups writes together into the same NAND block. Therefore it affords no extra protection to write a second copy at the same time the first copy is written.

__What has Apple done to ensure the reliability of my data?__

Apple products are designed to prevent data corruption and protect against data loss.

To protect data from hardware errors, all Flash/SSD and hard disk drives used in Apple products use Error Correcting Code (ECC). ECC checks for transmission errors, and when necessary, corrects on the fly. Apple File System uses a unique copy-on-write scheme to protect against data loss that can occur during a crash or loss of power. And to further ensure data integrity, Apple File System uses the Fletcher's checksum algorithm for metadata operations.

__Does Apple File System use journaling?__

Apple File System uses copy-on-write to avoid in-place changes to file data, which ensures that file system updates are crash protected without the write-twice overhead of journaling.

__Does Apple File System support data deduplication?__

No. With Apple File System individual extents can be encrypted, making it impossible to examine and deduplicate files and their content. Apple File System uses clone files to minimize data storage and data duplication.

__Does Apple File System support TRIM operations?__

Yes. TRIM operations are issued asynchronously from when files are deleted or free space is reclaimed, which ensures that these operations are performed only after metadata changes are persisted to stable storage.

__Is APFS open source?__

An open source implementation is not available at this time. Apple plans to document and publish the APFS volume format specification.

[Next](Tools%20and%20APIs.md)[Previous](Features.md)

