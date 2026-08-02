---
title: Apple File System Guide
apple_id: TP40016999
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/APFS_Guide/ToolsandAPIs/ToolsandAPIs.html
archived_at: '2026-07-15T07:31:54.657433Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Apple File System Guide](Introduction.md)


[Next](Volume%20Format%20Comparison.md)[Previous](Frequently%20Asked%20Questions.md)

# Tools and APIs

**__hfs_convert_apfs__**
: `hfs_convert_apfs`

**__diskutil apfs …__**
: `diskutil apfs createContainer /dev/disk1s1`

`diskutil apfs addVolume disk1s1 APFS newAPFS`

**__hdiutil__**
: `hdiutil create -fs APFS -size 1GB foo.sparseimage`

**__fsck_apfs__**
: `fsck_apfs`

**__Foundation / FileManager__**
: |  |
```swift
func copyItem(atPath srcPath: String,
              toPath dstPath: String) throws
```

```swift
func replaceItem(at originalItemURL: URL,
              withItemAt newItemURL: URL,
      backupItemName backupItemName: String?,
                    options options:
          FileManager.ItemReplacementOptions = [],
      resultingItemURL resultingURL:
          AutoreleasingUnsafeMutablePointer<NSURL?>?) throws
```

**__libcopyfile__**
: |  |
```c
#include <copyfile.h>

int copyfile(const char *from,
             const char *to,
       copyfile_state_t state,
       copyfile_flags_t flags);

int fcopyfile(int from_fd,
             int to_fd,
             copyfile_state_t state,
             copyfile_flags_t flags);
// new flag bit: COPYFILE_CLONE
// equivalent to (COPYFILE_EXCL | COPYFILE_ACL | COPYFILE_STAT | COPYFILE_XATTR | COPYFILE_DATA)
```

**__Safe Save APIs__**
: |  |
```c
#include <stdio.h>

int renamex_np(const char *, const char *, unsigned int)

int renameatx_np(int, const char *, int, const char *, unsigned int)
```

**__Cloning APIs__**
: |  |
```c
#include <sys/attr.h>
#include <sys/clonefile.h>

int clonefileat(int, const char *, int, const char *, uint32_t);
int fclonefileat(int, int, const char *, uint32_t);
int clonefile(const char *, const char *, uint32_t);
```

[Next](Volume%20Format%20Comparison.md)[Previous](Frequently%20Asked%20Questions.md)

