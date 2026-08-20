---
title: Memory Management Programming Guide for Core Foundation
apple_id: 10000127i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: CoreFoundation
published: '2009-10-21'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Tasks/UsingAllocators.html
archived_at: '2026-07-15T07:22:35.617837Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Memory Management Programming Guide for Core Foundation](Introduction.md)


[Next](Using%20the%20Allocator%20Context.md)[Previous](Byte%20Ordering.md)

# Using Allocators in Creation Functions

Each Core Foundation opaque type has one or more _creation functions_, functions that create and return an object of that type initialized in a particular way. All creation functions take as their first parameter a reference to an allocator object (`CFAllocatorRef`). Some functions may also have allocator parameters for specialized allocation and deallocation purposes.

You have several options for the allocator-reference parameters:

- You can pass the constant `kCFAllocatorSystemDefault`; this specifies the generic system allocator (which is the initial default allocator).
- You can pass `NULL` to specify the current default allocator (which might be a custom allocator or the generic system allocator). This is the same as passing `kCFAllocatorDefault`.
- You can pass the constant `kCFAllocatorNull` which indicates an allocator that does not allocate—it is an error to attempt to use it. Some creation functions have a parameter for a special allocator used to reallocate or free a backing store; by specifying `kCFAllocatorNull` for the parameter, you prevent automatic reallocation or deallocation.
- You can get a reference to the allocator used by another Core Foundation object with the `CFGetAllocator` function and pass that reference in. This technique allows you to put related objects in a memory “zone” by using the same allocator for allocating them.
- You can pass a reference to a custom allocator (see [Creating Custom Allocators](Creating%20Custom%20Allocators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge2tilkdjjbekscbifdq)).

If you are to use a custom allocator and you want to make it the default allocator, it is advisable to first get a reference to the current default allocator using the `CFAllocatorGetDefault` function and store that in a local variable. When you are finished using your custom allocator, use the `CFAllocatorSetDefault` function to reset the stored allocator as the default allocator.

[Next](Using%20the%20Allocator%20Context.md)[Previous](Byte%20Ordering.md)

