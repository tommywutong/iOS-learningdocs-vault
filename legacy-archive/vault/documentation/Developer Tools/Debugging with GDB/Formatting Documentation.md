---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_30.html
archived_at: '2026-07-15T07:31:03.452333Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


Go to the [first](Summary%20of%20GDB.md), [previous](Using%20History%20Interactively.md), [next](Installing%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).

---

# [Formatting Documentation](Debugging%20with%20GDB.md#apple-krhugmrzgy)

The GDB 4 release includes an already-formatted reference card, ready
for printing with PostScript or Ghostscript, in the `gdb'
subdirectory of the main source directory[(7)](Debugging%20with%20GDB-2.md#apple-izhu6vbx). If you can use PostScript or Ghostscript with your printer,
you can print the reference card immediately with `refcard.ps'.

The release also includes the source for the reference card. You
can format it, using TeX, by typing:

```
make refcard.dvi
```

The GDB reference card is designed to print in __landscape__
mode on US "letter" size paper;
that is, on a sheet 11 inches wide by 8.5 inches
high. You will need to specify this form of printing as an option to
your DVI output program.

All the documentation for GDB comes as part of the machine-readable
distribution. The documentation is written in Texinfo format, which is
a documentation system that uses a single source file to produce both
on-line information and a printed manual. You can use one of the Info
formatting commands to create the on-line version of the documentation
and TeX (or `texi2roff`) to typeset the printed version.

GDB includes an already formatted copy of the on-line Info
version of this manual in the `gdb' subdirectory. The main Info
file is `gdb-6.3.50.20050815-cvs/gdb/gdb.info', and it refers to
subordinate files matching `` `gdb.info*' `` in the same directory. If
necessary, you can print out these files, or read them with any editor;
but they are easier to read using the `info` subsystem in GNU
Emacs or the standalone `info` program, available as part of the
GNU Texinfo distribution.

If you want to format these Info files yourself, you need one of the
Info formatting programs, such as `texinfo-format-buffer` or
`makeinfo`.

If you have `makeinfo` installed, and are in the top level
GDB source directory (`gdb-6.3.50.20050815-cvs', in the case of
version 6.3.50.20050815-cvs), you can make the Info file by typing:

```
cd gdb
make gdb.info
```

If you want to typeset and print copies of this manual, you need TeX,
a program to print its DVI output files, and `texinfo.tex', the
Texinfo definitions file.

TeX is a typesetting program; it does not print files directly, but
produces output files called DVI files. To print a typeset
document, you need a program to print DVI files. If your system
has TeX installed, chances are it has such a program. The precise
command to use depends on your system; `lpr -d` is common; another
(for PostScript devices) is `dvips`. The DVI print command may
require a file name without any extension or a `` `.dvi' `` extension.

TeX also requires a macro definitions file called
`texinfo.tex'. This file tells TeX how to typeset a document
written in Texinfo format. On its own, TeX cannot either read or
typeset a Texinfo file. `texinfo.tex' is distributed with GDB
and is located in the `gdb-version-number/texinfo'
directory.

If you have TeX and a DVI printer program installed, you can
typeset and print this manual. First switch to the the `gdb'
subdirectory of the main source directory (for example, to
`gdb-6.3.50.20050815-cvs/gdb') and type:

```
make gdb.dvi
```

Then give `gdb.dvi' to your DVI printing program.

---

Go to the [first](Summary%20of%20GDB.md), [previous](Using%20History%20Interactively.md), [next](Installing%20GDB.md), [last](Index.md) section, [table of contents](Debugging%20with%20GDB.md).
