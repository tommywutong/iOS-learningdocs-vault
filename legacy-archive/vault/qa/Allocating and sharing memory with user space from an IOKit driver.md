---
title: Allocating and sharing memory with user space from an IOKit driver
apple_id: DTS10001724
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2008-10-13'
source_url: https://developer.apple.com/library/archive/qa/qa1197/_index.html
archived_at: '2026-07-18T02:30:12.412229Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1197

# Allocating and sharing memory with user space from an I/O Kit driver

## Q:  My I/O Kit kernel driver maps memory to user space using `IOMemoryDescriptor::createMappingInTask`. But `createMappingInTask` fails and returns `NULL`. How should a driver share memory with a user process?

A: My I/O Kit kernel driver maps memory to user space using `IOMemoryDescriptor::createMappingInTask`. But  `createMappingInTask`  fails and returns `NULL`. How should a driver share memory with a user process?

`IOMemoryDescriptor::createMappingInTask` returns `NULL` because the buffer could not be mapped as requested. There are a couple of reasons why this can happen.

I/O Kit uses the kernel `zalloc` pool as its small `malloc` resource. This gives driver writers fast allocations for local use. This is very important for `new` operators and short-lived buffers.

The problem arises when a driver writer tries to share memory with user space, forgetting that the zone allocator is designed for temporary and very private allocations. Under the covers, I/O Kit allocators such as `IOMalloc, IOMallocAligned,` and `IOMallocContiguous` may use this zone allocator to improve the performance of frequent, small allocations.

Also, since mapping is a virtual memory concept, maps are always sized to an integral number of pages.

The preferred way to allocate kernel memory for sharing is to allocate the buffer and memory descriptor together using  `IOBufferMemoryDescriptor` as shown in Listing 1.

__Listing 1__  Use of IOBufferMemoryDescriptor.

```
IOBufferMemoryDescriptor* memDesc;  memDesc = IOBufferMemoryDescriptor::withOptions(               kIODirectionOutIn | kIOMemoryKernelUserShared,               alloc_bytes, page_size );
```

The `kIOMemoryKernelUserShared` option ensures that the buffer is mapped to a page boundary.

A less-preferable option is to request an integral number of pages from `IOMallocAligned` or `IOMallocContiguous`. In that case, either of these interfaces will return a buffer capable of being shared.

Once you've allocated your buffer using either of these techniques, it can be shared with user space using `IOMemoryDescriptor::createMappingInTask`.

It is strongly recommended that you create buffers shared between the kernel and user space from the kernel. However, there are cases where that isn't practical, such as a driver that reads from or writes to application-created buffers. In that situation, `createMappingInTask` can fail for another reason. `createMappingInTask` can only create mappings for memory that is described by a single VM object. However, a memory range allocated in a typical fashion using `malloc`-based functions might be described by more than one VM object.

To allocate memory in user space that is guaranteed to be described by only a single VM object, use anonymous `mmap` as shown in Listing 2.

__Listing 2__  Use of anonymous mmap.

```c
#include <sys/mman.h>  size_t		bigBufferLen; uint8_t		*bigBuffer;  bigBufferLen = 54321;  // Use anonymous mmap to ensure we get a single VM object. bigBuffer = (uint8_t *) mmap(NULL, bigBufferLen, PROT_READ | PROT_WRITE, MAP_ANON | MAP_SHARED, -1, 0); if (bigBuffer == MAP_FAILED) {     perror("mmap() call error:"); } else {     // Success.     printf("buffer is created @ %p\n", bigBuffer); }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-10-13 | Modernized content and and made editorial changes. |
| 2002-09-13 | New document that describes the preferred technique for allocating and sharing buffers in an I/O Kit kernel driver. |

