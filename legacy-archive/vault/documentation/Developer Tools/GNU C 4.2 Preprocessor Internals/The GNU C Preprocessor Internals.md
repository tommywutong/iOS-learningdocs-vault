---
title: GNU C 4.2 Preprocessor Internals
apple_id: TP40007094
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/index.html
archived_at: '2026-07-15T07:31:01.130650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


# The GNU C Preprocessor Internals

## Table of Contents

- [The GNU C Preprocessor Internals](#apple-krxxa)
- [1 Cpplib—the GNU C Preprocessor](#apple-krxxa)
- [Conventions](Conventions.md#apple-inxw45tfnz2gs33oom)
- [The Lexer](Lexer.md#apple-jrsxqzls)
  - [Overview](Lexer.md#apple-jrsxqzls)
  - [Lexing a token](Lexer.md#apple-jrsxqzls)
  - [Lexing a line](Lexer.md#apple-jrsxqzls)
- [Hash Nodes](Hash-Nodes.md#apple-jbqxg2bnjzxwizlt)
- [Macro Expansion Algorithm](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o)
  - [Internal representation of macros](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o)
  - [Macro expansion overview](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o)
  - [Scanning the replacement list for macros to expand](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o)
  - [Looking for a function-like macro's opening parenthesis](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o)
  - [Marking tokens ineligible for future expansion](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o)
- [Token Spacing](Token-Spacing.md#apple-krxwwzlofvjxayldnfxgo)
- [Line numbering](Line-Numbering.md#apple-jruw4zjnjz2w2ytfojuw4zy)
  - [Just which line number anyway?](Line-Numbering.md#apple-jruw4zjnjz2w2ytfojuw4zy)
  - [Representation of line numbers](Line-Numbering.md#apple-jruw4zjnjz2w2ytfojuw4zy)
- [The Multiple-Include Optimization](Guard-Macros.md#apple-i52wc4tefvgwcy3sn5zq)
- [File Handling](Files.md#apple-izuwyzlt)
- [Concept Index](Concept-Index.md#apple-inxw4y3fob2c2slomrsxq)

Next: [Conventions](Conventions.md#apple-inxw45tfnz2gs33oom),
Up: [(dir)](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/index.html#dir)

---

## The GNU C Preprocessor Internals

## 1 Cpplib—the GNU C Preprocessor

The GNU C preprocessor is
implemented as a library, cpplib, so it can be easily shared between
a stand-alone preprocessor, and a preprocessor integrated with the C,
C++ and Objective-C front ends. It is also available for use by other
programs, though this is not recommended as its exposed interface has
not yet reached a point of reasonable stability.

The library has been written to be re-entrant, so that it can be used
to preprocess many files simultaneously if necessary. It has also been
written with the preprocessing token as the fundamental unit; the
preprocessor in previous versions of GCC would operate on text strings
as the fundamental unit.

This brief manual documents the internals of cpplib, and explains some
of the tricky issues. It is intended that, along with the comments in
the source code, a reasonably competent C programmer should be able to
figure out what the code is doing, and why things have been implemented
the way they have.

- [Conventions](Conventions.md#apple-inxw45tfnz2gs33oom): Conventions used in the code.
- [Lexer](Lexer.md#apple-jrsxqzls): The combined C, C++ and Objective-C Lexer.
- [Hash Nodes](Hash-Nodes.md#apple-jbqxg2bnjzxwizlt): All identifiers are entered into a hash table.
- [Macro Expansion](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o): Macro expansion algorithm.
- [Token Spacing](Token-Spacing.md#apple-krxwwzlofvjxayldnfxgo): Spacing and paste avoidance issues.
- [Line Numbering](Line-Numbering.md#apple-jruw4zjnjz2w2ytfojuw4zy): Tracking location within files.
- [Guard Macros](Guard-Macros.md#apple-i52wc4tefvgwcy3sn5zq): Optimizing header files with guard macros.
- [Files](Files.md#apple-izuwyzlt): File handling.
- [Concept Index](Concept-Index.md#apple-inxw4y3fob2c2slomrsxq): Index.
