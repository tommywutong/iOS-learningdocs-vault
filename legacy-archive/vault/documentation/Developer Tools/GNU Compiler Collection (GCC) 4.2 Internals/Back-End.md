---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Back-End.html
archived_at: '2026-07-15T07:31:01.240676Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Front End](Front-End.md#apple-izzg63tufvcw4za),
Up: [gcc Directory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs)

---

#### 6.3.9 Anatomy of a Target Back End

A back end for a target architecture in GCC has the following parts:

- A directory `machine` under `gcc/config`, containing a
  machine description `machine.md` file (see [Machine Descriptions](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)), header files `machine.h` and
  `machine-protos.h` and a source file `machine.c`
  (see [Target Description Macros and Functions](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)),
  possibly a target Makefile fragment `t-machine`
  (see [The Target Makefile Fragment](Target-Fragment.md#apple-krqxez3foqwum4tbm5wwk3tu)), and maybe
  some other files. The names of these files may be changed from the
  defaults given by explicit specifications in `config.gcc`.
- If necessary, a file `machine-modes.def` in the
  `machine` directory, containing additional machine modes to
  represent condition codes. See [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi), for further details.
- An optional `machine.opt` file in the `machine`
  directory, containing a list of target-specific options. You can also
  add other option files using the `extra_options` variable in
  `config.gcc`. See [Options](Options.md#apple-j5yhi2lpnzzq).
- Entries in `config.gcc` (see [The `config.gcc` File](System-Config.md#apple-kn4xg5dfnuwug33omzuwo)) for the systems with this target
  architecture.
- Documentation in `gcc/doc/invoke.texi` for any command-line
  options supported by this target (see [Run-time Target Specification](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a)). This means both entries in the summary table
  of options and details of the individual options.
- Documentation in `gcc/doc/extend.texi` for any target-specific
  attributes supported (see [Defining target-specific uses of `__attribute__`](Target-Attributes.md#apple-krqxez3foqwuc5duojuwe5lumvzq)), including where the
  same attribute is already supported on some targets, which are
  enumerated in the manual.
- Documentation in `gcc/doc/extend.texi` for any target-specific
  pragmas supported.
- Documentation in `gcc/doc/extend.texi` of any target-specific
  built-in functions supported.
- Documentation in `gcc/doc/extend.texi` of any target-specific
  format checking styles supported.
- Documentation in `gcc/doc/md.texi` of any target-specific
  constraint letters (see [Constraints for Particular Machines](Machine-Constraints.md#apple-jvqwg2djnzss2q3pnzzxi4tbnfxhi4y)).
- A note in `gcc/doc/contrib.texi` under the person or people who
  contributed the target support.
- Entries in `gcc/doc/install.texi` for all target triplets
  supported with this target architecture, giving details of any special
  notes about installation for this target, or saying that there are no
  special notes if there are none.
- Possibly other support outside the `gcc` directory for runtime
  libraries. FIXME: reference docs for this. The libstdc++ porting
  manual needs to be installed as info for this to work, or to be a
  chapter of this manual.

If the back end is added to the official GCC CVS repository, the
following are also necessary:

- An entry for the target architecture in `readings.html` on the
  GCC web site, with any relevant links.
- Details of the properties of the back end and target architecture in
  `backends.html` on the GCC web site.
- A news item about the contribution of support for that target
  architecture, in `index.html` on the GCC web site.
- Normally, one or more maintainers of that target listed in
  `MAINTAINERS`. Some existing architectures may be unmaintained,
  but it would be unusual to add support for a target that does not have
  a maintainer when support is added.
