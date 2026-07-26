---
title: 'Friday Q&A 2011-12-30: Disassembling the Assembly, Part 3: ARM edition'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-12-30-disassembling-the-assembly-part-3-arm-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:48e6c9e1fc764c1b'
translated: false
---

> 原文：[Friday Q&A 2011-12-30: Disassembling the Assembly, Part 3: ARM edition](https://www.mikeash.com/pyblog/friday-qa-2011-12-30-disassembling-the-assembly-part-3-arm-edition.html)　·　mikeash.com Friday Q&A

Posted at 2011-12-30 21:44 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Avoid Apress](https://www.mikeash.com/pyblog/avoid-apress.html)  
Previous article: [Friday Q&A 2011-12-23: Disassembling the Assembly, Part 2](https://www.mikeash.com/pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [disassembly](https://www.mikeash.com/pyblog/?tag=disassembly) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-12-30: Disassembling the Assembly, Part 3: ARM edition

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

Since I wrote [part 1](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html) of this series on reading x86_64 assembly language, I've gotten several requests for a version which talks about reading ARM assembly language, as ARM is the architecture used by devices running iOS. Unfortunately, at the time of those requests, I didn't know much of anything about ARM! So rather than disappoint, I embarked on a crash course in the instruction set.

Fortunately, it turned out that ARM isn't all that complicated; it's more like learning a new dialect of a language you already know than learning an entirely new language. For sanity's sake, in this article I will assume you've already read both [part 1](https://www.mikeash.com/pyblog/friday-qa-2011-12-16-disassembling-the-assembly-part-1.html) and [part 2](https://www.mikeash.com/pyblog/friday-qa-2011-12-23-disassembling-the-assembly-part-2.html), and explain only the differences that appear in ARM rather than reiterating all the basic concepts.

I have most likely made at least one mistake in my understanding of ARM, and I gladly invite any explanations and corrections that people may find.

**CPU and ABI**  
Unfortunately, the ARM specifications are a little harder to get your hands on than x86_64's; you have to [go to their website](http://infocenter.arm.com/) and register for an account before you can download the PDFs. On the bright side, it's _not_ a paywall and the registration process is fairly simple. If you go to the trouble, look for the documents "ARMv7-AR Architecture Reference Manual (Issue C)" under "ARM Architecture", and "Base Platform ABI for the ARM Architecture" and "Procedure Call Standard for the ARM Architecture" under "ARM software development tools". [Apple's documentation on the ARM ABI used for iOS](http://developer.apple.com/library/ios/#documentation/Xcode/Conceptual/iPhoneOSABIReference/Introduction/Introduction.html) is public, and gives nearly all information one would typically need regarding the ABI.

_I found it a little bemusing that the primary documentation for ARM is split across several dozen documents, while that for x86_64 is in six PDFs total. There are an equal number of documents under the x86_64 umbrella as a whole, but you need only two (maximum three if you do SIMD work) of them to do applications programming, and those are very clearly labeled. At least three documents are needed just to get the same amount of data for ARM, and they're considerably harder to find unless you already know a number of details about the platform and high-level language you'll be working with._

**The many flavors of ARM**  
Before I can talk about the particulars of how ARM does what it does, I have to explain something about the architecture: There are at least a dozen flavors of it. Unlike x86, ARM was designed from its very beginning for use in a variety of environments, all with different requirements for speed, power consumption, and efficiency. It has also gone through a number of major revisions, and has a long list of optional features. In this article I will focus on the particular flavor of ARM used by the modern iPhone, iPad, and iPod Touch: The ARMv7 architecture, Application profile, with Thumb 2 and NEON SIMD.

What does this mean? It means I'll be working from version 7 of the ARM instruction set (there are currently 8 revisions, but ARMv8 is not yet implemented in any shipping processors). I'll focus on the Application profile, which is intended for typical operating systems, rather than the Real-time profile (intended for small - you guessed it! - realtime systems) or the Mobile profile (intended for embedded systems). ARMv6, used in first- and second-generation iDevices save the iPad, is largely similar, but not identical. It also means I'll use the Thumb instruction set, as it's strongly recommended by Apple for use on iOS.

**Thumb**  
The ARM architecture specifies a secondary instruction set called Thumb. The purpose of Thumb is fairly simple: Do all the common tasks with smaller instructions. While ARM instructions have a fixed size of 32 bits each, Thumb instructions (with a very few exceptions) are 16 bits each, making for much smaller code. Apple has recommending building iOS code with Thumb for most of iOS' lifetime for exactly this reason, though their toolchain is famous for creating crashing code when building ARMv6 Thumb with floating-point support.

In ARMv6, reading Thumb versus ARM assembler was annoying at best, as they didn't use the same language. With ARMv7, however, ARM developed a "Unified Assembly Language" (UAL) which covers all the operations of both ARM and Thumb instructions in a single (you guessed it!) unified set of mnemonics. This is another reason I'm sticking to ARMv7.

_Note: It was also not until ARMv7 that Thumb (more specifically, Thumb 2) got proper support for floating-point extensions, which is part of the reason Apple's compilers had so much trouble earlier on._

A particular quirk of Thumb is how you tell the CPU which instruction set you're running at any given moment. This is solved by a set of "interworking" branch instructions; when a branch is taken by one of these instructions to an address stored in a register, it interprets the least significant (last) bit of the address as a flag telling the CPU which mode to switch to. When a branch is taken to a hardcoded address, however, the instruction set flag is simply flipped. Therefore, a `bx #12345` instruction will branch to Thumb if the current ISA is ARM, and ARM if the current ISA is Thumb, whereas a `bx r5` instruction will set the current ISA based on the low bit of `r5` (a `1` bit branches to Thumb, a `0` bit to ARM).

Keep in mind, however, that all this fancy interworking stuff only happens if the program asks it to. The normal `b` and `bl` instructions don't do any of this. Whether or not you change instruction sets during any branch is up to you!

Don't worry if this doesn't make too much sense; thanks to UAL, the meaning of the instructions is the same between Thumb and ARM in almsot all cases, so knowing how to read the assembly language is most of what you need. It is important to remember only that most Thumb instructions can only access a limited set of registers, and take much smaller ranges of immediate values.

**Registers**  
ARM specifies sixteen general-purpose registers and one status register for application use. NEON further defines sixteen 128-bit vector registers which overlap with the set of thirty-two double precision floating-point registers used by the earlier VFP specification (these in turn overlap with the set of thirty-two single precision registers). Registers with multiple names can be referred to by either name with the same result, though by convention it is always preferred to use a name (such as `lr`) over a number (such as `r14`) except in specific situations. Of these fifteen, several are reserved for specific purposes.

- `r0-r3` - The first four GPRs are used for argument passing and return values, but are freely available for use as scratch storage within a function.
- `r4-r6, r8, r10, r11` - The next three GPRs, as well as `r8`, `r10`, and `r11` are documented as being preserved across function calls, but are also otherwise available for use.
- `r7` - On iOS, `r7` is the frame pointer, much as `rbp` is in x86_64. The ARM architecture in general does not specify a use for `r7`; this is specific to iOS. _To be exact, ARM specifies `r11` as `fp`, but Apple chose not to use that register on iOS, and avoided the `fp` name so as not to make their assembler incompatible with other ARM implementations._
- `r9` - On iOS 2.x, `r9` is a special register used by the OS for unspecified purposes and must not be modified. On iOS 3.0 and above, `r9` is free for use and does not need to be preserved across function calls.
- `r12`, `ip` - `r12` is the "intra-procedure scratch register". Between calls, it has the same semantics as `r9` and does not have to be preserved. It is also called `ip` (_not_ to be confused with x86_64's `rip` register - they are _not_ similar), and is used as such for computing destination addresses for long branches.
- `r13`, `sp` - `r13`, also called `sp`, is the stack pointer. This serves the same purpose as `rsp` on x86_64 and works in much the same way.
- `r14`, `lr` - The link register is loaded by the `bl` and `blx` instructions, which make subroutine calls (much as `call` does on x86_64). ARM dedicates a register to storing the return address for a call rather than relying on the stack to hold it. This means that a subroutine can, at least in theory, operate without ever touching the stack at all, an important win in real-time and embedded systems.
- `r15`, `pc` - The program counter holds the address of the next instruction to be excuted. It is the counterpart to x86_64's `rip` register. Some non-branch instructions can access `pc` directly, but it is very strongly discouraged except in very specific situations (for example, as we'll see below, it is a common technique to push `lr` to the stack in a prolog and pop the value into `pc` in an epilogue, which results in a return from subroutine).
- `q0-q15` - A set of sixteen 128-bit vector registers which are used for parameter passing, result values, and scratch computation. Of these, `q4-q7` are preserved across function calls.
- `d0-d31` - A set of thirty-two 64-bit double-precision floating-point registers. These are mapped onto the corresponding vector registers such that `d0` and `d1` are the low and high 64 bits of `q0`, `d2` and `d3` are the low and high 64 bits of `q1`, and so on.
- `s0-s31` - A set of thirty-two 32-bit single-precision floating-point registers. These are mapped onto the corresponding double-precision registers such that `s0` and `s1` are the low and high bits of `d0`, and so forth. This also implies that `s0-s3` are the four 32-bit components of `q0`.
- `cpsr` - The CPU's status register, partially equivelant to `rflags` in x86_64. It has the following bits, most of which are not preserved across function calls:

    - `N` - Negative flag, i.e. the sign bit of the result of a computation.
    - `Z` - Zero flag, i.e. whether a result is equal to zero.
    - `C` - Carry flag, i.e. whether an addition carried or a subtraction borrowed.
    - `V` - Overflow flag, i.e. whether a computation result overflowed its destination.
    - `Q` - Saturation flag, i.e. whether a computation resulted in saturation; this is used by instructons that saturate on overflow (i.e. set all bits to 1 rather than wrapping around the integer range).
    - `GE` - The Greater than or Equal flags, used by parallel arithmetic instructions to represent the results from several additions or subtractions at once.
    - `E` - Endianness. The ARM architecture supports switching the endianness mode of the CPU at runtime, but iOS specifies that this bit must always remain zero for little-endian mode.
    - `T` - Thumb. This is the status flag which determines whether Thumb or ARM code is being executed. It can not be modified directly and the preservation of its value is context-dependant. (There is also a `J` flag for Jazelle mode, but iOS does not implement or use it.)
    - All other bits are system-level and can only be accessed by privileged code.

**Calling conventions**  
Actually, I don't have to say much here; it's all in the registers commentary. `r0-r3` are used for integer argument passing and returns, `s/d/q0-qN` are used for floating-point argument passing and returns, and anything that doesn't fit in the registers is spilled to the stack. As usual, this is a bit simplified, but it works!

Oh, and by the way, the memory model for ARM is, for all intents and purposes, the same as that for x86_64, save for the smaller memory space.

**Disassembling, at last**  
Enough architecture talk, let's look at some assembler. I'm using the same code again as in parts 1 and 2, and the following command for compilation:

```
        /Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/clang -S test.m -fobjc-arc -arch armv7 -miphoneos-version-min=5.0 -isysroot /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS5.0.sdk -mthumb -Os
```

That's use the iOS SDK's Clang, show assembler output, compile with ARC, compile for ARMv7, require iOS 5 (required to link properly), build against the iOS SDK (required for ARM compilation), use Thumb, and optimize for size. And here's the result for the `main` function:

```
                .thumb_func        _main
        _main:
                push        {r4, r5, r6, r7, lr}
                add        r7, sp, #12
                str        r8, [sp, #-4]!
                blx        _objc_autoreleasePoolPush
                movw        r1, :lower16:(L_OBJC_SELECTOR_REFERENCES_25-(LPC8_0+4))
                movt        r1, :upper16:(L_OBJC_SELECTOR_REFERENCES_25-(LPC8_0+4))
                mov        r8, r0
                movw        r0, :lower16:(L_OBJC_CLASSLIST_REFERENCES_$_-(LPC8_1+4))
        LPC8_0:
                add        r1, pc
                movt        r0, :upper16:(L_OBJC_CLASSLIST_REFERENCES_$_-(LPC8_1+4))
        LPC8_1:
                add        r0, pc
                ldr        r1, [r1]
                ldr        r0, [r0]
                blx        _objc_msgSend
                movw        r1, :lower16:(L_OBJC_SELECTOR_REFERENCES_28-(LPC8_2+4))
                movs        r3, #42
                movt        r1, :upper16:(L_OBJC_SELECTOR_REFERENCES_28-(LPC8_2+4))
        LPC8_2:
                add        r1, pc
                ldr        r1, [r1]
                movw        r2, :lower16:(L__unnamed_cfstring_27-(LPC8_3+4))
                movt        r2, :upper16:(L__unnamed_cfstring_27-(LPC8_3+4))
        LPC8_3:
                add        r2, pc
                blx        _objc_msgSend
                mov        r5, r0
                movw        r0, :lower16:(L_OBJC_SELECTOR_REFERENCES_29-(LPC8_4+4))
                movt        r0, :upper16:(L_OBJC_SELECTOR_REFERENCES_29-(LPC8_4+4))
        LPC8_4:
                add        r0, pc
                ldr        r1, [r0]
                mov        r0, r5
                blx        _objc_msgSend
                mov        r7, r7                @ marker for objc_retainAutoreleaseReturnValue
                blx        _objc_retainAutoreleasedReturnValue
                mov        r4, r0
                mov        r0, r4
                bl        _MyFunction
                mov        r7, r7                @ marker for objc_retainAutoreleaseReturnValue
                blx        _objc_retainAutoreleasedReturnValue
                mov        r6, r0
                mov        r0, r4
                blx        _objc_release
                movw        r0, :lower16:(L__unnamed_cfstring_23-(LPC8_5+4))
                mov        r1, r6
                movt        r0, :upper16:(L__unnamed_cfstring_23-(LPC8_5+4))
        LPC8_5:
                add        r0, pc
                blx        _NSLog
                mov.w        r0, #1065353216
                bl        _MyFPFunction
                vmov        s0, r0
                movw        r0, :lower16:(L__unnamed_cfstring_31-(LPC8_6+4))
                movt        r0, :upper16:(L__unnamed_cfstring_31-(LPC8_6+4))
                vcvt.f64.f32        d16, s0
        LPC8_6:
                add        r0, pc
                vmov        r1, r2, d16
                blx        _NSLog
                mov        r0, r6
                blx        _objc_release
                mov        r0, r5
                blx        _objc_release
                mov        r0, r8
                blx        _objc_autoreleasePoolPop
                movs        r0, #0
                ldr        r8, [sp], #4
                pop        {r4, r5, r6, r7, pc}
```

Whew! For a function built with an instruction set specifically designed to be small, this is pretty long. Seventy-two lines. In truth, the compiled machine code is quite small; only the assembler that produces that code is verbose, which is typical of RISC architectures.

Some quick notes about ARM assembler syntax:

- The order of operands in an ARM instruction is reversed from the "GAS" (GNU ASsembler) syntax used by the x86_64 assembler. A typical instruction is "mnemonic destination, operand1, operand2". This is ironically closer to the original Intel assembler syntax.
- Immediate operands are delimited with `#` rather than `$`.
- Register names are _not_ prefixed by `%`.

Let's see what we can make of `main`:

1. ```
              .thumb_func        _main
      _main:
              push        {r4, r5, r6, r7, lr}
              add        r7, sp, #12
              str        r8, [sp, #-4]!
  ```

  `.thumb_func` is an assembler directive that tells `clang` to use the Thumb ISA for the function named. Then we have the symbol for the function. ARM's `push` instruction can take an entire list of registers at once to save to the stack, so `main` is saving `r4` through `r6` so it can use them as scratch, `r7` (the old frame pointer), and `lr` (the return address of the calling function). `lr` must be saved because any subroutine calls `main` makes will overwrite the value - it is not preserved across function calls. Not only that, but iOS (and any other implementation with a frame pointer) requires the return address to be on the stack as part of the stack frame for the function. The iOS ABI says that failure to set up a stack frame "can prevent debugging and performance tools from generating valid backtraces." Next, we add `12` to the stack pointer and store the result in `r7` to create the frame pointer. Notice that this does _not_ modify `sp` itself! The last instruction is rather tricky: It subtracts `4` from `sp`, saves the new value of `sp`, and writes the value in `r8` to memory at `sp`. The net result of this is to push `r8` to the stack. The compiler doesn't use another `push` instruction because the encoding of `str` for `r8` is smaller in Thumb (16-bit versus needing a 32-bit Thumb instruction to `push` it).
2. ```
              blx        _objc_autoreleasePoolPush
              mov        r8, r0
  ```

  Branch and link with interworking to `objc_autoreleasePoolPush`. This is just a subroutine call, with the option to switch to the ARM ISA. The function takes no parameters, and will return its result in `r0`. The result is saved in `r8`. _Yes, I know I've read the instructions out of order here, but the compiler separated them for some reason and it makes no difference to the code flow to show them in conceptual order rather than assembler order._
3. ```
              movw        r1, :lower16:(L_OBJC_SELECTOR_REFERENCES_25-(LPC8_0+4))
              movt        r1, :upper16:(L_OBJC_SELECTOR_REFERENCES_25-(LPC8_0+4))
              movw        r0, :lower16:(L_OBJC_CLASSLIST_REFERENCES_$_-(LPC8_1+4))
      LPC8_0:
              add        r1, pc
              movt        r0, :upper16:(L_OBJC_CLASSLIST_REFERENCES_$_-(LPC8_1+4))
      LPC8_1:
              add        r0, pc
              ldr        r1, [r1]
              ldr        r0, [r0]
              blx        _objc_msgSend
  ```

  Welcome to calling Objective-C selectors on ARM! This reads: Take the address of label `L_OBJC_SELECTOR_REFERENCES_25`, subtract the address of label `LPC8_0+4`, and select the low sixteen bits of the result, writing them into the bottom 16 bits of `r1`. Then take upper 16 bits of the same address and write them into the upper 16 bits of `r1`. This is done in two steps because there is no Thumb encoding for a 32-bit immediate register load. `pc` is then added to `r1`, forming a `pc`-relative address. This idiom should look familiar from x86_64's `rip`-relative addressing. The same is done again for `L_OBJC_CLASSLIST_REFERENCES_$_`, loading it into `r0`. The two `ldr` instructions read values from the addresses in the two registers into the registers themselves, equivelant to the C code `a = *a;`. Finaly, the code does a branch and link with interworking instruction to `objc_msgSend`, completing the method call. Congratulations, you've just learned how ARM calls `[MyClass alloc]`! The vtable tricks done in x86_64 don't exist for ARM, as ARM's addressing and branching modes don't make direct dispatch more efficient than a subroutine call.
4. ```
              movw        r1, :lower16:(L_OBJC_SELECTOR_REFERENCES_28-(LPC8_2+4))
              movt        r1, :upper16:(L_OBJC_SELECTOR_REFERENCES_28-(LPC8_2+4))
      LPC8_2:
              add        r1, pc
              ldr        r1, [r1]
              movw        r2, :lower16:(L__unnamed_cfstring_27-(LPC8_3+4))
              movt        r2, :upper16:(L__unnamed_cfstring_27-(LPC8_3+4))
      LPC8_3:
              add        r2, pc
              movs        r3, #42
              blx        _objc_msgSend
              mov        r5, r0
  ```

  Once again I've slightly rearranged the instruction stream to make more sense. This call is really no different from the first. The result from `alloc` is already in `r0`. The `-initWithName:number:` selector is loaded into `r1`, the string `@"name"` into `r2`, and the immediate value `42` into `r3`. The result of the method call is saved in `r5`.
5. ```
              movw        r0, :lower16:(L_OBJC_SELECTOR_REFERENCES_29-(LPC8_4+4))
              movt        r0, :upper16:(L_OBJC_SELECTOR_REFERENCES_29-(LPC8_4+4))
      LPC8_4:
              add        r0, pc
              ldr        r1, [r0]
              mov        r0, r5
              blx        _objc_msgSend
  ```

  This is the `[obj name]` method call. Nothing special here.
6. ```
              mov        r7, r7                @ marker for objc_retainAutoreleaseReturnValue
              blx        _objc_retainAutoreleasedReturnValue
              mov        r4, r0
  ```

  The ARC-aware compiler inserts an effective `nop` (move a register to itself) into the instruction stream so certain code in the Objective-C runtime can detect the call to `objc_retainAutoreleasedReturnValue`, then actulaly makes the call. No registers need to be set up, as the return value in `r0` matches the intended first parameter also in `r0`. The result of the function, i.e. the retained `[obj name]`, is saved in `r4`.
7. ```
              mov        r0, r4
              bl        _MyFunction
              mov        r7, r7                @ marker for objc_retainAutoreleaseReturnValue
              blx        _objc_retainAutoreleasedReturnValue
              mov        r6, r0
  ```

  The value from `r4` is reloaded into `r0`, unnecessarily! The compiler seems to have stumbled in optimizing here, and I'm not sure why. In any case, it then calls `MyFunction`, and another `objc_retainAutoreleasedReturnValue` stanza, saving the final result (i.e. `string`) in `r6`.
8. ```
              mov        r0, r4
              blx        _objc_release
  ```

  `[obj name]` is no longer needed, so release it.
9. ```
              movw        r0, :lower16:(L__unnamed_cfstring_23-(LPC8_5+4))
              movt        r0, :upper16:(L__unnamed_cfstring_23-(LPC8_5+4))
      LPC8_5:
              add        r0, pc
              mov        r1, r6
              blx        _NSLog
  ```

  Again having rearranged the instructions slightly, this is a load of `@"%@"` into `r0` and `string` into `r1`, and a call to `NSLog`. Variadic functions appear to have no special semantics on ARM.
10. ```
              mov.w        r0, #1065353216
              bl        _MyFPFunction
              vmov        s0, r0
  ```

  The 32-bit decimal representation of `1.0` is loaded into `r0`, an integer register. Why? Because it fits and integer registers are more efficient than vector or floating-point registers when possible. `MyFPFunction` is called, and the result (again in `r0`!) loaded into the `s0` floating-point register. _Note: The `.w` suffix on the `mov` instruction means to use the 32-bit Thumb encoding for the instruction even if the 16-bit encoding would otherwise be selected. For this particular instruction, it is probably unnecessary, but it's considered good form to use the annotation even if the 32-bit encoding would chosen automatically._
11. ```
              movw        r0, :lower16:(L__unnamed_cfstring_31-(LPC8_6+4))
              movt        r0, :upper16:(L__unnamed_cfstring_31-(LPC8_6+4))
      LPC8_6:
              add        r0, pc
              vcvt.f64.f32        d16, s0
              vmov        r1, r2, d16
              blx        _NSLog
  ```

  Load `@"%f"` into `r0`. Convert the single-precision floating-point value in `s0` to a double-precision floating-point value in `d16`, per the C type promotion rules for variadic function parameter lists (`float` is converted to `double`). Load the double-precision value in `d16` into the two integer registers `r1` and `r2`, and call `NSLog`. It is always preferred to pass floating-point arguments in integer registers if they are available.
12. ```
              mov        r0, r6
              blx        _objc_release
              mov        r0, r5
              blx        _objc_release
              mov        r0, r8
              blx        _objc_autoreleasePoolPop
  ```

  Release `string`, release `objc`, pop the autorelease pool.
13. ```
              movs        r0, #0
              ldr        r8, [sp], #4
              pop        {r4, r5, r6, r7, pc}
  ```

  Load `0` as the return value of `main`, pop `r8` off the stack (remember, `r8` can not be efficiently addressed by a `pop` instruction in Thumb), and restore all the saved registers. Notice that while we saved `lr` at the beginning of `main`, we now pop that value into `pc`. This effectively executes an interworking return from subroutine. (`pop` into `pc` is explicitly documented as an interworking branch).

And that's `main`.

**MyFPFunction**  
Let's take a quick look at the floating-point operations:

```
                .thumb_func        _MyFPFunction
        _MyFPFunction:
                vmov.f32        s2, #5.000000e-01
                vldr.32        s0, LCPI7_0
                vmov        s4, r0
                vadd.f32        d16, d2, d1
                vadd.f32        d0, d16, d0
                vmov        r0, s0
                bx        lr
        LCPI7_0:
                .long        3197737370
```

1. Declare a Thumb function `MyFPFunction`.
2. ```
              vmov.f32        s2, #5.000000e-01
              vldr.32        s0, LCPI7_0
              vmov        s4, r0
  ```

  Load the immediate single-precision floating-point value `5.0` into `s2`. Load the single-precision floating-point value at `LCPI7_0` (`-0.3`) into `s0`. Load the single-precision floating-point value stored in `r0` into `s4`.
3. ```
              vadd.f32        d16, d2, d1
              vadd.f32        d0, d16, d0
              vmov        r0, s0
  ```

  Using single-precision math, first add `d1` and `d2` into `d16` (remember that `s0` corresponds to `d0`, `s2` corresponds to `d1`, and `s4` corresponds to `d2`). Then add `d0` and `d16` into `d0`. Finally, store the single-precision result back into `r0`.
4. ```
              bx        lr
  ```

  Branch, with interworking, to the link register. This function is so small and simple that it has no prologue, no epilogue, and no stack frame, when built in optimizing mode. This is a noticable win for ARM code, where it wouldn't have been for x86_64. Since `lr` contains the return address for `main`, this returns us there.

That's the whole function! Wasn't that simple?

**Conclusion**  
This concludes the whirlwind tour of ARM assembly, and this series of articles on assembly in general. There is quite a bit I haven't covered in both architectures, such as conditional instructions, looping, and optional flag updates on instructions, but this was meant only as an introduction after all. I hope you've enjoyed it. Thanks for reading!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-12-30-disassembling-the-assembly-part-3-arm-edition.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
