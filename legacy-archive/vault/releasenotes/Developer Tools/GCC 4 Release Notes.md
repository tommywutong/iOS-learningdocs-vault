---
title: GCC 4 Release Notes
apple_id: TP40001825
resource_type: Release Note
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-GCC4/index.html
archived_at: '2026-07-18T02:50:26.731183Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# GCC 4.0 Release Notes

> [!IMPORTANT]
> 

#### Contents:

- [Xcode 3.0 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrvfvjvomy)
- [Xcode 2.4 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrvfvjvona)
- [Xcode 2.3 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrvfvjvonq)
- [Xcode 2.2 release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrvfvjvomjw)
- [Xcode 2.1 release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrvfvjvomjx)
- [Mac OS X v10.4 Xcode Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrvfvjvomjy)

### Xcode 3.0 Release

64-bit Objective C or Objective C++ uses the new ObjC2 ABI.

The behavior of `-mmacosx-version-min` has changed. Previously, this flag would default to 10.1 when building for PowerPC and 10.4 when building for Intel. Now it will default to the system version on which the compiler is running. When using an SDK through the command line it is strongly recommended to explicitly set `-mmacosx-version-min`.

Two new security features have been backported from later versions of gcc into this release: `-fstack-protector` and `__builtin_object_size`. Object size checking can be enabled for C code by using `-D_FORTIFY_SOURCE=1` or `-D_FORTIFY_SOURCE=2`.

### Xcode 2.4 Release

### 64-bit

This compiler release adds support for the Intel 64bit architecture. This rounds out our architecture support to include 32bit and 64bit code generation for both PPC and Intel based platforms.

### Xcode 2.3 Release

Apple's GCC 4.0 is now based on version 4.0.1 of the Free Software Foundation's GNU Compiler Collection.

### Changes in command-line options

- `-fno-nested-functions` is the default for C and Objective-C which disables nested functions by default. `-fnested-functions` can be used to enable support for nested functions.
- The `-fuse-cxa-atexit` flag is now working and on by default, which means that destructor ordering is now correctly the inverse of constructor ordering, and bundles may be unloaded when running on Mac OS v10.4 and higher.
- `-ggdb` now produces DWARF, since this gives better debugging than STABS.
- The `-fnasm` flag was removed from the compiler; users should use nasm directly if running GCC from the command-line.

### Optimization

- Optimization for code size (`-Os`) optimizes for size, but not at the expense of speed. `-Os` enables all `-O2` optimizations that do not typically increase size. However, instructions are chosen for best performance, regardless of size.
- Optimization for code size at any cost (`-Oz`) optimizes for size, regardless of performance. `-Oz` enables the same optimization flags that `-Os` uses, but `-Oz` enables instructions that encode into fewer bytes.

### 64-bit

The CALL_ON_UNLOAD pragma, which never worked, has been made an error. Users should use '__attribute__(\ (destructor))' or another alternative.

### Support for section attribute on functions

This version of the compiler now supports the section attribute on functions. For example, the following code will assign function foo into section __bar of segment __TEXT:

```
    void foo (void) __attribute__((section("__TEXT,__bar")));
    void foo (void) { }
```


### x86

`long long` is now used as principal type for Vector intrinsic type `__m64`. This is a C++ ABI change. Now function names, whose signature includes `__m64`, are mangled differently.

### C++

Now #pragma visibility(default) wrappers are added around to ensure that the exception classes are not hidden.

### DWARF

DWARF debugging format is now supported. However, STABS is still used as default debugging format. In subsequent releases, DWARF will be used as default debugging format.

### Major bugs fixed in this release of GCC 4.0

- Radar 4053179: gcc-5001: Conditional vector operation is not supported by auto vectorizer.
- Radar 4299630: Xcode linking fails with warnings about relocation overflow
- Radar 4333194 Rotoshape crashes Intel Release builds crash at optimization levels above 1.
- Radar 4334498 var obj created for STL string is 'out of scope'.
- Radar 4343764 Link error after XCode 2.2 update (std::__ioinit, fixed by turning off "Separate PCH Symbols").
- Radar 4375453 -ftree-vectorize results in a misaligned stack (bad codegen).
- Radar 4382844 GCC halts and reports internal error.
- Radar 4458276 gcc bus error while precompiling.
- Radar 419339 Wrong warning with gcc version 4.0
- Radar 4505813 Definition of MMX/SSE constants not working as expected
- Radar 4493694 GCC crash when precompiling the attached header on x86

### How to build the compiler from source

The source code for the Apple GCC 4.0 compiler is now available for download using anonymous svn from `svn://gcc.gnu.org/svn/gcc/branches/apple/200605-release`

The file `README.Apple`, in the top level source directory, explains how to build the compiler.

### Xcode 2.2 release

### Xcode 2.1 release

### Mac OS X v10.4 Xcode Release

These notes describe Apple's GCC 4.0, which is based on version 4.0 of the Free Software Foundation's GNU Compiler Collection. GCC 4.0 will be the default compiler on Mac OS X for C, C++, Objective-C, and Objective-C++ source code after this package is installed. GCC 3.3, which was the default compiler in the Mac OS X 10.3 Development Tools, continues to be provided for backward compatibility.

These release notes are not comprehensive. For a complete list of compiler changes, please also consult the release notes for previous Mac OS X Developer Tools releases, the FSF 3.4 release notes, and the FSF 4.0 release notes.

### Switching to GCC 4.0

The Xcode Tools package provides two compilers: GCC 3.3, based on version 3.3 of the Free Software Foundation's GCC compiler suite, and GCC 4.0, which is based on version 4.0 of the Free Software Foundation's GCC compiler suite. GCC 2.95 and GCC 3.1 are no longer provided.

Here are some important things to keep in mind before you switch from an earlier compiler version to GCC 4.0.

- Recompile all your C++ and Objective-C++ code, including all libraries and frameworks that export a C++ interface. The application binary interface (ABI) for C++ programs changed between GCC 3.1 and GCC 3.3, and again between GCC 3.3 and GCC 4.0. The changes are small bug fixes, but are still large enough to prevent a mixed C++ program from operating correctly. _Do not link C++ modules compiled with one of these compilers against modules compiled with the other._ Even if the modules appear to link correctly, C++ ABI differences may still cause problems that will not manifest themselves until run time.
- You do not need to recompile C or Objective-C code (unless you're using long double as described below). The C and Objective-C ABI has not changed.
- You do not need to recompile C or Objective-C code (unless you're using long double as described below). The C and Objective-C ABI has not changed.
- Test your code. Even if the compiler doesn't raise any errors or warnings, your code may rely on idiosyncrasies in previous compilers that GCC 4.0 handles differently. As one example, where order of execution is undefined there are cases where gcc 3.3 and gcc 4.0 make different choices.

### Switching between compilers

Both compilers may coexist on the same system. GCC 3.3 is always available as `/usr/bin/gcc-3.3`, and GCC 4.0 is always available as `/usr/bin/gcc-4.0`. In addition, there are symbolic links at `/usr/bin/cc` and `/usr/bin/gcc` that point to the selected compiler. By default, the selected compiler is GCC 4.0.

If you have a lot of make files and shell scripts that refer to `/usr/bin/cc` or `/usr/bin/gcc`, changing all those references to your compiler of choice may be impractical. In that case, use the gcc_select command to change the selected compiler.

To use GCC 3.3 as the selected compiler:

- Open the Terminal, and enter `sudo /usr/sbin/gcc_select 3.3`. If you're asked, enter your password.
- This command line logs in as root, makes the neccesary changes, and leaves you logged in under your original account. When it's done, `/usr/bin/cc` and `/usr/bin/gcc` use GCC 3.3.

To use GCC 4.0 as the selected compiler:

- Open the Terminal, and enter `sudo /usr/sbin/gcc_select 4.0`. If you're asked, enter your password.
- This command line logs in as root, makes the neccesary changes, and leaves you logged in under your original account. When it's done, `/usr/bin/cc` and `/usr/bin/gcc` use GCC 4.0.

### Switching between compilers in Xcode

To set the compiler for a classic (Jambase) target, double-click on the target in the project window to open it in an editor. Choose Settings -> Simple View -> GCC Compiler Settings. Select the compiler with which you wish to build the target using the _Compiler version_ popup.

To set the compiler for a native target, bring up the inspector for the target. Select the _Build Rules_ tab. If the compiler shown in the System C Rule is not the desired compiler, then add a new build rule by clicking on the + button. Configure your new build rule to process "C source files" using the desired version of GCC. If you wish to revert to using the system compiler, you can delete the build rule.

### Documentation

Documentation for the 4.0 compiler is available in /Developer/ADC Reference Library/documentation/DeveloperTools/gcc-4.0.0.

Documentation for the 3.3 compiler is available in /Developer/ADC Reference Library/documentation/DeveloperTools/gcc-3.3.

Look for additional and updated documentation on the [ADC web site](https://developer.apple.com/referencelibrary/DeveloperTools).

### Source code compatibility issues

### Changes related to C++ templates

GCC 4.0 has moved much closer to full conformance with the C++ standard; the only remaining C++ language feature that is not yet supported is export. As a result of this better conformance, some incorrect programs that were accepted by GCC 3.3 will have to be modified for compilation with GCC 4.0. This section describes some of the main issues; see the FSF 3.4 release notes and the FSF 4.0 release notes for a more complete list.

Complete template specialization requires the `template<>` syntax, as described in the C++ standard. (This is because of uniformity between complete specialization and partial specialization.) For example:

```
template<> class X<int> { ... };
```

is a syntactially valid template specialization, but

```
class X<int> { ... };
```

is not. Earlier versions of GCC incorrectly accepted the latter form.

GCC 4.0 now implements "two-phase name lookup" correctly. This has the following consequences:

- Within a template, you have to use the the `typename` keyword when a nested type depends on a template parameter. For example, if `T` is a template parameter, you have to write `typename list<T>::iterator`, not just `list<T>::iterator`. Without the typename, the compiler will parse this under the assumption that the name iterator doesn't refer to a type. (See section 14.6 of the C++ standard for more details.)
- Names that do not depend on a template parameter are looked up at the point of template definition, not the point of instantiation. Within a template, for example, `f(3)` means whatever overload of `f` best matches an `int` argument _at the point where the template is defined_. If there is no appropriate version of `f` in scope then this is an error, even if such a function is declared later on.
- If a class template inherits from another class template, then base class members won't be found unless they are qualified. (See section 14.6.2, paragraph 3, of the C++ standard.) For example:

```swift
template <typename T> struct Base {
    void f();
};

template <typename T> struct Derived : public Base<T> {
    void g() {
        f();          // Error, name not found.
        this->f();    // OK
        Derived::f(); // OK
        Base<T>::f(); // OK
    }
};
```

  See the GCC 4.0 manual for more information about two-phase name lookup.

### Generalized lvalues

The C and C++ languages distinguish between _lvalues_ and _rvalues_. Informally, the names "l" and "r" come from the left- and right-hand side of assignment statements. An lvalue refers to some location in memory, and an rvalue may be a temporary result that doesn't correspond to a memory location.

Previous versions of GCC supported a partially documented "generalized lvalue" extension: they treated certain expressions as lvalues even though the relevant language standards said they were not. GCC supported _cast as lvalue_, _conditional as lvalue_, and _compound expression as lvalue_. That is, previous versions of GCC allowed the following constructs, which the C and C++ standards say are illegal:

```
(int) x = 17; (is_ok ? x : y) = 3; (x, y) = 0;
```

All of these generalized lvalue extensions have been removed from the FSF version of GCC; see the FSF 3.4 release notes.

In Apple's version of GCC 4.0, generalized lvalues are _deprecated_. GCC 4.0 will accept code that uses cast-as-lvalue and conditional-as-lvalue for this release only, but the compiler will issue a warning. Generalized lvalues will be removed in a future release of Apple's version of GCC, to match the FSF version. To match the FSF behavior with GCC 4.0 (i.e. to get errors instead of merely warnings), use the `-fno-non-lvalue-assign` flag.

### Changes in command-line options

The following command-line flags have been removed from GCC 4.0:

- `-fcoalesce`
- `-fno-coalesce`
- `-fweak-coalesced`
- `-fno-weak-coalesced`
- `-fcoalesce-templates`
- `-fno-coalesce-templates`

There is no need to use `-fcoalesce`, `-fweak-coalesced`, or `-fcoalesce-templates`, since the behavior specified by those flags is now the default. Those flags can safely be removed from any projects that use them.

The vast majority of projects also have no need to use `-fno-coalesce`, `-fno-weak-coalesced`, or `-fno-coalesce-templates`. The projects that used those flags in earlier compiler versions usually did so as workarounds for compiler bugs that no longer exist, and those flags, too, can safely be removed. In the very rare cases where there is a real need to disable C++ "vague linkage", use the flag `-fno-weak`.

### Objective-C selector checking

When a message is sent to a receiver of type id, the compiler looks at all matching selectors and warns about argument type inconsistencies. The FSF version of GCC 4.0 is better at this than previous versions of GCC were, revealing inconsistencies that were previously hidden. To ease the transition, we have made Apple's version of GCC 4.0 slightly more lenient so that it will not warn about type inconsistencies so long as the types involved have the same size and alignment.

To match the behavior of the FSF version of GCC 4.0, specify `-Wstrict-selector-match`. Stricter selector type checking can be especially useful for framework vendors.

### 64-bit address space

GCC 4.0 on Tiger can build programs that run in a 64-bit address space. You do this by adding `-arch ppc64` to compile and link commands, or by choosing the `ppc64` architecture in Xcode 2.0. Note that programs compiled using this option will run only on a G5 machine.

The 64-bit programming model is "LP64", meaning that `int` remains 32 bits in size, while `long` and pointers are 64 bits. `long long` remains unchanged at 64 bits.

Most correctly-written code will not need any source changes, but beware of reading/writing binary files, uses of casts to store different types of data in the same memory location, and other low-level techniques that make assumptions about the sizes of fundamental types. By default 64-bit programs run in the low 4GB of the address space, but `malloc()` and other allocation calls will return 8-byte pointers, possibly with values far above four billion. Attempts to store these values in variables of type int will not go well, and a cast will merely silence the compiler's valid warning, not produce correct code.

64-bit programs use a 64-bit version of the Mach-O file format; these can be identified using the `file` command. 32-bit and 64-bit programs may not mix directly; a 64-bit application may use only 64-bit frameworks, and so forth. However 32-bit programs may use a shared memory region along with 64-bit programs.

It is possible to build an application that has both 32-bit and 64-bit versions bundled together (a "fat" binary); a G5 running Tiger will choose to run 64-bit version by default, otherwise the 32-bit version will be used. The debugger, GDB, can debug both types of programs.

In Tiger, only the System and Xcelerate frameworks have 64-bit versions, meaning that only C and C++ are supported (no Objective-C). Additional 64-bit frameworks may be available in future releases.

The 64-bit ABI is different from the 32-bit ABI in several ways; bool's are one byte in size, alignment in structs is "natural" (meaning that structs with pointer fields will be padded so the pointers are 8-byte aligned), and more kinds of structs are passed by value and in registers (for instance, a struct with three "double" fields will be passed using three float registers).

### New language features

### Source-level control of symbol visibility

GCC 4.0 supports finer grain control over which symbols defined in a dynamic library are external, meaning that they are visible to other programs that link to that dylib, and which are _private extern_, meaning they are visible throughout the dylib but hidden to the dylib's clients. The compiler uses _hidden visibility_ as a synonym for private extern, and _default visibility_ as a synonym for external.

The new mechanism consists of two parts: a new compiler flag to choose whether symbols are exported unless explicitly hidden or hidden unless explicitly exported, and new syntax for explicitly specifying a symbol's visibility in the source code itself. The compiler flag is `-fvisibility=`_vis_, where _vis_ is either `default` or `hidden`. Using `-fvisibility=hidden` means that all symbols have hidden visibility unless explicitly exported. Using `-fvisibility=default` means that all symbols have default visibility unless explicitly hidden. If you don't use either flag, the behavior is the the same as if you had used `-fvisibility=default`.

Visibility within source code is controlled by an _attribute_, which is a GCC language extension. `__attribute__ ((visibility("hidden")))` gives a declaration hidden visibility, and `__attribute__ ((visibility("default")))` gives it default visibility.

The visibility attribute may be applied to functions, variables, and C++ classes. It is not applicable to Objective-C classes.

See the C++ Runtime Environment Programming Guide for more details on symbol visibility. See the GCC 4.0 manual for more information about attribute syntax.

### Long double

In previous releases of GCC, the `long double` type was just a synonym for `double`. GCC 4.0 now supports true `long double`. In GCC 4.0 `long double` is made up of two `double` parts, arranged so that the number of bits of precision is approximately twice that of `double`.

> [!WARNING]
> 

### Coalescing across dylibs

In C++, if you instantiate a template with the same arguments in more than one file, these instantiations refer to the same thing. For example, if you take the address of function `f<int>` in two different files, you get the same address. A more useful example involves class templates with static member variables: given

```
template <typename T>>
struct X {
    static T x;
};
```

there should only be one copy of `X<int>::x` in the entire program, so if there is an assignment statement `X<int>::x = 17` in one file you should see the new value when you examine `X<int>::x` in a different file.

In previous GCC and Mac OS X releases this behaved correctly within a single executable or dylib, but not across the dylib boundary. In previous releases each dylib had its own copy of `X<int>::x`, so an assignment in one dylib was not reflected in other dylibs.

GCC 4.0 supports full coalescing both within and across dylibs. If a template instantiation has external visibility then all copies of it, in all dylibs, will be merged into a single copy.

If you want to ensure that a template instantiation in a dylib is _not_ merged with template instantiations in any other dylib, use the visibility attribute to give the template hidden visibility.

See the C++ Runtime Environment Programming Guide for more details.

### Initialization of C++ objects in Objective-C++ classes

When using Objective-C++, it is now possible for instance variables of Objective-C classes ("ivars") to be C++ objects with nontrivial destructors and default constructors. To enable this feature, use the `-fobjc-call-cxx-cdtors` flag.

When this flag is used, the compiler synthesizes a special `- (id) .cxx_construct` method that invokes the default constructors for all such ivars and a special `- (void) .cxx_destruct` method that invokes the destructors.

The `.cxx_construct` method will be invoked by the runtime immediately after a new object instance is allocated, and the `.cxx_destruct` methods will be invoked immediately before the runtime deallocates an object instance.

### libstdc++ dylib and C++ ABI stability

In Apple's previous releases of GCC the C++ runtime, `libstdc++`, was packaged as a static archive. In GCC 4.0 it is a dynamic library, `libstdc++.dylib`. This has important benefits for both correctness and performance.

C++ applications compiled with GCC 4.0 will run only on systems where `libstdc++.dylib` is installed. It is installed on all user systems that run Mac OS X v10.4, or that run 10.3.9 or later. To target earlier systems, use Xcode's SDK feature.

GCC 4.0 conforms to a multi-vendor C++ ABI, and Apple guarantees that this ABI will be maintained in future compiler releases. However, this ABI covers the core C++ langauge only, not the C++ runtime. Classes defined in `libstdc++` may change in an incompatible way in some future compiler release, so for maximum compatibility, a dylib that is designed to be compatible far into the future must avoid using `libstdc++` features anywhere in its exported interface.

For more information about `libstdc++` and about C++ binary compatibility issues see the C++ Runtime Environment Programming Guide. For more information about Xcode's SDK feature see "Using Cross-Development in Xcode" in the Xcode Help documentation from inside of Xcode.

### Support for bit-field reversing

Support is provided for the CodeWarrior pragma `reverse_bitfields`. This allows PowerPC applications to correctly access bitfield data that was created in a Windows or other x86 environment.

Bitfield allocation is reversed from what is ordinarily generated on the PowerPC.

```
#pragma reverse_bitfields  on | off | reset
```

This pragma has no effect when generating code for x86 processors.

### Optimization

GCC 4.0 has greatly improved code optimization. It has an entirely new optimization infrastructure based on a higher level intermediate representation, the Static Single Assignment form (SSA). Many new optimization passes based on this framework have been added, and many bugs and missed optimization opportunities have been fixed. For more information on this framework see the [Tree SSA project page](http://gcc.gnu.org/projects/tree-ssa/) and references therein.

### Levels of optimization

Xcode automatically chooses the recommended optimization level for you. Just be sure to build with the `xcodebuild` tool or to choose the Deployment build style before building your final product.

For deployment builds, the recommended setting is `-Os`, which produces the smallest possible binary size. Generally, a binary that's smaller is also faster. That's because a large application spends much of its time paging its binary code in and out of memory. The smaller the binary, the less the application needs to page. Since the disk is much slower than the CPU, optimizations that reduce the amount of work the CPU does, at the cost of increased paging, are usually a poor tradeoff. Smaller applications are also better for overall system performance.

For debugging versions, the recommended optimization level is `-O0`.

The different optimization levels are:

- No optimization (`-O0`). This option level is intended for debugging; it ensures that the debugger works as you would expect.
- Simple optimizations (`-O`) performs simple optimizations, including automatic register allocation and jump threading. This optimization level makes a trade-off between compile speed and execution speed.
- More optimizations (`-O2`) performs all of GCC's optimizations that don't involve a space-time trade-off. In addition to all the optimizations for level 1, it performs common subexpression elimination, strength reduction, and loop optimizations. It also considers any function declared with the inline keyword for inlining.
- Optimization for speed (`-O3`) performs still more optimizations. It may be best for code with heavy use of loops and much computation. In addition to all the optimizations for level 2, it considers all functions for inlining, even if they aren't declared with the inline keyword.
- Optimization for code size (`-Os`) produces the smallest binary size. It performs no loop unrolling or register renaming. The performance is similar to `-O2`.
- -fast: see Optimization using the -fast flag.

### Optimization using the -fast flag

`-fast` changes the overall optimization strategy of GCC 4.0 in order to produce the fastest possible running code for G4 and G5 architectures, at the expense of code size. Three flavors of `-fast` are provided to facilitate language specfic optimizations.

- `-fast` is the most common flag and is intended for C and C++.
- `-fastcp` is intended for C++ only. Currently it is identical to `-fast`, but its meaning may change in the future to allow for better C++ optimization.
- `-fastf` is not intended for general use, but only for C code generated by the NAG FORTRAN-to-C translator. It allows the compiler to optimize these programs better by relying on FORTRAN semantics.

`-fast` sets the optimization level to `-O3`, the highest level of optimization curretly allowed by GCC 4.0. If any other optimization level(`-O0`, `-O1`, `-O2`, or `-Os`) is specified, it is ignored by the compiler. Additionally, `-fast` enables extra optimization options. The exact list of options it enables may change in a future release, but currently it is:

- `-falign-loops-max-skip=15`
- `-falign-jumps-max-skip=15`
- `-falign-loops=16`
- `-falign-jumps=16`
- `-falign-functions=16`
- `-malign-natural`
- `-ffast-math`
- `-fstrict-aliasing`
- `-funroll-loops`
- `-ftree-loop-linear`
- `-ftree-loop-memset`
- `-mcpu=G5`
- `-mtune=G5`
- `-mpowerpc64`
- `-mpowerpc-gpopt`
- `-fsched-interblock`
- `-fgcse-sm`
- `-mdynamic-no-pic`

With only three exceptions, these options may not be overridden. The options enabled by `-fast` that may be overridden are `-mcpu=G5`, `-mtune=G5`, and `-mdynamic-no-pic`. The first may be overridden with `-mcpu=G3` or `-mcpu=G4`, the second may be overridden with `-mtune=G4`, and the last may be overridden with `-fPIC`.

There are important caveats to be aware of when considering the use of `-fast`:

- `-fast` enables floating-point transformations that are not permitted by the IEEE-754 standard. _If your application depends on strict IEEE-754 conformance, you should not use -fast or -fast-math._
- `-fast` allows the compiler to assume the strictest aliasing rules applicable to the language being compiled. For C and C++, this activates optimizations based on the type of expressions: an object of one type is assumed never to reside at the same address as an object of a different type, unless the types are almost the same. This will not change the behavior of programs that adhere strictly to the language standards but _it will cause programs that use types in nonstandard ways to behave incorrectly_. For example, the idiom `*((T*) &x) = val` is nonstandard (unless `x` and `T` already have the same type) and will not work reliably with `-fast` or `-fstrict-aliasing`.
- `-fast` changes the compiler's alignment mode to `-malign-natural`, which is not the default mode for 32-bit PowerPC. This can create binary compatibility issues, especially for C++, because the alignment mode affects structure and class layout. _Code compiled with -fast cannot always be linked against code compiled without it._

### Auto Vectorization

GCC 4.0 introduces a new optimization, _Auto Vectorization_. This feature allows the compiler to automatically transform suitable loops so that they use the processor's vector instructions, thus providing the performance gains of AltiVec while freeing programmers from the tedium of rewriting their code to use explicit AltiVec intrinsics.

To enable Auto Vectorization use the `-ftree-vectorize` flag. Caveats and limitations:

- This feature is available only at optimization level `-O2` or higher.
- This feature is useful only when the target CPU supports vector instructions (i.e. `-mcpu=G4` or higher). An auto-vectorized binary is not suitable for G3.
- Auto vectorization automatically enables `-fstrict-aliasing`. As described above, this will cause some programs, those that use types in nonstandard ways, to behave incorrectly.

See the GCC 4.0 documentation for more details.

### Compilation speed

Compilation speed, particularly for C++ programs that use precompiled headers, has improved significantly. GCC 4.0 with the Mac OS X v10.4 Development Tools builds typical C++ applications about 20% faster than GCC 3.3 with the Mac OS X v10.3 Development Tools did.

### Major bugs fixed in this release of GCC 4.0

- radar 3027082: In some cases -Os failed to make code as small as -O3 does.
- radar 3067823: Virtual inheritance didn't work with varargs functions.
- radar 3344103: Compiler would exhaust virtual memory compiling CPU2004 benchmark.
- radar 3385001: C++ front end didn't handle very large bitfields correctly.
- radar 3305878: thunks had inconsistent visbility depending on optimization level.
- radar 3222264: -frepo didn't work
- radar 3462971: template instantiation incorrectly instantiated const version for a reference.
- radar 3476909: typeinfo wasn't generated correctly when #pragmas were involved
- radar 3502162: ifstream didn't handle /dev/tty correctly
- radar 3619824: codegen for sqrt was unnecessarily bad
- radar 2177733: memmove wasn't recognized as a builtin by the compiler.
- radar 3165108: a friend declaration was ignored for a friend of a C++ template specialization.
- radar 3170976: Missed optimization opportunity: fmadd wasn't used effectively
- radar 2872232: Compiler should provide a tgmath.h
- radar 3191624: -save-temps didn't work with PCH.
- radar 3278745: -fshort-wchar worked correctly for C++, but not for C.
- radar 3323946: std::char_traits couldn't be instantiated for unsigned short.
- radar 3346713: zero-sized static objects didn't work.
- radar 3373515: set_terminate didn't affect C++ exception handling in other dylibs
- radar 3168188: it wasn't possible to override the default new and delete in C++ programs
- radar 3315288: compiler wasn't using -fexceptions when validating pch files
- radar 3016816: lazy dynamic initialization caused iostream deadlock
- radar 3418237: compiling Python at -O3 caused compiler crash.
- radar 3460707: bad codegen in trivial floating-point program
- radar 3593057: Extraneous loads and stores generated when passing objects by value
- radar 3593057: Extraneous loads and stores generated when passing objects by value

Many missed optimization opportunities have been fixed.

Many internal compiler errors have been fixed.

Many bugs affecting C++ template coalescing have been fixed. The typical symptom of these bugs was a mysterious failure at link time involving templates, usually either a multiple definition error or an undefined symbol error. If you have experienced these errors, it is likely that switching to 4.0 will fix them.

Many bugs involving C++ parsing have been fixed, especially bugs involving the ambiguity between the declaration of a function and the declaration of a variable initialized with constructor syntax.

### Known problems in this release of GCC 4.0

### Objective-C/Objective-C++ Exception Handling

GCC 4.0 may produce spurious warnings (in Objective-C) or errors (in Objective-C++) when the address of a non-static local variable is taken in a function that uses Objective-C exception handling constructs (enabled via the -fobjc-exceptions option). For example, compiling the following in Objective-C++:

```
extern void foo (int *arg1);
void bar (int arg) {
    int rcvr;
    @try {
        rcvr = arg;
    }
    @finally {
        foo (&rcvr);
    }
}
```

will produce the following error:

```
error: invalid conversion from 'volatile int*' to 'int*'
error:   initializing argument 1 of 'void foo(int*)'
```

This is a bug in the Tiger release of GCC 4.0, and will be fixed in a subsequent release. For the time being, an explicit cast will be needed to allow the code to compile:

```
foo ((int *)&rcvr);
```


### Optimization bugs when using -ftree-loop-linear

The new optimization flag `-ftree-loop-linear` is known to have bugs that cause incorrect code to be generated in some rare cases. Note this flag is included in `-fast`. This will be fixed in a future release.

### How to build the compiler from source

The source code for the Apple GCC 4.0 compiler is available for download using anonymous CVS from `gcc.gnu.org:/cvs/gcc` using module `gcc`. The development branch for this compiler is `apple-ppc-branch`, and the tag for the Mac OS X 10.4 Xcode Tools release is `apple-gcc-TigerGM`.

The file `README.Apple`, in the top level source directory, explains how to build the compiler.

### Ways in which Apple GCC 4.0 differs from gcc on other platforms

- Xcode Tools uses STABS as its debugging format, and does not support DWARF.
- Apple GCC 4.0 generates optimized STABS by default. That is, it emits debug symbols only for symbols that are actually used. The "generic" FSF GCC emits debug information for all symbols, regardless of whether they are used. The `-gfull` command line option directs the Apple GCC compiler to turn off STABS optimization and to emit debug information for all symbols, as the FSF GCC compiler does.
- Apple's version of GCC 4.0 supports both the FSF's AltiVec syntax and the older Motorola AltiVec syntax.
- Apple's version of GCC 4.0 supports Objective-C++, which is not yet present in FSF versions of GCC.
- Apple's version of GCC 4.0 supports inline assembly using syntax as in CodeWarrior, as well as the traditional GNU syntax for inline assembly. The FSF vesion of GCC 4.0 does not support CodeWarrior-style inline assembly.
- In the FSF's version of GCC 4.0, the `-fwritable-strings option` has been removed. (The [FSF 4.0 release notes](http://gcc.gnu.org/gcc-4.0/changes.html) recommend using named character arrays, instead of string literals, when writable strings are important.) This option is still present in Apple's version of GCC 4.0, but it may be removed from a future compiler release.
- The `-fast` option is specific to Apple's version of GCC 4.0. Some of the optimizations controlled by `-fast` are not yet present in the FSF version of GCC.
- Generalized lvalues have been removed from the FSF's version of GCC, but they are merely deprecated in Apple's current release of GCC. Apple will remove generalized lvalues in a future GCC release.
- Apple's version of GCC 4.0 does not have _mudflap_ support for pointer checking.
