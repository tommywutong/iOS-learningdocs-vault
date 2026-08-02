---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Alias-analysis.html
archived_at: '2026-07-15T07:31:01.170196Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [SSA](SSA.md#apple-knjuc),
Up: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc)

---

### 10.6 Alias analysis

Alias analysis proceeds in 4 main phases:

1. Structural alias analysis.

   This phase walks the types for structure variables, and determines which
   of the fields can overlap using offset and size of each field. For each
   field, a “subvariable” called a “Structure field tag” (SFT) is
   created, which represents that field as a separate variable. All
   accesses that could possibly overlap with a given field will have
   virtual operands for the SFT of that field.

   ```
             struct foo
             {
               int a;
               int b;
             }
             struct foo temp;
             int bar (void)
             {
               int tmp1, tmp2, tmp3;
               SFT.0_2 = V_MUST_DEF <SFT.0_1>
               temp.a = 5;
               SFT.1_4 = V_MUST_DEF <SFT.1_3>
               temp.b = 6;

               VUSE <SFT.1_4>
               tmp1_5 = temp.b;
               VUSE <SFT.0_2>
               tmp2_6 = temp.a;

               tmp3_7 = tmp1_5 + tmp2_6;
               return tmp3_7;
             }

   ```

   If you copy the symbol tag for a variable for some reason, you probably
   also want to copy the subvariables for that variable.
2. Points-to and escape analysis.

   This phase walks the use-def chains in the SSA web looking for
   three things:

   - Assignments of the form `P_i = &VAR`
   - Assignments of the form P_i = malloc()
   - Pointers and ADDR_EXPR that escape the current function.

   The concept of `escaping' is the same one used in the Java world.
   When a pointer or an ADDR_EXPR escapes, it means that it has been
   exposed outside of the current function. So, assignment to
   global variables, function arguments and returning a pointer are
   all escape sites.

   This is where we are currently limited. Since not everything is
   renamed into SSA, we lose track of escape properties when a
   pointer is stashed inside a field in a structure, for instance.
   In those cases, we are assuming that the pointer does escape.

   We use escape analysis to determine whether a variable is
   call-clobbered. Simply put, if an ADDR_EXPR escapes, then the
   variable is call-clobbered. If a pointer P_i escapes, then all
   the variables pointed-to by P_i (and its memory tag) also escape.
3. Compute flow-sensitive aliases

   We have two classes of memory tags. Memory tags associated with
   the pointed-to data type of the pointers in the program. These
   tags are called “symbol memory tag” (SMT). The other class are
   those associated with SSA_NAMEs, called “name memory tag” (NMT).
   The basic idea is that when adding operands for an INDIRECT_REF
   \*P_i, we will first check whether P_i has a name tag, if it does
   we use it, because that will have more precise aliasing
   information. Otherwise, we use the standard symbol tag.

   In this phase, we go through all the pointers we found in
   points-to analysis and create alias sets for the name memory tags
   associated with each pointer P_i. If P_i escapes, we mark
   call-clobbered the variables it points to and its tag.
4. Compute flow-insensitive aliases

   This pass will compare the alias set of every symbol memory tag and
   every addressable variable found in the program. Given a symbol
   memory tag SMT and an addressable variable V. If the alias sets
   of SMT and V conflict (as computed by may_alias_p), then V is
   marked as an alias tag and added to the alias set of SMT.

For instance, consider the following function:

```
     foo (int i)
     {
       int *p, *q, a, b;

       if (i > 10)
         p = &a;
       else
         q = &b;

       *p = 3;
       *q = 5;
       a = b + 2;
       return *p;
     }
```

After aliasing analysis has finished, the symbol memory tag for
pointer `p` will have two aliases, namely variables `a` and
`b`.
Every time pointer `p` is dereferenced, we want to mark the
operation as a potential reference to `a` and `b`.

```
     foo (int i)
     {
       int *p, a, b;

       if (i_2 > 10)
         p_4 = &a;
       else
         p_6 = &b;
       # p_1 = PHI <p_4(1), p_6(2)>;

       # a_7 = V_MAY_DEF <a_3>;
       # b_8 = V_MAY_DEF <b_5>;
       *p_1 = 3;

       # a_9 = V_MAY_DEF <a_7>
       # VUSE <b_8>
       a_9 = b_8 + 2;

       # VUSE <a_9>;
       # VUSE <b_8>;
       return *p_1;
     }
```

In certain cases, the list of may aliases for a pointer may grow
too large. This may cause an explosion in the number of virtual
operands inserted in the code. Resulting in increased memory
consumption and compilation time.

When the number of virtual operands needed to represent aliased
loads and stores grows too large (configurable with `--param
max-aliased-vops`), alias sets are grouped to avoid severe
compile-time slow downs and memory consumption. The alias
grouping heuristic proceeds as follows:

1. Sort the list of pointers in decreasing number of contributed
   virtual operands.
2. Take the first pointer from the list and reverse the role
   of the memory tag and its aliases. Usually, whenever an
   aliased variable Vi is found to alias with a memory tag
   T, we add Vi to the may-aliases set for T. Meaning that
   after alias analysis, we will have:

   ```
             may-aliases(T) = { V1, V2, V3, ..., Vn }

   ```

   This means that every statement that references T, will get
   `n` virtual operands for each of the Vi tags. But, when
   alias grouping is enabled, we make T an alias tag and add it
   to the alias set of all the Vi variables:

   ```
             may-aliases(V1) = { T }
             may-aliases(V2) = { T }
             ...
             may-aliases(Vn) = { T }

   ```

   This has two effects: (a) statements referencing T will only get
   a single virtual operand, and, (b) all the variables Vi will now
   appear to alias each other. So, we lose alias precision to
   improve compile time. But, in theory, a program with such a high
   level of aliasing should not be very optimizable in the first
   place.
3. Since variables may be in the alias set of more than one
   memory tag, the grouping done in step (2) needs to be extended
   to all the memory tags that have a non-empty intersection with
   the may-aliases set of tag T. For instance, if we originally
   had these may-aliases sets:

   ```
             may-aliases(T) = { V1, V2, V3 }
             may-aliases(R) = { V2, V4 }

   ```

   In step (2) we would have reverted the aliases for T as:

   ```
             may-aliases(V1) = { T }
             may-aliases(V2) = { T }
             may-aliases(V3) = { T }

   ```

   But note that now V2 is no longer aliased with R. We could
   add R to may-aliases(V2), but we are in the process of
   grouping aliases to reduce virtual operands so what we do is
   add V4 to the grouping to obtain:

   ```
             may-aliases(V1) = { T }
             may-aliases(V2) = { T }
             may-aliases(V3) = { T }
             may-aliases(V4) = { T }

   ```
4. If the total number of virtual operands due to aliasing is
   still above the threshold set by max-alias-vops, go back to (2).
