---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Type-Information.html
archived_at: '2026-07-15T07:31:00.956596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Funding](Funding.md#apple-iz2w4zdjnztq),
Previous: [Header Dirs](Header-Dirs.md#apple-jbswczdfoiwui2lsom),
Up: [Top](index.md#apple-krxxa)

---

## 18 Memory Management and Type Information

GCC uses some fairly sophisticated memory management techniques, which
involve determining information about GCC's data structures from GCC's
source code and using this information to perform garbage collection and
implement precompiled headers.

A full C parser would be too complicated for this task, so a limited
subset of C is interpreted and special markers are used to determine
what parts of the source to look at. All `struct` and
`union` declarations that define data structures that are
allocated under control of the garbage collector must be marked. All
global variables that hold pointers to garbage-collected memory must
also be marked. Finally, all global variables that need to be saved
and restored by a precompiled header must be marked. (The precompiled
header mechanism can only save static variables if they're scalar.
Complex data structures must be allocated in garbage-collected memory
to be saved in a precompiled header.)

The full format of a marker is

```
     GTY (([option] [(param)], [option] [(param)] ...))
```

but in most cases no options are needed. The outer double parentheses
are still necessary, though: `GTY(())`. Markers can appear:

- In a structure definition, before the open brace;
- In a global variable declaration, after the keyword `static` or
  `extern`; and
- In a structure field definition, before the name of the field.

Here are some examples of marking simple data structures and globals.

```
     struct tag GTY(())
     {
       fields...
     };

     typedef struct tag GTY(())
     {
       fields...
     } *typename;

     static GTY(()) struct tag *list;   /* points to GC memory */
     static GTY(()) int counter;        /* save counter in a PCH */
```

The parser understands simple typedefs such as
`typedef struct` tag `*`name`;` and
`typedef int` name`;`.
These don't need to be marked.

- [GTY Options](GTY-Options.md#apple-i5kfslkpob2gs33oom): What goes inside a `GTY(())`.
- [GGC Roots](GGC-Roots.md#apple-i5duglksn5xxi4y): Making global variables GGC roots.
- [Files](Files.md#apple-izuwyzlt): How the generated files work.
