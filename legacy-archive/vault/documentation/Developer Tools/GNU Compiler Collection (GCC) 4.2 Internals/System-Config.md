---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/System-Config.html
archived_at: '2026-07-15T07:31:02.934380Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Configuration Files](Configuration-Files.md#apple-inxw4ztjm52xeylunfxw4lkgnfwgk4y),
Previous: [Config Fragments](Config-Fragments.md#apple-inxw4ztjm4wum4tbm5wwk3tuom),
Up: [Configuration](Configuration.md#apple-inxw4ztjm52xeylunfxw4)

---

##### 6.3.2.2 The `config.build`; `config.host`; and `config.gcc` Files

The `config.build` file contains specific rules for particular systems
which GCC is built on. This should be used as rarely as possible, as the
behavior of the build system can always be detected by autoconf.

The `config.host` file contains specific rules for particular systems
which GCC will run on. This is rarely needed.

The `config.gcc` file contains specific rules for particular systems
which GCC will generate code for. This is usually needed.

Each file has a list of the shell variables it sets, with descriptions, at the
top of the file.

FIXME: document the contents of these files, and what variables should
be set to control build, host and target configuration.
