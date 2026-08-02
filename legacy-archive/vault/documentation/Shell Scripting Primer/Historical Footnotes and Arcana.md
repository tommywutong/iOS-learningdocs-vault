---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/HistoricalFootnotes/HistoricalFootnotes.html
archived_at: '2026-07-18T01:39:29.280578Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](An%20Extreme%20Example-%20The%20Monte%20Carlo%20%28Bourne%29%20Method%20for%20Pi.md)

# Historical Footnotes and Arcana

This appendix contains historical footnotes extracted from elsewhere in the document to improve readability. They appear in this appendix because although they may be of some interest, they are not critical to a general understanding of the subject.

In some early Bourne-compatible shells, the second statement below does not do what you might initially suspect:

```
STRING1="This is a test"
STRING2=$STRING1
```

Most modern Bourne shells parse the right side of the assignment statement first (including any splitting on spaces), _then_ expand the variable `$STRING1`, thus copying the complete value of `STRING1` into `STRING2`.

Some older shells, however, may do the space splitting after expanding the variable. Such shells interpret the second statement as though you had typed the following:

```
STRING2=This is a test
```

as a two-part statement: an assignment statement (`FIRST_ARGUMENT=This`) followed by a command (`is`) with two arguments (`a` and `test`).

Because there is no semicolon between the assignment and the command, the shell treats this assignment statement as an attempt to modify the environment passed to the `is` command (a technique described in [Overriding Environment Variables for Child Processes (Bourne Shell)](Shell%20Script%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzrgi)). This is clearly not what you intended to do.

For maximum compatibility, you should always write such assignment statements like this:

```
STRING1="This is a test"
STRING2="$STRING1"
```

In any Bourne shell, this is interpreted correctly as:

```
STRING2="This is a test"
```

Similarly, in modern shells, quotation marks and other special characters are parsed before expansion. Thus, quotation marks inside a variable do not affect the splitting behavior. For example:

```
FOO="\"this is\" a test"
ls $FOO
```

is equivalent to:

```
ls \"this
ls is\"
ls a
ls test
```

In older Bourne shells, however, this may be misinterpreted as:

```
ls "this is"
ls a
ls test
```

In general, it is not worth the effort to support shells with this broken splitting behavior, and it is unlikely that you will encounter them; the modern splitting behavior has been common since the mid-1990s.

[Next](Document%20Revision%20History.md)[Previous](An%20Extreme%20Example-%20The%20Monte%20Carlo%20%28Bourne%29%20Method%20for%20Pi.md)

