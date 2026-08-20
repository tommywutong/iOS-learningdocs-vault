---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Man-Page-Generation.html
archived_at: '2026-07-15T07:31:02.369607Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Miscellaneous Docs](Miscellaneous-Docs.md#apple-jvuxgy3fnrwgc3tfn52xglken5rxg),
Previous: [Texinfo Manuals](Texinfo-Manuals.md#apple-krsxq2lomzxs2tlbnz2wc3dt),
Up: [Documentation](Documentation.md#apple-irxwg5lnmvxhiylunfxw4)

---

##### 6.3.7.2 Man Page Generation

Because of user demand, in addition to full Texinfo manuals, man pages
are provided which contain extracts from those manuals. These man
pages are generated from the Texinfo manuals using
`contrib/texi2pod.pl` and `pod2man`. (The man page for
`g++`, `cp/g++.1`, just contains a ``.so`' reference
to `gcc.1`, but all the other man pages are generated from
Texinfo manuals.)

Because many systems may not have the necessary tools installed to
generate the man pages, they are only generated if the
`configure` script detects that recent enough tools are
installed, and the Makefiles allow generating man pages to fail
without aborting the build. Man pages are also included in release
distributions. They are generated in the source directory.

Magic comments in Texinfo files starting ``@c man`' control what
parts of a Texinfo file go into a man page. Only a subset of Texinfo
is supported by `texi2pod.pl`, and it may be necessary to add
support for more Texinfo features to this script when generating new
man pages. To improve the man page output, some special Texinfo
macros are provided in `doc/include/gcc-common.texi` which
`texi2pod.pl` understands:

**`@gcctabopt`**
: Use in the form ``@table @gcctabopt`' for tables of options,
where for printed output the effect of ``@code`' is better than
that of ``@option`' but for man page output a different effect is
wanted.

**`@gccoptlist`**
: Use for summary lists of options in manuals.

**`@gol`**
: Use at the end of each line inside ``@gccoptlist`'. This is
necessary to avoid problems with differences in how the
``@gccoptlist`' macro is handled by different Texinfo formatters.

FIXME: describe the `texi2pod.pl` input language and magic
comments in more detail.
