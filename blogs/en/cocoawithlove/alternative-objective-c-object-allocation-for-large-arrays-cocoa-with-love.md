---
title: 'Alternative Objective-C object allocation for large arrays | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/08/alternative-objective-c-object.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:685f9a1d65ba0785'
translated: false
---

> 原文：[Alternative Objective-C object allocation for large arrays | Cocoa with Love](https://www.cocoawithlove.com/2010/08/alternative-objective-c-object.html)　·　Cocoa with Love (Matt Gallagher)

In this post, I'll show you how you can create objects without using the standard instance allocation process (either `+[NSObject alloc]` or `class_createInstance()`). I'll also explain why you might do this — the benefits and drawbacks to a custom object creation process.

## Introduction to object allocation

The first point to understand when looking at Objective-C object allocation is what is an Objective-C object?

The answer is pretty simple: any block of data that starts with an Objective-C `Class` pointer can be treated as an Objective-C object. This pointer is normally called the `isa` pointer and allows the block of memory to be used in the Objective-C message sending system.

Normally, Objective-C objects are individually allocated on the malloc heap using `malloc_zone_calloc` from within the `+[NSObject alloc]` or `class_createInstance()` implementation. These allocation approaches automatically set the `isa` pointer for the object once it is allocated.

## Alternative object allocation

Since any block of memory that starts with an `isa` pointer can be treated as an object, then there are numerous ways you could actually allocate objects. I'm going to consider just one alternative approach: malloc'ing a single large block of data, treating this single block as a C array of Objective-C objects and manually setting the `isa` pointer at the start of each of these objects.

The approach is fairly simple. Step one, allocate the C array (using `calloc` to obey Objective-C conventions):

```objc
const NSInteger arrayLength = /* some array length */;
Class someClass = [SomeClass class];
NSInteger runtimeInstanceSize = class_getInstanceSize(someClass);
char *instanceArray = calloc(
    runtimeInstanceSize,
    arrayLength);
```

Notice that we use the runtime size of the instance, not a compile-time value. This is because the instance size may change if a superclass adds extra instance variables at runtime (see [my previous post on Dynamic Ivars](https://www.cocoawithlove.com/2010/03/dynamic-ivars-solving-fragile-base.html)). If your class doesn't have a superclass or you're otherwise cavalier enough to ignore this possibility, then you could use a fixed or compile-time size value.

Once the block is allocated, we need to set all the isa pointers:

```objc
for (NSInteger instanceIndex = 0; instanceIndex < arrayLength; instanceIndex++)
{
    Class *currentInstanceIsa =
        (Class *)(instanceArray + (runtimeInstanceSize * instanceIndex));
    *currentInstanceIsa = someClass;
}
```

Then if desired, you can invoke the `init` method or otherwise initialize each object some other way.

## Reasons for using alternative allocation approaches

The reason to avoid standard allocation is generally because `malloc_zone_calloc` does not offer the memory efficiency or performance required.

I've previously examined [how malloc works on the Mac](https://www.cocoawithlove.com/2010/05/look-at-how-malloc-works-on-mac.html). This post briefly looked at two of the limitations with malloc:

- malloc allocations have an "allocation resolution" (objects not a multiple of the resolution will result in wasted space)
- malloc must maintain metadata on allocated objects and this imposes an additional memory overhead

The biggest malloc limitation however is simply the fact that it imposes a per-object CPU overhead on allocations.

Finally, there is one other advantage associated with using alternative allocation approaches: it is lower level. This is not an advantage in all situations — low level implementations can be fussy and prone to errors. But low-level C implementations can be easier to join with other low-level C implementations, so if much of your program is already a low-level C implementation, it may end up being an advantage to have low-level access to your object's allocation.

## Drawbacks to alternative object allocation

Alternative object allocation should not be used lightly. First of all: it is simply more work as a programmer, so you need to be sure it's work the effort.

But the biggest problem it creates is the fact that individual objects cannot be retained beyond lifetime of the larger block in which they're allocated. To address this, you must either

- Give the containing block a global lifetime (never released) like a singleton or other permanent instance
- Carefully manage all retains and releases to ensure that no object is retained beyond the containing block's lifetime
- Make retains illegal (use a retain implementation that throws an exception).

This limitation can be justified but only if the efficiency benefits are significant. On the iPhone, you may be able to justify it for a few 10s of thousands but on the Mac, your block should contain hundreds of thousands before you'd bother.

## An example: loading the "/usr/share/dict/words" file

To illustrate how you can use alternative allocation, I'm going to show a traditional Objective-C approach for reading, parsing and storing the contents of the "/usr/share/dict/words" file as an array of `NSString`s. I will compare the time taken and memory used by this approach with an approach that uses the alternate allocation approach.

The traditional Objective-C approach:

```objc
words = [[NSString
        stringWithContentsOfFile:@"/usr/share/dict/words"
        encoding:NSASCIIStringEncoding
        error:NULL]
    arrayBySeparatingIntoParagraphs];
```

where `arrayBySeparatingIntoParagraphs` is an `NSString` category method that uses `getParagraphStart:end:contentsEnd:forRange:` to divide the `NSString` into lines.

The alternative approach uses a custom `NSString` class, allocated as described in the "Alternative object allocation" section above. This `NSString` stores a fixed length 24 character ASCII character string (24 characters is the maximum length of a line in the words file). The string storage is not actually a C string; if the stored string is 24 characters long, it isn't null terminated.

```objc
@interface CustomAsciiString : NSString
{
    char value[CUSTOM_ASCII_STRING_LENGTH];
}
@end
```

The allocation itself happens in the init method of a custom NSArray subclass.

```objc
@interface CustomAsciiStringArray : NSArray
{
    NSInteger count;
    char *stringArray;
}
@end
```

This custom array subclass is used to provide `NSArray`-compatible access to the C array of `CustomAsciiString`.

The array of `CustomAsciiString` is actually referenced here as a `char*` because at compile time we don't presume to know the allocated size of the `CustomAsciiString` so we'll need to offset into the array by bytes (i.e. `char`s).

The code for all of this is too big to include here but you can download the [CustomObjectCreation.zip](https://www.cocoawithlove.com/assets/objc-era/CustomObjectCreation.zip) for the complete code.

## Results

There are 234936 words in the dictionary with a maximum length of 24 characters and an average length of 9.6 characters.

The "traditional" Objective-C approach took 3.12 seconds to load, parse and store the file in the string array 20 times. Memory usage after the final iteration (all other iterations were released) was 16.5 MB.

The "alternative allocation" approach took 0.49 seconds to load, parse and store the file in the string array 20 times. Memory usage after the final iteration was 8MB.

Final result: 6 times faster using half the memory.

## Potential issues with the methodology behind these numbers

Based on these numbers, the "alternative allocation" would appear to be more than 6 times faster and more than twice as memory efficient.

This isn't an "apples to apples" comparison though.

The "alternative allocation" approach is storing ASCII strings (which are half the size, character-for-character compared to typical `unichar` `NSString`s). However, this is largely compensated by the fact that every one of the ASCII strings is 24 characters long — significantly more than twice the average length of the strings, so the useful memory allocated here is actually greater. Even if you double the ASCII string length to 48 characters, the memory usage is only 13.4MB — still 20% less than the traditional allocation approach. The "alternative allocation" approach is also allocating a fixed 250000 entry array (even though only 234936 are used).

The parsing used by each approach is radically different. However, this is related to my earlier statement that lower-level allocation lends itself to integration with lower-level parsing and handling. I have not attempted to make the parsing more comparable between the two approaches because I believe the different parsing approaches are correctly matched to the different allocation approaches.

The biggest problem that I would have liked to address better — but I don't really know how I would — is that simply reading memory usage from `getrusage` is not a highly precise way of determining memory used by the test. The `getrusage` results count allocated memory pages whether they're truly in use or not. It also can't separate memory that may have been allocated by the runtime for different purposes. Due to the difficulty of measuring memory, I've had to assume that `getrusage` is sufficient but there is certainly a margin for error in the numbers.

## Conclusion

> CustomObjectCreation.zip
> 
> (20kB) which contains all the code used in the test project for this post.

For very large arrays of Objective-C objects, it is certainly more efficient to allocate them yourself within C-style arrays. It is faster (on the order of 6 times faster) and more memory efficient (between 20% and 60% lower memory usage).

However, it is not something you should do for all arrays. There's a lot of extra code — any part of which could introduce issues — and it introduces object-lifetime issues but for very large arrays, the advantages (especially in CPU or memory constraint scenarios) could be worth the effort.
