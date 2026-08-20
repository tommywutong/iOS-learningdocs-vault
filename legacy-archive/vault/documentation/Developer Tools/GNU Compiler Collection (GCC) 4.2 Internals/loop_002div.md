---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/loop_002div.html
archived_at: '2026-07-15T07:31:03.167426Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Number of iterations](Number-of-iterations.md#apple-jz2w2ytfoiww6zrnnf2gk4tboruw63tt),
Previous: [Scalar evolutions](Scalar-evolutions.md#apple-knrwc3dboiwwk5tpnr2xi2lpnzzq),
Up: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa)

---

### 11.6 IV analysis on RTL

The induction variable on RTL is simple and only allows analysis of
affine induction variables, and only in one loop at once. The interface
is declared in `cfgloop.h`. Before analyzing induction variables
in a loop L, `iv_analysis_loop_init` function must be called on L.
After the analysis (possibly calling `iv_analysis_loop_init` for
several loops) is finished, `iv_analysis_done` should be called.
The following functions can be used to access the results of the
analysis:

- `iv_analyze`: Analyzes a single register used in the given
  insn. If no use of the register in this insn is found, the following
  insns are scanned, so that this function can be called on the insn
  returned by get_condition.
- `iv_analyze_result`: Analyzes result of the assignment in the
  given insn.
- `iv_analyze_expr`: Analyzes a more complicated expression.
  All its operands are analyzed by `iv_analyze`, and hence they must
  be used in the specified insn or one of the following insns.

The description of the induction variable is provided in `struct
rtx_iv`. In order to handle subregs, the representation is a bit
complicated; if the value of the `extend` field is not
`UNKNOWN`, the value of the induction variable in the i-th
iteration is

```
     delta + mult * extend_{extend_mode} (subreg_{mode} (base + i * step)),
```

with the following exception: if `first_special` is true, then the
value in the first iteration (when `i` is zero) is `delta +
mult * base`. However, if `extend` is equal to `UNKNOWN`,
then `first_special` must be false, `delta` 0, `mult` 1
and the value in the i-th iteration is

```
     subreg_{mode} (base + i * step)
```

The function `get_iv_value` can be used to perform these
calculations.
