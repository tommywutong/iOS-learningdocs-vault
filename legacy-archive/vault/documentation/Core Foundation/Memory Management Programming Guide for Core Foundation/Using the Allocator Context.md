---
title: Memory Management Programming Guide for Core Foundation
apple_id: 10000127i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: CoreFoundation
published: '2009-10-21'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Tasks/UsingAllocatorContext.html
archived_at: '2026-07-15T07:22:34.802042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Memory Management Programming Guide for Core Foundation](Introduction.md)


[Next](Creating%20Custom%20Allocators.md)[Previous](Using%20Allocators%20in%20Creation%20Functions.md)

# Using the Allocator Context

Every allocator in Core Foundation has a _context_. A context is a structure that defines the operating environment for an object and typically consists of function pointers. The context for allocators is defined by the `CFAllocatorContext` structure. In addition to function pointers, the structure contains fields for a version number and for user-defined data

__Listing 1__  The CFAllocatorContext structure

```
typedef struct {
    CFIndex version;
    void * info;
    const void *(*retain)(const void *info);
    void (*release)(const void *info);
    CFStringRef (*copyDescription)(const void *info);
    void * (*allocate)(CFIndex size, CFOptionFlags hint, void *info);
    void * (*reallocate)(void *ptr, CFIndex newsize, CFOptionFlags hint, void *info);
    void (*deallocate)(void *ptr, void *info);
    CFIndex (*preferredSize)(CFIndex size, CFOptionFlags hint, void *info);
} CFAllocatorContext;
```

The `info` field contains any specially defined data for the allocator. For example, an allocator could use the `info` field to track outstanding allocations.

If you have some user-defined data in the allocator context (the `info` field), use the `CFAllocatorGetContext` function to obtain the `CFAllocatorContext` structure for an allocator. Then evaluate or handle the data as needed. The following code provides an example of this:

__Listing 2__  Getting the allocator context and user-defined data

```
static int numOutstandingAllocations(CFAllocatorRef alloc) {
    CFAllocatorContext context;
    context.version = 0;
    CFAllocatorGetContext(alloc, &context);
    return (*(int *)(context.info));
}
```

Other Core Foundation functions invoke the memory-related callbacks defined in an allocator context and take or return an untyped pointer to a block of memory (`void *`):

- `CFAllocatorAllocate`, allocates a block of memory.
- `CFAllocatorReallocate` reallocates a block of memory.
- `CFAllocatorDeallocate` deallocates a block of memory.
- `CFAllocatorGetPreferredSizeForSize` gives the size of memory likely to be allocated, given a certain request.

[Next](Creating%20Custom%20Allocators.md)[Previous](Using%20Allocators%20in%20Creation%20Functions.md)

