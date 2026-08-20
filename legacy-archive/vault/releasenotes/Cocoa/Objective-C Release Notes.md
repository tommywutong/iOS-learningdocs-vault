---
title: Objective-C Release Notes
apple_id: TP40004309
resource_type: Release Note
platform: macOS
topic: Languages & Utilities
technology: Foundation
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Cocoa/RN-ObjectiveC/index.html
archived_at: '2026-07-18T02:50:22.825763Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Objective-C Runtime Release Notes for OS X v10.5

This document describes some of the changes in the Objective-C runtime in OS X v10.5.

#### Contents:

- [Garbage Collection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Loading and Unloading Bundles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [Method and Class Attributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)
- [@package Instance Variables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ny)
- [Runtime API changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oa)
- [64-bit ABI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oi)
- [64-bit Class and Instance Variable Access Control](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnknltc)
- [64-bit Non-Fragile Instance Variables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjq)
- [64-bit Zero-Cost C++-Compatible Exceptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjr)

### Garbage Collection

The Objective-C runtime examines on startup the execution image to determine whether to run with garbage collection or not. Each object file has an info section and they must all agree for execution to proceed. Standard compilation results in an info section that indicates that no GC capability is present. Compiling with `-fobjc-gc` indicates that both GC and retain/release logic is present. Compiling with `-fobjc-gc-only` indicates that only GC logic is present. A non-GC executable that attempts to load a gc-only framework will fail, as will a GC capable executable that attemps to load a GC incapable framework (or bundle).

The compiler uses three "helper" functions for assignments of strong pointers to garbage collected memory into global memory (`objc_assign_global`), garbage collected heap memory (`objc_assign_ivar`), or into unknown memory (`objc_assign_strongCast`). For assignments of weak pointers it uses `objc_assign_weak` and for reads it uses `objc_read_weak`.

When copying memory in bulk into a garbage collected block you must use the API `objc_memmove_collectable(void *dst, const void *src, size_t size)`.

### Threads

The collector initially runs only on the main thread when requested via `objc_collect_if_needed`(1), which is called automatically from the `NSAutoreleasePool` [drain](https://developer.apple.com/documentation/foundation/nsautoreleasepool/1520553-drain) method. The AppKit arranges to call `objc_start_collector_thread()` after launch and subsequently collections run on a dedicated thread and are responsive to pure allocation demand. The `objc_set_collection_threshold` and `objc_set_collection_ratio` calls are used to establish the "need" for a collection. Once every ratio times a full (complete) collection will occur; otherwise a generational collection will be done if allocations have exceeded the threshold.

The garbage collector minimally pauses those threads which have been registered to it while collecting. Registration occurs during establishment of an `NSThread` object, not simply a `pthread`.

### Garbage Collection Errors

The collector itself is found in /usr/lib/libauto.dylib. Its error messages are printed using `malloc_printf`. The ObjC runtime is found in /usr/lib/libobjc.dylib. Its errors are printed using `_objc_inform`. Currently, resurrection and reference count underflow errors are noted by calling the following routines:

```
objc_assign_global_error
objc_assign_ivar_error
objc_exception_during_finalize_error
auto_zone_resurrection_error
auto_refcount_underflow_error
```


### Properties

The syntax for Objective-C properties has been overhauled since WWDC 2006. See the property documentation ([Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html#//apple_ref/doc/uid/TP30001163-CH17)) for details.

In summary, `@property(attributes) type name` introduces an implicit declaration of a "getter" and a "setter" method (unless a read-only property is requested) for the "variable" named. The `setter=` and `getter=` attributes allow one to specify the names of the methods, otherwise a "name" method and a "setName:" method are implicitly declared. They may also be explicitly named.

By default, properties are assigned when set. For objects under non-GC this is often incorrect and a warning is issued unless the assignment semantic is explicitly named. There are three choices: `assign`, for non-retained object references; `copy`, for objects that are copied and implicitly retained; and `retain`, for objects that require being retained when set.

Access to properties is atomic by default. This is trivial under GC for almost everything and also trivial under non-GC for everything but objects and structures. In particular atomic access to retained objects under non-GC conditions can be expensive. As such, a `nonatomic` property attribute is available.

Pointers may be held strongly under GC by declaring them `__strong`, and they can be zeroing weak by declaring them `__weak`.

The implementations for properties can be provided by the compiler and runtime through the use of the `@synthesize` statement in the `@implementation` section of the class (or class extension). The compiler expects an instance variable of the same name as the property. If you want to use a different name, you supply it to the `@synthesize` statement.

In particular the compiler and runtime will implement accessors to retained objects by using atomic compare and swap instructions. It is extremely dangerous to directly access an atomic object property through its instance variable since another thread might change its value unpredictably. As such the compiler will warn you about such unprotected accesses. The runtime, in fact, will temporarily use the least significant bit of the instance variable as a temporary lock while retaining the new value and releasing the old. Direct use of an atomic instance variable under non-GC is strongly discouraged.

### Loading and Unloading Bundles

Since OS X v10.4 it has been possible to unload bundles containing Objective-C. No attempt is made to prevent this if objects are still present for classes that are unloaded. Subclasses of classes loaded in bundles are particularly vulnerable.

### Method and Class Attributes

Objective-C now supports some gcc attributes for Objective-C methods. Syntactically, attributes for a method follow the method's declaration, and attributes for a method parameter sit between the parameter type and the parameter name. Supported attributes include:

- Deprecation and availability, including AvailabilityMacros.h

```objc
   - (void)method:(id)param  __attribute__((deprecated));
```
- Unused parameters

```objc
    - (void)method:(id) __attribute__((unused)) param;
```
- Sentinel parameters, including `NS_REQUIRES_NIL_TERMINATION`

```objc
    - (void)methodWithObjects:(id)obj, ...  NS_REQUIRES_NIL_TERMINATION;
```

Objective-C also supports some gcc attributes for Objective-C classes. Syntactically, attributes for a class precede the class's `@interface` declaration. Supported attributes include:

- Deprecation and availability, including AvailabilityMacros.h

```objc
    __attribute__((deprecated))
    @interface MyDeprecatedClass : SomeSuperclass
```
- Visibility

```objc
    __attribute__((visibility("hidden")))
    @interface MyPrivateClass : SomeSuperclass
```


### @package Instance Variables

`@package` is a new instance variable protection class, like `@public` and `@protected`. `@package` instance variables behave as follows:

- `@public` in 32-bit;
- `@public` in 64-bit, inside the framework that defined the class;
- `@private` in 64-bit, outside the framework that defined the class.

In 64-bit, the instance variable symbol for an `@package` ivar is not exported, so any attempt to use the ivar from outside the framework that defined the class will fail with a link error. See "[64-bit Class and Instance Variable Access Control](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgmbzfvbuqmjnknltc)" for more about instance variable symbols.

### Runtime API changes

The C interface to the Objective-C runtime (in `<objc/*.h>`) has changed significantly. Highlights include:

- Almost all structures are deprecated, including `struct objc_class`. Functional replacements for most of these are provided.
- `class_poseAs` is deprecated. Use method list manipulation functions instead.
- `class_nextMethodList` is deprecated. Use [class_copyMethodList](https://developer.apple.com/documentation/objectivec/1418490-class_copymethodlist) instead.
- `class_addMethods` is deprecated. Use [class_addMethod](https://developer.apple.com/documentation/objectivec/1418901-class_addmethod) instead.
- `objc_addClass` is deprecated. Use [objc_allocateClassPair](https://developer.apple.com/documentation/objectivec/1418559-objc_allocateclasspair) and [objc_registerClassPair](https://developer.apple.com/documentation/objectivec/1418603-objc_registerclasspair) instead.
- In general, all deprecated declarations are absent in 64-bit.
- The API in `objc/objc-runtime.h` and `objc/objc-class.h` is now in `objc/runtime.h` and `objc/message.h`. The old header files simply `#include` the new ones.

### 64-bit ABI

The 64-bit Objective-C ABI is generally unlike the 32-bit ABI. The new ABI provides new features, better performance, and improved future adaptability. All aspects of the 64-bit ABI are private and subject to future change. Forthcoming documentation will describe the ABI for the use of compilers and developer tools only.

### 64-bit Class and Instance Variable Access Control

In 64-bit Objective-C, access control for classes and each class and instance variable has a symbol associated with it. All uses of a class or instance variable reference this symbol. These symbols are subject to access control by the linker.

The upshot is that access to private classes and ivars is more strictly enforced. Illegal use of a private ivar may fail with a link error. Frameworks that provide classes and ivars must correctly export their symbols. In particular, frameworks built with `-fvisibility=hidden` or a linker export list may need to be changed.

Class symbols have names of the form `_OBJC_CLASS_$_ClassName` and `_OBJC_METACLASS_$_ClassName` . The class symbol is used by clients who send messages to the class (i.e. `[ClassName someMessage]`). The metaclass symbol is used by clients who subclass the class.

By default, class symbols are exported. They are affected by gcc's symbol visibility flags, so `-fvisibility=hidden` will make the class symbols non-exported. The linker recognizes the old symbol name `.objc_class_name_ClassName` in linker export lists and translates it to these symbols.

Visibility of a single class can be changed using an attribute.

```objc
__attribute__((visibility("hidden")))
@interface ClassName : SomeSuperclass
```

For classes with "`default`" visibility, the class symbols are exported, and the ivar symbols are handled as described below. For classes with "hidden" visibility, the class symbols and ivar symbols are all not exported.

Ivar symbols have the form `_OBJC_IVAR_$_ClassName.IvarName` . The ivar symbol is used by clients who read or write the ivar.

By default, ivar symbols for `@private` and `@package` ivars are not exported, and ivar symbols for `@public` and `@protected` ivars are exported. This can be changed by export lists, `-fvisibility`, or a visibility attribute on the class. Visibility attributes on individual ivars are currently not supported.

### 64-bit Non-Fragile Instance Variables

All instance variables in 64-bit Objective-C are non-fragile. That is, existing compiled code that uses a class's ivars will not break when the class or a superclass changes its own ivar layout. In particular, framework classes may add new ivars without breaking subclasses compiled against a previous version of the framework.

Ivars may be added or reordered freely; existing users of a reordered ivar will adapt transparently. Other ivar changes are safe except that they will break any existing users of the ivar: deleting an ivar, renaming an ivar, moving an ivar to a different class, and changing the type of an ivar.

Do not use `@defs`. The ivar layout it presents cannot adapt to superclass changes.

Do not use `sizeof(SomeClass)`. Use `class_getInstanceSize([SomeClass class])` instead.

Do not use `offsetof(SomeClass, SomeIvar)`. Use `ivar_getOffset(class_getInstanceVariable([SomeClass class], "SomeIvar"))` instead.

### 64-bit Zero-Cost C++-Compatible Exceptions

In 64-bit, the implementation of Objective-C exceptions has been rewritten. The new system provides "zero-cost" try blocks and interoperability with C++.

"Zero-cost" try blocks incur no time penalty when entering an @try block, unlike 32-bit which must call `setjmp()` and other additional bookkeeping. On the other hand, actually throwing an exception is much more expensive. For best performance in 64-bit, exceptions should be thrown only in exceptional cases.

The Cocoa frameworks require that all exceptions be instances of `NSException` or its subclasses. Do not throw objects of other types.

The Cocoa frameworks are generally not exception-safe. Their general pattern is that exceptions are reserved for programmer error only, and the program should quit soon after catching such an exception. Be careful when throwing exceptions across the Cocoa frameworks.

In 64-bit, C++ exceptions and Objective-C exceptions are interoperable. In particular, C++ destructors and Objective-C `@finally` blocks are honored when unwinding any exception, and default catch clauses—`catch (...)` and `@catch (...)`—are able to catch and re-throw any exception.

Objective-C `@catch (id e)` catches any Objective-C exception, but no C++ exceptions. Use `@catch (...)` to catch everything, and `@throw;` to re-throw caught exceptions. `@catch (...)` is allowed in 32-bit, and has the same effect there as `@catch (id e)`.
