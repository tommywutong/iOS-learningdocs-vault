---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Host-Config.html
archived_at: '2026-07-15T07:31:02.054344Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Fragments](Fragments.md#apple-izzgcz3nmvxhi4y),
Previous: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg),
Up: [Top](index.md#apple-krxxa)

---

## 16 Host Configuration

Most details about the machine and system on which the compiler is
actually running are detected by the `configure` script. Some
things are impossible for `configure` to detect; these are
described in two ways, either by macros defined in a file named
`xm-machine.h` or by hook functions in the file specified
by the out_host_hook_obj variable in `config.gcc`. (The
intention is that very few hosts will need a header file but nearly
every fully supported host will need to override some hooks.)

If you need to define only a few macros, and they have simple
definitions, consider using the `xm_defines` variable in your
`config.gcc` entry instead of creating a host configuration
header. See [System Config](System-Config.md#apple-kn4xg5dfnuwug33omzuwo).

- [Host Common](Host-Common.md#apple-jbxxg5bninxw23lpny): Things every host probably needs implemented.
- [Filesystem](Filesystem.md#apple-izuwyzltpfzxizln): Your host can't have the letter `a' in filenames?
- [Host Misc](Host-Misc.md#apple-jbxxg5bnjvuxgyy): Rare configuration options for hosts.
