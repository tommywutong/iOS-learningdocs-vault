---
title: 'Friday Q&A 2017-06-30: Dissecting objc_msgSend on ARM64'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d8990aca06001b81'
translated: false
---

> 原文：[Friday Q&A 2017-06-30: Dissecting objc_msgSend on ARM64](https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html)　·　mikeash.com Friday Q&A

Posted at 2017-07-01 04:23 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2017-07-14: Swift.Codable](https://www.mikeash.com/pyblog/friday-qa-2017-07-14-swiftcodable.html)  
Previous article: [More Advanced Swift Workshop, and Blog and Book Updates](https://www.mikeash.com/pyblog/more-advanced-swift-workshop-and-blog-and-book-updates.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2017-06-30: Dissecting objc_msgSend on ARM64

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
Every Objective-C object has a class, and every Objective-C class has a list of methods. Each method has a selector, a function pointer to the implementation, and some metadata. The job of `objc_msgSend` is to take the object and selector that's passed in, look up the corresponding method's function pointer, and then jump to that function pointer.

Looking up a method can be extremely complicated. If a method isn't found on a class, then it needs to continue searching in the superclasses. If no method is found at all, then it needs to call into the runtime's message forwarding code. If this is the very first message being sent to a particular class, then it has to call that class's `+initialize` method.

Looking up a method also needs to be extremely fast in the common case, since it's done for every method call. This, of course, is in conflict with the complicated lookup process.

Objective-C's solution to this conflict is the method cache. Each class has a cache which stores methods as pairs of selectors and function pointers, known in Objective-C as `IMP`s. They're organized as a hash table so lookups are fast. When looking up a method, the runtime first consults the cache. If the method isn't in the cache, it follows the slow, complicated procedure, and then places the result into the cache so that the next time can be fast.

`objc_msgSend` is written in assembly. There are two reasons for this: one is that it's not possible to write a function which preserves unknown arguments and jumps to an arbitrary function pointer in C. The language just doesn't have the necessary features to express such a thing. The other reason is that it's extremely important for `objc_msgSend` to be fast, so every last instruction of it is written by hand so it can go as fast as possible.

Naturally, you don't want to write the whole complicated message lookup procedure in assembly langauge. It's not necessary, either, because things are going to be slow no matter what the moment you start going through it. The message send code can be divided into two parts: there's the _fast path_ in `objc_msgSend` itself, which is written in assembly, and the _slow path_ implemented in C. The assembly part looks up the method in the cache and jump to it if it's found. If the method is not in the cache, then it calls into the C code to handle things.

Therefore, when looking at `objc_msgSend` itself, it does the following:

1. Get the class of the object passed in.
2. Get the method cache of that class.
3. Use the selector passed in to look up the method in the cache.
4. If it's not in the cache, call into the C code.
5. Jump to the `IMP` for the method.

How does it do all of that? Let's see!

**Instruction by Instruction**  
`objc_msgSend` has a few different paths it can take depending on circumstances. It has special code for handling things like messages to `nil`, tagged pointers, and hash table collisions. I'll start by looking at the most common, straight-line case where a message is sent to a non-`nil`, non-tagged pointer and the method is found in the cache without any need to scan. I'll note the various branching-off points as we go through them, and then once we're done with the common path I'll circle back and look at all of the others.

I'll list each instruction or group of instructions followed by a description of what it does and why. Just remember to look _up_ to find the instruction any given piece of text is discussing.

Each instruction is preceded by its offset from the beginning of the function. This serves as a counter, and lets you identify jump targets.

ARM64 has 31 integer registers which are 64 bits wide. They're referred to with the notation `x0` through `x30`. It's also possible to access the lower 32 bits of each register as if it were a separate register, using `w0` through `w30`. Registers `x0` through `x7` are used to pass the first eight parameters to a function. That means that `objc_msgSend` receives the `self` parameter in `x0` and the selector `_cmd` parameter in `x1`.

Let's begin!

```
    0x0000 cmp     x0, #0x0
    0x0004 b.le    0x6c
```

This performs a signed comparison of `self` with `0` and jumps elsewhere if the value is less than or equal to zero. A value of zero is `nil`, so this handles the special case of messages to nil. This also handles [tagged pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html). Tagged pointers on ARM64 are indicated by setting the high bit of the pointer. (This is an interesting contrast with x86-64, where it's the low bit.) If the high bit is set, then the value is negative when interpreted as a signed integer. For the common case of `self` being a normal pointer, the branch is not taken.

```
    0x0008 ldr    x13, [x0]
```

This loads `self`'s `isa` by loading the 64-bit quantity pointed to by `x0`, which contains `self`. The `x13` register now contains the `isa`.

```
    0x000c and    x16, x13, #0xffffffff8
```

ARM64 can use [non-pointer isas](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html). Traditionally the `isa` points to the object's class, but non-pointer `isa` takes advantage of spare bits by cramming some other information into the `isa` as well. This instruction performs a logical AND to mask off all the extra bits, and leaves the actual class pointer in `x16`.

```
    0x0010 ldp    x10, x11, [x16, #0x10]
```

This is my favorite instruction in `objc_msgSend`. It loads the class's cache information into `x10` and `x11`. The `ldp` instruction loads _two_ registers' worth of data from memory into the registers named in the first two arguments. The third argument describes where to load the data, in this case at offset `16` from `x16`, which is the area of the class which holds the cache information. The cache itself looks like this:

```
    typedef uint32_t mask_t;

    struct cache_t {
        struct bucket_t *_buckets;
        mask_t _mask;
        mask_t _occupied;
    }
```

Following the `ldp` instruction, `x10` contains the value of `_buckets`, and `x11` contains `_occupied` in its high 32 bits, and `_mask` in its low 32 bits.

`_occupied` specifies how many entries the hash table contains, and plays no role in `objc_msgSend`. `_mask` is important: it describes the size of the hash table as a convenient AND-able mask. Its value is always a power of two minus 1, or in binary terms something that looks like `000000001111111` with a variable number of 1s at the end. This value is needed to figure out the lookup index for a selector, and to wrap around the end when searching the table.

```
    0x0014 and    w12, w1, w11
```

This instruction computes the starting hash table index for the selector passed in as `_cmd`. `x1` contains `_cmd`, so `w1` contains the bottom 32 bits of `_cmd`. `w11` contains `_mask` as mentioned above. This instruction ANDs the two together and places the result into `w12`. The result is the equivalent of computing `_cmd % table_size` but without the expensive modulo operation.

```
    0x0018 add    x12, x10, x12, lsl #4
```

The index is not enough. To start loading data from the table, we need the actual address to load from. This instruction computes that address by adding the table index to the table pointer. It shifts the table index left by `4` bits first, which multiplies it by `16`, because each table bucket is `16` bytes. `x12` now contains the address of the first bucket to search.

```
    0x001c ldp    x9, x17, [x12]
```

Our friend `ldp` makes another appearance. This time it's loading from the pointer in `x12`, which points to the bucket to search. Each bucket contains a selector and an `IMP`. `x9` now contains the selector for the current bucket, and `x17` contains the `IMP`.

```
    0x0020 cmp    x9, x1
    0x0024 b.ne   0x2c
```

These instructions compare the bucket's selector in `x9` with `_cmd` in `x1`. If they're not equal then this bucket does not contain an entry for the selector we're looking for, and in that case the second instruction jumps to offset `0x2c`, which handles non-matching buckets. If the selectors do match, then we've found the entry we're looking for, and execution continues with the next instruction.

```
    0x0028 br    x17
```

This performs an unconditional jump to `x17`, which contains the `IMP` loaded from the current bucket. From here, execution will continue in the actual implementation of the target method, and this is the end of `objc_msgSend's` fast path. All of the argument registers have been left undisturbed, so the target method will receive all passed in arguments just as if it had been called directly.

When everything is cached and all the stars align, this path can execute in less than 3 nanoseconds on modern hardware.

That's the fast path, how about the rest of the code? Let's continue with the code for a non-matching bucket.

```
    0x002c cbz    x9, __objc_msgSend_uncached
```

`x9` contains the selector loaded from the bucket. This instruction compares it with zero and jumps to `__objc_msgSend_uncached` if it's zero. A zero selector indicates an empty bucket, and an empty bucket means that the search has failed. The target method isn't in the cache, and it's time to fall back to the C code that performs a more comprehensive lookup. `__objc_msgSend_uncached` handles that. Otherwise, the bucket doesn't match but isn't empty, and the search continues.

```
    0x0030 cmp    x12, x10
    0x0034 b.eq   0x40
```

This instruction compares the current bucket address in `x12` with the beginning of the hash table in `x10`. If they match, it jumps to code that wraps the search back to the end of the hash table. We haven't seen it yet, but the hash table search being performed here actually runs backwards. The search examines decreasing indexes until it hits the beginning of the table, then it starts over at the end. I'm not sure why it works this way rather than the more common approach of increasing addresses that wrap to the beginning, but it's a safe bet that it's because it ends up being faster this way.

Offset `0x40` handles the wraparound case. Otherwise, execution proceeds to the next instruction.

```
    0x0038 ldp    x9, x17, [x12, #-0x10]!
```

Another `ldp`, once again loading a cache bucket. This time, it loads from offset `0x10` to the address of the current cache bucket. The exclamation point at the end of the address reference is an interesting feature. This indicates a register write-back, which means that the register is updated with the newly computed value. In this case, it's effectively doing `x12 -= 16` in addition to loading the new bucket, which makes `x12` point to that new bucket.

```
    0x003c b      0x20
```

Now that the new bucket is loaded, execution can resume with the code that checks to see if the current bucket is a match. This loops back up to the instruction labeled `0x0020` above, and runs through all of that code again with the new values. If it continues to find non-matching buckets, this code will keep running until it finds a match, an empty bucket, or hits the beginning of the table.

```
    0x0040 add    x12, x12, w11, uxtw #4
```

This is the target for when the search wraps. `x12` contains a pointer to the current bucket, which in this case is also the first bucket. `w11` contains the table mask, which is the size of the table. This adds the two together, while also shifting `w11` left by 4 bits, multiplying it by `16`. The result is that `x12` now points to the end of the table, and the search can resume from there.

```
    0x0044 ldp    x9, x17, [x12]
```

The now-familiar `ldp` loads the new bucket into `x9` and `x17`.

```
    0x0048 cmp    x9, x1
    0x004c b.ne   0x54
    0x0050 br     x17
```

This code checks to see if the bucket matches and jumps to the bucket's `IMP`. It's a duplicate of the code at `0x0020` above.

```
    0x0054 cbz    x9, __objc_msgSend_uncached
```

Just like before, if the bucket is empty then it's a cache miss and execution proceeds into the comprehensive lookup code implemented in C.

```
    0x0058 cmp    x12, x10
    0x005c b.eq   0x68
```

This checks for wraparound _again_, and jumps to `0x68` if we've hit the beginning of the table a second time. In this case, it jumps into the comprehensive lookup code implemented in C:

```
    0x0068 b      __objc_msgSend_uncached
```

This is something that should never actually happen. The table grows as entries are added to it, and it's never 100% full. Hash tables become inefficient when they're too full because collisions become too common.

Why is this here? A comment in the source code explains:

> Clone scanning loop to miss instead of hang when cache is corrupt. The slow path may detect any corruption and halt later.

I doubt that this is common, but evidently the folks at Apple have seen memory corruption which caused the cache to be filled with bad entries, and jumping into the C code improves the diagnostics.

The existence of this check should have minimal impact on code that doesn't suffer from this corruption. Without it, the original loop could be reused, which would save a bit of instruction cache space, but the effect is minimal. This wraparound handler is not the common case anyway. It will only be invoked for selectors that get sorted near the beginning of the hash table, and then only if there's a collision and all the prior entries are occupied.

```
    0x0060 ldp    x9, x17, [x12, #-0x10]!
    0x0064 b      0x48
```

The remainder of this loop is the same as before. Load the next bucket into `x9` and `x17`, update the bucket pointer in `x12`, and go back to the top of the loop.

That's the end of the main body of `objc_msgSend`. What remains are special cases for `nil` and tagged pointers.

**Tagged Pointer Handler**  
You'll recall that the very first instructions checked for those and jumped to offset `0x6c` to handle them. Let's continue from there:

```
    0x006c b.eq    0xa4
```

We've arrived here because `self` is less than or equal to zero. Less than zero indicates a tagged pointer, and zero is `nil`. The two cases are handled completely differently, so the first thing the code does here is check to see whether `self` is `nil` or not. If `self` is equal to zero then this instruction branches to `0xa4`, which is where the `nil` handler lives. Otherwise, it's a tagged pointer, and execution continues with the next instruction.

Before we move on, let's briefly discuss how tagged pointers work. Tagged pointers support multiple classes. The top four bits of the tagged pointer (on ARM64) indicate which class the "object" is. They are essentially the tagged pointer's isa. Of course, four bits isn't nearly enough to hold a class pointer. Instead, there's a special table which stores the available tagged pointer classes. The class of a tagged pointer "object" is found by looking up the index in that table which corresponds to the top four bits.

This isn't the whole story. Tagged pointers (at least on ARM64) also support extended classes. When the top four bits are all set to `1` the next eight bits are used to index into an extended tagged pointer class table. This allows the runtime to support more tagged pointer classes, at the cost of having less storage for them.

Let's continue.

```
    0x0070 mov    x10, #-0x1000000000000000
```

This sets `x10` to an integer value with the top four bits set and all other bits set to zero. This will serve as a mask to extract the tag bits from `self`.

```
    0x0074 cmp    x0, x10
    0x0078 b.hs   0x90
```

This checks for an extended tagged pointer. If `self` is greater than or equal to the value in `x10`, then that means the top four bits are all set. In that case, branch to `0x90` which will handle extended classes. Otherwise, use the primary tagged pointer table.

```
    0x007c adrp   x10, _objc_debug_taggedpointer_classes@PAGE
    0x0080 add    x10, x10, _objc_debug_taggedpointer_classes@PAGEOFF
```

This little song and dance loads the address of `_objc_debug_taggedpointer_classes`, which is the primary tagged pointer table. ARM64 requires two instructions to load the address of a symbol. This is a standard technique on RISC-like architectures. Pointers on ARM64 are 64 bits wide, and instructions are only 32 bits wide. It's not possible to fit an entire pointer into one instruction.

x86 doesn't suffer from this problem, since it has variable-length instructions. It can just use a 10-byte instruction, where two bytes identify the instruction itself and the target register, and eight bytes hold the pointer value.

On a machine with fixed-length instructions, you load the value in pieces. In this case, only two pieces are needed. The `adrp` instruction loads the top part of the value, and the `add` then adds in the bottom part.

```
    0x0084 lsr    x11, x0, #60
```

The tagged class index is in the top four bits of `x0`. To use it as an index, it has to be shifted right by `60` bits so it becomes an integer in the range `0-15`. This instruction performs that shift and places the index into `x11`.

```
    0x0088 ldr    x16, [x10, x11, lsl #3]
```

This uses the index in `x11` to load the entry from the table that `x10` points to. The `x16` register now contains the class of this tagged pointer.

```
    0x008c b      0x10
```

With the class in `x16`, we can now branch back to the main code. The code starting with offset `0x10` assumes that the class pointer is loaded into `x16` and performs dispatch from there. The tagged pointer handler can therefore just branch back to that code rather than duplicating logic here.

```
    0x0090 adrp   x10, _objc_debug_taggedpointer_ext_classes@PAGE
    0x0094 add    x10, x10, _objc_debug_taggedpointer_ext_classes@PAGEOFF
```

The extended tagged class handler looks similar. These two instructions load the pointer to the extended table.

```
    0x0098 ubfx   x11, x0, #52, #8
```

This instruction loads the extended class index. It extracts `8` bits starting from bit `52` in `self` into `x11`.

```
    0x009c ldr    x16, [x10, x11, lsl #3]
```

Just like before, that index is used to look up the class in the table and load it into `x16`.

```
    0x00a0 b      0x10
```

With the class in `x16`, it can branch back into the main code.

That's nearly everything. All that remains is the `nil` handler.

**`nil` Handler**  
Finally we get to the `nil` handler. Here it is, in its entirety.

```
    0x00a4 mov    x1, #0x0
    0x00a8 movi   d0, #0000000000000000
    0x00ac movi   d1, #0000000000000000
    0x00b0 movi   d2, #0000000000000000
    0x00b4 movi   d3, #0000000000000000
    0x00b8 ret
```

The `nil` handler is completely different from the rest of the code. There's no class lookup or method dispatch. All it does for `nil` is return `0` to the caller.

This task is a bit complicated by the fact that `objc_msgSend` doesn't know what kind of return value the caller expects. Is this method returning one integer, or two, or a floating-point value, or nothing at all?

Fortunately, all of the registers used for return values can be safely overwritten even if they're not being used for this particular call's return value. Integer return values are stored in `x0` and `x1` and floating point return values are stored in vector registers `v0` through `v3`. Multiple registers are used for returning smaller `struct`s.

This code clears `x1` and `v0` through `v3`. The `d0` through `d3` registers refer to the bottom half of the corresponding `v` registers, and storing into them clears the top half, so the effect of the four `movi` instructions is to clear those four registers. After doing this, it returns control to the caller.

You might wonder why this code doesn't clear `x0`. The answer to that is simple: `x0` holds `self` which in this case is `nil`, so it's already zero! You can save an instruction by not clearing `x0` since it already holds the value we want.

What about larger `struct` returns that don't fit into registers? This requires a little cooperation from the caller. Large `struct` returns are performed by having the caller allocate enough memory for the return value, and then passing the address of that memory in `x8`. The function then writes to that memory to return a value. `objc_msgSend` can't clear this memory, because it doesn't know how big the return value is. To solve this, the compiler generates code which fills the memory with zeroes before calling `objc_msgSend`.

That's the end of the `nil` handler, and of `objc_msgSend` as a whole.

**Conclusion**  
It's always interesting to dive into framework internals. `objc_msgSend` in particular is a work of art, and delightful to read through.

That's it for today. Come back next time for more squishy goodness. Friday Q&A is driven by reader input, so if you have something you'd like to see discussed here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
