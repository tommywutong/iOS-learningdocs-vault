---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_27.html
archived_at: '2026-07-15T07:31:03.411413Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Annotations.md), [next](Command%20Line%20Editing.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Reporting Bugs in GDB](Debugging%20with%20GDB.md#apple-krhugmrwgy)

Your bug reports play an essential role in making GDB reliable.

Reporting a bug may help you by bringing a solution to your problem, or it
may not. But in any case the principal function of a bug report is to help
the entire community by making the next version of GDB work better. Bug
reports are your contribution to the maintenance of GDB.

In order for a bug report to serve its purpose, you must include the
information that enables us to fix the bug.

## [Have you found a bug?](Debugging%20with%20GDB.md#apple-krhugmrwg4)

If you are not sure whether you have found a bug, here are some guidelines:

- 

  If the debugger gets a fatal signal, for any input whatever, that is a
  GDB bug. Reliable debuggers never crash.
  
- If GDB produces an error message for valid input, that is a
  bug. (Note that if you're cross debugging, the problem may also be
  somewhere in the connection to the target.)
  
- If GDB does not produce an error message for invalid input,
  that is a bug. However, you should note that your idea of
  "invalid input" might be our idea of "an extension" or "support
  for traditional practice".
- If you are an experienced user of debugging tools, your suggestions
  for improvement of GDB are welcome in any case.

## [How to report bugs](Debugging%20with%20GDB.md#apple-krhugmrwha)

A number of companies and individuals offer support for GNU products.
If you obtained GDB from a support organization, we recommend you
contact that organization first.

You can find contact information for many support companies and
individuals in the file `etc/SERVICE' in the GNU Emacs
distribution.

In any event, we also recommend that you submit bug reports for
GDB. The prefered method is to submit them directly using
@uref{http://www.gnu.org/software/gdb/bugs/, GDB's Bugs web
page}. Alternatively, the @email{bug-gdb@gnu.org, e-mail gateway} can
be used.

__Do not send bug reports to `` `info-gdb' ``, or to
`` `help-gdb' ``, or to any newsgroups.__ Most users of GDB do
not want to receive bug reports. Those that do have arranged to receive
`` `bug-gdb' ``.

The mailing list `` `bug-gdb' `` has a newsgroup `` `gnu.gdb.bug' `` which
serves as a repeater. The mailing list and the newsgroup carry exactly
the same messages. Often people think of posting bug reports to the
newsgroup instead of mailing them. This appears to work, but it has one
problem which can be crucial: a newsgroup posting often lacks a mail
path back to the sender. Thus, if we need to ask for more information,
we may be unable to reach you. For this reason, it is better to send
bug reports to the mailing list.

The fundamental principle of reporting bugs usefully is this:
__report all the facts__. If you are not sure whether to state a
fact or leave it out, state it!

Often people omit facts because they think they know what causes the
problem and assume that some details do not matter. Thus, you might
assume that the name of the variable you use in an example does not matter.
Well, probably it does not, but one cannot be sure. Perhaps the bug is a
stray memory reference which happens to fetch from the location where that
name is stored in memory; perhaps, if the name were different, the contents
of that location would fool the debugger into doing the right thing despite
the bug. Play it safe and give a specific, complete example. That is the
easiest thing for you to do, and the most helpful.

Keep in mind that the purpose of a bug report is to enable us to fix the
bug. It may be that the bug has been reported previously, but neither
you nor we can know that unless your bug report is complete and
self-contained.

Sometimes people give a few sketchy facts and ask, "Does this ring a
bell?" Those bug reports are useless, and we urge everyone to
_refuse to respond to them_ except to chide the sender to report
bugs properly.

To enable us to fix the bug, you should include all these things:

- The version of GDB. GDB announces it if you start
  with no arguments; you can also print it at any time using `show
  version`.
  Without this, we will not know whether there is any point in looking for
  the bug in the current version of GDB.
- The type of machine you are using, and the operating system name and
  version number.
- What compiler (and its version) was used to compile GDB---e.g.
  "gcc--2.8.1".
- What compiler (and its version) was used to compile the program you are
  debugging--e.g. "gcc--2.8.1", or "HP92453-01 A.10.32.03 HP
  C Compiler". For GCC, you can say `gcc --version` to get this
  information; for other compilers, see the documentation for those
  compilers.
- The command arguments you gave the compiler to compile your example and
  observe the bug. For example, did you use `` `-O' ``? To guarantee
  you will not omit something important, list them all. A copy of the
  Makefile (or the output from make) is sufficient.
  If we were to try to guess the arguments, we would probably guess wrong
  and then we might not encounter the bug.
- A complete input script, and all necessary source files, that will
  reproduce the bug.
- A description of what behavior you observe that you believe is
  incorrect. For example, "It gets a fatal signal."
  Of course, if the bug is that GDB gets a fatal signal, then we
  will certainly notice it. But if the bug is incorrect output, we might
  not notice unless it is glaringly wrong. You might as well not give us
  a chance to make a mistake.
  Even if the problem you experience is a fatal signal, you should still
  say so explicitly. Suppose something strange is going on, such as, your
  copy of GDB is out of synch, or you have encountered a bug in
  the C library on your system. (This has happened!) Your copy might
  crash and ours would not. If you told us to expect a crash, then when
  ours fails to crash, we would know that the bug was not happening for
  us. If you had not told us to expect a crash, then we would not be able
  to draw any conclusion from our observations.

  To collect all this information, you can use a session recording program
  such as @command{script}, which is available on many Unix systems.
  Just run your GDB session inside @command{script} and then
  include the `typescript' file with your bug report.
  Another way to record a GDB session is to run GDB
  inside Emacs and then save the entire buffer to a file.
- If you wish to suggest changes to the GDB source, send us context
  diffs. If you even discuss something in the GDB source, refer to
  it by context, not by line number.
  The line numbers in our development sources will not match those in your
  sources. Your line numbers would convey no useful information to us.

Here are some things that are not necessary:

- A description of the envelope of the bug.
  Often people who encounter a bug spend a lot of time investigating
  which changes to the input file will make the bug go away and which
  changes will not affect it.
  This is often time consuming and not very useful, because the way we
  will find the bug is by running a single example under the debugger
  with breakpoints, not by pure deduction from a series of examples.
  We recommend that you save your time for something else.
  Of course, if you can find a simpler example to report _instead_
  of the original one, that is a convenience for us. Errors in the
  output will be easier to spot, running under the debugger will take
  less time, and so on.
  However, simplification is not vital; if you do not want to do this,
  report the bug anyway and send us the entire test case you used.
- A patch for the bug.
  A patch for the bug does help us if it is a good one. But do not omit
  the necessary information, such as the test case, on the assumption that
  a patch is all we need. We might see problems with your patch and decide
  to fix the problem another way, or we might not understand it at all.
  Sometimes with a program as complicated as GDB it is very hard to
  construct an example that will make the program follow a certain path
  through the code. If you do not send us the example, we will not be able
  to construct one, so we will not be able to verify that the bug is fixed.
  And if we cannot understand what bug you are trying to fix, or why your
  patch should be an improvement, we will not install it. A test case will
  help us to understand.
- A guess about what the bug is or what it depends on.
  Such guesses are usually wrong. Even we cannot guess right about such
  things without first using the debugger to find the facts.

---

Go to the [first](Summary%20of%20GDB.md), [previous](GDB%20Annotations.md), [next](Command%20Line%20Editing.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
