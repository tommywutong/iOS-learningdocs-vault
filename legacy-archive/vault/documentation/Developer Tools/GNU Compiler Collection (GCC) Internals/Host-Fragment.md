---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Host-Fragment.html
archived_at: '2026-07-15T07:31:00.040430Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Target Fragment](Target-Fragment.md#apple-krqxez3foqwum4tbm5wwk3tu),
Up: [Fragments](Fragments.md#apple-izzgcz3nmvxhi4y)

---

### 15.2 Host Makefile Fragments

The use of `x-host` fragments is discouraged. You should do
so only if there is no other mechanism to get the behavior desired.
Host fragments should never forcibly override variables set by the
configure script, as they may have been adjusted by the user.

Variables provided for host fragments to set include:

**`X_CFLAGS`

**`X_CPPFLAGS`****
: These are extra flags to pass to the C compiler and preprocessor,
respectively. They are used both when building GCC, and when compiling
things with the just-built GCC.

**`XCFLAGS`**
: These are extra flags to use when building the compiler. They are not
used when compiling `libgcc.a`. However, they _are_ used when
recompiling the compiler with itself in later stages of a bootstrap.

**`BOOT_LDFLAGS`**
: Flags to be passed to the linker when recompiling the compiler with
itself in later stages of a bootstrap. You might need to use this if,
for instance, one of the front ends needs more text space than the
linker provides by default.

**`EXTRA_PROGRAMS`**
: A list of additional programs required to use the compiler on this host,
which should be compiled with GCC and installed alongside the front
ends. If you set this variable, you must also provide rules to build
the extra programs.
