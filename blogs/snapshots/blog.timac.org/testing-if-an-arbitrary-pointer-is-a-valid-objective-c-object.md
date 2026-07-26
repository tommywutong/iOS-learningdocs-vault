---
title: Testing if an arbitrary pointer is a valid Objective-C object
source_url: 'https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/'
source_domain: blog.timac.org
source_group: single-site
original_language: en
published: 2016-11-24
archived_at: 2026-07-27
content_hash: 'sha256:7e5cb42dfcd2c3cd'
plan_ref: 第一周：对象、类与所有权的地基 / Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06）
plan_week: 第一周：对象、类与所有权的地基
plan_day: Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
---

> 原文：[Testing if an arbitrary pointer is a valid Objective-C object](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/)

Let’s say you pick a random pointer. Can we know if it points to a valid Objective-C object? Of course without crashing… Well there is no simple solution. In this post I give a solution for 64-bit architectures. The code provided has only been tested on macOS 10.12.1 and iOS 10.1.1 with the modern Objective-C runtime.

Want to support this blog? Please check out

![MarkChart](https://blog.timac.org/apps/MarkChart.png) [MarkChart - Mermaid Editor](https://apps.apple.com/app/apple-store/id6475648822?pt=120357958&ct=blog.timac.org&mt=8)

- Easily preview Mermaid diagrams
- Sequence diagrams, flowcharts, …
- Built-in editor
- Export to PDF, PNG, and SVG
- Quick Look integration
- Available on macOS, iOS, and iPadOS
- [Free download on the App Store](https://apps.apple.com/app/apple-store/id6475648822?pt=120357958&ct=blog.timac.org&mt=8)

[![MarkChart](https://blog.timac.org/MarkChart.png)](https://apps.apple.com/app/apple-store/id6475648822?pt=120357958&ct=blog.timac.org&mt=8)

There is not much documentation available on this subject. There is one article written in 2010 by [Matt Gallagher](https://www.cocoawithlove.com/2010/10/testing-if-arbitrary-pointer-is-valid.html) but the content is outdated and not working properly anymore. Most of the information in this post comes from:

- [objc4-706 from macOS 10.12](https://opensource.apple.com/source/objc4/objc4-706/)
- [LLDB git repository (November 2016)](http://lldb.llvm.org/source.html)

# Disclaimer

The content of this post - as well as the source code - relies on internal structures of the Objective-C runtime. There is no guarantee on the correctness and might possibly break with any macOS/iOS update. Don't use this code in real applications!

In fact I started to write this post based on the objc4-680 sources (mac OS 10.11.6). But just before publishing, Apple released the sources for objc4-706 (macOS 10.12). As you can see in the image below, some internal structures I rely on have been changed:

[![Changes between objc4-680 and objc4-706](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/objc4-680_objc4-706_small.png)](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/objc4-680_objc4-706.png)

# What is a pointer?

A pointer is just an integer referencing a location in memory. On iOS and macOS, there are however 2 kinds of pointers: regular pointers and tagged pointers. Let’s start by solving the problem for tagged pointers.

# Tagged Pointers

Tagged pointers were introduced in iOS 7 and Mac OS X 10.7 for 64-bit architectures. A tagged pointer is a special pointer with data stored directly into the pointer instead of doing memory allocations. This has obvious performance advantages.

Tagged pointers are declared in [objc-internal.h](https://opensource.apple.com/source/objc4/objc4-706/runtime/objc-internal.h). In macOS 10.11 and earlier tagged pointers were simple:

- 60 bits for the payload
- 3 bits for the tag index
- 1 bit to identify tagged pointer objects vs. ordinary objects

In macOS 10.12 the tagged pointer layout has been changed to also support 52 bits payload and more tag indexes:

```c
// Tag indexes 0..<7 have a 60-bit payload.
// Tag index 7 is reserved.
// Tag indexes 8..<264 have a 52-bit payload.
// Tag index 264 is reserved.
```

The tag index tells you the class represented by the tagged pointer:

```c
{
    OBJC_TAG_NSAtom            = 0, 
    OBJC_TAG_1                 = 1, 
    OBJC_TAG_NSString          = 2, 
    OBJC_TAG_NSNumber          = 3, 
    OBJC_TAG_NSIndexPath       = 4, 
    OBJC_TAG_NSManagedObjectID = 5, 
    OBJC_TAG_NSDate            = 6, 
    OBJC_TAG_RESERVED_7        = 7, 
 
    OBJC_TAG_First60BitPayload = 0, 
    OBJC_TAG_Last60BitPayload  = 6, 
    OBJC_TAG_First52BitPayload = 8, 
    OBJC_TAG_Last52BitPayload  = 263, 
 
    OBJC_TAG_RESERVED_264      = 264
};
```

Checking if a pointer is a tagged pointer is really simple using the functions declared in objc-internal.h:

```c
static inline bool
_objc_isTaggedPointer(const void *ptr) 
{
    return ((intptr_t)ptr & _OBJC_TAG_MASK) == _OBJC_TAG_MASK;
}
 
static inline objc_tag_index_t 
_objc_getTaggedPointerTag(const void *ptr) 
{
    // assert(_objc_isTaggedPointer(ptr));
    uintptr_t basicTag = ((uintptr_t)ptr >> _OBJC_TAG_INDEX_SHIFT) & _OBJC_TAG_INDEX_MASK;
    uintptr_t extTag =   ((uintptr_t)ptr >> _OBJC_TAG_EXT_INDEX_SHIFT) & _OBJC_TAG_EXT_INDEX_MASK;
    if (basicTag == _OBJC_TAG_INDEX_MASK) {
        return (objc_tag_index_t)(extTag + OBJC_TAG_First52BitPayload);
    } else {
        return (objc_tag_index_t)basicTag;
    }
}
```

Sadly these functions are static inline and not exported and we have no other choice but to copy the implementations in our source code.

On the other hand the function to get the registered class for the given tag is exported and can be used:

```c
/**
 Returns the registered class for the given tag.
 Returns nil if the tag is valid but has no registered class.
 
 This function searches the exported function: _objc_getClassForTag(objc_tag_index_t tag)
 declared in https://opensource.apple.com/source/objc4/objc4-706/runtime/objc-internal.h
 */
static Class _objc_getClassForTag(objc_tag_index_t tag)
{
    static bool _objc_getClassForTag_searched = false;
    static Class (*_objc_getClassForTag_func)(objc_tag_index_t) = NULL;
    if(!_objc_getClassForTag_searched)
    {
        _objc_getClassForTag_func = (Class(*)(objc_tag_index_t))dlsym(RTLD_DEFAULT, "_objc_getClassForTag");
        _objc_getClassForTag_searched = true;
        if(_objc_getClassForTag_func == NULL)
        {
            fprintf(stderr, "*** Could not find _objc_getClassForTag()!\n");
        }
    }
     
    if(_objc_getClassForTag_func != NULL)
    {
        return _objc_getClassForTag_func(tag);
    }
     
    return NULL;
}
```

It is now simple to create a function that checks if a pointer is a tagged pointer and thus a valid Objective-C object:

```c
/**
 Test if a pointer is a tagged pointer
 
 @param inPtr is the pointer to check
 @param outClass returns the registered class for the tagged pointer.
 @return true if the pointer is a tagged pointer.
 */
bool IsObjcTaggedPointer(const void *inPtr, Class *outClass)
{
    bool isTaggedPointer = _objc_isTaggedPointer(inPtr);
    if(outClass != NULL)
    {
        if(isTaggedPointer)
        {
            objc_tag_index_t tagIndex = _objc_getTaggedPointerTag(inPtr);
            *outClass = _objc_getClassForTag(tagIndex);
        }
        else
        {
            *outClass = NULL;
        }
    }
     
    return isTaggedPointer;
}
```

If you want to read more about tagged pointers you can read these 2 articles from Mike Ash:

- [Friday Q&A 2013-09-27: ARM64 and You](https://www.mikeash.com/pyblog/friday-qa-2013-09-27-arm64-and-you.html)
- [Friday Q&A 2012-07-27: Let’s Build Tagged Pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)

Now that we handled tagged pointers, let’s look at ‘regular’ pointers.

# Alignment

Valid pointers have to be aligned to the pointer size. Such a check is done in LLDB when trying to print a pointer in the python function `is_valid_pointer` in [objc_runtime.py](http://llvm.org/svn/llvm-project/lldb/trunk/examples/summaries/cocoa/objc_runtime.py):

```python
@staticmethod
def is_valid_pointer(pointer, pointer_size, allow_tagged=0, allow_NULL=0):
    logger = lldb.formatters.Logger.Logger()
    if pointer is None:
        return 0
    if pointer == 0:
        return allow_NULL
    if allow_tagged and (pointer % 2) == 1:
        return 1
    return ((pointer % pointer_size) == 0)
```

The last check verifies that the pointer is aligned to the pointer size. We can implement the same check:

```python
if (((uintptr_t)inPtr % sizeof(uintptr_t)) != 0)
{
  return false;
}
```

# Bits used

The LLDB source code has another interesting function in [objc_runtime.py](http://llvm.org/svn/llvm-project/lldb/trunk/examples/summaries/cocoa/objc_runtime.py):

```python
# Objective-C runtime has a rule that pointers in a class_t will only have bits 0 thru 46 set
# so if any pointer has bits 47 thru 63 high we know that this is not a
# valid isa
@staticmethod
def is_allowed_pointer(pointer):
    logger = lldb.formatters.Logger.Logger()
    if pointer is None:
        return 0
    return ((pointer & 0xFFFF800000000000) == 0)
```

Again we can easily implement the same check:

```python
if(((uintptr_t)inPtr & 0xFFFF800000000000) != 0)
{
  return false;
}
```

# Valid and readable memory

In order to be valid, a pointer should point to valid and readable memory. We can use `vm_region_64()` to ensure that the memory is readable and `vm_read()` to ensure that the memory is valid:

```c
/**
 Test if the pointer points to readable and valid memory.
 
 @param inPtr is the pointer
 @return true if the pointer points to readable and valid memory.
 */
static bool IsValidReadableMemory(const void *inPtr)
{
    kern_return_t error = KERN_SUCCESS;
     
    // Check for read permissions
    bool hasReadPermissions = false;
     
    vm_size_t vmsize;
    vm_address_t address = (vm_address_t)inPtr;
    vm_region_basic_info_data_t info;
    mach_msg_type_number_t info_count = VM_REGION_BASIC_INFO_COUNT_64;
 
    memory_object_name_t object;
 
    error = vm_region_64(mach_task_self(), &address, &vmsize, VM_REGION_BASIC_INFO, (vm_region_info_t)&info, &info_count, &object);
    if(error != KERN_SUCCESS)
    {
        // vm_region/vm_region_64 returned an error
        hasReadPermissions = false;
    }
    else
    {
        hasReadPermissions = (info.protection & VM_PROT_READ);
    }
     
    if(!hasReadPermissions)
    {
        return false;
    }
     
    // Read the memory
    vm_offset_t readMem = 0;
    mach_msg_type_number_t size = 0;
    error = vm_read(mach_task_self(), (vm_address_t)inPtr, sizeof(uintptr_t), &readMem, &size);
    if(error != KERN_SUCCESS)
    {
        // vm_read returned an error
        return false;
    }
     
    return true;
}
```

# Validating the isa pointer and getting the Class pointer

Now that we know the address points to valid and readable memory, we can extract the possible isa pointer and get the class pointer. This is documented by Greg Parker in [[objc explain]: Non-pointer isa](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html):

> If you are writing a debugger-like tool, the Objective-C runtime exports some variables to help decode isa fields. objc_debug_isa_class_mask describes which bits are the class pointer: (isa & class_mask) == class pointer. objc_debug_isa_magic_mask and objc_debug_isa_magic_value describe some bits that help distinguish valid isa fields from other invalid values: (isa & magic_mask) == magic_value for isa fields that are not raw class pointers. These variables may change in the future so do not use them in application code.

Here is the implementation to validate the isa pointer and extract the Class pointer:

```c
uintptr_t isa = (*(uintptr_t *)inPtr);
Class ptrClass = NULL;
 
if ((isa & ~ISA_MASK) == 0)
{
    ptrClass = (Class)isa;
}
else
{
    if ((isa & ISA_MAGIC_MASK) == ISA_MAGIC_VALUE)
    {
        ptrClass = (Class)(isa & ISA_MASK);
    }
    else
    {
        ptrClass = (Class)isa;
    }
}
 
if(ptrClass == NULL)
{
    return false;
}
```

# Verifying if the class exists

Now that we have the class, we can check if the Objective-C runtime knows it:

```c
bool isKnownClass = false;
 
unsigned int numClasses = 0;
Class *classesList = objc_copyClassList(&numClasses);
for (int i = 0; i < numClasses; i++)
{
    if (classesList[i] == ptrClass)
    {
        isKnownClass = true;
        break;
    }
}
free(classesList);
 
if(!isKnownClass)
{
    return false;
}
```

# Filtering out some false positives

A [good trick](https://twitter.com/gparker/status/801894068502433792) from Greg Parker consists of filtering out some false positives by checking if the pointer malloc’ed size is greater than the class instance size:

```c
size_t pointerSize = malloc_size(inPtr);
if(pointerSize > 0 && pointerSize < class_getInstanceSize(ptrClass))
{
    return false;
}
```

# Summing it up

We now have all the elements to build a function that returns a boolean indicating if a pointer is an Objective-C object:

```c
/**
 Test if a pointer is an Objective-C object
 
 @param inPtr is the pointer to check
 @return true if the pointer is an Objective-C object
 */
bool IsObjcObject(const void *inPtr)
{
    //
    // NULL pointer is not an Objective-C object
    //
    if(inPtr == NULL)
    {
        return false;
    }
     
    //
    // Check for tagged pointers
    //
    if(IsObjcTaggedPointer(inPtr, NULL))
    {
        return true;
    }
     
    //
    // Check if the pointer is aligned
    //
    if (((uintptr_t)inPtr % sizeof(uintptr_t)) != 0)
    {
        return false;
    }
     
    //
    // From LLDB:
    // Objective-C runtime has a rule that pointers in a class_t will only have bits 0 thru 46 set
    // so if any pointer has bits 47 thru 63 high we know that this is not a valid isa
    // See http://llvm.org/svn/llvm-project/lldb/trunk/examples/summaries/cocoa/objc_runtime.py
    //
    if(((uintptr_t)inPtr & 0xFFFF800000000000) != 0)
    {
        return false;
    }
     
    //
    // Check if the memory is valid and readable
    //
    if(!IsValidReadableMemory(inPtr))
    {
        return false;
    }
     
    //
    // Get the Class from the pointer
    // From http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html :
    // If you are writing a debugger-like tool, the Objective-C runtime exports some variables
    // to help decode isa fields. objc_debug_isa_class_mask describes which bits are the class pointer:
    // (isa & class_mask) == class pointer.
    // objc_debug_isa_magic_mask and objc_debug_isa_magic_value describe some bits that help
    // distinguish valid isa fields from other invalid values:
    // (isa & magic_mask) == magic_value for isa fields that are not raw class pointers.
    // These variables may change in the future so do not use them in application code.
    //
     
    uintptr_t isa = (*(uintptr_t *)inPtr);
    Class ptrClass = NULL;
     
    if ((isa & ~ISA_MASK) == 0)
    {
        ptrClass = (Class)isa;
    }
    else
    {
        if ((isa & ISA_MAGIC_MASK) == ISA_MAGIC_VALUE)
        {
            ptrClass = (Class)(isa & ISA_MASK);
        }
        else
        {
            ptrClass = (Class)isa;
        }
    }
     
    if(ptrClass == NULL)
    {
        return false;
    }
     
    //
    // Verifies that the found Class is a known class.
    //
    bool isKnownClass = false;
     
    unsigned int numClasses = 0;
    Class *classesList = objc_copyClassList(&numClasses);
    for (int i = 0; i < numClasses; i++)
    {
        if (classesList[i] == ptrClass)
        {
            isKnownClass = true;
            break;
        }
    }
    free(classesList);
     
    if(!isKnownClass)
    {
        return false;
    }
     
     
    //
    // From Greg Parker
    // https://twitter.com/gparker/status/801894068502433792
    // You can filter out some false positives by checking malloc_size(obj) >= class_getInstanceSize(cls).
    //
    size_t pointerSize = malloc_size(inPtr);
    if(pointerSize > 0 && pointerSize < class_getInstanceSize(ptrClass))
    {
        return false;
    }
     
    return true;
}
```

# Testing

To test this function, I built a simple iOS application that checks various pointers. Here is the output when running on iOS 10.1.1 (64-bit):

![Tests](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/tests.png)

# Downloads

- [IsObjcObject.c](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/IsObjcObject.c)
- [Sources of the test app](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/IsObjcObject.zip)

# References

- [objc4-706](https://opensource.apple.com/source/objc4/objc4-706/) from macOS 10.12
- [LLDB git repository](http://lldb.llvm.org/source.html) (November 2016)
- [Testing if an arbitrary pointer is a valid object pointer](https://www.cocoawithlove.com/2010/10/testing-if-arbitrary-pointer-is-valid.html) from Matt Gallagher
- [Friday Q&A 2013-09-27: ARM64 and You](https://www.mikeash.com/pyblog/friday-qa-2013-09-27-arm64-and-you.html) from Mike Ash
- [Friday Q&A 2012-07-27: Let’s Build Tagged Pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html) from Mike Ash
- [[objc explain]: Non-pointer isa](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html) from Greg Parker

# Updates

**24.11.2016**: 2 changes based on feedback from Greg Parker:

- Filtering out some false positives
- Use `objc_copyClassList()` instead of `objc_getClassList()`
