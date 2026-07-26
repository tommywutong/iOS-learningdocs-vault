---
title: converting blocks into function pointers
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-02-12-trampolining-blocks-with-mutable-code.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:87f53fcc883c7c36'
translated: false
---

> 原文：[converting blocks into function pointers](https://www.mikeash.com/pyblog/friday-qa-2010-02-12-trampolining-blocks-with-mutable-code.html)　·　mikeash.com Friday Q&A

Posted at 2010-02-12 18:20 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-02-19: Character Encodings](https://www.mikeash.com/pyblog/friday-qa-2010-02-19-character-encodings.html)  
Previous article: [Friday Q&A 2010-02-05: Error Returns with Continuation Passing Style](https://www.mikeash.com/pyblog/friday-qa-2010-02-05-error-returns-with-continuation-passing-style.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [trampoline](https://www.mikeash.com/pyblog/?tag=trampoline)

Friday Q&A 2010-02-12: Trampolining Blocks with Mutable Code

by [Mike Ash](https://www.mikeash.com/)

**Background**  
 Blocks are really great, but not all APIs on the Mac have caught up to them yet. Lots of APIs still use older-style callbacks that take function pointers. And while you can adapt those APIs to use blocks by building small adapter functions, it's annoying to have to do that every time you want to use one, especially since each one works a little bit differently.

The toy project I've built allows a block to be transformed into a function pointer which, when called, invokes the block. This function pointer can then be passed to any API which takes a function pointer callback, and it will call your block and be none the wiser about it.

**Warning**  
 The code which I'm about to discuss is an _extreme hack_. It relies on intimate details of low-level platform calling conventions, so much so that I haven't bothered to make it work for any architecture other than `x86_64`. Even there it has important limitations. The purpose of this post is _not_ to present a practical library, but rather to explore some interesting but impractical low-level hacking. Do not, under any circumstances, use this code.

**Code**  
 Now that that's out of the way, let's talk about the code! It can be found in the usual place if you want to follow along with the entire codebase:

```
    svn co http://mikeash.com/svn/BlockFptr/
```

Before I get into specifics, let's talk quickly about how this whole thing is supposed to work, anyway. So I don't have to repeat this a thousand times later, let me state up front that every platform-specific detail I discuss is about

, and may not necessarily apply to other platforms, not even necessarily the other platforms that OS X runs on.

If you're still used to thinking of a 32-bit world, keep in mind that this means pointers are _eight_ bytes long.

First, a quick reminder of what a function pointer is: it's just a plain old pointer to the beginning of a function. To call it, the compiler generates code that sets up the stack and registers to pass parameters and save temporary values, and then simply jumps to that location in memory. Execution continues from there.

Blocks work similarly, but are somewhat more complex. A block is an _Objective-C object_, meaning it's a region of memory whose first eight bytes contain an `isa` pointer. The remainder of the block contains various other data useful to the block, like captured local variables. One of those pieces of data is a function pointer to the block's actual implementation. In order to call a block, the compiler generates code which simply fetches this function pointer, then calls it just like any other function pointer.

The major differentiator between function pointers and blocks at runtime is _context_. Function pointers are pure code, with no data associated. Whenever you encounter a function pointer callback API, you will invariably see a _context pointer_ that goes with it. This is typically just a `void *` pointing to arbitrary data. It's a way for the caller to get _context_ to the function pointer through the API, so that the function pointer can know what's going on. A pure function pointer with no context can really only access the parameters given to it and global variables. With a context pointer, it can refer back to the object that set up the callback, data from the particular invocation it's working on, etc.

Blocks automatically carry context. The function pointer which points to their implementation takes, as a hidden first parameter, a pointer to the block object itself. Through this, blocks are able to access captured local variables, giving them access to all the context they want, and with no extra work by the programmer.

The goal for my code is to bridge this context gap. The way I decided to do it is to build a _trampoline_. This is a small piece of code which has a block's address embedded in it. When the trampoline executes, it loads the block's address and the block's function pointer, then jumps to it with the block passed as the first parameter. By embedding the block's address directly in the code, this solves the problem of _context_, because now a single pointer will get you to both code and data.

In order to embed the address of a specific block into the code, that code needs to be copied and modified, which is the _really_ fun part of all of this.

**Trampoline Factory**  
 Yes, you can copy, modify, and then execute code. It's not even all that hard! You do need to ensure that the code in question will tolerate being modified (doesn't include any PC-relative references that won't be valid after it's moved), but that's easy if you write it in assembly, which I'm going to have to do anyway in order to do the parameter mangling and tail-calling that this trampoline requires.

Code can be accessed by just doing a memory copy starting with its pointer. A small assembler trick lets you figure out where the end is. Once you've copied it onto the heap, you can modify its contents at will. Once you're done with that, and you're ready to run it, then you can call `mprotect()` to make the data executable, and at that point you can call it.

However, this process is expensive. The call to `mprotect()` is a system call. Plus, it only works on full pages of memory (4096 bytes), but the trampoline itself is only a couple of dozen bytes, so there's a lot of wasted space. In order to make this cheaper, I want a way to construct trampolines in bulk, and to reuse them _without_ modifying their code after the initial construction.

As such, my architecture adds an additional level of indirection. The code contains a pointer to another region of memory. That bit of memory in turn contains a pointer to a block. Want to re-point the trampoline to a new block? Easy, just modify that extra bit of memory. This way, I can fill an entire 4096-byte page full of trampoline copies, then fill out their block pointers later on.

If this is confusing (and how could it not be?), here's a diagram:

```
    Trampoline      Intermediary        Block
    ----------      ------------        -----
    ...code...
    ...code...
    ...code...                         +------+
      pointer ------> pointer -------->|block |
    ...code...                         |object|
    ...code...                         +------+
    ...code...
```

Enough jabber, let's get to some code.

The trampoline needs to do four things. First, load the intermediary pointer into a register. The particular register in question is `%r11`, a designated scratch register whose value is not expected to survive across the function call:

```
    movabsq $0xdeadbeefcafebabe, %r11
```

Second, load the block pointer from the intermediary into

, the register which holds the first parameter to a function:

```
    mov (%r11), %rdi
```

Third, extract the function pointer from the block into

, the scratch register:

```
    mov BLOCK_FUNCTION_POINTER_OFFSET(%rdi), %r11
```

(

is just a macro

d to

.)

Fourth, jump to the address contained in `%r11`:

```
    jmp *%r11
```

The pointer value

used in the first instruction is literal in the code. I use a recognizable pattern so that it can be searched for later on by the code that modifies this code, so that I don't have to hardcode the offset to the pointer value.

**Finding the Address**  
 The code to search for `0xdeadbeefcafebabe` is simple. First, we start out with a couple of extern definitions which allow the compiler to find the assembly code:

```
    extern char Trampoline;
    extern char TrampolineEnd;
```

These correspond to labels used in the assembly. The first is the trampoline function itself, and the second is a label placed just after it so that the end can easily be identified.

Notice that these aren't pointers. When the program is linked, `Trampoline` ends up being on the first byte of the trampoline function. In order to get a pointer to the trampoline, we write `&Trampoline`, and likewise write `&TrampolineEnd` to get the end. The `char` type is fairly incidental, but makes it easy to do pointer arithmetic on the resulting pointers, because `char` is by definition one byte long.

Given that, the code to find the magic value is pretty simple: just loop through, trying each memory location, until it's found or you run off the end. And of course I can't help but throw in a little [Grand Central Dispatch](http://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html) to make this value be computed lazily:

```
    static int TrampolineAddrOffset(void)
    {
        static int addrOffset;
        static dispatch_once_t pred;
        dispatch_once(&pred, ^{
            uint64_t magic = 0xdeadbeefcafebabeULL;
            for(addrOffset = 0; addrOffset <= &TrampolineEnd - &Trampoline - sizeof(uint64_t); addrOffset++)
                if(*((uint64_t *)(&Trampoline + addrOffset)) == magic)
                    break;
        });
        
        return addrOffset;
    }
```

Right about now, you might be wondering, but what if the code

to contain the bit pattern

at some spot before the magic pointer value itself, and this gets the wrong offset?

Well, it's extremely unlikely (and probably impossible, if you look at what instruction sequences that could possibly represent), but ultimately it doesn't matter even if it did. The beauty of writing the trampoline in assembly is that it gives you the exact same output every time it's built. It's not like writing C code, where the compiler might generate different code depending on optimization levels, other code, the compiler version, the phase of the moon, etc. Thus, if this code returns the correct value once, it'll do it every time. Likewise, if it fails, it'll fail immediately. The only risk is after changing the trampoline, so you just have to test it out real quick to make sure that this piece is still functional.

**Intermediary**  
 The intermediary is pretty simple, but a bit more complex than strictly needed just for the trampoline. The reason for this is that I want to reuse these values, and that means holding onto them in a cache after they're done being used. For maximum thread safety and speed, the cache takes the form of an [OSQueue](http://developer.apple.com/Mac/library/documentation/Darwin/Reference/ManPages/man3/OSAtomicDequeue.3.html). That in turn requires that the intermediary have two fields (one for the queue's internal `next` pointer, and one to reference back to the trampoline it's associated with so we can fetch it) even though the trampoline only needs one. This is the definition of the intermediary:

```
    struct Intermediary
    {
        // when in the queue, the first field is the required 'next' pointer
        // when in use, the first field is the block pointer
        void *nextPtrOrBlock;
        
        // when in the queue, the second field is to the associated trampoline
        // when in use, the second field is unused
        void *trampoline;
    };
```

Now we're ready to actually copy the trampoline onto the heap and point it to its intermediary. Given a location in the heap, a length (computed from

and

), an offset (from

, and an intermediary pointer), the code to do the copy and modification is easy. First, copy the code:

```
    static void CreateTrampoline(void *destination, int length, int addrOffset, struct Intermediary *intermediary)
    {
        memcpy(destination, &Trampoline, length);
```

Fill out the intermediary:

```
        intermediary->nextPtrOrBlock = NULL;
        intermediary->trampoline = destination;
```

(The intermediary block pointer isn't being assigned yet, because we do that later, when a block is actually on hand. I set it to

here just for safety.)

Finally, point the newly minted trampoline back at the intermediary:

```
        *((void **)(destination + addrOffset)) = &intermediary->nextPtrOrBlock;
    }
```

That's how you create an individual trampoline, but the plan was to build them in bulk to amortize the cost of that

call. To do that, I built a function which creates a page full of them, and then enqueues them all onto the

so they can be fetched later.

The first thing to do is to figure out the trampoline's length, the offset of the intermediary address, the system's page size, and how many trampolines will fit into that page size:

```
    void CreateNewFptrsAndEnqueue(void)
    {
        int trampolineLength = &TrampolineEnd - &Trampoline;
        int addrOffset = TrampolineAddrOffset();
        
        int pageSize = getpagesize();
        int howmany = pageSize / trampolineLength;
```

Next, allocate a page for the trampolines (using

, to ensure that the resulting address is actually page-aligned) and a block of memory for the intermediaries:

```
        void *page = valloc(pageSize);
        
        struct Intermediary *intermediaries = malloc(howmany * sizeof(*intermediaries));
```

Next, loop through and create all the trampolines:

```
        for(int i = 0; i < howmany; i++)
        {
            void *destination = page + i * trampolineLength;
            CreateTrampoline(destination, trampolineLength, addrOffset, &intermediaries[i]);
        }
```

Then mark the page executable:

```
        int err = mprotect(page, pageSize, PROT_READ | PROT_EXEC);
        if(err)
            perror("mprotect");
```

Finally, push them all onto the trampoline cache:

```
        for(int i = 0; i < howmany; i++)
        {
            void *trampoline = page + i * trampolineLength;
            EnqueueCachedFptr(trampoline);
        }
    }
```

Next up, we need a bit of code that will dequeue a trampoline off that global cache, and set the intermediary to point to a block:

```
    static void *DequeueCachedFptr(id block)
    {
        struct Intermediary *intermediary = OSAtomicDequeue(&gFptrCache, 0);
        if(!intermediary)
            return NULL;
        
        intermediary->nextPtrOrBlock = [block copy];
        return intermediary->trampoline;
    }
```

Finally, we can put it all together, with a public-facing function that returns a trampoline. It first tries the cache. If the cache is empty, it creates a page full of trampolines, then tries the cache again. In the unlikely event that the caceh is

empty (other threads used all the trampolines before it could get any), then it creates another page and tries again, and keeps doing this until it gets one:

```
    void *CreateBlockFptr(id block)
    {
        void *fptr;
        while(!(fptr = DequeueCachedFptr(block)))
            CreateNewFptrsAndEnqueue();
        return fptr;
    }
```

Finally, the returned argument can be used to actually call a block like a function pointer:

```
    void (*fptr)(void) = CreateBlockFptr(^{ printf("hello, world!\n"); });
    fptr();
```

This will print out,

**Argument Shifting**  
 If you were to run this code, you'd find that it works fine for the case where the block takes no arguments, but not so well for blocks that do take arguments. The problem is that the function signatures don't match: since the block implementation takes the block pointer as an implicit first argument, all of the other arguments get shifted down. Since the trampoline doesn't touch the arguments that were in place when it got called, the result is that the first argument is obliterated by the block pointer, and the remaining arguments all end up shifted down.

There's some bad news here: in the general case, without knowing the full function signature ahead of time (this trampoline is intended to work with arbitrary function pointers), it is _impossible_ to reliably shift the arguments down by one in the `x86_64` ABI.

To be more specific: under the `x86_64` ABI, the first six `INTEGER` type parameters (which are basically integers and pointers, with some interesting things that happen to smaller structs composed of multiple integer/pointer types) get stored into six general-purpose registers, which are, in order: `%rdi`, `%rsi`, `%rdx`, `%rcx`, `%r8`, and `%r9`. Past six, they get spilled onto the stack. The problem is that a lot of other arguments can get spilled onto the stack as well, and the order in which that happens depends on the precise nature and ordering of all the arguments that the function takes.

The trampoline needs to shift all of those registers down by one (move `%rdi` to `%rsi`, `%rsi` to `%rdx`, etc.) _and_ spill the contents of `%r9` onto the stack. However, it's impossible to know where to spill it, or even whether it's necessary to do so.

Just because we can't solve this in the general case doesn't mean we can't solve enough to be useful, though. If we skip the step of spilling `%r9` onto the stack, the result will fail for functions which take more than five `INTEGER` types, but most callbacks won't be affected by that. Simply shifting the registers down by one will be enough. This can be done by putting a series of `mov` instructions at the beginning to shuffle all of the arguments down, then proceeding with the remainder of the trampoline as shown previously. The final result looks like this:

```
    .globl _Trampoline
    _Trampoline:
        // shuffle integer argument registers down by one
        // to make room for the implicit block ptr argument
        mov %r8, %r9
        mov %rcx, %r8
        mov %rdx, %rcx
        mov %rsi, %rdx
        mov %rdi, %rsi
        
        // move ptr-to-block-ptr into r11, dummy value is replaced at runtime
        movabsq $0xdeadbeefcafebabe, %r11
        // dereference ptr-to-block-ptr, move block ptr into %rdi
        mov (%r11), %rdi
        // extract block implementation function pointer into %r11
        mov BLOCK_FUNCTION_POINTER_OFFSET(%rdi), %r11
        // jump to block implementation
        jmp *%r11
    .globl _TrampolineEnd
    _TrampolineEnd:
        .long 0
        .long 0
```

Since the trampoline copying/modifying code is already fully generalized and just searches for the magic pointer value, it doesn't need to be changed at all to accommodate the new trampoline. If you try this, you'll find that it works with arguments... as long as you don't exceed five

-type arguments.

**Examples**  
 That was fun to build, but how about _using_ it?

These examples make use of an `AutoBlockFptr` function which basically wraps `CreateBlockFptr` to create an "autoreleased" block trampoline which is automatically destroyed when the enclosing `NSAutoreleasePool` is popped. I won't go into details of how it works (I didn't even cover how trampolines are recycled at all, for that matter) but you can check it out [in the code](http://mikeash.com/svn/BlockFptr/) if you want to see.

The `pthread` API is a classic one that deals with function pointers. You create a new thread with `pthread_create`, but it takes a function pointer and a context pointer, and that's always a pain. Of course, `pthread` is perhaps a bit less useful now that we have Grand Central Dispatch, but there are still lots of places where it comes in handy. Let's use this new code to adapt a block instead of dealing with function pointers:

```
    pthread_t thread;
    pthread_create(&thread, NULL, AutoBlockFptr(^(void *ignore) {
        printf("hello, world from a pthread!\n");
    }), NULL);
    pthread_join(thread, NULL);
```

This works just as you'd expect. The

API was never so easy!

How about some Objective-C runtime hackery?

```
    int captured = 99;
    class_addMethod([NSObject class], @selector(printInt:), CreateBlockFptr(^(id self, SEL _cmd, int x) {
        printf("in object %p, the captured integer is %d, the passed integer is %d\n", self, captured, x);
    }), "v@:i");
    NSObject *obj = [[NSObject alloc] init];
    [obj printInt: 42];
    [obj printInt: -11];
    [obj release];
```

Again, works perfectly:

```
    in object 0x1002003d0, the captured integer is 99, the passed integer is 42
    in object 0x1002003d0, the captured integer is 99, the passed integer is -11
```

CoreFoundation is a place where function pointers are common. How about creating a

with custom callbacks, all written inline?

```
    CFArrayCallBacks callbacks = {
        0,
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value) {
            NSLog(@"retain %@", value);
            return value;
        }),
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value) {
            NSLog(@"release %@", value);
        }),
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value) {
            NSLog(@"description of %@", value);
            return [(id)value description];
        }),
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value1, const void *value2) {
            NSLog(@"equality %@ %@", value1, value2);
            return (Boolean)[(id)value1 isEqual: (id)value2];
        })
    };
    
    CFMutableArrayRef array = CFArrayCreateMutable(NULL, 0, &callbacks);
    CFArrayAppendValue(array, @"first object");
    CFArrayAppendValue(array, @"second object");
    CFArrayRemoveAllValues(array);
```

When run, produces this:

```
    2010-02-11 00:21:51.238 BlockFptr[9201:a0f] retain first object
    2010-02-11 00:21:51.241 BlockFptr[9201:a0f] retain second object
    2010-02-11 00:21:51.242 BlockFptr[9201:a0f] release first object
    2010-02-11 00:21:51.243 BlockFptr[9201:a0f] release second object
```

That's all there is to it!

**Caveats**  
 I already mentioned that this code is dangerous and that you should never use it, but wanted to repeat that warning a second time. There are a _lot_ of limitations:

1. arguments.
2. returns at all, if the

  is big enough to trigger the special

  return calling conventions. Large structs are essentially returned by reference, by passing a pointer as an implicit first argument to the function. The trampoline will put the block pointer there instead, leading to hilarity. This could be worked around by adding a second trampoline just for

  returns.
3. , you can destroy the trampoline as soon as your block has started running. For uses which persist for the lifetime of the process, like adding a permanent method to an Objective-C object, you can just create it and leave it be. It's when it might be called multiple times but you eventually want to clean it up that it gets tricky, because normal code just assumes that any function pointer will last forever. The

  example is a good example of this: there's no easy way to link the lifetime of the trampolines to the lifetime of the

  . (The best way to do it is probably to use the Objective-C associated object API, but that's pretty ugly.)
4. . While it could be ported to other architectures, the argument and return-type limitations are likely to be different on those other architectures, breaking previously working code. (On iPhone OS, Apple doesn't even allow this sort of runtime generation of code at all.)

Despite these problems, it's still a good learning experience and a fun toy to play with.

**Conclusion**  
 This sort of low-level assembly hacking can be tricky and, as you can see, the result isn't always completely practical. However, it's a lot of fun, and a great way to learn about how the system is put together at the bottom.

That's it for this week. As always (except this week!) Friday Q&A is driven by user suggestions, so if you have a topic that you'd like to see covered here, [send it in](mailto:mike@mikeash.com)! Otherwise, see you next week.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
