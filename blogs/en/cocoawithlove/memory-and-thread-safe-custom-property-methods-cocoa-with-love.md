---
title: 'Memory and thread-safe custom property methods | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/memory-and-thread-safe-custom-property.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:aa9079f6824c40ea'
translated: false
---

> 原文：[Memory and thread-safe custom property methods | Cocoa with Love](https://www.cocoawithlove.com/2009/10/memory-and-thread-safe-custom-property.html)　·　Cocoa with Love (Matt Gallagher)

Objective-2.0 property methods are a nice convenience but if you need to override a property implementation — particularly an atomic, retained or copied object setter property — there are some potential bugs you can create if you don't follow the rules carefully. I'll show you the pitfalls and the correct way to implement a property accessor. I'll also show a way to directly invoke hidden runtime functions to let Objective-C perform atomic getting and setting safely for you.

## Custom getter and setter methods for implicitly atomic types

For implicitly atomic types or for types where memory management doesn't apply, custom getter and setter methods in Objective-C are easy. These "easy" situations include:

- Basic value types (`char`, `short`, `int`, `float`, `long`, `double`, etc).
- Objective-C objects in a garbage collected environment
- Assigned (non-retained) pointers

For these types, it is pretty hard to get a custom getter or setter method wrong. For the following property declaration:

```objc
@property SomeAtomicType somePropertyVariable;
```

the custom getter and setter simply look like this:

```objc
- (SomeAtomicType)somePropertyVariable
{
    return somePropertyVariable;
}
- (void)setSomePropertyVariable:(SomeAtomicType)aValue
{
    somePropertyVariable = aValue;
}
```

## Common mistakes in accessor methods for non-atomic types

Non-atomic types require greater care. These types include:

- Objective-C objects in a manually managed memory environment
- `struct`s and other compound types

Given how simple custom getter and setter methods are for atomic types, it is easy to be complacent about implementing methods for these types. However, following the wrong approach can lead to memory crash bugs and lack of proper thread safety.

To illustrate how simple it can be to introduce bugs while implementing a custom setter method, consider the following declared property:

```objc
@property NSString (copy) someString;
```

A hasty implementation of the setter might be:

```objc
- (void)setSomeString:(NSString *)aString
{
    [someString release];
    someString = [aString copy];
}
```

This implementation actually contains two bugs:

1. **This method is not atomic.**  
  The `someString` object changes twice: once on `release` and again when it is assigned the copied object's address. This method is _not_ atomic and therefore violates the declaration (which omits the `nonatomic` keyword and therefore requires atomicity).
2. **The assignment contains a potential memory deallocation bug.**  
  If `someString` is ever assigned its own value, it will `release` it before `copy`ing it, causing potential use of a `release`d variable. The code: `self.someString = someString;` is an example of this potential issue.

Don't feel too bad if you've ever made these mistakes. I spent some time looking at [clang's](http://clang.llvm.org/) synthesized method implementations when I was researching this post and I noticed that [they've forgotten to handle struct accessor methods in an atomic manner](http://llvm.org/svn/llvm-project/cfe/trunk/lib/CodeGen/CGObjC.cpp) when required.

## Safe implementations of custom accessor methods for non-atomic types

To address this second issue, [Apple's Declared Properties documentation](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/ObjectiveC/Articles/ocProperties.html) suggests that your setter methods should look like this:

```objc
- (void)setSomeString:(NSString *)aString
{
    if (someString != aString)
    {
        [someString release];
        someString = [aString copy];
    }
}
```

This only fixes the memory issue, it doesn't fix the atomicity issue. To handle that, the only simple solution is to used a `@synchronized` section:

```objc
- (void)setSomeString:(NSString *)aString
{
    @synchronized(self)
    {
        if (someString != aString)
        {
            [someString release];
            someString = [aString copy];
        }
    }
}
```

This approach will also work for `retain` properties as well (simply replace the `copy` method with a `retain`.

To maintain atomicity, you also need a `retain/autorelease` pattern and lock on any getter methods too:

```objc
- (NSString *)someString
{
    @synchronized(self)
    {
        id result = [someString retain];
    }
    return [result autorelease];
}
```

The `@synchronized` section is only required around the `retain` since that will prevent a setter releasing the value before we can return it (the `autorelease` is then safely done outside the section).

For `struct` and other compound data types, we don't need to `retain` or `copy`, so only the `@synchronized` section is required:

```objc
- (NSRect)someRect
{
    @synchronized(self)
    {
        return someRect;
    }
}
- (void)setSomeRect:(NSRect)aRect
{
    @synchronized(self)
    {
        someRect = aRect;
    }
}
```

## A faster, shorter way to implement custom accessors

There are two negative points to the custom accessor methods listed above:

- They need to be coded exactly to avoid bugs.
- The `@synchronized` section on `self` is coarse-grained and slow.

There is another way to implement these methods that doesn't require as much careful coding and uses much more efficient locking: use the same functions that the `synthesized` methods use.

The following functions are implemented in the Objective-C runtime:

```objc
id objc_getProperty(id self, SEL _cmd, ptrdiff_t offset, BOOL atomic);
void objc_setProperty(id self, SEL _cmd, ptrdiff_t offset, id newValue, BOOL atomic,
    BOOL shouldCopy);
void objc_copyStruct(void *dest, const void *src, ptrdiff_t size, BOOL atomic,
    BOOL hasStrong);
```

While these functions are implemented in the runtime, they are not declared, so if you want to use them, you must declare them yourself (the compiler will then find their definitions when you compile).

These methods are much faster than using a `@synchronized` section on the whole object because (as shown in their [Apple opensource implementation](http://www.opensource.apple.com/source/objc4/objc4-371.2/runtime/Accessors.subproj/objc-accessors.m)) they use a finely grained, instance variable only spin lock for concurrent access (although the copy struct function uses two locks following an interface design mixup).

When you declare these functions, you can also declare the following convenience macros:

```objc
#define AtomicRetainedSetToFrom(dest, source) \
    objc_setProperty(self, _cmd, (ptrdiff_t)(&dest) - (ptrdiff_t)(self), source, YES, NO)
#define AtomicCopiedSetToFrom(dest, source) \
    objc_setProperty(self, _cmd, (ptrdiff_t)(&dest) - (ptrdiff_t)(self), source, YES, YES)
#define AtomicAutoreleasedGet(source) \
    objc_getProperty(self, _cmd, (ptrdiff_t)(&source) - (ptrdiff_t)(self), YES)
#define AtomicStructToFrom(dest, source) \
    objc_copyStruct(&dest, &source, sizeof(__typeof__(source)), YES, NO)
```

I like to include the "To/From" words so I can remember the ordering of the source and destination parameters. You can remove them if they bother you.

With these macros, the `someString` "copy" getter and setter methods above would become:

```objc
- (NSString *)someString
{
    return AtomicAutoreleasedGet(someString);
}
- (void)setSomeString:(NSString *)aString
{
    AtomicCopiedSetToFrom(someString, aString);
}
```

and the someRect accessor methods shown above would become:

```objc
- (NSRect)someRect
{
    NSRect result;
    AtomicStructToFrom(result, someRect);
    return result;
}
- (void)setSomeRect:(NSRect)aRect
{
    AtomicStructToFrom(someRect, aRect);
}
```

## Conclusion

Most of the accessor methods I've shown here are atomic but in reality, most Objective-C object accessors are declared `nonatomic`.

Even if your properties are declared `nonatomic`, the memory management rules still apply. These rules are important to follow since they can lead to some very obscure and hard to track down memory bugs.

The macros I've provided are all for atomic properties. For non-atomic properties the boilerplate assignment code is probably simple enough to remember. If not, you could also use a macro:

```objc
#define NonatomicRetainedSetToFrom(a, b) do{if(a!=b){[a release];a=[b retain];}}while(0)
#define NonatomicCopySetToFrom(a, b) do{if(a!=b){[a release];a=[b copy];}}while(0)
```

**Update:** following comments below, I realize I omitted to qualify the situations in which these accessors are thread-safe. Specifically:

1. These setter methods are only thread-safe if the parameters passed to them are immutable. For mutable parameters, you may need to ensure thread safety between mutations on the parameter and the assignment of the property.
2. Atomic accessors only provide thread safety to an instance variable if they are the sole way you access the instance variable. If non-property access is required, you must ensure shared thread safety between property accessor methods and the non-property access.
3. Atomic assignment for the "implicitly atomic" types I listed does not mean that all CPUs/cores see the same thing (since each CPU/core could have its own cache of the value) — it only ensures that value is wholly set without possibility of interruption. If you require all CPUs/core to be synchronized and see the same value at a given moment, then even the "implicitly atomic" types may require `volatile` qualifiers or a `@synchronized` section around the assignment to flush caches.
