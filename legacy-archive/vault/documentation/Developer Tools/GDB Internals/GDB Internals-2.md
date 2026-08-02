---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_foot.html
archived_at: '2026-07-15T07:31:03.930493Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


# GDB Internals

John Gilmore
Cygnus Solutions
Second Edition:
Stan Shebs
Cygnus Solutions

---

### [(1)](User%20Interface.md#apple-irhugrrr)

The function
cast is not portable ISO C.

### [(2)](User%20Interface.md#apple-irhugrrs)

As of this writing (April 2001),
setting verbosity level is not yet implemented, and is always returned
as zero. So calling `ui_out_message` with a verbosity
argument more than zero will cause the message to never be printed.

### [(3)](Target%20Architecture%20Definition.md#apple-irhugrrt)

Some D10V instructions are
actually pairs of 16-bit sub-instructions. However, since you can't
jump into the middle of such a pair, code addresses can only refer to
full 32 bit instructions, which is what matters in this explanation.

### [(4)](Target%20Architecture%20Definition.md#apple-irhugrru)

The
above is from the original example and uses K&R C. GDB
has since converted to ISO C but lets ignore that.

---

This document was generated on 18 May 2008 using the
[texi2html](http://wwwcn.cern.ch/dci/texi2html/)
translator version 1.51.
