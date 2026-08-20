---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_29.html
archived_at: '2026-07-15T07:31:03.435211Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Command%20Line%20Editing.md), [next](Formatting%20Documentation.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Using History Interactively](Debugging%20with%20GDB.md#apple-krhugmrzge)

This chapter describes how to use the GNU History Library interactively,
from a user's standpoint. It should be considered a user's guide.

## [History Expansion](Debugging%20with%20GDB.md#apple-krhugmrzgi)

The History library provides a history expansion feature that is similar
to the history expansion provided by `csh`. This section
describes the syntax used to manipulate the history information.

History expansions introduce words from the history list into
the input stream, making it easy to repeat commands, insert the
arguments to a previous command into the current input line, or
fix errors in previous commands quickly.

History expansion takes place in two parts. The first is to determine
which line from the history list should be used during substitution.
The second is to select portions of that line for inclusion into the
current one. The line selected from the history is called the
__event__, and the portions of that line that are acted upon are
called __words__. Various __modifiers__ are available to manipulate
the selected words. The line is broken into words in the same fashion
that Bash does, so that several words
surrounded by quotes are considered one word.
History expansions are introduced by the appearance of the
history expansion character, which is `` `!' `` by default.

### [Event Designators](Debugging%20with%20GDB.md#apple-krhugmrzgm)

An event designator is a reference to a command line entry in the
history list.

**`!`**
: Start a history substitution, except when followed by a space, tab,
the end of the line, `` `=' `` or `` `(' ``.

**`!n`**
: Refer to command line n.

**`!-n`**
: Refer to the command n lines back.

**`!!`**
: Refer to the previous command. This is a synonym for `` `!-1' ``.

**`!string`**
: Refer to the most recent command starting with string.

**`!?string[?]`**
: Refer to the most recent command containing string. The trailing
`` `?' `` may be omitted if the string is followed immediately by
a newline.

**`^string1^string2^`**
: Quick Substitution. Repeat the last command, replacing string1
with string2. Equivalent to
`!!:s/string1/string2/`.

**`!#`**
: The entire command line typed so far.

### [Word Designators](Debugging%20with%20GDB.md#apple-krhugmrzgq)

Word designators are used to select desired words from the event.
A `` `:' `` separates the event specification from the word designator. It
may be omitted if the word designator begins with a `` `^' ``, `` `$' ``,
`` `*' ``, `` `-' ``, or `` `%' ``. Words are numbered from the beginning
of the line, with the first word being denoted by 0 (zero). Words are
inserted into the current line separated by single spaces.

For example,

**`!!`**
: designates the preceding command. When you type this, the preceding
command is repeated in toto.

**`!!:$`**
: designates the last argument of the preceding command. This may be
shortened to `!$`.

**`!fi:2`**
: designates the second argument of the most recent command starting with
the letters `fi`.

Here are the word designators:

**`0 (zero)`**
: The `0`th word. For many applications, this is the command word.

**`n`**
: The nth word.

**`^`**
: The first argument; that is, word 1.

**`$`**
: The last argument.

**`%`**
: The word matched by the most recent `` `?string?' `` search.

**`x-y`**
: A range of words; `` `-y' `` abbreviates `` `0-y' ``.

**`*`**
: All of the words, except the `0`th. This is a synonym for `` `1-$' ``.
It is not an error to use `` `*' `` if there is just one word in the event;
the empty string is returned in that case.

**`x*`**
: Abbreviates `` `x-$' ``

**`x-`**
: Abbreviates `` `x-$' `` like `` `x*' ``, but omits the last word.

If a word designator is supplied without an event specification, the
previous command is used as the event.

### [Modifiers](Debugging%20with%20GDB.md#apple-krhugmrzgu)

After the optional word designator, you can add a sequence of one or more
of the following modifiers, each preceded by a `` `:' ``.

**`h`**
: Remove a trailing pathname component, leaving only the head.

**`t`**
: Remove all leading pathname components, leaving the tail.

**`r`**
: Remove a trailing suffix of the form `` `.suffix' ``, leaving
the basename.

**`e`**
: Remove all but the trailing suffix.

**`p`**
: Print the new command but do not execute it.

**`s/old/new/`**
: Substitute new for the first occurrence of old in the
event line. Any delimiter may be used in place of `` `/' ``.
The delimiter may be quoted in old and new
with a single backslash. If `` `&' `` appears in new,
it is replaced by old. A single backslash will quote
the `` `&' ``. The final delimiter is optional if it is the last
character on the input line.

**`&`**
: Repeat the previous substitution.

**`g`**
: Cause changes to be applied over the entire event line. Used in
conjunction with `` `s' ``, as in `gs/old/new/`,
or with `` `&' ``.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Command%20Line%20Editing.md), [next](Formatting%20Documentation.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
