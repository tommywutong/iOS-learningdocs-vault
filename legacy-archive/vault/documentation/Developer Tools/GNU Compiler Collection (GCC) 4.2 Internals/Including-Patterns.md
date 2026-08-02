---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Including-Patterns.html
archived_at: '2026-07-15T07:31:02.081586Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Peephole Definitions](Peephole-Definitions.md#apple-kbswk4din5wgklkemvtgs3tjoruw63tt),
Previous: [Insn Splitting](Insn-Splitting.md#apple-jfxhg3rnknygy2luoruw4zy),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 14.17 Including Patterns in Machine Descriptions.

The `include` pattern tells the compiler tools where to
look for patterns that are in files other than in the file
`.md`. This is used only at build time and there is no preprocessing allowed.

It looks like:

```

     (include
       pathname)
```

For example:

```

     (include "filestuff")

```

Where pathname is a string that specifies the location of the file,
specifies the include file to be in `gcc/config/target/filestuff`. The
directory `gcc/config/target` is regarded as the default directory.

Machine descriptions may be split up into smaller more manageable subsections
and placed into subdirectories.

By specifying:

```

     (include "BOGUS/filestuff")

```

the include file is specified to be in `gcc/config/target/BOGUS/filestuff`.

Specifying an absolute path for the include file such as;

```

     (include "/u2/BOGUS/filestuff")

```

is permitted but is not encouraged.

#### 14.17.1 RTL Generation Tool Options for Directory Search

The `-Idir` option specifies directories to search for machine descriptions.
For example:

```

     genrecog -I/p1/abc/proc1 -I/p2/abcd/pro2 target.md

```

Add the directory dir to the head of the list of directories to be
searched for header files. This can be used to override a system machine definition
file, substituting your own version, since these directories are
searched before the default machine description file directories. If you use more than
one `-I` option, the directories are scanned in left-to-right
order; the standard default directory come after.
