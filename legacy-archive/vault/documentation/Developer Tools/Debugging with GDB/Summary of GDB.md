---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_1.html
archived_at: '2026-07-15T07:31:03.178632Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the first, previous, [next](A%20Sample%20GDB%20Session.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Summary of GDB](Debugging%20with%20GDB.md#apple-krhugmi)

The purpose of a debugger such as GDB is to allow you to see what is
going on "inside" another program while it executes--or what another
program was doing at the moment it crashed. We call the other program
+"your program," or "the program being debugged."

GDB can do four main kinds of things (plus other things in support of
these) to help you catch bugs in the act:

- Start your program, specifying anything that might affect its behavior.
- Make your program stop on specified conditions.
- Examine what has happened, when your program has stopped.
- Change things in your program, so you can experiment with correcting the
  effects of one bug and go on to learn about another.

You can use GDB to debug programs written in C and C++.
For more information, see section [Supported languages](Using%20GDB%20with%20Different%20Languages.md#apple-kncugmjqg4).
For more information, see section [C and C++](Using%20GDB%20with%20Different%20Languages.md#apple-kncugmjqha).

Support for Modula-2 is partial. For information on Modula-2, see
section [Modula-2](Using%20GDB%20with%20Different%20Languages.md#apple-kncugmjsgi).

Debugging Pascal programs which use sets, subranges, file variables, or
nested functions does not currently work. GDB does not support
entering expressions, printing values, or similar features using Pascal
syntax.

GDB can be used to debug programs written in Fortran, although
it may be necessary to refer to some variables with a trailing
underscore.

GDB can be used to debug programs written in Objective-C and in
Objective-C++, using either the Apple or the GNU Objective-C
runtime.

## [Free software](Debugging%20with%20GDB.md#apple-krhugmq)

GDB is __free software__, protected by the GNU
General Public License
(GPL). The GPL gives you the freedom to copy or adapt a licensed
program--but every person getting a copy also gets with it the
freedom to modify that copy (which means that they must get access to
the source code), and the freedom to distribute further copies.
Typical software companies use copyrights to limit your freedoms; the
Free Software Foundation uses the GPL to preserve these freedoms.

Fundamentally, the General Public License is a license which says that
you have these freedoms and that you cannot take these freedoms away
from anyone else.

## [Free Software Needs Free Documentation](Debugging%20with%20GDB.md#apple-krhugmy)

The biggest deficiency in the free software community today is not in
the software--it is the lack of good free documentation that we can
include with the free software. Many of our most important
programs do not come with free reference manuals and free introductory
texts. Documentation is an essential part of any software package;
when an important free software package does not come with a free
manual and a free tutorial, that is a major gap. We have many such
gaps today.

Consider Perl, for instance. The tutorial manuals that people
normally use are non-free. How did this come about? Because the
authors of those manuals published them with restrictive terms--no
copying, no modification, source files not available--which exclude
them from the free software world.

That wasn't the first time this sort of thing happened, and it was far
from the last. Many times we have heard a GNU user eagerly describe a
manual that he is writing, his intended contribution to the community,
only to learn that he had ruined everything by signing a publication
contract to make it non-free.

Free documentation, like free software, is a matter of freedom, not
price. The problem with the non-free manual is not that publishers
charge a price for printed copies--that in itself is fine. (The Free
Software Foundation sells printed copies of manuals, too.) The
problem is the restrictions on the use of the manual. Free manuals
are available in source code form, and give you permission to copy and
modify. Non-free manuals do not allow this.

The criteria of freedom for a free manual are roughly the same as for
free software. Redistribution (including the normal kinds of
commercial redistribution) must be permitted, so that the manual can
accompany every copy of the program, both on-line and on paper.

Permission for modification of the technical content is crucial too.
When people modify the software, adding or changing features, if they
are conscientious they will change the manual too--so they can
provide accurate and clear documentation for the modified program. A
manual that leaves you no choice but to write a new manual to document
a changed version of the program is not really available to our
community.

Some kinds of limits on the way modification is handled are
acceptable. For example, requirements to preserve the original
author's copyright notice, the distribution terms, or the list of
authors, are ok. It is also no problem to require modified versions
to include notice that they were modified. Even entire sections that
may not be deleted or changed are acceptable, as long as they deal
with nontechnical topics (like this one). These kinds of restrictions
are acceptable because they don't obstruct the community's normal use
of the manual.

However, it must be possible to modify all the _technical_
content of the manual, and then distribute the result in all the usual
media, through all the usual channels. Otherwise, the restrictions
obstruct the use of the manual, it is not free, and we need another
manual to replace it.

Please spread the word about this issue. Our community continues to
lose manuals to proprietary publishing. If we spread the word that
free software needs free reference manuals and free tutorials, perhaps
the next person who wants to contribute by writing documentation will
realize, before it is too late, that only free manuals contribute to
the free software community.

If you are writing documentation, please insist on publishing it under
the GNU Free Documentation License or another free documentation
license. Remember that this decision requires your approval--you
don't have to let the publisher decide. Some commercial publishers
will use a free license if you insist, but they will not propose the
option; it is up to you to raise the issue and say firmly that this is
what you want. If the publisher you are dealing with refuses, please
try other publishers. If you're not sure whether a proposed license
is free, write to @email{licensing@gnu.org}.

You can encourage commercial publishers to sell more free, copylefted
manuals and tutorials by buying them, and particularly by buying
copies from the publishers that paid for their writing or for major
improvements. Meanwhile, try to avoid buying non-free documentation
at all. Check the distribution terms of a manual before you buy it,
and insist that whoever seeks your business must respect your freedom.
Check the history of the book, and try to reward the publishers that
have paid or pay the authors to work on it.

The Free Software Foundation maintains a list of free documentation
published by other publishers, at
@url{http://www.fsf.org/doc/other-free-books.html}.

## [Contributors to GDB](Debugging%20with%20GDB.md#apple-krhugna)

Richard Stallman was the original author of GDB, and of many
other GNU programs. Many others have contributed to its
development. This section attempts to credit major contributors. One
of the virtues of free software is that everyone is free to contribute
to it; with regret, we cannot actually acknowledge everyone here. The
file `ChangeLog' in the GDB distribution approximates a
blow-by-blow account.

Changes much prior to version 2.0 are lost in the mists of time.

> _Plea:_ Additions to this section are particularly welcome. If you
> or your friends (or enemies, to be evenhanded) have been unfairly
> omitted from this list, we would like to add your names!

So that they may not regard their many labors as thankless, we
particularly thank those who shepherded GDB through major
releases:
Andrew Cagney (releases 6.1, 6.0, 5.3, 5.2, 5.1 and 5.0);
Jim Blandy (release 4.18);
Jason Molenda (release 4.17);
Stan Shebs (release 4.14);
Fred Fish (releases 4.16, 4.15, 4.13, 4.12, 4.11, 4.10, and 4.9);
Stu Grossman and John Gilmore (releases 4.8, 4.7, 4.6, 4.5, and 4.4);
John Gilmore (releases 4.3, 4.2, 4.1, 4.0, and 3.9);
Jim Kingdon (releases 3.5, 3.4, and 3.3);
and Randy Smith (releases 3.2, 3.1, and 3.0).

Richard Stallman, assisted at various times by Peter TerMaat, Chris
Hanson, and Richard Mlynarik, handled releases through 2.8.

Michael Tiemann is the author of most of the GNU C++ support
in GDB, with significant additional contributions from Per
Bothner and Daniel Berlin. James Clark wrote the GNU C++
demangler. Early work on C++ was by Peter TerMaat (who also did
much general update work leading to release 3.0).

GDB uses the BFD subroutine library to examine multiple
object-file formats; BFD was a joint project of David V.
Henkel-Wallace, Rich Pixley, Steve Chamberlain, and John Gilmore.

David Johnson wrote the original COFF support; Pace Willison did
the original support for encapsulated COFF.

Brent Benson of Harris Computer Systems contributed DWARF 2 support.

Adam de Boor and Bradley Davis contributed the ISI Optimum V support.
Per Bothner, Noboyuki Hikichi, and Alessandro Forin contributed MIPS
support.
Jean-Daniel Fekete contributed Sun 386i support.
Chris Hanson improved the HP9000 support.
Noboyuki Hikichi and Tomoyuki Hasei contributed Sony/News OS 3 support.
David Johnson contributed Encore Umax support.
Jyrki Kuoppala contributed Altos 3068 support.
Jeff Law contributed HP PA and SOM support.
Keith Packard contributed NS32K support.
Doug Rabson contributed Acorn Risc Machine support.
Bob Rusk contributed Harris Nighthawk CX-UX support.
Chris Smith contributed Convex support (and Fortran debugging).
Jonathan Stone contributed Pyramid support.
Michael Tiemann contributed SPARC support.
Tim Tucker contributed support for the Gould NP1 and Gould Powernode.
Pace Willison contributed Intel 386 support.
Jay Vosburgh contributed Symmetry support.
Marko Mlinar contributed OpenRISC 1000 support.

Andreas Schwab contributed M68K GNU/Linux support.

Rich Schaefer and Peter Schauer helped with support of SunOS shared
libraries.

Jay Fenlason and Roland McGrath ensured that GDB and GAS agree
about several machine instruction sets.

Patrick Duval, Ted Goldstein, Vikram Koka and Glenn Engel helped develop
remote debugging. Intel Corporation, Wind River Systems, AMD, and ARM
contributed remote debugging modules for the i960, VxWorks, A29K UDI,
and RDI targets, respectively.

Brian Fox is the author of the readline libraries providing
command-line editing and command history.

Andrew Beers of SUNY Buffalo wrote the language-switching code, the
Modula-2 support, and contributed the Languages chapter of this manual.

Fred Fish wrote most of the support for Unix System Vr4.
He also enhanced the command-completion support to cover C++ overloaded
symbols.

Hitachi America (now Renesas America), Ltd. sponsored the support for
H8/300, H8/500, and Super-H processors.

NEC sponsored the support for the v850, Vr4xxx, and Vr5xxx processors.

Mitsubishi (now Renesas) sponsored the support for D10V, D30V, and M32R/D
processors.

Toshiba sponsored the support for the TX39 Mips processor.

Matsushita sponsored the support for the MN10200 and MN10300 processors.

Fujitsu sponsored the support for SPARClite and FR30 processors.

Kung Hsu, Jeff Law, and Rick Sladkey added support for hardware
watchpoints.

Michael Snyder added support for tracepoints.

Stu Grossman wrote gdbserver.

Jim Kingdon, Peter Schauer, Ian Taylor, and Stu Grossman made
nearly innumerable bug fixes and cleanups throughout GDB.

The following people at the Hewlett-Packard Company contributed
support for the PA-RISC 2.0 architecture, HP-UX 10.20, 10.30, and 11.0
(narrow mode), HP's implementation of kernel threads, HP's aC++
compiler, and the Text User Interface (nee Terminal User Interface):
Ben Krepp, Richard Title, John Bishop, Susan Macchia, Kathy Mann,
Satish Pai, India Paul, Steve Rehrauer, and Elena Zannoni. Kim Haase
provided HP-specific information in this manual.

DJ Delorie ported GDB to MS-DOS, for the DJGPP project.
Robert Hoehne made significant contributions to the DJGPP port.

Cygnus Solutions has sponsored GDB maintenance and much of its
development since 1991. Cygnus engineers who have worked on GDB
fulltime include Mark Alexander, Jim Blandy, Per Bothner, Kevin
Buettner, Edith Epstein, Chris Faylor, Fred Fish, Martin Hunt, Jim
Ingham, John Gilmore, Stu Grossman, Kung Hsu, Jim Kingdon, John Metzler,
Fernando Nasser, Geoffrey Noer, Dawn Perchik, Rich Pixley, Zdenek
Radouch, Keith Seitz, Stan Shebs, David Taylor, and Elena Zannoni. In
addition, Dave Brolley, Ian Carmichael, Steve Chamberlain, Nick Clifton,
JT Conklin, Stan Cox, DJ Delorie, Ulrich Drepper, Frank Eigler, Doug
Evans, Sean Fagan, David Henkel-Wallace, Richard Henderson, Jeff
Holcomb, Jeff Law, Jim Lemke, Tom Lord, Bob Manson, Michael Meissner,
Jason Merrill, Catherine Moore, Drew Moseley, Ken Raeburn, Gavin
Romig-Koch, Rob Savoye, Jamie Smith, Mike Stump, Ian Taylor, Angela
Thomas, Michael Tiemann, Tom Tromey, Ron Unrau, Jim Wilson, and David
Zuhn have made contributions both large and small.

Andrew Cagney, Fernando Nasser, and Elena Zannoni, while working for
Cygnus Solutions, implemented the original GDB/MI interface.

Jim Blandy added support for preprocessor macros, while working for Red
Hat.

Andrew Cagney designed GDB's architecture vector. Many
people including Andrew Cagney, Stephane Carrez, Randolph Chung, Nick
Duffek, Richard Henderson, Mark Kettenis, Grace Sainsbury, Kei
Sakamoto, Yoshinori Sato, Michael Snyder, Andreas Schwab, Jason
Thorpe, Corinna Vinschen, Ulrich Weigand, and Elena Zannoni, helped
with the migration of old architectures to this new framework.

---

Go to the first, previous, [next](A%20Sample%20GDB%20Session.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
