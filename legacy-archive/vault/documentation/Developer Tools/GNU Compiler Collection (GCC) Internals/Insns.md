---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Insns.html
archived_at: '2026-07-15T07:31:00.097943Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Calls](Calls.md#apple-inqwy3dt),
Previous: [Assembler](Assembler.md#apple-ifzxgzlnmjwgk4q),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.18 Insns

The RTL representation of the code for a function is a doubly-linked
chain of objects called insns. Insns are expressions with
special codes that are used for no other purpose. Some insns are
actual instructions; others represent dispatch tables for `switch`
statements; others represent labels to jump to or various sorts of
declarative information.

In addition to its own specific data, each insn must have a unique
id-number that distinguishes it from all other insns in the current
function (after delayed branch scheduling, copies of an insn with the
same id-number may be present in multiple places in a function, but
these copies will always be identical and will only appear inside a
`sequence`), and chain pointers to the preceding and following
insns. These three fields occupy the same position in every insn,
independent of the expression code of the insn. They could be accessed
with `XEXP` and `XINT`, but instead three special macros are
always used:

**`INSN_UID (`i`)`**
: Accesses the unique id of insn i.

**`PREV_INSN (`i`)`**
: Accesses the chain pointer to the insn preceding i.
If i is the first insn, this is a null pointer.

**`NEXT_INSN (`i`)`**
: Accesses the chain pointer to the insn following i.
If i is the last insn, this is a null pointer.

The first insn in the chain is obtained by calling `get_insns`; the
last insn is the result of calling `get_last_insn`. Within the
chain delimited by these insns, the `NEXT_INSN` and
`PREV_INSN` pointers must always correspond: if insn is not
the first insn,

```
     NEXT_INSN (PREV_INSN (insn)) == insn
```

is always true and if insn is not the last insn,

```
     PREV_INSN (NEXT_INSN (insn)) == insn
```

is always true.

After delay slot scheduling, some of the insns in the chain might be
`sequence` expressions, which contain a vector of insns. The value
of `NEXT_INSN` in all but the last of these insns is the next insn
in the vector; the value of `NEXT_INSN` of the last insn in the vector
is the same as the value of `NEXT_INSN` for the `sequence` in
which it is contained. Similar rules apply for `PREV_INSN`.

This means that the above invariants are not necessarily true for insns
inside `sequence` expressions. Specifically, if insn is the
first insn in a `sequence`, `NEXT_INSN (PREV_INSN (`insn`))`
is the insn containing the `sequence` expression, as is the value
of `PREV_INSN (NEXT_INSN (`insn`))` if insn is the last
insn in the `sequence` expression. You can use these expressions
to find the containing `sequence` expression.

Every insn has one of the following six expression codes:

**`insn`**
: The expression code `insn` is used for instructions that do not jump
and do not do function calls. `sequence` expressions are always
contained in insns with code `insn` even if one of those insns
should jump or do function calls.

Insns with code `insn` have four additional fields beyond the three
mandatory ones listed above. These four are described in a table below.

**`jump_insn`**
: The expression code `jump_insn` is used for instructions that may
jump (or, more generally, may contain `label_ref` expressions). If
there is an instruction to return from the current function, it is
recorded as a `jump_insn`.

`jump_insn` insns have the same extra fields as `insn` insns,
accessed in the same way and in addition contain a field
`JUMP_LABEL` which is defined once jump optimization has completed.

For simple conditional and unconditional jumps, this field contains
the `code_label` to which this insn will (possibly conditionally)
branch. In a more complex jump, `JUMP_LABEL` records one of the
labels that the insn refers to; the only way to find the others is to
scan the entire body of the insn. In an `addr_vec`,
`JUMP_LABEL` is `NULL_RTX`.

Return insns count as jumps, but since they do not refer to any
labels, their `JUMP_LABEL` is `NULL_RTX`.

**`call_insn`**
: The expression code `call_insn` is used for instructions that may do
function calls. It is important to distinguish these instructions because
they imply that certain registers and memory locations may be altered
unpredictably.

`call_insn` insns have the same extra fields as `insn` insns,
accessed in the same way and in addition contain a field
`CALL_INSN_FUNCTION_USAGE`, which contains a list (chain of
`expr_list` expressions) containing `use` and `clobber`
expressions that denote hard registers and `MEM`s used or
clobbered by the called function.

A `MEM` generally points to a stack slots in which arguments passed
to the libcall by reference (see [TARGET_PASS_BY_REFERENCE](Register-Arguments.md#apple-kjswo2ltorsxelkbojtxk3lfnz2hg)) are stored. If the argument is
caller-copied (see [TARGET_CALLEE_COPIES](Register-Arguments.md#apple-kjswo2ltorsxelkbojtxk3lfnz2hg)),
the stack slot will be mentioned in `CLOBBER` and `USE`
entries; if it's callee-copied, only a `USE` will appear, and the
`MEM` may point to addresses that are not stack slots. These
`MEM`s are used only in libcalls, because, unlike regular function
calls, `CONST_CALL`s (which libcalls generally are, see [CONST_CALL_P](Flags.md#apple-izwgcz3t)) aren't assumed to read and write all memory, so flow
would consider the stores dead and remove them. Note that, since a
libcall must never return values in memory (see [RETURN_IN_MEMORY](Aggregate-Return.md#apple-iftwo4tfm5qxizjnkjsxi5lsny)), there will never be a `CLOBBER` for a memory
address holding a return value.

`CLOBBER`ed registers in this list augment registers specified in
`CALL_USED_REGISTERS` (see [Register Basics](Register-Basics.md#apple-kjswo2ltorsxelkcmfzwsy3t)).

**`code_label`**
: A `code_label` insn represents a label that a jump insn can jump
to. It contains two special fields of data in addition to the three
standard ones. `CODE_LABEL_NUMBER` is used to hold the label
number, a number that identifies this label uniquely among all the
labels in the compilation (not just in the current function).
Ultimately, the label is represented in the assembler output as an
assembler label, usually of the form ``Ln`' where n is
the label number.

When a `code_label` appears in an RTL expression, it normally
appears within a `label_ref` which represents the address of
the label, as a number.

Besides as a `code_label`, a label can also be represented as a
`note` of type `NOTE_INSN_DELETED_LABEL`.

The field `LABEL_NUSES` is only defined once the jump optimization
phase is completed. It contains the number of times this label is
referenced in the current function.

The field `LABEL_KIND` differentiates four different types of
labels: `LABEL_NORMAL`, `LABEL_STATIC_ENTRY`,
`LABEL_GLOBAL_ENTRY`, and `LABEL_WEAK_ENTRY`. The only labels
that do not have type `LABEL_NORMAL` are alternate entry
points to the current function. These may be static (visible only in
the containing translation unit), global (exposed to all translation
units), or weak (global, but can be overridden by another symbol with the
same name).

Much of the compiler treats all four kinds of label identically. Some
of it needs to know whether or not a label is an alternate entry point;
for this purpose, the macro `LABEL_ALT_ENTRY_P` is provided. It is
equivalent to testing whether ``LABEL_KIND (label) == LABEL_NORMAL`'.
The only place that cares about the distinction between static, global,
and weak alternate entry points, besides the front-end code that creates
them, is the function `output_alternate_entry_point`, in
`final.c`.

To set the kind of a label, use the `SET_LABEL_KIND` macro.

**`barrier`**
: Barriers are placed in the instruction stream when control cannot flow
past them. They are placed after unconditional jump instructions to
indicate that the jumps are unconditional and after calls to
`volatile` functions, which do not return (e.g., `exit`).
They contain no information beyond the three standard fields.

**`note`**
: `note` insns are used to represent additional debugging and
declarative information. They contain two nonstandard fields, an
integer which is accessed with the macro `NOTE_LINE_NUMBER` and a
string accessed with `NOTE_SOURCE_FILE`.

If `NOTE_LINE_NUMBER` is positive, the note represents the
position of a source line and `NOTE_SOURCE_FILE` is the source file name
that the line came from. These notes control generation of line
number data in the assembler output.

Otherwise, `NOTE_LINE_NUMBER` is not really a line number but a
code with one of the following values (and `NOTE_SOURCE_FILE`
must contain a null pointer):

**`NOTE_INSN_DELETED`**
: Such a note is completely ignorable. Some passes of the compiler
delete insns by altering them into notes of this kind.

**`NOTE_INSN_DELETED_LABEL`**
: This marks what used to be a `code_label`, but was not used for other
purposes than taking its address and was transformed to mark that no
code jumps to it.

**`NOTE_INSN_BLOCK_BEG`

**`NOTE_INSN_BLOCK_END`****
: These types of notes indicate the position of the beginning and end
of a level of scoping of variable names. They control the output
of debugging information.

**`NOTE_INSN_EH_REGION_BEG`

**`NOTE_INSN_EH_REGION_END`****
: These types of notes indicate the position of the beginning and end of a
level of scoping for exception handling. `NOTE_BLOCK_NUMBER`
identifies which `CODE_LABEL` or `note` of type
`NOTE_INSN_DELETED_LABEL` is associated with the given region.

**`NOTE_INSN_LOOP_BEG`

**`NOTE_INSN_LOOP_END`****
: These types of notes indicate the position of the beginning and end
of a `while` or `for` loop. They enable the loop optimizer
to find loops quickly.

**`NOTE_INSN_LOOP_CONT`**
: Appears at the place in a loop that `continue` statements jump to.

**`NOTE_INSN_LOOP_VTOP`**
: This note indicates the place in a loop where the exit test begins for
those loops in which the exit test has been duplicated. This position
becomes another virtual start of the loop when considering loop
invariants.

**`NOTE_INSN_FUNCTION_END`**
: Appears at the start of the function body, after the function
prologue.

**`NOTE_INSN_FUNCTION_END`**
: Appears near the end of the function body, just before the label that
`return` statements jump to (on machine where a single instruction
does not suffice for returning). This note may be deleted by jump
optimization.

**`NOTE_INSN_SETJMP`**
: Appears following each call to `setjmp` or a related function.

These codes are printed symbolically when they appear in debugging dumps.

The machine mode of an insn is normally `VOIDmode`, but some
phases use the mode for various purposes.

The common subexpression elimination pass sets the mode of an insn to
`QImode` when it is the first insn in a block that has already
been processed.

The second Haifa scheduling pass, for targets that can multiple issue,
sets the mode of an insn to `TImode` when it is believed that the
instruction begins an issue group. That is, when the instruction
cannot issue simultaneously with the previous. This may be relied on
by later passes, in particular machine-dependent reorg.

Here is a table of the extra fields of `insn`, `jump_insn`
and `call_insn` insns:

**`PATTERN (`i`)`**
: An expression for the side effect performed by this insn. This must be
one of the following codes: `set`, `call`, `use`,
`clobber`, `return`, `asm_input`, `asm_output`,
`addr_vec`, `addr_diff_vec`, `trap_if`, `unspec`,
`unspec_volatile`, `parallel`, `cond_exec`, or `sequence`. If it is a `parallel`,
each element of the `parallel` must be one these codes, except that
`parallel` expressions cannot be nested and `addr_vec` and
`addr_diff_vec` are not permitted inside a `parallel` expression.

**`INSN_CODE (`i`)`**
: An integer that says which pattern in the machine description matches
this insn, or −1 if the matching has not yet been attempted.

Such matching is never attempted and this field remains −1 on an insn
whose pattern consists of a single `use`, `clobber`,
`asm_input`, `addr_vec` or `addr_diff_vec` expression.

Matching is also never attempted on insns that result from an `asm`
statement. These contain at least one `asm_operands` expression.
The function `asm_noperands` returns a non-negative value for
such insns.

In the debugging output, this field is printed as a number followed by
a symbolic representation that locates the pattern in the `md`
file as some small positive or negative offset from a named pattern.

**`LOG_LINKS (`i`)`**
: A list (chain of `insn_list` expressions) giving information about
dependencies between instructions within a basic block. Neither a jump
nor a label may come between the related insns.

**`REG_NOTES (`i`)`**
: A list (chain of `expr_list` and `insn_list` expressions)
giving miscellaneous information about the insn. It is often
information pertaining to the registers used in this insn.

The `LOG_LINKS` field of an insn is a chain of `insn_list`
expressions. Each of these has two operands: the first is an insn,
and the second is another `insn_list` expression (the next one in
the chain). The last `insn_list` in the chain has a null pointer
as second operand. The significant thing about the chain is which
insns appear in it (as first operands of `insn_list`
expressions). Their order is not significant.

This list is originally set up by the flow analysis pass; it is a null
pointer until then. Flow only adds links for those data dependencies
which can be used for instruction combination. For each insn, the flow
analysis pass adds a link to insns which store into registers values
that are used for the first time in this insn. The instruction
scheduling pass adds extra links so that every dependence will be
represented. Links represent data dependencies, antidependencies and
output dependencies; the machine mode of the link distinguishes these
three types: antidependencies have mode `REG_DEP_ANTI`, output
dependencies have mode `REG_DEP_OUTPUT`, and data dependencies have
mode `VOIDmode`.

The `REG_NOTES` field of an insn is a chain similar to the
`LOG_LINKS` field but it includes `expr_list` expressions in
addition to `insn_list` expressions. There are several kinds of
register notes, which are distinguished by the machine mode, which in a
register note is really understood as being an `enum reg_note`.
The first operand op of the note is data whose meaning depends on
the kind of note.

The macro `REG_NOTE_KIND (`x`)` returns the kind of
register note. Its counterpart, the macro `PUT_REG_NOTE_KIND
(`x`,` newkind`)` sets the register note type of x to be
newkind.

Register notes are of three classes: They may say something about an
input to an insn, they may say something about an output of an insn, or
they may create a linkage between two insns. There are also a set
of values that are only used in `LOG_LINKS`.

These register notes annotate inputs to an insn:

**`REG_DEAD`**
: The value in op dies in this insn; that is to say, altering the
value immediately after this insn would not affect the future behavior
of the program.

It does not follow that the register op has no useful value after
this insn since op is not necessarily modified by this insn.
Rather, no subsequent instruction uses the contents of op.

**`REG_UNUSED`**
: The register op being set by this insn will not be used in a
subsequent insn. This differs from a `REG_DEAD` note, which
indicates that the value in an input will not be used subsequently.
These two notes are independent; both may be present for the same
register.

**`REG_INC`**
: The register op is incremented (or decremented; at this level
there is no distinction) by an embedded side effect inside this insn.
This means it appears in a `post_inc`, `pre_inc`,
`post_dec` or `pre_dec` expression.

**`REG_NONNEG`**
: The register op is known to have a nonnegative value when this
insn is reached. This is used so that decrement and branch until zero
instructions, such as the m68k dbra, can be matched.

The `REG_NONNEG` note is added to insns only if the machine
description has a ``decrement_and_branch_until_zero`' pattern.

**`REG_NO_CONFLICT`**
: This insn does not cause a conflict between op and the item
being set by this insn even though it might appear that it does.
In other words, if the destination register and op could
otherwise be assigned the same register, this insn does not
prevent that assignment.

Insns with this note are usually part of a block that begins with a
`clobber` insn specifying a multi-word pseudo register (which will
be the output of the block), a group of insns that each set one word of
the value and have the `REG_NO_CONFLICT` note attached, and a final
insn that copies the output to itself with an attached `REG_EQUAL`
note giving the expression being computed. This block is encapsulated
with `REG_LIBCALL` and `REG_RETVAL` notes on the first and
last insns, respectively.

**`REG_LABEL`**
: This insn uses op, a `code_label` or a `note` of type
`NOTE_INSN_DELETED_LABEL`, but is not a
`jump_insn`, or it is a `jump_insn` that required the label to
be held in a register. The presence of this note allows jump
optimization to be aware that op is, in fact, being used, and flow
optimization to build an accurate flow graph.

**`REG_CROSSING_JUMP`**
: This insn is an branching instruction (either an unconditional jump or
an indirect jump) which crosses between hot and cold sections, which
could potentially be very far apart in the executable. The presence
of this note indicates to other optimizations that this this branching
instruction should not be “collapsed” into a simpler branching
construct. It is used when the optimization to partition basic blocks
into hot and cold sections is turned on.

The following notes describe attributes of outputs of an insn:

**`REG_EQUIV`

**`REG_EQUAL`****
: This note is only valid on an insn that sets only one register and
indicates that that register will be equal to op at run time; the
scope of this equivalence differs between the two types of notes. The
value which the insn explicitly copies into the register may look
different from op, but they will be equal at run time. If the
output of the single `set` is a `strict_low_part` expression,
the note refers to the register that is contained in `SUBREG_REG`
of the `subreg` expression.

For `REG_EQUIV`, the register is equivalent to op throughout
the entire function, and could validly be replaced in all its
occurrences by op. (“Validly” here refers to the data flow of
the program; simple replacement may make some insns invalid.) For
example, when a constant is loaded into a register that is never
assigned any other value, this kind of note is used.

When a parameter is copied into a pseudo-register at entry to a function,
a note of this kind records that the register is equivalent to the stack
slot where the parameter was passed. Although in this case the register
may be set by other insns, it is still valid to replace the register
by the stack slot throughout the function.

A `REG_EQUIV` note is also used on an instruction which copies a
register parameter into a pseudo-register at entry to a function, if
there is a stack slot where that parameter could be stored. Although
other insns may set the pseudo-register, it is valid for the compiler to
replace the pseudo-register by stack slot throughout the function,
provided the compiler ensures that the stack slot is properly
initialized by making the replacement in the initial copy instruction as
well. This is used on machines for which the calling convention
allocates stack space for register parameters. See
`REG_PARM_STACK_SPACE` in [Stack Arguments](Stack-Arguments.md#apple-kn2gcy3lfvaxez3vnvsw45dt).

In the case of `REG_EQUAL`, the register that is set by this insn
will be equal to op at run time at the end of this insn but not
necessarily elsewhere in the function. In this case, op
is typically an arithmetic expression. For example, when a sequence of
insns such as a library call is used to perform an arithmetic operation,
this kind of note is attached to the insn that produces or copies the
final value.

These two notes are used in different ways by the compiler passes.
`REG_EQUAL` is used by passes prior to register allocation (such as
common subexpression elimination and loop optimization) to tell them how
to think of that value. `REG_EQUIV` notes are used by register
allocation to indicate that there is an available substitute expression
(either a constant or a `mem` expression for the location of a
parameter on the stack) that may be used in place of a register if
insufficient registers are available.

Except for stack homes for parameters, which are indicated by a
`REG_EQUIV` note and are not useful to the early optimization
passes and pseudo registers that are equivalent to a memory location
throughout their entire life, which is not detected until later in
the compilation, all equivalences are initially indicated by an attached
`REG_EQUAL` note. In the early stages of register allocation, a
`REG_EQUAL` note is changed into a `REG_EQUIV` note if
op is a constant and the insn represents the only set of its
destination register.

Thus, compiler passes prior to register allocation need only check for
`REG_EQUAL` notes and passes subsequent to register allocation
need only check for `REG_EQUIV` notes.

These notes describe linkages between insns. They occur in pairs: one
insn has one of a pair of notes that points to a second insn, which has
the inverse note pointing back to the first insn.

**`REG_RETVAL`**
: This insn copies the value of a multi-insn sequence (for example, a
library call), and op is the first insn of the sequence (for a
library call, the first insn that was generated to set up the arguments
for the library call).

Loop optimization uses this note to treat such a sequence as a single
operation for code motion purposes and flow analysis uses this note to
delete such sequences whose results are dead.

A `REG_EQUAL` note will also usually be attached to this insn to
provide the expression being computed by the sequence.

These notes will be deleted after reload, since they are no longer
accurate or useful.

**`REG_LIBCALL`**
: This is the inverse of `REG_RETVAL`: it is placed on the first
insn of a multi-insn sequence, and it points to the last one.

These notes are deleted after reload, since they are no longer useful or
accurate.

**`REG_CC_SETTER`

**`REG_CC_USER`****
: On machines that use `cc0`, the insns which set and use `cc0`
set and use `cc0` are adjacent. However, when branch delay slot
filling is done, this may no longer be true. In this case a
`REG_CC_USER` note will be placed on the insn setting `cc0` to
point to the insn using `cc0` and a `REG_CC_SETTER` note will
be placed on the insn using `cc0` to point to the insn setting
`cc0`.

These values are only used in the `LOG_LINKS` field, and indicate
the type of dependency that each link represents. Links which indicate
a data dependence (a read after write dependence) do not use any code,
they simply have mode `VOIDmode`, and are printed without any
descriptive text.

**`REG_DEP_ANTI`**
: This indicates an anti dependence (a write after read dependence).

**`REG_DEP_OUTPUT`**
: This indicates an output dependence (a write after write dependence).

These notes describe information gathered from gcov profile data. They
are stored in the `REG_NOTES` field of an insn as an
`expr_list`.

**`REG_BR_PROB`**
: This is used to specify the ratio of branches to non-branches of a
branch insn according to the profile data. The value is stored as a
value between 0 and REG_BR_PROB_BASE; larger values indicate a higher
probability that the branch will be taken.

**`REG_BR_PRED`**
: These notes are found in JUMP insns after delayed branch scheduling
has taken place. They indicate both the direction and the likelihood
of the JUMP. The format is a bitmask of ATTR_FLAG_\* values.

**`REG_FRAME_RELATED_EXPR`**
: This is used on an RTX_FRAME_RELATED_P insn wherein the attached expression
is used in place of the actual insn pattern. This is done in cases where
the pattern is either complex or misleading.

For convenience, the machine mode in an `insn_list` or
`expr_list` is printed using these symbolic codes in debugging dumps.

The only difference between the expression codes `insn_list` and
`expr_list` is that the first operand of an `insn_list` is
assumed to be an insn and is printed in debugging dumps as the insn's
unique id; the first operand of an `expr_list` is printed in the
ordinary way as an expression.
