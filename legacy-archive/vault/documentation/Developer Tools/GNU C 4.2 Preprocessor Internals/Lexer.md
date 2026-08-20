---
title: GNU C 4.2 Preprocessor Internals
apple_id: TP40007094
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Lexer.html
archived_at: '2026-07-15T07:31:01.106706Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU C 4.2 Preprocessor Internals](The%20GNU%20C%20Preprocessor%20Internals.md)



Next: [Hash Nodes](Hash-Nodes.md#apple-jbqxg2bnjzxwizlt),
Previous: [Conventions](Conventions.md#apple-inxw45tfnz2gs33oom),
Up: [Top](The%20GNU%20C%20Preprocessor%20Internals.md#apple-krxxa)

---

## The Lexer

### Overview

The lexer is contained in the file `lex.c`. It is a hand-coded
lexer, and not implemented as a state machine. It can understand C, C++
and Objective-C source code, and has been extended to allow reasonably
successful preprocessing of assembly language. The lexer does not make
an initial pass to strip out trigraphs and escaped newlines, but handles
them as they are encountered in a single pass of the input file. It
returns preprocessing tokens individually, not a line at a time.

It is mostly transparent to users of the library, since the library's
interface for obtaining the next token, `cpp_get_token`, takes care
of lexing new tokens, handling directives, and expanding macros as
necessary. However, the lexer does expose some functionality so that
clients of the library can easily spell a given token, such as
`cpp_spell_token` and `cpp_token_len`. These functions are
useful when generating diagnostics, and for emitting the preprocessed
output.

### Lexing a token

Lexing of an individual token is handled by `_cpp_lex_direct` and
its subroutines. In its current form the code is quite complicated,
with read ahead characters and such-like, since it strives to not step
back in the character stream in preparation for handling non-ASCII file
encodings. The current plan is to convert any such files to UTF-8
before processing them. This complexity is therefore unnecessary and
will be removed, so I'll not discuss it further here.

The job of `_cpp_lex_direct` is simply to lex a token. It is not
responsible for issues like directive handling, returning lookahead
tokens directly, multiple-include optimization, or conditional block
skipping. It necessarily has a minor rôle to play in memory
management of lexed lines. I discuss these issues in a separate section
(see [Lexing a line](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Lexing-a-line.html#Lexing-a-line)).

The lexer places the token it lexes into storage pointed to by the
variable `cur_token`, and then increments it. This variable is
important for correct diagnostic positioning. Unless a specific line
and column are passed to the diagnostic routines, they will examine the
`line` and `col` values of the token just before the location
that `cur_token` points to, and use that location to report the
diagnostic.

The lexer does not consider whitespace to be a token in its own right.
If whitespace (other than a new line) precedes a token, it sets the
`PREV_WHITE` bit in the token's flags. Each token has its
`line` and `col` variables set to the line and column of the
first character of the token. This line number is the line number in
the translation unit, and can be converted to a source (file, line) pair
using the line map code.

The first token on a logical, i.e. unescaped, line has the flag
`BOL` set for beginning-of-line. This flag is intended for
internal use, both to distinguish a ``#`' that begins a directive
from one that doesn't, and to generate a call-back to clients that want
to be notified about the start of every non-directive line with tokens
on it. Clients cannot reliably determine this for themselves: the first
token might be a macro, and the tokens of a macro expansion do not have
the `BOL` flag set. The macro expansion may even be empty, and the
next token on the line certainly won't have the `BOL` flag set.

New lines are treated specially; exactly how the lexer handles them is
context-dependent. The C standard mandates that directives are
terminated by the first unescaped newline character, even if it appears
in the middle of a macro expansion. Therefore, if the state variable
`in_directive` is set, the lexer returns a `CPP_EOF` token,
which is normally used to indicate end-of-file, to indicate
end-of-directive. In a directive a `CPP_EOF` token never means
end-of-file. Conveniently, if the caller was `collect_args`, it
already handles `CPP_EOF` as if it were end-of-file, and reports an
error about an unterminated macro argument list.

The C standard also specifies that a new line in the middle of the
arguments to a macro is treated as whitespace. This white space is
important in case the macro argument is stringified. The state variable
`parsing_args` is nonzero when the preprocessor is collecting the
arguments to a macro call. It is set to 1 when looking for the opening
parenthesis to a function-like macro, and 2 when collecting the actual
arguments up to the closing parenthesis, since these two cases need to
be distinguished sometimes. One such time is here: the lexer sets the
`PREV_WHITE` flag of a token if it meets a new line when
`parsing_args` is set to 2. It doesn't set it if it meets a new
line when `parsing_args` is 1, since then code like

```
     #define foo() bar
     foo
     baz
```

would be output with an erroneous space before ``baz`':

```
     foo
      baz
```

This is a good example of the subtlety of getting token spacing correct
in the preprocessor; there are plenty of tests in the testsuite for
corner cases like this.

The lexer is written to treat each of ``\r`', ``\n`', ``\r\n`'
and ``\n\r`' as a single new line indicator. This allows it to
transparently preprocess MS-DOS, Macintosh and Unix files without their
needing to pass through a special filter beforehand.

We also decided to treat a backslash, either ``\`' or the trigraph
``??/`', separated from one of the above newline indicators by
non-comment whitespace only, as intending to escape the newline. It
tends to be a typing mistake, and cannot reasonably be mistaken for
anything else in any of the C-family grammars. Since handling it this
way is not strictly conforming to the ISO standard, the library issues a
warning wherever it encounters it.

Handling newlines like this is made simpler by doing it in one place
only. The function `handle_newline` takes care of all newline
characters, and `skip_escaped_newlines` takes care of arbitrarily
long sequences of escaped newlines, deferring to `handle_newline`
to handle the newlines themselves.

The most painful aspect of lexing ISO-standard C and C++ is handling
trigraphs and backlash-escaped newlines. Trigraphs are processed before
any interpretation of the meaning of a character is made, and unfortunately
there is a trigraph representation for a backslash, so it is possible for
the trigraph ``??/`' to introduce an escaped newline.

Escaped newlines are tedious because theoretically they can occur
anywhere—between the ``+`' and ``=`' of the ``+=`' token,
within the characters of an identifier, and even between the ``*`'
and ``/`' that terminates a comment. Moreover, you cannot be sure
there is just one—there might be an arbitrarily long sequence of them.

So, for example, the routine that lexes a number, `parse_number`,
cannot assume that it can scan forwards until the first non-number
character and be done with it, because this could be the ``\`'
introducing an escaped newline, or the ``?`' introducing the trigraph
sequence that represents the ``\`' of an escaped newline. If it
encounters a ``?`' or ``\`', it calls `skip_escaped_newlines`
to skip over any potential escaped newlines before checking whether the
number has been finished.

Similarly code in the main body of `_cpp_lex_direct` cannot simply
check for a ``=`' after a ``+`' character to determine whether it
has a ``+=`' token; it needs to be prepared for an escaped newline of
some sort. Such cases use the function `get_effective_char`, which
returns the first character after any intervening escaped newlines.

The lexer needs to keep track of the correct column position, including
counting tabs as specified by the `-ftabstop=` option. This
should be done even within C-style comments; they can appear in the
middle of a line, and we want to report diagnostics in the correct
position for text appearing after the end of the comment.

Some identifiers, such as `__VA_ARGS__` and poisoned identifiers,
may be invalid and require a diagnostic. However, if they appear in a
macro expansion we don't want to complain with each use of the macro.
It is therefore best to catch them during the lexing stage, in
`parse_identifier`. In both cases, whether a diagnostic is needed
or not is dependent upon the lexer's state. For example, we don't want
to issue a diagnostic for re-poisoning a poisoned identifier, or for
using `__VA_ARGS__` in the expansion of a variable-argument macro.
Therefore `parse_identifier` makes use of state flags to determine
whether a diagnostic is appropriate. Since we change state on a
per-token basis, and don't lex whole lines at a time, this is not a
problem.

Another place where state flags are used to change behavior is whilst
lexing header names. Normally, a ``<`' would be lexed as a single
token. After a `#include` directive, though, it should be lexed as
a single token as far as the nearest ``>`' character. Note that we
don't allow the terminators of header names to be escaped; the first
``"`' or ``>`' terminates the header name.

Interpretation of some character sequences depends upon whether we are
lexing C, C++ or Objective-C, and on the revision of the standard in
force. For example, ``::`' is a single token in C++, but in C it is
two separate ``:`' tokens and almost certainly a syntax error. Such
cases are handled by `_cpp_lex_direct` based upon command-line
flags stored in the `cpp_options` structure.

Once a token has been lexed, it leads an independent existence. The
spelling of numbers, identifiers and strings is copied to permanent
storage from the original input buffer, so a token remains valid and
correct even if its source buffer is freed with `_cpp_pop_buffer`.
The storage holding the spellings of such tokens remains until the
client program calls cpp_destroy, probably at the end of the translation
unit.

### Lexing a line

When the preprocessor was changed to return pointers to tokens, one
feature I wanted was some sort of guarantee regarding how long a
returned pointer remains valid. This is important to the stand-alone
preprocessor, the future direction of the C family front ends, and even
to cpplib itself internally.

Occasionally the preprocessor wants to be able to peek ahead in the
token stream. For example, after the name of a function-like macro, it
wants to check the next token to see if it is an opening parenthesis.
Another example is that, after reading the first few tokens of a
`#pragma` directive and not recognizing it as a registered pragma,
it wants to backtrack and allow the user-defined handler for unknown
pragmas to access the full `#pragma` token stream. The stand-alone
preprocessor wants to be able to test the current token with the
previous one to see if a space needs to be inserted to preserve their
separate tokenization upon re-lexing (paste avoidance), so it needs to
be sure the pointer to the previous token is still valid. The
recursive-descent C++ parser wants to be able to perform tentative
parsing arbitrarily far ahead in the token stream, and then to be able
to jump back to a prior position in that stream if necessary.

The rule I chose, which is fairly natural, is to arrange that the
preprocessor lex all tokens on a line consecutively into a token buffer,
which I call a token run, and when meeting an unescaped new line
(newlines within comments do not count either), to start lexing back at
the beginning of the run. Note that we do _not_ lex a line of
tokens at once; if we did that `parse_identifier` would not have
state flags available to warn about invalid identifiers (see [Invalid identifiers](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Invalid-identifiers.html#Invalid-identifiers)).

In other words, accessing tokens that appeared earlier in the current
line is valid, but since each logical line overwrites the tokens of the
previous line, tokens from prior lines are unavailable. In particular,
since a directive only occupies a single logical line, this means that
the directive handlers like the `#pragma` handler can jump around
in the directive's tokens if necessary.

Two issues remain: what about tokens that arise from macro expansions,
and what happens when we have a long line that overflows the token run?

Since we promise clients that we preserve the validity of pointers that
we have already returned for tokens that appeared earlier in the line,
we cannot reallocate the run. Instead, on overflow it is expanded by
chaining a new token run on to the end of the existing one.

The tokens forming a macro's replacement list are collected by the
`#define` handler, and placed in storage that is only freed by
`cpp_destroy`. So if a macro is expanded in the line of tokens,
the pointers to the tokens of its expansion that are returned will always
remain valid. However, macros are a little trickier than that, since
they give rise to three sources of fresh tokens. They are the built-in
macros like `__LINE__`, and the ``#`' and ``##`' operators
for stringification and token pasting. I handled this by allocating
space for these tokens from the lexer's token run chain. This means
they automatically receive the same lifetime guarantees as lexed tokens,
and we don't need to concern ourselves with freeing them.

Lexing into a line of tokens solves some of the token memory management
issues, but not all. The opening parenthesis after a function-like
macro name might lie on a different line, and the front ends definitely
want the ability to look ahead past the end of the current line. So
cpplib only moves back to the start of the token run at the end of a
line if the variable `keep_tokens` is zero. Line-buffering is
quite natural for the preprocessor, and as a result the only time cpplib
needs to increment this variable is whilst looking for the opening
parenthesis to, and reading the arguments of, a function-like macro. In
the near future cpplib will export an interface to increment and
decrement this variable, so that clients can share full control over the
lifetime of token pointers too.

The routine `_cpp_lex_token` handles moving to new token runs,
calling `_cpp_lex_direct` to lex new tokens, or returning
previously-lexed tokens if we stepped back in the token stream. It also
checks each token for the `BOL` flag, which might indicate a
directive that needs to be handled, or require a start-of-line call-back
to be made. `_cpp_lex_token` also handles skipping over tokens in
failed conditional blocks, and invalidates the control macro of the
multiple-include optimization if a token was successfully lexed outside
a directive. In other words, its callers do not need to concern
themselves with such issues.
