---
title: GNU C 4.2 Preprocessor Internals
apple_id: TP40007094
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Line-Numbering.html
archived_at: '2026-07-15T07:31:01.113553Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU C 4.2 Preprocessor Internals](The%20GNU%20C%20Preprocessor%20Internals.md)



Next: [Guard Macros](Guard-Macros.md#apple-i52wc4tefvgwcy3sn5zq),
Previous: [Token Spacing](Token-Spacing.md#apple-krxwwzlofvjxayldnfxgo),
Up: [Top](The%20GNU%20C%20Preprocessor%20Internals.md#apple-krxxa)

---

## Line numbering

### Just which line number anyway?

There are three reasonable requirements a cpplib client might have for
the line number of a token passed to it:

- The source line it was lexed on.
- The line it is output on. This can be different to the line it was
  lexed on if, for example, there are intervening escaped newlines or
  C-style comments. For example:

  ```
            foo /* A long
            comment */ bar \
            baz
            =>
            foo bar baz

  ```
- If the token results from a macro expansion, the line of the macro name,
  or possibly the line of the closing parenthesis in the case of
  function-like macro expansion.

The `cpp_token` structure contains `line` and `col`
members. The lexer fills these in with the line and column of the first
character of the token. Consequently, but maybe unexpectedly, a token
from the replacement list of a macro expansion carries the location of
the token within the `#define` directive, because cpplib expands a
macro by returning pointers to the tokens in its replacement list. The
current implementation of cpplib assigns tokens created from built-in
macros and the ``#`' and ``##`' operators the location of the most
recently lexed token. This is a because they are allocated from the
lexer's token runs, and because of the way the diagnostic routines infer
the appropriate location to report.

The diagnostic routines in cpplib display the location of the most
recently _lexed_ token, unless they are passed a specific line and
column to report. For diagnostics regarding tokens that arise from
macro expansions, it might also be helpful for the user to see the
original location in the macro definition that the token came from.
Since that is exactly the information each token carries, such an
enhancement could be made relatively easily in future.

The stand-alone preprocessor faces a similar problem when determining
the correct line to output the token on: the position attached to a
token is fairly useless if the token came from a macro expansion. All
tokens on a logical line should be output on its first physical line, so
the token's reported location is also wrong if it is part of a physical
line other than the first.

To solve these issues, cpplib provides a callback that is generated
whenever it lexes a preprocessing token that starts a new logical line
other than a directive. It passes this token (which may be a
`CPP_EOF` token indicating the end of the translation unit) to the
callback routine, which can then use the line and column of this token
to produce correct output.

### Representation of line numbers

As mentioned above, cpplib stores with each token the line number that
it was lexed on. In fact, this number is not the number of the line in
the source file, but instead bears more resemblance to the number of the
line in the translation unit.

The preprocessor maintains a monotonic increasing line count, which is
incremented at every new line character (and also at the end of any
buffer that does not end in a new line). Since a line number of zero is
useful to indicate certain special states and conditions, this variable
starts counting from one.

This variable therefore uniquely enumerates each line in the translation
unit. With some simple infrastructure, it is straight forward to map
from this to the original source file and line number pair, saving space
whenever line number information needs to be saved. The code the
implements this mapping lies in the files `line-map.c` and
`line-map.h`.

Command-line macros and assertions are implemented by pushing a buffer
containing the right hand side of an equivalent `#define` or
`#assert` directive. Some built-in macros are handled similarly.
Since these are all processed before the first line of the main input
file, it will typically have an assigned line closer to twenty than to
one.
