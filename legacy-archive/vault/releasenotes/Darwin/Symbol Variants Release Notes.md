---
title: Symbol Variants Release Notes
apple_id: TP40006658
resource_type: Release Note
platform: macOS
topic: Xcode
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/releasenotes/Darwin/SymbolVariantsRelNotes/index.html
archived_at: '2026-07-18T02:50:23.540088Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Symbol Variants: Why Those Dollar Signs?

Since OS X v10.4, in the system library, `libSystem.dylib`, new symbols that contain dollar signs (`$`) have been added. This release note explains why they are there, and how a developer might want to take advantage of them.

#### Contents:

- [Software Evolution vs. Backward Compatibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Symbol Variants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Prototypes in Header Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Preprocessor Macros Controlling the Variants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Summary of Variants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [gdb Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnjyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)

### Software Evolution vs. Backward Compatibility

Software is always changing. New demands require new features to be implemented. Bugs are discovered and fixed. Hardware and lower layers of the OS change, sometimes requiring upper layers to adapt.

For a commercial operating system like OS X, third-party software expects that the system software will always act the same way. This backward compatibility prolongs the users’ investment in software and fosters the notion of greater stability in the system.

The need to evolve the software often conflicts with the desire to provide backward compatibility, but innovative solutions can allow both. If you remember the (classic) Mac OS before OS X, a Classic environment was created specifically to run old applications on OS X. Similarly, the transition to Intel-based hardware spurred the creation of the Rosetta dynamic translation software to provide compatibility with PowerPC-based applications.

Early in the OS X v10.4 timeframe, two major software initiatives required an equally innovative solution to maintain backward compatibility. First, to be certified for UNIX™ conformance, hundreds of system routines needed to be modified. Some changes were considered just bug fixes, but many of the changes required significant change in behavior to the largely BSD-style routines. These changes would surely break existing applications.

> [!NOTE]
> 

Secondly, up until v10.4, there was no support for real (PowerPC) long double floating-point numbers (or more correctly, the long double type was the same size as the regular 64-bit double floating-point type). Support for a real, 128-bit long double type would mean incompatible API changes. Code compiled for one type of long double would crash or produce incorrect results when using routines for the other long double type.

### Symbol Variants

One way to allow routines to behave in new ways for new code but maintain the legacy behavior for previously compiled code is to use _symbol versioning_. In symbol versioning, different code can have the same symbol name, but have different version numbers. Unfortunately, this would require lots of changes to the compiler, linker and binary file format; a major undertaking that would have to happen before the real work could even be started.

So as an alternative, a feature of the `gcc` compiler was used; the `__asm` command can be used to rename a symbol. A special suffix was added to the symbol, and by using different suffixes, we can generate families of _symbol variants_.

That is where the dollar sign comes in. It is used as a separator between the real symbol name and the variant name. Since it can’t occur in normal C code, this avoids the possibility of symbol name collision.

This is what it looks like:

```
% nm /usr/lib/libSystem.dylib
...
00086e9f T _fputs
0003a14f T _fputs$UNIX2003
...
```

By OS X convention, all variables and routine names are automatically prefixed with an underscore. The `_fputs` symbol is the legacy variant, while the `_fputs$UNIX2003` symbol is the new, UNIX™ conforming one. All programs previously built will only know about the `_fputs` symbol, and will continue to use it and get legacy behavior, while new code can link to the new `_fputs$UNIX2003` symbol and get UNIX™ conforming behavior.

A symbol may have more than one suffix. For instance:

```
000a6905 T _ftw
000a6603 T _ftw$INODE64$UNIX2003
000a6dc7 T _ftw$UNIX2003
```

> [!NOTE]
> 

### Prototypes in Header Files

It is in the header files that the real magic occurs. For instance, to generate the `_fputs$UNIX2003` symbol, we would need something like:

```
int fputs(const char * __restrict, FILE * __restrict) __asm("_fputs$UNIX2003");
```

In `<stdio.h>`, the actual prototype looks like:

```
int fputs(const char * __restrict, FILE * __restrict) __DARWIN_ALIAS(fputs);
```

The `__DARWIN_ALIAS` macro resolves to the necessary `__asm` command, as appropriate for the legacy or UNIX™ conforming variant.

### Preprocessor Macros Controlling the Variants

The UNIX™ conformance variants use the `$UNIX2003` suffix.

> [!NOTE]
> 

Because the 64-bit environment has no legacy to maintain, it was created to be UNIX™ conforming from the start, without the use of the `$UNIX2003` suffix. So, for example, `_fputs$UNIX2003` in 32-bit and `_fputs` in 64-bit will have the same conforming behavior.

As of OS X v10.5, UNIX™ conformance is on by default, and newly compiled code will link against the UNIX™ conformance variants, unless overridden with the following five macros.

|  |  |
| --- | --- |
| **`_POSIX_C_SOURCE` and `_XOPEN_SOURCE`** | : The `_POSIX_C_SOURCE` and `_XOPEN_SOURCE` macros are often set to specify the various levels of standards support. On OS X, only _SUSv3_ is supported, so the actual value of these macros is not used (but they are reset to appropriate values when necessary).  When either or both of these macros are set, the UNIX™ conforming variants will be used. In addition, unless `_DARWIN_C_SOURCE` is also set (see below), these macros will cause the hiding of any variable, routine, structure, etc., in covered header files that are not specified in the standards. (These extra definitions are referred to as _extensions_ to the standards.) Thus, only _SUSv3_ definitions will be visible in those header files. |

|  |  |
| --- | --- |
| **`_DARWIN_C_SOURCE`** | : The `_DARWIN_C_SOURCE` macro (defined to any value), causes the UNIX™ conforming variants to be used, but does not hide the extensions to the standards, as `_POSIX_C_SOURCE` and `_XOPEN_SOURCE` do. The `_DARWIN_C_SOURCE` macro can be used in conjunction with the `_POSIX_C_SOURCE` and `_XOPEN_SOURCE` macros, with the `_DARWIN_C_SOURCE` behavior overriding the other two, allowing the extensions to the standards to be visible.  In addition, the `_DARWIN_C_SOURCE` macro will enable a few other extensions to the standards. These extensions occur where the _SUSv3_ standard puts additional limitations on the functionality beyond that of legacy (and, typically, BSD) behavior. The extension variants use the `$DARWIN_EXTSN` suffix, and can also be enabled with separate macros. (See the macro descriptions below.)   > [!NOTE] >  |

|  |  |
| --- | --- |
| **`_NONSTD_SOURCE`** | : The `_NONSTD_SOURCE` macro can be used to turn off the default UNIX™ conformance, and allow code to be built with legacy behavior. However, this macro will produce a compiler error when any of the above macros are set.     > [!NOTE] >  |

|  |  |
| --- | --- |
| **`MACOSX_DEPLOYMENT_TARGET`** | : When none of the previous four macros are set, the variants chosen are affected by the environment variable `MACOSX_DEPLOYMENT_TARGET` or the `−mmacosx-version-min=...` argument passed to the compiler. For example, you might pass `−mmacosx-version-min=10.5` to the compiler or set `MACOSX_DEPLOYMENT_TARGET=10.5` to target OS X v10.5.  If you target version 10.5 or later, the UNIX™ conforming variants are used automatically. If you target version 10.4 or earlier, the legacy variants are used. (There are other side effects as well, such as disabling newer linker features.)  In OS X v10.5 or later, if you do not use this or the previous four macros, the UNIX™ conforming variants are used by default.  In addition, if you target version 10.5 or later (or by default if you do not target a specific version), the OS X v10.5 variants (those with the `$1050` suffix) are used. These variants have significant new behavior that might cause previously compiled programs to misbehave. For example, the (legacy) `_select` routine imposed a minimum timeout value of 10 milliseconds; the new `_select$1050` routine has no such minimum. |

|  |  |
| --- | --- |
| **`MACOSX_DEPLOYMENT_TARGET` (32-bit PowerPC only)** | : Setting `MACOSX_DEPLOYMENT_TARGET` to 10.4 or later (or passing `−mmacosx-version-min=10.4` or later to the compiler) enables 128-bit long double support. Routines that pass long doubles either directly (like `strtold`) or indirectly (like `printf` and family) have the 128-bit long double variant which uses the `$LDBL128` suffix, while the legacy 64-bit long double variants are unadorned.    What happens when `MACOSX_DEPLOYMENT_TARGET` is set to 10.3 or earlier (or is not set at all) is more complicated. During the development of OS X v10.4, it was desired to have 128-bit long double support be the default. However, when `MACOSX_DEPLOYMENT_TARGET` is not set, things would default to the behavior three releases before—that of 10.1. While it was possible to back-port the standard C library routines that used long double support to 10.3 (though not the math routines), they couldn’t be back-ported to 10.1 or 10.2.   > [!NOTE] >    As a compromise, when `MACOSX_DEPLOYMENT_TARGET` is not set, or set to 10.3 or earlier, the header files would use a different variant, with the `$LDBLStub` suffix. The compiler would instruct the loader to link against `/usr/lib/libSystemStubs.a`, where the `$LDBLStub` suffixed symbols are defined. At runtime, these assembly language stubs try to lookup the symbol with the same base name and a `$LDBL128` suffix, and if it finds it, uses it. Otherwise, it will call the unadorned symbol name. This allows the code to adapt to whichever symbols are actually available in the current system library.   > [!NOTE] >   > [!NOTE] >    On OS X v10.5, not setting `MACOSX_DEPLOYMENT_TARGET` and not using `−mmacosx-version-min` will result in 10.5 behavior by default, so the `$LDBL128` variants are used instead of the `$LDBLStub` variants. However, as before, if `MACOSX_DEPLOYMENT_TARGET` is set to 10.3 or earlier, the `$LDBLStub` variants are used.   > [!NOTE] >   > [!NOTE] >  |

|  |  |
| --- | --- |
| **`_DARWIN_UNLIMITED_SELECT`** | : Setting the `_DARWIN_UNLIMITED_SELECT` macro will select the extension variants of `select()` and `pselect()`, which uses the `$DARWIN_EXTSN` suffix. The extended versions do not fail if the first argument is greater than `FD_SETSIZE`. This was the original BSD behavior.   > [!NOTE] >  |

|  |  |
| --- | --- |
| **`_DARWIN_BETTER_REALPATH`** | : Setting the `_DARWIN_BETTER_REALPATH` macro selects the extension variant of `realpath()`, which uses the `$DARWIN_EXTSN` suffix. The extended version uses a fast shortcut to determine the current working directory, but this shortcut does not fail if the parent directories are not readable, as is dictated by the standards.   > [!NOTE] >  |

|  |  |
| --- | --- |
| **`_DARWIN_USE_64_BIT_INODE`** | : Setting the `_DARWIN_USE_64_BIT_INODE` macro selects the 64-bit inode variants (those with a `$INODE64` suffix) of routines like `stat()` and `readdir()`, which return an `ino_t` value. The current default is to return legacy 32-bit `ino_t` values, but 64-bit `ino_t` values will become the default in the future. Structures containing `ino_t` fields, like `struct stat`, are larger than the 32-bit `ino_t` versions, may have different ordering of the fields (to improve packing efficiency) and may have entirely new fields.   > [!NOTE] >     > [!IMPORTANT] >  |

### Summary of Variants

Below is a table that summarizes the variant suffixes and the corresponding, controlling and feature test macros.

| Variant Suffix | Controlling Preprocessor Macro | Feature Test Macro | Description |
| --- | --- | --- | --- |
| `$1050` | `MACOSX_DEPLOYMENT_TARGET` |  | OS X v10.5 and later behavior change |
| `$DARWIN_EXTSN` | `_DARWIN_C_SOURCE` or specific extension macro |  | Extended behavior beyond standards |
| `$INODE64` | `_DARWIN_USE_64_BIT_INODE` | `_DARWIN_FEATURE_64_BIT_INODE` | 64-bit `ino_t` values |
| `$LDBL128` | `MACOSX_DEPLOYMENT_TARGET` | `_DARWIN_FEATURE_LONG_DOUBLE_IS_DOUBLE` (negation) | 128-bit long double support (32-bit PowerPC only) |
| `$UNIX2003` | `_POSIX_C_SOURCE`  `_XOPEN_SOURCE`  `_DARWIN_C_SOURCE`  `_NONSTD_SOURCE`  `MACOSX_DEPLOYMENT_TARGET` | `_DARWIN_FEATURE_UNIX_CONFORMANCE` | UNIX™ conformance |
| `$NOCANCEL`  `$fenv_access_off` |  |  | (used internally) |
| `$LDBL64` |  |  | (unused; may be removed) |

### gdb Support

When setting a breakpoint at a routine that has multiple variants, `gdb` will set a breakpoint at each variant. The `delete` command can be used to remove any unwanted breakpoint at any of the variants. For example:

```
(gdb) b select Breakpoint 1 at 0x85edd Breakpoint 2 at 0x54592 Breakpoint 3 at 0x4ff50 Breakpoint 4 at 0x37b44 Breakpoint 5 at 0x37b09 warning: Multiple breakpoints were set. Use the "delete" command to delete unwanted breakpoints. (gdb) info breakpoints Num Type           Disp Enb Address    What 1   breakpoint     keep y   0x00085edd <select+6> 2   breakpoint     keep y   0x00054592 <select$UNIX2003+6> 3   breakpoint     keep y   0x0004ff50 <select$DARWIN_EXTSN> 4   breakpoint     keep y   0x00037b44 <select$DARWIN_EXTSN$NOCANCEL> 5   breakpoint     keep y   0x00037b09 <select$NOCANCEL$UNIX2003+6>
```
