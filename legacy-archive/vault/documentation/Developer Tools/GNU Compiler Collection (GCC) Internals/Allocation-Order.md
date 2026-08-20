---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Allocation-Order.html
archived_at: '2026-07-15T07:30:59.255551Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Values in Registers](Values-in-Registers.md#apple-kzqwy5lfomwws3rnkjswo2ltorsxe4y),
Previous: [Register Basics](Register-Basics.md#apple-kjswo2ltorsxelkcmfzwsy3t),
Up: [Registers](Registers.md#apple-kjswo2ltorsxe4y)

---

#### 13.7.2 Order of Allocation of Registers

Registers are allocated in order.

— Macro: __REG_ALLOC_ORDER__
> If defined, an initializer for a vector of integers, containing the
> numbers of hard registers in the order in which GCC should prefer
> to use them (from most preferred to least).
>
> If this macro is not defined, registers are used lowest numbered first
> (all else being equal).
>
> One use of this macro is on machines where the highest numbered
> registers must always be saved and the save-multiple-registers
> instruction supports only sequences of consecutive registers. On such
> machines, define `REG_ALLOC_ORDER` to be an initializer that lists
> the highest numbered allocable register first.

— Macro: __ORDER_REGS_FOR_LOCAL_ALLOC__
> A C statement (sans semicolon) to choose the order in which to allocate
> hard registers for pseudo-registers local to a basic block.
>
> Store the desired register order in the array `reg_alloc_order`.
> Element 0 should be the register to allocate first; element 1, the next
> register; and so on.
>
> The macro body should not assume anything about the contents of
> `reg_alloc_order` before execution of the macro.
>
> On most machines, it is not necessary to define this macro.
