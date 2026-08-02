---
title: LLVM-GCC Release Notes
apple_id: TP40007133
resource_type: Release Note
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-llvm-gcc/index.html
archived_at: '2026-07-18T02:50:29.097718Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# LLVM-GCC 4.2 Release Notes

> [!IMPORTANT]
> 

LLVM-GCC is a new compiler optimization technology based on the LLVM (Low-Level Virtual Machine) open source project. In Xcode 3.1.x, LLVM-GCC is manifested in the LLVM-GCC 4.2 compiler.

In LLVM-GCC, LLVM is used to provide an optimizer and code generator plug-in to GCC. This technology is used in the OpenGL software stack in Mac OS X v.10.5. You can take advantage of it in your projects.

You can learn more about LLVM at [http://llvm.org](http://llvm.org/).

To learn about the changes made to LLVM-GCC 4.2 in Xcode 3.1.1, see [Xcode 3.1.1 Additions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcoa).

#### Contents:

- [LLVM-GCC 4.2 Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcma)
- [LLVM-GCC 4.2 Installation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcmi)
- [Using LLVM-GCC 4.2 in Xcode Projects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcmq)
- [Using LLVM-GCC 4.2 in UNIX-Based Development Environments](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcmy)
- [Link-Time Optimization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcna)
- [GCC-4.2 Features Not Available in LLVM-GCC-4.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknlto)
- [LLVM Open-Source Community Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcnq)
- [Submitting Feedback to Apple](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcoi)
- [Xcode 3.1.1 Additions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltcoa)

### LLVM-GCC 4.2 Overview

LLVM-GCC 4.2 is a standalone compiler that combines the industry standard GCC 4.2 front end with the innovative LLVM optimizer and code generator. Therefore, you can use LLVM-GCC 4.2 as a replacement for GCC 4.2. The two compilers are largely compatible, supporting the same languages and using the same command-line option and architectures. Like GCC 4.2, LLVM-GCC 4.2 supports compilation of C, C++, Objective-C, and Objective-C++ on x86, x86-64, PowerPC, and PowerPC-64. See [GCC-4.2 Features Not Available in LLVM-GCC-4.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknlto) for a list of GCC 4.2 features that LLVM-GCC 4.2 does not support.

### LLVM-GCC 4.2 Installation

The Xcode 3.1 installer places LLVM-GCC 4.2 in `<Xcode>/usr/bin` (`<Xcode>` is the directory into which you installed Xcode, which the installer sets as `/Developer` by default).

### Using LLVM-GCC 4.2 in Xcode Projects

In Xcode projects, you use build rules to specify the compiler to use for particular source files. To use LLVM-GCC 4.2 instead of GCC 4.2 in an Xcode project:

1. Open the target editor by double-clicking the appropriate target.
2. In the Rules pane choose Rules Specific to Target from the pop-up menu.
3. Click the Add (+) button.
4. Configure the new rule:

   1. Chose the appropriate language form the Process pop-up menu.
   2. Choose “llvmgcc42” from the “using” pop-up menu.

### Using LLVM-GCC 4.2 in UNIX-Based Development Environments

You use LLVM-GCC 4.2 in UNIX-based development environments just as you use GCC 4.2. The majority of such environments respect the `CC` and `CXX` environment variables. For example, the following listing shows one way to set LLVM-GCC 4.2 as the compiler for C source files.

```
CC=<Xcode>/usr/bin/llvm-gcc-4.2 make
```

Here, `<Xcode>` is the directory into which you installed Xcode.

If you have several copies of Xcode installed on your computer, may also use `` `xcode-select -print-path` `` in `CC`, `CXX`, or shell scripts to get the path to the Xcode release you have selected as the one to use for UNIX-based development.

```
CC=`xcode-select -print-path`/usr/bin/llvm-gcc-4.2 make
```

See `xcode-select` for more information on this facility, but keep in mind that you cannot use all the features of `xcode-select` to locate Xcode directories on your file system. Only `xcode-select -print-path` is supported with LLVM-GCC 4.2.

### Link-Time Optimization

Traditionally, compilers optimize individual source files while building a project. However, this model does not allow compilers to take advantage of symbol information available in separate source files, but the linker collects this information during the link stage. Link-Time Optimization allows the optimizer to look across object files in your program and optimize across file boundaries. For example, one possible optimization is the inlining of a function defined in one file into a function defined in another file. See Listing 1-1 and Listing 1-2.

__Listing 1-1__`sourcefile1.c`: `getNumber()`

```
int getNumber() {
    return 42;
}
```


__Listing 1-2__`sourcefile2.c`: `processNo(int)`

```
extern int getNumber();

int processNo(int i) {
    return i * getNumber();
}
```

During the link-time optimization stage, the function `getNumber()` (defined in `sourcefile1.c`) is inlined inside the function `processNo(int)` (defined in `sourcefile2.c`).

To turn on Link-Time Optimization use `-O4` command-line option or set the Optimization Level build setting to `4` in the build settings editor for the appropriate target.

LLVM-GCC 4.2 supports a wide range of interprocedural optimizations, including global variable optimization, inter modular inlining, interprocedural constant propagation and dead argument elimination.

### Mixing LLVM Bitcode Files with Mach-O Files

When Link-Time Optimization is turned on, the object files LLVM-GCC 4.2 generates are not Mach-O object files. Instead they are object files that use the LLVM bitcode file format ([http://llvm.org/docs/BitCodeFormat.html](http://llvm.org/docs/BitCodeFormat.html)). These files contain LLVM bitcode that the linker optimizes using the LLVM optimizer. Specifically, the Xcode linker links LLVM files together. But it can also link LLVM bitcode files with Mach-O object files to generate an optimized Mach-O binary.

Let’s look at an example that illustrates how the linker links one LLVM bitcode file with a Mach-O object file. In this example, the source files Listing 1-3, Listing 1-4, and Listing 1-5 are compiled and linked with [Listing 1-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltq).

__Listing 1-3__`header.h`

```
extern int fn1(void);
extern void fn2(void);
extern void fn4(void);
```


__Listing 1-4__`sourcefile3.c`

```c
#include "header.h"

static signed int flag = 0;
void fn2(void) {
    flag = -1;
}

static int fn3() {
    fn4();
    return 10;
}

int fn1(void) {
    int data = 0;
    if (flag < 0) {
        data = fn3();
    }
    data = data + 42;
    return data;
}
```


__Listing 1-5__`main.c`

```c
#include <stdio.h>
#include "header.h"

void fn4() {
    printf("Hi\n");
}

int main() {
    return fn1();
}
```


__Listing 1-6__Compiling and linking `sourcefile3.c` and `main.c`

```shell
$ llvm-gcc-4.2 -O4 -c sourcefile3.c -o sourcefile3.o
$ llvm-gcc-4.2 -c main.c -o main.o
$ llvm-gcc-4.2 sourcefile3.o main.o -o main
```

The linker recognizes that `fn2()` is an externally visible symbol defined in LLVM bitcode but unused. This information helps the LLVM optimizer remove `fn2()`, which, in turn, allows the optimizer to prove that `flag` is always `0`. As a result, the optimizer removes the branch in `fn1()`, which results in the removal of `fn3()` because it’s now unused. With the removal of `fn3()`, the linker concludes that `fn4()` is also unused, which it then removes.

Note that `sourcefile3.o` is an LLVM bitcode file and `main.o` is a Mach-O object file. No additional linker command-line options are required to link them together and generate the optimized `main` executable.

### Link-Time Optimization and Symbol Visibility

Link-Time Optimization respects symbol visibility. The link-time optimizer does not remove a symbol that is marked as externally visible while building a dynamic library, even if the optimizer determines that the symbol is unused. If a function is not marked as externally visible, the optimizer is free to change its signature by removing dead arguments or removing the function entirely, for example.

In a dynamic library, symbols are considered externally visible by default, but in a standalone executable, symbols other than `main()` are internal by default. This behavior allows the optimizer to remove `fn2()` in the example in [Mixing LLVM Bitcode Files with Mach-O Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tcmztfvbuqmjnknltm). For more information on symbol visibility, see [Controlling Symbol Visibility](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/SymbolVisibility.html#//apple_ref/doc/uid/TP40001670).

### GCC-4.2 Features Not Available in LLVM-GCC-4.2

These are GCC 4.2 features that are not available in LLVM-GCC 4.2:

- Profile-guided optimization
- Auto vectorization
- Stack canaries
- Inline assembly that uses x87 registers
- Generating debug information for optimized code

### LLVM Open-Source Community Information

LLVM is supported by an active open-source community, whose home is located at [http://llvm.org](http://llvm.org/). You can interact directly with LLVM developers through the mailing lists available at this website.

> [!NOTE]
> 

### Submitting Feedback to Apple

Apple Developer Connection members can submit bug reports and technical-support inquiries:

- To submit bug reports, visit [https://bugreport.apple.com](https://bugreport.apple.com/).
- Send technical-support inquiries to `dts@apple.com`.

If you’re not an ADC member, vist [http://developer.apple.com](https://developer.apple.com/) to sign up.

For a list of Apple mailing lists, visit [http://lists.apple.com](http://lists.apple.com/).

### Xcode 3.1.1 Additions

These are the improvements made to LLVM-GCC 4.2 in Xcode 3.1.1:

- OpenMP support (with the inclusion of atomic built-in functions)
- Object-size checking; for example, `-D_FORTIFY_SOURCE=2`
- LLVM bitcode format change to align files to 16 bytes and to contain the CPU type to fix a problem with link-time optimization (LTO)
- Several ABI fixes:

  - In the 64-bit ABI, nonfragile Objective-C instance-variable sizes are calculated at runtime instead of compile time.
  - Fixed problem in which some Objective-C metadata is incorrectly generated for nonoptimized code.
  - Fixed minor vector-related ABI mismatches between GCC 4.2 and LLVM-GCC 4.2 on the x86-64 architecture.
  - Fixed a problem in which the alignment of a structure of a field assumes the alignment of the base of the structure.
  - Fixed a problem in which explicit trailing padding bytes of a structure with a trailing union didn’t fill out the structure completely.
- Debugging improvements and bug fixes:

  - Improved compilation time when the `-O0` and `-g` flags are used:

    - Unreferenced static functions are no longer emitted
    - Explicit names for variables in LLVM bitcode files are not used
    - DWARF output improvements to prevent unnecessary information duplication
    - Reduction of the amount of unnecessary work the compiler does when compiling for debugging
    - Improvement of the compiler’s memory management
  - Debug information is emitted for data-only files
  - The linker accepts some command-line options (such as `-mllvm`) to turn on LTO debugging, statistics dumping, and so on
  - Fixed memory corruption problem with precompiled headers (PCH)
