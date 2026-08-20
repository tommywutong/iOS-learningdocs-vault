---
title: GNU C 4.2 Preprocessor Internals
apple_id: TP40007094
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Conventions.html
archived_at: '2026-07-15T07:31:01.083933Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU C 4.2 Preprocessor Internals](The%20GNU%20C%20Preprocessor%20Internals.md)



Next: [Lexer](Lexer.md#apple-jrsxqzls),
Previous: [Top](The%20GNU%20C%20Preprocessor%20Internals.md#apple-krxxa),
Up: [Top](The%20GNU%20C%20Preprocessor%20Internals.md#apple-krxxa)

---

## Conventions

cpplib has two interfaces—one is exposed internally only, and the
other is for both internal and external use.

The convention is that functions and types that are exposed to multiple
files internally are prefixed with ``_cpp_`', and are to be found in
the file `internal.h`. Functions and types exposed to external
clients are in `cpplib.h`, and prefixed with ``cpp_`'. For
historical reasons this is no longer quite true, but we should strive to
stick to it.

We are striving to reduce the information exposed in `cpplib.h` to the
bare minimum necessary, and then to keep it there. This makes clear
exactly what external clients are entitled to assume, and allows us to
change internals in the future without worrying whether library clients
are perhaps relying on some kind of undocumented implementation-specific
behavior.
