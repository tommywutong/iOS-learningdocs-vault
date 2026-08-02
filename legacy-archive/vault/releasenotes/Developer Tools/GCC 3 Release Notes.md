---
title: GCC 3 Release Notes
apple_id: TP40001007
resource_type: Release Note
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-GCC3/index.html
archived_at: '2026-07-18T02:50:26.644101Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# GCC 3 Release Notes for Mac OS X v10.3

> [!IMPORTANT]
> 

These notes describe Apple's GCC 3.3, which is based on version 3.3 of the Free Software Foundation's GNU Compiler Collection. GCC 3.3 will be the default compiler on Mac OS X for C, C++, Objective-C, and Objective-C++ source code after this package is installed. GCC 3.1, which was the default compiler in the Mac OS X 10.2 Development Tools, continues to be provided for backward compatibility. GCC 2.95 is also still provided for backward compatibility.

The actual FSF GCC versions that each compiler in this release is based on are:

| gcc2 | 2.95.2 final release |
| gcc3 | 3.1 prerelease snapshot dated 2002-10-03 |
| gcc-3.3 | 3.3 prerelease snapshot dated 2003-03-04 |

#### Contents:

- [Switching to GCC 3.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvomq)
- [Documentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvoni)
- [Compiler option compatibility issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvonq)
- [Source code compatibility issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvony)
- [Precompiled headers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvooa)
- [New language features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvooi)
- [Compilation speed](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvomju)
- [Symbol Separation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvomjv)
- [Major bugs fixed in this release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvomjw)
- [Optimization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvomjx)
- [How to build the compiler from source](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvomrq)
- [Ways in which Apple GCC 3.3 differs from gcc on other platforms](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambxfvjvomrr)

### Switching to GCC 3.3

The Xcode Tools package provides three compilers: GCC 2, based on version 2.95 of the Free Software Foundation's GCC compiler suite, GCC 3 (also called GCC 3.1), based on version 3.1 of the Free Software Foundation's GCC compiler suite, and GCC 3.3, which is based on version 3.3 of the Free Software Foundation's GCC compiler suite.

Here are some important things to keep in mind before you switch from GCC 2 or GCC 3.1 to GCC 3.3:

- Recompile all your C++ and Objective-C++ code, including all libraries and frameworks that export a C++ interface. The application binary interface (ABI) for C++ programs changed between GCC 2 and GCC 3.1, and again between GCC 3.1 and GCC 3.3. The changes between GCC 2 and GCC 3.1 were comprehensive, including changes to name mangling, exception handling, and class layout and alignment. The changes between 3.1 and 3.3 are much smaller, but are still large enough to prevent a mixed C++ program from operating correctly. Do not link C++ modules compiled with one of these compilers against modules compiled with any of the other two compilers. Even if the modules appear to link correctly, C++ ABI differences may still cause problems that will not manifest themselves until run time.
- You do not need to recompile C or Objective-C code. The C and Objective-C ABI has not changed.
- Do not ignore warnings. GCC 3.3 enforces the C and C++ standards much more strictly. New warnings may point out errors that GCC 2 or GCC 3.1 overlooked.
- Test your code. Even if the compiler doesn't raise any errors or warnings, your code may rely on idiosyncrasies in GCC 2 or GCC 3.1 that GCC 3.3 handles differently.
- If you're creating kernel extensions that must run on Mac OS X 10.1 and earlier, you must use GCC 2. If the extensions will run only on Mac OS X 10.2 and later, you should use GCC 3.1 or GCC 3.3.

### Switching between compilers

All three compilers may coexist on the same system. GCC 3.3 is always available as /usr/bin/gcc-3.3, GCC 3.1 is always available as /usr/bin/gcc-3.1 and /usr/bin/gcc3, and GCC 2 is always available as /usr/bin/gcc2. In addition, there are symbolic links at /usr/bin/cc and /usr/bin/gcc that point to the selected compiler. By default, the selected compiler is GCC 3.3.

However, if you have a lot of make files and shell scripts that refer to /usr/bin/cc or /usr/bin/gcc, changing all those references to your compiler of choice may be impractical. In that case, use the gcc_select command to change the selected compiler.

To use GCC 2 as the selected compiler:

- Open the Terminal, and enter `sudo /usr/sbin/gcc_select 2`. If you're asked, enter your password.
- This command line logs in as root, makes the necessary changes, and leaves you logged in under your original account. When it's done, /usr/bin/cc and /usr/bin/gcc use GCC 2.

To use GCC 3.1 as the selected compiler:

- Open the Terminal, and enter `sudo /usr/sbin/gcc_select 3.1` or `sudo /usr/sbin/gcc_select 3`. If you're asked, enter your password.
- This command line logs in as root, makes the necessary changes, and leaves you logged in under your original account. When it's done, /usr/bin/cc and /usr/bin/gcc use GCC 3.1.

To use GCC 3.3 as the selected compiler:

- Open the Terminal, and enter `sudo /usr/sbin/gcc_select 3.3`. If you're asked, enter your password.
- This command line logs in as root, makes the necessary changes, and leaves you logged in under your original account. When it's done, /usr/bin/cc and /usr/bin/gcc use GCC 3.3.

To see which compiler version you are using, enter `gcc -v`. For more help on gcc_select, enter `/usr/sbin/gcc_select -h`.

### Switching between compilers in Xcode

To set the compiler for your target for a classic (Jambase) target, double-click on the target in the project window to open it in an editor. Choose Settings -> Simple View -> GCC Compiler Settings. Select the compiler with which you wish to build the target using the _Compiler version_ popup.

To set the compiler for your target for a native target, bring up the inspector for the target. Select the _Build Rules_ tab. If the compiler shown in the System C Rule is not the desired compiler, then add a new build rule by clicking on the + button. Configure your new build rule to process "C source files" using the desired version of GCC. If you wish to revert to using the system compiler, you can delete the build rule.

### Documentation

Documentation for the 3.3 compiler is available in _GNU C/C++/Objective-C 3.3 Compiler_.

### Compiler option compatibility issues

- The compiler now checks that an option is valid for the current language, and warns if an invalid option is passed. For instance, `-frtti`, an option that only makes sense for C++, is no longer silently accepted by the C compiler.
- The `-traditional-cpp` option has changed. In Apple GCC 3.1 and earlier Apple GCC compilers, `-traditional-cpp` was used to toggle between the standard GNU GCC preprocessor and Apple's own preprocessor, "cpp-precomp". The GNU GCC compiler interpreted `-traditional-cpp` differently on all other platforms. Since cpp-precomp has been removed for Apple's GCC 3.3 compiler, the standard GNU meaning of `-traditional-cpp` has been restored. By default, the GCC 3.3 preprocessor conforms to the ISO C standard. Using the `-tradtional-cpp` option means the C preprocessor should instead try to emulate the old "K&R C".
- The `-nostdinc` option directs the compiler not to search for header files in the standard system directories. In previous compiler releases the implementation of this option was incomplete, and the compiler would still search for header files in standard umbrella frameworks. This bug has been fixed in the GCC 3.3 compiler: `-nostdinc` now removes all standard directories from the header search path, as it is supposed to.
- The Apple build number is now output with the `--version` option, and the format of the `-v` output has changed. The `--version` output is intended to be machine-parseable.

### Source code compatibility issues

Some source code will need to be changed when moving to GCC 3.3 because the new compiler adheres more closely to the rules of the relevant language standards. Here are some specific areas where you may notice a difference:

- The C++ Standard permits in-class initialization of static const member variables of integer types. Previous versions of the GCC compiler were more lax than that, and also allowed in-class initialization of static const member variables of pointer types. GCC 3.3 no longer permits this. This fix is simply to move the initialization to the member variable's definition.
- Taking the address of a cast, as in "&(int)p" is illegal, in both C and C++. The C compiler has always enforced this rule, but the C++ compiler used to permit taking the address of a cast. This bug has now been fixed. If you have code that takes the address of casts, it will have to be fixed. The fix is simply to take the address and then cast the resulting pointer.
- As required by the C++ standard, the C++ compiler now issues a warning when the `offsetof` macro is applied to a non-POD type. The `-Wno-invalid-offsetof` compiler flag can be used to suppress this warning.
- In C++, the ordinary template name lookup rules now apply to names from a base class template that are referred to from a derived class template: that is, they must explicitly be written as dependent names. If a class template `D<T>` inherits from another class template `B<T>` then, to access names from `B<>` from within `D<>`, you should write "`B<T>::x`" instead of just "`x`". An alternative solution is for the derived class template `D` to include using-declarations of names that it needs to access from `B`.
- GCC 3.3 now supports hexadecimal floating-point numbers, as defined in the C99 Standard. There are rare constructs that may have to be changed as a result of this new feature: for example, GCC 3.1 interpreted the expression "0x5e-0x03" as a subtraction of two integer constants, and GCC 3.3 rejects it as a malformed hexadecimal floating point constant. The simplest fix is to put spaces around the minus sign.
- The GCC 3.3 preprocessor inserts a new pragma, `#pragma GCC set_debug_pwd`, as part of the new Distributed Builds feature. (See below.) This may surprise tools and scripts that depended on the exact form of preprocessed output from GCC. These scripts should be rewritten to ignore unrecognized pragmas.
- GCC 3.3 warns about nested comments when `-Wall` is turned on.
- The GCC 3.3 preprocessor does not support the use of token pasting to create new invalid tokens.
- GCC 3.3 enforces #import and #include semantics strictly compared to cpp-precomp.
- Because of the removal of cpp-precomp, the GCC 3.3 preprocessor is stricter and more standards compliant than cpp-precomp was. (Similar to the preprocessor used in 3.1 when using the `-no-cpp-precomp` flag.)

### Precompiled headers

Apple's 3.3 compilers support a new form of precompiled headers. The new form is available from Xcode; refer to the Xcode documentation for more information. If you're using some other build system, such as make, see the “3.20 Using Precompiled Headers” section of _GNU C/C++/Objective-C 3.3 Compiler_ for information on specific compiler options.

cpp-precomp is no longer supported in the GCC 3.3 compiler. GCC 3.3 ignores cpp-precomp specific options.

GCC 3.1's form of precompiled headers, "PFE", is no longer supported in GCC 3.3; use the new form instead.

### New language features

### STL debugging mode for C++

By default, libstdc++ is built with efficiency in mind, and therefore performs little or no error checking that is not required by the C++ standard. This release adds support for the _libstdc++ debug mode_, which performs run-time checking for correct usage of the C++ standard library. Incorrect usage (such as passing an iterator to the wrong container, or passing an invalid range to a generic algorithm) will result in a clear error message followed by an abort, rather than an unpredictable crash.

To enable STL debugging mode, compile your application with the `-D_GLIBCXX_DEBUG` compile flag. Note that this flag changes the sizes and behavior of standard class templates such as `std::vector`, and therefore you can only link code compiled with debug mode and code compiled without debug mode if no instantiation of a container is passed between the two translation units. This does not mean that you are required to recompile your entire application: for instance, if one source file uses `std::vector` but `std::vector` doesn't occur in its public interface, that file can be recompiled in debug mode even if the rest of the program is not compiled in debug mode.

When it is not feasible to recompile your application, or when only specific containers need checking, debugging containers are available as GNU extensions. These debugging containers are functionally equivalent to the containers used in debug mode, e.g., `__gnu_debug::vector<int>` is equivalent to `std::vector<int>` in debug mode, but the `__gnu_debug` versions can be used in either release or debug mode without changing semantics.

Pedantic debug mode checks not only for errors, but also for usages that rely on GNU extensions and that, while correct, may not be portable to other compilers. In pedantic mode, for example, constructing an `std::string` with a null pointer will result in an abort, not an exception. Pedantic debug mode is not the default. To enable pedantic debug mode, compile your program with both `-D_GLIBCXX_DEBUG` and `-D_GLIBCXX_DEBUG_PEDANTIC`.

STL debugging mode is recommended during development or when you suspect an error caused by incorrect use of the C++ standard library. It is not recommended for deployment builds, because it introduces substantial overhead.

### Wide character support

Mac OS X 10.3 adds support for the `wchar_t` data type and for the library functions that manipulate wide strings, as required by the ISO C99 standard. On Mac OS X 10.3, GCC 3.3 adds support for wide character manipulation in C++. For example, `std::wstring` is now enabled.

Note that wide character support is unavailable on previous releases of Mac OS X. Programs that are intended to be run on previous versions of Mac OS X should avoid `wchar_t` and `wstring`.

Wide character support is provided for compliance with the ISO C and C++ standards, and for ease of porting applications from other operating systems. New Mac OS X applications should instead use Apple's Unicode APIs, such as CFString and NSString.

### ObjC/ObjC++ exception and synchronization support

The Objective-C language now offers syntactic support for structured exception handling that is similar to what is offered by C++ and Java. To enable the new syntax, you must pass the '-fobjc-exceptions' options to the ObjC/ObjC++ compiler, and/or set the MACOSX_DEPLOYMENT_TARGET environment variable to "10.3".

```
    @try {
      ...
         @throw expr;
      ...
    }
    @catch (AnObjCClass *exc) {
      ...
        @throw expr;
      ...
        @throw;
      ...
    }
    @catch (AnotherClass *exc) {
      ...
    }
    @catch (id allOthers) {
      ...
    }
    @finally {
      ...
    }
```

The @throw statement may appear anywhere in an Objective-C program; when used inside of a @catch block, the @throw may appear without an argument (as show above), in which case the object caught by the @catch will be rethrown.

Note that only (pointers to) Objective-C objects may be thrown and caught using this scheme. When an object is thrown, it will be caught by the nearest @catch clause capable of handling objects of that type, just as is the case in C++ and Java. A @catch(id) clause (as shown above) may also be provided to catch any and all Objective-C exceptions not caught by previous @catch clauses.

The @finally clause, if present, will be executed upon exit from the immediately preceding @try-@catch section. This will happen regardless of whether any exceptions are thrown, caught or rethrown inside the @try-@catch section, just as is the case in Java.

There are several caveats to using the new exception mechanism:

- Although currently designed to be binary compatible with NS_HANDLER-style idioms provided by the NSException class, the new exceptions can only be used on Mac OS X 10.3 (Panther) and later systems, due to additional functionality needed in the Objective-C runtime.
- As mentioned above, the new exceptions do not support handling types other than Objective-C objects. The Objective-C exception model does not interoperate with C++ exceptions at this time. This means you cannot throw an exception from Objective-C and catch it from C++, or vice versa.

The `-fobjc-exceptions` switch also enables the use of synchronization blocks for thread-safe execution:

```
   ObjCClass *lockObject = ...;
   ...
   @synchronized (lockObject) {
     ...
   }
```

Unlike Java, Objective-C does not allow for entire methods to be marked @synchronized. Note that throwing exceptions out of @synchronized blocks is allowed, and will cause the guarding object to be unlocked properly.

### Inline Assembly

In addition to the traditional GCC syntax for inline assembly, Apple GCC 3.3 now supports inline assembly using syntax as in CodeWarrior, which allows you to write assembly instructions in function bodies the same way as you do for assembly source files. Both asm functions and asm blocks within functions are available. This feature is not turned on by default; use -fasm-blocks to enable.

In general, the syntax and capabilities are exactly the same as what is documented for CodeWarrior, and so the assembly code can refer to variables and local parameters, use structure fields for offsets, and so forth. (The Apple GCC manual includes a short section describing the basics of the syntax.) However, the implementation is new, and some bugs did not get fixed in time for this release.

1. Function names cannot be referenced in the block; they will be interpreted as (undefined) labels, resulting in an error. There is no workaround.
2. Macros whose expansions include one or more instruction opcodes will result in syntax errors. For instance,

```
#define INSN_SEQ(X,Y) \
  mr r9,X \
  mr Y,r9

asm void fn() {
  INSN_SEQ(r3,r4)
}
```

   should work, but fails. This is a side-effect of the preprocessor being integrated in 3.3; a slow but reliable workaround is to use -save-temps. Beware that -save-temps will leave preprocessor output and assembly files behind, and you will need to clean those up manually.

### Compilation speed

Compilation speed in GCC 3.3 is significantly faster than it was in GCC 3.1, particularly for C++ projects that use precompiled headers. In addition to the general speedup, there are several special features that are related to compilation speed.

The following features are available from Xcode:

- The _Distributed Build_ feature makes it possible to farm a project build to several different machines.
- _ZeroLink_ makes it possible to avoid static link during a development build. This feature is particularly useful for builds where only a small number of files change.
- _Fix and Continue_ enables some changes (particularly changes within a function body) while a program is still running.

### Symbol Separation

_Symbol Separation_ is not yet available from Xcode, but it is available by explicitly providing command-line options to the compiler.

If your project contains large headers that are included in many different source files, Symbol Separation makes it possible to put the debug symbols from those headers in a separate repository. The compiler can thus save disk space and I/O time, because it no longer has to put the debug symbols into every object file where the headers are included. Symbols repositories are themselves normal object files, and can be supplied to the linker so that the debug information is included in the final executable.

To create the symbol repository for a header file foo.h, use the following command:

```
    gcc-3.3 <other flags> -fsave-repository=
cinfo_dir_name
 foo.h
```

This command will create two files:

- `foo.cinfo` in the _cinfo_dir_name_ directory.
- An output file, which by default is foo.h.o in the current folder. As usual, the name and location can be changed from the default by explicitly using the `-o` compiler flag.

To use the repository in subsequent compilations, you must provide the `-grepository` command line option. The compiler will then search for `.cinfo` files in all include paths.

### Major bugs fixed in this release

- Type checking has been fixed and improved in many situations involving Objective-C message dispatching and protocol lookup.
- Type checking has been fixed and improved in many situations involving Objective-C protocols.
- In Objective-C when -Wselector is used, check the whole list of selectors at the end of compilation, and emit a warning if a @selector() is not known.
- In C++, a number of bugs involving static member variables of class templates have been fixed.
- An bug in the C++ I/O library, which involved EOF being signaled incorrectly and sometimes required multiple carriage returns in interactive input, has been fixed. (Radar 3027668, 3043108, 3057353, 3057473, 3066494, 3068598 and many other duplicates.)
- A C++ front end bug, which caused an internal compiler error for some template friend declarations where the friend class template was defined in a namespace, has been fixed. (Radar 3081259)
- The Altivec type vector `bool` is now being treated correctly as a distinct type. In previous compiler versions it was being treated incorrectly as a synonym for unsigned.
- The printf formatting macros for `int32_t` and `uint32_t` in `<inttypes.h>` have been fixed.
- An bug in tail recursion optimization, which sometimes caused incorrect code generation at -O2 and above, has been fixed. (Radar 3109864)

### Optimization

GCC 3.3 has greatly improved code optimization, especially for Altivec code. If you've turned off optimization before, particularly if you are switching from GCC2, it's recommended that you turn it on now. Many bugs and inefficiencies have been fixed.

Xcode automatically chooses the recommended optimization level for you. Just be sure to build with the pbxbuild tool or to choose the Deployment build style before building your final product.

For deployment builds, the recommended setting is -Os, which produces the smallest possible binary size. Generally, a binary that's smaller is also faster. That's because a large application spends much of its time paging its binary code in and out of memory. The smaller the binary, the less the application needs to page. For example, say a binary uses aggressive function inlining. That binary saves time with fewer function calls, but it could easily spend far more time paging the binary code containing those inlined functions in and out of memory.

For debugging versions, the recommended optimization level is -O0.

Here are the different levels for C, C++, Objective-C and Objective-C++:

- No optimization (-O0). This option level is intended for debugging; it ensures that the debugger works as you would expect.
- Simple optimizations (-O) performs simple optimizations, including automatic register allocation and jump threading. This optimization level makes a trade-off between compile speed and execution speed.
- More optimizations (-O2)performs all of GCC's optimizations that don't involve a space-time trade-off. In addition to all the optimizations for level 1, it performs common subexpression elimination, strength reduction, and loop optimizations. It also considers any function declared with the inline keyword for inlining.
- Optimization for speed (-O3) performs still more optimizations. It can be best for code that contains lots of loops and computation. In addition to all the optimizations for level 2, it considers all functions for inlining, even if they aren't declared with the inline keyword.
- Optimization for code size (-Os) produces the smallest binary size. It performs no loop unrolling, scheduling optimizations, or register renaming. The performance is similar to -O2.
- `-fast`: see below.

When performing function inlining, GCC 3 inlines forward-referenced functions in addition to the functions it inlined before. A function is inlined if it's smaller than the inlining limit. The default limit is 600 internal GCC instructions. To raise the limit, add -finline-limit=number to the command line. Raising this limit too high can slow down compiling, increase the size of your executables with too much inlining, and lower execution speed.

Here are some interesting optimizations that aren't included by -O2 or -O3:

|  |  |
| --- | --- |
| **`-faltivec`** | : Optimizes code for Altivec. Code built with this flag might not run on G3 processors. |
| **`-mtune=G3 -mtune=G4 -mtune=G5`** | : Optimizes for speed on the indicated chip. The default is close to G4, but produces slightly smaller and slower code. Code built with these flags will still run on any processor; if you only want code that runs on one processor, you may use `-mcpu=G4` and similar.  When `-mtune=G5` is used in conjunction with -O3, the following alignment flags should also be enabled for optimum performance:   - `-falign-loops-max-skip=32` - `-falign-jumps-max-skip=32` - `-falign-loops=16` - `-falign-jumps=16` - `-falign-functions=32` |
| **`-mdynamic-no-pic`** | : Produces better code for references to static and global data. Generally, you should use this option when building an executable. Do not use it when building shared libraries or plug-ins because the produced code is not valid for them. |
| **`-funroll-loops`** | : Unrolls loops. Unrolling makes the code larger, but may make it faster by reducing the number of branches executed. |
| **`-ffast-math`** | : Enables some floating point optimizations that are not IEEE754-compliant, but which usually work. Programs which require strict IEEE compliance may not work with this option. |
| **`-fstrict-aliasing`** | : Optimize code by making more aggressive assumptions about whether pointers can point to the same objects as other pointers. Programs which use pointers a lot may benefit from this, but programs that don't strictly follow the ISO C rules about the type with which an object may be accessed may behave unexpectedly. |

### Optimization using the new -fast flag

-fast changes the overall optimization strategy of GCC 3.3 in order to produce the fastest possible running code for G4 and G5 architectures. Optimizations under -fast are roughly grouped under the following categories.

1. `-fast` sets the optimization level to -O3, the highest level of optimization supported by GCC 3.3. If any other optimization level (`-O0`, `-O1`, `-O2` or `-Os`) is specified, it is ignored by the compiler.
2. Alignment. Assume alignments for loops, functions, branches and structure data fields that provide fastest performance on the PowerPC. `-fast` sets the following alignment-specific options:

   - `-falign-loops-max-skip=15`
   - `-falign-jumps-max-skip=15`
   - `-falign-loops=16`
   - `-falign-jumps=16`
   - `-falign-functions=16`
   - `-malign-natural`
3. `-fast` enables the `-ffast-math` option, which allows certain unsafe math operations for performance gains.
4. Strict aliasing rules. -fast allows the compiler to assume the strictest aliasing rules applicable to the language being compiled. For C and C++, this activates optimizations based on the type of expressions: an object of one type is assumed never to reside at the same address as an object of a different type, unless the types are almost the same. Furthermore, struct field references are assumed not to alias each other as long as their direct and indirect enclosing structure types are distinct. -fast enables the following aliasing options:

   - `-frelax-aliasing`
   - `-fgcse-mem-alias`

   Warning: the behavior of standard-conforming programs will not be affected by strict aliasing, but programs that make use of nonstandard type conversions may behave in unexpected ways.
5. `-fast` enables various performance-related code transformations. These include loop unrolling, transposing nested loops to improve locality of array element access, conversion of certain initialization loops to memset calls, and inline expansion of calls to library functions such as floor. `-fast` enables the following code transformation options:

   - `-funroll-loops`
   - `-floop-transpose`
   - `-floop-to-memset`
   - `-finline-floor` (G5 only)

   Some of these transformations increase code size.
6. G5 specific instruction generation. With -fast (unless `-mcpu=G4` is specified), GCC 3.3 generates instructions which are specific to G5 and result in performance gain for G5. The following options are assumed for G5 under `-fast`:

   - `-mcpu=G5`
   - `-mpowerpc64`
   - `-mpowerpc-gpopt`
7. Scheduling changes. `-fast` option allows inter-block scheduling, and scheduling specific to the G5 architecture. One such scheduling change is load after a store that partially loads what was stored. The following scheduling-related options are enabled by `-fast`:

   - `-mtune=G5` (unless `-mtune=G4` is specified)
   - `-fsched-interblock`
   - `-fload-after-store`
   - `--param max-gcse-passes=3`
   - `-fno-gcse-sm`
   - `-fgcse-loop-depth`
8. `-fast` enables intermodule inlining when all source files are placed on the same command line. The following options are set by `-fast` and affect such inlining:

   - -funit-at-a-time
   - -fcallgraph-inlining
   - -fdisable-typechecking-for-spec
9. `-fast` sets `-mdynamic-no-pic` by default. This allows for generation of non-relocatable code and is not suitable for shared libraries. This option may be overridden by `-fPIC`.

Users of `-fast` should be aware of the following caveats:

- Because `-fast` enables highly aggressive optimizations, some of which may have an effect on code size or on program behavior, thorough testing is especially important before deploying applications compiled with `-fast`.
- For maximum run-time performance you should experiment with a variety of optimization options; no one set of flags is best for all applications.
- In future releases of GCC, -fast may enable a different set of optimization options. The intention behind this option is that -fast will enable optimizations that result in the fastest code for most applications.
- The `-malign-natural` option incorporated in `-fast` results in non-ABI-conforming code, which can cause problems when mixing code compiled with and without `-fast`. In particular, some of the functions in the C++ I/O libraries do not currently work properly on MacOSX 10.3 when linked with code compiled `-fast`. Use `-fastf` (below) for C++ on MacOSX 10.3.

### Optimization using the new -fastf flag

`-fastf` is just like `-fast` (above), except that it does not set `-malign-natural`. This is useful for cases where the ABI incompatibilities introduced by `-malign-natural` cause problems. In particular, C++ on MacOSX 10.3 should use `-fastf` rather than `-fast`.

### How to build the compiler from source

The source code for the Apple GCC 3.3 compiler is available for download using anonymous CVS from `:pserver:anonymous@anoncvs.opensource.apple.com:/cvs/root` using password `anonymous` and module `gcc3`. See the “Source Code” section of _GNU C/C++/Objective-C 3.3 Compiler_ for more information about how to obtain specific compiler versions using CVS. The opensource.apple.com repository may also contain compilers that are more up-to-date (and less stable) than the compiler in this release.

The file `README.Apple`, in the top level source directory, explains how to build the compiler.

### Ways in which Apple GCC 3.3 differs from gcc on other platforms

- Xcode Tools uses STABS as its debugging format, and does not support DWARF.
- Apple GCC 3.3 generates optimized STABS by default. That is, it emits debug symbols only for symbols that are actually used. The "generic" FSF GCC emits debug information for all symbols, regardless of whether they are used. The `-gfull` command line option directs the Apple GCC compiler to turn off STABS optimization and to emit debug information for all symbols, as the FSF GCC compiler does.
- Apple GCC 3.3 removes empty BINCL/EINCL STABS. This is helpful in improving GDB startup time. This optimization will be available in FSF GCC 3.4.
- Apple GCC's implementation of Altivec uses the older Motorola syntax, as described in the Altivec PIM. The newer GNU syntax is not yet supported. (Programs using the GNU syntax may compile without messages, yet produce unexpected results at runtime.)
- Apple's version of GCC 3.3 supports precompiled headers (PCH). In the "generic" FSF GCC, precompiled headers will not appear until version 3.4.
- Apple's version of GCC 3.3 supports Objective-C++. In addition, Apple's Objective-C implementation contains numerous fixes and improvements, most notably exception and synchronization support (see above).
- Apple's version of libstdc++ supports STL debugging mode (see above). This feature is not yet present in the FSF version.
- The -fast option is specific to Apple's version of GCC 3.3. Some of the optimizations controlled by `-fast` are not yet present in the FSF version of GCC.
