---
title: GNU C 4.2 Preprocessor Internals
apple_id: TP40007094
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/cppinternals/Token-Spacing.html
archived_at: '2026-07-15T07:31:01.124916Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU C 4.2 Preprocessor Internals](The%20GNU%20C%20Preprocessor%20Internals.md)



Next: [Line Numbering](Line-Numbering.md#apple-jruw4zjnjz2w2ytfojuw4zy),
Previous: [Macro Expansion](Macro-Expansion.md#apple-jvqwg4tpfvcxq4dbnzzws33o),
Up: [Top](The%20GNU%20C%20Preprocessor%20Internals.md#apple-krxxa)

---

## Token Spacing

First, consider an issue that only concerns the stand-alone
preprocessor: there needs to be a guarantee that re-reading its preprocessed
output results in an identical token stream. Without taking special
measures, this might not be the case because of macro substitution.
For example:

```
     #define PLUS +
     #define EMPTY
     #define f(x) =x=
     +PLUS -EMPTY- PLUS+ f(=)
             ==> + + - - + + = = =
     not
             ==> ++ -- ++ ===
```

One solution would be to simply insert a space between all adjacent
tokens. However, we would like to keep space insertion to a minimum,
both for aesthetic reasons and because it causes problems for people who
still try to abuse the preprocessor for things like Fortran source and
Makefiles.

For now, just notice that when tokens are added (or removed, as shown by
the `EMPTY` example) from the original lexed token stream, we need
to check for accidental token pasting. We call this paste
avoidance. Token addition and removal can only occur because of macro
expansion, but accidental pasting can occur in many places: both before
and after each macro replacement, each argument replacement, and
additionally each token created by the ``#`' and ``##`' operators.

Look at how the preprocessor gets whitespace output correct
normally. The `cpp_token` structure contains a flags byte, and one
of those flags is `PREV_WHITE`. This is flagged by the lexer, and
indicates that the token was preceded by whitespace of some form other
than a new line. The stand-alone preprocessor can use this flag to
decide whether to insert a space between tokens in the output.

Now consider the result of the following macro expansion:

```
     #define add(x, y, z) x + y +z;
     sum = add (1,2, 3);
             ==> sum = 1 + 2 +3;
```

The interesting thing here is that the tokens ``1`' and ``2`' are
output with a preceding space, and ``3`' is output without a
preceding space, but when lexed none of these tokens had that property.
Careful consideration reveals that ``1`' gets its preceding
whitespace from the space preceding ``add`' in the macro invocation,
_not_ replacement list. ``2`' gets its whitespace from the
space preceding the parameter ``y`' in the macro replacement list,
and ``3`' has no preceding space because parameter ``z`' has none
in the replacement list.

Once lexed, tokens are effectively fixed and cannot be altered, since
pointers to them might be held in many places, in particular by
in-progress macro expansions. So instead of modifying the two tokens
above, the preprocessor inserts a special token, which I call a
padding token, into the token stream to indicate that spacing of
the subsequent token is special. The preprocessor inserts padding
tokens in front of every macro expansion and expanded macro argument.
These point to a source token from which the subsequent real token
should inherit its spacing. In the above example, the source tokens are
``add`' in the macro invocation, and ``y`' and ``z`' in the
macro replacement list, respectively.

It is quite easy to get multiple padding tokens in a row, for example if
a macro's first replacement token expands straight into another macro.

```
     #define foo bar
     #define bar baz
     [foo]
             ==> [baz]
```

Here, two padding tokens are generated with sources the ``foo`' token
between the brackets, and the ``bar`' token from foo's replacement
list, respectively. Clearly the first padding token is the one to
use, so the output code should contain a rule that the first
padding token in a sequence is the one that matters.

But what if a macro expansion is left? Adjusting the above
example slightly:

```
     #define foo bar
     #define bar EMPTY baz
     #define EMPTY
     [foo] EMPTY;
             ==> [ baz] ;
```

As shown, now there should be a space before ``baz`' and the
semicolon in the output.

The rules we decided above fail for ``baz`': we generate three
padding tokens, one per macro invocation, before the token ``baz`'.
We would then have it take its spacing from the first of these, which
carries source token ``foo`' with no leading space.

It is vital that cpplib get spacing correct in these examples since any
of these macro expansions could be stringified, where spacing matters.

So, this demonstrates that not just entering macro and argument
expansions, but leaving them requires special handling too. I made
cpplib insert a padding token with a `NULL` source token when
leaving macro expansions, as well as after each replaced argument in a
macro's replacement list. It also inserts appropriate padding tokens on
either side of tokens created by the ``#`' and ``##`' operators.
I expanded the rule so that, if we see a padding token with a
`NULL` source token, _and_ that source token has no leading
space, then we behave as if we have seen no padding tokens at all. A
quick check shows this rule will then get the above example correct as
well.

Now a relationship with paste avoidance is apparent: we have to be
careful about paste avoidance in exactly the same locations we have
padding tokens in order to get white space correct. This makes
implementation of paste avoidance easy: wherever the stand-alone
preprocessor is fixing up spacing because of padding tokens, and it
turns out that no space is needed, it has to take the extra step to
check that a space is not needed after all to avoid an accidental paste.
The function `cpp_avoid_paste` advises whether a space is required
between two consecutive tokens. To avoid excessive spacing, it tries
hard to only require a space if one is likely to be necessary, but for
reasons of efficiency it is slightly conservative and might recommend a
space where one is not strictly needed.
