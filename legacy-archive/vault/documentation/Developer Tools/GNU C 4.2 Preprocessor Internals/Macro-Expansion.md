---
title: GNU C 4.2 Preprocessor Internals
apple_id: TP40007094
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Macro-Expansion.html
archived_at: '2026-07-15T07:31:01.118604Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU C 4.2 Preprocessor Internals](The%20GNU%20C%20Preprocessor%20Internals.md)



Next: [Token Spacing](Token-Spacing.md#apple-krxwwzlofvjxayldnfxgo),
Previous: [Hash Nodes](Hash-Nodes.md#apple-jbqxg2bnjzxwizlt),
Up: [Top](The%20GNU%20C%20Preprocessor%20Internals.md#apple-krxxa)

---

## Macro Expansion Algorithm

Macro expansion is a tricky operation, fraught with nasty corner cases
and situations that render what you thought was a nifty way to
optimize the preprocessor's expansion algorithm wrong in quite subtle
ways.

I strongly recommend you have a good grasp of how the C and C++
standards require macros to be expanded before diving into this
section, let alone the code!. If you don't have a clear mental
picture of how things like nested macro expansion, stringification and
token pasting are supposed to work, damage to your sanity can quickly
result.

### Internal representation of macros

The preprocessor stores macro expansions in tokenized form. This
saves repeated lexing passes during expansion, at the cost of a small
increase in memory consumption on average. The tokens are stored
contiguously in memory, so a pointer to the first one and a token
count is all you need to get the replacement list of a macro.

If the macro is a function-like macro the preprocessor also stores its
parameters, in the form of an ordered list of pointers to the hash
table entry of each parameter's identifier. Further, in the macro's
stored expansion each occurrence of a parameter is replaced with a
special token of type `CPP_MACRO_ARG`. Each such token holds the
index of the parameter it represents in the parameter list, which
allows rapid replacement of parameters with their arguments during
expansion. Despite this optimization it is still necessary to store
the original parameters to the macro, both for dumping with e.g.,
`-dD`, and to warn about non-trivial macro redefinitions when
the parameter names have changed.

### Macro expansion overview

The preprocessor maintains a context stack, implemented as a
linked list of `cpp_context` structures, which together represent
the macro expansion state at any one time. The `struct
cpp_reader` member variable `context` points to the current top
of this stack. The top normally holds the unexpanded replacement list
of the innermost macro under expansion, except when cpplib is about to
pre-expand an argument, in which case it holds that argument's
unexpanded tokens.

When there are no macros under expansion, cpplib is in base
context. All contexts other than the base context contain a
contiguous list of tokens delimited by a starting and ending token.
When not in base context, cpplib obtains the next token from the list
of the top context. If there are no tokens left in the list, it pops
that context off the stack, and subsequent ones if necessary, until an
unexhausted context is found or it returns to base context. In base
context, cpplib reads tokens directly from the lexer.

If it encounters an identifier that is both a macro and enabled for
expansion, cpplib prepares to push a new context for that macro on the
stack by calling the routine `enter_macro_context`. When this
routine returns, the new context will contain the unexpanded tokens of
the replacement list of that macro. In the case of function-like
macros, `enter_macro_context` also replaces any parameters in the
replacement list, stored as `CPP_MACRO_ARG` tokens, with the
appropriate macro argument. If the standard requires that the
parameter be replaced with its expanded argument, the argument will
have been fully macro expanded first.

`enter_macro_context` also handles special macros like
`__LINE__`. Although these macros expand to a single token which
cannot contain any further macros, for reasons of token spacing
(see [Token Spacing](Token-Spacing.md#apple-krxwwzlofvjxayldnfxgo)) and simplicity of implementation, cpplib
handles these special macros by pushing a context containing just that
one token.

The final thing that `enter_macro_context` does before returning
is to mark the macro disabled for expansion (except for special macros
like `__TIME__`). The macro is re-enabled when its context is
later popped from the context stack, as described above. This strict
ordering ensures that a macro is disabled whilst its expansion is
being scanned, but that it is _not_ disabled whilst any arguments
to it are being expanded.

### Scanning the replacement list for macros to expand

The C standard states that, after any parameters have been replaced
with their possibly-expanded arguments, the replacement list is
scanned for nested macros. Further, any identifiers in the
replacement list that are not expanded during this scan are never
again eligible for expansion in the future, if the reason they were
not expanded is that the macro in question was disabled.

Clearly this latter condition can only apply to tokens resulting from
argument pre-expansion. Other tokens never have an opportunity to be
re-tested for expansion. It is possible for identifiers that are
function-like macros to not expand initially but to expand during a
later scan. This occurs when the identifier is the last token of an
argument (and therefore originally followed by a comma or a closing
parenthesis in its macro's argument list), and when it replaces its
parameter in the macro's replacement list, the subsequent token
happens to be an opening parenthesis (itself possibly the first token
of an argument).

It is important to note that when cpplib reads the last token of a
given context, that context still remains on the stack. Only when
looking for the _next_ token do we pop it off the stack and drop
to a lower context. This makes backing up by one token easy, but more
importantly ensures that the macro corresponding to the current
context is still disabled when we are considering the last token of
its replacement list for expansion (or indeed expanding it). As an
example, which illustrates many of the points above, consider

```
     #define foo(x) bar x
     foo(foo) (2)
```

which fully expands to ``bar foo (2)`'. During pre-expansion
of the argument, ``foo`' does not expand even though the macro is
enabled, since it has no following parenthesis [pre-expansion of an
argument only uses tokens from that argument; it cannot take tokens
from whatever follows the macro invocation]. This still leaves the
argument token ``foo`' eligible for future expansion. Then, when
re-scanning after argument replacement, the token ``foo`' is
rejected for expansion, and marked ineligible for future expansion,
since the macro is now disabled. It is disabled because the
replacement list ``bar foo`' of the macro is still on the context
stack.

If instead the algorithm looked for an opening parenthesis first and
then tested whether the macro were disabled it would be subtly wrong.
In the example above, the replacement list of ``foo`' would be
popped in the process of finding the parenthesis, re-enabling
``foo`' and expanding it a second time.

### Looking for a function-like macro's opening parenthesis

Function-like macros only expand when immediately followed by a
parenthesis. To do this cpplib needs to temporarily disable macros
and read the next token. Unfortunately, because of spacing issues
(see [Token Spacing](Token-Spacing.md#apple-krxwwzlofvjxayldnfxgo)), there can be fake padding tokens in-between,
and if the next real token is not a parenthesis cpplib needs to be
able to back up that one token as well as retain the information in
any intervening padding tokens.

Backing up more than one token when macros are involved is not
permitted by cpplib, because in general it might involve issues like
restoring popped contexts onto the context stack, which are too hard.
Instead, searching for the parenthesis is handled by a special
function, `funlike_invocation_p`, which remembers padding
information as it reads tokens. If the next real token is not an
opening parenthesis, it backs up that one token, and then pushes an
extra context just containing the padding information if necessary.

### Marking tokens ineligible for future expansion

As discussed above, cpplib needs a way of marking tokens as
unexpandable. Since the tokens cpplib handles are read-only once they
have been lexed, it instead makes a copy of the token and adds the
flag `NO_EXPAND` to the copy.

For efficiency and to simplify memory management by avoiding having to
remember to free these tokens, they are allocated as temporary tokens
from the lexer's current token run (see [Lexing a line](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Lexing-a-line.html#Lexing-a-line)) using the
function `_cpp_temp_token`. The tokens are then re-used once the
current line of tokens has been read in.

This might sound unsafe. However, tokens runs are not re-used at the
end of a line if it happens to be in the middle of a macro argument
list, and cpplib only wants to back-up more than one lexer token in
situations where no macro expansion is involved, so the optimization
is safe.
