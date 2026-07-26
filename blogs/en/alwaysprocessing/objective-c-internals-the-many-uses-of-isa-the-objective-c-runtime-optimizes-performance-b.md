---
title: 'Objective-C Internals: The Many Uses of isa The Objective-C runtime optimizes performance by packing additional information into an object’s isa pointer. This post compares the different packing mecha'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/01/19/objc-class-isa'
original_language: en
published: 2023-01-19
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d9c27a69ebece0ab'
translated: false
---

> 原文：[Objective-C Internals: The Many Uses of isa The Objective-C runtime optimizes performance by packing additional information into an object’s isa pointer. This post compares the different packing mecha](https://alwaysprocessing.blog/2023/01/19/objc-class-isa)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: The Many Uses of isa

![Two dogs sitting in a long hallway with many different doors. Which variant will they choose?](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c42b427a-167d-4a99-224d-48f7af07c100/public)

The Objective-C runtime optimizes performance by packing additional information into an object’s `isa` pointer. This post compares the different packing mechanisms and discusses the various field values stored in the pointer value.

The first post in this series [introduced](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#method-dispatch) the `isa` pointer: an instance variable in every Objective-C object that points to its class object, which identifies the type of the object instance. The previous post cited the [internal definition](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl#preamble) of this field (`char isa_storage[sizeof(isa_t)]`) and mentioned the `isa` field is deprecated. Now, we’ll explore how the runtime uses this field and its deprecation in more detail.

## Background

In Apple’s 32-bit Objective-C runtime on iOS, macOS, and tvOS, the `isa` field is just a pointer to the object’s class object. The following code from [`objc-private.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-private.h#L80-L110), [`objc-object.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L976-L993), and [`objc-class.mm`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-class.mm#L181-L185) shows the effective implementation (for these platforms) of the `object_getClass()` runtime function, which gets the `isa` class pointer value from an object instance.

```
// objc-private.h
union isa_t {
private:
    Class cls;

public:
    Class getClass(bool authenticated);
};

// objc-object.h
Class objc_object::getIsa() {
    return ISA(); // bool argument defaulted to false
}

Class isa_t::getClass(bool) {
    return cls;
}

Class objc_object::ISA(bool) {
    return isa().getClass(false);
}

// objc-class.mm
Class object_getClass(id obj) {
    if (obj) return obj->getIsa();
    else return Nil;
}
```

## Non-Pointer isa

Apple’s 64-bit Objective-C runtime (except for simulators on 64-bit Intel processors) and the Apple Watch Objective-C runtime use a “non-pointer `isa`,” which packs additional information into unused pointer bits.

Setting additional bits in the pointer value changes the address it references and invalidates its value—the new value may not be an address in the process address space, it may cause unaligned memory access if dereferenced, etc. Hence the name “non-pointer `isa`.”

Because the `isa` field no longer stores only the class pointer value, it is marked as deprecated in the [`objc.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc.h#L41-L43) public header to discourage direct use that may lead to undefined behavior. (The availability macro definition is in [`objc-api.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-api.h#L170-L172).) The `object_getClass()` and `object_setClass()` functions are the official replacement for direct use of the `isa` field.

```
// objc-api.h
#if !defined(OBJC_ISA_AVAILABILITY)
#   define OBJC_ISA_AVAILABILITY  __attribute__((deprecated))
#endif

// objc.h
struct objc_object {
    Class _Nonnull isa  OBJC_ISA_AVAILABILITY;
};
```

### Non-Pointer isa Variants

At the time of this writing, there are [three implementations](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/isa.h#L44-L171) of the non-pointer `isa`:

1. Packed `isa` (Apple Silicon `arm64`-not-`e` variant, 64-bit Intel)
2. Packed `isa` with Pointer Authentication (Apple Silicon `arm64e` variant)
3. Indexed `isa` (Apple Watch)

The following table shows the additional fields packed into the unused class pointer bits for each non-pointer `isa` variant:

Packed `isa`

Packed `isa` + Ptr Auth

Indexed `isa`

`nonpointer`

✓

✓

✓

`has_assoc`

✓

✓

✓

`has_cxx_dtor`

✓

x

✓

`shiftcls`

✓

−

−

`shiftcls_and_sig`

−

✓

−

`indexcls`

−

−

✓

`magic`

✓

✓

✓

`weakly_referenced`

✓

✓

✓

`has_sidetable_rc`

✓

✓

✓

`extra_rc`

✓

✓

✓

**Legend:**

- ✓ variant has this field
- − field not applicable for variant
- x variant does **not** have this field

Now, let’s explore the use of each field in the runtime and how they’re used to improve Objective-C runtime performance.

### nonpointer

This is the least significant bit of the pointer payload (and therefore always zero for pointer values) and, if set, indicates the `isa` value is the non-pointer variant. This field enables the runtime to use the legacy `isa`-value-is-a-class-pointer behavior or the non-pointer-`isa` optimizations on a per-class basis at run time for compatibility purposes.

On macOS, non-pointer `isa` is disabled for any application [linked for OS X 10.10 or earlier](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L3610-L3616), as direct `isa` usage was not deprecated until OS X 10.11.

```
if (dyld_get_active_platform() == PLATFORM_MACOS && !dyld_program_sdk_at_least(dyld_platform_version_macOS_10_11)) {
    DisableNonpointerIsa = true;
}
```

If the main application executable has a [`__DATA,__objc_rawisa`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L3620-L3631) section, the runtime disables the non-pointer `isa` feature. Applications that may load plug-ins linked before the deprecation of direct `isa` usage use this section to enable binary compatibility. (This is also macOS-only.)

```
for (EACH_HEADER) {
    if (hi->mhdr()->filetype != MH_EXECUTE) continue;
    unsigned long size;
    if (getsectiondata(hi->mhdr(), "__DATA", "__objc_rawisa", &size)) {
        DisableNonpointerIsa = true;
    }
    break;  // assume only one MH_EXECUTE image
}
```

For all platforms, the Objective-C runtime [disables the non-pointer `isa` feature for the `OS_object` class](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2679-L2684) and its descendants because `libdispatch` also uses the `isa` pointer as a vtable.

```
else if (!hackedDispatch  &&  0 == strcmp(ro->getName(), "OS_object")) {
    // hack for libdispatch et al - isa also acts as vtable pointer
    hackedDispatch = true;
    instancesRequireRawIsa = true;
}
```

### has_assoc, has_cxx_dtor, weakly_referenced, and has_sidetable_rc

The primary purpose of these four fields is to determine if an object can use the fast deallocation path, which simply `free()`s the object’s memory. Otherwise, the runtime must first perform additional bookkeeping before freeing the memory. From [`objc-object.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L562-L583):

```
void objc_object::rootDealloc() {
    if (isTaggedPointer()) return;

    if (isa().nonpointer                     &&
        !isa().weakly_referenced             &&
        !isa().has_assoc                     &&
#if ISA_HAS_CXX_DTOR_BIT
        !isa().has_cxx_dtor                  &&
#else
        !isa().getClass(false)->hasCxxDtor() &&
#endif
        !isa().has_sidetable_rc)
    {
        free(this);
    } else {
        object_dispose((id)this);
    }
}
```

- `has_assoc`: Set if an object has an [associated object](https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj) created through the use of the `objc_setAssociatedObject()` runtime API. If an object has one or more associated objects, the runtime must remove the entries from its side table before freeing the object’s memory.
- `has_cxx_dtor`: Set if the class or a superclass has a `.cxx_destruct` method. If an Objective-C object has one or more instance variables with a C++ type^[[1](#_footnotedef_1)], the runtime calls the class’s `.cxx_construct` instance method to run any non-trivial constructors during object allocation (before any `init` method). After the `dealloc` method chain completes, the runtime calls the class’s `.cxx_destruct` instance method to run any non-trivial destructors before freeing the object’s memory.

    - When Automatic Reference Counting (ARC) is enabled, the compiler implements releasing of a class’s instance variables in its `.cxx_destruct` method, inhibiting the optimization to call `free()` directly. The [`object_dispose()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L8582-L8591:) code path calls [`objc_destructInstance()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L8560-L8574:), which uses the non-pointer `isa` bits, if available, to elide unnecessary clean-up operations.
    - Note this bit isn’t available when pointer authentication is enabled, but the information is available on the class object at the cost of an additional memory load.
- `weakly_referenced`: Set whenever a weak reference^[[2](#_footnotedef_2)] to the object is created. Like associated objects, the runtime must remove the entries from its side table before freeing the object’s memory.
- `has_sidetable_rc`: If the [retain count](https://alwaysprocessing.blog/2023/07/22/objc-retain#the-full-variant) has overflowed [extra_rc](#extra_rc), a side table stores the additional retain counts where, again, the runtime must remove the entries before freeing the object’s memory.

### shiftcls and shiftcls_and_sig

These fields store the class pointer for the packed `isa` variants. Class objects are always 8-byte aligned (either though layout in the binary image or via the standard allocator at runtime), so the least significant 3 bits are always 0. Thus, the “shift class” field stores the class pointer with the [bottom 3 bits shifted away](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L201). This field also relies on knowledge of the [maximum pointer value](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/isa.h#L116) allowed by the virtual memory system, as storing the value in the bit field truncates the value’s high bits.

The runtime signs the class pointer on Apple Silicon with Pointer Authentication (and stores it in the `shiftcls_and_sig` field). In addition to the lower and upper bounds of valid pointer values, this field also relies on knowledge of the bits used by pointer authentication.

### indexcls

The Objective-C runtime on Apple Watch stores class pointers in an array and stores the class’s array index in the `isa`’s `indexcls` field. Indexes are [assigned lazily at runtime](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L7171-L7189), and the runtime falls back to using a pointer `isa` if the array’s capacity (32,767 entries) is exhausted.

The Apple Watch ABI uses 32-bit pointers^[[3](#_footnotedef_3)], which don’t have enough unused bits to store both the pointer value and packed bits. Using an array to store the class pointers reduces the number of bits required for the class identity, enabling the performance advantages of the non-pointer isa at the cost of some indirection.

### magic

This field is unused by the runtime. The runtime exports constants for the magic mask and magic value, which the debugger uses to identify object instances with a non-pointer `isa` to enable Objective-C debugging facilities.

### extra_rc

The retain count of an object instance is stored in a side table when the non-pointer `isa` feature is unavailable for the platform or class hierarchy. However, using a side table can be a performance bottleneck for many concurrent retains or releases, as each operation must acquire a lock. The non-pointer `isa` feature reduces this contention by storing an instance’s retain count in this field.

If the retain count overflows the field, [half of the retain count is moves to a side table](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-object.h#L673-L695), and half remains in this field. Moving only half of the count enables future releases to decrement the field value before acquiring the lock to access the counts in the side table.

The size of this field varies by platform. The following table notes the field’s size and maximum inline retain count value for each platform.

`extra_rc` Bit Count

Max. Value

Packed `isa` on 64-bit Intel

8

255

Packed `isa` on Apple Silicon `arm64`-not-`e` variant

19

524,287

Packed `isa` on Apple Silicon with Pointer Authentication (`arm64e` variant)

8

255

Indexed `isa` (Apple Watch)

7

127

---

[1](#_footnoteref_1). A future post will explore Objective-C++ in more detail.

[2](#_footnoteref_2). A future post will explore weak references in more detail.

[3](#_footnoteref_3). A future post will examine Apple’s `arm64_32` ABI in more detail.
