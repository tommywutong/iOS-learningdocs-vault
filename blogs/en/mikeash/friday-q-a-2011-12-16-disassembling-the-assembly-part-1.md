---
title: 'Friday Q&A 2011-12-16: Disassembling the Assembly, Part 1'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:84f4a29b1e594f86'
translated: false
---

> 原文：[Friday Q&A 2011-12-16: Disassembling the Assembly, Part 1](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html)　·　mikeash.com Friday Q&A

Posted at 2011-12-16 15:02 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-12-23: Disassembling the Assembly, Part 2](https://www.mikeash.com/pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html)  
Previous article: [Friday Q&A 2011-12-02: Object File Inspection Tools](https://www.mikeash.com/pyblog/friday-qa-2011-12-02-object-file-inspection-tools.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [disassembly](https://www.mikeash.com/pyblog/?tag=disassembly) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-12-16: Disassembling the Assembly, Part 1

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

In [the December 2 edition](https://www.mikeash.com/pyblog/friday-qa-2011-12-02-object-file-inspection-tools.html) of his Friday Q&A series, Michael Ash wrote about several tools for object file analysis, based around a simple piece of sample code which he ran through each tool for examples to show.

His article is lacking in only one respect: it doesn't go into detail about what the assembly language that these tools show actually means. It's just common sense that he didn't; it's an advanced and intricate topic, deserving of an article of its own. I decided to write that article.

**The Sample Code**  
I'll be using exactly the same code that Mike did, replicated here:

```
    // clang -framework Cocoa -fobjc-arc test.m

    #import <Cocoa/Cocoa.h>

    @interface MyClass : NSObject
    {
        NSString *_name;
        int _number;
    }

    - (id)initWithName: (NSString *)name number: (int)number;

    @property (strong) NSString *name;
    @property int number;

    @end

    @implementation MyClass

    @synthesize name = _name, number = _number;

    - (id)initWithName: (NSString *)name number: (int)number
    {
        if((self = [super init]))
        {
            _name = name;
            _number = number;
        }
        return self;
    }

    @end

    NSString *MyFunction(NSString *parameter)
    {
        NSString *string2 = [@"Prefix" stringByAppendingString: parameter];
        NSLog(@"%@", string2);
        return string2;
    }

    int main(int argc, char **argv)
    {
        @autoreleasepool
        {
            MyClass *obj = [[MyClass alloc] initWithName: @"name" number: 42];
            NSString *string = MyFunction([obj name]);
            NSLog(@"%@", string);
            return 0;
        }
    }
```

Some things to notice right away:

1. This code uses ARC.
2. Accordingly, this code is 64-bit only and requires a recent version of the Clang compiler.
3. " twice.

**A Crash Course in x86 Architecture**  
Before diving into the assembly language itself, here's a quick lesson in the basics of the x86_64 (aka AMD64) architecture. The official reference manuals can be found at [the AMD developer website](http://developer.amd.com/documentation/guides/Pages/default.aspx#manuals), and cover in extremely technical detail almost everything you'll ever need to know about the underlying workings of the CPU. Several gaps are filled in by the [AMD64 Application Binary Interface Specification](http://www.x86-64.org/documentation/abi-0.99.pdf), which defines the Application Binary Interface (ABI) for C and C++ programs running in 64-bit mode on an Intel processor. The AMD64 specifications document the running of the CPU itself, while the ABI spec defines the conventions used by programs running on the CPU.

Where possible, I will speak in general terms about x86_64 architecture. Very little about how programs work at this level is specific to Mac OS X. While the functions called by the Objective-C runtime are very much OS-specific, the assembly language instructions that call those functions follow the same specifications as any x86_64 system.

_Note: If you're already familiar with such concepts as virtual memory, the stack, the heap, and CPU registers, you can skip this entire section._

**A Model of Memory**  
First, we look at the memory model of the computer. The x86_64 architecture specifies a "flat, paged memory model", which in simple terms means that all of the physical memory is laid out as one enormous block, divided up evenly into equally-sized "pages" of a predefined size. Software running on the x86_64 architecture can address a maximum of 48 bits worth of physical memory; this is less than the 64 bits one might expect due to the fact that no shipping CPU actually supports that many address lines. Addresses are always 64 bits long, but the top 16 bits of a physical memory address are always zero. The x86_64 specification does not provide for any other use of those 16 bits, such as tagging; they are reserved for a time when future implementations have both the need and the capability of addressing more than 32 TB of physical RAM at a time.

x86_64 also requires the implementation to provide virtual memory and protected memory. This means that the OS can set up the system in such a way that every process it runs sees its own complete 64-bit address space (virtual memory), and _only_ its own (protected memory). The OS is responsible for ensuring that an application gets the memory it actually uses by the use of "paging". The CPU intercepts all memory accesses by userland processes ("virtual addresses") and translates them to physical addresses with the help of the OS. A more in-depth description of how virtual memory and paging work is beyond this article; for now, it's enough to understand that every application has its own individual 64-bit memory space and can't see any other process' space.

_Note: This is not the same as the "virtual memory" which you may be familiar with, using space on the computer's hard drive as extra RAM, though that kind of virtual memory (a "paging file", or "swap space") is implemented in part by use of the CPU's virtual memory system._

This enormous 64 bits worth of address space is divided up into two areas: The stack and the heap. The stack is an area set aside high in the address space (typically high, anyway; in practice it can be just about anywhere) for the use of subroutine calls and local variable storage. The stack always grows _downward_; as the amount of information on the stack increases, the address of the top of the stack _decreases_. On older systems with smaller memory models, it was possible for the stack to grow too far downward and collide with other areas, but while it's still technically possible for this to happen, other things would go wrong long before a heap collision (in particular, the stack would run off the edge of its allocated memory pages and cause a protection fault). The CPU has a few instructions specifically designed for manipulating the stack, though they often go unused in favor of more efficient methods in modern code. You can think of the stack as a moderately large chunk of memory allocated by the system at the launch of your program.

The heap effectively consists of every area of memory that is not the stack; memory from the heap is allocated at runtime by the system for the process' use. The heap contains the stack, in fact, though they are usually considered conceptually separate. All of your executable code is loaded into a section of the heap, as well as copies of any libraries your executable links to. _Note: These are not actually copies, as it would be ridiculously inefficient to copy every library for every loaded process, but it's easier to just think of them as copies until you have a good grasp of virtual memory._ Memory allocated by your process during its execution also comes from the heap.

**The CPU and Its Registers**  
The CPU is the chip that actually does all the work. It fetches, decodes, and executes an _instruction stream_; what this means in practical terms is you give it a bunch of machine code and it does what the code tells it. Machine code is a bunch of bytes generated from source code by a compiler. A human could build machine code by hand, but it would be an exceedingly arduous process, and it's rarely if ever worth the time to do with any computer made in the last thirty years or so. The intermediate step between source code and machine code is, of course, assembly language, and humans _do_ spend a lot of time working in assembly language for various reasons, mostly having to do with either things source code can't do or things compilers can't optimize as well as humans - yet.

_Note: In fact, most compilers work by compiling the source code from C or another high-level language to assembly language and then translating the assembly language to machine code (along with some other intermediate steps). However, you never see the assembly language unless you ask to._

A _register_ is an area of storage set aside inside the CPU itself for effectively instantaneous access. Registers serve a large variety of purposes. An x86_64 CPU has a set of at least 100 registers - whew! Fortunately, an application developer, even working in assembly language, rarely has to be concerned with more than about 20 of them at most. The majority of the registers (including the control, debug, table descriptor, performance, and machine-check registers, to name a few) are accessible only to kernel code. Most of the rest, such as the `mmx`, `xmm`, and `ymm` registers, are only used by vector code, and the `fpr` registers are only used for floating-point calculations (there are exceptions, but as a rule of thumb it's a safe starting point). In addition, only parts of the `rflags` register are ever used by application code.

One of the quirks of the x86 architecture, ever since the original 16-bit 8086 instruction set, is that many of the same registers can be addressed by different names which determine which _part_ of the register is being read or written. Most of the general-purpose registers can be addressed down to a single byte. For example, the `rax` (accumulator) register, the first 64-bit general-purpose register, can also be addressed as `eax` (the low 32 bits of `rax`), `ax` (the low 16 bits of `rax`), `ah` (the second lowest 8 bits of `rax`), and `al` (the low 8 bits of `rax`). This capability is useful for handling smaller data types - for example, to handle a signed 32-bit addition requires only a single `add` instruction based on 32-bit register names rather than several instructions designed to emulate 32-bit sign extension and integer overflow on 64-bit registers.

A register named `r*x` is 64 bits; `e*x` is 32 bits, `*x` is 16 bits, and `*h` or `*l` are 8 bits. For the `r8-r15` registers, these names are instead `rN` (64 bits), `rNd` (32 bits), `rNw` (16 bits), and `rNb` (8 bits). `rip` and `rflags` can only be accessed as 64-bit registers, and the 8-bit versions of `rsi`, `rdi`, `rsp`, and `rbp` are named `sil`, `dil`, `spl`, and `bpl`.

The registers that a userland process _is_ concerned with on a regular basis are:

- - These are general-purpose registers, used for just about anything at any given moment, though the ABI locks these down to considerably more specific purposes. These registers can also be called the accumulator (

  ), the base register (

  ), the count register (

  ), and the data register (

  ).
- - These are technically index registers ('source index' and 'destination index'), but in modern code they are typically used as general purpose registers, within the specification of the ABI.
- - The "base pointer" and "stack pointer" registers. These are used for accessing the stack; the CPU's stack instructions will always assume that

  holds the address of the top of the stack.
- - The flags register, holding a long list of flags indicating the results of calculations done by instructions. The flags register can not be directly addressed. Operations affected by CPU flags are generally part of the instructions themselves; for instance, conditional jump instructions work differently depending on the current flags, and arithmetic operations change the flags. Certain instructions affect the flags directly, such as

  and

  , which respectively set and clear the Carry Flag. It is also possible to read the flags register directly by pushing it to the stack and write to it directly by popping from the stack into it. The flags a userland process can affect are:

    - - Carry Flag.

      is set when the result of an addition is a carry or the result of a subtraction is a borrow. It is also affected by arithmetic bit shifting instructions and bit test instructions, cleared by bitwise logic instructions, and manipulated directly by the

      ,

      , and

      instructions.
    - - Parity Flag.

      is set when there are an even number of 1 bits in the low byte of the last result of some operations. It can be used for parity checks.
    - - Auxiliary Carry Flag.

      is set when an arithmetic or BCD operation generates a carry or borrow from bit 3 of the result. Its use is limited to doing decimal math directly on the CPU, and it sees little use.
    - - Zero Flag.

      is

      when the last arithmetic operation had a result of zero. Compare and test instructions also set or clear

      appropriately. It is often used as for equality testing, as it is set when comparing two equal operands.
    - - Sign Flag.

      is set if the last arithmetic operation had a negative result. More exactly, after an arithmetic operation,

      is set to the value of the highest significant bit of the result.
    - - Direction Flag.

      is used to control whether the string instructions increment or decrement

      and

      during their operation, and can be manipulated by the

      and

      instructions. This flag is rarely used in modern code, as the string instructions see little use.
    - - Overflow Flag.

      is set when the sign of the result of the last signed arithmetic operation is different from the signs of both source operands. This means that the result was too big or too small to hold in the destination.
- - The instruction pointer register. This holds the memory address of the instruction currently being executed by the CPU.

  can be addressed directly in x86_64, but only for use as a memory offset. To write to

  , one must execute one of the many control transfer instructions. As instructions are executed,

  increases by the size of each one (instructions are of very variable size in the x86 architectures), with the exception of control transfer instructions, which work by changing the value of

  according to the transfer target.

**Calling Conventions**  
The calling conventions of an architecture, which are typically what people mean when they say ABI, specify the ways that functions receive parameters, return values, manage the stack, and other fundamentals not already part of the CPU architecture. x86_64's calling conventions are somewhat complicated, so I'll include an abbreviated version here which will get you through all of the sample code.

Conveniently, none of the functions in the sample code take non-integer parameters, or any large number of parameters. At this point, one might immediately protest that `char **`, `NSString *`, and `id` certainly are **not** integers! However, for the purpose of function parameter passing, an integer is a value that fits within the bit width of the architecture, i.e. 64 bits for x86_64. Pointers are exactly that size, while `int` is smaller (x86_64 is an LP64 architecture, which means that `long` is 64 bits, but `int` is 32).

Integer parameters to functions are passed via a series of registers. The first parameter goes in `rdi`. The second goes in `rsi`, the third in `rdx`, then `rcx`, `r8`, and `r9`, in that order. If there are more integer arguments than that, the remainder are pushed onto the stack in right-to-left (reverse) order.

Apart from that, the only quirk of the calling conventions we need to be concerned with for this code is the sequence for variadic functions. A variadic function is one which uses the `stdarg` interface to take a variable number of parameters. In this case, `NSLog` is the culprit. There's only one oddity in how variadic functions take parameters, at least at the assembly language level: The byte value of `al` (the low 8 bits of `rax`) is used to specify the number of vector registers used to pass arguments to the function. Since no vector registers are used by our sample code, this number is always zero.

Finally, functions return simple integer values (again, remember that for these purposes, a pointer is an integer value) in `rax`, or in some rarer cases, `rdx`.

The complete calling conventions are considerably more complicated; if you're curious, have a look at the [AMD64 Application Binary Interface Specification](http://www.x86-64.org/documentation/abi-0.99.pdf).

**The Assembly Language**  
The full disassembly of the program is 645 lines long. For sanity's sake, I won't be pasting it here. I'll instead be following along with the code as I explain it. You can disassemble it yourself by running `/usr/bin/clang -S test.m -o test.s -fobjc-arc` in the directory where you compiled the sample code and viewing the `test.s` file. This is the compiler's generated assembly code, which is better annotated than anything else, as the compiler doesn't have to guess at anything's name or location.

Looking at the disassembly, one might notice that the code contains eight functions. Eight? The sample code only has three! Where did those other five come from? Four methods are synthesized by the compiler per the `@synthesize` directive, and the `[MyClass .cxx_destruct]` method is created by the compiler to do C++- and ARC-related cleanup.

**`main`**  
The code for `main` is:

```
    int main(int argc, char **argv)
    {
        @autoreleasepool
        {
            MyClass *obj = [[MyClass alloc] initWithName: @"name" number: 42];
            NSString *string = MyFunction([obj name]);
            NSLog(@"%@", string);
            return 0;
        }
    }
```

And the compiler's assembly language output, stripped of several confusing directives for brevity's sake:

```
    _main:
            pushq        %rbp
            movq        %rsp, %rbp
            subq        $96, %rsp
            leaq        L__unnamed_cfstring_23(%rip), %rax
            leaq        L__unnamed_cfstring_26(%rip), %rcx
            movl        $42, %edx
            leaq        l_objc_msgSend_fixup_alloc(%rip), %r8
            movl        $0, -4(%rbp)
            movl        %edi, -8(%rbp)
            movq        %rsi, -16(%rbp)
            movq        %rax, -48(%rbp)         ## 8-byte Spill
            movq        %rcx, -56(%rbp)         ## 8-byte Spill
            movq        %r8, -64(%rbp)          ## 8-byte Spill
            movl        %edx, -68(%rbp)         ## 4-byte Spill
            callq        _objc_autoreleasePoolPush
            movq        L_OBJC_CLASSLIST_REFERENCES_$_(%rip), %rcx
            movq        %rcx, %rdi
            movq        -64(%rbp), %rsi         ## 8-byte Reload
            movq        %rax, -80(%rbp)         ## 8-byte Spill
            callq        *l_objc_msgSend_fixup_alloc(%rip)
            movq        L_OBJC_SELECTOR_REFERENCES_27(%rip), %rsi
            movq        %rax, %rdi
            movq        -56(%rbp), %rdx         ## 8-byte Reload
            movl        -68(%rbp), %ecx         ## 4-byte Reload
            callq        _objc_msgSend
            movq        %rax, -24(%rbp)
            movq        -24(%rbp), %rax
            movq        L_OBJC_SELECTOR_REFERENCES_28(%rip), %rsi
            movq        %rax, %rdi
            callq        _objc_msgSend
            movq        %rax, %rdi
            callq        _objc_retainAutoreleasedReturnValue
            movq        %rax, %rdi
            movq        %rax, -88(%rbp)         ## 8-byte Spill
            callq        _MyFunction
            movq        %rax, %rdi
            callq        _objc_retainAutoreleasedReturnValue
            movq        %rax, -32(%rbp)
            movq        -88(%rbp), %rax         ## 8-byte Reload
            movq        %rax, %rdi
            callq        _objc_release
            movq        -32(%rbp), %rsi
            movq        -48(%rbp), %rdi         ## 8-byte Reload
            movb        $0, %al
            callq        _NSLog
            movl        $0, -4(%rbp)
            movl        $1, -36(%rbp)
            movq        -32(%rbp), %rdx
            movq        %rdx, %rdi
            callq        _objc_release
            movq        -24(%rbp), %rdx
            movq        %rdx, %rdi
            callq        _objc_release
            movq        -80(%rbp), %rdi         ## 8-byte Reload
            callq        _objc_autoreleasePoolPop
            movl        -4(%rbp), %eax
            addq        $96, %rsp
            popq        %rbp
            ret
```

Whew! `main`'s pretty long in assembly, huh? There are some important things to recognize here:

1. is the first argument register for integer/pointer arguments, and contains the value of

  .
2. contains the value of

  .
3. has the value of

  . This holds true

  !
4. holds the value of a more mysterious

  parameter, whose presence I only discovered when I peeked at the disassembly of the

  function, part of the C runtime.
5. points to the top of the stack. Because

  is a subroutine of

  , the 8 bytes pointed to by

  are the return address for

  , the next instruction in

  .

Let's take it one instruction at a time.

1. `pushq %rbp` - Starting off pretty simple. Save the base pointer on the stack so we can restore it later. The ABI specifies that `rbp` must be preserved across function calls, so since it's about to change, it gets saved.
2. `movq %rsp,%rbp` - Copy `rsp` to `rbp`. This is part of a standard C function's prologue, setting up the stack to hold any local variables that aren't put in registers for whatever reason.
3. `subq $96,%rsp` - A number preceded by `$` in assembly language is a literal decimal number used as an operand to an instruction, so this line subtracts 96 from `rsp`, growing the stack by 96 bytes. This is how much stack space the compiler has determined it will need for the rest of the function.
4. `leaq L__unnamed_cfstring_23(%rip),%rax` - Load the address of `L__unnamed_cfstring_23` into `rax`, using `rip` as the base. `rip`-relative addressing is typically used for loading such things as constant strings and selector names, as well as for fast branches. This particular load grabs the string `@"%@"` from the place it was stored in the executable. This string will later be used as a method parameter.
5. `leaq L__unnamed_cfstring_26(%rip),%rcx` - Same as above, but loading `@"name"` into `rcx`.
6. `movl $42,%edx` - Load the 32-bit value 42 into `edx` (the low 32 bits of `rdx`). This value is also used later.
7. `leaq l_objc_msgSend_fixup_alloc(%rip),%r8` - Grab the address of the `l_objc_msgSend_fixup_alloc` symbol from the Objective-C segment of the executable, and save that address in `r8`. Once again, this is used later.
8. `movl $0, -4(%rbp)` - Load a 32-bit zero into the bottom of the stack.

  This serves as a useful reminder that the stack grows _downwards_; given that we know that `%rbp` points to the _bottom_ of the stack, i.e. the highest address at which the stack exists, this line is actually setting the _last_ four bytes of the stack to zero.

  So what does this actually do? As it turns out, for all intents and purposes, it does absolutely nothing! It's the result of the compiler's determination to make sure no garbage value gets used later, as seen in the next instruction, even though the value is never again read.
9. `movl %edi, -8(%rbp)` - Save `edi`, the low 32 bits of `rdi`, on the stack. As `edi` is the first integer argument register, this is actually the value of `argc`. The previous instruction, setting the last 32 bits of the stack to zero, now makes a bit more sense; the same effect could have been achieved by code something like `*rbp = ((int64_t)argc & 0x00000000FFFFFFFF);`, except that sign-extending and ANDing the value of argc would have been several more operations. Unfortunately for the unoptimizing compiler's track record, this instruction also turns out to be useless, as the value of `argc` is never actually used.
10. `movq %rsi, -16(%rbp)` - Save `rsi`, also known as `argv` at the moment, on the stack. A third useless instruction in a row, since `argv` isn't used either.
11. ```
          movq %rax, -48(%rbp) ## 8-byte Spill
          movq %rcx, -56(%rbp) ## 8-byte Spill
          movq %r8, -64(%rbp) ## 8-byte Spill
          movl %edx, -68(%rbp) ## 4-byte Spill
  ```

  Save `rax` (the string `@"%@"`), `rcx` (the string `@"name"`), `r8` (a pointer to `l_objc_msgSend_fixup_alloc`) and `edx` (the number 42) on the stack as "spill" values.

  What in the world is a spill value, you might ask? A register spill takes place when the compiler needs a register to store a value in, typically as a parameter to a function call since parameters go in specific registers, and none are available. The value in the needed register is saved on the stack ("spilled") so it can be restored ("reloaded") later. In this case, where optimization is shut off, the compiler doesn't have any of the data-flow analysis it would need to realize that all this spilling is unnecessary, and everything in useful registers gets spilled.
12. `callq _objc_autoreleasePoolPush` - Make a subroutine call to `objc_autoreleasePoolPush()`. A subroutine call consists of two operations, performed atomically with respect to other instructions (i.e. they can not be preempted halfway through): Push the address of the next instruction to be executed to the stack, and execute a branch to the address of the first instruction of the called function. Since `objc_autoreleasePoolPush()` doesn't take any parameters, what's in most of the registers doesn't matter. When it returns, however, `rax` contains its `void *` return value, a pointer which acts as an opaque handle to the position of the new autorelease pool on the pool stack. This value is invisible to the Objective-C code, which sees only the `@autoreleasepool` statement.
13. ```
          movq L_OBJC_CLASSLIST_REFERENCES_$_(%rip), %rcx
          movq %rcx, %rdi
          movq -64(%rbp), %rsi ## 8-byte Reload
          movq %rax, -80(%rbp) ## 8-byte Spill
          callq *l_objc_msgSend_fixup_alloc(%rip)
  ```

  Load the value at `rip + L_OBJC_CLASSLIST_REFERENCES_$_` into `rcx`, copy `rcx` into `rdi`, reload the address of `l_objc_msgSend_fixup_alloc` from the stack into `rsi`, spill `rax` (the autorelease pool handle) to the stack, and finally, make a subroutine call to `l_objc_msgSend_fixup_alloc`.

  `L_OBJC_CLASSLIST_REFERENCES_$_` is the symbol for the `MyClass` class object. The load into `rcx` and then the immediate copy to `rdi` is once again a problem of lack of data-flow analysis; the compiler blindly picks the first available register to load the value into, then stores it in the first integer parameter register from there.

  What rules cause it to consider `rcx` the first available register? `rax` is still in use as a return value until the next couple of instructions, and `rbx` isn't considered because its value is preserved across function calls, making it a very un-preferred register for use.

  So far, the `MyClass` class object is parameter 1. The reload from the stack pulls the pointer to `l_objc_msgSend_fixup_alloc` into argument 2. The spill of `rax` saves the autorelease pool handle, since `rax` will be clobbered by the subroutine return. And `l_objc_msgSend_fixup_alloc` is a _vtable_ call; the address of the real `alloc` method will be "fixed up" at runtime for optimization purposes.

  This sequence therefore amounts to an optimized Objective-C message send. Recall that every Objective-C method takes two hidden arguments, `self` and `_cmd`. In this case, `self` is `[MyClass class]`, and `_cmd` is `alloc` (or more exactly, a vtable pointer to a common alloc method for all classes). A very similar sequence follows.
14. ```
          movq L_OBJC_SELECTOR_REFERENCES_27(%rip), %rsi
          movq %rax, %rdi
          movq -56(%rbp), %rdx ## 8-byte Reload
          movl -68(%rbp), %ecx ## 4-byte Reload
          callq _objc_msgSend
  ```

  Load the value at `rip + L_OBJC_SELECTOR_REFERENCES_27` into `rsi`, copy `rax` to `rdi`, reload `@"name"` into `rdx`, reload `42` into `ecx` and subroutine-call to objc_msgSend.

  `L_OBJC_SELECTOR_REFERENCES_27` is the selector for `[MyClass initWithName:number:]`, placed into `rsi`, or argument 2. `rax` holds the return value of `alloc`, which is the new `MyClass` object, and it's copied into argument 1. The third parameter, `rdx`, is loaded with the constant NSString `@"name"`, and the fourth parameter with the number 42. Finally, `objc_msgSend()` is called. This is the call sequence for `[ initWithName:@"name" number:42]`. The init method will return the value of `self` in `rax`.
15. `movq %rax, -24(%rbp)` and `movq -24(%rbp), %rax` - Yes, that's right, these two instructions are entirely redundant. Because `-24(%rbp)` is used later, it's good for the value to be saved. Unfortunately, the immediate reload back into `rax` is not justified.
16. ```
          movq L_OBJC_SELECTOR_REFERENCES_28(%rip), %rsi
          movq %rax, %rdi
          callq _objc_msgSend
  ```

  Hopefully, you've got the hang of this by now; this is `objc_msgSend(rax, @selector(name));`. Return value in `rax` as usual.
17. `movq %rax, %rdi` and `callq _objc_retainAutoreleasedReturnValue` should be obvious now. `objc_retainAutoreleasedReturnValue(obj);` is inserted by ARC to keep the return value of the `name` method alive, since the temporary variable created invisibly by the Objective-C compiler to hold the value is implicitly declared `__strong`.
18. ```
          movq %rax, %rdi
          movq %rax, -88(%rbp) ## 8-byte Spill
          callq _MyFunction
          movq %rax, %rdi
          callq _objc_retainAutoreleasedReturnValue
  ```

  Save the return value of `name`, copy it as the first parameter to `MyFunction()`, call `MyFunction()`, call `objc_retainAutoreleasedReturnValue()` on the return from it.
19. ```
          movq %rax, -32(%rbp)
          movq -88(%rbp), %rax ## 8-byte Reload
          movq %rax, %rdi
          callq _objc_release
  ```

  Save the return value of `MyFunction()`. Then, reload the result of `[MyClass name]`, and call `objc_release()` on it, as ARC has noticed that it's no longer used.
20. ```
          movq -32(%rbp), %rsi
          movq -48(%rbp), %rdi ## 8-byte Reload
          movb $0, %al
          callq _NSLog
  ```

  A simple call to `NSLog()`, with the only odd feature being the set of `al` to zero. Because `NSLog()` is a variadic function, the calling convention specifies that `al` holds the number of vector registers used when calling it. No vector registers are used, so it's just set to zero.
21. `movl $0, -4(%rbp)` and `movl $1, -36(%rbp)` - I have to admit, I see no reason whatsoever for the compiler to toss a zero and a one onto what look rather like random parts of the stack, here or anywhere else in `main()`. Nothing like these values is used anywhere in the optimized version of the code. The store of zero at least gets used further down, but the store of a 1 seems entirely meaningless.
22. ```
          movq -32(%rbp), %rdx
          movq %rdx, %rdi
          callq _objc_release
  ```

  Release the return value of `MyFunction()` - you have set aside a sheet of paper to keep track of which values went in which offsets on the stack and in which registers, haven't you? If not, it'd be little wonder if you were a little lost by now.
23. ```
          movq -24(%rbp), %rdx
          movq %rdx, %rdi
          callq _objc_release
  ```

  Now release `obj`, the object of class `MyClass` that we allocated before.
24. ```
          movq -80(%rbp), %rdi ## 8-byte Reload
          callq _objc_autoreleasePoolPop
  ```

  Reload the autorelease pool handle and pop it by calling `objc_autoreleasePoolPop()`. This is the code inserted by the closing brace `}` of the `@autoreleasepool` statement.
25. ```
          movl -4(%rbp), %eax
          addq $96, %rsp
          popq %rbp
          ret
  ```

  Load the zero on the stack into `eax` as `main`'s return value.

  Restore the stack pointer to its original position when `main` was called.

  Pop the original value of `rbp` off the stack and back into `rbp`.

  Pop the address of the next instruction off the stack into `rip`, also known as returning from a subroutine call.

And that's `main()`! What a long-winded mess.

I must admit at this point that I went out of my way to make this function difficult to understand in one critical respect: I've been working from the _unoptimized_ version of the code generated by the compiler. The code built with `-Os` is, surprisingly, much easier to understand, with a lot of redundant work completely eliminated and the registers managed much more efficiently. There's also almost no work done on the stack, since the compiler in optimizing mode is free to make use of a larger pool of scratch registers.

I did this because until you can understand the control flow of an unoptimized routine, there's no point in reading optimized code. Starting with the optimized code is a bit like learning to swim in water so shallow you can't even put your face under, except for those times when the compiler does something fantastically tricky to get a speed or size bonus, when it suddenly becomes rather like diving into the deep end of an Olympic pool.

**Conclusion**  
That's the end of this article, but it's only part 1 in a series. Hopefully, you've enjoyed it so far; in part 2 I'll explore the rest of the methods in the sample code, as well as the optimized version of the code and the C runtime's `start` function.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
