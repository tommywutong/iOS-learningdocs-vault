---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/NamingConventions.html
archived_at: '2026-07-15T07:22:23.170627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Foundation Design Concepts](Introduction%20to%20Core%20Foundation%20Design%20Concepts.md)


[Next](Other%20Types.md)[Previous](Varieties%20of%20Objects.md)

# Naming Conventions

A major programming-interface convention in Core Foundation is to use the name of the opaque type that is most closely related to a symbol as the symbol’s prefix. For functions, this prefix identifies not only the type to which the function “belongs” but usually the type of object that is the target of the function’s action. (An exception to this convention are constants, which put “k” before the type prefix.) Here are a few examples from the header files:

```
/* from CFDictionary.h */
CF_EXPORT CFIndex CFDictionaryGetCountOfKey(CFDictionaryRef dict, const void *key);
/* from CFString.h */
typedef UInt32 CFStringEncoding;
/* from CFCharacterSet.h */
typedef enum {
    kCFCharacterSetControl = 1,
    kCFCharacterSetWhitespace,
    kCFCharacterSetWhitespaceAndNewline,
    kCFCharacterSetDecimalDigit,
    kCFCharacterSetLetter,
    kCFCharacterSetLowercaseLetter,
    kCFCharacterSetUppercaseLetter,
    kCFCharacterSetNonBase,
    kCFCharacterSetDecomposable,
    kCFCharacterSetAlphaNumeric,
    kCFCharacterSetPunctuation,
    kCFCharacterSetIllegal
} CFCharacterSetPredefinedSet;
```

Core Foundation has a few programming-interface conventions in addition to those related to opaque types and memory management.

- There is an important distinction between Get, and Copy and Create, in names of functions that return values. If you use a Get function, you cannot be certain of the returned object’s life span. To ensure the persistence of such an object you can retain it (using the CFRetain function) or, in some cases, copy it. If you use a Copy or Create function, you are responsible for releasing the object (using the CFRelease function). For more details, see _[Memory Management Programming Guide for Core Foundation](../Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i)_.
- Some Core Foundation objects have their own naming conventions to impose consistency among common operations. For example, collections embed the following verbs in function names to mean specific operations on the elements of a collection:

  - “Add” means “add if absent, do nothing if present” (if a uniquing collection).
  - “Replace” means “replace if present, do nothing if absent.”
  - “Set” means “add if absent, replace if present.”
  - “Remove” means “remove if present, do nothing if absent.”
- The `CFIndex` type is used for index, count, length, and size parameters and return values. The integer value this type represents (currently 32 bits) can grow over time as the processor’s address size grows. On architectures where pointer sizes are different, say 64 bits, `CFIndex` might be declared to be 64 bits, independent of the size of `int`. By using `CFIndex` for variables that interact with Core Foundation arguments of the same type, you ensure a higher degree of source compatibility for your code.
- Some Core Foundation header files may seem to define opaque types but actually contain convenience functions not associated with a specific type. A case in point is `CFPropertyList.h`. CFPropertyList is a placeholder type for any of the property-list types: CFString, CFData, CFBoolean, CFNumber, CFDate, CFArray, and CFDictionary.
- Unless otherwise specified, all by-reference parameters intended for the return of values can accept `NULL`. This indicates that the caller is not interested in that return value.

[Next](Other%20Types.md)[Previous](Varieties%20of%20Objects.md)

