---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Defining-Predicates.html
archived_at: '2026-07-15T07:30:59.719277Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Machine-Independent Predicates](Machine_002dIndependent-Predicates.md#apple-jvqwg2djnzsv6mbqgjses3temvygk3temvxhilkqojswi2ldmf2gk4y),
Up: [Predicates](Predicates.md#apple-kbzgkzdjmnqxizlt)

---

#### 12.7.2 Defining Machine-Specific Predicates

Many machines have requirements for their operands that cannot be
expressed precisely using the generic predicates. You can define
additional predicates using `define_predicate` and
`define_special_predicate` expressions. These expressions have
three operands:

- The name of the predicate, as it will be referred to in
  `match_operand` or `match_operator` expressions.
- An RTL expression which evaluates to true if the predicate allows the
  operand op, false if it does not. This expression can only use
  the following RTL codes:

  **`MATCH_OPERAND`**
  : When written inside a predicate expression, a `MATCH_OPERAND`
  expression evaluates to true if the predicate it names would allow
  op. The operand number and constraint are ignored. Due to
  limitations in `genrecog`, you can only refer to generic
  predicates and predicates that have already been defined.

  **`MATCH_CODE`**
  : This expression has one operand, a string constant containing a
  comma-separated list of RTX code names (in lower case). It evaluates
  to true if op has any of the listed codes.

  **`MATCH_TEST`**
  : This expression has one operand, a string constant containing a C
  expression. The predicate's arguments, op and mode, are
  available with those names in the C expression. The `MATCH_TEST`
  evaluates to true if the C expression evaluates to a nonzero value.
  `MATCH_TEST` expressions must not have side effects.

  **`AND`

  **`IOR`

  **`NOT`

  **`IF_THEN_ELSE`********
  : The basic ``MATCH_`' expressions can be combined using these
  logical operators, which have the semantics of the C operators
  ``&&`', ``||`', ``!`', and ``? :`' respectively.
- An optional block of C code, which should execute
  ``return true`' if the predicate is found to match and
  ``return false`' if it does not. It must not have any side
  effects. The predicate arguments, op and mode, are
  available with those names.

  If a code block is present in a predicate definition, then the RTL
  expression must evaluate to true _and_ the code block must
  execute ``return true`' for the predicate to allow the operand.
  The RTL expression is evaluated first; do not re-check anything in the
  code block that was checked in the RTL expression.

The program `genrecog` scans `define_predicate` and
`define_special_predicate` expressions to determine which RTX
codes are possibly allowed. You should always make this explicit in
the RTL predicate expression, using `MATCH_OPERAND` and
`MATCH_CODE`.

Here is an example of a simple predicate definition, from the IA64
machine description:

```
     ;; True if op is a SYMBOL_REF which refers to the sdata section.
     (define_predicate "small_addr_symbolic_operand"
       (and (match_code "symbol_ref")
            (match_test "SYMBOL_REF_SMALL_ADDR_P (op)")))
```

And here is another, showing the use of the C block.

```
     ;; True if op is a register operand that is (or could be) a GR reg.
     (define_predicate "gr_register_operand"
       (match_operand 0 "register_operand")
     {
       unsigned int regno;
       if (GET_CODE (op) == SUBREG)
         op = SUBREG_REG (op);

       regno = REGNO (op);
       return (regno >= FIRST_PSEUDO_REGISTER || GENERAL_REGNO_P (regno));
     })
```

Predicates written with `define_predicate` automatically include
a test that mode is `VOIDmode`, or op has the same
mode as mode, or op is a `CONST_INT` or
`CONST_DOUBLE`. They do _not_ check specifically for
integer `CONST_DOUBLE`, nor do they test that the value of either
kind of constant fits in the requested mode. This is because
target-specific predicates that take constants usually have to do more
stringent value checks anyway. If you need the exact same treatment
of `CONST_INT` or `CONST_DOUBLE` that the generic predicates
provide, use a `MATCH_OPERAND` subexpression to call
`const_int_operand`, `const_double_operand`, or
`immediate_operand`.

Predicates written with `define_special_predicate` do not get any
automatic mode checks, and are treated as having special mode handling
by `genrecog`.

The program `genpreds` is responsible for generating code to
test predicates. It also writes a header file containing function
declarations for all machine-specific predicates. It is not necessary
to declare these predicates in `cpu-protos.h`.
