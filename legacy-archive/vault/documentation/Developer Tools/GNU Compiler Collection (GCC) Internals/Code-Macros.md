---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Code-Macros.html
archived_at: '2026-07-15T07:30:59.374340Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Mode Macros](Mode-Macros.md#apple-jvxwizjnjvqwg4tpom),
Up: [Macros](Macros.md#apple-jvqwg4tpom)

---

#### 12.22.2 Code Macros

Code macros operate in a similar way to mode macros. See [Mode Macros](Mode-Macros.md#apple-jvxwizjnjvqwg4tpom).

The construct:

```
     (define_code_macro name [(code1 "cond1") ... (coden "condn")])
```

defines a pseudo rtx code name that can be instantiated as
codei if condition condi is true. Each codei
must have the same rtx format. See [RTL Classes](RTL-Classes.md#apple-kjkeylkdnrqxg43fom).

As with mode macros, each pattern that uses name will be
expanded n times, once with all uses of name replaced by
code1, once with all uses replaced by code2, and so on.
See [Defining Mode Macros](Defining-Mode-Macros.md#apple-irswm2lonfxgolknn5sgklknmfrxe33t).

It is possible to define attributes for codes as well as for modes.
There are two standard code attributes: `code`, the name of the
code in lower case, and `CODE`, the name of the code in upper case.
Other attributes are defined using:

```
     (define_code_attr name [(code1 "value1") ... (coden "valuen")])
```

Here's an example of code macros in action, taken from the MIPS port:

```
     (define_code_macro any_cond [unordered ordered unlt unge uneq ltgt unle ungt
                                  eq ne gt ge lt le gtu geu ltu leu])

     (define_expand "b<code>"
       [(set (pc)
             (if_then_else (any_cond:CC (cc0)
                                        (const_int 0))
                           (label_ref (match_operand 0 ""))
                           (pc)))]
       ""
     {
       gen_conditional_branch (operands, <CODE>);
       DONE;
     })
```

This is equivalent to:

```
     (define_expand "bunordered"
       [(set (pc)
             (if_then_else (unordered:CC (cc0)
                                         (const_int 0))
                           (label_ref (match_operand 0 ""))
                           (pc)))]
       ""
     {
       gen_conditional_branch (operands, UNORDERED);
       DONE;
     })

     (define_expand "bordered"
       [(set (pc)
             (if_then_else (ordered:CC (cc0)
                                       (const_int 0))
                           (label_ref (match_operand 0 ""))
                           (pc)))]
       ""
     {
       gen_conditional_branch (operands, ORDERED);
       DONE;
     })

     ...
```
