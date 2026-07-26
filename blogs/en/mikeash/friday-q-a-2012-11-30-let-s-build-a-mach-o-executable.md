---
title: 'Friday Q&A 2012-11-30: Let''s Build A Mach-O Executable'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f5e089a6803c6ed6'
translated: false
---

> 原文：[Friday Q&A 2012-11-30: Let's Build A Mach-O Executable](https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)　·　mikeash.com Friday Q&A

Posted at 2012-11-30 17:59 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-12-14: Objective-C Pitfalls](https://www.mikeash.com/pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html)  
Previous article: [Friday Q&A 2012-11-16: Let's Build objc_msgSend](https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)  
Tags: [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [dwarf](https://www.mikeash.com/pyblog/?tag=dwarf) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [macho](https://www.mikeash.com/pyblog/?tag=macho)

Friday Q&A 2012-11-30: Let's Build A Mach-O Executable

by [Gwynne Raskind](http://www.darkrainfall.org/)

**The Right Tool For the Right Job**  
The best tool on OS X for producing binary files from assembly-language inputs is, of course, the assembler, `as`. But, if you try to build a raw binary from this, you'll find that `as` also functions as a static linker in its own right. This isn't what we're after.

A more flexible tool, in this particular respect, is `nasm`, the [Netwide Assembler](http://nasm.us/). `nasm` is installed by the Xcode commandline tools, but unfortunately, Apple ships a horrifyingly outdated version, 0.98.40, which dates back to 2007 in terms of bug fixes, and to 1999 for features. The most recent version at the time of this writing is 2.10.05, which can be installed with `port install nasm`, `brew install nasm`, or whatever other package manager of your choice. If you don't use a package manager, you can download and compile the source yourself.

`nasm` 2.x includes a number of useful things, like 64-bit support, and Mach-O output. We won't be using `nasm`'s Mach-O support, since the point of all this is to do it by hand, but it'd be kind of nice to build a 64-bit binary using 64-bit instructions instead of split 32-bit words!

**Reinserting the Prime Program**  
Here's the C source code for which we'll build our Mach-O binary. To keep the resulting binary relatively simple, I've written it to avoid importing more than the bare minimum of information:

```
    #define NULL ((void *)0L)
    extern int printf(const char * restrict format, ...);
    typedef long time_t;
    extern time_t time(time_t *sloc);

    int main(void)
    {
        printf("Hello, world #%ld!\n", time(NULL));
        return 0;
    }
```

Some things to notice:

- Rather than `#include <stdio.h>` and `#include <time.h>`, I've manually declared `printf()` and `time()`, defined the `time_t` type, and macroed `NULL`. This avoids emitting extra debug information for the various stuff defined in the standard headers.
- I've defined `main()` as taking no parameters. This is extremely poor practice in general, but because of C's calling conventions, it works correctly.
- I've used a format string that actually does a format replacement so that the compiler with which I produced my test files doesn't get all efficient and replace it with a `puts()` call instead.

This generates the following assembly (built with Clang 3.3svn at `-Os`):

```
            .section        __TEXT,__text,regular,pure_instructions
            .globl  _main
    _main:                                  ## @main
            .cfi_startproc
    ## BB#0:                                ## %entry
            pushq   %rbp
    Ltmp2:
            .cfi_def_cfa_offset 16
    Ltmp3:
            .cfi_offset %rbp, -16
            movq    %rsp, %rbp
    Ltmp4:
            .cfi_def_cfa_register %rbp
            xorl    %edi, %edi
            callq   _time
            leaq    L_.str(%rip), %rdi
            movq    %rax, %rsi
            xorb    %al, %al
            callq   _printf
            xorl    %eax, %eax
            popq    %rbp
            ret
            .cfi_endproc

            .section        __TEXT,__cstring,cstring_literals
    L_.str:                                 ## @.str
            .asciz   "Hello, world #%ld!\n"

    .subsections_via_symbols
```

The code itself is very straightforward: Inside the `__TEXT,__text` section, set up a stack frame, call `time()`, load the `L_.str` string, set `al` to zero, call `printf`, zero `eax`, tear down the stack frame, and return. Then, in the `__TEXT,__cstring` section, define the `L_.str` label to point to a zero-terminated ASCII string. Finally, declare that no symbols in this file occur inside basic blocks, which the linker uses during dead code stripping.

The rest of the directives are related to Call Frame Information, which is used for unwinding data ('.unwind_info' and `.eh_frame`, exception handling support) and debug information (`.debug_frame`). We'll be building the first two by hand.

For sanity's sake, I'll be omitting the full DWARF debugging information. Even for this very simple program it would represent a considerable addition to this already overlong article.

**The Start of a Mach-O Executable**  
Our `nasm` input file will be used to generate a Mach-O file, so we need to start it with a Mach-O header. We'll use the 64-bit Mach-O little-endian format, whose header looks like this:

```
    struct mach_header_64 {
        uint32_t    magic;      /* mach magic number identifier */
        cpu_type_t  cputype;    /* cpu specifier */
        cpu_subtype_t   cpusubtype; /* machine specifier */
        uint32_t    filetype;   /* type of file */
        uint32_t    ncmds;      /* number of load commands */
        uint32_t    sizeofcmds; /* the size of all the load commands */
        uint32_t    flags;      /* flags */
        uint32_t    reserved;   /* reserved */
    };

    /* Constant for the magic field of the mach_header_64 (64-bit architectures) */
    #define MH_MAGIC_64 0xfeedfacf /* the 64-bit mach magic number */
    #define MH_CIGAM_64 0xcffaedfe /* NXSwapInt(MH_MAGIC_64) */
```

Here's the `nasm` input for our Mach-O header:

```
    bits 64
    cpu x64

    __mh_execute_header:
        dd 0xfeedfacf   ; MH_MAGIC_64
        dd 16777223     ; CPU_TYPE_X86 | CPU_ARCH_ABI64
        dd 0x80000003   ; CPU_SUBTYPE_I386_ALL | CPU_SUBTYPE_LIB64
        dd 2            ; MH_EXECUTE
        dd 16           ; number of load commands
        dd ___loadcmdsend - ___loadcmdsstart    ; size of load commands
        dd 0x00200085   ; MH_NOUNDEFS | MH_DYLDLINK | MH_TWOLEVEL | MH_PIE
        dd 0            ; reserved
    ___loadcmdsstart:
```

The `bits` and `cpu` directives just tell `nasm` to run in 64-bit mode.

Immediately after the Mach-O header comes the load commands. There's a whole list of commands which are required for an executable, and a huge pile more which _might_ be in one. Clang produces 16 load commands for this executable. A load command looks like this:

```
    struct load_command {
        uint32_t cmd;       /* type of load command */
        uint32_t cmdsize;   /* total size of command in bytes */
    };
```

Each load command is actually larger than this; the `cmd` field tells the loader how to interpret the following data. Load commands **must** be aligned to an 8-byte boundary for 64-bit Mach-O files.

**Segments and Sections**  
Segments are the blocks of data and code which `dyld` actually maps into memory at runtime. Sections are subdivisions of segments. Segments and sections both have names, and quite a few are standard and predefined.

Here's our first segment command:

```
    ___pagezerostart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___pagezeroend - ___pagezerostart    ; command size
        db '__PAGEZERO',0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0            ; VM address
        dq 0x100000000  ; VM size
        dq 0            ; file offset
        dq 0            ; file size
        dd 0x0          ; VM_PROT_NONE (maximum protection)
        dd 0x0          ; VM_PROT_NONE (inital protection)
        dd 0            ; number of sections
        dd 0x0          ; flags
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___pagezeroend:
```

This is the `__PAGEZERO` segment, which predefines the entire lower 4GB of the 64-bit virtual memory space as inaccessible. Because of this segment, which is marked unreadable, unwriteable, and nonexecutable, dereferencing `NULL` pointers causes an immediate segmentation fault.

The next segment command is more complicated:

```
    ___TEXTstart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___TEXTend - ___TEXTstart    ; command size
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000  ; VM address
        dq 0x1000       ; VM size
        dq 0            ; file offset
        dq 0x1000       ; file size
        dd 0x7          ; VM_PROT_READ | VM_PROT_WRITE | VM_PROT_EXECUTE
        dd 0x5          ; VM_PROT_READ | VM_PROT_EXECUTE
        dd 6            ; number of sections
        dd 0x0          ; flags
    ___TEXTtextstart:
        db '__text',0,0,0,0,0,0,0,0,0,0 ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___codestart - ___TEXTload ; address
        dq ___codeend - ___codestart    ; size
        dd ___codestart ; offset
        dd 0            ; alignment as power of 2 (1)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x80000400   ; S_REGULAR | S_ATTR_PURE_INSTRUCTIONS | S_ATTR_SOME_INSTRUCTIONS
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___TEXTstubsstart:
        db '__stubs',0,0,0,0,0,0,0,0,0  ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___stubstart - ___TEXTload ; address
        dq ___stubend - ___stubstart    ; size
        dd ___stubstart ; offset
        dd 1            ; alignment as power of 2 (2)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x80000408   ; S_SYMBOL_STUBS | S_ATTR_PURE_INSTRUCTIONS | S_ATTR_SOME_INSTRUCTIONS
        dd 0            ; reserved1 (index into indirect symbol table)
        dd 6            ; reserved2 (size per stub)
        dd 0            ; reserved3
    ___TEXTstubhelperstart:
        db '__stub_helper',0,0,0    ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___stubhelpstart - ___TEXTload ; address
        dq ___stubhelpend - ___stubhelpstart    ; size
        dd ___stubhelpstart ; offset
        dd 2            ; alignment as power of 2 (4)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x80000400   ; S_REGULAR | S_ATTR_PURE_INSTRUCTIONS | S_ATTR_SOME_INSTRUCTIONS
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___TEXTcstringstart:
        db '__cstring',0,0,0,0,0,0,0    ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___strsstart - ___TEXTload ; address
        dq ___strsend - ___strsstart    ; size
        dd ___strsstart ; offset
        dd 0            ; alignment as power of 2 (1)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000002   ; S_CSTRING_LITERALS
        dd 0            ; reserved1
        dd 6            ; reserved2
        dd 0            ; reserved3
    ___TEXTunwindinfostart:
        db '__unwind_info',0,0,0    ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___uwstart - ___TEXTload   ; address
        dq ___uwend - ___uwstart    ; size
        dd ___uwstart   ; offset
        dd 0            ; alignment as power of 2 (1)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000000   ; no flags
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___TEXTehframestart:
        db '__eh_frame',0,0,0,0,0,0 ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___ehstart - ___TEXTload   ; address
        dq ___ehend - ___ehstart    ; size
        dd ___ehstart   ; offset
        dd 3            ; alignment as power of 2 (8)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000000   ; no flags
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___TEXTend:
```

So, this is the `__TEXT` segment, which covers all the executable code and a good bit of other data. It contains six sections. Each section is aligned according to its section information, and all the sections are shoved together at the end of the segment, such that the first quite-a-few bytes of `__TEXT` are zeroed. However, because of how the linker maps segments, `__TEXT` actually includes all the Mach-O headers. As we'll see later, the symbol table even has its own entry for `__mh_execute_header`. Here are the sections:

1. `__text` - The actual _code_ code of the executable, where all the functions are. In this case, just one function - `main()`. It's marked as `S_REGULAR`, which means "it's a plain old section", and flagged as containing both "some instructions" (at least some executable code) and "pure instructions" (_only_ executable code).
2. `__stubs` - The jump table which redirects into the lazy and non-lazy symbol sections. See my previous article for an explanation of the contents of this section. It's marked as `S_SYMBOL_STUBS`, the meaning of which is fairly obvious.
3. `__stub_helper` - The helper function for lazy dynamically bound symbols.
4. `__cstring` - A section containing the read-only C string literals used within the code.
5. `__unwind_info` - The compact unwind information for the executable's code. Generated for exception handling on OS X.
6. `__eh_frame` - The DWARF2 unwind information for the executable's code. Generated for exception handling and debugging.

Next comes the `__DATA` segment:

```
    ___DATAstart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___DATAend - ___DATAstart    ; command size
        db '__DATA',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100001000  ; VM address
        dq 0x1000       ; VM size
        dq 0x1000       ; file offset
        dq 0x1000       ; file size
        dd 0x7          ; VM_PROT_READ | VM_PROT_WRITE | VM_PROT_EXECUTE
        dd 0x3          ; VM_PROT_READ | VM_PROT_WRITE
        dd 2            ; number of sections
        dd 0x0          ; flags
    ___DATAnlsymptrstart:
        db '__nl_symbol_ptr',0  ; section name (pad to 16 bytes)
        db '__DATA',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100001000 + ___nlsymptrstart - ___DATAload ; address
        dq ___nlsymptrend - ___nlsymptrstart    ; size
        dd ___nlsymptrstart ; offset
        dd 3            ; alignment as power of 2 (8)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000006   ; S_NON_LAZY_SYMBOL_POINTERS
        dd 2            ; reserved1 (index into indirect symbol table)
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___DATAlasymptrstart:
        db '__la_symbol_ptr',0  ; section name (pad to 16 bytes)
        db '__DATA',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100001000 + ___lasymptrstart - ___DATAload ; address
        dq ___lasymptrend - ___lasymptrstart    ; size
        dd ___lasymptrstart ; offset
        dd 3            ; alignment as power of 2 (8)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000007   ; S_LAZY_SYMBOL_POINTERS
        dd 4            ; reserved1 (index into indirect symbol table)
        dd 0            ; reserved2
        dd 0            ; reserved3
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___DATAend:
```

There's only two sections here, since this program doesn't have any global or static data: the non-lazy and lazy symbol stubs.

And then the last segment, `__LINKEDIT`:

```
    ___LINKEDITstart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___LINKEDITend - ___LINKEDITstart    ; command size
        db '__LINKEDIT',0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100002000  ; VM address
        dq 0x1000       ; VM size
        dq 0x2000       ; file offset
        dq ___LINKEDITdataend - ___LINKEDITdatastart    ; file size
        dd 0x7          ; VM_PROT_READ | VM_PROT_WRITE | VM_PROT_EXECUTE
        dd 0x1          ; VM_PROT_READ
        dd 0            ; number of sections
        dd 0x0          ; flags
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___LINKEDITend:
```

The `__LINKEDIT` segment contains a variety of data used by `dyld`, such as the symbol table, the indirect symbol table, the rebase opcodes, the binding opcodes, the exports table, the function starts information, the data-in-code table, and some codesigning data.

**Lots and Lots of Linker Data**  
The next several load commands deal with static and dynamic linking information:

```
    ___dyldinfostart:
        dd 0x80000022   ; LC_DYLD_INFO | LC_REQ_DYLD
        dd ___dyldinfoend - ___dyldinfostart    ; command size
        dd ___rebasestart   ; rebase info offset
        dd ___rebaseend - ___rebasestart    ; rebase info size
        dd ___bindstart ; binding info offset
        dd ___bindend - ___bindstart    ; binding info size
        dd 0            ; weak binding info offset
        dd 0            ; weak binding info size
        dd ___lazystart ; lazy binding info offset
        dd ___lazyend - ___lazystart    ; lazy binding info size
        dd ___exportstart   ; export info offset
        dd ___exportend - ___exportstart    ; export info size
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___dyldinfoend:
    ___symtabinfostart:
        dd 0x2          ; LC_SYMTAB
        dd ___symtabinfoend - ___symtabinfostart    ; command size
        dd ___symtabstart   ; symbol table offset
        dd (___symtabend - ___symtabstart) >> 4 ; number of symbols
        dd ___strtabstart   ; string table offset
        dd ___strtabend - ___strtabstart    ; string table size
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___symtabinfoend:
    ___dysymtabinfostart:
        dd 0xb          ; LC_DYSYMTAB
        dd ___dysymtabinfoend - ___dysymtabinfostart    ; command size
        dd 0            ; local symbols index
        dd 8            ; number of local symbols
        dd 8            ; external symbols index
        dd 2            ; number of external symbols
        dd 10           ; undefined symbols index
        dd 3            ; number of undefined symbols
        dd 0            ; table of contents offset
        dd 0            ; table of contents entries
        dd 0            ; module table offset
        dd 0            ; module table entries
        dd 0            ; external references table offset
        dd 0            ; external references table entries
        dd ___indirsymstart ; indirect symbol table offset
        dd (___indirsymend - ___indirsymstart) >> 2 ; indirect symbol table entries
        dd 0            ; local relocation table offset
        dd 0            ; local relocation table entries
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___dysymtabinfoend:
    ___loaddylinkerstart:
        dd 0xe          ; LC_LOAD_DYLINKER
        dd ___loaddylinkerend - ___loaddylinkerstart    ; command size
        dd ___loaddylinkername - ___loaddylinkerstart   ; offset to name
    ___loaddylinkername:
        db '/usr/lib/dyld',0    ; name
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___loaddylinkerend:
    ___maincmdstart:
        dd 0x80000028   ; LC_MAIN | LC_REQ_DYLD
        dd ___maincmdend - ___maincmdstart  ; command size
        dq _main        ; offset of main from start of __TEXT
        dq 0            ; stack size
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___maincmdend:
    ___loadlibsystemstart:
        dd 0xc          ; LC_LOAD_DYLIB
        dd ___loadlibsystemend - ___loadlibsystemstart  ; command size
        dd ___loadlibsystemname - ___loadlibsystemstart ; offset to path
        dd 2            ; UNIX time stamp Wed Dec 31 19:00:02 1960
        dd 0x00a90300   ; current version (0.169.3.0)
        dd 0x00010000   ; compatibility version (0.1.0.0)
    ___loadlibsystemname:
        db '/usr/lib/libSystem.B.dylib' ; path
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___loadlibsystemend:
    ___fstartscmdstart:
        dd 0x26         ; LC_FUNCTION_STARTS
        dd ___fstartscmdend - ___fstartscmdstart    ; command size
        dd ___functionstartsstart   ; offset to function starts data (fun label name, isn't it?)
        dd ___functionstartsend - ___functionstartsstart    ; size of function starts data (even more fun name!)
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___fstartscmdend:
    ___datacodecmdstart:
        dd 0x29         ; LC_DATA_IN_CODE
        dd ___datacodecmdend - ___datacodecmdstart  ; command size
        dd ___datacodestart ; offset to data-in-code information
        dd ___datacodeend - ___datacodestart ; size of data-in-code information
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___datacodecmdend:
    ___dycodesigncmdstart:
        dd 0x2b         ; LC_DYLIB_CODE_SIGN_DRS
        dd ___dycodesigncmdend - ___dycodesigncmdstart  ; command size
        dd ___dylibcodesignaturesstart  ; offset to code signatures from dylibs
        dd ___dylibcodesignaturesend - ___dylibcodesignaturesstart  ; you get the idea, right?
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___dycodesigncmdend:
```

To summarize, this long blather of data consists of:

1. A list of dynamic linking info for the binary. This command, along with some others, is marked with `LC_REQ_DYLD`, meaning that if the version of `dyld` loading the binary doesn't understand the command, it must give up right then rather than continue without the information.
2. The location of the symbol and strings tables. These are given as offsets from the beginning of the file, but it is understood that the data is contained within the `__LINKEDIT` segment. At runtime, `dyld` will perform the calculation `symtable_base_address = linkedit_base_address + (symtab_offset - linkedit_offset)` to get the actual location in memory of the symbol table. This is repeated similarly for the strings table, as well as the offsets given in the `LC_DYLD_INFO` and `LC_DYSYMTAB` commands.
3. A set of dynamic symbol data for the binary, giving the offsets and counts within the symbol table for various types of symbols.
4. The `LC_LOAD_DYLINKER` command which gives the hardcoded path for the dynamic linker to load the executable with. This is used by the kernel rather than the dynamic linker, which will run the specified program when the process is spawned. Don't get the idea that you can use this to subvert the loading process, however; the kernel won't let you pick just any dynamic linker.
5. `LC_MAIN`, a replacement for the older `LC_UNIXTHREAD` command. It used to be that executables were initialized with a thread state specified within the binary itself, but recently, someone realized this was a waste of time and space with `dyld` running early and the state being exactly the same in practically every executable. Instead, `LC_MAIN` gives the address of the entry point (`main()`) and `dyld` jumps right to that instead, also replacing the old `crt1.o` object which contained glue code to set up `main()`.
6. `LC_LOAD_DYLIB` is the "I link to this dynamic library for some of my undefined symbols" command. This binary only links to `libSystem.B.dylib`, the OS X equivalent of `libc`.
7. `LC_FUNCTION_STARTS` is a table of data in the `__LINKEDIT` segment which gives the address of every function entry point in the executable. Among other things, this allows for functions to exist that have no entries in the symbol table.
8. `LC_DATA_IN_CODE` is similarly a table giving the locations of data bytes which are embedded within executable code. This is useful for any number of purposes, not the least of which is accurate disassembly.
9. `LC_DYLIB_CODE_SIGN_DRS`, finally, gives a list of designated requirements for each dynamic library linked with the executable. This allows the code signing machinery to determine the suitability of the executable without having to load every dynamic library it links to.

**A Few More!**  
Just when you thought we were done, there're three more load commands we haven't covered yet:

```
    ___uuidstart:
        dd 0x1b         ; LC_UUID
        dd ___uuidend - ___uuidstart    ; command size
        db 0xd3,0xec,0x58,0x28,0x02,0x26,0x36,0x29,0xab,0xc3,0x7d,0x6d,0xc9,0xf9,0x2d,0xda  ; D3EC5828-0226-3629-ABC3-7D6DC9F92DDA
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___uuidend:
    ___osverstart:
        dd 0x24         ; LC_VERSION_MIN_MACOSX
        dd ___osverend - ___osverstart  ; command size
        dd 0x000a0800   ; OS min version: 10.8
        dd 0x000a0800   ; Build SDK version: 10.8
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___osverend:
    ___sourceverstart:
        dd 0x2a         ; LC_SOURCE_VERSION
        dd ___sourceverend - ___sourceverstart  ; command size
        dq 0            ; Source version: 0.0.0.0.0
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___sourceverend:
    ___loadcmdsend:
```

These are the binary's UUID, the version of OS X it's meant for, the version of the SDK it was linked against, and the "source version". I can't find any clue what the "source version" actually is, and it's just a bunch of zeroes in the binaries I've looked at, so your guess is as good as mine.

**Finally, Something Else!**  
The first thing we do now is pad out the file to the start of `main()`:

```
    ___TEXTload:
        times (0xf14-($-$$)) db 0   ; pad the __TEXT segment
```

You might ask why I didn't write `_main-($-$$)` there, and hardcoded the start address. It certainly looks fragile. Well, it is. The problem is that `nasm` doesn't provide a simple means to align data to the "end" of a segment, especially since we're not using its built-in sectioning support. It doesn't know where `_main` is until the padding has been added! In this case, I just hardcode the offset where `main()` starts (which is the exact value of the `__TEXT,__text` section's `addr` field) and let it stand as a hack, rather than trying to figure out an elegant-but-complicated solution.

Now we take the data in order; we don't even really have to do it in any particular order, since the labels we used in the load commands will relocate everything according to where we place it in the file, but there's no reason not to. The first thing is `__TEXT,__text`, the executable code. Notice that we have to rewrite the original assembly code to `nasm`'s syntax - `nasm` uses the Intel syntax, rather than the GNU syntax. The major difference is that all the operands are backwards, and there's no qualifier on the register names. All the various directives are also stripped out, since we're doing their jobs by hand.

```
    ___codestart:
    _main:
        push    rbp
        mov     rbp, rsp
        xor     edi, edi
        call    _time
        lea     rdi, [rel L_str]
        mov     rsi, rax
        xor     al, al
        call    _printf
        xor     eax, eax
        pop     rbp
        ret
    ___codeend:
```

We also don't have any size suffixes on the instructions, since `nasm` can infer them from the operands. The `rel` qualifier for the string load just tells `nasm` to generate a `rip`-relative access instead of an absolute position, which is necessary since we marked the executable as position-independent.

Next we have the symbol stubs for `time()` and `printf()`, and the stub helper:

```
    ___stubstart:
    _printf:
        jmp     [rel _lazy_printf]
    _time:
        jmp     [rel _lazy_time]
    ___stubend:

    ___stubhelpstart:
    _stub_helper:
        lea     r11, [rel _nonlazy_dyld_stub_binder]
        push    r11
        jmp     [rel _nonlazy_dyld_stub_binder]
        nop
        push    strict qword (_lazy_printf - ___lasymptrstart)
        jmp     _stub_helper
        push    strict qword (_lazy_time - ___lasymptrstart)
        jmp     _stub_helper
    ___stubhelpend:
```

The stubs themselves jump to the lazy symbol bindings in the `__DATA` segment. These initially jump right back into the bottom of `_stub_helper`, which loads the offset into the lazy symbol section of the symbol and calls into `dyld` itself through a nonlazy symbol (which will be bound by `dyld` when the executable is loaded). `dyld` will bind the symbol and rewrite the lazy symbol section so that future calls to that stub go directly to the function. Notice, these are all direct, non-conditional jumps, not subroutine calls. Also notice the use of the `strict qword` directives to force `nasm` to emit the full 64-bit values for the stack pushes.

Next comes the C strings section, very short and simple since we only have one string:

```
    ___strsstart:
    L_str:
        db      "Hello, world #%ld!\n",0
    ___strsend:
```

And now the unwinding table. This is encoded with the "compact unwind encoding" defined by Apple (as far as I know).

```
    ___uwstart:
        dd 1            ; unwind info version
        dd _commonEncodings - ___uwstart    ; common encodings array offset
        dd 0            ; count of common encodings
        dd _personalities - ___uwstart  ; personality array offset
        dd 0            ; count of personalities
        dd _index - ___uwstart  ; first-level index offset
        dd 2            ; count of entries in first-level index
    _commonEncodings:
    _personalities:
    _index:
    __entry1_0:
        dd _main        ; function offset
        dd __entry2_0 - ___uwstart  ; offset to second-level entry
        dd _lsda - ___uwstart   ; offset to language-specific data array entry
    __entry1_1:
        dd ___codeend+1 ; function offset (end of table)
        dd 0            ; offset to second-level entry - zero means end of table
        dd _lsda - ___uwstart   ; offset to LSDA
    _lsda:
    _pages:
    __entry2_0:
        dd 3            ; UNWIND_SECOND_LEVEL_COMPRESSED
        dw ___entrypage0 - __entry2_0   ; offset to entry page
        dw 1            ; number of entries in entry page
        dw ___enc0 - __entry2_0 ; offset to encoding page
        dw 1            ; number of entries in encoding page
    ___entrypage0:
    ____entrypage0_0:
        dd (0 << 24) | (0)  ; encoding index and function offset relative to first-level index offset
    ___enc0:
    ____enc0_0:
        dd 0x01000000   ; UNWIND_X86_64_MODE_RBP_FRAME | UNWIND_X86_64_REG_NONE
    ___uwend:
```

And then the DWARF-encoded version of the same information. To save everyone some time, I'm not going to write this part out with all the comments, because it's complex and it just duplicates the unwinding info above in a much more verbose fashion.

```
    ___ehstart:
        db 0x14,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x7a,0x52,0x00,0x01,0x78,0x10,0x01
        db 0x10,0x0c,0x07,0x08,0x90,0x01,0x00,0x00,0x24,0x00,0x00,0x00,0x1c,0x00,0x00,0x00
        db 0x34,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00
        db 0x00,0x41,0x0e,0x10,0x86,0x02,0x43,0x0d,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00
    ___ehend:
```

**Data, data, data... well, sort of**  
That ends off the `__TEXT` segment. Now we have the `__DATA` segment, which contains the lazy and non-lazy symbol pointers:

```
    ___DATAload:

    ___nlsymptrstart:
    _nonlazy_dyld_stub_binder:
        dq 0x0000000000000000
    _nonlazy_table_start:
        dq 0x0000000000000000
    ___nlsymptrend:

    ___lasymptrstart:
    _lazy_printf:
        dq 0x100000000 + _stub_helper_printf
    _lazy_time:
        dq 0x100000000 + _stub_helper_time
    ___lasymptrend:
```

In a real executable, `__DATA` would usually also contain static data, space for globals, and some other stuff.

**The link editor**  
`__LINKEDIT` is a real pain, because it's arbitrarily structured and the data within it isn't always all that documented. I've done my best to represent what's in it comprehensibly, but I can't guarantee I've succeeded.

We start with the rebasing opcodes, which `dyld` uses when applying ASLR:

```
    ___rebasestart:
        db 0x10 | 0x01  ; REBASE_OPCODE_SET_TYPE_IMM | REBASE_TYPE_POINTER
        db 0x20 | 0x02  ; REBASE_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2)
        db 0x10         ; uleb128_encode(_lazy_printf - ___DATAload)
        db 0x50 | 0x02  ; REBASE_OPCODE_DO_REBASE_IMM_TIMES | 2
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___rebaseend:
```

This says, "using pointers, in the __DATA segment at offset 0x10, rebase 2 pointers based on the load address of that segment".

Next come the binding opcodes and lazy binding opcodes:

```
    ___bindstart:
        db 0x11         ; BIND_OPCODE_SET_DYLIB_ORDINAL_IMM | 1
        db 0x40         ; BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM | 0
        db 'dyld_stub_binder',0 ; immediate operand
        db 0x51         ; BIND_OPCODE_SET_TYPE_IMM | BIND_TYPE_POINTER
        db 0x72         ; BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2)
        db 0x00         ; uleb128_encode(0)
        db 0x90         ; BIND_OPCODE_DO_BIND
        db 0x00         ; BIND_OPCODE_DONE
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___bindend:
    ___lazystart:
        db 0x72,0x10    ; BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2), uleb128_encode(0x10)
        db 0x11         ; BIND_OPCODE_SET_DYLIB_ORDINAL_IMM | 1
        db 0x40,'_printf',0 ; BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM | 0, '_printf'
        db 0x90,0x00    ; BIND_OPCODE_DO_BIND, BIND_OPCODE_DONE
        db 0x72,0x18    ; BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2), uleb128_encode(0x18)
        db 0x11         ; BIND_OPCODE_SET_DYLIB_ORDINAL_IMM | 1
        db 0x40,'_time',0   ; BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM | 0, '_time'
        db 0x90,0x00    ; BIND_OPCODE_DO_BIND, BIND_OPCODE_DONE
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___lazyend:
```

These opcodes bind a non-lazy symbol named `dyld_stub_binder` to offset 0 in the `__DATA` segment as a pointer. For lazy symbols, they bind a symbol named `_printf` to offset `0x10` in the `__DATA` segment and `_time` to offset `0x18`.

And here's the export trie:

```
    ___exportstart:
    _exnode0:
        db 0x00         ; terminal size
        db 0x01         ; child count
        db '_',0        ; name
        db _exnode1 - ___exportstart    ; child node offset
    _exnode1:
        db 0x00         ; terminal size
        db 0x02         ; child count
        db '_mh_execute_header',0   ; name
        db _exnode3 - ___exportstart    ; child node offset
    _exnode2:
        db 'main',0     ; name
        db _exnode4 - ___exportstart    ; child node offset
    _exnode3:
        db 0x02         ; terminal size
        db 0x00         ; flags
        db 0x00         ; address - uleb128_encode(0)
        db 0x00         ; child count
    _exnode4:
        db 0x03         ; terminal size
        db 0x00         ; flags
        db 0x94,0x1e    ; address - uleb128_encode(0xf14)
        db 0x00         ; child count
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___exportend:
```

This forms a trie, or prefix tree, for the two symbols exported by the executable, `__mh_execute_header` and `_main`.

Have the compressed function starts table, represented as a set of deltas to be added to the base code address:

```
    ___functionstartsstart:
        db 0x94         ; delta = 0x14, address  = ___codestart
        db 0x1e         ; delta = 0x1e, end 
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___functionstartsend:
```

Here's the data-in-code table. Whoops, there isn't any in this executable, the load command's just added anyway:

```
    ___datacodestart:
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___datacodeend:
```

How about some designated requirements for dylibs? I have no real idea what format this is in, I just interpreted it as best I could:

```
    ___dylibcodesignaturesstart:
        dd 1            ; count of code signatures (maybe?)
        dd 0            ; unknown
        dd 0x14         ; unknown
        db 0xfa,0xde,0x0c,0x00,0x00,0x00,0x00,0x28
        db 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x06
        db 0x00,0x00,0x00,0x02,0x00,0x00,0x00,0x0b
        db 0x6c,0x69,0x62,0x53,0x79,0x73,0x74,0x65
        db 0x6d,0x2e,0x42,0x00,0x00,0x00,0x00,0x03  ; code signature for libSystem.B.dylib
        dd 0            ; unknown
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___dylibcodesignaturesend:
```

**A symbol table**  
The symbol table is where most the interesting stuff that's left happens:

```
    ___symtabstart:
        dd L_srcdir - ___strtabstart    ; string table offset
        db 0x64         ; N_SO
        db 0x00         ; section 0
        dw 0x00         ; no desc
        dq 0            ; address 0
        dd L_srcfile - ___strtabstart   ; string table offset
        db 0x64         ; N_SO
        db 0x00         ; section 0
        dw 0x00         ; no desc
        dq 0            ; address 0
        dd L_objfile - ___strtabstart   ; string table offset
        db 0x66         ; N_OSO
        db 0x03         ; section 3
        dw 0x01         ; desc(?)
        dq 0x50b8c91f   ; st_mtime
        dd L_empty - ___strtabstart ; no string
        db 0x2e         ; N_BNSYM
        db 0x01         ; section 1
        dw 0x00         ; desc
        dq 0x100000000 + _main      ; start address
        dd L_main1 - ___strtabstart ; string table offset
        db 0x24         ; N_FUN
        db 0x01         ; section 1
        dw 0x00         ; desc
        dq 0x100000f14  ; start address
        dd L_empty - ___strtabstart ; no string
        db 0x24         ; N_FUN
        db 0x00         ; section 0
        dw 0x00         ; desc
        dq 0x20         ; address
        dd L_empty - ___strtabstart ; no string
        db 0x4e         ; N_ENSYM
        db 0x01         ; section 1
        dw 0x00         ; desc
        dw 0x20         ; address
    _sym_mh_execute_header:
        dd L_mhexechead - ___strtabstart    ; string table offset
        db 0x0f         ; N_SECT | N_EXT
        db 0x01         ; section 1
        dw 0x0010       ; REFERENCED_DYNAMICALLY
        dq 0x100000000 + __mh_execute_header    ; start address
    _sym_main:
        dd L_main2 - ___strtabstart ; string table offset
        db 0x0f         ; N_SECT | N_EXT
        dw 0x0000       ; no extra flags
        dq 0x100000000 + _main  ; start address
    _sym_printf:
        dd L_printf - ___strtabstart    ; string table offset
        db 0x01         ; N_UNDF | N_EXT
        dw 0x0100       ; dynamic library 1
        dq 0            ; address
    _sym_time:
        dd L_time - ___strtabstart  ; string table offset
        db 0x01         ; N_UNDF | N_EXT
        dw 0x0100       ; dynamic library 1
        dq 0            ; address
    _sym_dyld_stub_binder:
        dd L_binder - ___strtabstart    ; string table offset
        db 0x01         ; N_UNDF | N_EXT
        dw 0x0100       ; dynamic library 1
        dq 0            ; address
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___symtabend:

    ___indirsymstart:
        dd (_sym_printf - ___symtabstart) >> 4  ; index into symbol table
        dd (_sym_time - ___symtabstart) >> 4    ; index into symbol table
        dd (_sym_dyld_stub_binder - ___symtabstart) >> 4    ; index into symbol table
        dd 0x40000000   ; INDIRECT_SYMBOL_ABS
        dd (_sym_printf - ___symtabstart) >> 4  ; index into symbol table
        dd (_sym_time - ___symtabstart) >> 4    ; index into symbol table
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___indirsymend:

    ___strtabstart:
    L_spc:
        db ' '
    L_empty:
        db 0
    L_srcdir:
        db '/Users/gwynne/',0
    L_srcfile:
        db 'test.c',0
    L_objfile:
        db '/var/folders/b8/qgjb841d71d55cf8jh1myb540000gn/T/test-KyuIba.o',0
    L_main1:
        db '_main',0
    L_mhexechead:
        db '__mh_execute_header',0
    L_main2:
        db '_main',0
    L_printf:
        db '_printf',0
    L_time:
        db '_time',0
    L_binder:
        db 'dyld_stub_binder',0
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___strtabend:

    ___LINKEDITdataend:
```

Here you have the symbol table (including STABS entries), the indirect symbol table (which is nothing but a set of indexes into the symbol table which tell `dyld` how to use the symbol stubs in the event that the binding opcodes aren't good enough - basically, legacy data), and the string table, which holds all the user-readable strings for the symbol table.

**Conclusion**  
That is one long mess of mostly raw hexadecimal bytes. And here's the punch line: As written here, it **still** doesn't produce a working Mach-O binary!

Why not? Because I didn't account for alignment requirements properly, and I ran out of time to fix the problem before the article had to go up. All the tables and structures here are correct, though, so hopefully, it's still instructional as to just how much goes into even the simplest binary, and how much work you should be very glad `ld` and `dyld` are doing for you!

Thanks for reading, as always. I hope you enjoyed it!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
