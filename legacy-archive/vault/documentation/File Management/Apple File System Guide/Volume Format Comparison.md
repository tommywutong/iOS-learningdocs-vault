---
title: Apple File System Guide
apple_id: TP40016999
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/VolumeFormatComparison/VolumeFormatComparison.html
archived_at: '2026-07-15T07:31:54.670186Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple File System Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Tools%20and%20APIs.md)

# Volume Format Comparison

|  | Mac OS Extended (HFS+) | Apple File System (APFS) |
| --- | --- | --- |
| Number of allocation blocks | 232 (4 billion) | 263 (9 quintillion) |
| File IDs | 32-bit | 64-bit |
| Maximum file size | 263 bytes | 263 bytes |
| Time stamp granularity | 1 second | 1 nanosecond |
| Copy-on-write |  | ✔ |
| Crash protected | Journaled | ✔ |
| File and directory clones |  | ✔ |
| Snapshots |  | ✔ |
| Space sharing |  | ✔ |
| Native encryption |  | ✔ |
| Sparse files |  | ✔ |
| Fast directory sizing |  | ✔ |

[Next](Document%20Revision%20History.md)[Previous](Tools%20and%20APIs.md)

