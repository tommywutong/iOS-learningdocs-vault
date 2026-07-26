---
title: '__NSDictionaryI objectForKey: – Bartosz Ciechanowski'
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/extra/objectforkeyassembly/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f51ddffdbf9ea808'
translated: false
---

> 原文：[__NSDictionaryI objectForKey: – Bartosz Ciechanowski](https://ciechanow.ski/extra/objectforkeyassembly/)　·　Bartosz Ciechanowski

# [__NSDictionaryI objectForKey:](https://ciechanow.ski/extra/objectforkeyassembly/)

This is a companion article for my [blog post](https://ciechanow.ski/blog/2014/04/08/exposing-nsdictionary/#howItWorks) on `NSDictionary`. It contains the disassembly analysis for `objectForKey:` method of `__NSDictionaryI` class. The disassembly was generated using [Hopper](http://www.hopperapp.com) and it’s based on iOS 7.1 SDK targeting ARM64 architecture.

## The Code[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#the-code)

Here’s what we’re going to digest:

```s
0x14e90       stp        x29, x30, [sp, #0xfffffff0]!
0x14e94       mov        x29, sp
0x14e98       stp        x20, x19, [sp, #0xfffffff0]!
0x14e9c       stp        x22, x21, [sp, #0xfffffff0]!
0x14ea0       stp        x24, x23, [sp, #0xfffffff0]!
0x14ea4       mov        x19, x2
0x14ea8       mov        x8, x0
0x14eac       movz       x0, #0x0
0x14eb0       adrp       x9, #0x1d1000
0x14eb4       ldrsw      x9, [x9, #0x60]
0x14eb8       ldrb       w9, [x8, x9]
0x14ebc       lsr        w21, w9, #0x2
0x14ec0       cbz        w21, 0x14f80

0x14ec4       mov        x0, x8
0x14ec8       bl         imp___stubs__object_getIndexedIvars
0x14ecc       mov        x20, x0
0x14ed0       adrp       x8, #0x1ad000
0x14ed4       add        x8, x8, #0x768
0x14ed8       ldr        x1, [x8]
0x14edc       mov        x0, x19
0x14ee0       bl         imp___stubs__objc_msgSend
0x14ee4       mov        x8, x0
0x14ee8       movz       x0, #0x0
0x14eec       and        w9, w21, #0xff
0x14ef0       cmp        w9, #0x3f
0x14ef4       b.eq       0x14f80

0x14ef8       movz       x23, #0x0
0x14efc       adrp       x9, #0x156000
0x14f00       add        x9, x9, #0xf38
0x14f04       add        x9, x9, w21, uxtb #3
0x14f08       ldr        x22, [x9]
0x14f0c       udiv       x9, x8, x22
0x14f10       msub       x24, x9, x22, x8
0x14f14       adrp       x8, #0x1ad000
0x14f18       add        x8, x8, #0x770
0x14f1c       ldr        x21, [x8]

0x14f20       add        x8, x20, x24, lsl #4
0x14f24       ldr        x0, [x8]
0x14f28       cmp        x0, #0x0
0x14f2c       ccmp       x0, x19, #0x4, ne
0x14f30       b.eq       0x14f68

0x14f34       mov        x1, x21
0x14f38       mov        x2, x19
0x14f3c       bl         imp___stubs__objc_msgSend
0x14f40       tbnz       w0, #0x0, 0x14f68

0x14f44       movz       x0, #0x0
0x14f48       add        x8, x24, #0x1
0x14f4c       cmp        x8, x22
0x14f50       csel       x9, xzr, x22, lo
0x14f54       sub        x24, x8, x9
0x14f58       add        x23, x23, #0x1
0x14f5c       cmp        x23, x22
0x14f60       b.lo       0x14f20

0x14f64       b          0x14f80

0x14f68       movz       x0, #0x0
0x14f6c       lsl        x8, x24, #0x1
0x14f70       cmp        x8, x22, lsl #1
0x14f74       b.hs       0x14f80

0x14f78       orr        x8, x8, #0x1
0x14f7c       ldr        x0, [x20, x8, lsl #3]

0x14f80       ldp        x24, x23, [sp], #0x10
0x14f84       ldp        x22, x21, [sp], #0x10
0x14f88       ldp        x20, x19, [sp], #0x10
0x14f8c       ldp        x29, x30, [sp], #0x10
0x14f90       ret      
```

This is quite a lot, but we’re going to take it chunk by chunk and I will more or less describe what each instruction does.

## The Setup[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#the-setup)

We begin the procedure by with ARM64 function prolog. We’re also storing `x19`, `x20`, `x21`, `x22`, `x23` and `x24` registers on the stack. Those are callee-saved registers and since the function is going to make use of those, we have to store their previous value, thus fulfilling caller’s expectations of those register maintaining their value:

```s
0x14e90       stp        x29, x30, [sp, #0xfffffff0]!
0x14e94       mov        x29, sp
0x14e98       stp        x20, x19, [sp, #0xfffffff0]!
0x14e9c       stp        x22, x21, [sp, #0xfffffff0]!
0x14ea0       stp        x24, x23, [sp, #0xfffffff0]!
```

When the function is called, the `x0` register contains `self` pointer and `x2` register has a pointer to `key`. Since we’re going to make a few calls from the function itself, and those registers are used for arguments passing, we need to keep their current value aside. We move the values from `x2` and `x0` registers to `x19` and `x8` register respectively:

```s
0x14ea4       mov        x19, x2
0x14ea8       mov        x8, x0
```

We clear out the `x0` register, effectively making it store `nil` value:

```s
0x14eac       movz       x0, #0x0
```

## Fetching Size Index[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#fetching-size-index)

As [it’s been discussed previously](https://ciechanow.ski/blog/2014/03/05/exposing-nsmutablearray/#fetching-count), the next three instructions simply fetch the one byte contents of `_szidx` ivar into `w9` register:

```s
0x14eb0       adrp       x9, #0x1d1000
0x14eb4       ldrsw      x9, [x9, #0x60]
0x14eb8       ldrb       w9, [x8, x9]
```

Notice that we’ve fetched 8 bits of memory, but `_szidx` is defined as 6-bits bitfield. We have to shift the `w9` register 2 bits to the right, discarding the unwanted bits, and storing the result into `w21` register:

```s
0x14ebc       lsr        w21, w9, #0x2
```

At this point we can compare whether the value of `_szidx` is equal to `0`, if so, we jump to instruction at offset of `0x14f80`, which is a function epilog. At this point we still have `0` in `x0` so the function will return `nil`:

```s
0x14ec0       cbz        w21, 0x14f80
```

As we will see very soon, it’s rare for `_szidx` to be equal to zero, so we can safely keep interpreting instructions one by one.

## Dynamic Linking[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#dynamic-linking)

We restore the `self` pointer kept in `x8` back into `x0`. It will be passed as the first argument to the `imp___stubs__object_getIndexedIvars` function. After the function returns its result is kept in `x0`, but since this register will be used heavily, it is moved into the `x20`:

```s
0x14ec4       mov        x0, x8
0x14ec8       bl         imp___stubs__object_getIndexedIvars
0x14ecc       mov        x20, x0
```

One might wonder why we’re calling the `imp___stubs__object_getIndexedIvars` function instead of `object_getIndexedIvars`. It all boils down to dynamic linking. At the point of compilation the compiler merely knows that when the program is run, there will be an `object_getIndexedIvars` function available in the system. It creates a very short stub function that fetches a memory address and jumps to it.

On the first run this memory address points to a helper function that will run the dyld machinery to figure out where the function is and then the memory address gets overwritten to point to the correct location of `object_getIndexedIvars`. This process is called lazy binding and provides very fast booting (since the application doesn’t have to link anything that hasn’t been yet needed) at the cost of very slight call overhead.

## The Hash[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#the-hash)

Another round of program counter relative memory fetching. This time the `hash` selector lands in `x1`:

```s
0x14ed0       adrp       x8, #0x1ad000
0x14ed4       add        x8, x8, #0x768
0x14ed8       ldr        x1, [x8]
```

We’re moving back the `key` pointer from `x19` into `x0` and with `hash` selector in `x1` we’re calling everyone’s favorite `objc_msgSend` (through a stub), then we move the `hash`’s return value from `x0` to `x8`:

```s
0x14edc       mov        x0, x19
0x14ee0       bl         imp___stubs__objc_msgSend
0x14ee4       mov        x8, x0
```

Using pseudo C we might summarize those few instructions with:

```obj
x8 = [key hash];
```

We conveniently put `nil` into the `x0` register:

```s
0x14ee8       movz       x0, #0x0
```

I’m not entirely sure why it’s needed, but we clear all but last 8 bits of `w21` (which contains the value of `_szidx`) by binary ANDing it with `0xff`. Then we compare the value with `0x3f`. In case the values are equal, we jump to the function epilog, returning a `nil` value stored previously in `x0` register:

```s
0x14eec       and        w9, w21, #0xff
0x14ef0       cmp        w9, #0x3f
0x14ef4       b.eq       0x14f80
```

Very soon we’ll use `x23` register as a loop counter, so it makes sense to zero it out:

```s
0x14ef8       movz       x23, #0x0
```

A quick fetch of some address into `x9`:

```s
0x14efc       adrp       x9, #0x156000
0x14f00       add        x9, x9, #0xf38
```

What’s at `0x156f38?` Hopper comes to help:

```s
___NSDictionarySizes:
0000000000156f38         db  0x00 ;
0000000000156f39         db  0x00 ;
...
```

I’ve explained what `__NSDictionarySizes` contains in the main article, but for the purpose of assembly analysis suffice it to say, it’s an _array_ of some values.

With `_szidx` still in `w21`, we left-shift it by 3, which is the same as multiplying by 8 which is the size of `NSUInteger` on 64-bit architectures. Finally we fetch the contents of memory at that location into `x22` register:

```s
0x14f04       add        x9, x9, w21, uxtb #3
0x14f08       ldr        x22, [x9]
```

While the fetching arithmetics looks quite complicated, the C equivalent is super simple:

```obj
x22 = __NSDictionarySizes[_szidx];
```

## Division[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#division)

Here comes the fun part! With return value of `hash` in `x8` and some kind of size in `x22` we divide the former by the latter, storing the result in `x9`. Then we use **m**ultiply-**sub**tract instruction which in this case subtracts `x9 * x22` from `x8` storing the result in `x24`:

```s
0x14f0c       udiv       x9, x8, x22
0x14f10       msub       x24, x9, x22, x8
```

What just happened? Here’s the C pseudocode:

```c
x9 = x8 / x22;
x24 = x8 - x9 * x22;
```

Treating the code algebraically one might argue that the value of `x24` is simply `0`, since values of `x22` in both nominator and denominator cancel each other out. However, the `udiv` instruction does _integer_ division, discarding the remainder. It turns out, there is an operator in C that does the very same calculation in a more compact way:

```c
x24 = x8 % x22;
```

That’s it. We’re just doing a modulo calculation in a form of `hash % size`. As you might suspect, we’re checking which slot does the hash fall into. We can expect `x22` to contain some kind of limit of the storage size.

## The Most Important Selector[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#the-most-important-selector)

We’re just one step shy of fetching value for a key, all that’s missing is the `isEqual:` selector that the next three instructions fetch into `x21` register:

```s
0x14f14       adrp       x8, #0x1ad000
0x14f18       add        x8, x8, #0x770
0x14f1c       ldr        x21, [x8]
```

## The Loop[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#the-loop)

At this point we have the address of indexed ivars in `x20` register and the modulo calculation result in `x24` from now on called index. We’re going to shift it to the left by _four_ bits. The three bit shift is responsible for making the index equal to 64-bit pointer size (8 bytes), but the one addition shift multiplies the index by two. The fetch result is stored in `x0`:

```s
0x14f20       add        x8, x20, x24, lsl #4
0x14f24       ldr        x0, [x8]
```

Here’s the conditional comparison magic of ARM64. At first we **c**o**mp**are if the previously fetched value is equal to `0`. The **c**onditional **c**o**mp**are instruction works as follow: if the result of the previous operation was **n**ot **e**qual, then the NZCV flags (**n**egative, **z**ero, **c**arry, o**v**erflow) will contain the comparison result of `x0` and `x19`, otherwise the NZCV flags will be equal to 0x4 which is 0100 in binary. If you look at the pattern you might notice that only the **Z**ero flag will be set. The `b.eq` instruction actually checks the `Z` flag jumping to the `0x14f68` address only if it’s set to 1:

```s
0x14f28       cmp        x0, #0x0
0x14f2c       ccmp       x0, x19, #0x4, ne
0x14f30       b.eq       0x14f68
```

Let’s go through this once again. The `b.eq` will jump if `Z` flag is set. The `Z` flag will be set either when `x0` is equal to `0` (`cmp` instruction also sets `Z` to 1 when true) _or_ when `x0` is equal to `key` stored in `x19`. Here’s the equivalent C pseudocode:

```objc
if (x0 == 0 || x0 == key)
    goto 0x14f68; 
```

In other words, if the value fetched somewhere from within index ivars is `nil`, _or_ it is equal to key, then we’re done. This is super important, it means that we’ve actually fetched the stored key and we’re comparing it with the key passed into `objectForKey:` call.

We’re going to go into `0x14f68` shortly, but for now we can assume that the fetched key is not `nil` and is not equal (as in pointer equality) to the query key, so let’s keep going. We’re getting ready for another Objective-C method call. With fetched `key` in `x0` (will map to `self`), `isEqual:` selector in `x21` (will map to `_cmd`) and query key in `x19` (will map to `object` argument), it’s just the matter of preparing `x1` and `x2` registers and executing the call:

```s
0x14f34       mov        x1, x21
0x14f38       mov        x2, x19
0x14f3c       bl         imp___stubs__objc_msgSend
```

In other words we’re doing:

```obj
x0 = [fetchedKey isEqualTo:queryKey];
```

If the method call returns YES (the 0^th bit is **n**ot **z**ero), we’re jumping into the `0x14f68`.

```s
0x14f40       tbnz       w0, #0x0, 0x14f68
```

Here’s where we are at this point: we’ve fetched a non-nil key, that is not equal to query key in terms of both pointer and `isEqual:` comparison.

We clear out `x0`:

```s
0x14f44       movz       x0, #0x0
```

We add one to `x24` (which keeps the modulo operation result) at store it into `x8`:

```s
0x14f48       add        x8, x24, #0x1
```

We do a bounds check. If `x8` is lower than the size limit kept in `x22` then we store `0` (kept in `xzr` zero register) into `x9`, otherwise we feed it with `x22`:

```s
0x14f4c       cmp        x8, x22
0x14f50       csel       x9, xzr, x22, lo
0x14f54       sub        x24, x8, x9
```

The equivalent C code is less complicated:

```objc
x9 = x8 < x22 ? 0 : x22;
x24 = x8 - x9;
```

This is a very simple iteration that advances the index one by one, but when we hit the end it’s wrapped around back to the beginning.

At `0x14ef8` we cleared the loop counter `x23` and now it finally gets used. We increment it and compare to the limit in `x22`. If we haven’t yet crossed the iteration limit we jump back to the beginning of the loop:

```s
0x14f58       add        x23, x23, #0x1
0x14f5c       cmp        x23, x22
0x14f60       b.lo       0x14f20
```

This check prevents the dictionary from iterating over its contents endlessly.

## Getting Past the Loop[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#getting-past-the-loop)

The only way we got to this point is when we’ve iterated over all the keys stored in the indexed ivars, every key was non-nil and no key was equal to query key. We haven’t find what we’ve been looking for and at this point with `0` still in `x0` register we can jump to the function prolog, returning the `nil` from the function:

```s
0x14f64       b        0x14f80
```

Here comes the long awaited `0x14f68` part. As a reminder, at this point the `x24` register contains the index, that when multiplied by two, can be used to fetch the key that is either `nil` or is _equal_ to the query key.

Next comes the very convenient `x0` clearing, we’ll see why it’s handy in a second:

```s
0x14f68       movz       x0, #0x0
```

We shift the fetch index to the left and store the result in `x8`:

```s
0x14f6c       lsl        x8, x24, #0x1
```

Then we compare this to 1-bit-left-shifted value of `x22` register (`x22` contains the storage limit). If the doubled fetch index is larger than doubled limit then we jump to the epilog at `0x14f80`:

```s
0x14f70       cmp        x8, x22, lsl #1
0x14f74       b.hs       0x14f80
```

This is why we needed the `x0` clearing at `0x14f68`. If we succeed the test, i.e. when the fetch index is out of bounds, then we jump to the epilog at `0x14f80`, and we will safely return `nil` from the function.

Assuming we are within the bounds we can finally digest the last two crucial instructions.

## The Object Fetch[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#the-object-fetch)

We’re doing a bitwise OR operation on the fetch index in `x8`, but since `x8` has been recently shifted to the left (multiplied by two) then this is no different than adding one to `x8`. With address of indexed ivars in `x20` we add it to the 3-bits-left shifted `x8` (pointer size shift) and then we dereference the entire thing into `x0`.

```s
0x14f78       orr        x8, x8, #0x1
0x14f7c       ldr        x0, [x20, x8, lsl #3]
```

We’ve just fetched the object corresponding to the query key into `x0`.

## Epilog[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/extra/objectforkeyassembly/#epilog)

We’re done at this point. With the return value safely stored in `x0` we can clean up the stack and return:

```s
0x14f80       ldp        x24, x23, [sp], #0x10
0x14f84       ldp        x22, x21, [sp], #0x10
0x14f88       ldp        x20, x19, [sp], #0x10
0x14f8c       ldp        x29, x30, [sp], #0x10
0x14f90       ret      
```
