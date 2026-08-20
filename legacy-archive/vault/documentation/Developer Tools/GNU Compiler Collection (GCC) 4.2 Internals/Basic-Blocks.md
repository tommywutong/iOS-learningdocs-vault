---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Basic-Blocks.html
archived_at: '2026-07-15T07:31:01.246667Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Edges](Edges.md#apple-ivsgozlt),
Up: [Control Flow](Control-Flow.md#apple-inxw45dsn5wc2rtmn53q)

---

### 13.1 Basic Blocks

A basic block is a straight-line sequence of code with only one entry
point and only one exit. In GCC, basic blocks are represented using
the `basic_block` data type.

Two pointer members of the `basic_block` structure are the
pointers `next_bb` and `prev_bb`. These are used to keep
doubly linked chain of basic blocks in the same order as the
underlying instruction stream. The chain of basic blocks is updated
transparently by the provided API for manipulating the CFG. The macro
`FOR_EACH_BB` can be used to visit all the basic blocks in
lexicographical order. Dominator traversals are also possible using
`walk_dominator_tree`. Given two basic blocks A and B, block A
dominates block B if A is _always_ executed before B.

The `BASIC_BLOCK` array contains all basic blocks in an
unspecified order. Each `basic_block` structure has a field
that holds a unique integer identifier `index` that is the
index of the block in the `BASIC_BLOCK` array.
The total number of basic blocks in the function is
`n_basic_blocks`. Both the basic block indices and
the total number of basic blocks may vary during the compilation
process, as passes reorder, create, duplicate, and destroy basic
blocks. The index for any block should never be greater than
`last_basic_block`.

Special basic blocks represent possible entry and exit points of a
function. These blocks are called `ENTRY_BLOCK_PTR` and
`EXIT_BLOCK_PTR`. These blocks do not contain any code, and are
not elements of the `BASIC_BLOCK` array. Therefore they have
been assigned unique, negative index numbers.

Each `basic_block` also contains pointers to the first
instruction (the head) and the last instruction (the tail)
or end of the instruction stream contained in a basic block. In
fact, since the `basic_block` data type is used to represent
blocks in both major intermediate representations of GCC (`tree`
and RTL), there are pointers to the head and end of a basic block for
both representations.

For RTL, these pointers are `rtx head, end`. In the RTL function
representation, the head pointer always points either to a
`NOTE_INSN_BASIC_BLOCK` or to a `CODE_LABEL`, if present.
In the RTL representation of a function, the instruction stream
contains not only the “real” instructions, but also notes.
Any function that moves or duplicates the basic blocks needs
to take care of updating of these notes. Many of these notes expect
that the instruction stream consists of linear regions, making such
updates difficult. The `NOTE_INSN_BASIC_BLOCK` note is the only
kind of note that may appear in the instruction stream contained in a
basic block. The instruction stream of a basic block always follows a
`NOTE_INSN_BASIC_BLOCK`, but zero or more `CODE_LABEL`
nodes can precede the block note. A basic block ends by control flow
instruction or last instruction before following `CODE_LABEL` or
`NOTE_INSN_BASIC_BLOCK`. A `CODE_LABEL` cannot appear in
the instruction stream of a basic block.

In addition to notes, the jump table vectors are also represented as
“pseudo-instructions” inside the insn stream. These vectors never
appear in the basic block and should always be placed just after the
table jump instructions referencing them. After removing the
table-jump it is often difficult to eliminate the code computing the
address and referencing the vector, so cleaning up these vectors is
postponed until after liveness analysis. Thus the jump table vectors
may appear in the insn stream unreferenced and without any purpose.
Before any edge is made fall-thru, the existence of such
construct in the way needs to be checked by calling
`can_fallthru` function.

For the `tree` representation, the head and end of the basic block
are being pointed to by the `stmt_list` field, but this special
`tree` should never be referenced directly. Instead, at the tree
level abstract containers and iterators are used to access statements
and expressions in basic blocks. These iterators are called
block statement iterators (BSIs). Grep for `^bsi`
in the various `tree-*` files.
The following snippet will pretty-print all the statements of the
program in the GIMPLE representation.

```
     FOR_EACH_BB (bb)
       {
          block_stmt_iterator si;

          for (si = bsi_start (bb); !bsi_end_p (si); bsi_next (&si))
            {
               tree stmt = bsi_stmt (si);
               print_generic_stmt (stderr, stmt, 0);
            }
       }
```
