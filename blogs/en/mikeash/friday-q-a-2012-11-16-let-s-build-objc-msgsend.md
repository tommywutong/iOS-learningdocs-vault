---
title: 'Friday Q&A 2012-11-16: Let''s Build objc_msgSend'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4830a06afb70dcc9'
translated: false
---

> 原文：[Friday Q&A 2012-11-16: Let's Build objc_msgSend](https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)　·　mikeash.com Friday Q&A

Posted at 2012-11-16 14:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-11-30: Let's Build A Mach-O Executable](https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)  
Previous article: [Friday Q&A 2012-11-09: dyld: Dynamic Linking On OS X](https://www.mikeash.com/pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-11-16: Let's Build objc_msgSend

by [Mike Ash](https://www.mikeash.com/)

**Tramapoline! Trampopoline!**  
Whenever you write an Objective-C message send:

```
    [obj message]
```

The compiler generates a call to `objc_msgSend`:

```
    objc_msgSend(obj, @selector(message));
```

`objc_msgSend` then takes care of dispatching the message.

How does it do that? It looks up the appropriate function pointer, or `IMP`, to invoke, then jumps to it. Any arguments passed to `objc_msgSend` end up being arguments to the `IMP` after the jump. The return value from the `IMP` ends up as the return value seen by the caller.

Because `objc_msgSend` only takes control long enough to obtain the right function pointer and directly jump to it, it's sometimes referred to as a _trampoline_. In general, any small piece of code that serves to redirect code somewhere else can be called a trampoline.

It is this trampolining behavior that makes `objc_msgSend` special. Because it simply looks up the right code and then jumps directly to it, it's relatively generic. It works with _any_ combination of parameters passed to it, because it just leaves them alone for the method `IMP` to read. Return values are a bit trickier, but it turns out that every possible return type can be accounted for with just a couple of variants of `objc_msgSend`.

Unfortunately, this trampoline behavior cannot be written in pure C. There is no way to write a C function that passes through generic parameters to another function. You can come close by using variable arguments, but variable arguments are passed differently from normal arguments and in a way that's slower, so it's not compatible with regular C parameters.

If you _could_ write `objc_msgSend` in C, the basic idea would look something like this:

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        Class c = object_getClass(self);
        IMP imp = class_getMethodImplementation(c, _cmd);
        return imp(self, _cmd, ...);
    }
```

This is actually a bit over-simplified. There's a method cache to make the whole lookup faster, so it's more like this:

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        Class c = object_getClass(self);
        IMP imp = cache_lookup(c, _cmd);
        if(!imp)
            imp = class_getMethodImplementation(c, _cmd);
        return imp(self, _cmd, ...);
    }
```

Except that, for speed, `cache_lookup` is implemented inline.

**Assembly**  
In Apple's runtime, the whole function is implemented in assembly for maximum speed. `objc_msgSend` runs for every single Objective-C message send, and the simplest action in app can result in thousands or millions of messages.

To simplify things a bit, my own implementation will do the bare minimum in assembly, with all of the smarts in a separate C function. The assembly itself will do the equivalent of:

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        IMP imp = GetImplementation(self, _cmd);
        imp(self, _cmd, ...);
    }
```

Then `GetImplementation` can do all of the work in a more understandable fashion.

The assembly code needs to:

1. Save all potential parameters somewhere safe, so that `GetImplementation` won't overwrite them.
2. Call `GetImplementation`.
3. Save the return value somewhere.
4. Restore all of the parameter values.
5. Jump to the `IMP` returned from `GetImplementation`.

So let's get started!

I'm going to use x86-64 assembly here, as it's the most convenient to work with on a Mac. The same principles would apply for i386 or ARM.

This function goes into its own file, which I called `msgsend-asm.s`. This file can be passed to the compiler as just another source file, and it will assemble it and link it into the rest of the program.

The first thing to do is to actually declare the global symbol. For boring historical reasons, C functions get an extra leading underscore in their global symbol name:

```
    .globl _objc_msgSend
    _objc_msgSend:
```

The compiler will happily link against the nearest available `objc_msgSend`. Simply linking this into a test app is enough to get `[obj message]` expressions going to our own code rather than Apple's runtime, which is terribly convenient when it comes to testing this code to make sure it actually works.

Integer and pointer parameters are passed in registers `%rsi`, `%rdi`, `%rdx`, `%rcx`, `%r8`, and `%r9`. Any additional parameters beyond what would fit in there get passed on the stack. The first thing this function does is save those six registers onto the stack as well, so they can be restored later:

```
    pushq %rsi
    pushq %rdi
    pushq %rdx
    pushq %rcx
    pushq %r8
    pushq %r9
```

In addition to these registers, the `%rax` register acts as something of a hidden parameter. It's used for variable-argument calls, and in that case it stores the number of vector registers passed in, which is used by the called function to properly prepare the variable argument list. In case the target method is a variable-argument method, I save this register as well:

```
    pushq %rax
```

For completeness, the `%xmm` registers used to pass floating-point arguments really ought to be saved as well. However, if I can safely assume that `GetImplementation` doesn't use any floating point, then I can ignore them, which I do simply to keep the code shorter.

Next, I align the stack. Mac OS X requires that the stack be aligned to a 16-byte boundary when making function calls. The above code leaves us with an aligned stack anyway, but it's nice to have code to explicitly handle it so that you don't have to worry about making sure everything is lined up, or wondering why your app is crashing in `dyld` functions. To align the stack, I save the existing stack pointer into `%r12` after saving the original value of `%r12` onto the stack. The choice of `%r12` is somewhat arbitrary, and any caller-saved register would do. The important thing is that the value is guaranteed to survive across the call to `GetImplementation`. Then I `and` the stack pointer with `-0x10`, which just clears the bottom four bits:

```
    pushq %r12
    mov %rsp, %r12
    andq $-0x10, %rsp
```

Now the stack pointer is aligned. It's also safely past any of the saved registers from above, since the stack grows down, and this alignment procedure will only move it further down.

It's finally time to call into `GetImplementation`. It takes two parameters, `self` and `_cmd`. Calling conventions are for those two parameters to go into `%rsi` and `%rdi`, respectively. However, they were passed into `objc_msgSend` like that, and haven't been moved, so nothing has to be done to get them into place. All that has to be done is actually make the call to `GetImplementation`, which also gets a leading underscore:

```
    callq _GetImplementation
```

Integer and pointer return values are returned in `%rax`, so that's where the returned `IMP` is found. Since `%rax` has to be restored to its original state, the returned `IMP` needs to be moved elsewhere. I arbitrarily chose to store it into `%r11`:

```
    mov %rax, %r11
```

Now it's time to start putting things back the way they were. The first item is to restore the stack pointer, which was stashed in `%r12`, and restore the old value of `%r12`:

```
    mov %r12, %rsp
    popq %r12
```

Then pop all of the argument registers off the stack in the opposite order from when they were pushed:

```
    popq %rax
    popq %r9
    popq %r8
    popq %rcx
    popq %rdx
    popq %rdi
    popq %rsi
```

Everything is now ready. The argument registers are restored to how they were before. All parameters intended for the target method are in the place where the target method will expect to find them. The `IMP` itself is in `%r11`, so all that has to be done is to jump there:

```
    jmp *%r11
```

And that's it! There's nothing more to be done in the assembly code. The jump passes control to the method implementation. From the perspective of that code, it looks _exactly_ as if the message sender directly invoked the method. All of the indirection above just disappears. When the method returns, it will return directly to the caller of `objc_msgSend` without any further intervention. Any return value from the method will be found in the correct place.

There's a bit of subtlety when it comes to unusual return values. Large `struct`s (anything too large to be returned in a register) are the most common example of this. On x86-64, large `struct`s are returned by using a hidden first parameter. When you make a call like this:

```
    NSRect r = SomeFunc(a, b, c);
```

The call gets translated to something more like this:

```
    NSRect r;
    SomeFunc(&r, a, b, c);
```

The address of memory to use for the return value gets passed in `%rdi`. Since `objc_msgSend` expects `%rdi` and `%rsi` to contain `self` and `_cmd`, it won't work for messages that return large `struct`s. This same basic problem exists on many different platforms. The runtime solves this problem by providing a separate `objc_msgSend_stret` function used for `struct` returns, which works like `objc_msgSend`, but knows to find `self` in `%rsi` and `_cmd` in `%rdx`.

A similar problem arises on some platforms with messages that return floating point values. On those platforms, the runtime provides `objc_msgSend_fpret` (and on x86-64, `objc_msgSend_fpret2` for extremely special cases).

**Method Lookup**  
Let's move on to the implementation of `GetImplementation`. The above assembly trampoline means that this code can be written in C. Remember that in the real runtime, this code is all straight assembly, in order to get the best speed possible. Not only does this allow for fine control over the code, but it also eliminates the need to save and restore all of those registers like the code above does.

`GetImplementation` could simply call `class_getMethodImplementation` and be done with it, foisting all of the work onto the Objective-C runtime. This is a bit boring, though. The real `objc_msgSend` looks in the class's method cache first, for maximum speed. Since `GetImplementation` is intended to mimic `objc_msgSend`, it will do the same. Only if the cache doesn't contain an entry for the given selector will it fall back to querying the runtime.

The first thing we need is some `struct` definitions. The method cache is a private set of structures accessed through the class structure, so to get to it we need our own definitions. Note that, while private, these definitions are all available as part of Apple's open source release of the Objective-C runtime.

First comes the definition for a single cache entry:

```
    typedef struct {
        SEL name;
        void *unused;
        IMP imp;
    } cache_entry;
```

Pretty easy. Don't ask me about the `unused` field, I don't know why that's there. Here's the definition for the cache as a whole:

```
    struct objc_cache {
        uintptr_t mask;
        uintptr_t occupied;        
        cache_entry *buckets[1];
    };
```

The cache is implemented as a hash table. This table is built for speed and simplicity over all else, so it's a bit unusual. The table size is always a power of two. The table is indexed by selector, and the bucket index is computed by simply taking the selector's value, possibly shifting it to get rid of irrelevant low bits, and performing a logical _and_ with the appropriate mask. While we're at it, here are macros used to compute the bucket index for a particular selector and mask:

```
    #ifndef __LP64__
    # define CACHE_HASH(sel, mask) (((uintptr_t)(sel)>>2) & (mask))
    #else
    # define CACHE_HASH(sel, mask) (((unsigned int)((uintptr_t)(sel)>>0)) & (mask))
    #endif
```

Finally, there's the structure for the class itself. This is what a `Class` actually points to:

```
    struct class_t {
        struct class_t *isa;
        struct class_t *superclass;
        struct objc_cache *cache;
        IMP *vtable;
    };
```

Let's get started with `GetImplementation` now that the necessary structs are there:

```
    IMP GetImplementation(id self, SEL _cmd)
    {
```

The first thing it does is get the object's class. The real `objc_msgSend` does this with the equivalent of `self->isa`, but I'll be gentle and use the official API for that part:

```
        Class c = object_getClass(self);
```

Since I want access to the guts, I'll immediately cast to a pointer to the `class_t` `struct`:

```
        struct class_t *classInternals = (struct class_t *)c;
```

Now it's time to look up the `IMP`. We'll start off with it set to `NULL`. If we find an entry in the cache, we'll set it. If it's still `NULL` after checking the cache, we'll fall back to the slow path:

```
        IMP imp = NULL;
```

Next, grab a pointer to the cache:

```
        struct objc_cache *cache = classInternals->cache;
```

Compute the bucket index, and grab a pointer to the array of buckets:

```
        uintptr_t index = CACHE_HASH(_cmd, cache->mask);
        cache_entry **buckets = cache->buckets;
```

Next, we search for a cache entry with the appropriate selector. The runtime uses linear chaining, so it's just a matter of searching subsequent buckets until either we find a match or find a `NULL` entry:

```
        for(; buckets[index] != NULL; index = (index + 1) & cache->mask)
        {
            if(buckets[index]->name == _cmd)
            {
                imp = buckets[index]->imp;
                break;
            }
        }
```

If no entry was found, we fall back to the slow path and call into the runtime. In the real `objc_msgSend`, all of the above code is written in assembly, and this is the point where it would drop out of assembly and call into the runtime itself. Once the cache has been tried and no entry was found, any hope for a fast message send is gone. The need to go fast becomes much less important at this point, partly because it's already doomed to be slow, and partly because this path should be taken extremely rarely. Because of that, it's acceptable to drop out of the assembly code and call into more maintainable C:

```
        if(imp == NULL)
            imp = class_getMethodImplementation(c, _cmd);
```

The `IMP` has now been obtained, one way or another. If it was in the cache, it was retrieved from there, and otherwise it was populated by the runtime. The `class_getMethodImplementation` call will also populate the cache, so subsequent calls will go faster. All that's left is to return it the `IMP`:

```
        return imp;
    }
```

**Testing**  
To make sure this stuff actually works, I whipped up a quick test program:

```
    @interface Test : NSObject
    - (void)none;
    - (void)param: (int)x;
    - (void)params: (int)a : (int)b : (int)c : (int)d : (int)e : (int)f : (int)g;
    - (int)retval;
    @end

    @implementation Test

    - (id)init
    {
        fprintf(stderr, "in init method, self is %p\n", self);
        return self;
    }

    - (void)none
    {
        fprintf(stderr, "in none method\n");
    }

    - (void)param: (int)x
    {
        fprintf(stderr, "got parameter %d\n", x);
    }

    - (void)params: (int)a : (int)b : (int)c : (int)d : (int)e : (int)f : (int)g
    {
        fprintf(stderr, "got params %d %d %d %d %d %d %d\n", a, b, c, d, e, f, g);
    }

    - (int)retval
    {
        fprintf(stderr, "in retval method\n");
        return 42;
    }

    @end

    int main(int argc, char **argv)
    {
        for(int i = 0; i < 20; i++)
        {
            Test *t = [[Test alloc] init];
            [t none];
            [t param: 9999];
            [t params: 1 : 2 : 3 : 4 : 5 : 6 : 7];
            fprintf(stderr, "retval gave us %d\n", [t retval]);

            NSMutableArray *a = [[NSMutableArray alloc] init];
            [a addObject: @1];
            [a addObject: @{ @"foo" : @"bar" }];
            [a addObject: @("blah")];
            a[0] = @2;
            NSLog(@"%@", a);
        }
    }
```

I also added some debug logs to `GetImplementation` to make sure it actually got called, in case I screwed up the build and ended up calling the runtime's implementation by mistake. Everything worked, and even the literals and subscripting called the replacement implementation.

**Conclusion**  
At its core, `objc_msgSend` is relatively simple. The way that it's used requires the use of assembly code, however, which makes it more difficult to understand than it really needs to be. Additionally, the extreme performance demands and requisite optimizations mean that it's pretty dense and tricky assembly. However, by building a simple assembly trampoline and then reimplementing the logic in C, we can see just how it works, and there really isn't all that much to it.

This should be obvious, but never ship your own `objc_msgSend` in your own app. You'll break stuff and you'll be sorry. Do this for educational purposes only.

That's it for today's hallucinatory, assembly-soaked article. Come back next time for more fun, games, and hacking. As I've said roughly one thousand times by now, but can't help but reminding you, Friday Q&A is driven by reader suggestions. If you have a topic that you'd like to see me write about, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
