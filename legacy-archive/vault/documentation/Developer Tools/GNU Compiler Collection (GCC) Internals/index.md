---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/index.html
archived_at: '2026-07-15T07:31:01.052234Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


This file documents the internals of the GNU compilers.

```

```

Copyright © 1988, 1989, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
1999, 2000, 2001, 2002, 2003, 2004, 2005 Free Software Foundation, Inc.

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2 or
any later version published by the Free Software Foundation; with the
Invariant Sections being “GNU General Public License” and “Funding
Free Software”, the Front-Cover texts being (a) (see below), and with
the Back-Cover Texts being (b) (see below). A copy of the license is
included in the section entitled “GNU Free Documentation License”.

(a) The FSF's Front-Cover Text is:

A GNU Manual

(b) The FSF's Back-Cover Text is:

You have freedom to copy and modify this GNU Manual, like GNU
software. Copies published by the Free Software Foundation raise
funds for GNU development.

```

```

## Short Contents

- [Introduction](#apple-orxwgx2un5ya)
- [1 Contributing to GCC Development](#apple-orxwgx2dn5xhi4tjmj2xi2lom4)
- [2 GCC and Portability](#apple-orxwgx2qn5zhiylcnfwgs5dz)
- [3 Interfacing to GCC Output](#apple-orxwgx2jnz2gk4tgmfrwk)
- [4 The GCC low-level runtime library](#apple-orxwgx2mnfrgoy3d)
- [5 Language Front Ends in GCC](#apple-orxwgx2mmfxgo5lbm5sxg)
- [6 Source Tree Structure and Build System](#apple-orxwgx2tn52xey3ffvkhezlf)
- [7 Passes and Files of the Compiler](#apple-orxwgx2qmfzxgzlt)
- [8 Trees: The intermediate representation used by the C and C++ front ends](#apple-orxwgx2uojswk4y)
- [9 Analysis and Optimization of GIMPLE Trees](#apple-orxwgx2uojswklktknaq)
- [10 RTL Representation](#apple-orxwgx2skrga)
- [11 Control Flow Graph](#apple-orxwgx2dn5xhi4tpnqwum3dpo4)
- [12 Machine Descriptions](#apple-orxwgx2nmfrwq2lomuwuizltmm)
- [13 Target Description Macros and Functions](#apple-orxwgx2umfzgozlufvgwcy3sn5zq)
- [14 Host Configuration](#apple-orxwgx2in5zxilkdn5xgm2lh)
- [15 Makefile Fragments](#apple-orxwgx2gojqwo3lfnz2hg)
- [16 `collect2`](#apple-orxwgx2dn5wgyzldoqza)
- [17 Standard Header File Directories](#apple-orxwgx2imvqwizlsfvcgs4tt)
- [18 Memory Management and Type Information](#apple-orxwgx2upfygklkjnztg64tnmf2gs33o)
- [Funding Free Software](#apple-orxwgx2govxgi2lom4)
- [The GNU Project and GNU/Linux](#apple-orxwgx2hjzks2udsn5vgky3u)
- [GNU GENERAL PUBLIC LICENSE](#apple-orxwgx2dn5yhs2lom4)
- [GNU Free Documentation License](#apple-orxwgx2hjzks2rtsmvss2rdpmn2w2zloorqxi2lpnywuy2ldmvxhgzi)
- [Contributors to GCC](#apple-orxwgx2dn5xhi4tjmj2xi33som)
- [Option Index](#apple-orxwgx2pob2gs33ofvew4zdfpa)
- [Concept Index](#apple-orxwgx2dn5xggzlqoqwus3temv4a)

## Table of Contents

- [Introduction](#apple-krxxa)
- [1 Contributing to GCC Development](GNU%20Compiler%20Collection%20%28GCC%29%20Internals.md#apple-inxw45dsnfrhk5djnztq)
- [2 GCC and Portability](Portability.md#apple-kbxxe5dbmjuwy2lupe)
- [3 Interfacing to GCC Output](Interface.md#apple-jfxhizlsmzqwgzi)
- [4 The GCC low-level runtime library](Libgcc.md#apple-jruwez3dmm)
  - [4.1 Routines for integer arithmetic](Integer-library-routines.md#apple-jfxhizlhmvzc23djmjzgc4tzfvzg65lunfxgk4y)
    - [4.1.1 Arithmetic functions](Integer-library-routines.md#apple-jfxhizlhmvzc23djmjzgc4tzfvzg65lunfxgk4y)
    - [4.1.2 Comparison functions](Integer-library-routines.md#apple-jfxhizlhmvzc23djmjzgc4tzfvzg65lunfxgk4y)
    - [4.1.3 Trapping arithmetic functions](Integer-library-routines.md#apple-jfxhizlhmvzc23djmjzgc4tzfvzg65lunfxgk4y)
    - [4.1.4 Bit operations](Integer-library-routines.md#apple-jfxhizlhmvzc23djmjzgc4tzfvzg65lunfxgk4y)
  - [4.2 Routines for floating point emulation](Soft-float-library-routines.md#apple-knxwm5bnmzwg6ylufvwgsytsmfzhsllsn52xi2lomvzq)
    - [4.2.1 Arithmetic functions](Soft-float-library-routines.md#apple-knxwm5bnmzwg6ylufvwgsytsmfzhsllsn52xi2lomvzq)
    - [4.2.2 Conversion functions](Soft-float-library-routines.md#apple-knxwm5bnmzwg6ylufvwgsytsmfzhsllsn52xi2lomvzq)
    - [4.2.3 Comparison functions](Soft-float-library-routines.md#apple-knxwm5bnmzwg6ylufvwgsytsmfzhsllsn52xi2lomvzq)
  - [4.3 Language-independent routines for exception handling](Exception-handling-routines.md#apple-iv4ggzlqoruw63rnnbqw4zdmnfxgollsn52xi2lomvzq)
  - [4.4 Miscellaneous runtime library routines](Miscellaneous-routines.md#apple-jvuxgy3fnrwgc3tfn52xgllsn52xi2lomvzq)
    - [4.4.1 Cache control functions](Miscellaneous-routines.md#apple-jvuxgy3fnrwgc3tfn52xgllsn52xi2lomvzq)
- [5 Language Front Ends in GCC](Languages.md#apple-jrqw4z3vmftwk4y)
- [6 Source Tree Structure and Build System](Source-Tree.md#apple-knxxk4tdmuwvi4tfmu)
  - [6.1 Configure Terms and History](Configure-Terms.md#apple-inxw4ztjm52xezjnkrsxe3lt)
  - [6.2 Top Level Source Directory](Top-Level.md#apple-krxxalkmmv3gk3a)
  - [6.3 The `gcc` Subdirectory](gcc-Directory.md#apple-m5rwglkenfzgky3un5zhs)
    - [6.3.1 Subdirectories of `gcc`](Subdirectories.md#apple-kn2wezdjojswg5dpojuwk4y)
    - [6.3.2 Configuration in the `gcc` Directory](Configuration.md#apple-inxw4ztjm52xeylunfxw4)
      - [6.3.2.1 Scripts Used by `configure`](Config-Fragments.md#apple-inxw4ztjm4wum4tbm5wwk3tuom)
      - [6.3.2.2 The `config.build`; `config.host`; and `config.gcc` Files](System-Config.md#apple-kn4xg5dfnuwug33omzuwo)
      - [6.3.2.3 Files Created by `configure`](Configuration-Files.md#apple-inxw4ztjm52xeylunfxw4lkgnfwgk4y)
    - [6.3.3 Build System in the `gcc` Directory](Build.md#apple-ij2ws3de)
    - [6.3.4 Makefile Targets](Makefile.md#apple-jvqwwzlgnfwgk)
    - [6.3.5 Library Source Files and Headers under the `gcc` Directory](Library-Files.md#apple-jruwe4tboj4s2rtjnrsxg)
    - [6.3.6 Headers Installed by GCC](Headers.md#apple-jbswczdfojzq)
    - [6.3.7 Building Documentation](Documentation.md#apple-irxwg5lnmvxhiylunfxw4)
      - [6.3.7.1 Texinfo Manuals](Texinfo-Manuals.md#apple-krsxq2lomzxs2tlbnz2wc3dt)
      - [6.3.7.2 Man Page Generation](Man-Page-Generation.md#apple-jvqw4lkqmftwklkhmvxgk4tboruw63q)
      - [6.3.7.3 Miscellaneous Documentation](Miscellaneous-Docs.md#apple-jvuxgy3fnrwgc3tfn52xglken5rxg)
    - [6.3.8 Anatomy of a Language Front End](Front-End.md#apple-izzg63tufvcw4za)
      - [6.3.8.1 The Front End `language` Directory](Front-End-Directory.md#apple-izzg63tufvcw4zbniruxezldorxxe6i)
      - [6.3.8.2 The Front End `config-lang.in` File](Front-End-Config.md#apple-izzg63tufvcw4zbninxw4ztjm4)
    - [6.3.9 Anatomy of a Target Back End](Back-End.md#apple-ijqwg2znivxgi)
  - [6.4 Testsuites](Testsuites.md#apple-krsxg5dtovuxizlt)
    - [6.4.1 Idioms Used in Testsuite Code](Test-Idioms.md#apple-krsxg5bnjfsgs33nom)
    - [6.4.2 Directives used within DejaGnu tests](Test-Directives.md#apple-krsxg5bniruxezldoruxmzlt)
    - [6.4.3 Ada Language Testsuites](Ada-Tests.md#apple-ifsgclkumvzxi4y)
    - [6.4.4 C Language Testsuites](C-Tests.md#apple-imwvizltorzq)
    - [6.4.5 The Java library testsuites.](libgcj-Tests.md#apple-nruwez3dniwvizltorzq)
    - [6.4.6 Support for testing `gcov`](gcov-Testing.md#apple-m5rw65rnkrsxg5djnztq)
    - [6.4.7 Support for testing profile-directed optimizations](profopt-Testing.md#apple-obzg6ztpob2c2vdfon2gs3th)
    - [6.4.8 Support for testing binary compatibility](compat-Testing.md#apple-mnxw24dboqwvizltoruw4zy)
- [7 Passes and Files of the Compiler](Passes.md#apple-kbqxg43fom)
  - [7.1 Parsing pass](Parsing-pass.md#apple-kbqxe43jnzts24dbonzq)
  - [7.2 Gimplification pass](Gimplification-pass.md#apple-i5uw24dmnftgsy3boruw63rnobqxg4y)
  - [7.3 Pass manager](Pass-manager.md#apple-kbqxg4znnvqw4ylhmvza)
  - [7.4 Tree-SSA passes](Tree_002dSSA-passes.md#apple-krzgkzk7gaydezctknas24dbonzwk4y)
  - [7.5 RTL passes](RTL-passes.md#apple-kjkeyllqmfzxgzlt)
- [8 Trees: The intermediate representation used by the C and C++ front ends](Trees.md#apple-krzgkzlt)
  - [8.1 Deficiencies](Deficiencies.md#apple-irswm2ldnfsw4y3jmvzq)
  - [8.2 Overview](Tree-overview.md#apple-krzgkzjnn53gk4twnfsxo)
    - [8.2.1 Trees](Macros-and-Functions.md#apple-jvqwg4tpomwwc3tefvdhk3tdoruw63tt)
    - [8.2.2 Identifiers](Identifiers.md#apple-jfsgk3tunftgszlsom)
    - [8.2.3 Containers](Containers.md#apple-inxw45dbnfxgk4tt)
  - [8.3 Types](Types.md#apple-kr4xazlt)
  - [8.4 Scopes](Scopes.md#apple-knrw64dfom)
    - [8.4.1 Namespaces](Namespaces.md#apple-jzqw2zltobqwgzlt)
    - [8.4.2 Classes](Classes.md#apple-inwgc43tmvzq)
  - [8.5 Declarations](Declarations.md#apple-irswg3dbojqxi2lpnzzq)
  - [8.6 Functions](Functions.md#apple-iz2w4y3unfxw44y)
    - [8.6.1 Function Basics](Function-Basics.md#apple-iz2w4y3unfxw4lkcmfzwsy3t)
    - [8.6.2 Function Bodies](Function-Bodies.md#apple-iz2w4y3unfxw4lkcn5sgszlt)
      - [8.6.2.1 Statements](Function-Bodies.md#apple-iz2w4y3unfxw4lkcn5sgszlt)
  - [8.7 Attributes in trees](Attributes.md#apple-if2hi4tjmj2xizlt)
  - [8.8 Expressions](Expression-trees.md#apple-iv4ha4tfonzws33ofv2hezlfom)
- [9 Analysis and Optimization of GIMPLE Trees](Tree-SSA.md#apple-krzgkzjnknjuc)
  - [9.1 GENERIC](GENERIC.md#apple-i5cu4rksjfbq)
  - [9.2 GIMPLE](GIMPLE.md#apple-i5eu2ucmiu)
    - [9.2.1 Interfaces](Interfaces.md#apple-jfxhizlsmzqwgzlt)
    - [9.2.2 Temporaries](Temporaries.md#apple-krsw24dpojqxe2lfom)
    - [9.2.3 Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg)
      - [9.2.3.1 Compound Expressions](Compound-Expressions.md#apple-inxw24dpovxgilkfpbyhezltonuw63tt)
      - [9.2.3.2 Compound Lvalues](Compound-Lvalues.md#apple-inxw24dpovxgilkmozqwy5lfom)
      - [9.2.3.3 Conditional Expressions](Conditional-Expressions.md#apple-inxw4zdjoruw63tbnqwuk6dqojsxg43jn5xhg)
      - [9.2.3.4 Logical Operators](Logical-Operators.md#apple-jrxwo2ldmfwc2t3qmvzgc5dpojzq)
    - [9.2.4 Statements](Statements.md#apple-kn2gc5dfnvsw45dt)
      - [9.2.4.1 Blocks](Blocks.md#apple-ijwg6y3lom)
      - [9.2.4.2 Statement Sequences](Statement-Sequences.md#apple-kn2gc5dfnvsw45bnknsxc5lfnzrwk4y)
      - [9.2.4.3 Empty Statements](Empty-Statements.md#apple-ivwxa5dzfvjxiylumvwwk3tuom)
      - [9.2.4.4 Loops](Loops.md#apple-jrxw64dt)
      - [9.2.4.5 Selection Statements](Selection-Statements.md#apple-knswyzldoruw63rnkn2gc5dfnvsw45dt)
      - [9.2.4.6 Jumps](Jumps.md#apple-jj2w24dt)
      - [9.2.4.7 Cleanups](Cleanups.md#apple-inwgkyloovyhg)
      - [9.2.4.8 Exception Handling](GIMPLE-Exception-Handling.md#apple-i5eu2ucmiuwuk6ddmvyhi2lpnywuqylomrwgs3th)
    - [9.2.5 GIMPLE Example](GIMPLE-Example.md#apple-i5eu2ucmiuwuk6dbnvygyzi)
    - [9.2.6 Rough GIMPLE Grammar](Rough-GIMPLE-Grammar.md#apple-kjxxkz3ifvdustkqjrcs2r3smfww2yls)
  - [9.3 Annotations](Annotations.md#apple-ifxg433umf2gs33oom)
  - [9.4 Statement Operands](Statement-Operands.md#apple-kn2gc5dfnvsw45bnj5ygk4tbnzshg)
    - [9.4.1 Operand Iterators](Statement-Operands.md#apple-kn2gc5dfnvsw45bnj5ygk4tbnzshg)
  - [9.5 Static Single Assignment](SSA.md#apple-knjuc)
    - [9.5.1 Preserving the SSA form](SSA.md#apple-knjuc)
    - [9.5.2 Examining `SSA_NAME` nodes](SSA.md#apple-knjuc)
    - [9.5.3 Walking use-def chains](SSA.md#apple-knjuc)
    - [9.5.4 Walking the dominator tree](SSA.md#apple-knjuc)
  - [9.6 Alias analysis](Alias-analysis.md#apple-ifwgsyltfvqw4ylmpfzws4y)
- [10 RTL Representation](RTL.md#apple-kjkey)
  - [10.1 RTL Object Types](RTL-Objects.md#apple-kjkeylkpmjvgky3uom)
  - [10.2 RTL Classes and Formats](RTL-Classes.md#apple-kjkeylkdnrqxg43fom)
  - [10.3 Access to Operands](Accessors.md#apple-ifrwgzltonxxe4y)
  - [10.4 Access to Special Operands](Special-Accessors.md#apple-knygky3jmfwc2qldmnsxg43pojzq)
  - [10.5 Flags in an RTL Expression](Flags.md#apple-izwgcz3t)
  - [10.6 Machine Modes](Machine-Modes.md#apple-jvqwg2djnzss2tlpmrsxg)
  - [10.7 Constant Expression Types](Constants.md#apple-inxw443umfxhi4y)
  - [10.8 Registers and Memory](Regs-and-Memory.md#apple-kjswo4znmfxgilknmvww64tz)
  - [10.9 RTL Expressions for Arithmetic](Arithmetic.md#apple-ifzgs5dinvsxi2ld)
  - [10.10 Comparison Operations](Comparisons.md#apple-inxw24dbojuxg33oom)
  - [10.11 Bit-Fields](Bit_002dFields.md#apple-ijuxixzqgazgirtjmvwgi4y)
  - [10.12 Vector Operations](Vector-Operations.md#apple-kzswg5dpoiwu64dfojqxi2lpnzzq)
  - [10.13 Conversions](Conversions.md#apple-inxw45tfojzws33oom)
  - [10.14 Declarations](RTL-Declarations.md#apple-kjkeylkemvrwyylsmf2gs33oom)
  - [10.15 Side Effect Expressions](Side-Effects.md#apple-knuwizjnivtgmzldorzq)
  - [10.16 Embedded Side-Effects on Addresses](Incdec.md#apple-jfxggzdfmm)
  - [10.17 Assembler Instructions as Expressions](Assembler.md#apple-ifzxgzlnmjwgk4q)
  - [10.18 Insns](Insns.md#apple-jfxhg3tt)
  - [10.19 RTL Representation of Function-Call Insns](Calls.md#apple-inqwy3dt)
  - [10.20 Structure Sharing Assumptions](Sharing.md#apple-knugc4tjnztq)
  - [10.21 Reading RTL](Reading-RTL.md#apple-kjswczdjnzts2usujq)
- [11 Control Flow Graph](Control-Flow.md#apple-inxw45dsn5wc2rtmn53q)
  - [11.1 Basic Blocks](Basic-Blocks.md#apple-ijqxg2ldfvbgy33dnnzq)
  - [11.2 Edges](Edges.md#apple-ivsgozlt)
  - [11.3 Profile information](Profile-information.md#apple-kbzg6ztjnrss22lomzxxe3lboruw63q)
  - [11.4 Maintaining the CFG](Maintaining-the-CFG.md#apple-jvqws3tumfuw42lom4wxi2dffvbumry)
  - [11.5 Liveness information](Liveness-information.md#apple-jruxmzlomvzxglljnztg64tnmf2gs33o)
- [12 Machine Descriptions](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)
  - [12.1 Overview of How the Machine Description is Used](Overview.md#apple-j53gk4twnfsxo)
  - [12.2 Everything about Instruction Patterns](Patterns.md#apple-kbqxi5dfojxhg)
  - [12.3 Example of `define_insn`](Example.md#apple-iv4gc3lqnrsq)
  - [12.4 RTL Template](RTL-Template.md#apple-kjkeylkumvwxa3dborsq)
  - [12.5 Output Templates and Operand Substitution](Output-Template.md#apple-j52xi4dvoqwvizlnobwgc5df)
  - [12.6 C Statements for Assembler Output](Output-Statement.md#apple-j52xi4dvoqwvg5dborsw2zlooq)
  - [12.7 Predicates](Predicates.md#apple-kbzgkzdjmnqxizlt)
    - [12.7.1 Machine-Independent Predicates](Machine_002dIndependent-Predicates.md#apple-jvqwg2djnzsv6mbqgjses3temvygk3temvxhilkqojswi2ldmf2gk4y)
    - [12.7.2 Defining Machine-Specific Predicates](Defining-Predicates.md#apple-irswm2lonfxgolkqojswi2ldmf2gk4y)
  - [12.8 Operand Constraints](Constraints.md#apple-inxw443uojqws3tuom)
    - [12.8.1 Simple Constraints](Simple-Constraints.md#apple-knuw24dmmuwug33oon2heyljnz2hg)
    - [12.8.2 Multiple Alternative Constraints](Multi_002dAlternative.md#apple-jv2wy5djl4ydamteifwhizlsnzqxi2lwmu)
    - [12.8.3 Register Class Preferences](Class-Preferences.md#apple-inwgc43tfvihezlgmvzgk3tdmvzq)
    - [12.8.4 Constraint Modifier Characters](Modifiers.md#apple-jvxwi2lgnfsxe4y)
    - [12.8.5 Constraints for Particular Machines](Machine-Constraints.md#apple-jvqwg2djnzss2q3pnzzxi4tbnfxhi4y)
  - [12.9 Standard Pattern Names For Generation](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y)
  - [12.10 When the Order of Patterns Matters](Pattern-Ordering.md#apple-kbqxi5dfojxc2t3smrsxe2lom4)
  - [12.11 Interdependence of Patterns](Dependent-Patterns.md#apple-irsxazlomrsw45bnkbqxi5dfojxhg)
  - [12.12 Defining Jump Instruction Patterns](Jump-Patterns.md#apple-jj2w24bnkbqxi5dfojxhg)
  - [12.13 Defining Looping Instruction Patterns](Looping-Patterns.md#apple-jrxw64djnzts2udbor2gk4toom)
  - [12.14 Canonicalization of Instructions](Insn-Canonicalizations.md#apple-jfxhg3rninqw433onfrwc3djpjqxi2lpnzzq)
  - [12.15 Defining RTL Sequences for Code Generation](Expander-Definitions.md#apple-iv4haylomrsxelkemvtgs3tjoruw63tt)
  - [12.16 Defining How to Split Instructions](Insn-Splitting.md#apple-jfxhg3rnknygy2luoruw4zy)
  - [12.17 Including Patterns in Machine Descriptions.](Including-Patterns.md#apple-jfxgg3dvmruw4zznkbqxi5dfojxhg)
    - [12.17.1 RTL Generation Tool Options for Directory Search](Including-Patterns.md#apple-jfxgg3dvmruw4zznkbqxi5dfojxhg)
  - [12.18 Machine-Specific Peephole Optimizers](Peephole-Definitions.md#apple-kbswk4din5wgklkemvtgs3tjoruw63tt)
    - [12.18.1 RTL to Text Peephole Optimizers](define_005fpeephole.md#apple-mrswm2lomvptambvmzygkzlqnbxwyzi)
    - [12.18.2 RTL to RTL Peephole Optimizers](define_005fpeephole2.md#apple-mrswm2lomvptambvmzygkzlqnbxwyzjs)
  - [12.19 Instruction Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)
    - [12.19.1 Defining Attributes and their Values](Defining-Attributes.md#apple-irswm2lonfxgolkbor2he2lcov2gk4y)
    - [12.19.2 Attribute Expressions](Expressions.md#apple-iv4ha4tfonzws33oom)
    - [12.19.3 Assigning Attribute Values to Insns](Tagging-Insns.md#apple-krqwoz3jnzts2sloonxhg)
    - [12.19.4 Example of Attribute Specifications](Attr-Example.md#apple-if2hi4rniv4gc3lqnrsq)
    - [12.19.5 Computing the Length of an Insn](Insn-Lengths.md#apple-jfxhg3rnjrsw4z3unbzq)
    - [12.19.6 Constant Attributes](Constant-Attributes.md#apple-inxw443umfxhilkbor2he2lcov2gk4y)
    - [12.19.7 Delay Slot Scheduling](Delay-Slots.md#apple-irswyylzfvjwy33uom)
    - [12.19.8 Specifying processor pipeline description](Processor-pipeline-description.md#apple-kbzg6y3fonzw64rnobuxazlmnfxgkllemvzwg4tjob2gs33o)
  - [12.20 Conditional Execution](Conditional-Execution.md#apple-inxw4zdjoruw63tbnqwuk6dfmn2xi2lpny)
  - [12.21 Constant Definitions](Constant-Definitions.md#apple-inxw443umfxhilkemvtgs3tjoruw63tt)
  - [12.22 Macros](Macros.md#apple-jvqwg4tpom)
    - [12.22.1 Mode Macros](Mode-Macros.md#apple-jvxwizjnjvqwg4tpom)
      - [12.22.1.1 Defining Mode Macros](Defining-Mode-Macros.md#apple-irswm2lonfxgolknn5sgklknmfrxe33t)
      - [12.22.1.2 String Substitution in Mode Macros](String-Substitutions.md#apple-kn2he2lom4wvg5lcon2gs5dvoruw63tt)
      - [12.22.1.3 Mode Macro Examples](Examples.md#apple-iv4gc3lqnrsxg)
    - [12.22.2 Code Macros](Code-Macros.md#apple-inxwizjnjvqwg4tpom)
- [13 Target Description Macros and Functions](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)
  - [13.1 The Global `targetm` Variable](Target-Structure.md#apple-krqxez3foqwvg5dsovrxi5lsmu)
  - [13.2 Controlling the Compilation Driver, `gcc`](Driver.md#apple-irzgs5tfoi)
  - [13.3 Run-time Target Specification](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a)
  - [13.4 Defining data structures for per-function information.](Per_002dFunction-Data.md#apple-kbsxexzqgazgirtvnzrxi2lpnywuiylume)
  - [13.5 Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a)
  - [13.6 Layout of Source Language Data Types](Type-Layout.md#apple-kr4xazjnjrqxs33voq)
  - [13.7 Register Usage](Registers.md#apple-kjswo2ltorsxe4y)
    - [13.7.1 Basic Characteristics of Registers](Register-Basics.md#apple-kjswo2ltorsxelkcmfzwsy3t)
    - [13.7.2 Order of Allocation of Registers](Allocation-Order.md#apple-ifwgy33dmf2gs33ofvhxezdfoi)
    - [13.7.3 How Values Fit in Registers](Values-in-Registers.md#apple-kzqwy5lfomwws3rnkjswo2ltorsxe4y)
    - [13.7.4 Handling Leaf Functions](Leaf-Functions.md#apple-jrswczrniz2w4y3unfxw44y)
    - [13.7.5 Registers That Form a Stack](Stack-Registers.md#apple-kn2gcy3lfvjgkz3jon2gk4tt)
  - [13.8 Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom)
  - [13.9 Stack Layout and Calling Conventions](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)
    - [13.9.1 Basic Stack Layout](Frame-Layout.md#apple-izzgc3lffvggc6lpov2a)
    - [13.9.2 Exception Handling Support](Exception-Handling.md#apple-iv4ggzlqoruw63rnjbqw4zdmnfxgo)
    - [13.9.3 Specifying How Stack Checking is Done](Stack-Checking.md#apple-kn2gcy3lfvbwqzldnnuw4zy)
    - [13.9.4 Registers That Address the Stack Frame](Frame-Registers.md#apple-izzgc3lffvjgkz3jon2gk4tt)
    - [13.9.5 Eliminating Frame Pointer and Arg Pointer](Elimination.md#apple-ivwgs3ljnzqxi2lpny)
    - [13.9.6 Passing Function Arguments on the Stack](Stack-Arguments.md#apple-kn2gcy3lfvaxez3vnvsw45dt)
    - [13.9.7 Passing Arguments in Registers](Register-Arguments.md#apple-kjswo2ltorsxelkbojtxk3lfnz2hg)
    - [13.9.8 How Scalar Function Values Are Returned](Scalar-Return.md#apple-knrwc3dboiwvezluovzg4)
    - [13.9.9 How Large Values Are Returned](Aggregate-Return.md#apple-iftwo4tfm5qxizjnkjsxi5lsny)
    - [13.9.10 Caller-Saves Register Allocation](Caller-Saves.md#apple-inqwy3dfoiwvgylwmvzq)
    - [13.9.11 Function Entry and Exit](Function-Entry.md#apple-iz2w4y3unfxw4lkfnz2he6i)
    - [13.9.12 Generating Code for Profiling](Profiling.md#apple-kbzg6ztjnruw4zy)
    - [13.9.13 Permitting tail calls](Tail-Calls.md#apple-krqws3bninqwy3dt)
  - [13.10 Implementing the Varargs Macros](Varargs.md#apple-kzqxeylsm5zq)
  - [13.11 Trampolines for Nested Functions](Trampolines.md#apple-krzgc3lqn5wgs3tfom)
  - [13.12 Implicit Calls to Library Routines](Library-Calls.md#apple-jruwe4tboj4s2q3bnrwhg)
  - [13.13 Addressing Modes](Addressing-Modes.md#apple-ifsgi4tfonzws3thfvgw6zdfom)
  - [13.14 Condition Code Status](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi)
  - [13.15 Describing Relative Costs of Operations](Costs.md#apple-inxxg5dt)
  - [13.16 Adjusting the Instruction Scheduler](Scheduling.md#apple-knrwqzleovwgs3th)
  - [13.17 Dividing the Output into Sections (Texts, Data, ...)](Sections.md#apple-knswg5djn5xhg)
  - [13.18 Position Independent Code](PIC.md#apple-kbeug)
  - [13.19 Defining the Output Assembler Language](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)
    - [13.19.1 The Overall Framework of an Assembler File](File-Framework.md#apple-izuwyzjnizzgc3lfo5xxe2y)
    - [13.19.2 Output of Data](Data-Output.md#apple-irqxiyjnj52xi4dvoq)
    - [13.19.3 Output of Uninitialized Variables](Uninitialized-Data.md#apple-kvxgs3tjoruwc3djpjswilkemf2gc)
    - [13.19.4 Output and Generation of Labels](Label-Output.md#apple-jrqwezlmfvhxk5dqov2a)
    - [13.19.5 How Initialization Functions Are Handled](Initialization.md#apple-jfxgs5djmfwgs6tboruw63q)
    - [13.19.6 Macros Controlling Initialization Routines](Macros-for-Initialization.md#apple-jvqwg4tpomwwm33sfvew42lunfqwy2l2mf2gs33o)
    - [13.19.7 Output of Assembler Instructions](Instruction-Output.md#apple-jfxhg5dsovrxi2lpnywu65luob2xi)
    - [13.19.8 Output of Dispatch Tables](Dispatch-Tables.md#apple-iruxg4dborrwqlkumfrgyzlt)
    - [13.19.9 Assembler Commands for Exception Regions](Exception-Region-Output.md#apple-iv4ggzlqoruw63rnkjswo2lpnywu65luob2xi)
    - [13.19.10 Assembler Commands for Alignment](Alignment-Output.md#apple-ifwgsz3onvsw45bnj52xi4dvoq)
  - [13.20 Controlling Debugging Information Format](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y)
    - [13.20.1 Macros Affecting All Debugging Formats](All-Debuggers.md#apple-ifwgylkemvrhkz3hmvzhg)
    - [13.20.2 Specific Options for DBX Output](DBX-Options.md#apple-irbfqlkpob2gs33oom)
    - [13.20.3 Open-Ended Hooks for DBX Format](DBX-Hooks.md#apple-irbfqlkin5xww4y)
    - [13.20.4 File Names in DBX Format](File-Names-and-DBX.md#apple-izuwyzjnjzqw2zltfvqw4zbnirbfq)
    - [13.20.5 Macros for SDB and DWARF Output](SDB-and-DWARF.md#apple-knceellbnzsc2rcxifjem)
    - [13.20.6 Macros for VMS Debug Format](VMS-Debug.md#apple-kzgvglkemvrhkzy)
  - [13.21 Cross Compilation and Floating Point](Floating-Point.md#apple-izwg6ylunfxgolkqn5uw45a)
  - [13.22 Mode Switching Instructions](Mode-Switching.md#apple-jvxwizjnkn3ws5ddnbuw4zy)
  - [13.23 Defining target-specific uses of `__attribute__`](Target-Attributes.md#apple-krqxez3foqwuc5duojuwe5lumvzq)
  - [13.24 Defining coprocessor specifics for MIPS targets.](MIPS-Coprocessors.md#apple-jvevauzninxxa4tpmnsxg43pojzq)
  - [13.25 Parameters for Precompiled Header Validity Checking](PCH-Target.md#apple-kbbuqlkumfzgozlu)
  - [13.26 C++ ABI parameters](C_002b_002b-ABI.md#apple-inptambsmjptambsmiwucqsj)
  - [13.27 Miscellaneous Parameters](Misc.md#apple-jvuxgyy)
- [14 Host Configuration](Host-Config.md#apple-jbxxg5bninxw4ztjm4)
  - [14.1 Host Common](Host-Common.md#apple-jbxxg5bninxw23lpny)
  - [14.2 Host Filesystem](Filesystem.md#apple-izuwyzltpfzxizln)
  - [14.3 Host Misc](Host-Misc.md#apple-jbxxg5bnjvuxgyy)
- [15 Makefile Fragments](Fragments.md#apple-izzgcz3nmvxhi4y)
  - [15.1 Target Makefile Fragments](Target-Fragment.md#apple-krqxez3foqwum4tbm5wwk3tu)
  - [15.2 Host Makefile Fragments](Host-Fragment.md#apple-jbxxg5bnizzgcz3nmvxhi)
- [16 `collect2`](Collect2.md#apple-inxwy3dfmn2de)
- [17 Standard Header File Directories](Header-Dirs.md#apple-jbswczdfoiwui2lsom)
- [18 Memory Management and Type Information](Type-Information.md#apple-kr4xazjnjfxgm33snvqxi2lpny)
  - [18.1 The Inside of a `GTY(())`](GTY-Options.md#apple-i5kfslkpob2gs33oom)
  - [18.2 Marking Roots for the Garbage Collector](GGC-Roots.md#apple-i5duglksn5xxi4y)
  - [18.3 Source Files Containing Type Information](Files.md#apple-izuwyzlt)
- [Funding Free Software](Funding.md#apple-iz2w4zdjnztq)
- [The GNU Project and GNU/Linux](GNU-Project.md#apple-i5hfklkqojxwuzldoq)
- [GNU GENERAL PUBLIC LICENSE](Copying.md#apple-inxxa6ljnztq)
  - [Preamble](Copying.md#apple-inxxa6ljnztq)
  - [How to Apply These Terms to Your New Programs](Copying.md#apple-inxxa6ljnztq)
- [GNU Free Documentation License](GNU-Free-Documentation-License.md#apple-i5hfklkgojswklken5rxk3lfnz2gc5djn5xc2tdjmnsw443f)
  - [ADDENDUM: How to use this License for your documents](GNU-Free-Documentation-License.md#apple-i5hfklkgojswklken5rxk3lfnz2gc5djn5xc2tdjmnsw443f)
- [Contributors to GCC](Contributors.md#apple-inxw45dsnfrhk5dpojzq)
- [Option Index](Option-Index.md#apple-j5yhi2lpnywus3temv4a)
- [Concept Index](Concept-Index.md#apple-inxw4y3fob2c2slomrsxq)

Next: [Contributing](GNU%20Compiler%20Collection%20%28GCC%29%20Internals.md#apple-inxw45dsnfrhk5djnztq),
Up: [(DIR)](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/index.html#DIR)

---

## Introduction

This manual documents the internals of the GNU compilers, including
how to port them to new targets and some information about how to
write front ends for new languages. It corresponds to GCC version
4.0.1. The use of the GNU compilers is documented in a
separate manual. See [Introduction](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gcc/index.html#Top).

This manual is mainly a reference manual rather than a tutorial. It
discusses how to contribute to GCC (see [Contributing](GNU%20Compiler%20Collection%20%28GCC%29%20Internals.md#apple-inxw45dsnfrhk5djnztq)), the
characteristics of the machines supported by GCC as hosts and targets
(see [Portability](Portability.md#apple-kbxxe5dbmjuwy2lupe)), how GCC relates to the ABIs on such systems
(see [Interface](Interface.md#apple-jfxhizlsmzqwgzi)), and the characteristics of the languages for
which GCC front ends are written (see [Languages](Languages.md#apple-jrqw4z3vmftwk4y)). It then
describes the GCC source tree structure and build system, some of the
interfaces to GCC front ends, and how support for a target system is
implemented in GCC.

Additional tutorial information is linked to from
[http://gcc.gnu.org/readings.html](http://gcc.gnu.org/readings.html).

- [Contributing](GNU%20Compiler%20Collection%20%28GCC%29%20Internals.md#apple-inxw45dsnfrhk5djnztq): How to contribute to testing and developing GCC.
- [Portability](Portability.md#apple-kbxxe5dbmjuwy2lupe): Goals of GCC's portability features.
- [Interface](Interface.md#apple-jfxhizlsmzqwgzi): Function-call interface of GCC output.
- [Libgcc](Libgcc.md#apple-jruwez3dmm): Low-level runtime library used by GCC.
- [Languages](Languages.md#apple-jrqw4z3vmftwk4y): Languages for which GCC front ends are written.
- [Source Tree](Source-Tree.md#apple-knxxk4tdmuwvi4tfmu): GCC source tree structure and build system.
- [Passes](Passes.md#apple-kbqxg43fom): Order of passes, what they do, and what each file is for.
- [Trees](Trees.md#apple-krzgkzlt): The source representation used by the C and C++ front ends.
- [RTL](RTL.md#apple-kjkey): The intermediate representation that most passes work on.
- [Control Flow](Control-Flow.md#apple-inxw45dsn5wc2rtmn53q): Maintaining and manipulating the control flow graph.
- [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc): Analysis and optimization of the tree representation.
- [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq): How to write machine description instruction patterns.
- [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg): How to write the machine description C macros and functions.
- [Host Config](Host-Config.md#apple-jbxxg5bninxw4ztjm4): Writing the `xm-machine.h` file.
- [Fragments](Fragments.md#apple-izzgcz3nmvxhi4y): Writing the `t-target` and `x-host` files.
- [Collect2](Collect2.md#apple-inxwy3dfmn2de): How `collect2` works; how it finds `ld`.
- [Header Dirs](Header-Dirs.md#apple-jbswczdfoiwui2lsom): Understanding the standard header file directories.
- [Type Information](Type-Information.md#apple-kr4xazjnjfxgm33snvqxi2lpny): GCC's memory management; generating type information.
- [Funding](Funding.md#apple-iz2w4zdjnztq): How to help assure funding for free software.
- [GNU Project](GNU-Project.md#apple-i5hfklkqojxwuzldoq): The GNU Project and GNU/Linux.
- [Copying](Copying.md#apple-inxxa6ljnztq): GNU General Public License says
  how you can copy and share GCC.
- [GNU Free Documentation License](GNU-Free-Documentation-License.md#apple-i5hfklkgojswklken5rxk3lfnz2gc5djn5xc2tdjmnsw443f): How you can copy and share this manual.
- [Contributors](Contributors.md#apple-inxw45dsnfrhk5dpojzq): People who have contributed to GCC.
- [Option Index](Option-Index.md#apple-j5yhi2lpnywus3temv4a): Index to command line options.
- [Concept Index](Concept-Index.md#apple-inxw4y3fob2c2slomrsxq): Index of concepts and symbol names.
