---
title: 'Objective-C Internals: Tagged Pointer Objects Tagged pointer objects (a private runtime feature) optimize performance by storing an object’s data in its pointer value, eliminating the object’s heap al'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr'
original_language: en
published: 2023-03-19
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0204f51cfe1e305c'
translated: false
---

> 原文：[Objective-C Internals: Tagged Pointer Objects Tagged pointer objects (a private runtime feature) optimize performance by storing an object’s data in its pointer value, eliminating the object’s heap al](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Tagged Pointer Objects

![Two yellow dogs jumping in a wooded meadow. Their noses point up as each jumps to tag the other.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/0349e4f7-98ee-4653-764c-48a72cea8000/public)

Tagged pointer objects (a private runtime feature) optimize performance by storing an object’s data in its pointer value, eliminating the object’s heap allocation. This post looks at the implementation of `NSNumber` to highlight the use of and implications of this optimization.

Tagged pointer objects is a private feature of the Objective-C runtime that Apple uses to optimize some core Foundation classes (pun intended).

## What is a tagged pointer?

Most memory allocators guarantee a minimum alignment for each allocation. For example, `malloc()` on Apple’s platforms guarantees an alignment that "can be used for any data type, including AltiVec- and SSE-related types."

In practice, all allocations are 16-byte aligned, so the bottom four bits of any pointer are always zero. Sometimes it is advantageous to use this fact and store additional information in those bits (which requires updating all uses of the pointer value to handle the extra bits correctly). When unused bits in a pointer store additional information, the pointer is often referred to as _tagged_.

The `isa` pointer in Objective-C objects may be tagged, the details of which were discussed in the [Non-Pointer isa](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#non-pointer-isa) section of [The Many Uses of isa](https://alwaysprocessing.blog/2023/01/19/objc-class-isa) post earlier in this series.

## Tagged Pointer Objects

Tagged pointer objects in Objective-C are a special type of object pointer. If the object pointer is tagged, the data held by the class instance represented by the tagged pointer is encoded entirely into the pointer value itself. No heap allocation occurs.

Eliminating the heap allocation can significantly reduce the cost of, for example, an `NSArray` of `NSNumber`s. An `NSNumber` allocated on the heap uses a minimum of 16 bytes (since the allocation is 16-byte aligned) plus the 8 bytes for its pointer. However, an `NSNumber` encoded into a tagged pointer uses only the 8 bytes for its pointer, saving both memory and time by not calling the allocator.

### Tag Identity

The bit used to identify a pointer as tagged varies by platform. [objc-internal.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L755-L759) provides a convenience function to the runtime implementation that identifies whether a pointer is tagged. macOS and Catalyst apps on Intel processors use bit 0 to identify a tagged pointer object, and everything else uses bit 63.

```
#if __arm64__
  // ARM64 uses a new tagged pointer scheme...
# define _OBJC_TAG_MASK (1UL<<63)
#elif (TARGET_OS_OSX || TARGET_OS_MACCATALYST) && __x86_64__
  // 64-bit Mac - tag bit is LSB
# define _OBJC_TAG_MASK 1UL
#else
  // Everything else - tag bit is MSB
# define _OBJC_TAG_MASK (1UL<<63)
#endif

static inline bool
_objc_isTaggedPointer(const void *ptr) {
  return ((uintptr_t)ptr & _OBJC_TAG_MASK) == _OBJC_TAG_MASK;
}
```

Eliminating the heap allocation to store the object’s value also eliminates the storage for the `isa` pointer. So, the tagged pointer object scheme reserves some bits to identify the object’s class.

At the time of this writing, the Objective-C runtime has two schemes to reserve class identity bits: one reserves 3 bits for objects with 60-bit payloads, and the other reserves 11 bits for objects with 52-bit payloads.

Up to 7 class types can use the 60-bit payload variant (with the eighth type being a special case to identify the 52-bit payload variant). And up to 256 class types can use the 52-bit payload variant. [objc-internal.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L447-L509) has an enum that provides some symbolic identity for various class identity bit values.

When the runtime requires the `isa` pointer for an object, it calls `objc_object::getIsa()`^[[1](#_footnotedef_1)] (defined in [objc-object.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L76-L92)), which returns the `isa` instance variable for objects allocated on the heap and the `isa` pointer stored in one of the tag class arrays for tagged pointer objects.

```
inline Class
objc_object::getIsa() {
  if (fastpath(!isTaggedPointer())) return ISA(/*authenticated*/true);

  extern objc_class OBJC_CLASS_$___NSUnrecognizedTaggedPointer;
  uintptr_t slot, ptr = (uintptr_t)this;
  Class cls;

  slot = (ptr >> _OBJC_TAG_SLOT_SHIFT) & _OBJC_TAG_SLOT_MASK;
  cls = objc_tag_classes[slot];
  if (slowpath(cls == (Class)&OBJC_CLASS_$___NSUnrecognizedTaggedPointer)) {
      slot = (ptr >> _OBJC_TAG_EXT_SLOT_SHIFT) & _OBJC_TAG_EXT_SLOT_MASK;
      cls = objc_tag_ext_classes[slot];
  }
  return cls;
}
```

When system frameworks initialize at the start of a process, they call `_objc_registerTaggedPointerClass()` to set the `Class` object for the given tag value. We can observe this by adding a symbolic breakpoint for that function and print its arguments when called:

```
(lldb) reg re x0 x1
      x0 = 0x0000000000000003
      x1 = 0x0000000203a994f0  (void *)0x0000000203a99518: __NSCFNumber
```

### Anatomy of a Message Send

Any code that operates on the pointer value must specifically handle tagged pointers, as unconditionally dereferencing the pointer will almost certainly result in a runtime crash.

The first step in `objc_msgSend()` [checks for a tagged pointer](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/Messengers.subproj/objc-msg-arm64.s#L578-L596) to determine how to load the object’s `isa` pointer to find its class’s methods, similar to the `objc_object:getIsa()` implementation above. After the `isa` pointer is loaded, whether or not the pointer is tagged is immaterial to the remainder of the message send logic.

When an Objective-C class that supports tagged pointer objects receives a message, it must check whether its `self` pointer is tagged and handle that case appropriately. The following is my disassembly of `-[NSNumber integerValue]` to show, in part, how `NSNumber` tagged pointers work (per my interpretation of the disassembly of the following functions on macOS 12.6.2 for arm64).

```
@implementation __NSCFNumber
- (NSInteger)integerValue {
  return [self longValue];
}

- (long)longValue {
  long longValue;
  CFNumberGetValue((__bridge CFNumberRef)self, kCFNumberSInt64Type, &longValue);
  return longValue;
}
@end

Boolean CFNumberGetValue(CFNumberRef number, CFNumberType theType, void *valuePtr) {
  if (_objc_isTaggedPointer(number)) {
    if (_objc_getTaggedPointerTag(number) == OBJC_TAG_NSNumber) {
      long localMemory;
      valuePtr = valuePtr ?: (void *)&localMemory;

      uintptr_t value = _objc_getTaggedPointerValue(number);
      uintptr_t shift = (value & 0x08) ? 0x4 : 0x6;

      CFNumberType type = __CFNumberTypeTable[theType].canonicalType;
      if (type <= kCFNumberFloat64Type) {
        value = value >> shift;

        switch (type) {
        case kCFNumberSInt8Type:
          *(uint8_t *)valuePtr = (uint8_t)value;
          break;
        case kCFNumberSInt16Type:
          *(uint16_t *)valuePtr = (uint16_t)value;
          break;
        case kCFNumberSInt32Type:
          *(uint32_t *)valuePtr = (uint32_t)value;
          break;
        case kCFNumberSInt64Type:
          *(uint64_t *)valuePtr = (uint64_t)value;
          break;
        case kCFNumberFloat32Type:
          *(float *)valuePtr = (float)value;
          break;
        case kCFNumberFloat64Type:
          *(double *)valuePtr = (double)value;
          break;
        }
        return true;
      } else {
        return __CFNumberGetValueCompat(number, theType, valuePtr);
      }
    } else {
      theType = __CFNumberTypeTable[theType].canonicalType;
      return [(__bridge id)number _getValue:valuePtr forType:theType];
    }
  } else {
    // ...
  }
}
```

I’ll share a few comments and observations about the manually decompiled code above:

1. The private `__NSCFNumber` subclass (in this code path) doesn’t operate on the value of `self` and therefore does not need to handle the tagged pointer case. The `-integerValue` method acts as an alias for the `longValue` method, which calls into CoreFoundation to do the heavy lifting. Given `CFNumberRef` and `NSNumber *` are [toll-free bridged](https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes#toll-free-bridging), it makes sense to see that one type is a wrapper of the other.
2. Apple’s implementation of `CFNumber` almost certainly includes [objc-internal.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L755-L825) for access to functions that simplify working with tagged pointer objects.
3. It seems that either 4 or 6 bits of the payload act as bitflags for other `CFNumber` features, but whatever functionality that may be is not used by this function.
4. The [`__CFNumberTypeTable`](https://github.com/apple-oss-distributions/CF/blob/CF-1153.18/CFNumber.c#L385-L424) maps the public-facing type values to the corresponding fixed size type, simplifying the value extraction logic.
5. Apple has a private type, [`kCFNumberSInt128Type`](https://github.com/apple-oss-distributions/CF/blob/CF-1153.18/CFNumber.c#L423), not handled by the switch statement, so the call to `__CFNumberGetValueCompat()` is necessary for that case.
6. Floating point numbers with a non-zero fractional value do not use the tagged pointer object optimization, given the logic in the `switch` statement does not handle that scenario.
7. I am intrigued by the call to `-_getValue:forType:`. It implies another private subclass uses the tag pointer object optimization, but I didn’t trace through the various code paths to attempt to identify it.

---

[1](#_footnoteref_1). The use of C++ to implement the Objective-C runtime is pretty clever, in my opinion. I’ll discuss the mechanics of how that works in a future post.
