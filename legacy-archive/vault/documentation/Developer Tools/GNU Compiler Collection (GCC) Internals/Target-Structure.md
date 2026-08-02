---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Target-Structure.html
archived_at: '2026-07-15T07:31:00.887669Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Driver](Driver.md#apple-irzgs5tfoi),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.1 The Global `targetm` Variable

— Variable: struct gcc_target __targetm__
> The target `.c` file must define the global `targetm` variable
> which contains pointers to functions and data relating to the target
> machine. The variable is declared in `target.h`;
> `target-def.h` defines the macro `TARGET_INITIALIZER` which is
> used to initialize the variable, and macros for the default initializers
> for elements of the structure. The `.c` file should override those
> macros for which the default definition is inappropriate. For example:
>
> ```
>           #include "target.h"
>           #include "target-def.h"
>
>           /* Initialize the GCC target structure.  */
>
>           #undef TARGET_COMP_TYPE_ATTRIBUTES
>           #define TARGET_COMP_TYPE_ATTRIBUTES machine_comp_type_attributes
>
>           struct gcc_target targetm = TARGET_INITIALIZER;
>
> ```

Where a macro should be defined in the `.c` file in this manner to
form part of the `targetm` structure, it is documented below as a
“Target Hook” with a prototype. Many macros will change in future
from being defined in the `.h` file to being part of the
`targetm` structure.
