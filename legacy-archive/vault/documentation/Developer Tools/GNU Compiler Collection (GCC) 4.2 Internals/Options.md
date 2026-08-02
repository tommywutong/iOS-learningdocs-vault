---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Options.html
archived_at: '2026-07-15T07:31:02.526174Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Passes](Passes.md#apple-kbqxg43fom),
Previous: [Source Tree](Source-Tree.md#apple-knxxk4tdmuwvi4tfmu),
Up: [Top](index.md#apple-krxxa)

---

## 7 Option specification files

Most GCC command-line options are described by special option
definition files, the names of which conventionally end in
`.opt`. This chapter describes the format of these files.

- [Option file format](Option-file-format.md#apple-j5yhi2lpnywwm2lmmuwwm33snvqxi): The general layout of the files
- [Option properties](Option-properties.md#apple-j5yhi2lpnywxa4tpobsxe5djmvzq): Supported option properties
