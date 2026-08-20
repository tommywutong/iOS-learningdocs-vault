---
title: Compiler Tools Release Notes
apple_id: TP40001264
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-CompilerTools/index.html
archived_at: '2026-07-18T02:50:26.455373Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# OS X Xcode 2.4 Release Notes: Compiler Tools

> [!IMPORTANT]
> 

#### Contents:

- [Overview](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzr)
- [Notes Specific to OS X Xcode 2.4 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzs)
- [Notes Specific to OS X Xcode 2.3.1 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzt)
- [Notes Specific to OS X Xcode 2.3 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzu)
- [Notes Specific to OS X Xcode 2.2.1 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzv)
- [Notes Specific to OS X Xcode 2.2 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzw)
- [Notes Specific to OS X Xcode 2.1 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzy)
- [Notes Specific to OS X Xcode 2.0 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzrga)
- [Notes Specific to OS X Xcode 1.5 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzrgi)
- [Notes Specific to OS X v10.3.4 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzsgm)
- [Notes Specific to OS X December 2003 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzsg4)
- [Notes Specific to OS X v10.3 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzsha)
- [Notes Specific to OS X June 2003 Developer Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixztge)
- [Notes Specific to OS X November 2002 Developer Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixztha)
- [Notes Specific to OS X v10.2 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzugm)
- [Notes Specific to OS X v10.1 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzug4)
- [Notes Specific to OS X v10.0 Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzuhe)
- [Notes Specific to OS X Public Beta Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzvga)
- [Notes Specific to OS X Developer Release 4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzvgi)
- [Notes Specific to OS X Developer Release 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzvgm)
- [Notes Specific to OS X Developer Preview Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzvgu)
- [Notes Specific to OS X Server Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzvg4)
- [There are no Notes Specific to Rhapsody Developer Release 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzvhe)
- [Notes Specific to Rhapsody Developer Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrufvcg63tujruw422fnrsw2zlooreuixzwga)

### Overview

These notes are for the OS X Xcode 2.4 Release of the compiler tools. They contain information about the following topics:

- The OS X Mach-O GNU-based assemblers
- The OS X 32-bit Mach-O static link editor
- Mach-O object file tools (_nm_, _otool_, and so on)

### Notes Specific to OS X Xcode 2.4 Release

The tools now support development of 64-bit Mach-O binaries for Intel with the -arch x86_64 flag.

The design of the relocation entries for the x86_64 architecture does not make it possible to strip local symbols from relocable object files. As such the feature of running strip(1) with the -x option to limit the symbols to just the exported symbols is not available on the x86_64 architeture. And the strip(1) -x option for an x86_64 object file does nothing.

### Notes Specific to OS X Xcode 2.3.1 Release

The one feature of this release is support for the Intel Vanderpool instructions in the assembler and disassembler.

### Notes Specific to OS X Xcode 2.3 Release

The major new feature for this release is the support of the use of DWARF for debug information.

The other new feature for this release is the support of the .quad assembler directive for the 32-bit assemblers. With this feature the assembler now treates all expressions as 64-bit values. This change can cause code code to no longer assemble. For example the following construct:

```
addi r11, r11, (-33120 &lt;&lt; 16) >> 16
```

will now generate an error of the form:

x.s:1:Parameter error: expression out of range (parameter 3)

The correct way this should be coded is:

```
addi r11, r11, lo16(-33120)
```


### Notes Specific to OS X Xcode 2.2.1 Release

There are no new features and only bug fixes. But there are some changes to improve the performance of the static link editor.

### Notes Specific to OS X Xcode 2.2 Release

### New Features

The static link editor now supports the new option -Sp to strip, edit and add debugging symbols so the debugger can used most of the debugging symbols from the object files.

The ar(1) tool has the new -S option to suppress building the table of contents.

### Notes Specific to OS X Xcode 2.1 Release

### New Features

The tools now have support for the handful of x86 sse3 instructions.

### Notes Specific to OS X Xcode 2.0 Release

### New Features

The tools now support development of 64-bit Mach-O binaries for the PowerPC with the -arch ppc64 flag. The one tool that has not been seamlessly ported for this release is otool(1). And there is an otool64(1) for 64-bit Mach-O binaries.

### Notes Specific to OS X Xcode 1.5 Release

### New Features

### The static linker has an option to do dead code stripping

The static link editor now can do dead code stripping. The new _ld_(1) option to do this is _-dead_strip_. There is also an additional option _-no_dead_strip_inits_and_terms_ that can be used when _-dead_strip_ is specified to cause all constructors and destructors to never be dead code stripped. The load map printed with the _ld_(1) option _-M_ notes what was dead stripped from the input files.

There is one known bug with the tools that do dead code stripping. It is possible for some debugging information for types made to be stripped. This can lead to the debugger not being able to print the values of some variables and get unknow type errors.

For testing, the environment variable LD_DEAD_STRIP can be set. which causes _-dead_strip_ to specified for all _ld_(1) commands that don't specify the _-r_ option. The environment variable LD_NO_DEAD_STRIP_INITS_AND_TERMS likewise causes _-no_dead_strip_inits_and_terms_ to specified for all _ld_(1) commands that don't specify the _-r_ option. And the environment variable LD_DEAD_STRIP_DYLIB causes _-dead_strip_ to specified for all _ld_(1) commands that have the _-dylib_ option specified.

The static link editor determines what unreachable code and data can be stripped based on the references from the initial live symbols and blocks. The initial live symbols include the symbols to be exported in the linked output. The set of exported symbols are specified with the _-exported_symbols_list_ option or a list of symbols not to be exported is specified with the _-unexported_symbols_list_ option. If no exported symbols are specified and the output is not an executable (shared library, bundle, etc) it is assumed all global symbols are to be exported. If the output is a shared library and a shared library initialization symbol is specified with _-init_ _symbol_name_ option then that _symbol_name_ is an initial live symbol. If the output is an executable then the block that contains the entry point or the symbol specified with the _-e_ _symbol_name_ is an initial live symbol. Other symbols can be marked by the programmer as an initial live symbols with the GNU compiler's __attribute__((used)). For Objective-C code, the compiler will also mark the blocks of Objective-C runtime data it produces so they are part of the initial live blocks. For symbols marked referenced dynamically (via the REFERENCED_DYNAMICALLY bit in <mach-o/nlist.h>), such as the symbol __environ_ from /usr/lib/crt1.o, they are also part of the initial live symbols.

Before turning on the _-dead_strip_ option your project will first have to be "ported" to work with dead code stripping. This will include changing from -gused (the default for -g) to -gfull and re-compiling all of the objects files being linked into your program with the new compiler from the OS X June 2004 release. Also if your building an executable that loads plugins, which uses symbols from the executable, you will have to make sure the symbols the plugins use are not stripped (by using __attribute__((used)) or the _-exported_symbols_list_ option). If you are using an export list and building a shared library, or an executable that will be used with ld(1)'s -bundle_loader flag, you need to include the symbols for exception frame information in the export list for your exported C++ symbols. These symbols end with .eh and can be seen with the nm(1) tool.

Various auto configure test programs that expect to get undefined symbol errors when they have a possible undefined symbol referenced from dead code can't use the _-dead_strip_ option. Because the dead code and the unused undefined reference will be stripped allowing the program to successfully linked. We have geneally found that auto configure programs on UNIX based system can't be configured with the _-dead_strip_ option on.

Recompiling with a new compiler is required to get effective dead code stripping. As it marks the object files it creates as OK to divide up the section contents into individual blocks by the symbols that are in the object files. Objects not marked are assumed to be generated from assembly code, older compilers, or from compilers that are not know to be safe to divide up their section contents by their symbols. For non-marked objects if any symbol is used from a section the entire section is kept and not dead stripped.

### Work around for objects incorrectly marked object files as OK to divide up

The new compiler unconditionally marks the object files it creates as OK to divide up. There may be cases, especially with _asm()_ statements, that it should not mark the object it creates as OK to divide up. In these cases turning on the _-dead_strip_ option may fail to produce a working program because it can incorrectly strip a live block. The reason for this is that the heuristic of dividing up the section contents by their symbols is incorrect if any individual block has more than one symbol. This makes the heuristic fragile.

The reason that the current dead code stripping inplementation is fragile is because the static linker is guessing at the structure of the program. Namely it is guess at which bytes of a section make up a individual block of code or data. It makes its guess based on the symbols that are in the object files being linked. In the same way it guesses for the blocks it uses for the _-sectorder_ option. With the difference being that all sections are broken up into individual blocks with the goal to eliminate the unreachable (dead) blocks in the linked output. The reason this is fragile is that all the symbols in an object file may not be the start of an individual block.

As a workaround to the problem of incorrectly strip a live block you can produce a -sectorder file for objects that have section contents that must be linked whole. You would create a line in the sectorder file specifying the object and the psuedo symbol .section_all. For example if .text section of crt1.o and the archive member of darwin-tramp.o in libgcc.a must be linked whole, you would add the following:

```
/usr/lib/crt1.o:.section_all
/usr/lib/libgcc.a:darwin-tramp.o:section_all
```

to your _order_file_ for the __TEXT __text section. Then use the ld(1) option _-sectorder_ __TEXT __text _order_file_ when linking.

### Current design limitations

There is a limitation in the current design for individual blocks that have no symbols visible in the object file. Symbols that are temporary labels that start with a 'L', or symbols that have been stripped. An individual block that starts with these symbols will appear to be part of the previous block that has a symbol in the object file. This can result in a linked image that does not have all of its dead code stripped. When what would have been a dead individual block becomes part of the previous block which is live. Causing the dead individual block and all of its references to be live.

By default when there are multiply defined symbols in the linked objects this is treated as an error. Even when the _-dead_strip_ option is specified. Unused multiply defined symbols can be stripped if the strongly discouraged _-m_ option is also specified. The duplicate symbols other than the first symbol may still end up being used in the resulting output file through local references however.

Symbols from the linked objects in the output file that are only referenced via a shared library will not be dead stripped. Currently the static linker marks them with the REFERENCED_DYNAMICALLY bit in <mach-o/nlist.h> which causes them to be live.

There is no support in the current design to dead strip branch islands created with the compiler option _-mlongcall_.

### Assembly level and object file support for dead code stripping

### Marking of objects that can have their section contents divided up

The marking of object files which are OK to divide their section contents into individual blocks is done with the new assembler directive _.subsections_via_symbols_. This directive sets a previously unused bit in the object file's mach_header structure in the flags field. This bit is defined as the following new constant in the header file <mach-o/loader.h>:

```
#define MH_SUBSECTIONS_VIA_SYMBOLS 0x2000 /* safe to divide up the sections into sub-sections via symbols for dead code stripping */
```

This can be see with _otool_(1)'s _-hv_ options and shows up as _SUBSECTIONS_VIA_SYMBOLS_ in the following output:

```
% otool.NEW -hv a.out a.out: Mach header magic cputype cpusubtype filetype ncmds sizeofcmds flags MH_MAGIC PPC ALL OBJECT 3 228 SUBSECTIONS_VIA_SYMBOLS
```

The new assembler directive _.subsections_via_symbols_ can be added to hand written assembly files provided the symbols are at the start of individual blocks. Since this applies to the entire file, when multiple object files are combined by the static link ediror, ld(1), to produce a relocable object, using the -r flag, if any of the objects do not have this flag set the output file will not have this flag set.

For example this assembly code contains only two individual blocks but four symbols:

```
.text .globl _plus_three _plus_three: addi r3, r3, 1 .globl _plus_two _plus_two: addi r3, r3, 1 .globl _plus_one _plus_one: addi r3, r3, 1 blr  .globl _some_other_routine _some_other_routine: blr
```

And if the new assembler directive _.subsections_via_symbols_ were added to the above code the static link editor would make 4 blocks about of the above code. Then if the program uses _add_three but not _add_two or _add_one it will get the wrong answer if the _-dead_strip_ option is used. As the blocks for _add_two or _add_one will be dead stripped. And if _some_other_routine is not live then when _add_three is called it will fall through to what ever bit of code follows it and likely crash.

### The .no_dead_strip assembler directive

The new assembler directive _.no_dead_strip_ _symbol_name_ can be used to specify that a symbol is not to be dead stripped. For example:

```
.no_dead_strip _my_version_string .cstring _my_version_string: .ascii "cctools-501"
```

This can be seen (in object files only) with _nm_(1)'s _-m_ option and shows up as _[no dead strip]_ in the following output:

```
% nm -m x.o 00000000 (__TEXT,__cstring) non-external [no dead strip] _my_version_string
```

The _.no_dead_strip_ directive is generated by the new compiler when the __attribute__((used)) is specified on a symbol.

In object files, this bit is N_NO_DEAD_STRIP as defined in <mach-o/nlist.h>. And is set in relocatable .o files (MH_OBJECT filetype) only in the n_desc field of an nlist struct.

### The section attribute no_dead_strip

The new section attribute _no_dead_strip_ can be specified on a section to cause its entire contents to not to be dead stripped. The new compiler uses this for all Objective-C sections it creates. For example:

```
.section __OBJC, __image_info, regular, no_dead_strip
```

In object files, this bit is S_ATTR_NO_DEAD_STRIP as defined in <mach-o/loader.h>. And is set in the flags field of a section struct.

### The section attribute live_support

The new section attribute _live_support_ can be specified on a section to cause its blocks to not be dead stripped if they reference something that is live. The new compiler uses this for C++ exception frame information. For example:

```
.section __TEXT, __eh_frame, coalesced, no_toc+strip_static_syms+live_support
```

In object files, this bit is S_ATTR_LIVE_SUPPORT as defined in <mach-o/loader.h>. And is set in the flags field of a section struct.

### The assembler has a new .machine directive

The assembler now takes a new _.machine_ directive as an alternate to using the command line _-arch_ _arch_name_ option. It is specified as for example as:

```
.machine ppc970
```

Where _ppc970_ can be any _arch_name_ that would appear in the _-arch_ _arch_name_ option as listed on the _arch_(3) man page for the assembler's architecture family.

### Notes Specific to OS X v10.3.4 Release

### New Features

### Improved launch times of applications

The dynamic linker has been changed that improve launch times of applications.

### The redo_prebinding command supports unprebinding

The _redo_prebinding_(1) command has a new option, _-u_, that does a unprebind operation. The unprebind operation produces a canonical form of a Mach-O file that can be used for binary diffing and patching. Bundles and non-prebound executables and dylibs can also be canonicalized with the unprebind operation.

### Notes Specific to OS X December 2003 Release

There are no notes specific to the OS X December 2003 release of the compiler tools.

### Notes Specific to OS X v10.3 Release

### New Features

### The static linker has an option to find @executable_path dynamic libraries

Added the _-executable_path_ _path_name_ option to _ld_(1) where _path_name_ is is used to replace @executable_path for dependent libraries.

### Notes Specific to OS X June 2003 Developer Release

### New Features

### The compiler tools now support the PowerPC 970 processor

The compiler tools now support the PowerPC 970 processor. The architecture specific flag _-arch ppc970_ is used to specify this specific processor. The assembler will only assemble 64-bit instructions and other PowerPC AS User Instruction Set Architecture Version 2.00 instructions supported by the PowerPC 970 processor when _-arch ppc970_ or _-force_cpusubtype_ALL_ is specified.

To specify branch predictions which use the AT bit encodings for _The branch is very likely to be taken_ and _The branch is very likely not to be taken_ the two character suffixes ++ and -- are used. For example:

```
bge-- foo
```

The single character suffixes + and - continue to encode branch predictions which use the Y-bit encoding by default. The encoding can be changed for the single character suffixes to use the AT bit encodings with the assembler flag _-static_branch_prediction_AT_bits_ (see the _as_(1) man page for more details).

### The compiler tools now support stub libraries

The compiler tools now support stub libraries created from dynamic libraries which are used in the SDKs. Stub libraries are created via _strip_(1) and the new _-c_ option. And can be linked against in place of the actual dynamic library.

### The static linker now can search for libraries first in the library paths

By default when the _-dynamic flag_ is in effect, the _-l__x_ and _-weak-l__x_ options first search for a file of the form lib_x_.dylib in each directory in the library search path, then a file of the form lib_x_.a is searched for in the library search paths. The new option _-search_paths_first_ changes it so that in each path lib_x_.dylib is searched for then lib_x_.a before the next path in the library search path is searched.

### The static linker now supports forcing a dynamic library to be weak

Added the _-weak_framework_, _-weak_library_ and _-weak-l_ options to _ld_(1) to force the dynamic library and the symbols referenced from it to be marked as weak imports. See the _ld_(1) man page for more details.

### The static linker now has a work around for not having dead code stripping

Added the _-undefined define_a_way_ option to _ld_(1) as a work a round to not having dead-code stripping that also strips out references to undefined symbols from the dead code. Which leads to link time failures due to undefined symbols. With this option _ld_(1) defines the remaining undefined symbols as private definitions and allows the link to succeed. The program then runs as long as it does not use any of the undefined symbols.

### Notes Specific to OS X November 2002 Developer Release

### New Features

### Exports lists can now be specified to the static linker

The static link editor, _ld_(1), now has two new options, _-exported_symbols_list_ _filename_ and _-unexported_symbols_list_ _filename_ to limit the global symbols in the linked output file. This was previously done by with an _nmedit_(1). By using the new options to _ld_(1) the use of _nmedit_(1) can be eliminated resulting in faster build times.

### The static linker now can build single module dynamic libraries

The static link editor, _ld_(1), now has a new option, _-single_module_, to build a dynamic library containing only one module. This was previously done by first creating a master.o file with an _ld_(1) _-r_ step and then using the master.o to created the dynamic library. By using the new _-single_module_ option to _ld_(1) this first step can be eliminated resulting in faster build times.

The default in the static link editor remains the same and dynamic libraries are built with multiple modules. The new flag _-multi_module_ has also been added to allow this to be explicitly specified.

### The static linker's -s option now works like strip on dynamic executables

The static link editor's _-s_ option can now be used to strip an executable that use the dynamic link editor. This will produce the same result as running _strip_(1) with no options on the executable. By using the _-s_ option when building an executable the _strip_(1) step can be eliminated resulting in faster build times.

### Notes Specific to OS X v10.2 Release

The compiler tools for the MacOS X 10.2 Release must be used with prebound images (executables, and shared libraries) from the MacOS X 10.2 User Release. The compiler tools in MacOS 10.1 will not work with prebound images from with the MacOS X 10.2 User Release. If the 10.1 compiler tools are used on prebound images from the MacOS X 10.2 User Release the compiler tools will generate error messages indicating that the image is a malformed file.

### New Features

### The dynamic linker now supports weak references and weak dylibs

The dynamic linker now supports weak symbol references and weak dymamic libraries. When creating a binary with the static link editor if all the symbols referenced from a given dependent dynamic library are weak references then the library is marked weak. When the binary is used at execution time and a weak library is missing the dynamic linker will not cause an error. For all weak symbols that are missing execution time the dynamic linker uses zero as their address. This allows a weak symbol's address to be tested for zero at runtime allowing the code to avoid using the weak symbol when it is missing. Binaries that use weak references require a dynamic linker from OS X v10.2 or later.

To indicate a symbol is to be a weak reference the __attribute((weak_import)) is used on the prototype of the symbol. When a binary is created by the static link editor normally the all the undefined symbol references of the object files being linked should be consistent for each undefined symbol. That is all undefined symbols should either be weak or non-weak references. If they are not by default this is treated as an error and can be changed with the ld(1) _-weak_reference_mismatches_ _treatment_ flag (see the ld(1) man page for more details).

Weak referenced symbols and weak libraries are only created in the output by the static link editor, _ld_(1), when the MACOSX_DEPLOYMENT_TARGET environment variable is set to 10.2. If not a warning is generated when a weak reference would be in the output and it is not marked weak. Note the default for the MACOSX_DEPLOYMENT_TARGET environment variable 10.1 so weak referenced symbols and weak libraries are not created by default. See the _ld_(1) man page for more information on the MACOSX_DEPLOYMENT_TARGET environment variable.

### redo_prebinding can now slide dylibs

The redo_prebinding(1) command now can slide dymamic libraries to new prefered addresses (see the man page for more details).

### Notes Specific to OS X v10.1 Release

You must use the 10.1 compiler tools with images (executables, plugins and shared libraries) created with the 10.1 tools. The compiler tools in MacOS 10.0 will not work with images created with the 10.1 compiler tools. If you attempt to use the 10.0 compiler tools on images created with the 10.1 compiler tools, error messages may result indicating that the image is a malformed file.

By default the compiler tools build images using the new two-level namespace binding semantics, which has important consequences for compatibility with OS X v10.0 (see below for more information).

### New Features

The following new features have been added to the Compiler Tools for the OS X v10.1 system release.

- The compiler tools now support two-level namespaces for binding undefined references from shared libraries. In flat namespace images, all symbols are referenced globally using a single name table. In two-level namespace images, symbols are referenced by library name and symbol name. This prevents multiple-defined-symbol errors when one image exports the same symbol as another image in the same program. You must rebuild your applications and plugins to take advantage of this feature, and there are compatibility restrictions with OS X v10.0 that you should understand. For more information see the _ld_(1) man page and the _Two-Level Namespace Executables Release Notes_.
- The dynamic linker now has API's for doing two-levelnamespace lookups. They are `NSAddImage`, `NSLookupSymbolInImage` and `NSIsSymbolNameDefinedInImage`. For more information see the NSModule(3) man page. [This fixes Apple bug number 2689833.]
- Prebinding is now documented in _Prebinding Release Notes_. [This fixes Apple bug number 2611234.]

### Notes Specific to OS X v10.0 Release

There are no notes specific to the OS X v10.0 release of the compiler tools.

### Notes Specific to OS X Public Beta Release

### New Features

The following new features have been added to the Compiler Tools since the OS X Developer Release 4.

- The dynamic linker now calls shared library initialization routines in their dependent order (reference number 2441683).
- The new function __initialize_Cplusplus() now can be called from a shared library initialization routine to cause the static C++ objects in the library to be initialized. This allows shared library initialization routines to make use of statically initialized C++ objects (reference number 2441683).
- The dynamic linker now supports module termination functions for all types of images (executables, plugins that are not unloaded and shared libraries). See the decription below as part of the notes specific to OS X Developer preview of module termination functions (reference number 2469527).
- The compiler tools support the new directory layout for MacOS X Public Beta. The new location for Frameworks local to the machine is /MacOSX/Library/Framework (in DP4 and previous releases this was /Local/Library/Frameworks).

### Notes Specific to OS X Developer Release 4

There are no notes specific to the compiler tools for Developer Release 4.

### Notes Specific to OS X Developer Release 3

### New Features

The following new features have been added to the Compiler Tools since the OS X Developer Preview Release.

- Dynamic shared libraries now can have a dynamic shared library initialization routine (reference number 2367584). This routine is specified to libtool(1) with the new "-init _symbol_name_" argument. The library initialization routine is called before any symbol is used from the library including C++ static initializers (and #pragma CALL_ON_MODULE_BIND routines). So the code in a library initialization routine or code called by it can not depend on C++ static initializers. Also code in a library initialization routine or code called by it can not call any of the dynamic linker API, <mach-o/dyld.h>, otherwise that could result in more than one library initialization routine being partially executed on the stack.
- The dynamic linker now supports shared library install names that start with "@executable_path/" and substitutes the directory path of the executable for "@executable_path/"when locating the library. This requires a kernel from OS X Developer Release 2 or later. Without that kernel, this feature can only be used if argv[0] is in fact the name of the executable and it is an absolute path or relative to the current directory (contains at a '/' in the argv[0] string).
- The `NSLinkModule` API now has an option to cause it to return when there is an error loading the module and a new API `NSLinkEditError` to get the error information. To use this the constant NSLINKMODULE_OPTION_RETURN_ON_ERROR needs to be or'ed into the options parameter to `NSLinkModule`. Then if NSLinkModule returns NULL the error information can be retrieved with NSLinkEditError.

  The NSLINKMODULE_OPTION_RETURN_ON_ERROR option is an alternative method to the existing dyld error handling which fits better with a plugin model. With the NSLINKMODULE_OPTION_RETURN_ON_ERROR option, the model for handling errors is to simply return without any changes to the program. To support this model of error handling a new API has been added to allow the programmer to get the error information that the dyld error handlers would normally have gotten. The API is similar to the dyld linkEdit error handler except that all the parameters are passed as pointers to be filled in.

```
extern void NSLinkEditError(
NSLinkEditErrors *c,
int *errorNumber,
const char **fileName,
const char **errorString);
```

  The last two parameters return pointers to static buffers allocated in the dynamic linker which get reused on subsequent calls to `NSLinkEditError`. The `NSLinkEditErrors` enum has been extended to include `NSLinkEditUndefinedError` and `NSLinkEditMultiplyDefinedError`.

### Notes Specific to OS X Developer Preview Release

### New Features

The following new features have been added to the Compiler Tools since the OS X Server Release.

- The `NSLinkModule` API now can create private modules and the new API `NSLookupSymbolInModule` allows symbols to be looked up in a private module. To do this the interface to `NSLinkModule` has changed in a compatible way from:

```
extern NSModule NSLinkModule(
NSObjectFileImage objectFileImage,
const char *moduleName,
enum bool bindNow);
```

  to:

```
extern NSModule NSLinkModule(
NSObjectFileImage objectFileImage,
const char *moduleName,
unsigned long options);
```

  with the options as follows:

```
#define NSLINKMODULE_OPTION_NONE 0x0
#define NSLINKMODULE_OPTION_BINDNOW 0x1
#define NSLINKMODULE_OPTION_PRIVATE 0x2
```

  The first two are the same as bindNow with a value of FALSE and TRUE. The private options are used to load a private module. The API for getting to the symbols of a NSModule that has been privately linked is:

```
extern NSSymbol NSLookupSymbolInModule(
NSModule module,
const char *symbolName);
```

  Then to get the address of the returned NSSymbol, the existing `NSAddressOfSymbol` API can be used.

  The `NSUnLinkModule` API is now implemented with enough functionality to make Apache work (reference number 2262020). It currently has the following limitations (to be fixed in future releases):

  - Only works for plugins (can only be called on modules that were returned by `NSLinkModule`).
  - C++ plugins that have a static destructor can't be unloaded. The program will crash in atexit(3) when the unlinked destructor is attempted to be called.
  - Objective-C plugins should not be unloaded. The Objective-C runtime has not been updated to know about unloading and the result is very likely to crash the program.
  - The debugger has not been updated to know about unloading and trying to debug a program that unloads its plugins may confuse or crash the debugger.

  The interface to NSUnLinkModule has changed in a compatible way from:

```
extern enum bool NSUnLinkModule(
NSModule module,
enum bool keepMemoryMapped);
```

  to:

```
extern enum bool NSUnLinkModule(
NSModule module,
int options);
```

  where the options are:

```
#define NSUNLINKMODULE_OPTION_NONE 0x0
#define NSUNLINKMODULE_OPTION_KEEP_MEMORY_MAPPED 0x1
#define NSUNLINKMODULE_OPTION_RESET_LAZY_REFERENCES 0x2
```

  The first two are the same as keepMemoryMapped with a value of FALSE and TRUE. The reset lazy references option allows unloading modules with only call sites to undefined functions (direct calls, not calls through pointers) to not cause an undefined symbol error. Then if a subsequent module is loaded that defines symbols that were previously undefined, the call sites will use the new definitions. This is currently only implemented for PowerPC.

  Support for module termination functions has been added for plugins (only). Currently the compiler pragma CALL_ON_UNLOAD (as well as CALL_ON_LOAD) is not yet implemented to use this feature as intended. A work around can be done in place of having the pragma:

```
void my_term(void)
{
/* do module termination */
}
/* #pragma CALL_ON_UNLOAD my_term */
#pragma SECTION data ".section __DATA, __mod_term_func,
mod_init_funcs"
static void (*dummy)(void) = my_term;
#pragma SECTION data
```


### Notes Specific to OS X Server Release

### New Features

The following new features have been added to the Compiler Tools since the Rhapsody Developer Release 2:

- The 4.4bsd ar extended format #1 is now supported by the compiler tools. The default is to use 4.4bsd ar extended format #1 when creating static archives whose member names are longer than 16 characters or have spaces in the name. The tools that create static archives, ar(1), libtool(1) and ranlib(1), all take the options -T (to truncate member names) and -L (to used long member names, the default) (reference 1670513).
- The AltiVec opcodes have been added to the OS X PowerPC assembler. To assemble files with these instructions it requires the option -force_cpusubtype_ALL and then it is the code's responsibility to only use these instructions when the CPU supports them. (references 2237908, 2227999, 2213821, 2004760).
- The header file <mach-o/getsect.h> has been added to the system as the proper place to get the prototypes of the Mach-O routines. (reference 2227839).

### There are no Notes Specific to Rhapsody Developer Release 2

### Notes Specific to Rhapsody Developer Release

### New Features

The following new features have been added to the compiler tools since OPENSTEP 4.2 (NeXT):

- The PowerPC architecture is now supported via the _-arch ppc_ switch.

### Known Problems

These bugs are known to exist in the compiler tools:

### Radar #1670513

4.4BSD ar extended format #1 not compatible with compiler tools.

##### Description:

The 4.4 __ar__ command can create an archive with the base name of an object file that is longer than 16 characters. With the __-L__ option, it produces a format that makes the object file in the archive invisible to various tools, including the static link editor. This can lead to undefined symbols when this archive is linked against. Other tools like __nm__ and __ranlib__ also don't see the long-name object files in the archive. To avoid this problem, __ar__ makes the __-T__ option, which truncates names, a default option. The compiler tools will understand the extended format in future releases.

##### Workaround:

Do not use the __-L__ option with __ar__ when creating archive libraries. Use the __-T__ option (the default for the Premier release) to tuncate file names or use __libtool -static__ to create archive libraries.

### Radar #1666993

The OS X assembler is different from ppcasm.

##### Description:

The major difference is that the OS X assembler is not TOC-based and uses two instructions to load a global or static item. The directives and the syntax of labels and directives of the two assemblers are very different. Also, the OS X assembler is stricter in the parameter types and ranges for instructions. For more on this last topic, see "Instruction Parameter Differences," below.

##### Workaround:

The difference between the OS X assembler and the TOC-based model, plus the differences in directives and syntax, may necessitate significant rewriting of assembly code for the Developer Release. The strict parameter requirements might require rewriting of assembly code for the Developer Release but the resulting code should work with __ppcasm__.

### Radar #1670513

BSD 4.4 ar format is not compatible with compiler tools

##### Description:

The BSD 4.4 __ar__ command, which creates an archive with object file names longer than 16 characters, produces a format that makes the object file invisible to various tools, including the static link editor. This can lead to undefined symbols when a program links against this archive. Other tools like __nm__ and __ranlib__ also don't see the object files with longer names in the archive.

##### Workaround:

Use the __-T__ option with __ar__ to tuncate file names or use __libtool -static__ to create archive libraries.

### PowerPC Assembly Instruction Parameter Differences

Register names can't be designated with just a number. You must refer to them with their register name. This restriction includes general registers (`r`_N_), floating point registers, (`f`_N_), condition registers (`cr`_N_), and segment registers (`sr`_N_). However, you can refer to special registers by their register number or their special register names. The special register names are in lowercase only (for example, `mq`, `xer`, `lr`, `ctr`, and `dsisr`).

For instance, for the _ppcasm_ assember you could code a move from segment register instruction as:

```
mfsr r24,9 ; ppcasm assembler
```

But, for the OS X assembler, this same move would be coded as:

```
mfsr r24,sr9 ; OS X assembler
```

For instructions that take the value 0 or a register, shown in the processor manual as "(rA|0)", r0 can't be used and 0 must be coded. The OS X assembler generates an error messages in these cases.

Where a numeric value is expected as a parameter, a register name can't be use. For example, the _ppcasm_ assembler allows the following:

```
lwz r1,r2(r3) ; ppcasm assembler
```

For OS X, this must be coded as:

```
lwz r1,2(r3) ; OS X assembler
```

The OS X assembler generates a warning if branch prediction is coded with an unconditional branch.

The OS X assembler checks all fields for range errors and generates error messages if an expression is out of range. The _ppcasm_ assembler simply uses the low _N_ bits of the expression (where _N_ is the field width) if the value is greater than zero. For example the simplified mnemonic:

```
inslwi r
A
,r
S
,
n
,
b
```

is equivalent to

```
rlwimi r
A
,r
S
,32-
b
,
b
,(
b
+
n
)-1
```

The following code:

```
inslwi r17,r18,19,20 ; equivalent to rlwimi r17,r18,32-20,20,(20+19)-1
```

assembles to

```
rlwimi r17,r18,12,20,6 ; where the low 5 bits (20+19)-1 is 6
```

with _ppcasm_. This generates an out-of-range error with the OS X assembler.

For fields less than zero, the _ppcasm_ assembler uses the value of zero. For example, the simplified mnemonic:

```
clrlslwi r
A
,r
S
,
b
,
n
```

is equivalent to

```
rlwinm r
A
,r
B
,
n
,
b
-
n
,31-
b
```

Thus the following code:

```
clrlslwi r5,r6,7,8 ; equivalent to rlwinm r5,r6,8,7-8,31-7
```

assembles to:

```
rlwinm r5,r6,7,0,24 ; where 7-8 gets turned into 0
```

with _ppcasm_. This generates an out-of-range error with the OS X assembler.

All integer expressions in the OS X assembler are signed 32-bit values. Parameters that are 16-bit signed or unsigned immediate values must agree in their upper 16 bits or the assembler generates an out-of-range error message.

For example:

```
addi r1,r2,0xffff ; out of range for a 16-bit signed immediate
```

generates the message "Parameter error: expression out of range (parameter 3)".

The `addi` instruction takes a signed immediate value so it will sign extend its parameter to 32 bits before performing the operation. If the value 0xffffffff is intended, it would be coded as:

```
addi r1,r2,0xffffffff
```

If this is half of a two-instruction 32-bit add it should be coded as:

```
addis r1,0,ha16(expression)
addi r1,r2,lo16(expression)
```

Many of the simplified mnemonics are implemented as OS X assembler macros (as noted in the listing of PowerPC assembler instructions in the assember manual). Like all macros, the macro is expanded and assembled. This expansion can result in errors that can seem confusing when you look at the coded macro. For example, the simplified mnemonic:

```
extldi r
A
,r
S
,
n
,
b
```

is equivalent to

```
rldicr rA,rS,b,n-1
```

Thus the following code:

```
extldi r1,r2,0,2
```

generates the error message "Parameter error: expression out of range (parameter 4)," which refers to "n-1" or "0-1", or parameter 4 of the expanded macro.

The instruction `tlbiex`, which has been removed from the PowerPC architecture, is not supported by the OS X assembler. This instruction is assembled by _ppcasm_.
