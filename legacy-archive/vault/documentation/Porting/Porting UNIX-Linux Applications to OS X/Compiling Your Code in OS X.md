---
title: Porting UNIX/Linux Applications to OS X
apple_id: TP30001003
resource_type: Guide
platform: macOS
topic: Cross Platform
technology: null
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingUnix/compiling/compiling.html
archived_at: '2026-07-18T01:50:44.332899Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting UNIX/Linux Applications to OS X](Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md)


[Next](Using%20OS%20X%20Native%20Application%20Environments.md)[Previous](Preparing%20to%20Port.md)

# Compiling Your Code in OS X

Now that you have the basic pieces in place, it is time to build your application. This section covers some of the more common issues that you may encounter in bringing your UNIX application to OS X. These issues apply largely without regard to what type of development you are doing.

If you are bringing a preexisting command-line utility to OS X that uses GNU `autoconf`, `automake`, or `autoheader`, you will probably find that it configures itself without modification (though the resulting configuration may be insufficient). Just run `configure` and `make` as you would on any other UNIX-based system.

If running the `configure` script fails because it doesn’t understand the architecture, try replacing the project’s `config.sub` and `config.guess` files with those available in `/usr/share/automake-1.6`. If you are distributing applications that use autoconf, you should include an up-to-date version of `config.sub` and `config.guess` so that OS X users don’t have to do anything extra to build your project.

If that still fails, you may need to run `/usr/bin/autoconf` on your project to rebuild the `configure` script before it works. OS X includes autoconf in the BSD tools package. Beyond these basics, if the project does not build, you may need to modify your makefile using some of the tips provided in the following sections. After you do that, more extensive refactoring may be required.

Some programs may use autoconf macros that are not supported by the version of autoconf that shipped with OS X. Because autoconf changes periodically, you may actually need to get a new version of autoconf if you need to build the very latest sources for some projects. In general, most projects include a prebuilt `configure` script with releases, so this is usually not necessary unless you are building an open source project using sources obtained from CVS or from a daily source snapshot.

However, if you find it necessary to upgrade autoconf, you can get a current version from [http://www.gnu.org/software/autoconf/](http://www.gnu.org/software/autoconf/). Note that autoconf, by default, installs in `/usr/local/`, so you may need to modify your `PATH` environment variable to use the newly updated version. Do _not_ attempt to replace the version installed in `/usr/`.

For additional information about using the GNU autotoolset, see [http://autotoolset.sourceforge.net/tutorial.html](http://autotoolset.sourceforge.net/tutorial.html) and the manual pages `autoconf`, `automake`, and `autoheader`.

Because the Macintosh platform includes more than one processor family, it is often important to compile software for multiple processor architectures. For example, libraries should generally be compiled as universal binaries even if you are exclusively targeting an Intel-based Macintosh computer, as your library may be used by a PowerPC binary running under Rosetta. For executables, if you plan to distribute compiled versions, you should generally create universal binaries for convenience.

When compiling programs for architectures other than your default host architecture, such as compiling for a ppc64 or Intel-based Macintosh target on a PowerPC-based build host, there are a few common problems that you may run into. Most of these problems result from one of the following mistakes:

- Assuming that the build host is architecturally similar to the target architecture and will thus be capable of executing intermediate build products
- Trying to determine target-processor-specific information at configuration time (by compiling and executing small code snippets) rather than at compile time (using macro tests) or execution time (for example, by using conditional byte swap functions)

Whenever cross-compiling occurs, extra care must be taken to ensure that the target architecture is detected correctly. This is particularly an issue when generating a binary containing object code for more than one architecture.

In many cases, binaries containing object code for more than one architecture can be generated simply by running the normal configuration script, then overriding the architecture flags at compile time.

For example, you might run

```
./configure
```

followed by

```
make CFLAGS="-isysroot /Developer/SDKs/MacOSX10.4u.sdk -arch ppc \
    -arch i386" LDFLAGS="-syslibroot /Developer/SDKs/MacOSX10.4u.sdk \
    -arch ppc -arch i386"
```

to generate a universal binary (for Intel-based and PowerPC-based Macintosh computers). To generate a 4-way universal binary that includes 64-bit versions, you would add `-arch ppc64` and `-arch x86_64` to the `CFLAGS` and `LDFLAGS`.

However, applications that make configuration-time decisions about the size of data structures will generally fail to build correctly in such an environment (since those sizes may need to be different depending on whether the compiler is executing a `ppc` pass, a `ppc64` pass, or an `i386` pass). When this happens, the tool must be configured and compiled for each architecture as separate executables, then glued together manually using `lipo`.

In rare cases, software not written with cross-compilation in mind will make configure-time decisions by executing code on the build host. In these cases, you will have to manually alter either the configuration scripts or the resulting headers to be appropriate for the actual target architecture (rather than the build architecture). In some cases, this can be solved by telling the configure script that you are cross-compiling using the `--host`, `--build`, and `--target` flags. However, this may simply result in defaults for the target platform being inserted, which doesn’t really solve the problem.

The best fix is to replace configure-time detection of endianness, data type sizes, and so on with compile-time or run-time detection. For example, instead of testing the architecture for endianness to obtain consistent byte order in a file, you should do one of the following:

- Use C preprocessor macros like `__BIG_ENDIAN__` and `__LITTLE_ENDIAN__` to test endianness at compile time.
- Use functions like `htonl`, `htons`, `ntohl`, and `ntohs` to guarantee a big-endian representation on any architecture.
- Extract individual bytes by bitwise masking and shifting (for example, `lowbyte=word & 0xff; nextbyte = (word >> 8) & 0xff;` and so on).

Similarly, instead of performing elaborate tests to determine whether to use `int` or `long` for a 4-byte piece of data, you should simply use a standard sized type such as `uint32_t`.

There are a few other caveats when working with universal binaries:

- The library archive utility, `ar`, cannot work with libraries containing code for more than one architecture (or single-architecture libraries generated with `lipo`) after ranlib has added a table of contents to them. Thus, if you need to add additional object files to a library, you must keep a separate copy without a TOC.
- The `-M` switch to gcc (to output dependency information) is not supported when multiple architectures are specified on the command line. Depending on your makefile, this may require substantial changes to your makefile rules. For autoconf-based configure scripts, the flag `--disable-dependency-tracking` should solve this problem.

  For projects using automake, it may be necessary to run automake with the `-i` flag to disable dependency checks or put `no-dependencies` in the `AUTOMAKE_OPTIONS` variable in each Makefile.am file.
- If you run into problems building a universal binary for an open source tool, the first thing you should do is to get the latest version of the source code. This does two things:

  - Ensures that the version of autoconf and automake used to generate the configuration scripts is reasonably current, reducing the likelihood of build failures, execution failures, backwards or forwards compatibility problems, and other idiosyncratic or downright broken behavior.
  - Reduces the likelihood of building a version of an open source tool that contains known security holes or other serious bugs.
- Older versions of autoconf do not handle the case where `--target`, `--host`, and `--build` are not handled gracefully. Different versions also behave differently when you specify only one or two of these flags. Thus, you should always specify all three of these options if you are running an autoconf-generated configure script with intent to cross-compile.
- Some earlier versions of autoconf handle cross-compiling poorly. If your tool contains a configure script generated by an early autoconf, you may be able to significantly improve things by replacing some of the `config.*` files (and `config.guess` in particular) with updated copies from the version of autoconf that comes with OS X.

  This will not always work, however, in which case it may be necessary to actually regenerate the configure script by running autoconf. To do this, simply change into the root directory of the project and run `/usr/bin/autoconf`. It will automatically detect and use the `configure.in` file and use it to generate a new configure script. If you get warnings, you should first try a web search for the error message, as someone else may have already run into the problem (possibly on a different tool) and found a solution.

  If you get errors about missing `AC_` macros, you may need to download a copy of libraries on which your tool depends and copy their `.m4` autoconf configuration files into `/usr/share/autoconf`. Alternately, you can add the macros to the file `acinclude.m4` in your project’s main directory and autoconf should automatically pick up those macros.

  You may, in some cases, need to rerun `automake` and/or `autoheader` if your tool uses them. Be prepared to run into missing `AM_` and `AH_` macros if you do, however. Because of the added risk of missing macros, this should generally only be done if running autoconf by itself does not correct a build problem.
- Different makefiles and configure scripts handle command-line overrides in different ways. The most consistent way to force these overrides is to specify them prior to the command. For example:

```
make CFLAGS="-isysroot /Developer/SDKs/MacOSX10.4u.sdk -arch i386 -arch ppc"
```

  should generally result in the above being added to `CFLAGS` during compilation. However, this behavior is not completely consistent across makefiles from different projects.

For additional information about autoconf, automake, and autoheader, you can view the autoconf documentation at [http://www.gnu.org/software/autoconf/manual/index.html](http://www.gnu.org/software/autoconf/manual/index.html).

For additional information on compiler flags for Intel-based Macintosh computers, modifying code to support little-endian CPUs, and other porting concerns, you should read _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_, available from the ADC Reference Library.

Probably the most difficult situation you may experience is that of a self-bootstrapping tool—a tool that uses a (possibly stripped-down) copy of itself to either compile the final version of itself or to construct support files or libraries. Some examples include TeX, Perl, and gcc.

Ideally, you should be able to build the executable as a universal binary in a single build pass. If that is possible, everything “just works”, since the universal binary can execute on the host. However, this is not always possible. If you have to cross-compile and glue the pieces together with `lipo`, this obviously will not work.

If the build system is written well, the tool will bootstrap itself by building a version compiled for the host, then use that to build the pieces for the target, and finally compile a version of the binary for the target. In that case, you should not have to do anything special for the build to succeed.

In some cases, however, it is not possible to simultaneously compile for multiple architectures and the build system wasn’t designed for cross-compiling. In those cases, the recommended solution is to pre-install a version of the tool for the host architecture, then modify the build scripts to rename the target’s intermediate copy of the tool and copy the host’s copy in place of that intermediate build product (for example, `mv miniperl miniperl-target; cp /usr/bin/perl miniperl`).

By doing this, later parts of the build script will execute the version of the tool built for the host architecture. Assuming there are no architecture dependencies in the dependent tools or support files, they should build correctly using the host’s copy of the tool. Once the dependent build is complete, you should swap back in the original target copy in the final build phase. The trick is in figuring out when to have each copy in place.

You will sometimes find it necessary to use conditional compilation to make your code behave differently depending on whether certain functionality is available.

Older code sometimes used conditional statements like `#ifdef __MACH__` or `#ifdef __APPLE__` to try to determine whether it was being compiled on OS X or not. While this seems appealing as a quick way of getting ported, it ultimately causes more work in the long run. For example, if you make the assumption that a particular function does not exist in OS X and conditionally replace it with your own version that implements the same functionality as a wrapper around a different API, your application may no longer compile or may be less efficient if Apple adds that function in a later version.

Apart from displaying or using the name of the OS for some reason (which you can more portably obtain from the [uname](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/uname.3.html#//apple_ref/doc/man/3/uname) API), code should never behave differently on OS X merely because it is running on OS X. Code should behave differently because OS X behaves differently in some way—offering an additional feature, not offering functionality specific to another operating system, and so on. Thus, for maximum portability and maintainability, you should focus on that difference and make the conditional compilation dependent upon detecting the _difference_ rather than dependent upon the OS itself. This not only makes it easier to maintain your code as OS X evolves, but also makes it easier to port your code to other platforms that may support different but overlapping feature sets.

The most common reasons you might want to use such conditional statements are attempts to detect differences in:

- processor architecture
- byte order
- file system case sensitivity
- other file system properties
- compiler, linker, or toolchain differences
- availability of application frameworks
- availability of header files
- support for a function or feature

Instead it is better to figure out _why_ your code needs to behave differently in OS X, then use conditional compilation techniques that are appropriate for the _actual_ root cause.

The misuse of these conditionals often causes problems. For example, if you assume that certain frameworks are present if those macros are defined, you might get compile failures when building a 64-bit executable. If you instead test for the availability of the framework, you might be able to fall back on an alternative mechanism such as X11, or you might skip building the graphical portions of the application entirely.

For example, OS X provides preprocessor macros to determine the CPU architecture and byte order. These include:

- `__i386__`—Intel (32-bit)
- `__x86_64__`—Intel (64-bit)
- `__ppc__`—PowerPC (32-bit)
- `__ppc64__`—PowerPC (64-bit)
- `__BIG_ENDIAN__`—Big endian CPU
- `__LITTLE_ENDIAN__`—Little endian CPU
- `__LP64__`—The LP64 (64-bit) data model

In addition, using tools like `autoconf`, you can create arbitrary conditional compilation on nearly any practical feature of the installation, from testing to see if a file exists to seeing if you can successfully compile a piece of code.

For example, if a portion of your project requires a particular application framework, you can compile a small test program whose `main` function calls a function in that framework. If the test program compiles and links successfully, the application framework is present for the specified CPU architecture.

You can even use this technique to determine whether to include workarounds for known bugs in Apple or third-party libraries and frameworks, either by testing the versions of those frameworks or by providing a test case that reproduces the bug and checking the results.

For example, in OS X, [poll](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/poll.2.html#//apple_ref/doc/man/2/poll) does not support device files such as `/dev/tty`. If you just avoid `poll` if your code is running on OS X, you are making two assumptions that you should not make:

- You are assuming that what you are doing will always be unsupported. OS X is an evolving operating system that adds new features on a regular basis, so this is not necessarily a valid assumption.
- You are assuming that OS X is the only platform that does not support using `poll` on device files. While this is probably true for most device files, not all device files support `poll` in all operating systems, so this is also not necessarily a valid assumption.

A better solution is to use a configuration-time test that tries to use `poll` on a device file, and if the call fails, disables the use of `poll`. If using `poll` provides some significant advantage, it may be better to perform a runtime test early in your application execution, then use `poll` only if that test succeeds. By testing for support at runtime, your application can use the `poll` API if is supported by a particular version of any operating system, falling back gracefully if it is not supported.

A good rule is to always test for the most specific thing that is guaranteed to meet your requirements. If you need a framework, test for the framework. If you need a library, test for the library. If you need a particular compiler version, test the compiler version. And so on. By doing this, you increase your chances that your application will continue to work correctly without modification in the future.

OS X ships two compilers and their corresponding toolchains. The default compiler is based on GCC 4.2. In addition, a compiler based on GCC 4.0 is provided. Older versions of Xcode also provide prior versions. Compiling for 64-bit PowerPC and Intel-based Macintosh computers is only supported in version 4.0 and later. Compiling 64-bit kernel extensions is only supported in version 4.2 and later.

Always try to compile your software using GCC 4 because future toolchains will be based on GCC version 4 or later. However, because GCC 4 is a relatively new toolchain, you may find bugs that prevent compiling certain programs.

Use of the legacy GCC 2.95.2-based toolchain is strongly discouraged unless you have to maintain compatibility with OS X version 10.1.

If you run into a problem that looks like a compiler bug, try using a different version of GCC. You can run a different version by setting the `CC` environment variable in your Makefile. For example, `CC=gcc-4.0` chooses GCC 4.0. In Xcode, you can change the compiler setting on a per-project basis or a per-file basis by selecting a different compiler version in the appropriate build settings inspector.

When building your projects in OS X, simply supplying or modifying the compiler flags of a few key options is all you need to do to port most programs. These are usually specified by either the `CFLAGS` or `LDFLAGS` variable in your makefile, depending on which part of the compiler chain interprets the flags. Unless otherwise specified, you should add these flags to `CFLAGS` if needed.

Some common flags include:

**`-flat_namespace` (in `LDFLAGS`)**
: Changes from a two-level to a single-level (flat) namespace. By default, OS X builds libraries and applications with a two-level namespace where references to dynamic libraries are resolved to a definition in a specific dynamic library when the image is built. Use of this flag is generally discouraged, but in some cases, is unavoidable. For more information, see [Understanding Two-Level Namespaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvbegskijjbeerq).

**`-bundle` (in `LDFLAGS`)**
: Produces a Mach-O bundle format file, which is used for creating loadable plug-ins. See the `ld` man page for more discussion of this flag.

**`-bundle_loader` _executable_ (in `LDFLAGS`)**
: Specifies which executable will load a plug-in. Undefined symbols in that bundle are checked against the specified executable as if it were another dynamic library, thus ensuring that the bundle will actually be loadable without missing symbols.

**`-framework` _framework_ (in `LDFLAGS`)**
: Links the executable being built against the listed framework. For example, you might add -framework vecLib to include support for vector math.

**`-mmacosx-version-min` _version_**
: Specifies the version of OS X you are targeting. You must target your compile for the _oldest_ version of OS X on which you want to run the executable. In addition, you should install and use the cross-development SDK for that version of OS X. For more information, see _[SDK Compatibility Guide](../../Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_.

__Note:__ OS X also uses this value to determine the UNIX conformance behavior of some APIs. For more information, read _[Unix 03 Conformance Release Notes](../../../releasenotes/Darwin/Unix%2003%20Conformance%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzs)_.

More extensive discussion for the compiler in general can be found at [http://developer.apple.com/releasenotes/DeveloperTools/](https://developer.apple.com/releasenotes/DeveloperTools/).

By default, OS X builds libraries and applications with a two-level namespace. In a two-level namespace environment, when you compile a new dynamic library, any references that the library might make to other dynamic libraries are resolved to a definition in those _specific_ dynamic libraries.

The two-level namespace design has many advantages for Carbon applications. However, it can cause problems for many traditional UNIX applications if they were designed to work in a flat namespace environment.

For example, suppose one library, call it `libfoo`, uses another library, `libbar`, for its implementation of the function `barIt`. Now suppose an application wants to override the use of `libbar` with a compressed version, called `libzbar`. Since `libfoo` was linked against `libbar` at compile time, this is not possible without recompiling `libfoo`.

To allow the application to override references made by `libfoo` to `libbar`, you would use the flag `-flat_namespace`. The `ld` man page has a more detailed discussion of this flag.

If you are writing libraries from scratch, it may be worth considering the two-level namespace issue in your design. If you expect that someone may want to override your library’s use of another library, you might have an initializer routine that takes pointers to the second library as its arguments, and then use those pointers for the calls instead of calling the second library directly.

Alternately, you might use a plug-in architecture in which the calls to the outside library are made from a plug-in that could be easily replaced with a different plug-in for a different outside library. See [Dynamic Libraries and Plug-ins](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvkfawcsivddcmbt) for more information.

For the most part, however, unless you are designing a library from scratch, it is not practical to avoid using `-flat_namespace` if you need to override a library’s references to another library.

If you are compiling an executable (as opposed to a library), you can also use `-force_flat_namespace` to tell `dyld` to use a flat namespace when loading any dynamic libraries and bundles loaded by the binary. This is usually not necessary, however.

The only executable format that the OS X kernel understands is the Mach-O format. Some bridging tools are provided for classic Macintosh executable formats, but Mach-O is the native format. It is very different from the commonly used Executable and Linking Format (ELF). For more information on Mach-O, see _OS X ABI Mach-O File Format Reference_.

Dynamic libraries and plug-ins behave differently in OS X than in other operating systems. This section explains some of those differences.

When linking an executable, OS X treats dynamic libraries just like libraries in any other UNIX-based or UNIX-like operating system. If you have a library called `libmytool.a`, `libmytool.dylib`, or `libmytool.so`, for example, all you have to do is this:

```
ld a.o b.o c.o ... -L/path/to/lib -lmytool
```

As a general rule, you should avoid creating static libraries (`.a`) except as a temporary side product of building an application. You _must_ run `ranlib` on any archive file before you attempt to link against it.

OS X makes heavy use of dynamically linked code. Unlike other binary formats such as ELF and xcoff, Mach-O treats plug-ins differently than it treats shared libraries.

The preferred mechanism for dynamic loading of shared code, beginning in OS X v10.4 and later, is the [dlopen](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/dlopen.3.html#//apple_ref/doc/man/3/dlopen) family of functions. These are described in the man page for [dlopen](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/dlopen.3.html#//apple_ref/doc/man/3/dlopen). The `ld` and `dyld` man pages give more specific details of the dynamic linker’s implementation.

Libraries that you are familiar with from other UNIX-based systems might not be in the same location in OS X. This is because OS X has a single dynamically loadable framework, `libSystem`, that contains much of the core system functionality. This single module provides the standard C runtime environment, input/output routines, math libraries, and most of the normal functionality required by command-line applications and network services.

The `libSystem` library also includes functions that you would normally expect to find in libc and libm, RPC services, and a name resolver. Because `libSystem` is automatically linked into your application, you do not need to explicitly add it to the compiler’s link line. For your convenience, many of these libraries exist as symbolic links to `libSystem`, so while explicitly linking against `-lm` (for example) is not needed, it will not cause an error.

To learn more about how to use dynamic libraries, see _[Dynamic Library Programming Topics](../../Developer%20Tools/Dynamic%20Library%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnrz)_.

For the most part, you can treat dynamic libraries and plugins the same way as on any other platform if you use GNU libtool. This tool is installed in OS X as `glibtool` to avoid a name conflict with NeXT libtool. For more information, see the manual page for `glibtool`.

You can also create dynamic libraries and plugins manually if desired. As mentioned in [Using Dynamic Libraries Programmatically](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvjvomi), dynamic libraries and plugins are not the same thing in OS X. Thus, you must pass different flags when you create them.

To create dynamic libraries in OS X, pass the `-dynamiclib` flag.

To create plugins, pass the `-bundle` flag.

Because plugins can be tailored to a particular application, the OS X compiler provides the ability to check these plugins for loadability at compile time. To take advantage of this feature, use the `-bundle_loader` flag. For example:

```
gcc -bundle a.o b.o c.o -o mybundle.bundle \
    -bundle_loader /Applications/MyApp.app/Contents/MacOS/MyApp
```

If the compiler finds symbol requests in the plugin that cannot be resolved in the application, you will get a link error. This means that you `must` use the `-l` flag to link against any libraries that the plugin requires as though you were building a complete executable.

To learn more about how to create and use dynamic libraries, see _[Dynamic Library Programming Topics](../../Developer%20Tools/Dynamic%20Library%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnrz)_.

In the OS X file system, some directories store executable code and the software resources related to that code in one discrete package. These packages, known as bundles, come in two varieties: application bundles and frameworks.

There are two basic types of bundles that you should be familiar with during the basic porting process: application bundles and frameworks. In particular, you should be aware of how to use frameworks, since you may need to link against the contents of a framework when porting your application.

Application bundles are special directories that appear in the Finder as a single entity. Having only one item allows a user to double-click it to get the application with all of its supporting resources. If you are building Mac apps, you should make application bundles. Xcode builds them by default if you select one of the application project types. More information on application bundles is available in [Bundles vs. Installers](Distributing%20Your%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjvfvbecqshivbumry) and in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

A framework is a type of bundle that packages a shared library with the resources that the library requires. Depending on the library, this bundle could include header files, images, and reference documentation. If you are trying to maintain cross-platform compatibility, you may not want to create your own frameworks, but you should be aware of them because you might need to link against them. For example, you might want to link against the Core Foundation framework. Since a framework is just one form of a bundle, you can do this by linking against `/System/Library/Frameworks/CoreFoundation.framework` with the `-framework` flag. A more thorough discussion of frameworks is in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

You can find additional information about bundles in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

A multiply defined symbol error occurs if there are multiple definitions for any symbol in the object files that you are linking together. You can specify the following flags to modify the handling of multiply defined symbols under certain circumstances:

**`-multiply_defined treatment`**
: Specifies how multiply defined symbols in dynamic libraries should be treated when `-twolevel_namespace` is in effect. The values for treatment must be one of:

- `error`—Treat multiply defined symbols as an error.
- `warning`—Treat multiply defined symbols as a warning.
- `suppress`—Ignore multiply defined symbols.

The default behavior is to treat multiply defined symbols in dynamic libraries as warnings when `-twolevel_namespace` is in effect.

**`-multiply_defined_unused treatment`**
: Specifies how unused multiply defined symbols in dynamic libraries should be treated when `-twolevel_namespace` is in effect. An unused multiply defined symbol is a symbol defined in the output that is also defined in one of the dynamic libraries, but in which but the symbol in the dynamic library is not used by any reference in the output. The values for treatment must be `error`, `warning`, or `suppress`. The default for unused multiply defined symbols is to suppress these messages.

The following macros are predefined in OS X:

**`__OBJC__`**
: This macro is defined when your code is being compiled by the Objective-C compiler. By default, this occurs when compiling a `.m` file or any header included by a `.m` file. You can force the Objective-C compiler to be used for a `.c` or `.h` file by passing the `-ObjC` or `-ObjC++` flags.

**`__cplusplus`**
: This macro is defined when your code is being compiled by the C++ compiler (either explicitly or by passing the `-ObjC++` flag).

**`__ASSEMBLER__`**
: This macro is defined when compiling `.s` files.

**`__NATURAL_ALIGNMENT__`**
: This macro is defined on systems that use natural alignment. When using natural alignment, an `int` is aligned on `sizeof(int)` boundary, a short int is aligned on `sizeof(short)` boundary, and so on. It is defined by default when you're compiling code for PowerPC architecutres. It is not defined when you use the `-malign-mac68k` compiler switch, nor is it defined on Intel architectures.

**`__MACH__`**
: This macro is defined if Mach system calls are supported.

**`__APPLE__`**
: This macro is defined in any Apple computer.

**`__APPLE_CC__`**
: This macro is set to an integer that represents the version number of
the compiler. This lets you distinguish, for example, between compilers
based on the same version of GCC, but with different bug fixes or
features. Larger values denote later compilers.

**`__BIG_ENDIAN__` and `__LITTLE_ENDIAN__`**
: These macros tell whether the current architecture uses little endian or big endian byte ordering. For more information, see [Compiling for Multiple CPU Architectures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnjqfvbecssdizcueqi).

This section describes alternatives to certain commonly used APIs.

The following headers commonly found in UNIX, BSD, or Linux operating systems are either unavailable or are unsupported in OS X:

**`alloc.h`**
: This file does not exist in OS X, but the functionality does exist. You should include `stdlib.h` instead. Alternatively, you can define the prototypes yourself as follows:

```
#ifndef _ALLOCA_H

#undef  __alloca

/* Now define the internal interfaces.  */
extern void *__alloca (size_t __size);

#ifdef  __GNUC__
# define __alloca(size) __builtin_alloca (size)
#endif /* GCC.  */

#endif
```

**`ftw.h`**
: The `ftw` function traverses through the directory hierarchy and calls a function to get information about each file. However, there isn't a function similar to `ftw` in `fts.h`.

One alternative is to use `fts_open`, `fts_children`, and `fts_close` to implement such a file traversal. To do this, use the `fts_open` function to get a handle to the file hierarchy, use `fts_read` to get information on each file, and use `fts_children` to get a link to a list of structures containing information about files in a directory.

Alternatively, you can use `opendir`, `readdir` and `closedir` with recursion to achieve the same result.

For example, in order to get a description of each file located in `/usr/include` using `fts.h`, then the code would be as follows:

```swift
/* assume that the path "/usr/include" has been passed through argv[3]*/

fileStruct = fts_open(&argv[3], FTS_COMFOLLOW, 0);
dirList = fts_children(fileStruct, FTS_NAMEONLY);

do
{
 fileInfo = fts_read(dirList->fts_pointer);

 /* at this point, you would be able to extract information from the
 FTSENT returned by fts_read */

 fileStruct = fts_open(dirList->fts_link->fts_name,
FTS_PHYSICAL, (void *)result);

}while (dirList->fts_link != NULL);

ftsResult = fts_close(fileStruct);
```

See the manual page for [fts](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/fts.3.html#//apple_ref/doc/man/3/fts) to understand the structures and macros used in the code. The sample code above shows a very simplistic file traversal. For instance, it does not consider possible subdirectories existing in the directory being searched.

**`getopt.h`**
: Not suported, use `unistd.h` instead.

**`lcrypt.h`**
: Not supported, use `unistd.h` instead.

**`malloc.h`**
: Not supported, use `stdlib.h` instead.

**`mm.h`**
: This header is supported in Linux for memory mapping, but is not supported in Max OS X. In OS X, you can use [mmap](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mmap.2.html#//apple_ref/doc/man/2/mmap) to map files into memory. If you wish to map devices, use the I/O Kit framework instead.

**`module.h`**
: Kernel modules should be loaded using the KextManager API in the I/O Kit framework. For more information, see [KextManagerLoadKextWithURL](https://developer.apple.com/documentation/iokit/1562906-kextmanagerloadkextwithurl) and related functions. The modules themselves must be compiled against the Kernel framework. For more information, see _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

**`nl_types.h`**
: Use the [CFBundleCopyLocalizedString](https://developer.apple.com/documentation/corefoundation/1537103-cfbundlecopylocalizedstring) API in Core Foundation for similar localization functionality.

**`ptms.h`**
: Although pseudo-TTYs are supported in OS X, this header is not. The implementation of pseudo-TTYs is very different from Linux. For more information, see the `pty` manual page.

**`stream.h`**
: This header file is not present in OS X. For file streaming, use `iostream.h`.

**`stropts.h`**
: Not supported.

**`swapctl.h`**
: OS X does not support this header file. You can use the header file `swap.h` to implement swap functionality. The `swap.h` header file contains many functions that can be used for swap tuning.

**`termio.h`**
: This header file is obsolete, and has been replaced by `termios.h`, which is part of the POSIX standard. These two header files are very similar. However, the `termios.h` does not include the same header files as `termio.h`. Thus, you should be sure to look directly at the `termios.h` header to make sure it includes everything your application needs.

**`utmp.h`**
: Deprecated, use `utmpx.h` instead.

**`values.h`**
: Not supported, use `limits.h` instead.

**`wchar.h`**
: Although this functionality is available, you should generally use the [CFStringRef](https://developer.apple.com/documentation/corefoundation/cfstringref) API in Core Foundation instead.

The following functions commonly seen in other Unix, Linux, or BSD operating systems are not supported or are discouraged in OS X.

**`btowc, wctob`**
: Although OS X supports the `wchar` API, the preferred way to work with international strings is the [CFStringRef](https://developer.apple.com/documentation/corefoundation/cfstringref) API, which is part of the Core Foundation framework. Some of the APIs available in Core Foundation are [CFStringGetSystemEncoding](https://developer.apple.com/documentation/corefoundation/1541720-cfstringgetsystemencoding), [CFStringCreateCopy](https://developer.apple.com/documentation/corefoundation/1542087-cfstringcreatecopy), [CFStringCreateMutable](https://developer.apple.com/documentation/corefoundation/1542987-cfstringcreatemutable), and so on. See the Core Foundation documentation for a complete list of supported APIs.

**`catopen, catgets, catclose`**
: `nl_types.h` is not supported, thus, these functions are not supported. These functions gives access to localized strings. There is no direct equivalent in OS X. In general, you should use Core Foundation to access localized resources ([CFBundleCopyLocalizedString](https://developer.apple.com/documentation/corefoundation/1537103-cfbundlecopylocalizedstring), for example).

**`crypt`**
: The `crypt` function performs password encryption, based on the NBS Data Encryption Standard (DES). Additional code has been added to deter key search attempts.`crypt`. OS X's version of the function `crypt` behaves very similarly to the Linux version, except that it encrypts a 64-bit constant rather than a 128-bit constant. This function is located in the `unistd.h` header file rather than `lcrypt.h`.

__Note:__ The linker flag `-lcrypt` is not supported in OS X.

**`dysize`**
: This function is not supported in OS X. Its calculation for leap year is based on:

```
(year) %4 == 0 && ((year) %100 != 0 || (year) % 400 == 0)
```

You can either use this code to implement this functionality, or you can use any of the existing APIs in time.h to do something similar.

**`ecvt`, `fcvt`**
: Discouraged in OS X. Use [sprintf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sprintf.3.html#//apple_ref/doc/man/3/sprintf), [snprintf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/snprintf.3.html#//apple_ref/doc/man/3/snprintf), and similar functions instead.

**`fcloseall`**
: This function is an extension to `fclose`. Although OS X supports `fclose`, `fcloseall` is not supported. You can use `fclose` to implement `fcloseall` by storing the file pointers in an array and iterating through the array.

**`getmntent`, `setmntent`, `addmntent`, `endmntent`, `hasmntopt`**
: In general, volumes in OS X are not in `/etc/fstab`. However, to the extent that they are, you can get similar functionality from [getfsent](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getfsent.3.html#//apple_ref/doc/man/3/getfsent) and related functions.

**`poll`**
: This API is partially supported in OS X. It does not support polling devices.

**`sbrk`, `brk`**
: The `brk` and `sbrk` functions are historical curiosities left over from earlier days before the advent of virtual memory management. Although they are present on the system, they are not recommended.

**`shmget`**
: This API is supported but is not recommended. `shmget` has a limited memory blocks allocation. When several applications use `shmget`, this limit may change and cause problems for the other applications. In general, you should either use [mmap](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/mmap.2.html#//apple_ref/doc/man/2/mmap) for mapping files into memory or use the POSIX [shm_open](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/shm_open.2.html#//apple_ref/doc/man/2/shm_open) function and related functions for creating non-file-backed shared memory.

**`swapon`, `swapoff`**
: These functions are not supported in OS X.

The chapter [Designing Scripts for Cross-Platform Deployment](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/PortingScriptstoMacOSX/PortingScriptstoMacOSX.html#//apple_ref/doc/uid/TP40004268-TP40003517) in _[Shell Scripting Primer](../../Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denry)_ describes a number of cross-platform compatibility issues that you may run into with command-line utilities that are commonly scripted.

This section lists several commands that are primarily of interest to people porting compiled applications and drivers, rather than general-purpose scripting.

**`ldd`**
: The `ldd` command is not available in OS X. However, you can use the command `otool -L` to get the same functionality that `ldd` provides. The `otool` command displays specified parts of object files or libraries. The option `-L` displays the name and version numbers of the shared libraries that an object file uses. To see all the existing options, see the manual page for `otool`.

**`lsmod`**
: `lsmod` is not available on OS X, but other commands exist that offer similar functionality. The

**`kextutil`**
: Loads, diagnoses problems with, and generates symbols for kernel extensions.

**`kextstat`**
: Prints statistics about currently loaded drivers and other kernel extensions.

**`kextload`**
: Loads the kernel module for a device driver or other kernel extensions. This command is a basic command intended for use in scripts. For developer purposes, use `kextutil` instead.

**`kmodunload`**
: Unloads the kernel module for a device driver or other kernel extensions. This command is a basic command intended for use in scripts. For developer purposes, use `kextutil` instead.

For more information about loading kernel modules, see _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_.

[Next](Using%20OS%20X%20Native%20Application%20Environments.md)[Previous](Preparing%20to%20Port.md)

