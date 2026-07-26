---
title: Tagged pointers
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af51233dc62f68c4'
translated: false
---

> 原文：[Tagged pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)　·　mikeash.com Friday Q&A

Posted at 2012-07-27 13:35 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-08-10: A Tour of CommonCrypto](https://www.mikeash.com/pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html)  
Previous article: [Friday Q&A 2012-07-06: Let's Build NSNumber](https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-07-27: Let's Build Tagged Pointers

by [Mike Ash](https://www.mikeash.com/)

**Pointer Alignment Theory**  
As we all know, a pointer is just an integer that's treated as an address in memory. Under the covers, a variable holding a pointer to an object is really just an integer holding a value like `0x7f84a41000c0`. The pointer nature of this value is entirely in how the program uses in. In C, we can extract the integer value of a pointer with a simple cast:

```
    void *somePointer = ...;
    uintptr_t pointerIntegerValue = (uintptr_t)somePointer;
```

(The `uintptr_t` type is a standard C `typedef` for an integer type large enough to hold a pointer. This is useful, as pointer sizes will vary across platforms.)

Most computer architectures have a concept of _pointer alignment_. This means that a pointer to a particular data type should be a multiple of some power of two. For example, a pointer to a 4-byte integer should be a multiple of 4 on most architectures. Violating alignment restrictions can cause performance impacts (on some platforms, the attempt throws a hardware exception that has to be emulated by the OS) and, on certain performance-sensitive architectures, can just crash outright. Correct alignment is also required for things like atomic reads and writes to memory. In short, pointer alignment is important and something you want to respect.

If you make a local variable, the compiler can ensure that the alignment is correct:

```
    void f(void)
    {
        int x;
        // x is aligned properly, because
        // the compiler has full control
        // over its location
    }
```

However, things are not so simple for dynamically allocated memory:

```
    int *ptr = malloc(sizeof(*ptr));
    // is ptr aligned properly?
```

`malloc` has no idea what kind of data the program is going to be storing. It gets a request for 4 bytes (assuming that `int` is 4 bytes), but it has no idea if this is an `int`, a pointer (on 32-bit platforms), two `short`s, four `char`s, or something else.

In order to ensure proper alignment, `malloc` takes a paranoid approach and returns pointers that are aligned to a boundary large enough to guarantee correct alignment no matter what data types are stored. On Mac OS X, `malloc` always returns pointers aligned to 16-byte boundaries.

Because of alignment, there are unused bits in any aligned pointer. The hex representation of a 16-byte aligned pointer looks like:

```
    0x-------0
```

That last hex digit is _always_ `0`. It's possible to have a valid pointer that doesn't respect this (for example, a `char *` has no alignment restrictions), but object pointers will always have some zero bits at the end.

**Tagged Pointer Theory**  
Some objects contain very little data. `NSNumber` is an excellent example of this: depending on exactly what kind of number the object is storing, the data it stores is only one, two, four, or eight bytes. Having an entire object dedicated to these, with memory allocation and deallocation, and indirecting through pointers to that object for every access, is wasteful.

What if we took advantage of those unused low bits in a pointer to indicate that this is not a real pointer? What if we then stored the object data inline in the rest of this non-pointer instead of off in a separate memory allocation? The result of doing so is a tagged pointer.

Systems which use tagged pointers require an extra check. Any time an object pointer is used, the system checks the low bit. If it's zero, it's a real object pointer and treated normally. If the low bit is one, then it can't be a real pointer, since it's not correctly aligned. In that case, the pointer is handled specially. Typically, the object type is encoded in the low bits of the pointer, with the object data in the high bits. A normal pointer will look like this:

```
    ....0000
        ^ all zeroes at the end
```

While a tagged pointer looks like this:

```
    ....xxx1
        ^ type encoded in bottom bits
```

There are variations on this. For example, a tagged pointer could have _any_ of the bottom four bits set. You can have even more tag bits by taking advantage of additional architecture peculiarities. For example, `x86_64` actually only uses 48 bits of a pointer, leaving you with 16 bits free on top of the 4 you get due to alignment. With this, you can do crazy things like stuff pointers into floating-point `not a number` values.

For whatever reason, the Objective-C implementation of tagged pointers has the bottom bit always set to `1` in a tagged pointer, with the other three bits indicating the class of the tagged pointer. I'm not sure why they chose to implement it in this way, but my guess is some combination between speed (it may be easier to check only the bottom bit, and this has to be done in the fast path of `objc_msgSend`) and simple convenience in programming.

**Tagged Pointer Uses**  
Tagged pointers often show up in languages where everything is an object. When the number `3` is an object, and an expression like `3 + 4` involves two objects and creates a third, object creation and value extraction becomes important to performance.

We generally think of an object as a separate memory allocation, referenced with a pointer. This was always the case in Objective-C before tagged pointers came along, and is always the case in a lot of other languages as well. However, memory allocation and management incurs substantial overhead. When evaluating `3 + 4`, the overhead of allocating memory for the result of `7` and then eventually disposing of it when nobody is using it far outweighs the cost of actually performing the addition.

Referring to everything with a pointer also incurs overhead simply for accessing the data. To load the value of the `3` object, the CPU has to load the value of the pointer to that object, then load the primitive `3` stored within the object itself. Since memory is slow, this extra access can be costly.

By using tagged pointers, these costs can be eliminated for data which fits within the tagged pointer. Small integers are an excellent candidate for this, since they can easily fit, and tend to be used a lot. The integer `3` would normally be represented like:

```
    0000 0000 0000 0000 0000 0000 0000 0011
                                         ^ binary 3
```

With tagged pointers, it would look something like this:

```
    0000 0000 0000 0000 0000 0000 0011 1011
                                    ^  ^  ^ tag bit
                                    |  |
                                    |  tagged pointer class (5)
                                    |
                                    binary 3
```

The actual value is shifted over a bit, and the tag bits are set appropriately. For this example, I've assumed that the integer class is identified by the value `5` in the tag bits, but that's entirely arbitrary, and it's up to the system to figure out the meaning of each value in the tag bits.

The observant reader will notice that the space left for storing the value is smaller than that of a plain integer. After using 4 bits for the tag, there are 28 bits left for a value on 32-bit systems, and 60 bits left for a value on 64-bit systems. Integers which require more than 28 or 60 bits to store can't be placed in a tagged pointer, and will have to be stored in a regular object.

When everything fits within the tagged pointer, there's no need for a separate memory allocation. This means no overhead to allocate or destroy the memory. No additional memory loads are needed, since all of the data is right there. There's a bit of extra overhead because some shifting and masking is needed to extract the `3`, but CPUs are really fast at those operations and they're much faster than accessing a separate chunk of memory.

In addition to the speed benefits, this also reduces memory usage, since no separate chunk of memory has to be allocated to hold these integers. It's inconsequential for a single expression like `3 + 4`, but it can make for a substantial savings in code that uses a lot of integers.

With the ability to use the tag bits distinguish between several classes of tagged pointers, it's possible to store more than just integers. Floating point numbers could be stored in tagged pointers as well. Even off-the-wall items like small strings could be stored. (A 64-bit pointer can hold eight ASCII characters in addition to the tag bits.) A one-element array holding a single (non-tagged) pointer to an object could be held in a tagged pointer. Any class which is both small and frequently used is a good candidate for a tagged pointer.

Although Objective-C has primitive integers and doesn't use objects for every single mathematical expression, numeric objects are still common in a lot of Objective-C code. Any time we put numbers into an array or dictionary, we have to use `NSNumber` to box them up into an object. Any time we encode or decode a property list or JSON we have to route all numbers through `NSNumber`. Since `NSNumber` is used a lot, and is mostly used to store numbers that fit within a tagged pointer, `NSNumber` is an excellent candidate for tagged pointers, and that's what Cocoa does. Tagged pointers are also used for suitable `NSDate` objects. Plenty of room is available for expansion to other uses as well.

**Tagged Pointer Practice**  
Enough theory, let's write some code.

You'll recall my `NSNumber` workalike from [last time](https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html), `MANumber`. I'm now going to add tagged pointer support to `MANumber`.

Note that tagged pointers are very, very, very private and cannot under any circumstances be used in any real code. There are an extremely limited number of tagged pointer classes. Since there are only three bits of tag available to indicate the class, only eight tagged classes can be used. If your tagged class conflicts with one in the frameworks, it's game over. Additionally, since details of the tagged pointer implementation aren't exposed through any public API, they're subject to change without notice. The meaning or number of the tag bits could change, or the whole thing could be thrown out if it's decided that it's not worth the trouble.

However, by using the appropriate private API, it is possible to _experiment_ with tagged pointers, even if we can never use them safely.

In particular, the private `_objc_insert_tagged_isa` function allows associating a class with a particular tag. This is its prototype:

```
    void _objc_insert_tagged_isa(unsigned char slotNumber, Class isa);
```

You give it a slot number (tag) and a class, and it sets the appropriate table entry so that the two are associated in the runtime.

Nearly any tagged pointer class also needs a non-tagged class to go along with it. For this case, we need the regular `MANumber` to store integers that don't fit into a tagged pointer, and also to store `double` values, which are _really_ hard to squeeze into a tagged pointer, and thus are something I skipped over. Depending on the value being stored, we either create a tagged pointer or allocate a normal instance.

There are two approaches here. One is to create two completely different classes, with some kind of common superclass so that they can share common code. The other is to use the same class for both, and have two code paths for tagged and non-tagged pointers whenever the code looks up internal data (like instance variables). I chose to go with the latter approach here, as it seemed simpler for this case.

For the most part, `MANumber` can stay the same. I routed some direct instance variable accesses through accessors in order to group the conditionalized code all in one place, but most of the class stayed the same. `MANumber` uses a `union` to store the actual value, which I found useful to break out so that it could be used to pass values around, and not just as an instance variable:

```
    union Value
    {
        long long i;
        unsigned long long u;
        double d;
    };
```

Next up are a bunch of constants used to manipulate the tagged pointer. First is the tagged pointer slot to use for `MANumber`, which I arbitrarily chose as `1`:

```
    const int kSlot = 1;
```

I also put the number of tag bits into a constant, since it's used for encoding and decoding the tagged pointers:

```
    const int kTagBits = 4;
```

I decided to keep the same basic structure of `MANumber` in the tagged pointer. It stores a value as well as a type which says how to interpret that value. The type can be either an integer, unsigned integer, or `double`. Since everything needs to be packed as tighly as possible, I want to use the minimum number of bits to represent the type. Since there are three types, I set aside two bits to hold the type:

```
    const int kTypeBits = 2;
```

Note that although I'm not supporting `double` in the tagged pointer, I still reserve enough space to represent its type. This is done purely for consistency, and to make it easier to add `double` support at some point.

Finally, since the integer type we're storing is a `long long`, it's useful to know exactly how many bits that is:

```
    const int kLongLongBits = sizeof(long long) * CHAR_BIT;
```

I'm assuming in this code that `long long` is the size of a pointer. I did not attempt to create a 32-bit compatible version of the tagged pointer code.

To better manipulate tagged pointers, I wrote some helper functions. The first is a function that constructs a tagged `MANumber` pointer out of a value and type:

```
    static id TaggedPointer(unsigned long long value, unsigned type)
    {
```

Recall the structure of a tagged pointer. The least significant bit is always `1`. The next three bits are the tag, or slot, which indicates the class of the object. After that is the class's own data. In this case, the next two bits are the type, and everything after that is the value. Here's a line which squishes all of these components together using bitwise shifting and `or`ing:

```
        id ptr = (__bridge id)(void *)((value << (kTagBits + kTypeBits)) | (type << kTagBits) | (kSlot << 1) | 1);
```

Note the odd double cast here. I'm building with ARC, which is picky about casting. You need `__bridge` when casting between object pointers and non-object pointers, and furthermore it won't allow casting between object pointers and integers at all. To convert between the integer version of the tagged pointer and the object version, I first have to cast the integer to a `void *`, and only then can I cast the result to an object.

That's all that needs to be done, so I return the newly constructed pointer:

```
        return ptr;
    }
```

I also have a function that checks whether a pointer is tagged or not. All this involves is checking the least-significant bit, but ugly casting is needed to work around ARC's demands, so it was good to wrap it up in a single function:

```
    static BOOL IsTaggedPointer(id pointer)
    {
        uintptr_t value = (uintptr_t)(__bridge void *)pointer;
        return value & 1;
    }
```

Finally, there's a function to break a tagged pointer out into its components. Since C doesn't support multiple return values, I created a `struct` that holds the two values to return: the value and the type.

```
    struct TaggedPointerComponents
    {
        unsigned long long value;
        unsigned type;
    };
```

The function itself first converts the pointer into an integer, using the reverse of the weird double cast shown above:

```
    static struct TaggedPointerComponents ReadTaggedPointer(id pointer)
    {
        uintptr_t value = (uintptr_t)(__bridge void *)pointer;
```

Next, it extracts the relevant fields. The tag bits themselves can be ignored, since they don't influence the `MANumber`'s value or type. The `MANumber` value is extracted by just shifting the pointer down by the appropriate amount:

```
        struct TaggedPointerComponents components = {
            value >> (kTagBits + kTypeBits),
```

The type must be masked as well as shifted. The mask is generated by shifting `1` to the left by the number of tag bits, generating the binary value `100`, then subtracting `1` from that value, resulting in the binary value `11`. By doing a logical `and` with that value, we get rid of all bits in the pointer aside from the bits that represent the type:

```
            (value >> kTagBits) & ((1ULL << kTypeBits) - 1)
        };
```

Now that the components are extracted, the function just returns them.

```
        return components;
    }
```

At some point, we have to actually tell the runtime that we want to act as a tagged pointer class, by calling `_objc_insert_tagged_isa`. The obvious place to do this is in `+initialize`. I actually call this twice, once to clear out any previous entry, and again to insert the new entry. As a protective measure, the Objective-C runtime gets very upset if you try to directly overwrite an existing class in the tagged pointer table:

```
    + (void)initialize
    {
        if(self == [MANumber class])
        {
            _objc_insert_tagged_isa(kSlot, nil);
            _objc_insert_tagged_isa(kSlot, self);
        }
    }
```

Now we can get to actually constructing the tagged pointers. I wrote two new methods: `+numberWithLongLong:` and `+numberWithUnsignedLongLong:`. These will try to construct a tagged pointer from their argument if possible, and otherwise fall back to allocating an instance of the class.

These methods can only create a tagged pointer if the value is within certain limits. Namely, the value has to fit within `kLongLongBits - kTagBits - kTypeBits` bits, which is 58 bits on a 64-bit system. The largest `long long` that fits within that space is 257-1. The smallest `long long` that fits is -257. One bit is needed for the sign bit, since `long long` is signed. Based on this, we compute the min and max for a tagged `long long`:

```
    + (id)numberWithLongLong: (long long)value {
        long long taggedMax = (1ULL << (kLongLongBits - kTagBits - kTypeBits - 1)) - 1;
        long long taggedMin = -taggedMax - 1;
```

The rest is simple. If the value lies beyond the bounds, we simply do the regular `alloc`/`init` dance. If it's within bounds, we call `TaggedPointer` with the value and `INT` to construct the tagged pointer:

```
        if(value > taggedMax || value < taggedMin)
            return [[self alloc] initWithLongLong: value];
        else
            return TaggedPointer(value, INT);
    }
```

The code for `unsigned long long` is similar. There's only one limit in this case, and it's 258-1:

```
    + (id)numberWithUnsignedLongLong:(unsigned long long)value {
        unsigned long long taggedMax = (1ULL << (kLongLongBits - kTagBits - kTypeBits)) - 1;

        if(value > taggedMax)
            return [[self alloc] initWithUnsignedLongLong: value];
        else
            return (id)TaggedPointer(value, UINT);
    }
```

Next, we need a `type` accessor that handles tagged pointers, so that the rest of the code can simply call `[self type]` without worrying about bits and masking and such. This is pretty simple. All it has to do is call `IsTaggedPointer`, call `ReadTaggedPointer` if the pointer is tagged, and otherwise simply return the `_type` instance variable:

```
    - (int)type
    {
        if(IsTaggedPointer(self))
            return ReadTaggedPointer(self).type;
        else
            return _type;
    }
```

There's also a `value` accessor, but it's a bit more complicated due to the need to handle sign extension in the resulting value. The first thing it does is check to see whether the pointer is tagged and, if it's not, return the `_value` instance variable:

```
    - (union Value)value
    {
        if(!IsTaggedPointer(self))
        {
            return _value;
        }
```

For tagged pointers, it first reads the value from `ReadTaggedPointer`. This pops out as an `unsigned long long`, and so needs some work in the event that the actual type is signed:

```
        else
        {
            unsigned long long value = ReadTaggedPointer(self).value;
```

It also creates a local variable of type `union Value` to hold the return value:

```
            union Value v;
```

If the value is unsigned, then life is simple: simply stuff `value` into `v`.

```
            int type = [self type];
            if(type == UINT)
            {
                v.u = value;
            }
```

However, signed integers get a bit more complex. The first thing it does is check the sign bit, which in this case lives in bit `57`:

```
            else if(type == INT)
            {
                unsigned long long signBit = (1ULL << (kLongLongBits - kTagBits - kTypeBits - 1));
```

If the sign bit is set, then all of the other bits in the number beyond `57` need to be set to `1` as well, in order for the resulting `long long` to be seen as a proper 64-bit negative number. This procedure is called [sign extension](http://en.wikipedia.org/wiki/Sign_extension), and it works this way due to the way that modern computers implement signed integers. The short version is that a negative number consists of all `1`s at the beginning, and the first `0` is really the first significant digit of the number. To make a positive number wider, you simply add `0`s to the left side. To make a negative number wider, you add `1`s to the left side:

```
                if(value & signBit)
                {
                    unsigned long long mask = (((1ULL << kTagBits + kTypeBits) - 1) << (kLongLongBits - kTagBits - kTypeBits));
                    value |= mask;
                }
```

Nothing needs to be done for positive numbers, as they're already filled with extra `0`s on the left side. All that needs to be done is to assign to the right field in `v`:

```
                v.i = value;
            }
```

If the type is something else, then something has gone wrong, so check for that and `abort`:

```
            else
                abort();
```

Finally, return `v`:

```
            return v;
        }
    }
```

With this code in place, all of the other `MANumber` code works without any changes other than modifying it to call these accessors rather than directly accessing instance variables. You can mix and match tagged and untagged `MANumber` instances with impunity, and even use `compare:` and `isEqual:` on mixed objects.

**Conclusion**  
Tagged pointers are a great addition to Cocoa and the Objective-C runtime which improve speed and reduce memory usage for `NSNumber` objects. By stuffing object data directly into the pointer, tagged pointers eliminate the need for a separate memory allocation and an extra level of indirection when retrieving values.

We can implement our own tagged pointer classes by using private runtime calls and some bit twiddling, which gives us some insight into just what `NSNumber` is doing behind the scenes. However, due to the restricted number of tagged pointer classes, it's not possible to safely use tagged pointers in our own code. They are purely a mechanism for Cocoa to perform better. They do this job wonderfully, and make `NSNumber` much less painful.

That's it for today! Come back next time for more crazy shenanigans. Friday Q&A is driven by reader suggestions, so if you have an idea for a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
