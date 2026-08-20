---
title: GDB Release Notes
apple_id: TP40001008
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-GDB/index.html
archived_at: '2026-07-18T02:50:26.830190Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# GDB Release Notes for OS X v10.5 WWDC Seed

> [!IMPORTANT]
> 

For complete information about GDB, please refer to the _[Debugging with GDB](https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_toc.html#//apple_ref/doc/uid/TP40000996)_.

#### Contents:

- [Changes Since Xcode 2.4.1 (gdb-563)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Changes since Xcode 2.2 Developer tools update (gdb-437)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Changes since August 2004 Devtools update (gdb-330.1)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Changes since June 2003 Developer Preview (gdb-282):](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Changes since December 2002 Devtools update (gdb-250):](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [Changes since MacOS X 10.2 (gdb-228):](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)
- [Changes since MacOS X 10.1:](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytambyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ny)

### Changes Since Xcode 2.4.1 (gdb-563)

- DWARF is the primary debug format

  Beginning with Leopard, DWARF (and DWARF + dSYM) is the primary, supported debug file format. The older format, stabs, will continue to work but no further development will be done to improve or enhance stabs. If you cannot transition your project to DWARF because of a problem with the tools, please file a bug report.
- Inlined function debugging support

  When debugging with DWARF, gdb will now treat inlined functions much like normal functions. You can set symbolic breakpoints on the inlined functions, you can next over inlined functions, you can step in to an inlined function and get a backtrace.
- More accurate reporting of variables optimized away

  When a variable has been optimized away by the compiler, instead of the old behavior (sometimes being told "variable optimized out" and sometimes being told gdb never heard of the variable), the debugger will always report "variable optimized away by the compiler" when the DWARF debugging format is used.

  When you request to see a variable which gdb can't currently get the value for (but which was not entirely optimized away by the compiler), instead of being told "variable optimized out", gdb will now report "value temporarily unavailable, due to optimizations" when the DWARF deubgging format is used.

  If you get the "temporarily unavailable" message, you can use the command "`info address <var>`" to see a list of address ranges where the value will be available. Then by monitoring `$pc` you can proceed to a location where you can examine the variable.
- Hardware watchpoint support on x86

  gdb can now use the hardware watchpoint support on 32-bit x86 programs. This will yield faster and more accurate watchpoint behavior for this architecture.
- `watch -location`

  The `watch` command has a new flag: `-location`. If you specify this flag (it has to be first in the command line, before the expression you are going to watch) then gdb will resolve the expression you've passed it to a memory location, and then just watch that. This is useful, for instance, if you want to watch a local variable which contains a pointer to memory, since watching the local variable will cease to work when the variable goes out of scope. It is also useful when you just want to watch what `foo->bar->baz` points to, and don't want to watch the "`foo`" or "`bar`" components in-between.
- New `-arch` command line argument

  By default, when gdb is running on a 64-bit capable CPU and has a universal file, it will examine/run the 64-bit side of that file. The gdb `-arch` option can now be used to specify which fork of a binary gdb will run. For instance, if you are on a G5 and have a Universal ppc/ppc64 binary, then:

```
$ gdb -arch ppc MyUniversalFile
```

  will run the 32 bit (ppc) side of the Universal binary. The valid options are `ppc`, `ppc64`, `x86` and `x86_64`.
- New `--waitfor` argument

  To catch processes that must launch outside gdb early in their startup, gdb has added a `--waitfor` command line argument and argument to the `attach` gdb command. `--waitfor` is followed by the name of the process to wait for. When `--waitfor` is used, gdb will poll repeatedly looking for the process to start running. As soon as gdb notices that the process is running, it will attach to the process, pause it, and give you the gdb prompt.
- Debugging KEXTs with DWARF

  Debugging system kernel extensions with the DWARF debug format requires a few special steps. First, you must build your project with the "DWARF with dSYM" build style. Second, you must keep an unstripped copy of your `.kext` bundle in addition to the `dSYM` bundle. When you run `kextload(8)` to load your kext you will get a `.sym` file -- you will need this piece as well.

  Put all three pieces -- the unstripped `.kext` bundle, the `dSYM` bundle and the `.sym` file in the same directory. Launch gdb as you normally would and load the kext by using the new `add-kext` gdb command instead of `add-symbol-file` as was done in the past.

```
(gdb) add-kext myextension.kext
```

  There is one additional setting that may help adjust to this new workflow: `kext-symbol-file-path`. This setting specifies a directory to search for the `.sym` file. For instance you may have your `dSYM` and `.kext` bundles in a working directory and your `.sym` files are in `/tmp`. You can avoid unnecessary copying of either of these by setting

```
(gdb) set kext-symbol-file-path /tmp
```
- Locating dSYM files

  In Xcode 2.4, the dSYM file for an executable had to be placed in the same directory as the executable for gdb to find it. There is a new framework for locating dSYM files, `DebugSymbols.framework`, that will be used by various developer tools to locate dSYM files automatically in other locations. By default, dSYM files will be searched by a Spotlight search and by implicit search paths. Defaults can be written to the `com.apple.DebugSymbols` to modify this behavior via the `defaults(1)` command line tool.. The full list of recognized settings is:

  - `DBGShellCommands`

    Shell commands can be used to return the paths to the matching dSYM files for provided UUIDs. Shell commands can provide a level of abstraction from the method of storing the UUID to dSYM mapping information, and allow build systems to store the data in a wide variety of ways. No shell command will be run by default.

    UUID values are specified to stdin of the shell command with one UUID value specified on a line with no leading or trailing white spaces. The command reads until the EOF and returns any matches to stdout.

    The shell command will return UTF8 encoded XML as a property list. Each UUID will result in a key whose value is the UUID string, with a dictionary of key/value pairs containing the results. All dictionary key value pairs are optional. The list of currently supported keys are:

    - `DBGError`

      An error describing why a the search failed.
    - `DBGDSYMPath`

      The path to the dSYM file.
    - `DBGSymbolRichExecutable`

      The path to the unstripped executable (if any).
    - `DBGSourcePath`

      The path to the sources for the executable.

    The number of supported keys may be expanded in the future to support more features.

    The shell commands to be used can be specified by setting the "DBGShellCommands" key to be a string for a single shell command, or an array of strings for multiple shell commands:

```shell
$ defaults write com.apple.DebugSymbols DBGShellCommands -string /usr/bin/find-dsym
$ defaults write com.apple.DebugSymbols DBGShellCommands -array /usr/bin/find-dsym /Network/bin/find-dsym
```

    To disable shell command searching we can write a boolean value set to false, or delete the key altogether:

```
defaults delete com.apple.DebugSymbols DBGShellCommands
```
  - `DBGSpotlightPaths`

    The spotlight paths used to limit a spotlight search to certain directories can can be specified by setting the "DBGSpotlightPaths" key to be a string for a single path, or an array of strings for multiple paths:

```shell
$ defaults write com.apple.DebugSymbols DBGSpotlightPaths -string /single/path/to/search
$ defaults write com.apple.DebugSymbols DBGSpotlightPaths -array /path/to/search1 /path/to/search2
```

    In order to allow spotlight searches along with other preferences, yet not limit the spotlight search to any directories, we create an empty array:

```
$ defaults write com.apple.DebugSymbols DBGSpotlightPaths -array
```

    To disable spotlight searching we can write an write a boolean value set to false:

```
$ defaults write com.apple.DebugSymbols DBGSpotlightPaths -bool NO
```
  - `DBGSearchPaths`

    The explicit search paths can can be specified by setting the "DBGSearchPaths" key to be a string for a single path, or an array of strings for multiple paths:

```shell
$ defaults write com.apple.DebugSymbols DBGSearchPaths -string /single/path/to/search
$ defaults write com.apple.DebugSymbols DBGSearchPaths -array /path/to/search1 /path/to/search2
```

    To disable explicit directory searching, delete the default key:

```
$ defaults delete com.apple.DebugSymbols DBGSearchPaths
```
  - `DBGFileMappedPaths`

    File mapped paths allow users to specify a directory that contains shallow or deep UUID symlinks that point to the dSYM files.

    A UUID whose value is C6F7EDC5-74C0-4CA8-A21D-ACED1357D811 whose dSYM file resides at /symbols/foo.dSYM has a shallow file mapped symlink that would appear as:

```
$ ls -lAF C6F7EDC5-74C0-4CA8-A21D-ACED1357D811
C6F7EDC5-74C0-4CA8-A21D-ACED1357D811@ -> /symbols/foo.dSYM
```

    The same UUID and file would have a deep symlink that would appear as:

```
$ ls -lAF C6F7/EDC5/74C0/4CA8/A21D/ACED1357D811
C6F7/EDC5/74C0/4CA8/A21D/ACED1357D811@ -> /symbols/foo.dSYM
```

    The file system mapping paths can be specified by setting the "DBGFileMappedPaths" key to be a string for a single path, or an array of strings for multiple paths:

```shell
$ defaults write com.apple.DebugSymbols DBGFileMappedPaths -string /single/path/to/search
$ defaults write com.apple.DebugSymbols DBGFileMappedPaths -array /path/to/search1 /path/to/search2
```

    To disable file mapped path searches, delete the default key:

```
$ defaults delete com.apple.DebugSymbols DBGFileMappedPaths
```
- Disabling dSYM lookups altogether

  You can instruct gdb to do none of the advanced dSYM lookup methods by setting `locate-dsym`.

```
(gdb) set locate-dsym 0
```

  gdb will still look for dSYM files next to the executable being debugged.

  This setting is particularly useful if you are writing code that may cause low level systems like Spotlight or DirectoryServices to be slow, hang or crash. The advanced dSYM lookup methods depend on these services and it is possible to hang your system requiring a reboot in some rare cases.
- Live kernel debugging

  The live kernel debugger permits examination of the running kernel's memory image. To use this facility,

  1. The system must be started with the "`kmem=1`" kernel boot-arg. To do this, issue the command: `sudo nvram boot-args="kmem=1"` (along with any other kernel boot-args set previously) followed by a restart.
  2. GDB must be started as the superuser:

```
$ sudo gdb <location of kernel image with debugging symbols>
```

     ("`/Volumes/KernelDebugKit/mach_kernel`", if you have the kernel debug kit diskimage for your OS X release mounted)
  3. Issue the following commands at the GDB prompt:

```
(gdb) target darwin-kernel
(gdb) attach
```
  4. GDB is now ready to examine the currently executing kernel's memory image. You can issue:

```
(gdb) source <location of kernel debugging macros>
```

     ("`/Volumes/KernelDebugKit/kgmacros`", for instance) to load the xnu kernel debugging macros. You may now execute kernel debugging macros ("`help kgm`" for a list) and examine kernel variables and data structures.

  Things to be aware of:

  - Your view of the kernel isn't necessarily coherent--this is a live kernel, and you may see some inconsistencies while examining memory locations that are being actively altered. Thread stacks and such can potentially mutate while you're in the process of examining them; in most debugging scenarios however, you're examining threads that are blocked in some fashion--stack frames are relatively stable in such cases.
  - The live kernel debugger does not support altering kernel memory, i.e. it is read-only. Most kernel debugging macros don't manipulate register state or alter memory, so they will function correctly, with the caveats regarding actively changing areas noted above.
- `info malloc-history`

  This is a new command in gdb. It is to be used with the "`MALLOC_STACK_LOGGING_NO_COMPACT`" malloc stack logging environment variable. If you run with this on, then in gdb, you can say:

```
(gdb) info malloc-history <SYMBOL/ADDRESS>
```

  and we will return the stacks of all the instances where data was malloc'ed at that address.
- `info gc-roots` / `info gc-references`

  This is a new command. It is only useful when you are debugging an Application that is running with the Objective-C Garbage Collection enabled. In that case,

```
(gdb) info gc-roots <ADDRESS/SYMBOL>
```

  will tell you all the unique shortest roots to a given symbol, and

```
(gdb) info gc-references <ADDRESS/SYMBOL>
```

  will tell you all the objects in the collector that reference the given symbol or address.
- Limit Function Names Displayed During Disassembly

  gdb now has a setting, `disassembly-name-length`, which limits the length of function names that are printed during disassembly. C++ in particular can have very long mangled function names which can make it difficult to read the disassembly. Use it like this:

```
(gdb) set disassembly-name-length  5 (gdb) disass $pc Dump of assembler code for function _ZN11TDescriptor12InitBaseFontEv: 0x94adf226 <_ZN11+0>:    push   %ebp 0x94adf227 <_ZN11+1>:    mov    %esp,%ebp 0x94adf229 <_ZN11+3>:    push   %edi 0x94adf22a <_ZN11+4>:    push   %esi 0x94adf22b <_ZN11+5>:    sub    $0x10,%esp     
```
- Fix and Continue build settings

  There are two new build settings in Xcode that should not be enabled if you are going to use the Fix and Continue feature:

  - "Generate Position-Dependent Code" must be disabled (unchecked).
  - "Symbols Hidden by Default" must be disabled (unchecked).

  These settings can be set as you please for your Release configuration but if you'd like to use Fix and Continue while debugging you will need to disable them for your Debug configuration.
- Debugging with libgmalloc and zsh

  If you are using zsh as your shell and want to run your program with libgmalloc under gdb you must do

```
(gdb) set start-with-shell 0
```
- CFM runtime support disabled by default

  If you are debugging CFM applications on PowerPC systems you will need to enable this support before executing your program by setting

```
(gdb) set inferior-auto-start-cfm 1
```

  Either on at the gdb command prompt or by adding this to your `$HOME/.gdbinit` file.

### Changes since Xcode 2.2 Developer tools update (gdb-437)

- Support for DWARF debug file format

  GDB now supports the use of the DWARF debug file format. It can work with DWARF in one of two ways: The debug information is stored primarily in the .o object files with a little bit in the executable, and with all of the debug information collected into a dSYM file and no debug information in the executable.

  For normal change-compile-debug, change-compile-debug workflow, leaving the debug information in the .o files is the intended usage. A dSYM file should be created when you are distributing your binary to another person who will need to debug it, or archiving the debug information of a release binary so you can debug crash reports/bugs that are reported to you later.

  In the case of debug information in .o files, the .o files must remain in their original location for gdb to find them. They may be copied to another system, but the pathname must remain the same -- or soft symbolic links (cf ln(1)) must be put in place.

  In the case of a dSYM file, `dsymutil(1)`, is run on the executable file before stripping to create the dSYM. After that has been done, the binary may be stripped and released - you will be able to use the dSYM file along with the stripped binary to debug it later. The dSYM file must be next to the binary you are debugging for GDB to find it. For instance if your application is `/path/to/my/Fun.app`, the dSYM file should be named `/path/to/my/Fun.app.dSYM` or GDB will not read in the dSYM file. There is currently no way to specify the location of a dSYM file to gdb -- again, soft links are one workaround if copying the file into place is not feasible.

### Changes since August 2004 Devtools update (gdb-330.1)

1. Lazy symbol and on-demand symbol loading under Xcode

   When gdb is used under Xcode, and the `Load symbols lazily` Debugging preference is checked, gdb will postpone symbol reading until the symbols are needed. This optimization will yield faster start-up times, particularly on larger applications.

   For developers with command line proclivities, some caution is needed when using Xcode and lazy symbol loading. When the application, dylib, bundle, or framework hasn't had a breakpoint set in it, or you haven't stopped execution while the PC was contained in that app/dylib/bundle/framework, gdb won't know anything about the symbols in that file so breakpoints in that file can't be set as you normally would. For instance, you run your application under Xcode, then pause it and open the Console window. In the Console window you type "`break MyFile.c:85`". If the symbols for the executable file containing `MyFile.c` haven't been loaded yet, gdb won't know where to set this breakpoint. In the case of a ZeroLink application where every source file is in its own bundle, this can happen often.

   Breakpoints set from the Xcode UI will be handled correctly because Xcode knows which executable file contains that source file and communicates this information to gdb. You can force the symbols to be read for a file by either disabling lazy symbol loading (Xcode's Debugging Preferences), or once the app is running, Pause execution, open the __Debug > Tools > Shared Libraries__, and raise the load level of the executable file you're working in to "__ALL__".

   From the debugger Console window in Xcode, if you are setting a breakpoint with the break command and want to inform gdb which executable file contains that breakpoint (so the symbols for that file are read in), you can use the `-shlib` argument to the break command. e.g. for the Sketch sample application, built in ZeroLink mode, you would do this to tell gdb that it should read in the symbols for the SKTGraphic ZeroLink bundle:

   `break -shlib SKTGraphic.ob SKTGraphic.m:19`

   Lazy symbol loading is only in effect when using gdb under Xcode. None of these caveats are required when using gdb from the command line.
2. Cached symfiles are no longer enabled

   The cached symfile feature has been superseded by the lazy and on-demaned symbol loading.
3. Support for 64-bit executables

   GDB now has support for debugging 64-bit executables.
4. No longer necessary to set osabi when working with 64 bits

   In previous gdb releases, it was necessary to use set `osabi Darwin64` to examine the full contents of registers in a 32-bit app on a processor with 64-bit registers. This is no longer necessary.
5. gdb's .app app bundle support works for more bundle layouts

   gdb will now look at the `CFBundleExecutable` key in the application bundle's `Info.plist` and look for the executable under that name. So the shortcut gdb `/My/Workdir/MyProg.app` will work for more applications.
6. gdb can step through a longjmp call

   If your application has a `setjmp()/longjmp()` call, stepping will work correctly through the longjmp.
7. Performance improvements for single stepping with data formatters

   The stepping speed in Xcode when there are custom data formatters that require function calls has been improved. For instance, in an Objective-C application, if you have a number of `NSString` local variables in a function, gdb must call one function per object after stepping to see if the contents have changed.
8. Calling Dead Code Stripping-elided functions in Fix and Continue won't work

   If you are developing with Dead Code Stripping, and you add a call to a function that has been stripped by DCS in the process of Fixing a source file at debug-time, that call will not work. You must do a re-link of your program, at which point the Dead Code Stripping feature will recognize the new call to the stripped function and keep the function in your executable.

### Changes since June 2003 Developer Preview (gdb-282):

1. Performance improvements for ZeroLink debugging

   Most of the performance problems when debugging large ZeroLink applications have been resolved. Start-up time remains a bit slower with ZeroLink applications versus traditionally linked applications, but after that gdb performs well.
2. Performance improvements for Carbon applications

   gdb will require less memory to debug Carbon applications than was often required previously. This was done with a change to the compiler, so you will need to rebuild your application with gcc 3.3 to realize these benefits.
3. Fixes for Fix & Continue

   A number of minor bugs were patched in the Fix & Continue feature, particularly with ZeroLink programs, multi-threaded programs which have many threads being created/destroyed, and cached symfiles. Several more illegal changes will correctly be reported as errors and the fix operation will be backed out.
4. Fixes for cached symfiles

   A number of fixes for cached symfiles were made, including renaming the gdb commands for better consistency. The previous release notes have been updated to reflect the new command names (using the word "cached" instead of "precompiled"). The old ("precompiled") names are deprecated, but will continue to work until the next major release.

### Changes since December 2002 Devtools update (gdb-250):

1. Support for cached symbol files

   GDB is now able to generate and used cached versions of symbol files, to speed up symbol reading. Cached symbol files should behave exactly like normal symbol files, except that they are significantly faster for GDB to read into memory. By default, the GDB installer builds cached symbol files for all system libraries in `/usr/libexec/gdb/symfiles`; you can regenerate these files using the `/usr/libexec/gdb/cache-symfiles` command. In the event that you run into a problem that you think might be related to cached symbol files, you can remove the `/usr/libexec/gdb/symfiles` directory, and GDB should behave normally.

   - `set use-cached-symfiles`

     Determines if GDB will use cached symbol files that it finds on the system. Defaults to on. Note that if you set this to off in your `.gdbinit`, it may not have the behavior you expect, since GDB parses the `.gdbinit` file after loading any executables specified on the command-line.
   - `set cached-symfile-path`

     Specifies a colon-separated set of directories that will be searched for cached symbol files, if use-cached-symfiles is set.
   - `sharedlibrary cache-symfile <filename> <destination>`

     Generates a cached symbol file for filename into the file or directory specified by `destination`. If `destination` is a directory, GDB will store the cached symbol file using the basename of the library, with `.syms` appended.
   - `sharedlibrary cache-symfiles <shlibnums> <destination>`

     Stores cached symbol files for all of the shared libraries specified by `shlibnums`. The value of `destination` is treated the same way as in `sharedlibrary cache-symfile`.
2. Support for app wrappers

   It is no longer necessary to point gdb at the binary in an application wrapper directory ("`app-name.app/Contents/MacOS/app-name`"). If you point gdb at the wrapper directory, it will look for the binary in the correct place.
3. 64-bit support

   GDB now contains basic support for debugging 64-bit programs, including several new opcode mnemonics, extended branch-prediction decoding, and 64-bit register support. To indicate to GDB that it should use 64-bit register accesses for a particular program, use the `set osabi Darwin64` command before running the executable.
4. C++ exception catching

   We added support for the `catch catch;` and `catch throw;` commands in gdb. If you set either one of these, gdb will stop on C++ exception catching and throwing, respectively. The gdb online docs are wrong, however, we don't support catching a particular exception by the `catch catch exception` syntax. Instead, you can set the gdb variable `exception-{throw,catch}-type-regexp` to any regular expression, and gdb will stop if the exception name matches the regexp. If you have many shared libraries, you will see catchpoints are set. That is to be expected - each shared library gets its own copy of the C++ runtime support, including the catch & throw routines. To stop catching exceptions, just delete the catchpoints.
5. print-object crashes will now unwind the stack automatically

   The `print-object` command now sets `unwindonsignal` unconditionally when calling the description on the object. This means that if the `print-object` crashes, the stack will unwind back to where you called it, and provided your objects description method doesn't affect program state you can continue safely.
6. Support for scheduler locking

   OS X gdb now supports the `schedlock` on gdb flag. You can use this to halt all the other threads but the current thread when you continue. This is useful if you want to run introspection calls in the target program without running the other threads. Be careful not to cause deadlocks in this situation.
7. Altivec vector printing

   A number of bugs (mostly in the debug output of gcc) have been fixed that affected printing Altivec vector variables. Since the bugs were mostly in the compiler, you will need to rebuild your code, but then you should have more success examining your altivec variables in gdb. Note that none of the bugs caused errors in the actual use of the vector variables, just the debug info was wrong.
8. `sharedlibrary specify-symbol-file`

   GDB now allows the user to specify the symbol file that should be loaded for a specific shared library loaded by the application using the `sharedlibrary specify-symbol-file` command. GDB will relocate the symbol file to the correct address for that shared library entry, unlike the previous behavior of `add-symbol-file`.
9. New output format for `info sharedlibrary`

   The 'Source' field of the output of `info sharedlibrary` can now include up to two additional fields. The second, if present, is the name of the object file to which the shared library entry actually refers (typically only used in ZeroLink binaries). The third, if present, is the name of the cached symbol file read in for the shared library in question.
10. "self" vs. "this" in ObjC++

    We now use the current function name to determine whether a function in an ObjC++ file is C++ -- and thus has member data hanging off "`this`", or ObjC -- and thus we should look up "`self`".
11. `thread_abort_safely`

    We now call `thread_abort_safely` before running functions in the target program. This makes it safe to call functions like pthread_self() on a thread that is blocked in the kernel - previously the call would just hang. This does mean if a thread is waiting in a kernel call, calling a function in the target on that thread will cause the kernel call to return with an EINTR. This will not cause a problem if your code protects against spurious wake-ups, which it should do. It is just something to be aware of.
12. `info threads` port numbers

    We now map the port numbers for threads that gdb receives back to the port space of the target program, so the output of `info threads` will match the return of `thread_self()`. This still provides a convenient way to match up your threads with what gdb presents.
13. `info mach-regions`

    This command now works correctly, rather than looping infinitely at high address ranges.

### Changes since MacOS X 10.2 (gdb-228):

1. Support for break ... `if <expression>`

   GDB now correctly supports the break ... `if <expression>` for specifying breakpoint conditions at the same time as a breakpoint.
2. Improved backtracing

   A number of fixes have been made to the backtrace mechanism, particularly for backtracing through signal handlers, corrupt stacks, and optimized code. If you find a situation where GDB fails to generate a correct backtrace, please file a complete bug report.
3. Improvements to `detach`

   It is now possible to detach from programs at any time, even if they were originally started from within GDB. Detaching from a program started from GDB will close that program's input stream.
4. Watchpoints on the contents of arrays

   GDB now supports the use of watchpoints on entire arrays. Given the declaration "`int x[100];`", the command `watch x` will cause GDB to stop whenever any element of `x` changes.
5. Improved register display

   The display of floating-point and Altivec registers has been cleaned up to be more legible. The new command `info float` and `info vector`. allow display of the floating-point and Altivec registers independently of the other registers.
6. More reliable variable lookup

   GDB is now configured with `set read-type-psyms 1` enabled by default. For more information, see "What to do if GDB is not finding types it should," below.
7. More reliable C++ stepping and breakpoints

   A number of bugs were fixed with C++ stepping and breakpoint handling. Stepping into and breaking on methods defined in header files should now be much more reliable (although there are still some issues stepping into inlined C++ functions in header files). If you find any bugs with either C++ stepping or breakpoint handling, please file a complete bug report.
8. Altivec variable display

   GDB now correctly displays the values of Altivec variables on the stack/heap. It no longer prints an extra f field for each variable, and correctly displays each of the separate vector subtypes of each variable. As several aspects of the Altivec improvements were the result of compiler changes, you will need to re-compile Altivec code in order to get the improved debugging support.
9. Improved C++ type detection

   The `set print object` command can be used to have GDB automatically detect the type of C++ objects based on their virtual table information. This was present in previous versions of GDB, but should be substantially more reliable in the current release. This feature should not be enabled when running under Xcode, as Xcode already gets the same information via a different mechanism.
10. Shared library processing

    GDB now models each executable as a single object file that can optionally load a number of associated images. GDB uses the properties of `exec-file` (or dyld, if the program is running) to determine which shared libraries to load, and the value of `symbol-file` to determine where to find `symbol-file` for the main executable. The result is that the `symbol-file` now behaves as one would expect. A number of bugs in shared library handling (mainly to do with slid executables) have also been fixed.
11. New commands `dump`, `append`, and `restore`

    These commands allow data to be copied from target memory to a bfd-format or binary file (`dump` and `append`), and back from a file into memory (`restore`).
12. Changes to command line processing

    The new `--args` feature can be used to specify command-line arguments for the inferior from the command line of GDB.
13. Reloading a changed app should no longer cause crashes

    If you launch gdb, load in and run an app, and quit the app, but NOT gdb, then in another terminal window rebuild the app, and finally re-run the app in the old gdb session, it has in the past been possible that gdb will crash (this was not true if you re-ran the app without rebuilding). We believe that all such crashes have are fixed in this release. If it should crash for some reason, the workaround is to quit and restart gdb each time you rebuild your app, as well as to file a full bug report using the normal channels.

### Changes since MacOS X 10.1:

1. Hardware (page protection) watchpoint support

   Hardware watchpoints are now supported, with a few limitations. They are implemented using the page-protection mechanism of Mach, not using the hardware watchpoint register. To insert a watchpoint, gdb write-protects the entire page containing the memory address, then traps for write faults to that page. Unfortunately, the Mach kernel does not generate a write fault when a system call tries to write to a protected page --- instead it returns error status to the calling application. So, for example, if you try to read() from a file into memory on any page that contains a watchpoint, read() will return with EADDR, rather than triggering the watchpoint. Also, watchpoints on stack addresses (local variables being the most likely example) can sometimes cause unexpected results.

   To use watchpoints in Xcode, use the gdb console. For more information about watchpoints in gdb, please refer to the [watchpoints section of the gdb manual](https://developer.apple.com/documentation/DeveloperTools/gdb/gdb/gdb_6.html#SEC31).
2. "step" or "next" over code that is generating signals:

   You should now be able to use gdb's "step" or "next" commands to step through code that is generating signals (for instance through a SIGALRM timer). Previous versions of gdb would occasionally report an error that the target stopped with TARGET_WAITKIND_SPURIOUS; we believe this to be fixed. If you encounter such an error; please file a complete bug report --- in the meantime you can work around the problem by using breakpoints and the "continue" command to move through this code.
3. Targets who have children who crash

   Gdb now properly handles exceptions from children of the program being debugged. Previously, gdb would intercept any exception sent to a child of the program being debugged, and treat it as if it were an exception to the parent. Now it correctly forwards the exceptions to the child, where they are handled normally.
4. What to do if gdb is not finding types it should

   There are two optimizations - one in the compiler, and one in gdb itself - that can cause gdb not to find types that actually are defined in your code. You will see this, for instance, if you try to call "ptype" on a pointer, and get "<unknown>" instead of the correct type. Of course, printing the pointer will also fail in this case.

   There are two potential causes for this.

   The first, and easiest to fix, is that gdb does not, by default, read in all the types when it reads in the symbols for your executable and libraries. This is because reading in types for all the libraries for a complex Mac app can take 3 or 4 seconds, and so we try to defer reading them till the types are actually used. Usually, the process of getting to a point where you can print a type will cause gdb to bring in all the relevant type information, but this is not foolproof. To switch this default, add the line:

   `set read-type-psyms 1`

   to your `.gdbinit` file.

   If that does not fix the problem, you may be running into a bug in gdb's ability to read the compressed type definitions that the "-g" option to gcc3 produces. gcc3 will only emit debug output for a type in any given compilation unit if the type is actually used in that compilation unit. This will make the compile and link go faster, so it is a good thing to do. But for relatively complex type definitions, particularly with C++, this can make the debug output harder to parse, and in some cases, gdb does not parse them correctly.

   To get around this, you can turn off this compressed type definition by using the "-gfull" option to the compiler. In Xcode, you can just add this to the OTHER_CFLAGS entry field in the Target panel. In many cases, particularly with C++, this will fix the problem, and you will be able to print all the types in your code again.
5. Using gcc2-compiled code with gcc3-compiled libraries

   Gdb assumes that it will never see a mix of gcc2 and gcc3 compiled C++ code in a single executable. So it determines which abi to use by setting it to gnu-v2, and then if it ever sees a v3 style mangled name, it switches it to v3. This breaks down in the case where you have some shared libraries compiled with gcc3, but the user code is compiled with gcc2. This is a perfectly okay thing to do if the libraries don't export any C++ symbols, but gdb will get the abi wrong, and you won't be able to print any C++ objects in the user code.

   To help in this situation, we have added the 'set cp-abi' command. Useful values are "gnu-v2" and "gnu-v3". You can use this to set the appropriate value by hand if you notice the problem arising.
6. "run" commands in `.gdbinit` scripts

   The "run" command issued in the startup .gdbinit script no longer works; instead, it causes gdb to hang. We will try to fix this. In the meantime, if you were using the "run" command in your .gdbinit to avoid having to type out a long argument string to pass to the program you are debugging, you can use the "set args" command instead, and just type "run" once gdb has started up.
7. Improved C++ support, particularly for gcc3-compiled code

   A number of improvements have been made for debugging C++ code, particularly C++ code compiled with gcc3. Notable improvements include more reliable support for calling virtual functions of classes, as well as better template support. If you have had problems debugging C++ code in the past because of limitations, you will want to check out the new support --- please report any bugs you may find.
8. Debugging CFM Applications

   Gdb does not support reading the symbolic information for CFM based applications. However, you can do assembly level debugging, and if you build your project with Traceback Tables Inlined (set in Project Preferences->Code Generation->PPC Processor in CodeWarrior) you will be able to see function names in backtraces.
   The only trick to this is that the system does not launch CFM Apps from the command line, it uses a helper app to do this. So to debug MyApp, you do:

```
$ gdb /System/LibraryFrameworks/Carbon.framework/Versions/A/Support/LaunchCFMApp
GNU gdb 5.1-20020125 (Apple version gdb-211) (Wed Mar 27 01:41:44 GMT 2002)
Copyright 2000 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "powerpc-apple-macos10".
Reading symbols for shared libraries ... done.

(gdb) run /Users/Myself/Build/MyApp
```
9. Finding the Mach-O executable in an App package:

   When you want to run an executable that you have built in an App package in gdb, you need to point gdb at the actual executable, and not the App package directory. For instance, if your application package is in `/Users/Myself/Build/MyApp.app`, then you would run gdb as:

   `$ gdb /Users/Myself/Build/MyApp.app/Contents/MacOS/MyApp`
10. Running a project with its own Framework under command-line gdb:

    When you debug a Project which uses its own framework(s) under gdb, you need to tell the dynamic loader where to find your framework files. To do this, set the environment variable `DYLD_FRAMEWORK_PATH` to point to the directory that contains your framework. You can do this inside gdb by saying:

    `(gdb) set env DYLD_FRAMEWORK_PATH /Users/Myself/Build`

    before you run the executable.

    > [!NOTE]
    > 
11. Setting breakpoints when you have LOTS of code in Frameworks:

    If your application is factored into many Frameworks, then setting breakpoints can be painful, since you have to wait till the Framework containing the code is actually loaded before gdb can successfully set the breakpoint. Gdb has the "future-break" command for just this situation. So you say:

    `(gdb) future-break someCode.c:123`

    and gdb will try to insert this breakpoint each time a new framework is loaded. You will see error messages telling you the breakpoint was not inserted each time a Framework is loaded, until gdb manages to set the breakpoint. Don't worry about these, they are just gdb trying to keep you up to date on its efforts.
12. Controlling symbol loading from Frameworks:

    Mac apps load many frameworks, either directly or implicitly. This can lead to long startup times as gdb processes the symbols in these frameworks. In gdb-200, we added a new set of commands that allow you to control the level of symbol loading from shared libraries. Look at the help for "set sharedlibrary load-rules" for details on how to use this facility.
13. Vector variables in registers in gcc2

    If a vector variable is stored in a register, gcc writes debug information telling gdb which register the variable is stored in. Unfortunately, the mapping changed between gcc2 & gcc3. Since there isn't anything in the debug output to distinguish code compiled by gcc3 from code compiled by gcc2, there is no way for gdb to know the right map. gdb supports the gcc3 map. If you happen to know your vector code is compiled by gcc2, then the register assignment will be off by 1. To get it right, you will need to look at the register one less than the given one (so if "info address v_var" says vr3, it is actually in vr2...). OTOH, if you are compiling your AltiVec code with gcc2, you should seriously consider switching to gcc3 anyway, since it does a much better job of optimising AltiVec code.
14. Disassembler bug with stwcx. and the like...

    The gdb disassembler has a bug with all the PowerPC store instructions, like stwcx., where the first argument is either 0, if the value is zero, or the name of the register from which to read the offset if non-zero. GDB will errantly report the "0" case as "r0". So for instance, you will see:

    `stxcw. r5,r0,r2`

    which should actually be:

    `stxcw. r5,0,r2`
