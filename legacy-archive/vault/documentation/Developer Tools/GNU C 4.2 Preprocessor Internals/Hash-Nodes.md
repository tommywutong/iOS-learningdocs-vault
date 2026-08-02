---
title: GNU C 4.2 Preprocessor Internals
apple_id: TP40007094
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Hash-Nodes.html
archived_at: '2026-07-15T07:31:01.101637Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU C 4.2 Preprocessor Internals](The%20GNU%20C%20Preprocessor%20Internals.md)



Next: [Macro Expansion](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o),
Previous: [Lexer](Lexer.md#apple-jrsxqzls),
Up: [Top](The%20GNU%20C%20Preprocessor%20Internals.md#apple-krxxa)

---

## Hash Nodes

When cpplib encounters an “identifier”, it generates a hash code for
it and stores it in the hash table. By “identifier” we mean tokens
with type `CPP_NAME`; this includes identifiers in the usual C
sense, as well as keywords, directive names, macro names and so on. For
example, all of `pragma`, `int`, `foo` and
`__GNUC__` are identifiers and hashed when lexed.

Each node in the hash table contain various information about the
identifier it represents. For example, its length and type. At any one
time, each identifier falls into exactly one of three categories:

- Macros

  These have been declared to be macros, either on the command line or
  with `#define`. A few, such as `__TIME__` are built-ins
  entered in the hash table during initialization. The hash node for a
  normal macro points to a structure with more information about the
  macro, such as whether it is function-like, how many arguments it takes,
  and its expansion. Built-in macros are flagged as special, and instead
  contain an enum indicating which of the various built-in macros it is.
- Assertions

  Assertions are in a separate namespace to macros. To enforce this, cpp
  actually prepends a `#` character before hashing and entering it in
  the hash table. An assertion's node points to a chain of answers to
  that assertion.
- Void

  Everything else falls into this category—an identifier that is not
  currently a macro, or a macro that has since been undefined with
  `#undef`.

  When preprocessing C++, this category also includes the named operators,
  such as `xor`. In expressions these behave like the operators they
  represent, but in contexts where the spelling of a token matters they
  are spelt differently. This spelling distinction is relevant when they
  are operands of the stringizing and pasting macro operators `#` and
  `##`. Named operator hash nodes are flagged, both to catch the
  spelling distinction and to prevent them from being defined as macros.

The same identifiers share the same hash node. Since each identifier
token, after lexing, contains a pointer to its hash node, this is used
to provide rapid lookup of various information. For example, when
parsing a `#define` statement, CPP flags each argument's identifier
hash node with the index of that argument. This makes duplicated
argument checking an O(1) operation for each argument. Similarly, for
each identifier in the macro's expansion, lookup to see if it is an
argument, and which argument it is, is also an O(1) operation. Further,
each directive name, such as `endif`, has an associated directive
enum stored in its hash node, so that directive lookup is also O(1).
