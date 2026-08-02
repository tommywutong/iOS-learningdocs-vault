---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Fragments.html
archived_at: '2026-07-15T07:31:01.891059Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Collect2](Collect2.md#apple-inxwy3dfmn2de),
Previous: [Host Config](Host-Config.md#apple-jbxxg5bninxw4ztjm4),
Up: [Top](index.md#apple-krxxa)

---

## 17 Makefile Fragments

When you configure GCC using the `configure` script, it will
construct the file `Makefile` from the template file
`Makefile.in`. When it does this, it can incorporate makefile
fragments from the `config` directory. These are used to set
Makefile parameters that are not amenable to being calculated by
autoconf. The list of fragments to incorporate is set by
`config.gcc` (and occasionally `config.build`
and `config.host`); See [System Config](System-Config.md#apple-kn4xg5dfnuwug33omzuwo).

Fragments are named either `t-target` or `x-host`,
depending on whether they are relevant to configuring GCC to produce
code for a particular target, or to configuring GCC to run on a
particular host. Here target and host are mnemonics
which usually have some relationship to the canonical system name, but
no formal connection.

If these files do not exist, it means nothing needs to be added for a
given target or host. Most targets need a few `t-target`
fragments, but needing `x-host` fragments is rare.

- [Target Fragment](Target-Fragment.md#apple-krqxez3foqwum4tbm5wwk3tu): Writing `t-target` files.
- [Host Fragment](Host-Fragment.md#apple-jbxxg5bnizzgcz3nmvxhi): Writing `x-host` files.
