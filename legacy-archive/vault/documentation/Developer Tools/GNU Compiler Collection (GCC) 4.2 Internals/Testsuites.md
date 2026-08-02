---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Testsuites.html
archived_at: '2026-07-15T07:31:02.997096Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs),
Up: [Source Tree](Source-Tree.md#apple-knxxk4tdmuwvi4tfmu)

---

### 6.4 Testsuites

GCC contains several testsuites to help maintain compiler quality.
Most of the runtime libraries and language front ends in GCC have
testsuites. Currently only the C language testsuites are documented
here; FIXME: document the others.

- [Test Idioms](Test-Idioms.md#apple-krsxg5bnjfsgs33nom): Idioms used in testsuite code.
- [Test Directives](Test-Directives.md#apple-krsxg5bniruxezldoruxmzlt): Directives used within DejaGnu tests.
- [Ada Tests](Ada-Tests.md#apple-ifsgclkumvzxi4y): The Ada language testsuites.
- [C Tests](C-Tests.md#apple-imwvizltorzq): The C language testsuites.
- [libgcj Tests](libgcj-Tests.md#apple-nruwez3dniwvizltorzq): The Java library testsuites.
- [gcov Testing](gcov-Testing.md#apple-m5rw65rnkrsxg5djnztq): Support for testing gcov.
- [profopt Testing](profopt-Testing.md#apple-obzg6ztpob2c2vdfon2gs3th): Support for testing profile-directed optimizations.
- [compat Testing](compat-Testing.md#apple-mnxw24dboqwvizltoruw4zy): Support for testing binary compatibility.
