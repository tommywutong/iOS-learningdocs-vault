---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/bs_linking/bs_linking.html
archived_at: '2026-07-15T07:29:03.187214Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Optimizing%20the%20Edit-Build-Debug%20Cycle.md)[Previous](Building%20a%20Product.md)

# Linking

The Link Binary With Libraries build phase
in Xcode projects links frameworks and libraries with object files
to produce a binary file. Source files that use code in a framework or
a library must include a reference to the appropriate programming
interface contained in them.

Libraries and frameworks are linked to object files when building
an executable file. However, this process is slow and can detract
from the development experience. Xcode provides a feature, called
ZeroLink, that eliminates the link step while you work on a project;
see [Using ZeroLink](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgmwugsceincuqrce) for details.

The order in which frameworks and libraries are listed in
the Link Binary With Libraries build phase specifies the order in
which external symbols are resolved by the static linker at build
time and the dynamic linker at runtime. When either of the linkers
encounters an undefined external symbol, they look for the symbol
starting with the first framework or library listed in the build
phase.

When a program is built, the static linker replaces references
to external symbols with the addresses of the symbols in the referenced
libraries (this is called _prebinding_), or tells the dynamic
linker to resolve the references when a program is loaded or when
a symbol is referenced. Having the dynamic linker resolve references
to external symbols at runtime provides the most flexibility, as
a program can link with new versions of the symbols as they become
available. However, this approach is not recommended for all situations,
as linking with newer versions of a method or a function may cause
problems during a program’s execution.

In addition, how frameworks and libraries are listed in a Link
Binary With Libraries build phase, tells the static linker the approach
(or the semantics) to use when binding or resolving references to
external symbols defined in libraries.

Placing static libraries after dynamic libraries in the Link
Binary With Libraries build phase, ensures that the static linker
binds references to external symbols defined in static libraries
at build time, even when newer versions of the static libraries
the application originally was linked with are present in the user’s
system.

When static libraries are listed before a dynamic library
in the Link Binary With Libraries build phase, the static linker
doesn’t resolve references to symbols in those static libraries. Instead,
those symbols are resolved by the dynamic linker at runtime. This
may cause problems when the static libraries are updated, as the
application links to the new, potentially incompatible versions
of the symbols instead of the ones the developer intended.

For details on how symbols are resolved, see “Finding Imported
Symbols” in Executing Mach-O Files in _Mach-O Runtime Architecture_ and the `ld` man
page.

Mac OS X includes a prebinding mechanism used to speed-up
application launch in programs that link against dynamic libraries.
When a user installs an application or upgrades the operating system,
a prebinding agent links the application against new versions of
the dynamic libraries. Sometimes, however, you may want to prevent
this behavior for specific applications.

To link the binary file, framework, library, or plug-in, so
that prebinding is never done on it, you need to add the `-nofixprebinding` option
to the linker invocation. To do this, add `-nofixprebinding` to
the Other Linker Flags (OTHER_LDFLAGS) build setting. See the `ld` man page
for more information.

When linking with system frameworks (located in `/System/Library/Frameworks`),
include only the umbrella header files in your source files and
link only with the appropriate umbrella framework for your application.
For example, in a Carbon application that uses the Address Book
framework, you would include the following line in the header files
of modules that access the Address Book programming interface:

```c
#include <Carbon/Carbon.h>
```

You would also add `AddressBook.framework` to
the list of files in the Frameworks & Libraries build phase.

When you need to link with a custom version of a dynamic library
but don’t want to replace the standard version of the library,
you can use the `-dylib_file` option
of the linker to tell it where to find the nonstandard version of
the library. Just add `-dylib_file` _standard_library_path_`:`_nonstandard_library_path_ to
the Other Linker Flags build setting, where _standard_library_path_ is
the path to the standard library and _nonstandard_library_path_ is
the path to the custom version of the library.

By default, Xcode builds binary files that export all their
symbols. To reduce the number of symbols you want to export from
a binary file, create an export file and set the Exported Symbols
File (EXPORTED_SYMBOLS_FILE) build setting to the name of the file.
For more information, see [Minimizing Your Exported Symbols](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/ReducingExports.html#//apple_ref/doc/uid/20001864) in _[Code Size Performance Guidelines](../../Performance/Code%20Size%20Performance%20Guidelines/Introduction%20to%20Code%20Size%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2ds2i)_.

To help reduce your application’s paging activity at runtime,
you may specify an order file to the linker. You do this by setting
the Symbol Ordering Flags (SECTORDER_FLAGS) build setting to `-sectorder
__TEXT __text <order_file>`. For information
on order files, see [Improving Locality of Reference](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/ImprovingLocality.html#//apple_ref/doc/uid/20001862) in _[Code Size Performance Guidelines](../../Performance/Code%20Size%20Performance%20Guidelines/Introduction%20to%20Code%20Size%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2ds2i)_.

The static linker (`ld`)
supports the removal of unused code and data blocks from executable
files. This process (known as dead-code stripping) helps reduce
the overall size of executables, which in turn improves performance
by reducing the memory footprint of the executable. It also allows
programs to link successfully in the situation where unused code
refers to an undefined symbol, something that would normally result
in a link error.

Dead-code stripping is not limited to removing only unused
functions and executable code from a binary. The linker also removes
any unused symbols and data that reside in data blocks. Such symbols
might include global variables, static variables, and string data among
others.

When dead-code stripping is enabled, the static linker searches
for code that is unreachable from an initial set of live symbols
and blocks. The initial list of live symbols and blocks may include
the following:

- Symbols listed
  in an exports file; alternatively, the symbols absent from a list
  of items marked as _not_ to be exported. For
  dynamic libraries or bundles without an exports file, all global
  symbols are part of the initial live list. See [Preventing the Stripping of Unused Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgmwueq2jjbeecrcc) for
  more information.
- The block representing the default entry point or the symbol
  listed after the `-e` linker option,
  either of which identifies the specific entry point for an executable.
  See the `ld` man page for
  more information on the `-e` option.
- The symbol listed after the `-init` linker
  option, which identifies the initialization routine for a shared
  library. See the `ld` man
  page for more information.
- Symbols whose declaration includes the `used` attribute.
  See [Preventing the Stripping of Unused Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgmwueq2jjbeecrcc) for more information.
- Objective-C runtime data.
- Symbols marked as being referenced dynamically (via the `REFERENCED_DYNAMICALLY` bit
  in `/usr/include/mach-o/nlist.h`).

To enable dead-code stripping in your project, you must pass
the appropriate command-line options to the linker. From Xcode,
you add these options in the Build pane of the target inspector;
otherwise, you must add these options to your makefile or build
scripts. Table 28-2 lists
the Xcode build settings that control dead-code stripping. Enabling
either of these build settings causes Xcode to build with the corresponding
linker option.

__Table 28-1__  Xcode build settings for dead stripping

| Linker option | Build setting |
| `-dead_strip` | Dead Code Stripping (DEAD_CODE_STRIPPING) |
| `-no_dead_strip_inits_and_terms` | Don’t Dead-Strip Inits and Terms (PRESERVE_DEAD_CODE_INITS_AND_TERMS) |

Table 28-1 lists the basic dead-code stripping options.

__Table 28-2__  Linker options for dead stripping

| Linker option | Description |
| `-dead_strip` | Enables basic dead-code stripping by the linker. |
| `-no_dead_strip_inits_and_terms` | Prevents all constructors and destructors from being stripped when the `-dead_strip` option is in effect, even if they are not live. |

You must recompile all object files using the compiler included
with Xcode 1.5 or later before dead-code stripping can be performed
by the linker. You must also compile the object files with the `-gfull` option
to ensure that the resulting binaries can be properly debugged.
In Xcode, change the value of the Level of Debug Symbols (GCC_DEBUGGING_SYMBOLS)
build setting to All Symbols (`-gfull`).

If you want to know what symbols were stripped by the static
linker, you can find out by examining the linker-generated load
map. This map lists all of the segments and sections in the linked
executable and also lists the dead-stripped symbols. To have the
linker generate a load map, add the `-M` option
to your linker command-line options. In Xcode, you can add this
option to the Other Linker Flags build setting.

If your executable contains symbols that you know should not
be stripped, you need to notify the linker that the symbol is actually
used. You must prevent the stripping of symbols in situations where
external code (such as plug-ins) use those symbols but local code
does not.

There are two ways to tell the linker not to dead strip a
symbol. You can include it in an exports file or mark the symbol
declaration explicitly. To mark the declaration of a symbol, you
include the `used` attribute
as part of its definition. For example, you would mark a function
as used by declaring it as follows:

```
void MyFunction(int param1) __attribute__((used));
```

Alternatively, you can provide an exports list for your executable
that lists any symbols you expect to be used by plug-ins or other
external code modules. To specify an exports file from Xcode, use
the Exported Symbols File (EXPORTED_SYMBOLS_FILE) build setting;
enter the path, relative to the project directory, to the exports
file. To specify an exports file from the linker command line use
the `-exported_symbols_list`.
option. (You can also specify a list of symbols _not_ to
export using the `-unexported_symbols_list` option.)

If you are using an exports list and building either a shared
library, or an executable that will be used with `ld`'s `-bundle_loader` flag,
you need to include the symbols for exception frame information
in the exports list for your exported C++ symbols. Otherwise, they
may be stripped. These symbols end with `.eh`;
you can view them with the `nm` tool.

If you are writing assembly language code, the assembler now
recognizes some additional directives to preserve or enhance the
dead-stripping of code and data. You can use these directives to
flag individual symbols or entire sections of assembly code.

To prevent the dead stripping of an individual symbol, use
the `.no_dead_strip` directive.
For example, the following code prevents the specified string from
being dead stripped:

```
.no_dead_strip _my_version_string
.cstring
_my_version_string:
.ascii "Version 1.1"
```


To prevent an entire section from being dead stripped, add
the `no_dead_strip` attribute
to the section declaration. The following example demonstrates the
use of this attribute:

```
.section __OBJC, __image_info, regular, no_dead_strip
```

You can also add the `live_support` attribute
to a section to prevent it from being dead stripped if it references
other code that is live. This attribute prevents the dead stripping
of some code that might actually be needed but not referenced in
a detectable way. For example, the compiler adds this attribute
to C++ exception frame information. In your code, you might use
the attribute as follows:

```
.section __TEXT, __eh_frame, coalesced, no_toc+strip_static_syms+live_support
```


The `.subsections_via_symbols` directive
notifies the assembler that the contents of sections may be safely
divided into individual blocks prior to dead-code stripping. This
directive makes it possible for individual symbols to be stripped
out of a given section if they are not used. This directive applies
to all section declarations in your assembly file and should be
placed outside of any section declarations, as shown below:

```
.subsections_via_symbols

; Section declarations...
```

If you use this directive, make sure that each symbol in the
section marks the beginning of a separate block of code. Implicit
dependencies between blocks of code might result in the removal
of needed code from the executable. For example, the following section contains
three individual symbols, but execution of the code at `_plus_three` ends
at the `blr` statement
at the bottom of the code block.

```
.text
.globl _plus_three
_plus_three:
addi r3, r3, 1
.globl _plus_two
_plus_two:
addi r3, r3, 1
.global _plus_one
_plus_one:
addi r3, r3, 1
blr
```

If you were to use the `.subsections_via_symbols` directive
on this code, the assembler would permit the stripping of the symbols `_plus_two` and `_plus_one` if
they were not called by any other code. If this occurred, `_plus_three` would
no longer return the correct value because part of its code would
be missing. In addition, if `_plus_one` were
dead stripped, the code might crash as it continued executing into
the next block.

ZeroLink speeds application development time by eliminating
the link process from development builds. Instead, Xcode generates
an application stub that contains the full paths to the object files
that make up the application. At runtime, each object (`.o`)
file is linked as it’s needed. This works only when running your
application within Xcode. You cannot deploy applications using ZeroLink.

To turn ZeroLink on or off, use the ZeroLink (ZERO_LINK) build
setting. ZeroLink is enabled by default in the Development build
style. If you build with this build style, you automatically get
ZeroLink functionality. See [Build Styles](Build%20Styles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgawugssbizcesr2g) for more information
on using build styles. ZeroLink works only for native targets.

The following sections explain how you can customize ZeroLink
to further reduce application launch times and identify issues you
must keep in mind when using ZeroLink.

ZeroLink postpones the linking of object files until the last
moment possible. However, there are some symbols that, by default,
are always resolved (that is, the corresponding object files are
linked against the application and the code is executed). These
symbols are static initializers in C++ and `+load` methods
and categories in Objective-C. You can tell ZeroLink not to search
the object files of your application for these symbols to reduce
the application’s launch time.

There are situations that require the initialization of objects
before a program’s `main` function
is called. For example, a class may declare global variables that
can be accessed by other code before the class has a chance to initialize
them. In Objective-C, the `+initialize` method
may be executed too late (see Initializing a Class Object in _[The Objective-C Programming Language](../../Cocoa/The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_. The purpose of static initializers in C++ and `+load` methods
in Objective-C is to provide developers with a mechanism to initialize
variables at the earliest possible point during a program’s launch
process. In Objective-C–based applications, categories are also
loaded before `main` is
called.

When you build an application, the static linker adds the
standard entry-point function to the main executable file. This
function sets up the runtime environment state for the kernel and
the application before calling `main`,
which involves calling static initializers for C++ code and loading
categories and invoking `+load` methods
for Objective-C code.

When using ZeroLink, you can further reduce the launch time
of the application by postponing the execution of static initializers
and `+load` methods, and
the loading of categories. But you must be certain that code in
your application doesn’t rely on static initializers or `+load` methods
being called before `main` or
on categories being loaded before `main` is
called. Otherwise, your application may crash or behave unexpectedly.

There are three linker options you can use to customize ZeroLink
in your project. To use these options, add them to the Other Linker
Flags (OTHER_LDFLAGS) build setting:

- `-no-run-initializers-before-main`:
  If an application contains C++ code, the linker looks for static
  initializers at launch time before calling `main` in
  all the object files that make up the application and, if it finds
  any, links the object files containing them into the application.
  This may slow down application launch. If you’re developing an application
  using C++ and it doesn’t depend on static initializers being run
  before `main`, use this
  option to prevent ZeroLink from scanning object files in search
  of static initializers before calling `main`.

  Keep
  in mind that if there’s code that requires that static initializers
  be run before `main`, your
  application could crash. This specially true for applications that
  use static initializers to register code with a registry. If the
  sole purpose of the static initializers is to perform the registration
  (that is, if no other code would ever trigger the execution of the
  static initializers by accessing a global variable, for example),
  no registration would take place. For example, when reading a serialized
  file, the reader reads the name of the class of each serialized
  object and tells the class to reconstruct an instance from the data. In
  C++ there is no infrastructure to look up a class by name. Instead,
  a common idiom is for each class capable of serializing and deserializing
  instances of itself to register its class name and deserialization
  method address with the reader using a static initializer.
- `-no-load-categories-before-main`:
  If an application contains Objective-C code, the linker looks for
  categories at launch time before calling `main` in
  all the object files that make up the application and, if it finds
  any, links the object files containing them into the application.
  As with `-no-run-initializers-before-main`,
  this may slow application launch. If your application doesn’t
  depend on categories, use this option to prevent ZeroLink from scanning
  object files in search of categories before calling `main`.

  Some
  developers rely on the use of categories in the implementation of
  their class hierarchies. In such a model, the implementation of
  a class spans one or more categories of that class. Using this design
  model, a program may run incorrectly when the categories that implement
  additional class functionality are not loaded. With ZeroLink, classes
  can be loaded when need because there’s a direct reference to
  them, but ZeroLink cannot load categories dynamically. Therefore,
  if your application depends on categories, it may crash or behave
  unexpectedly if you use the `-no-load-categories-before-main` flag.
- `-no-run-load-methods-before-main`:
  Similarly to `-no-load-categories-before-main`,
  ZeroLink scans object files for `+load` methods
  in Objective-C code before `main` is
  invoked to link them to the application. Using this option prevents
  the scanning of object files for `+load` methods
  before ZeroLink calls `main`. `+load` methods
  in Objective-C are similar to static initializers in C++: They are
  executed early during application launch, before main is called,
  to perform tasks that must be performed at the earliest possible
  time. However, the order of execution of `+load` methods
  is not guaranteed. If your code depends on `+load` methods
  to be run before `main`,
  your application may crash or run incorrectly if you use this flag.

When building an application that uses static libraries (`.a` files),
each static library is linked to produce a bundle. At runtime, each
bundle is loaded on demand. If your application starts slowly while
using ZeroLink and has a large number (100 or more) of object files,
you can try adding an intermediate static library target, containing
the relatively stable parts of your source code. This gives you
the best of both worlds: static (build time) linking for stable
code and dynamic (runtime) linking for code that changes frequently.

If you want to view information about the loading and linking
of object files as your application runs, set the `ZERO_LINK_VERBOSE` environment
variable to any value. The information appears in run log of the
application or `stderr`.

These are some things you should keep in mind when using ZeroLink:

- ZeroLink
  doesn’t support the use of private external symbols; that is symbols declared
  as `__private_extern__`.

  Private
  external symbols are visible only to other modules within the same
  Mach-O file as the modules that contain them. If you use a private
  external symbol in your project while ZeroLink is turned on, you
  get an unknown-symbol error when your code tries to access it. For
  example, if you have the definition `__private_extern__
  int my_extern = 800;` in a source file and
  the declaration `extern int my_extern;` in
  another source file, when the second module accesses `my_extern`,
  your application exits with the following log output:

```
ZeroLink: unknown symbol '_my_extern'
MyApplication has exited due to signal 6 (SIGABRT)
```

  For more information
  on private external symbols, see “Scope and Treatment of Symbol
  Definitions” in Executing Mach-O Files in _Mach-O Runtime Architecture_.
- When setting breakpoints on methods, you must use full method
  specifiers, not just selectors. For example, if your project has
  a class named MyClass with an instance method called `myMethod`,
  you must specify a breakpoint on `myMethod` like
  this:

```
-[MyClass myMethod]
```
- If you get an error similar to this one:

```
dyld: /Users/user_name/MyApp/build/MyApp.app/Contents/MacOS/MyApp  Undefined symbols:
Foundation undefined reference to _objc_exception_set_functions  expected to be defined in
/System/Library/PrivateFrameworks/ZeroLink.framework/Versions/A/Resources/libobjc.A.dylib
```

  delete `/System/Library/PrivateFrameworks/ZeroLink.framework/Versions/A/Resources/libobjc.A.dylib`.

  You
  would get this error if you install the Xcode tools in a system
  with a prerelease version of Mac OS X. The `libobjc.A.dylib` file
  contains a developmental copy of the Objective-C runtime. It’s
  not necessary for normal development.

[Next](Optimizing%20the%20Edit-Build-Debug%20Cycle.md)[Previous](Building%20a%20Product.md)

