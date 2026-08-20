---
title: Memory Management Programming Guide for Core Foundation
apple_id: 10000127i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: CoreFoundation
published: '2009-10-21'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Tasks/CustomAllocators.html
archived_at: '2026-07-15T07:22:34.330545Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Memory Management Programming Guide for Core Foundation](Introduction.md)


[Next](Byte%20Swapping.md)[Previous](Using%20the%20Allocator%20Context.md)

# Creating Custom Allocators

To create a custom allocator, first declare and initialize a structure of type `CFAllocatorContext`. Initialize the version field to 0 and allocate and assign any desired data, such as control information, to the `info` field. The other fields of this structure are function pointers described in [Implementing Allocator Callbacks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2tiljrgaytaobr), below.

Once you have assigned the proper values to the fields of the `CFAllocatorContext` structure, invoke the `CFAllocatorCreate` function to create the allocator object. The second parameter of this function is a pointer to the structure. The first parameter of this function identifies an allocator to use for allocating memory for the new object. If you want to use the `allocate` callback in the `CFAllocateContext` structure for this purpose, specify the `kCFAllocatorUseContext` constant for the first parameter. If you want to use the default allocator, specify `NULL` in this parameter.

__Listing 1__  Creating a custom allocator

```
static CFAllocatorRef myAllocator(void) {
    static CFAllocatorRef allocator = NULL;
    if (!allocator) {
        CFAllocatorContext context =
            {0, NULL, NULL, (void *)free, NULL,
             myAlloc, myRealloc, myDealloc, NULL};
        context.info = malloc(sizeof(int));
        allocator = CFAllocatorCreate(NULL, &context);
    }
    return allocator;
}
```


The `CFAllocatorContext` structure has seven fields defining callback functions. If you create a custom allocator you must implement at least the `allocate` function. Allocator callbacks should be thread-safe and, if the callback invokes other functions, they should be re-entrant as well.

The retain, release, and copy-description callbacks all take as their single argument the `info` field of the `CFAllocatorContext` structure. Typed as `void *`, this field points to any data that you define for the allocator, such as a structure containing control information.

_Retain Callback_:

```
const void *(*retain)(const void *info);
```

Retain the data you have defined for the allocator context in `info`. This might make sense only if the data is a Core Foundation object. You may set this function pointer to `NULL`.

_Release Callback_:

```
void (*release)(const void *info);
```

Release (or free) the data you have defined for the allocator context. You may set this function pointer to `NULL`, but doing so might result in memory leaks.

_Copy Description Callback_:

```
CFStringRef (*copyDescription)(const void *info);
```

Return a reference to a CFString that describes your allocator, particularly some characteristics of your user-defined data. You may set this function pointer to `NULL`, in which case Core Foundation will provide a rudimentary description.

_Allocate Callback_:

```
void *   (*allocate)(CFIndex size, CFOptionFlags hint, void *info);
```

Allocate a block of memory of at least `size` bytes and return a pointer to the start of the block. The `hint` argument is a bitfield that you should currently not use. The `size` parameter should always be greater than 0. If it is not, or if problems in allocation occur, return `NULL`. This callback may not be `NULL`.

_Reallocate Callback_:

```
void *   (*reallocate)(void *ptr, CFIndex newsize, CFOptionFlags hint, void *info);
```

Change the size of the block of memory pointed to by `ptr` to the size specified by `newsize` and return the pointer to the larger block of memory. Return `NULL` on any reallocation failure, leaving the old block of memory untouched. Note that the _ptr_ parameter will never be `NULL`, and _newsize_ will always be greater than `0`—this callback is not used unless those two conditions are met.

Leave the contents of the old block of memory unchanged up to the lesser of the new or old sizes. If the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur. The `hint` argument is a bitfield that you should currently not use. If you set this callback to `NULL` the `CFAllocatorReallocate` function returns `NULL` in most cases when it attempts to use this allocator.

_Deallocate Callback_:

```
void   (*deallocate)(void *ptr, void *info);
```

Make the block of memory pointed to by _ptr_ available for subsequent reuse by the allocator but unavailable for continued use by the program. The `ptr` parameter cannot be `NULL` and if the `ptr` parameter is not a block of memory that has been previously allocated by the allocator, the results are undefined; abnormal program termination can occur. You can set this callback to `NULL`, in which case the `CFAllocatorDeallocate` function has no effect.

_Preferred Size Callback_:

```
CFIndex   (*preferredSize)(CFIndex size, CFOptionFlags hint, void *info);
```

Return the actual size the allocator is likely to allocate given a request for a block of memory of size `size`. The `hint` argument is a bitfield that you should currently not use.

[Next](Byte%20Swapping.md)[Previous](Using%20the%20Allocator%20Context.md)

