---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_18.html
archived_at: '2026-07-15T07:31:03.765818Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Testsuite.md), [next](GDB%20Currently%20available%20observers.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Hints](GDB%20Internals.md#apple-krhugmjvga)

Check the `README' file, it often has useful information that does not
appear anywhere else in the directory.

## [Getting Started](GDB%20Internals.md#apple-krhugmjvge)

GDB is a large and complicated program, and if you first starting to
work on it, it can be hard to know where to start. Fortunately, if you
know how to go about it, there are ways to figure out what is going on.

This manual, the GDB Internals manual, has information which applies
generally to many parts of GDB.

Information about particular functions or data structures are located in
comments with those functions or data structures. If you run across a
function or a global variable which does not have a comment correctly
explaining what is does, this can be thought of as a bug in GDB; feel
free to submit a bug report, with a suggested comment if you can figure
out what the comment should say. If you find a comment which is
actually wrong, be especially sure to report that.

Comments explaining the function of macros defined in host, target, or
native dependent files can be in several places. Sometimes they are
repeated every place the macro is defined. Sometimes they are where the
macro is used. Sometimes there is a header file which supplies a
default definition of the macro, and the comment is there. This manual
also documents all the available macros.

Start with the header files. Once you have some idea of how
GDB's internal symbol tables are stored (see `symtab.h',
`gdbtypes.h'), you will find it much easier to understand the
code which uses and creates those symbol tables.

You may wish to process the information you are getting somehow, to
enhance your understanding of it. Summarize it, translate it to another
language, add some (perhaps trivial or non-useful) feature to GDB, use
the code to predict what a test case would do and write the test case
and verify your prediction, etc. If you are reading code and your eyes
are starting to glaze over, this is a sign you need to use a more active
approach.

Once you have a part of GDB to start with, you can find more
specifically the part you are looking for by stepping through each
function with the `next` command. Do not use `step` or you
will quickly get distracted; when the function you are stepping through
calls another function try only to get a big-picture understanding
(perhaps using the comment at the beginning of the function being
called) of what it does. This way you can identify which of the
functions being called by the function you are stepping through is the
one which you are interested in. You may need to examine the data
structures generated at each stage, with reference to the comments in
the header files explaining what the data structures are supposed to
look like.

Of course, this same technique can be used if you are just reading the
code, rather than actually stepping through it. The same general
principle applies--when the code you are looking at calls something
else, just try to understand generally what the code being called does,
rather than worrying about all its details.

A good place to start when tracking down some particular area is with
a command which invokes that feature. Suppose you want to know how
single-stepping works. As a GDB user, you know that the
`step` command invokes single-stepping. The command is invoked
via command tables (see `command.h'); by convention the function
which actually performs the command is formed by taking the name of
the command and adding `` `_command' ``, or in the case of an
`info` subcommand, `` `_info' ``. For example, the `step`
command invokes the `step_command` function and the `info
display` command invokes `display_info`. When this convention is
not followed, you might have to use `grep` or `M-x
tags-search` in emacs, or run GDB on itself and set a
breakpoint in `execute_command`.

If all of the above fail, it may be appropriate to ask for information
on `bug-gdb`. But _never_ post a generic question like "I was
wondering if anyone could give me some tips about understanding
GDB"---if we had some magic secret we would put it in this manual.
Suggestions for improving the manual are always welcome, of course.

## [Debugging GDB with itself](GDB%20Internals.md#apple-krhugmjvgi)

If GDB is limping on your machine, this is the preferred way to get it
fully functional. Be warned that in some ancient Unix systems, like
Ultrix 4.2, a program can't be running in one process while it is being
debugged in another. Rather than typing the command `./gdb
./gdb`, which works on Suns and such, you can copy `gdb' to
`gdb2' and then type `./gdb ./gdb2`.

When you run GDB in the GDB source directory, it will read a
`.gdbinit' file that sets up some simple things to make debugging
gdb easier. The `info` command, when executed without a subcommand
in a GDB being debugged by gdb, will pop you back up to the top level
gdb. See `.gdbinit' for details.

If you use emacs, you will probably want to do a `make TAGS` after
you configure your distribution; this will put the machine dependent
routines for your local machine where they will be accessed first by
`M-.`

Also, make sure that you've either compiled GDB with your local cc, or
have run `fixincludes` if you are compiling with gcc.

## [Submitting Patches](GDB%20Internals.md#apple-krhugmjvgm)

Thanks for thinking of offering your changes back to the community of
GDB users. In general we like to get well designed enhancements.
Thanks also for checking in advance about the best way to transfer the
changes.

The GDB maintainers will only install "cleanly designed" patches.
This manual summarizes what we believe to be clean design for GDB.

If the maintainers don't have time to put the patch in when it arrives,
or if there is any question about a patch, it goes into a large queue
with everyone else's patches and bug reports.

The legal issue is that to incorporate substantial changes requires a
copyright assignment from you and/or your employer, granting ownership
of the changes to the Free Software Foundation. You can get the
standard documents for doing this by sending mail to `gnu@gnu.org`
and asking for it. We recommend that people write in "All programs
owned by the Free Software Foundation" as "NAME OF PROGRAM", so that
changes in many programs (not just GDB, but GAS, Emacs, GCC,
etc) can be
contributed with only one piece of legalese pushed through the
bureaucracy and filed with the FSF. We can't start merging changes until
this paperwork is received by the FSF (their rules, which we follow
since we maintain it for them).

Technically, the easiest way to receive changes is to receive each
feature as a small context diff or unidiff, suitable for `patch`.
Each message sent to me should include the changes to C code and
header files for a single feature, plus `ChangeLog' entries for
each directory where files were modified, and diffs for any changes
needed to the manuals (`gdb/doc/gdb.texinfo' or
`gdb/doc/gdbint.texinfo'). If there are a lot of changes for a
single feature, they can be split down into multiple messages.

In this way, if we read and like the feature, we can add it to the
sources with a single patch command, do some testing, and check it in.
If you leave out the `ChangeLog', we have to write one. If you leave
out the doc, we have to puzzle out what needs documenting. Etc., etc.

The reason to send each change in a separate message is that we will not
install some of the changes. They'll be returned to you with questions
or comments. If we're doing our job correctly, the message back to you
will say what you have to fix in order to make the change acceptable.
The reason to have separate messages for separate features is so that
the acceptable changes can be installed while one or more changes are
being reworked. If multiple features are sent in a single message, we
tend to not put in the effort to sort out the acceptable changes from
the unacceptable, so none of the features get installed until all are
acceptable.

If this sounds painful or authoritarian, well, it is. But we get a lot
of bug reports and a lot of patches, and many of them don't get
installed because we don't have the time to finish the job that the bug
reporter or the contributor could have done. Patches that arrive
complete, working, and well designed, tend to get installed on the day
they arrive. The others go into a queue and get installed as time
permits, which, since the maintainers have many demands to meet, may not
be for quite some time.

Please send patches directly to
@email{gdb-patches@sources.redhat.com, the GDB maintainers}.

## [Obsolete Conditionals](GDB%20Internals.md#apple-krhugmjvgq)

Fragments of old code in GDB sometimes reference or set the following
configuration macros. They should not be used by new code, and old uses
should be removed as those parts of the debugger are otherwise touched.

**`STACK_END_ADDR`**
: This macro used to define where the end of the stack appeared, for use
in interpreting core file formats that don't record this address in the
core file itself. This information is now configured in BFD, and GDB
gets the info portably from there. The values in GDB's configuration
files should be moved into BFD configuration files (if needed there),
and deleted from all of GDB's config files.
Any `foo-xdep.c' file that references STACK_END_ADDR
is so old that it has never been converted to use BFD. Now that's old!

---

Go to the [first](Requirements.md), [previous](Testsuite.md), [next](GDB%20Currently%20available%20observers.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
