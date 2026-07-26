---
title: 'Last time on Friday Q&A'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2d9b330fce386d90'
translated: false
---

> 原文：[Last time on Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html)　·　mikeash.com Friday Q&A

Posted at 2013-03-08 14:33 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2013-03-22: Let's Build NSInvocation, Part II](https://www.mikeash.com/pyblog/friday-qa-2013-03-22-lets-build-nsinvocation-part-ii.html)  
Previous article: [Friday Q&A 2013-02-22: Let's Build UITableView](https://www.mikeash.com/pyblog/friday-qa-2013-02-22-lets-build-uitableview.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-03-08: Let's Build NSInvocation, Part I

by [Mike Ash](https://www.mikeash.com/)

**Code**  
The code for `MAInvocation` is available on GitHub here:

[https://github.com/mikeash/MAInvocation](https://github.com/mikeash/MAInvocation)

**Overview**  
An `NSInvocation` object represents a single method invocation. A method invocation has a target, a selector, a set of arguments, and a return value.

Just holding these values would be pretty boring. You can whip up a model class pretty easily to do that. Have a variable for the return value, an array for the arguments, and you're done. (The target and selector are just the first and second arguments.) Where `NSInvocation` gets interesting is in its ability to actually capture and send the invocations that it represents.

An `NSInvocation` can be _invoked_ on a particular object. This does the equivalent of code like `[target message: argument]`, except that the target, the message, and the arguments are all determined entirely at runtime. The `NSInvocation` can be constructed in code using runtime introspection without knowing anything about the method ahead of time.

Furthermore, an `NSInvocation` can be constructed _from_ an attempted message send. If you write `[target message: argument]`, and `target` doesn't actually implement `message:`, then it gets a `forwardInvocation:` call, which is given an `NSInvocation *` representing the invocation. It can then do whatever it wishes with that invocation, such as invoking it on another object, fiddling with the parameters, or setting an arbitrary return value which is passed back to the caller.

`NSInvocation` therefore has two complementary pieces of tricky business:

1. Code that's able to take a set of arguments, use them to make a method call, and collect the return value.
2. Code that's able to receive a method call, collect the arguments, then return an arbitrary return value to the caller.

Both pieces require extensive knowlede of the CPU architecture's calling conventions encoded in the implementation, as well as assembly language glue code.

**Calling Conventions**  
Because so much architecture-specific code is needed, I decided to focus on a single architecture. `x86-64` is the most convenient one to use for us Mac types. To further simplify things, I decided not to support floating-point arguments or return values, and also gave up on `struct` arguments, although I did implement support for `struct` return values. The following discussion ignores those parts that I didn't implement.

In order to implement even this limited `MAInvocation`, it's necessary to understand the relevant parts of the `x86-64` function calling conventions, and in order to understand that, you must first understand at least a bit of the `x86-64` architecture in general.

The `x86-64` architecture is a 64-bit extension of Intel's 32-bit `x86` architecture introduced with the 386 CPU. That is in turn an extension of the Intel 8086's 16-bit architecture which is in turn heavily based on the 8-bit architecture of the Intel 8080, generally considered to be the first microprocessor worth building a computer around. It could address a whopping 64kB of RAM, just enough to hold one medium-sized app icon these days.

There are sixteen general-purpose registers: `rax`, `rbx`, `rcx`, `rdx`, `rbp`, `rsp`, `rsi`, `rdi`, `r8`, `r9`, `r10`, `r11`, `r12`, `r13`, `r14`, and `r15`. The first half are all inherited from Intel's 32-bit architecture, while the second half are new additions for `x86-64`. Each register holds 64 bits.

Pointers and integers are treated identically when it comes to these calling conventions. Both are simply 64-bit quantities. Smaller integers are extended to 64 bits in size.

When calling a function, the first six parameters are passed by filling these registers in order: `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`. Additional arguments, if any, are passed on the stack as 64-bit quantities, so subsequent parameters can be found in memory at `rsp`, `rsp + 8`, `rsp + 16`, etc.

If the function returns a value, that value is returned by storing it in `rax`. If the function returns two values, such as when returning a struct like `NSRange` that contains two values, `rdx` is used for the second one. If the function returns a larger struct, this is handled by having the caller allocate enough memory to hold it, and then a pointer to that memory is passed as an implicit first argument to the function in `rdi`, with all of the explicit parameters moved down by one.

Note that, for Objective-C methods, the first two parameters are `self` and `_cmd`, which are therefore passed in `rdi` and `rsi` (or, if the method returns a larger struct, in `rsi` and `rdx`). The explicit parameters, if any, come after those two.

As far as I know, there's no particular fundamental reason for the number of registers used to pass parameters, or which ones are used. Calling conventions are a tradeoff between placing a burden on the caller, placing a burden on the callee, making parameter passing more efficient, and making surrounding code more efficient. These conventions presumably sit near some reasonable compromise between all of the competing desires.

In order to make a function call, `MAInvocation` needs to take the parameters to the function, place the first six in the appropriate registers, place any additional ones on the stack, then needs to actually jump to the function's address. Upon return, it needs to record the values in the two return-value registers.

In order to receive a function call, `MAInvocation` needs to record the values of the six parameter-passing registers, as well as the location of the stack pointer, and use these to extract the argument values. Upon returning, it needs to place the desired return values into the two return-value registers. The logic of which values go into registers and the stack can be written in Objective-C, but the code that actually manipulates the registers and the stack needs to be written in assembly.

**Data Structure**  
In order to cleanly communicate between the Objective-C and assembly code, I defined a `struct` that contains all of the relevant code. When making a call, `MAInvocation` will fill out the `struct` as appropriate, then invoke the assembly language glue code. When receiving a call, the assembly language glue code will construct the `struct` from the current state, then pass it over to the Objective-C code. Not all fields will be useful in both situations, but it's easier to use the same `struct` for everything rather than try to specialize.

The first thing this `struct` contains is the address of the function to call:

```
    struct RawArguments
    {
        void *fptr;
```

Next, it stores the values of the six 64-bit parameter-passing registers:

```
        uint64_t rdi;
        uint64_t rsi;
        uint64_t rdx;
        uint64_t rcx;
        uint64_t r8;
        uint64_t r9;
```

It then stores the address of the arguments passed on the stack, as well as how many stack arguments there are:

```
        uint64_t stackArgsCount;
        uint64_t *stackArgs;
```

After that, it stores the two return-value registers:

```
        uint64_t rax_ret;
        uint64_t rdx_ret;
```

`rdx` already exists in the parameter-passing section, but it's easier to make a separate entry for return values than to reuse that field.

Finally, it keeps a flag that records whether or not the call uses `struct` return conventions, i.e. whether the `rdi` is used to store a pointer to space allocated for the return value. In Objective-C runtime terminology, such calls are called `stret`, short for "`struct` return":

```
        uint64_t isStretCall;
    };
```

"Struct return" is something of a misnomer, since small structs are returned in registers, but that's how it is. When you see "struct return" or "stret", think "sufficiently large struct return".

**Function Call Glue**  
The function call glue is a function with this C signature:

```
    void MAInvocationCall(struct RawArguments *);
```

It is implemented in assembly, but with the above prototype, the Objective-C code can call it as if it were a C function. It will pass a filled-out `struct RawArguments` and the assembly glue will make the call.

The assembly code first declares the symbol. It's marked as global so it's accessible from other parts of the program. The leading underscore is due to ancient history involving Fortran, and every C symbol implicitly gets one. A non-C symbol that expects to be accessible from C code needs to have it as well:

```
    .globl _MAInvocationCall
    _MAInvocationCall:
```

The first thing any well-behaved `x86-64` function is save the old frame pointer (stored in `rbp`) and set up a new one by copying the stack pointer over:

```
    pushq %rbp
    movq %rsp, %rbp
```

I'll use `r12` through `r15` in the following code. These registers are designated as callee-saved by the platform calling conventions, meaning that we're not allowed to just obliterate their contents. Instead, we save their values onto the stack so they can be restored later:

```
    pushq %r12
    pushq %r13
    pushq %r14
    pushq %r15
```

The `struct RawArguments *` parameter is stored in `rdi`. It's the first parameter to the function, and the calling conventions state that the first parameter is passed it `rdi`. We need to use `rdi` for the first parameter to the function being called, so we save the current value into `r12`. The various elements of the `struct RawArguments` parameter can be accessed by loading various offsets from `r12`:

```
    mov %rdi, %r12
```

Now it's ready to start copying arguments where they need to go. Because this requires manipulating the stack pointer, it copies the stack pointer into `r15` so it's easy to restore later:

```
    mov %rsp, %r15
```

Stack arguments get copied first, for no particular reason. It does make the code to copy them slightly easier to write, as it can use the argument-passing registers as scratch space, since they don't contain anything important. The first thing it does is load the number of stack arguments, which is located at offset `56` in the `struct Rawarguments`:

```
    movq 56(%r12), %r10
```

If you're wondering where `56` comes from, each member in this struct is `8` bytes, and the number of stack arguments is the 8th element in the struct, meaning that it comes after space for `7` other elements. `7 * 8 = 56`. All the offsets in this code are computed in the same way.

`r10` now contains the number of stack arguments that need to be copied. Next, it computes the amount of stack space needed for these arguments. This is equal to the number of arguments multiplied by 8 (each argument is 64 bits, or 8 bytes). It does this by copying the number of arguments into `r11`, then shifting it left by three bits, which is equivalent to multiplying by 8:

```
    movq %r10, %r11
    shlq $3, %r11
```

Next, it loads the stack argument pointer from offset `64` in the `struct RawArguments` into `r13`:

```
    movq 64(%r12), %r13
```

Let's take a moment to recap what the temporary registers contain at the moment:

- `r10`: the number of stack arguments to copy.
- `r11`: the number of bytes needed for stack arguments.
- `r13`: the stack argument pointer.

We don't get to give things convenient names in assembly, so it's essential to keep careful track of what contains what at any given moment.

The next step is to move the stack pointer down to make room for the arguments, which is done by subtracting `r11` from the stack pointer:

```
    subq %r11, %rsp
```

The stack is also required to be 16-byte aligned before making a function call, and this is done by just doing a logical AND with a value that has the bottom four bits cleared:

```
    andq $-0x10, %rsp
```

The stage is now set. At this point, we just execute a simple memory copy loop. The equivalent C code would be:

```
    for(int i = 0; i != r10; i++)
        rsp[i] = r13[i];
```

`r14` will serve as the loop counter. The first step is to initialize it to zero:

```
    movq $0, %r14
```

The top of the loop needs a label so that later code can easily jump back to it:

```
    stackargs_loop:
```

Next comes the check for `r14 != r10`:

```
    cmpq %r14, %r10
    je done
```

The `cmp` instruction compares the two registers and sets the contents of the `FLAGS` register accordingly. The `je` instruction then jumps to the `done` label if the `FLAGS` register indicats that the two are equal. This two-stage construct is a bit odd, but it's how `x86-64` works.

If the two aren't equal, the loop continues. The next step is to copy the current argument. This is done in two stages. First, the argument is copied from the memory pointed to by `r13` into a temporary register, in this case `rdi`. Next, the argument is copied from `rdi` into the memory pointed to by `rsp`:

```
    movq 0(%r13, %r14, 8), %rdi
    movq %rdi, 0(%rsp, %r14, 8)
```

The parenthetical expressions are a little scary. `x86-64` allows memory references with a bunch of different components, which makes it easier to do computed array dereferences like this. The general form of the expression looks like:

```
    offset(%r1, %r2, elementSize)
```

This refers to this address:

```
    r1 + r2 * elementSize + offset
```

This can be thought of as an array dereference. `r1` is the array pointer, `r2` is the index, `elementSize` is the size of each element in the array, and `offset` is just a final fixup to apply to the whole result. In short, `0(%r13, %r14, 8)` is equivalent to `((uint64_t *)r13)[r14]`.

After that comes the `i++`, which has a simple assembly equivalent:

```
    inc %r14
```

Finally, a jump back to `stackargs_loop` completes the loop, with the `done` label following it so that execution resumes below once the loop exits:

```
    jmp stackargs_loop

    done:
```

The stack arguments are now ready to go. All that remains is to copy the register arguments into their actual registers. This is done by writing a sequence of move instructions:

```
    movq 8(%r12), %rdi
    movq 16(%r12), %rsi
    movq 24(%r12), %rdx
    movq 32(%r12), %rcx
    movq 40(%r12), %r8
    movq 48(%r12), %r9
```

With everything ready, it's time to call the target function. The function pointer is conveniently located right at the location pointed to by `r12`, since it's the first element in the `struct RawArguments`. This instruction makes the call:

```
    callq *(%r12)
```

Once the call returns, the return value (if any) is found in `rax` and `rdx`. The code immediately copies the contents of these registers into the `struct RawArguments`:

```
    movq %rax, 72(%r12)
    movq %rdx, 80(%r12)
```

It's just about done. The only thing that needs to be done, aside from returning, is to restore the values stored in `r12`-`r15` to whatever the caller had in them. First, the stack pointer needs to be restored to what it was after those registers were pushed onto the stack:

```
    mov %r15, %rsp
```

Then they're popped off in the opposite order from which they were pushed:

```
    popq %r15
    popq %r14
    popq %r13
    popq %r12
```

Finally, control is returned to the caller, using a magic combination of instructions which readjust the stack and frame pointer before jumping to the caller's address:

```
    leave
    ret
```

That takes care of the glue code for function calls. The Objective-C code can now fill out a `struct RawArguments` to suit the call being made, then call `MAInvocationCall` and pass the pointer to the `struct` to make the call.

**Forwarding Glue**  
Capturing a method invocation is called "forwarding" in Objective-C. The runtime has a special forwarding handler, which is called any time an implementation can't be found for a particular selector. In fact, there are two different forwarding handlers: one for normal calls, and one for `stret` calls. The forwarding handler needs to know where to find the `self` and `_cmd` parameters, and the locations of those parameters change for a `stret` call, so a bit of specialization is required.

The strategy here is to have two entry points that call through to a common implementation after making a note of whether or not it's a `stret` call. The common implementation then fills out a new `struct RawArguments` accordingly and calls into an Objective-C function. Once that function returns, it copies the return value back out into the return value registers, then returns.

The `r10` register doesn't contain anything in particular when a function is called, but neither is it required to save the value. This makes it a good spot to store the `stret` flag temporarily. The normal forwarding handler will set it to `0` before jumping to the common implementation, and the `stret` handler will set it to `1`. Here's the normal handler in its entirety:

```
    .globl _MAInvocationForward
    _MAInvocationForward:
    movq $0, %r10
    jmp _MAInvocationForwardCommon
```

The `stret` handler is nearly identical:

```
    .globl _MAInvocationForwardStret
    _MAInvocationForwardStret:
    movq $1, %r10
    jmp _MAInvocationForwardCommon
```

All the interesting stuff happens in the common handler:

```
    .globl _MAInvocationForwardCommon
    _MAInvocationForwardCommon:
```

The first thing it does is calculate the location of the stack arguments passed in to the function. The stack arguments start at `rsp + 8` from the callee's point of view. The `call` instruction issued by the caller pushes the return address onto the stack, which is why stack arguments start right at `rsp` from that side of things, but not here. `r11` is another convenient register that neither contains anything useful nor needs to be saved, so the code computes the address in that register:

```
    movq %rsp, %r11
    addq $8, %r11
```

Then the function performs the standard prologue of setting up the frame pointer:

```
    pushq %rbp
    movq %rsp, %rbp
```

Now it's finally time to construct the `struct RawArguments`. This is done by pushing values onto the stack. First, a quick recap of what the various register contain right now:

- `r10`: the `isStretCall` flag.
- `r11`: the pointer to the stack arguments.
- `rdi-r9`: register arguments.

The handler uses the `pushq` instruction to construct the `struct` on the stack. Because it's pushing onto the stack, it needs to push everything in reverse order. Because `isStretCall` is the last thing in the `struct`, it's the first thing to be pushed:

```
    pushq %r10
```

The return value registers don't need to contain anything in particular, so it makes space for them by pushing zero twice:

```
    pushq $0
    pushq $0
```

Next comes the `stackArgs` pointer, whose value is currently in `r11`:

```
    pushq %r11
```

After that comes the number of stack arguments. This is not currently known, so the handle just pushes a zero to make room for it. That field will be filled out by the Objective-C code:

```
    pushq $0
```

Next come the argument registers, which are pushed in reverse order:

```
    pushq %r9
    pushq %r8
    pushq %rcx
    pushq %rdx
    pushq %rsi
    pushq %rdi
```

The very first field of the `struct` is the function pointer. That's not used here, so another zero is pushed to make room for it:

```
    pushq $0
```

At this point, `rsp` now contains a pointer to the newly-built `struct RawArguments`. The goal is to call a C function with this prototype:

```
    void MAInvocationForwardC(struct RawArguments *r);
```

The pointer to the `struct` is its only parameter, so that address needs to be moved to `rdi`, where the first parameter is passed:

```
    movq %rsp, %rdi
```

The handler needs to consult the `struct` afterwards to extract the return value registers. Since `rdi` isn't saved across the function call, and `rsp` may be changed when aligning the stack for the call, the handler also copies the address into `r12` so it can be used afterwards:

```
    movq %rdi, %r12
```

It's now time to align the stack and call into Objective-C:

```
    andq $-0x10, %rsp
    callq _MAInvocationForwardC
```

The Objective-C code will now construct an `MAInvocation` instance and invoke the object's `forwardInvocation:` method.

Once control returns, the return value, if any, is found in the `struct`. To make them visible to the caller, that value is copied out of the `struct` and into the appropriate registers:

```
    movq 72(%r12), %rax
    movq 80(%r12), %rdx
```

That's it! Return to the caller:

```
    leave
    ret
```

The Objective-C runtime's forward handlers are, amazingly, configurable. To set them to this code, all you have to do is call this somewhere convenient:

```
    objc_setForwardHandler(MAInvocationForward, MAInvocationForwardStret);
```

The runtime will then use these forward handlers for all unimplemented selectors.

**Conclusion**  
That wraps up the assembly language glue code and the basic knowledge of calling conventions. Much work remains, but the two glue functions here provide the necessary foundation that the Objective-C parts of `MAInvocation` can be built on. `MAInvocation` needs to manage a `struct RawArguments` and translate between the contents of that `struct` and the arguments and return values provided and requested by the clients of the API. To make a method call, it needs to arrange the `struct` properly, then call into the above glue code. To receive a method call, it needs to construct a new `MAInvocation` from the `struct` contents.

All this shall be covered next time. Until then, please [send in your ideas](mailto:mike@mikeash.com) for topics to cover on Friday Q&A. The next article may be spoken for, but your suggestions for the future are always welcome.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

No comments have been posted.

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
