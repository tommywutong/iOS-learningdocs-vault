---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Calls.html
archived_at: '2026-07-15T07:30:59.351709Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Sharing](Sharing.md#apple-knugc4tjnztq),
Previous: [Insns](Insns.md#apple-jfxhg3tt),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.19 RTL Representation of Function-Call Insns

Insns that call subroutines have the RTL expression code `call_insn`.
These insns must satisfy special rules, and their bodies must use a special
RTL expression code, `call`.

A `call` expression has two operands, as follows:

```
     (call (mem:fm addr) nbytes)
```

Here nbytes is an operand that represents the number of bytes of
argument data being passed to the subroutine, fm is a machine mode
(which must equal as the definition of the `FUNCTION_MODE` macro in
the machine description) and addr represents the address of the
subroutine.

For a subroutine that returns no value, the `call` expression as
shown above is the entire body of the insn, except that the insn might
also contain `use` or `clobber` expressions.

For a subroutine that returns a value whose mode is not `BLKmode`,
the value is returned in a hard register. If this register's number is
r, then the body of the call insn looks like this:

```
     (set (reg:m r)
          (call (mem:fm addr) nbytes))
```

This RTL expression makes it clear (to the optimizer passes) that the
appropriate register receives a useful value in this insn.

When a subroutine returns a `BLKmode` value, it is handled by
passing to the subroutine the address of a place to store the value.
So the call insn itself does not “return” any value, and it has the
same RTL form as a call that returns nothing.

On some machines, the call instruction itself clobbers some register,
for example to contain the return address. `call_insn` insns
on these machines should have a body which is a `parallel`
that contains both the `call` expression and `clobber`
expressions that indicate which registers are destroyed. Similarly,
if the call instruction requires some register other than the stack
pointer that is not explicitly mentioned in its RTL, a `use`
subexpression should mention that register.

Functions that are called are assumed to modify all registers listed in
the configuration macro `CALL_USED_REGISTERS` (see [Register Basics](Register-Basics.md#apple-kjswo2ltorsxelkcmfzwsy3t)) and, with the exception of `const` functions and library
calls, to modify all of memory.

Insns containing just `use` expressions directly precede the
`call_insn` insn to indicate which registers contain inputs to the
function. Similarly, if registers other than those in
`CALL_USED_REGISTERS` are clobbered by the called function, insns
containing a single `clobber` follow immediately after the call to
indicate which registers.
