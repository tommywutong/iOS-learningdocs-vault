---
title: GDB Internals
apple_id: TP40001009
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gdb/gdbint/gdbint_14.html
archived_at: '2026-07-15T07:31:03.735692Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GDB Internals](GDB%20Internals.md)


Go to the [first](Requirements.md), [previous](Coding.md), [next](Versions%20and%20Branches.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).

---

# [Porting GDB](GDB%20Internals.md#apple-krhugmjsgm)

Most of the work in making GDB compile on a new machine is in
specifying the configuration of the machine. This is done in a
dizzying variety of header files and configuration scripts, which we
hope to make more sensible soon. Let's say your new host is called an
xyz (e.g., `` `sun4' ``), and its full three-part configuration
name is `arch-xvend-xos` (e.g.,
`` `sparc-sun-sunos4' ``). In particular:

- In the top level directory, edit `config.sub' and add arch,
  xvend, and xos to the lists of supported architectures,
  vendors, and operating systems near the bottom of the file. Also, add
  xyz as an alias that maps to
  `arch-xvend-xos`. You can test your changes by
  running

  ```
  ./config.sub xyz
  ```

  and

  ```
  ./config.sub arch-xvend-xos
  ```

  which should both respond with `arch-xvend-xos`
  and no error messages.
  You need to port BFD, if that hasn't been done already. Porting BFD is
  beyond the scope of this manual.
- To configure GDB itself, edit `gdb/configure.host' to recognize
  your system and set `gdb_host` to xyz, and (unless your
  desired target is already available) also edit `gdb/configure.tgt',
  setting `gdb_target` to something appropriate (for instance,
  xyz).
  _Maintainer's note: Work in progress. The file
  `gdb/configure.host' originally needed to be modified when either a
  new native target or a new host machine was being added to GDB.
  Recent changes have removed this requirement. The file now only needs
  to be modified when adding a new native configuration. This will likely
  changed again in the future._
- Finally, you'll need to specify and define GDB's host-, native-, and
  target-dependent `.h' and `.c' files used for your
  configuration.

---

Go to the [first](Requirements.md), [previous](Coding.md), [next](Versions%20and%20Branches.md), [last](Index.md) section, [table of contents](GDB%20Internals.md).
