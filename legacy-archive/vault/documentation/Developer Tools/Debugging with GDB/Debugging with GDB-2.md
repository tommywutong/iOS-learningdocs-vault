---
title: Debugging with GDB
apple_id: TP40000996
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdb/gdb_foot.html
archived_at: '2026-07-15T07:31:03.678052Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Debugging with GDB](Debugging%20with%20GDB.md)


# Debugging with GDB

## The GNU Source-Level Debugger

## Ninth Edition, for GDB version 6.3.50.20050815-cvs

Richard Stallman, Roland Pesch, Stan Shebs, et al.

---

### [(1)](Getting%20In%20and%20Out%20of%20GDB.md#apple-irhugrrr)

On
DOS/Windows systems, the home directory is the one pointed to by the
`HOME` environment variable.

### [(2)](Examining%20the%20Stack.md#apple-irhugrrs)

Note that embedded programs (the so-called "free-standing"
environment) are not required to have a `main` function as the
entry point. They could even have multiple entry points.

### [(3)](Examining%20Source%20Files.md#apple-irhugrrt)

The only restriction is that your editor (say `ex`), recognizes the
following command-line syntax:

```
ex +number file
```

The optional numeric value +number specifies the number of the line in
the file where to start editing.

### [(4)](Examining%20Data.md#apple-irhugrru)

`` `b' `` cannot be used because these format letters are also
used with the `x` command, where `` `b' `` stands for "byte";
see section [Examining memory](Examining%20Data.md#apple-kncugnrr).

### [(5)](Examining%20Data.md#apple-irhugrrv)

This is a way of removing
one word from the stack, on machines where stacks grow downward in
memory (most machines, nowadays). This assumes that the innermost
stack frame is selected; setting `$sp` is not allowed when other
stack frames are selected. To pop entire frames off the stack,
regardless of machine architecture, use `return`;
see section [Returning from a function](Altering%20Execution.md#apple-kncugmjugm).

### [(6)](Debugging%20remote%20programs.md#apple-irhugrrw)

If you choose a port number that
conflicts with another service, `gdbserver` prints an error message
and exits.

### [(7)](Formatting%20Documentation.md#apple-irhugrrx)

In
`gdb-6.3.50.20050815-cvs/gdb/refcard.ps' of the version 6.3.50.20050815-cvs
release.

### [(8)](Installing%20GDB.md#apple-irhugrry)

If you have a more recent version of GDB than 6.3.50.20050815-cvs,
look at the `README' file in the sources; we may have improved the
installation procedures since publishing this manual.

---

This document was generated on 18 May 2008 using the
[texi2html](http://wwwcn.cern.ch/dci/texi2html/)
translator version 1.51.
