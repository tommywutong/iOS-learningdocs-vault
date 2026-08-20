---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Side-Effects.html
archived_at: '2026-07-15T07:31:00.719947Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Incdec](Incdec.md#apple-jfxggzdfmm),
Previous: [RTL Declarations](RTL-Declarations.md#apple-kjkeylkemvrwyylsmf2gs33oom),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.15 Side Effect Expressions

The expression codes described so far represent values, not actions.
But machine instructions never produce values; they are meaningful
only for their side effects on the state of the machine. Special
expression codes are used to represent side effects.

The body of an instruction is always one of these side effect codes;
the codes described above, which represent values, appear only as
the operands of these.

**`(set` lval x`)`**
: Represents the action of storing the value of x into the place
represented by lval. lval must be an expression
representing a place that can be stored in: `reg` (or `subreg`,
`strict_low_part` or `zero_extract`), `mem`, `pc`,
`parallel`, or `cc0`.

If lval is a `reg`, `subreg` or `mem`, it has a
machine mode; then x must be valid for that mode.

If lval is a `reg` whose machine mode is less than the full
width of the register, then it means that the part of the register
specified by the machine mode is given the specified value and the
rest of the register receives an undefined value. Likewise, if
lval is a `subreg` whose machine mode is narrower than
the mode of the register, the rest of the register can be changed in
an undefined way.

If lval is a `strict_low_part` of a subreg, then the part
of the register specified by the machine mode of the `subreg` is
given the value x and the rest of the register is not changed.

If lval is a `zero_extract`, then the referenced part of
the bit-field (a memory or register reference) specified by the
`zero_extract` is given the value x and the rest of the
bit-field is not changed. Note that `sign_extract` can not
appear in lval.

If lval is `(cc0)`, it has no machine mode, and x may
be either a `compare` expression or a value that may have any mode.
The latter case represents a “test” instruction. The expression
`(set (cc0) (reg:`m n`))` is equivalent to
`(set (cc0) (compare (reg:`m n`) (const_int 0)))`.
Use the former expression to save space during the compilation.

If lval is a `parallel`, it is used to represent the case of
a function returning a structure in multiple registers. Each element
of the `parallel` is an `expr_list` whose first operand is a
`reg` and whose second operand is a `const_int` representing the
offset (in bytes) into the structure at which the data in that register
corresponds. The first element may be null to indicate that the structure
is also passed partly in memory.

If lval is `(pc)`, we have a jump instruction, and the
possibilities for x are very limited. It may be a
`label_ref` expression (unconditional jump). It may be an
`if_then_else` (conditional jump), in which case either the
second or the third operand must be `(pc)` (for the case which
does not jump) and the other of the two must be a `label_ref`
(for the case which does jump). x may also be a `mem` or
`(plus:SI (pc)` y`)`, where y may be a `reg` or a
`mem`; these unusual patterns are used to represent jumps through
branch tables.

If lval is neither `(cc0)` nor `(pc)`, the mode of
lval must not be `VOIDmode` and the mode of x must be
valid for the mode of lval.

lval is customarily accessed with the `SET_DEST` macro and
x with the `SET_SRC` macro.

**`(return)`**
: As the sole expression in a pattern, represents a return from the
current function, on machines where this can be done with one
instruction, such as VAXen. On machines where a multi-instruction
“epilogue” must be executed in order to return from the function,
returning is done by jumping to a label which precedes the epilogue, and
the `return` expression code is never used.

Inside an `if_then_else` expression, represents the value to be
placed in `pc` to return to the caller.

Note that an insn pattern of `(return)` is logically equivalent to
`(set (pc) (return))`, but the latter form is never used.

**`(call` function nargs`)`**
: Represents a function call. function is a `mem` expression
whose address is the address of the function to be called.
nargs is an expression which can be used for two purposes: on
some machines it represents the number of bytes of stack argument; on
others, it represents the number of argument registers.

Each machine has a standard machine mode which function must
have. The machine description defines macro `FUNCTION_MODE` to
expand into the requisite mode name. The purpose of this mode is to
specify what kind of addressing is allowed, on machines where the
allowed kinds of addressing depend on the machine mode being
addressed.

**`(clobber` x`)`**
: Represents the storing or possible storing of an unpredictable,
undescribed value into x, which must be a `reg`,
`scratch`, `parallel` or `mem` expression.

One place this is used is in string instructions that store standard
values into particular hard registers. It may not be worth the
trouble to describe the values that are stored, but it is essential to
inform the compiler that the registers will be altered, lest it
attempt to keep data in them across the string instruction.

If x is `(mem:BLK (const_int 0))` or
`(mem:BLK (scratch))`, it means that all memory
locations must be presumed clobbered. If x is a `parallel`,
it has the same meaning as a `parallel` in a `set` expression.

Note that the machine description classifies certain hard registers as
“call-clobbered”. All function call instructions are assumed by
default to clobber these registers, so there is no need to use
`clobber` expressions to indicate this fact. Also, each function
call is assumed to have the potential to alter any memory location,
unless the function is declared `const`.

If the last group of expressions in a `parallel` are each a
`clobber` expression whose arguments are `reg` or
`match_scratch` (see [RTL Template](RTL-Template.md#apple-kjkeylkumvwxa3dborsq)) expressions, the combiner
phase can add the appropriate `clobber` expressions to an insn it
has constructed when doing so will cause a pattern to be matched.

This feature can be used, for example, on a machine that whose multiply
and add instructions don't use an MQ register but which has an
add-accumulate instruction that does clobber the MQ register. Similarly,
a combined instruction might require a temporary register while the
constituent instructions might not.

When a `clobber` expression for a register appears inside a
`parallel` with other side effects, the register allocator
guarantees that the register is unoccupied both before and after that
insn. However, the reload phase may allocate a register used for one of
the inputs unless the ``&`' constraint is specified for the selected
alternative (see [Modifiers](Modifiers.md#apple-jvxwi2lgnfsxe4y)). You can clobber either a specific hard
register, a pseudo register, or a `scratch` expression; in the
latter two cases, GCC will allocate a hard register that is available
there for use as a temporary.

For instructions that require a temporary register, you should use
`scratch` instead of a pseudo-register because this will allow the
combiner phase to add the `clobber` when required. You do this by
coding (`clobber` (`match_scratch` ...)). If you do
clobber a pseudo register, use one which appears nowhere else—generate
a new one each time. Otherwise, you may confuse CSE.

There is one other known use for clobbering a pseudo register in a
`parallel`: when one of the input operands of the insn is also
clobbered by the insn. In this case, using the same pseudo register in
the clobber and elsewhere in the insn produces the expected results.

**`(use` x`)`**
: Represents the use of the value of x. It indicates that the
value in x at this point in the program is needed, even though
it may not be apparent why this is so. Therefore, the compiler will
not attempt to delete previous instructions whose only effect is to
store a value in x. x must be a `reg` expression.

In some situations, it may be tempting to add a `use` of a
register in a `parallel` to describe a situation where the value
of a special register will modify the behavior of the instruction.
An hypothetical example might be a pattern for an addition that can
either wrap around or use saturating addition depending on the value
of a special control register:

```
          (parallel [(set (reg:SI 2) (unspec:SI [(reg:SI 3)
                                                 (reg:SI 4)] 0))
                     (use (reg:SI 1))])

```

This will not work, several of the optimizers only look at expressions
locally; it is very likely that if you have multiple insns with
identical inputs to the `unspec`, they will be optimized away even
if register 1 changes in between.

This means that `use` can _only_ be used to describe
that the register is live. You should think twice before adding
`use` statements, more often you will want to use `unspec`
instead. The `use` RTX is most commonly useful to describe that
a fixed register is implicitly used in an insn. It is also safe to use
in patterns where the compiler knows for other reasons that the result
of the whole pattern is variable, such as ``movmemm`' or
``call`' patterns.

During the reload phase, an insn that has a `use` as pattern
can carry a reg_equal note. These `use` insns will be deleted
before the reload phase exits.

During the delayed branch scheduling phase, x may be an insn.
This indicates that x previously was located at this place in the
code and its data dependencies need to be taken into account. These
`use` insns will be deleted before the delayed branch scheduling
phase exits.

**`(parallel [`x0 x1 `...])`**
: Represents several side effects performed in parallel. The square
brackets stand for a vector; the operand of `parallel` is a
vector of expressions. x0, x1 and so on are individual
side effect expressions—expressions of code `set`, `call`,
`return`, `clobber` or `use`.

“In parallel” means that first all the values used in the individual
side-effects are computed, and second all the actual side-effects are
performed. For example,

```
          (parallel [(set (reg:SI 1) (mem:SI (reg:SI 1)))
                     (set (mem:SI (reg:SI 1)) (reg:SI 1))])

```

says unambiguously that the values of hard register 1 and the memory
location addressed by it are interchanged. In both places where
`(reg:SI 1)` appears as a memory address it refers to the value
in register 1 _before_ the execution of the insn.

It follows that it is _incorrect_ to use `parallel` and
expect the result of one `set` to be available for the next one.
For example, people sometimes attempt to represent a jump-if-zero
instruction this way:

```
          (parallel [(set (cc0) (reg:SI 34))
                     (set (pc) (if_then_else
                                  (eq (cc0) (const_int 0))
                                  (label_ref ...)
                                  (pc)))])

```

But this is incorrect, because it says that the jump condition depends
on the condition code value _before_ this instruction, not on the
new value that is set by this instruction.

Peephole optimization, which takes place together with final assembly
code output, can produce insns whose patterns consist of a `parallel`
whose elements are the operands needed to output the resulting
assembler code—often `reg`, `mem` or constant expressions.
This would not be well-formed RTL at any other stage in compilation,
but it is ok then because no further optimization remains to be done.
However, the definition of the macro `NOTICE_UPDATE_CC`, if
any, must deal with such insns if you define any peephole optimizations.

**`(cond_exec [`cond expr`])`**
: Represents a conditionally executed expression. The expr is
executed only if the cond is nonzero. The cond expression
must not have side-effects, but the expr may very well have
side-effects.

**`(sequence [`insns `...])`**
: Represents a sequence of insns. Each of the insns that appears
in the vector is suitable for appearing in the chain of insns, so it
must be an `insn`, `jump_insn`, `call_insn`,
`code_label`, `barrier` or `note`.

A `sequence` RTX is never placed in an actual insn during RTL
generation. It represents the sequence of insns that result from a
`define_expand` _before_ those insns are passed to
`emit_insn` to insert them in the chain of insns. When actually
inserted, the individual sub-insns are separated out and the
`sequence` is forgotten.

After delay-slot scheduling is completed, an insn and all the insns that
reside in its delay slots are grouped together into a `sequence`.
The insn requiring the delay slot is the first insn in the vector;
subsequent insns are to be placed in the delay slot.

`INSN_ANNULLED_BRANCH_P` is set on an insn in a delay slot to
indicate that a branch insn should be used that will conditionally annul
the effect of the insns in the delay slots. In such a case,
`INSN_FROM_TARGET_P` indicates that the insn is from the target of
the branch and should be executed only if the branch is taken; otherwise
the insn should be executed only if the branch is not taken.
See [Delay Slots](Delay-Slots.md#apple-irswyylzfvjwy33uom).

These expression codes appear in place of a side effect, as the body of
an insn, though strictly speaking they do not always describe side
effects as such:

**`(asm_input` s`)`**
: Represents literal assembler code as described by the string s.

**`(unspec [`operands `...]` index`)`

**`(unspec_volatile [`operands `...]` index`)`****
: Represents a machine-specific operation on operands. index
selects between multiple machine-specific operations.
`unspec_volatile` is used for volatile operations and operations
that may trap; `unspec` is used for other operations.

These codes may appear inside a `pattern` of an
insn, inside a `parallel`, or inside an expression.

**`(addr_vec:`m `[`lr0 lr1 `...])`**
: Represents a table of jump addresses. The vector elements lr0,
etc., are `label_ref` expressions. The mode m specifies
how much space is given to each address; normally m would be
`Pmode`.

**`(addr_diff_vec:`m base `[`lr0 lr1 `...]` min max flags`)`**
: Represents a table of jump addresses expressed as offsets from
base. The vector elements lr0, etc., are `label_ref`
expressions and so is base. The mode m specifies how much
space is given to each address-difference. min and max
are set up by branch shortening and hold a label with a minimum and a
maximum address, respectively. flags indicates the relative
position of base, min and max to the containing insn
and of min and max to base. See rtl.def for details.

**`(prefetch:`m addr rw locality`)`**
: Represents prefetch of memory at address addr.
Operand rw is 1 if the prefetch is for data to be written, 0 otherwise;
targets that do not support write prefetches should treat this as a normal
prefetch.
Operand locality specifies the amount of temporal locality; 0 if there
is none or 1, 2, or 3 for increasing levels of temporal locality;
targets that do not support locality hints should ignore this.

This insn is used to minimize cache-miss latency by moving data into a
cache before it is accessed. It should use only non-faulting data prefetch
instructions.
