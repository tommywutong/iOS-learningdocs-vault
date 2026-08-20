---
title: Empty Memory Objects
apple_id: DTS10002291
resource_type: QA
platform: macOS
topic: General
technology: null
published: '2011-07-26'
source_url: https://developer.apple.com/library/archive/qa/qa1259/_index.html
archived_at: '2026-07-18T02:30:17.996490Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1259

# Empty Memory Objects

## Q:  What does `malloc(0)` do? What about `free(NULL)`?

A: These seemingly simple questions have remarkably complex answers, especially if you generalize them to cover other Mac OS memory management APIs. Table 1 and Table 2 list some commonly-used routines and their behavior in these cases.

__Table 1__  Allocating a block of zero bytes

| Routine | Platform | Returns |
| malloc | ANSI C specification | either NULL or a pointer to a zero-length block |
| malloc | Mac OS X System framework | a pointer to a zero-length block |
| malloc | CodeWarrior MSL | NULL [1] [2] |
| CFAllocatorAllocate | all | NULL [3] |
| NewPtr | all | a pointer to a zero-length block |
| NewHandle | all | a handle to a zero-length block |
| MPAllocateAligned | Mac OS X | a pointer to a zero-length block |
| MPAllocateAligned | traditional Mac OS | NULL |
| OTAllocMem[InContext] | all | a pointer to a zero-length block |
| operator new [] | ANSI C++ specification | a pointer to a zero-length block |
| operator new [] | all | a pointer to a zero-length block |

__Table 2__  Freeing a NULL pointer

| Routine | Platform | Behavior |
| free | ANSI C specification | does nothing |
| free | all | does nothing [1] |
| CFAllocatorDeallocate | all | does nothing [4] |
| DisposePtr | Mac OS X | sets MemErr to noErr |
| DisposePtr | traditional Mac OS, PowerPC | sets MemErr to noErr |
| DisposePtr | traditional Mac OS, 68K | illegal |
| DisposeHandle | Mac OS X | sets MemErr to nilHandleErr |
| DisposeHandle | traditional Mac OS | sets MemErr to noErr |
| MPFree | Mac OS X | illegal [5] |
| MPFree | traditional Mac OS | does nothing |
| OTFreeMem | all | does nothing |
| operator delete | ANSI C++ specification | does nothing |
| operator delete | all | does nothing |

__Notes:__

1. MSL information obtained from CodeWarrior Pro 8.3 MSL.
2. You can alter this behavior by setting the `_MSL_MALLOC_0_RETURNS_NON_NULL` compile-time variable and rebuilding MSL.
3. This behavior is part of `CFAllocatorAllocate` and is independent of the actual allocator used.
4. This behavior is part of `CFAllocatorDeallocate` and is independent of the actual allocator used.
5. On current versions of Mac OS X (10.2 and earlier), this will not crash but instead print an a warning message to the console
   (r. 3227311)
   .

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-26 | Reformatted content and made minor editorial changes. |
| 2003-04-21 | New document that describes how two memory management edge cases are handled by the common Mac OS memory allocators. |

