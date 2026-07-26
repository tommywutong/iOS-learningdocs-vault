---
title: 'Friday Q&A 2011-12-23: Disassembling the Assembly, Part 2'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0e686c9a794bec43'
translated: false
---

> 原文：[Friday Q&A 2011-12-23: Disassembling the Assembly, Part 2](https://www.mikeash.com/pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html)　·　mikeash.com Friday Q&A

Posted at 2011-12-23 20:48 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-12-30: Disassembling the Assembly, Part 3: ARM edition](https://www.mikeash.com/pyblog/friday-qa-2011-12-30-disassembling-the-assembly-part-3-arm-edition.html)  
Previous article: [Friday Q&A 2011-12-16: Disassembling the Assembly, Part 1](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [disassembly](https://www.mikeash.com/pyblog/?tag=disassembly) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-12-23: Disassembling the Assembly, Part 2

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

In [last week's article](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html), I discussed the x86_64 architecture and the disassembly of the `main` function of Mike's example code. This is part 2, in which I look at the differences in optimized code, disassembly of the rest of the sample code, the `start` runtime function, and some functions that work with floating-point values. If you haven't yet read part 1, I strongly recommend it, since otherwise part 2 won't make much sense.

**Optimization**  
In part 1, I purposely examined the unoptimized version of the assembly language produced by the compiler, under the theory that optimization would obscure the finer details of how the code works at the assembler level. Now it's time to see what optimized code looks like. Here's `main` in assembly again, this time compiled with `-Os`:

```
    _main:
        pushq   %rbp
        movq    %rsp, %rbp
        pushq   %r15
        pushq   %r14
        pushq   %r12
        pushq   %rbx
        callq   _objc_autoreleasePoolPush
        movq    %rax, %r14
        movq    L_OBJC_CLASSLIST_REFERENCES_$_(%rip), %rdi
        leaq    l_objc_msgSend_fixup_alloc(%rip), %rsi
        callq   *l_objc_msgSend_fixup_alloc(%rip)
        movq    L_OBJC_SELECTOR_REFERENCES_27(%rip), %rsi
        leaq    L__unnamed_cfstring_26(%rip), %rdx
        movq    _objc_msgSend@GOTPCREL(%rip), %rbx
        movq    %rax, %rdi
        movl    $42, %ecx
        callq   *%rbx
        movq    %rax, %r15
        movq    L_OBJC_SELECTOR_REFERENCES_28(%rip), %rsi
        movq    %r15, %rdi
        callq   *%rbx
        movq    %rax, %rdi
        callq   _objc_retainAutoreleasedReturnValue
        movq    %rax, %rbx
        movq    %rbx, %rdi
        callq   _MyFunction
        movq    %rax, %rdi
        callq   _objc_retainAutoreleasedReturnValue
        movq    %rax, %r12
        movq    %rbx, %rdi
        callq   _objc_release
        leaq    L__unnamed_cfstring_23(%rip), %rdi
        movq    %r12, %rsi
        xorb    %al, %al
        callq   _NSLog
        movq    %r12, %rdi
        callq   _objc_release
        movq    %r15, %rdi
        callq   _objc_release
        movq    %r14, %rdi
        callq   _objc_autoreleasePoolPop
        xorl    %eax, %eax
        popq    %rbx
        popq    %r12
        popq    %r14
        popq    %r15
        popq    %rbp
        ret
```

The unoptimized version of `main` was 60 lines; this optimized code is only 49. The compiler managed to save 11 instructions. Expecting more is unreasonable; optimization, even when done for size savings, tends to be more concerned with making efficient use of the CPU and its abilities than using the absolute minimum number of instructions. On almost any modern processor, there is hugely more benefit in using a few extra simple instructions versus fewer instructions that are more complicated. Compiling with `-O3`, which optimizes heavily for speed over size, actually _increases_ the code size to 65 instructions, mostly due to inlining.

Because I've already explained the meaning of all of the individual instructions involved (with one exception), in this breakdown I'll look purely at groups of instructions and how the compiler has optimized each section.

1. ```
      pushq %rbp
      movq %rsp, %rbp
  ```

  Look familiar? It should; this is exactly the same instruction sequence `main` started with before. Nothing's changed about the code which sets up the stack pointer; the stack frame has to be set up in a particular way and this is it (more on this later).
2. ```
      pushq   %r15
      pushq   %r14
      pushq   %r12
      pushq   %rbx
  ```

  Instead of a bunch of values being stored to the stack, the optimizer has chosen to save the values of several registers to the stack so they can be used as scratch space during the function. The x86_64 ABI specifies which registers are preserved across function calls and which can be freely used as scratch, and none of these are freely usable. Since registers are potentially thousands of times faster than the stack in some cases - in fact, the delay can stretch into the space of seconds if the stack happened to be paged out to disk! - it's certain to be a win to use the stack once at the beginning and once at the end, and manipulate data in registers during the function's execution.
3. ```
      callq   _objc_autoreleasePoolPush
      movq    %rax, %r14
  ```

  `objc_autoreleasePoolPush` takes no arguments and returns a simple integer value in `rax`. The optimizer saves the return value in `r14` instead of spilling it to the stack.
4. ```
      movq    L_OBJC_CLASSLIST_REFERENCES_$_(%rip), %rdi
      leaq    l_objc_msgSend_fixup_alloc(%rip), %rsi
      callq   *l_objc_msgSend_fixup_alloc(%rip)
  ```

  Load the `MyClass` class object into `rdi`, load the address of `l_objc_msgSend_fixup_alloc` into `rsi`, and call the function. It's much the same sequence as the unoptimized code, but without the stack use and all in one place.
5. ```
      movq    L_OBJC_SELECTOR_REFERENCES_27(%rip), %rsi
      leaq    L__unnamed_cfstring_26(%rip), %rdx
      movq    _objc_msgSend@GOTPCREL(%rip), %rbx
      movq    %rax, %rdi
      movl    $42, %ecx
      callq   *%rbx
      movq    %rax, %r15
  ```

  Load the `[MyClass initWithName:number:]` selector into `rsi`, load `@"name"` into `rdx`, load the address of `objc_msgSend@GOTPCREL` into `rbx`, load the return value from `alloc` into `rdi`, load `42` into `ecx`, call `objc_msgSend@GOTPCREL`, and save the return value (i.e. `obj`) in `r15`.

  `objc_msgSend@GOTPCREL`? What in the world is that thing? Well, as it turns out, it's more than meets the eye. If you peek at the generated machine code with a disassembler, it turns out to not be a `mov` instruction at all, but rather a `lea`! `GOTPCREL` is a directive which allows the `rip`-relative address of a function to be inserted at link time so a direct call can be made, if that address can be calculated at link time. `objc_msgSend` is one of the functions for which this is true, and optimization lets the compiler make the attempt.

  In other words, when optimization is on, the compiler generates code that makes a short, fast call to the function instead of making it go through the slower dynamic library call, potentially a "far jump" (a branch over a long distance of code, which, by necessity, is much slower).

  _Note: I'm not 100% sure of my facts on this one; I'd appreciate any insight anyone has on the specifics of `@GOTPCREL`._
6. ```
      movq    L_OBJC_SELECTOR_REFERENCES_28(%rip), %rsi
      movq    %r15, %rdi
      callq   *%rbx
  ```

  Load the `name` selector into `rsi`, load `obj` from `r15` into `rdi`, and call `objc_msgSend` again. This is a case where optimization really begins to show its use. The unoptimized version of this call saved and loaded to and from the stack and other registers, effectively redoing the entire setup for the second message send. The optimizer recognizes that the extra data copying is redundant and just loads everything directly - and even more importantly, avoids loading data that's already in a register into it _again_.
7. ```
      movq    %rax, %rdi
      callq   _objc_retainAutoreleasedReturnValue
  ```

  Grab the return value from the last message send and immediately pass it to `objc_retainAutoreleasedReturnValue`. This is the same sequence as the unoptimized code. In fact, in the Objective-C runtime, certain operations work differently based specifically on the existence of these exact two instructions.
8. ```
      movq    %rax, %rbx
      movq    %rbx, %rdi
      callq   _MyFunction
      movq    %rax, %rdi
      callq   _objc_retainAutoreleasedReturnValue
      movq    %rax, %r12
  ```

  Call `MyFunction(name)`, retain its return value, and save the result in `r12`. The extra store to `rbx` looks redundant, but it isn't, as we'll see futher down.
9. ```
      movq    %rbx, %rdi
      callq   _objc_release
  ```

  See? Both `rax` and `rdi` have already been reused since `[MyClass name]`'s return value was saved off in `rbx`. Not redundant after all!

  "But why didn't the compiler just leave it in `rbx` to begin with?" Remember that the first parameter to a function _must_ be in `rdi`. The value had to be saved somewhere that wasn't about to be overwritten by the very next thing done.
10. ```
      leaq    L__unnamed_cfstring_23(%rip), %rdi
      movq    %r12, %rsi
      xorb    %al, %al
      callq   _NSLog
  ```

  Call `NSLog(@"%@", return value of MyFunction)` with no vector registers used - remember that variadic functions require the number of vector registers used as parameters to be in `al`. Nothing special here.
11. ```
      movq    %r12, %rdi
      callq   _objc_release
      movq    %r15, %rdi
      callq   _objc_release
  ```

  Release both objects (return value of `MyFunction` and `obj`) that are no longer in use. Technically, `obj` was already unused at the time of `NSLog`, but ARC's code flow analysis isn't that aggressive; releases are done at the end of the enclosing scope, not the instant the value is no longer used.

  _Note: The return from `[MyClass name]` had an effective enclosing scope of the `MyFunction` call itself; it was never assigned to a variable (specifically, to a `__strong` variable), and therefore was not considered potentially "live" after the function call._
12. ```
      movq    %r14, %rdi
      callq   _objc_autoreleasePoolPop
      xorl    %eax, %eax
      popq    %rbx
      popq    %r12
      popq    %r14
      popq    %r15
      popq    %rbp
      ret
  ```

  Pop the autorelease pool, set `eax` to zero as the return value of `main`, restore the saved registers, and return.

And that is `main` in optimized code. The major effects of optimization visible here are _much_ better utilization of registers; there's not a single use of the stack except for register saving, and there's not a single redundant or useless data copy anywhere to be found.

Do you think you can do better than the compiler did? It's possible that other optimization opportunities exist, but most of the ones that seem immediately obvious are actually prohibited by the CPU, the ABI, or the way Objective-C and ARC work.

_Hint: The push and pop of `rbp`, as well as the copy of `rsp` to `rbp`, are unnecessary, because the optimization removed all references to `rbp` in the function body! Without those three instructions, `main` would still work,_ but the debugger might not! _The debugger relies in some cases upon the presence of stack frames, which include a properly initialized base pointer register and the saved value of the base pointer on the stack. Certain other system functions can potentially rely upon presence of a stack frame, though these rarely come up in normal use. On OS X, the switch which tells GCC and Clang to skip the use of stack frames is disabled by default even at high optimization, suggesting that someone thought it wasn't worth saving three instructions per function. It probably isn't. The system frameworks are built with stack frames intact, for example. In general, you should always include stack frames unless you have a good reason not to._

**The MyFunction Function**  
Next, let's look at the `MyFunction` function:

```
    NSString *MyFunction(NSString *parameter)
    {
        NSString *string2 = [@"Prefix" stringByAppendingString: parameter];
        NSLog(@"%@", string2);
        return string2;
    }
```

I'm going to take this function backwards. Instead of looking directly at the assembler the compiler produced, I'll construct it myself using what we've already learned from `main` about how the compiler does its thing. This function doesn't do anything that `main` didn't, after all. For bonus points, we'll even insert the necessary ARC calls.

1. Function prologue:

  ```
      _MyFunction:
          pushq %rbp
          movq %rsp, %rbp
  ```

  Every C function has a prologue. See the discussion about stack frames above. This is the stack frame for our new function, along with its label, for completeness' sake. All C function names are prepended with an underscore at the assembler stage as a matter of language convention. A look at the name table of any executable or library will show that almost all of the symbols have at least one preceding underscore.
2. Save registers:

  ```
      pushq %rbx
  ```

  We'll only need one scratch register for this function, so let's use `rbx`.
3. Call `stringByAppendingString:`

  ```
      movq %rdi, %rdx
      leaq L_prefix_string_reference(%rip), %rdi
      movq L_stringByAppendingString__selector_reference(%rip), %rsi
      callq *_objc_msgSend@GOTPCREL(%rip)
      movq %rax, %rdi
      callq _objc_retainAutoreleasedReturnValue
  ```

  First, I make the assumption that the string `@"Prefix"` appears somewhere given the label `L_prefix_string_reference`, which I just made up. Label names are arbitrary; the compiler's very official-looking names are just autogenerated. Even having `L_` in front of them is just a convention I chose to follow to make it look more like the compiler's version. Likewise, I assume that `L_stringByAppendingString__selector_reference` points to the appropriate selector name. From there, I move `rdi` to `rdx`. Since `parameter`, being the first parameter to `MyFunction`, was in `rdi`, I've now made it the third parameter to whatever I'm about to call. I load `@"prefix"` as the first argument and the `-stringByAppendingString:` selector as the second, then call the `rip`-relative version of `objc_msgSend`. Finally, I take the return value and pass it to `objc_retainAutoreleasedReturnValue`, per ARC's requirements. ARC functions only at the Objective-C compiler level; in assembler, it has to be invoked manually, like normal retain-release code but with stricter rules.
4. Call `NSLog`:

  ```
      movq %rax, %rsi
      leaq L_format_string_reference(%rip), %rdi
      xorb %al, %al
      callq _NSLog
  ```

  I'll tell you right now that this code is wrong in one important respect: Because I know I'll need the return value from `-stringByAppendingString:` later, I've made the mistaken assumption that `rax` and `rsi` will not be changed by the call to `NSLog`. _However_, the x86_64 ABI explicitly specifies that both registers are **not** preserved across function calls. We've already clobbered them several times during the course of this code without saving them, so we can hardly expect `NSLog` not to do the same. (Not only that, but the code itself zeroes out the low byte of `rax` as part of the call sequence!) The value in `rax` and `rsi` before this section of code _must_ be preserved, or it will be lost during the call. _Note: Even if `NSLog` just so happened to preserve `rsi`, that's not an assumption the calling code can make safely. The_ only _time you can assume registers are preserved by a function outside the specification of the ABI is when you have written every line of that function yourself, in assembly language, and have documented the requirement so you don't violate it later on._ The solution is to replace the first `movq` with these two lines:

  ```
      movq %rax, %rbx
      movq %rbx, %rsi
  ```

  The value (known as `string2` in the original Objective-C source) is now saved in `rbx` so we can use it. This is why I saved `rbx` at the beginning of the function.
5. Return from the function:

  ```
      movq %rbx, %rdi
      popq %rbx
      popq %rbp
      jmp _objc_autoreleaseReturnValue ## TAIL CALL
  ```

  Whoa, whoa, wait, what's all this? What's a tail call?

  In ARC mode, an object returned from a function not annotated as `cf/ns_returns_retained` must be passed to `objc_autoreleaseReturnValue`. Therefore, that has to be the very last thing the function does before returning.

  "So," you ask, "why not `movq %rbx, %rdi`, then `callq _objc_autoreleaseReturnValue`, and let `rax` keep that return value while you `popq` and `ret`?" Answer: Because it's inefficient. When the very last thing a function does is return the _identically-typed_ result of calling another function, a _tail call_ can be used to save time, space, and effort. At the time of the first `movq` instruction, the stack looks something like this:

  ```
      +----------------+
      | RETURN ADDRESS | 16 <--- next instruction in main, pushed by `callq _MyFunction`
      |   Saved %rbp   | 8  <--- saved value of rbp, pushed by prologue
      |   Saved %rbx   | 0  <--- saved value of rbx, pushed by our code
      +----------------+
  ```

  If I were to simply `callq _objc_autreleaseReturnValue`, the stack would then look like this:

  ```
      +----------------+
      | RETURN ADDRESS | 24 <--- next instruction in main, pushed by `callq _MyFunction`
      |   Saved %rbp   | 16 <--- saved value of rbp, pushed by prologue
      |   Saved %rbx   | 8  <--- saved value of rbx, pushed by our code
      +----------------+
      | RETURN ADDRESS | 0  <---- next instruction in MyFunction, pushed by `callq _objc_autoreleaseReturnValue`
      +----------------+
  ```

  When `objc_autoreleaseReturnValue` returned, the stack would be popped by the `ret` instruction and go back to exactly where it was, and then the same thing would immediately happen again. Wouldn't it be more efficient if `objc_autoreleaseReturnValue` could return directly to `main`, since `MyFunction` has absolutely nothing left to do?

  This is what a tail call does. Instead of using `call`, which pushes a new return address to the stack, `MyFunction` restores the stack to having _only_ `main`'s return address, and then jumps directly to `objc_autoreleaseReturnValue`. The stack ends up looking like this:

  ```
      +----------------+
      | RETURN ADDRESS | 0  <---- next instruction in main, pushed by `callq _MyFunction`!
      +----------------+
  ```

  Now, when the `ret` in `objc_autoreleaseReturnValue` pops a return address off the stack into `rip`, it'll jump directly back to `main`, with `rax` containing the return value exactly as it should. We've saved a push, a pop, and less visibly, some extra work by the CPU. The `jmp` instruction is also potentially smaller than `callq` if it should happen that the target function is located nearby in memory.

  Tail calls may look like a minor optimization from the assembly language point of view, but the savings of an entire extra stack frame can make or break recursive algorithms. Also, `objc_msgSend` is fundamentally designed around the use of a tail call; Cocoa programs would probably be something like an order of magnitude slower without them, and can you imagine loading a program in the debugger and seeing `objc_msgSend` before _every single method call in the backtrace?_

If you look at Clang's version of the assembler code, it's almost exactly the same as ours! There are three exceptions:

- Clang, of course, names the string and selector references differently.
- Clang moves the parameters around in a slightly different order; this has no effect on the execution of the code.
- For no immediately apparent reason, Clang saves the value of `rax` on the stack, only to ignore that value entirely in the function epilogue. What's actually happening is that Clang is aligning the stack to a 16-byte boundary, as required by both SSE instructions in particular and Cocoa in general. This leads to a total of 32 bytes (an even multiple of 16) on the stack for the function: The return address for `main`, saved `rbp`, saved `rbx`, and saved `rax`. The requirement of stack alignment is sufficient to overcome the desire to save instructions; the code would be incorrect without that alignment, and probably crash the very next time `objc_msgSend` was called.

Here, then, is the final version of the function as we've written it, including an aligned stack:

Here's the entire listing in one chunk as we've written it:

```
    _MyFunction:
        pushq %rbp
        movq %rsp, %rbp
        pushq %rbx
        pushq %rax
        movq %rdi, %rdx
        leaq L_prefix_string_reference(%rip), %rdi
        movq L_stringByAppendingString__selector_reference(%rip), %rsi
        callq *_objc_msgSend@GOTPCREL(%rip)
        movq %rax, %rdi
        callq _objc_retainAutoreleasedReturnValue
        movq %rax, %rsi
        leaq L_format_string_reference(%rip), %rdi
        xorb %al, %al
        callq _NSLog
        movq %rax, %rbx
        movq %rbx, %rsi
        movq %rbx, %rdi
        addq $8, %rsp # ignore the saved rax
        popq %rbx
        popq %rbp
        jmp _objc_autoreleaseReturnValue ## TAIL CALL
```

**Simple Floating-Point**  
Next, I'll look at a new function as a simple example of dealing with non-integer values. Here is the Objective-C version:

```
    float MyFPFunction(float parameter)
    {
        float x = parameter + 0.5;

        x -= 0.3f;
        return x;
    }
```

The line in which I call it:

```
    NSLog(@"%f", MyFPFunction(1.0));
```

And here is the assembler Clang produces:

```
    LCPI7_0:
        .long   1056964608              ## float 5.000000e-01
    LCPI7_1:
        .long   3197737370              ## float -3.000000e-01
    _MyFPFunction:                          ## @MyFPFunction
        pushq   %rbp
        movq    %rsp, %rbp
        addss   LCPI7_0(%rip), %xmm0
        addss   LCPI7_1(%rip), %xmm0
        popq    %rbp
        ret
```

(I've omitted the assembler for the actual function call, as it turns out to be extremely difficult to get Clang to actually emit such assembly under optimizing compilation without just inlining the function, and the unoptimized version is different. The only interesting note there in any case is the setting of `al` to 1 for the `NSLog` call, as it uses a vector register.)

The function is extremely simple:

1. A standard prologue comes first.
2. Then, since the ABI specifies that the first floating-point value is passed in the first vector register, `xmm0`, the function operates directly on that register. The `addss` instruction, in simple terms, adds two floating-point values ("add signed single-precision"). The constants in the code, `0.5` and `-0.3` (subtracting `0.3` is the same as adding `-0.3`) are stored as data in the executable, since neither assembly language nor the actual machine code have a way to express floating-point immediate values. The values themselves are stored as IEEE-754 single-precision numbers. It just so happens that a floating-point return value is _also_ stored in the first vector register, so by operating directly on `xmm0`, the function has already done everything it needed to do.
3. Finally, a standard function epilogue.

Wasn't that simple? It turns out that the only thing you have to do to use floating-point values is switch to the 128-bit vector registers and the SSE1 instruction set. The old `mmx` and `st(n)` registers, along with the x87 instruction set, are obsolete. They're also inefficient in comparison to SSE1 operations.

**The C runtime**  
Some things are going on behind the scenes when you launch your program. Did you know that `main` isn't the first function the system calls?

That's right! Once `dyld` has finished setting up your process' memory space, it branches to the standard entry point, a function called `start` which is copied verbatim from the C runtime library (`libcrt`) into your executable. It's written in pure assembly and will not appear in Clang's assembler output, as it doesn't exist in your program until linking is done. Here's a look at it. I've borrowed the source code from Apple's website. Per the terms of the APSL under which the code is licensed, I've included the APSL license header in the code listing.

`dyld` sees the `LC_UNIXTHREAD` load command in your binary and sets up the CPU state accordingly for the new process. A quick glance at the output of `otool -l` tells us that the `rip` register is initialized to the load address of the `start` symbol in the binary image! Clever, no?

The `start` function consists of the following code:

```
    /*
     * Copyright (c) 1999-2008 Apple Inc. All rights reserved.
     *
     * @APPLE_LICENSE_HEADER_START@
     * 
     * Portions Copyright (c) 1999 Apple Computer, Inc.  All Rights
     * Reserved.  This file contains Original Code and/or Modifications of
     * Original Code as defined in and that are subject to the Apple Public
     * Source License Version 1.1 (the "License").  You may not use this file
     * except in compliance with the License.  Please obtain a copy of the
     * License at http://www.apple.com/publicsource and read it before using
     * this file.
     * 
     * The Original Code and all software distributed under the License are
     * distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, EITHER
     * EXPRESS OR IMPLIED, AND APPLE HEREBY DISCLAIMS ALL SUCH WARRANTIES,
     * INCLUDING WITHOUT LIMITATION, ANY WARRANTIES OF MERCHANTABILITY,
     * FITNESS FOR A PARTICULAR PURPOSE OR NON- INFRINGEMENT.  Please see the
     * License for the specific language governing rights and limitations
     * under the License.
     * 
     * @APPLE_LICENSE_HEADER_END@
     */
    start:  pushq   $0          # push a zero for debugger end of frames marker
            movq    %rsp,%rbp       # pointer to base of kernel frame
            andq    $-16,%rsp       # force SSE alignment
            movq    8(%rbp),%rdi        # put argc in %rdi
            leaq    16(%rbp),%rsi       # addr of arg[0], argv, into %rsi
            movl    %edi,%edx       # copy argc into %rdx
            addl    $1,%edx         # argc + 1 for zero word
            sall    $3,%edx         # * sizeof(char *)
            addq    %rsi,%rdx       # addr of env[0], envp, into %rdx
            movq    %rdx,%rcx
            jmp Lapple2
    Lapple: add $8,%rcx
    Lapple2:cmpq    $0,(%rcx)       # look for NULL ending env[] array
            jne Lapple          
            add $8,%rcx         # once found, next pointer is "apple" parameter now in %rcx
            call    _main
            movl    %eax,%edi       # pass result from main() to exit() 
            call    _exit           # need to use call to keep stack aligned
            hlt
```

`start` doesn't work like a C function, since it isn't one. It's intended specifically to transition from a bare-bones executable state to one that C (and Objective-C) can work in. Even the function prologue is unusual.

1. `pushq $0` - Push a zero on the stack. This is used by the debugger as a marker for 'end of stack frames', replacing the `pushq %rbp` in a normal function's prologue.
2. `movq %rsp,%rbp` - Grab hold of the stack pointer, since the stack is actually used in this function.
3. `andq $-16,%rsp` - Mask off the last four bits of the stack pointer. This aligns the initial stack to a 16-byte boundary, as SSE instructions and Cocoa in general require. It's probably an effective no-op, as the system will tend to give a properly aligned stack already, but the C runtime doesn't and can't make that assumption.
4. `movq 8(%rbp),%rdi` - The 'kernel frame' the comment mentions above is what exists on the stack when `dyld` calls `start`. The first (topmost) value is the familiar `argc` parameter to `main`. Putting it in `rdi` sets it up as the first argument for a function call.
5. `leaq 16(%rbp),%rsi` - The second value on the stack is `argv`, so it's now a second function parameter.
6. `movl %edi,%edx` - Grab the low 4 bytes of `argc` into `rdx`.
7. `addl $1,%edx` - Add 1 to the copy of `argc`
8. `sall $3,%edx` - Multiply the value by 8 (shifting left by 3 is equivalent). `edx` now contains the entire size in bytes of the `argv` array.
9. `addq %rsi,%rdx` - Add the address of `argv` to the calculated size, yielding a pointer to the end of `argv`. Why is this happening? On OS X, the little-used `envp` array passed as a third parameter to `main` occupies the space in memory immediately following `argv`. The third function parameter is now `envp`.
10. `movq %rdx,%rcx` - Now copy `envp` to the fourth function parameter.
11. ```
              jmp Lapple2
      Lapple: add $8,%rcx
      Lapple2:cmpq    $0,(%rcx)       # look for NULL ending env[] array
              jne Lapple
  ```

  These four lines constitute a simple loop which increases the value of `rcx` by 8 until the memory location it points to contains zero. In C terms, this would be `while (*((uint64_t *)rcx)++);`. The `jne` instruction means "jump if not equal", or equivalently, "jump if `ZF` is zero". `ZF` was set by the previous instruction, `cmp`, which says "set `rflags` based on the result of subtracting the two operands, discarding the result itself". This loop finds the end of the `NULL`-terminated `envp` array.
12. `addq $8,%rcx` - Skip to the next pointer after the end of `envp`, which is `exec_path`, the fourth argument to `main`, though it's little-known and even more little-used.
13. `callq _main` - Finally, call `main` itself.
14. `movl %eax,%edi` - Load `main`'s 4-byte return value as the first parameter to a function call.
15. `callq _exit` - Call the `exit(2)` function, passing it the value returned from `main`. `exit(2)` never returns, so no instructions following this one should ever be executed.
16. `hlt` - Just in case somehow execution gets here anyway, "halt" the CPU. `hlt` will cause a privilege violation exception if executed by non-kernel code, so it makes a fitting "you should not be here" epilogue. It's effectively the equivelant of "unreachable". On very old x86 processors, an application would call `hlt` to stop the CPU, but with all the other hardware in a modern computer that needs to be shut down properly, a single instruction is simply inadequate to the purpose. It wouldn't turn off the power, for example.

**Conclusion**  
There's no need to look at the rest of the sample code's disassembly; there's nothing in it that I haven't already explored elsewhere. If you can't make sense of it on your own by now, I've probably done a poor job of explaining! Therefore, I hereby mark the end of part 2.

I've gotten several requests since part 1 to explain these concepts in terms of the ARM architecture used by the iPhone and other iDevices. I haven't worked with ARM at this level before now, but I'm always willing to learn new things. So I've started studying the ARM architecture, and I'll be writing a part 3 to this series of articles based on what I learn and using the same sample code. Until then, good luck, and I hope you've enjoyed my work so far!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
