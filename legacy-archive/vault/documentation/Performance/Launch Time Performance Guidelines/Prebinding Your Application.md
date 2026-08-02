---
title: Launch Time Performance Guidelines
apple_id: 10000148i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/LaunchTime/Articles/Prebinding.html
archived_at: '2026-07-18T01:48:49.124428Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Launch Time Performance Guidelines](Introduction%20to%20Launch%20Time%20Performance%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](Minimizing%20File%20Access%20At%20Launch%20Time.md)

# Prebinding Your Application

Prebinding is the process of computing the addresses for symbols imported by a shared library or application prior to their use. Resolving these addresses before their use reduces the amount of work performed by the dynamic loader (`dyld`) at runtime and results in faster launch times for applications.

In OS X v10.4, `dyld` was improved in a way that eliminated the need for prebinding information in most situations. The system libraries are now the only executables that are still prebound, and they are prebound in a way that optimizes performance on the target system. Because of the improved prebinding of the system libraries, applications and third-party libraries no longer need to be prebound. A side benefit to this new behavior is that applications now have more usable address space than in previous versions of the operating system.

If you are developing applications for versions of OS X prior to v10.4, prebinding is considered optional. Changes in v10.3.4 made application prebinding unnecessary but applications running on earlier versions of the operating system still received some benefits from prebinding. If you feel your application launches slowly on pre-10.3.4 systems, build your application prebound and see if launch time improves.

If you are developing frameworks or other dynamic shared libraries for versions of OS X prior to 10.4, it is still recommended that you specify a base address for your library. Specifying this address allows prebinding to occur for applications that use your library. If your library is running in OS X v10.4 and later, specifying a base address is optional but can be useful for debugging shared libraries. The `atos` command-line tool lets you identify symbols located in memory. It is easier to identify specific symbols if your library has a known base address.

The following sections tell you how to prebind your application and framework projects and how to update that prebinding information if it becomes invalid.

Prior to OS X v10.4, prebinding was enabled for all new projects built using Xcode. In OS X v10.4 and later, this setting is no longer enabled due to changes that make prebinding unnecessary. If you aren’t sure if your project is being built with prebinding enabled, you can check the build settings for your project. Prebinding settings are set on a per-target basis in the Build options view of the Xcode inspector window. If the “Prebinding” option is enabled for your target, it is being built with prebinding information.

If you are not using Xcode, there are several other ways to enable prebinding of your application or framework. During the link phase, the `ld` tool looks to see if the `LD_PREBIND` environment variable is set. If it is, the tool enables prebinding unless a command-line option specifically disables it. If you are calling `ld` from the command-line, you can pass it the `-prebind` option to enable prebinding explicitly.

If you are developing a framework for versions of OS X prior to 10.4, you should always build and ship it with prebinding enabled. If your framework is not prebound, applications that reference your framework cannot be prebound either, which can impact their launch time. In addition to enabling prebinding, you need to specify a preferred memory address for your framework. You do this by passing the `-seg1addr` option to `ld`. In Xcode, you add this option to the "Other Linker Flags" build setting. From the command line, simply include this option along with the other linker options in your makefile. For more information about using this option, see the `ld` man page.

If you build with prebinding enabled, there are still times when `ld` may be unable to prebind your application. Prebinding fails if there are any symbol-name conflicts in the linked libraries or if the preferred address spaces for any libraries overlap. Prebinding also fails if any linked frameworks are not themselves prebound. When prebinding fails, the dynamic linker has to readjust the addresses of symbols in the affected libraries, which can slow down launch time.

In order to minimize symbol-name conflicts, Apple introduced a two-level namespace mechanism in OS X v10.0.4. Two-level namespaces use both the library name and the symbol name to identify each symbol, which reduces the chances of a collision. An executable built with the two-level namespace format is still compatible with versions of OS X prior to version 10.0.4. By default, Xcode builds all new projects using two-level namespaces.

Apple builds and ships its libraries with prebinding enabled and in a way that makes sure there are no address-space overlaps. However, other applications may install libraries and frameworks whose prebound addresses do overlap. Table 1 lists the virtual memory address ranges available to your code on versions of OS X prior to version 10.2. This table also lists the address ranges reserved for Apple-supplied frameworks and services. You can use this information to choose an appropriate location for your framework and library code.

__Table 1__  Prebinding address ranges prior to OS X v10.2)

| Address range | Usage |
| `0x00000000` to `0x410FFFFF` | Application and user framework address range. |
| `0x41100000` to `0x412FFFFF` | Address range reserved for use by Apple frameworks. Do not use this address range for your libraries. |
| `0x41300000` to `0x606DFFFF` | Address range is preferred for use by Apple frameworks |
| `0x606E0000` to `0x6FFFFFFF` | Additional space available for third-party application and framework code. |
| `0x70000000` to `0x8FFFFFFF` | Address range reserved for use by Apple frameworks. Do not use this address range. |
| `0x90000000` to `0x9FFFFFFF` | Additional space available for third-party application and framework code. |
| `0xA0000000` to `0xAFFFFFFF` | Preferred for use by the Window Manager. |
| `0xB0000000` to `0xBFFFFFFF` | Preferred for use by thread stacks. |
| `0xC0000000` to `0xFEFFFFFF` | Additional space available for third-party application and framework code. |
| `0xFF000000` to `0xFFBFFFFF` | Preferred for use by the pasteboard and other system services. |
| `0xFFC00000` to `0xFFFFFFFF` | Additional space available for third-party application and framework code. |

Table 2 lists the virtual memory address ranges available with OS X version 10.2 through version 10.3.x. In cases where an address range is preferred by Apple frameworks or services, you may still be able to use portions of that range. The availability of a given range depends on which frameworks or services your application uses.

__Table 2__  Prebinding address ranges for OS X v10.2 to v10.3.x

| Address range | Usage |
| `0x00000000` to `0x4FFFFFFF` | Application address range. |
| `0x50000000` to `0x8FDFFFFF` | Preferred address range for Apple frameworks. Applications may use this range as necessary. |
| `0x8FE00000` to `0xAFFFFFFF` | Reserved for use by Apple frameworks. Do not use this address range. |
| `0xB0000000` to `0xBFFFFFFF` | Preferred address range for the application’s main thread. The Window Manager may also use portions of this range. Applications may use this range as necessary. |
| `0xC0000000` to `0xEBFFFFFF` | Additional space available for third-party application and framework code. |
| `0xEC000000` to `0xEFFFFFFF` | Preferred for use by the Apple prebinding tools. Applications may use this range as necessary. |
| `0xF0000000` to `0xFDFFFFFF` | Preferred for use by additional thread stacks. Applications may use this range as necessary. |
| `0xFE000000` to `0xFFBFFFFF` | Reserved for use by the pasteboard and other system services. Do not use this address range. |
| `0xFFC00000` to `0xFFFDFFFF` | Preferred for use by other system services. Applications may use this range as necessary. |
| `0xFFFE0000` to `0xFFFFFFFF` | Reserved for use by system services. Do not use this address range. |

Table 3 lists the virtual memory address ranges available with OS X version 10.4 and later. This version consolidates the system libraries into a single address range and frees up more contiguous space for your application to use.

__Table 3__  Prebinding address ranges for OS X v10.4 and later

| Address range | Usage |
| `0x00000000` to `0x8FDFFFFF` | Application address range. |
| `0x8FE00000` to `0xAFFFFFFF` | Reserved exclusively for Apple system libraries. Do not use this address range. |
| `0xB0000000` to `0xBFFFFFFF` | Preferred address range for the application’s main thread. |
| `0xC0000000` to `0xEBFFFFFF` | Additional space available for third-party applications and framework code. |
| `0xEC000000` to `0xEFFFFFFF` | Preferred for use by the Apple prebinding tools. Applications may use this range as necessary. |
| `0xF0000000` to `0xFDFFFFFF` | Preferred for use by additional thread stacks. Applications may use this range as necessary. |
| `0xFE000000` to `0xFFBFFFFF` | Reserved for use by the pasteboard and other system services. Do not use this address range. |
| `0xFFC00000` to `0xFFFDFFFF` | Preferred for use by other system services. Applications may use this range as necessary. |
| `0xFFFE0000` to `0xFFFFFFFF` | Reserved for use by system services. Do not use this address range. |

An application’s binary code is loaded beginning at address `0x00000000`. You should never define a framework with a low address range as it will very likely collide with the address range of any applications that use it. Instead, use an address range that is higher in the available address space.

The simplest way to determine if your Mach-O executable is prebound is to use the `otool` command-line tool to examine the object file. Running this tool with the `-h` and `-v` options displays the Mach header information for the executable. If your executable is prebound, you should see the word `PREBOUND` in the flags section of the header. The following code listing shows the output for the TextEdit application.

```
Mach header
      magic cputype cpusubtype   filetype ncmds sizeofcmds      flags
   MH_MAGIC     PPC        ALL    EXECUTE    54       8108   NOUNDEFS DYLDLINK PREBOUND TWOLEVEL
```

Prior to OS X v10.4, another way to determine if a Mach-O executable is prebound is to enable the prebinding debugging option and launch your executable. (This does not work for applications in OS X v10.4 and later because prebinding for main executables is ignored.) From the `csh` shell, you can do this using the following steps:

1. Launch Terminal.
2. At the Terminal prompt, type the following:

```
setenv DYLD_PREBIND_DEBUG
```
3. At the Terminal prompt, enter the path to your application’s executable file. For TextEdit, you would enter something like the following:

```
/Applications/TextEdit.app/Contents/MacOS/TextEdit
```

If your application is prebound, the `dyld` tool outputs the message `prebinding enabled` to the command line. If you see messages about some number of two-level prebound libraries being used, then your application is only partially prebound.

In all versions of OS X, you should not need to do anything to keep your prebinding information up-to-date on the user’s system. On versions of OS X that require it, the system automatically fixes prebinding information as needed. In addition, the Installer program runs the `update_prebinding` tool at the end of the install cycle to update prebinding information. You should never need to call this tool directly.

[Next](Document%20Revision%20History.md)[Previous](Minimizing%20File%20Access%20At%20Launch%20Time.md)

