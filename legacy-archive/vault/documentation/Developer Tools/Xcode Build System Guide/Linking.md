---
title: Xcode Build System Guide
apple_id: TP40006904
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeBuildSystem/500-Linking/bs_linking.html
archived_at: '2026-07-15T07:27:33.078726Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Build System Guide](Introduction.md)


[Next](Reducing%20Build%20Times.md)[Previous](Build%20Configurations.md)

# Linking

The Link Binary With Libraries build phase in Xcode projects links frameworks and libraries with object files to produce a binary file. Source files that use code in a framework or a library must include a reference to the appropriate programming interface contained in them.

To learn the basics of linking frameworks and libraries, see [Managing Libraries and Frameworks](../Xcode%20Project%20Management%20Guide/Files%20in%20Projects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnrwfvjvona).

The binary file (or image) a target produces can be of one of these types:

- __Executable.__ Executable files are binaries containing the core logic of a program. Specifically, they contain the program’s entry point, which in C-based programs is the `main` function. Once loaded, however, these programs may require the loading of dynamic libraries to perform functionality they don’t implement. To generate an executable file, a target may include static libraries directly, or dynamic libraries, either directly or through frameworks. Executable binaries don’t have an extension; for example, `MyProgram`).
- __Bundle.__ Bundles are executable files that can be loaded at runtime by other products. Plug-ins are implemented using bundles. The term _bundle_ in this context refers to the binary itself, not to a structured hierarchy. Bundles have the `.bundle` extension; for example, `MyBundle.bundle`.
- __Static Library.__ Static libraries (also known as archives) are repositories of code that other programs incorporate as their own, which produces larger images. The code obtained from the static library is loaded at the same time the product is loaded. These products, however, do not benefit from improvements made in the static library after they are built. To get new functionality, the products must be rebuilt with the improved version of the static library. Static libraries have the `.a` extension; for example, `MyLibrary.a`.
- __Dynamic Library.__ Dynamic libraries contain code that programs load at runtime. The images of products that use dynamic libraries are smaller because they don’t incorporate the library’s code into their own. Instead, these products load the appropriate library at runtime. Using dynamic libraries, products can automatically take advantage of features introduced in versions of the libraries that were not available when the products were built. That is, a program can take advantage of new functionality without being rebuilt. Dynamic libraries have the .dylib extension; for example, `libMyLibrary.1.0.dylib`.

The Mach-O Type (MACH_O_TYPE) build setting allows you to specify the type of binary a target produces. By default, this build setting is set to the appropriate value depending on the target’s type. For example, in a Cocoa static library target, Mach-O Type is Static Library; in a BSD dynamic library target, Mach-O Type is Dynamic Library. However, you can change Mach-O Type for a target when you need a different binary type than the target default. For example, if you want to implement a Cocoa plug-in as a dynamic library instead of a bundle, create a Cocoa-bundle project and change Mach-O Type from Bundle to Dynamic Library.

The order in which frameworks and libraries are listed in the Link Binary With Libraries build phase specifies the order in which external symbols are resolved by the static linker at build time and the dynamic linker at runtime. When either of the linkers encounters an undefined external symbol, they look for the symbol starting with the first framework or library listed in the build phase.

When a program is built, the static linker replaces references to external symbols with the addresses of the symbols in the referenced libraries (this is called _prebinding_), or tells the dynamic linker to resolve the references when a program is loaded or when a symbol is referenced. Having the dynamic linker resolve references to external symbols at runtime provides the most flexibility, because a program can link with new versions of the symbols as they become available. However, this approach is not recommended for all situations, because linking with newer versions of a method or a function may cause problems during a program’s execution.

In addition, how frameworks and libraries are listed in a Link Binary With Libraries build phase tells the static linker the approach (or the semantics) to use when binding or resolving references to external symbols defined in libraries.

Placing static libraries after dynamic libraries in the Link Binary With Libraries build phase ensures that the static linker binds references to external symbols defined in static libraries at build time, even when newer versions of the static libraries the application originally was linked with are present in the user’s system.

When static libraries are listed before a dynamic library in the Link Binary With Libraries build phase, the static linker doesn’t resolve references to symbols in those static libraries. Instead, those symbols are resolved by the dynamic linker at runtime. This may cause problems when the static libraries are updated, because the application links to the new, potentially incompatible versions of the symbols instead of the ones the developer intended.

For details on how symbols are resolved, see “Finding Imported Symbols” in [Executing Mach-O Files](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MachOTopics/1-Articles/executing_files.html#//apple_ref/doc/uid/TP40001829) in _Mac OS X ABI Mach-O File Format Reference_ and the `ld` man page.

Mac OS X includes a prebinding mechanism used to speed up application launch in programs that link against dynamic libraries. When a user installs an application or upgrades the operating system, a prebinding agent links the application against new versions of the dynamic libraries. Sometimes, however, you may want to prevent this behavior for specific applications.

To link the binary file, framework, library, or plug-in so that prebinding is never performed on it, you need to add the `-nofixprebinding` option to the linker invocation. To do this, add `-nofixprebinding` to the Other Linker Flags (OTHER_LDFLAGS) build setting. See the `ld` man page for more information.

By default, Xcode builds binary files that export all their symbols. To reduce the number of symbols you want to export from a binary file, create an export file and set the Exported Symbols File (EXPORTED_SYMBOLS_FILE) build setting to the name of the file. For more information, see [Improving Locality of Reference](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/ImprovingLocality.html#//apple_ref/doc/uid/20001862).

To help reduce your application’s paging activity at runtime, you may specify an order file to the linker. You do this by setting the Symbol Ordering Flags (SECTORDER_FLAGS) build setting to `-sectorder __TEXT __text <order_file>`. For information on order files, see [Improving Locality of Reference](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/ImprovingLocality.html#//apple_ref/doc/uid/20001862) in _[Code Size Performance Guidelines](../../Performance/Code%20Size%20Performance%20Guidelines/Introduction%20to%20Code%20Size%20Performance%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2ds2i)_.

The static linker (`ld`) supports the removal of unused code and data blocks from executable files. This process (known as _dead-code stripping_) helps reduce the overall size of executables, which in turn improves performance by reducing the memory footprint of the executable. It also allows programs to link successfully when unused code refers to an undefined symbol (instead of resulting in a link error).

Dead-code stripping is not limited to removing only unused functions and executable code from a binary. The linker also removes any unused symbols and data that reside in data blocks. Such symbols might include global variables, static variables, and string data, among others.

When dead-code stripping is enabled, the static linker searches for code that is unreachable from an initial set of live symbols and blocks. The initial list of live symbols and blocks may include the following:

- Symbols listed in an exports file; alternatively, it would include the symbols absent from a list of items marked as _not_ to be exported. For dynamic libraries or bundles without an exports file, all global symbols are part of the initial live list. See [Preventing the Stripping of Unused Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojufvbegskijbauiqq) for more information.
- The block representing the default entry point or the symbol listed after the `-e` linker option, either of which identifies the specific entry point for an executable. See the `ld` man page for more information on the `-e` option.
- The symbol listed after the `-init` linker option, which identifies the initialization routine for a shared library. See the `ld` man page for more information.
- Symbols whose declaration includes the `used` attribute. See [Preventing the Stripping of Unused Symbols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojufvbegskijbauiqq) for more information.
- Objective-C runtime data.
- Symbols marked as being referenced dynamically (via the REFERENCED_DYNAMICALLY bit in `/usr/include/mach-o/nlist.h`).

To turn on dead-code stripping in your project, you must pass the appropriate command-line options to the linker. From Xcode, you add these options in the Build pane of the target or project inspector; otherwise, you must add these options to your makefile or build scripts. Table 5-1 lists the Xcode build settings that control dead-code stripping. Turning on either of these build settings causes Xcode to build with the corresponding linker option.

__Table 5-1__  Xcode build settings for dead-code stripping

| Build setting | Linker option |
| Dead Code Stripping (DEAD_CODE_STRIPPING) | `-dead_strip` |
| Don’t Dead-Strip Inits and Terms (PRESERVE_DEAD_CODE_INITS_AND_TERMS) | `-no_dead_strip_inits_and_terms` |

Table 5-2 lists the basic dead-code stripping options.

__Table 5-2__  Linker options for dead-code stripping

| Linker option | Description |
| `-dead_strip` | Enables basic dead-code stripping by the linker. |
| `-no_dead_strip_inits_and_terms` | Prevents all constructors and destructors from being stripped when the `-dead_strip` option is in effect, even if they are not live. |

After turning on dead-code stripping, you may want to set the _strip style_ used. The strip style specifies the level of stripping performed. There are three levels of stripping available:

- All Symbols. All symbols are stripped from the binary, which includes the symbol table and relocation information.
- Non-Global Symbols. Nonglobal symbols are removed. External symbols remain.
- Debugging Symbols: Debugging symbols are removed. Local and global symbols remain.

Use the Strip Style (STRIP_STYLE) build setting to specify the desired strip level.

You must recompile all object files using the compiler included with Xcode 1.5 or later before dead-code stripping can be performed by the linker. You must also compile the object files with the `-gfull` option to ensure that the resulting binaries can be properly debugged. In Xcode, change the value of the Level of Debug Symbols (GCC_DEBUGGING_SYMBOLS) build setting to All Symbols (`-gfull`).

If you want to know what symbols were stripped by the static linker, you can find out by examining the linker-generated load map. This map lists all of the segments and sections in the linked executable and also lists the dead-stripped symbols. To have the linker generate a load map, add the `-M` option to your linker command-line options. In Xcode, you can add this option to the Other Linker Flags build setting.

If your executable contains symbols that you know should not be stripped, you need to notify the linker that the symbol is actually used. You must prevent the stripping of symbols when external code (such as plug-ins) use's those symbols but local code does not.

There are two ways to tell the linker not to strip a symbol. You can include it in an exports file or mark the symbol declaration explicitly. To mark the declaration of a symbol, you include the `used` attribute as part of its definition. For example, you would mark a function as used by declaring it as follows:

```
void MyFunction(int param1) __attribute__((used));
```

Alternatively, you can provide an exports list for your executable that lists any symbols you expect to be used by plug-ins or other external code modules. To specify an exports file from Xcode, use the Exported Symbols File (EXPORTED_SYMBOLS_FILE) build setting; enter the path, relative to the project directory, to the exports file. To specify an exports file from the linker command line, use the `-exported_symbols_list` option. (You can also specify a list of symbols _not_ to export using the `-unexported_symbols_list` option.)

If you are using an exports list and building either a shared library, or an executable that will be used with `ld`'s `-bundle_loader` flag, you need to include the symbols for exception frame information in the exports list for your exported C++ symbols. Otherwise, they may be stripped. These symbols end with `.eh`; you can view them with the `nm` tool.

If you are writing assembly language code, the assembler now recognizes some additional directives to preserve or enhance the dead-stripping of code and data. You can use these directives to flag individual symbols, or entire sections of assembly code.

To prevent the stripping of an individual symbol, use the `.no_dead_strip` directive. For example, the following code prevents the specified string from being stripped:

```
.no_dead_strip _my_version_string
.cstring
_my_version_string:
.ascii "Version 1.1"
```


To prevent an entire section from being stripped, add the `no_dead_strip` attribute to the section declaration. The following example demonstrates the use of this attribute:

```
.section __OBJC, __image_info, regular, no_dead_strip
```

You can also add the `live_support` attribute to a section to prevent it from being stripped if it references other code that is live. This attribute prevents the stripping of some code that might actually be needed but not referenced in a detectable way. For example, the compiler adds this attribute to C++ exception frame information. In your code, you might use the attribute as follows:

```
.section __TEXT, __eh_frame, coalesced, no_toc+strip_static_syms+live_support
```


The `.subsections_via_symbols` directive notifies the assembler that the contents of sections may be safely divided into individual blocks prior to dead-code stripping. This directive makes it possible for individual symbols to be stripped out of a given section if they are not used. This directive applies to all section declarations in your assembly file and should be placed outside of any section declarations, as shown below:

```
.subsections_via_symbols

; Section declarations...
```

If you use this directive, make sure that each symbol in the section marks the beginning of a separate block of code. Implicit dependencies between blocks of code might result in the removal of needed code from the executable. For example, the following section contains three individual symbols, but execution of the code at `_plus_three` ends at the `blr` statement at the bottom of the code block.

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

If you were to use the `.subsections_via_symbols` directive on this code, the assembler would permit the stripping of the symbols `_plus_two` and `_plus_one` if they were not called by any other code. If this occurred, `_plus_three` would no longer return the correct value because part of its code would be missing. In addition, if `_plus_one` were stripped, the code might crash when it continued executing into the next block.

[Next](Reducing%20Build%20Times.md)[Previous](Build%20Configurations.md)

