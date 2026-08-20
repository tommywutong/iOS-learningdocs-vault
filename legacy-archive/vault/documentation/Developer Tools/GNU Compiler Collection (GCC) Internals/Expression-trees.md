---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Expression-trees.html
archived_at: '2026-07-15T07:30:59.813628Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Attributes](Attributes.md#apple-if2hi4tjmj2xizlt),
Up: [Trees](Trees.md#apple-krzgkzlt)

---

### 8.8 Expressions

The internal representation for expressions is for the most part quite
straightforward. However, there are a few facts that one must bear in
mind. In particular, the expression “tree” is actually a directed
acyclic graph. (For example there may be many references to the integer
constant zero throughout the source program; many of these will be
represented by the same expression node.) You should not rely on
certain kinds of node being shared, nor should rely on certain kinds of
nodes being unshared.

The following macros can be used with all expression nodes:

**`TREE_TYPE`**
: Returns the type of the expression. This value may not be precisely the
same type that would be given the expression in the original program.

In what follows, some nodes that one might expect to always have type
`bool` are documented to have either integral or boolean type. At
some point in the future, the C front end may also make use of this same
intermediate representation, and at this point these nodes will
certainly have integral type. The previous sentence is not meant to
imply that the C++ front end does not or will not give these nodes
integral type.

Below, we list the various kinds of expression nodes. Except where
noted otherwise, the operands to an expression are accessed using the
`TREE_OPERAND` macro. For example, to access the first operand to
a binary plus expression `expr`, use:

```
     TREE_OPERAND (expr, 0)
```

As this example indicates, the operands are zero-indexed.

The table below begins with constants, moves on to unary expressions,
then proceeds to binary expressions, and concludes with various other
kinds of expressions:

**`INTEGER_CST`**
: These nodes represent integer constants. Note that the type of these
constants is obtained with `TREE_TYPE`; they are not always of type
`int`. In particular, `char` constants are represented with
`INTEGER_CST` nodes. The value of the integer constant `e` is
given by

```
          ((TREE_INT_CST_HIGH (e) << HOST_BITS_PER_WIDE_INT)
          + TREE_INST_CST_LOW (e))

```

HOST_BITS_PER_WIDE_INT is at least thirty-two on all platforms. Both
`TREE_INT_CST_HIGH` and `TREE_INT_CST_LOW` return a
`HOST_WIDE_INT`. The value of an `INTEGER_CST` is interpreted
as a signed or unsigned quantity depending on the type of the constant.
In general, the expression given above will overflow, so it should not
be used to calculate the value of the constant.

The variable `integer_zero_node` is an integer constant with value
zero. Similarly, `integer_one_node` is an integer constant with
value one. The `size_zero_node` and `size_one_node` variables
are analogous, but have type `size_t` rather than `int`.

The function `tree_int_cst_lt` is a predicate which holds if its
first argument is less than its second. Both constants are assumed to
have the same signedness (i.e., either both should be signed or both
should be unsigned.) The full width of the constant is used when doing
the comparison; the usual rules about promotions and conversions are
ignored. Similarly, `tree_int_cst_equal` holds if the two
constants are equal. The `tree_int_cst_sgn` function returns the
sign of a constant. The value is `1`, `0`, or `-1`
according on whether the constant is greater than, equal to, or less
than zero. Again, the signedness of the constant's type is taken into
account; an unsigned constant is never less than zero, no matter what
its bit-pattern.

**`REAL_CST`**
: FIXME: Talk about how to obtain representations of this constant, do
comparisons, and so forth.

**`COMPLEX_CST`**
: These nodes are used to represent complex number constants, that is a
`__complex__` whose parts are constant nodes. The
`TREE_REALPART` and `TREE_IMAGPART` return the real and the
imaginary parts respectively.

**`VECTOR_CST`**
: These nodes are used to represent vector constants, whose parts are
constant nodes. Each individual constant node is either an integer or a
double constant node. The first operand is a `TREE_LIST` of the
constant nodes and is accessed through `TREE_VECTOR_CST_ELTS`.

**`STRING_CST`**
: These nodes represent string-constants. The `TREE_STRING_LENGTH`
returns the length of the string, as an `int`. The
`TREE_STRING_POINTER` is a `char*` containing the string
itself. The string may not be `NUL`-terminated, and it may contain
embedded `NUL` characters. Therefore, the
`TREE_STRING_LENGTH` includes the trailing `NUL` if it is
present.

For wide string constants, the `TREE_STRING_LENGTH` is the number
of bytes in the string, and the `TREE_STRING_POINTER`
points to an array of the bytes of the string, as represented on the
target system (that is, as integers in the target endianness). Wide and
non-wide string constants are distinguished only by the `TREE_TYPE`
of the `STRING_CST`.

FIXME: The formats of string constants are not well-defined when the
target system bytes are not the same width as host system bytes.

**`PTRMEM_CST`**
: These nodes are used to represent pointer-to-member constants. The
`PTRMEM_CST_CLASS` is the class type (either a `RECORD_TYPE`
or `UNION_TYPE` within which the pointer points), and the
`PTRMEM_CST_MEMBER` is the declaration for the pointed to object.
Note that the `DECL_CONTEXT` for the `PTRMEM_CST_MEMBER` is in
general different from the `PTRMEM_CST_CLASS`. For example,
given:

```
          struct B { int i; };
          struct D : public B {};
          int D::*dp = &D::i;

```

The `PTRMEM_CST_CLASS` for `&D::i` is `D`, even though
the `DECL_CONTEXT` for the `PTRMEM_CST_MEMBER` is `B`,
since `B::i` is a member of `B`, not `D`.

**`VAR_DECL`**
: These nodes represent variables, including static data members. For
more information, see [Declarations](Declarations.md#apple-irswg3dbojqxi2lpnzzq).

**`NEGATE_EXPR`**
: These nodes represent unary negation of the single operand, for both
integer and floating-point types. The type of negation can be
determined by looking at the type of the expression.

The behavior of this operation on signed arithmetic overflow is
controlled by the `flag_wrapv` and `flag_trapv` variables.

**`ABS_EXPR`**
: These nodes represent the absolute value of the single operand, for
both integer and floating-point types. This is typically used to
implement the `abs`, `labs` and `llabs` builtins for
integer types, and the `fabs`, `fabsf` and `fabsl`
builtins for floating point types. The type of abs operation can
be determined by looking at the type of the expression.

This node is not used for complex types. To represent the modulus
or complex abs of a complex value, use the `BUILT_IN_CABS`,
`BUILT_IN_CABSF` or `BUILT_IN_CABSL` builtins, as used
to implement the C99 `cabs`, `cabsf` and `cabsl`
built-in functions.

**`BIT_NOT_EXPR`**
: These nodes represent bitwise complement, and will always have integral
type. The only operand is the value to be complemented.

**`TRUTH_NOT_EXPR`**
: These nodes represent logical negation, and will always have integral
(or boolean) type. The operand is the value being negated. The type
of the operand and that of the result are always of `BOOLEAN_TYPE`
or `INTEGER_TYPE`.

**`PREDECREMENT_EXPR`

**`PREINCREMENT_EXPR`

**`POSTDECREMENT_EXPR`

**`POSTINCREMENT_EXPR`********
: These nodes represent increment and decrement expressions. The value of
the single operand is computed, and the operand incremented or
decremented. In the case of `PREDECREMENT_EXPR` and
`PREINCREMENT_EXPR`, the value of the expression is the value
resulting after the increment or decrement; in the case of
`POSTDECREMENT_EXPR` and `POSTINCREMENT_EXPR` is the value
before the increment or decrement occurs. The type of the operand, like
that of the result, will be either integral, boolean, or floating-point.

**`ADDR_EXPR`**
: These nodes are used to represent the address of an object. (These
expressions will always have pointer or reference type.) The operand may
be another expression, or it may be a declaration.

As an extension, GCC allows users to take the address of a label. In
this case, the operand of the `ADDR_EXPR` will be a
`LABEL_DECL`. The type of such an expression is `void*`.

If the object addressed is not an lvalue, a temporary is created, and
the address of the temporary is used.

**`INDIRECT_REF`**
: These nodes are used to represent the object pointed to by a pointer.
The operand is the pointer being dereferenced; it will always have
pointer or reference type.

**`FIX_TRUNC_EXPR`**
: These nodes represent conversion of a floating-point value to an
integer. The single operand will have a floating-point type, while the
the complete expression will have an integral (or boolean) type. The
operand is rounded towards zero.

**`FLOAT_EXPR`**
: These nodes represent conversion of an integral (or boolean) value to a
floating-point value. The single operand will have integral type, while
the complete expression will have a floating-point type.

FIXME: How is the operand supposed to be rounded? Is this dependent on
`-mieee`?

**`COMPLEX_EXPR`**
: These nodes are used to represent complex numbers constructed from two
expressions of the same (integer or real) type. The first operand is the
real part and the second operand is the imaginary part.

**`CONJ_EXPR`**
: These nodes represent the conjugate of their operand.

**`REALPART_EXPR`

**`IMAGPART_EXPR`****
: These nodes represent respectively the real and the imaginary parts
of complex numbers (their sole argument).

**`NON_LVALUE_EXPR`**
: These nodes indicate that their one and only operand is not an lvalue.
A back end can treat these identically to the single operand.

**`NOP_EXPR`**
: These nodes are used to represent conversions that do not require any
code-generation. For example, conversion of a `char*` to an
`int*` does not require any code be generated; such a conversion is
represented by a `NOP_EXPR`. The single operand is the expression
to be converted. The conversion from a pointer to a reference is also
represented with a `NOP_EXPR`.

**`CONVERT_EXPR`**
: These nodes are similar to `NOP_EXPR`s, but are used in those
situations where code may need to be generated. For example, if an
`int*` is converted to an `int` code may need to be generated
on some platforms. These nodes are never used for C++-specific
conversions, like conversions between pointers to different classes in
an inheritance hierarchy. Any adjustments that need to be made in such
cases are always indicated explicitly. Similarly, a user-defined
conversion is never represented by a `CONVERT_EXPR`; instead, the
function calls are made explicit.

**`THROW_EXPR`**
: These nodes represent `throw` expressions. The single operand is
an expression for the code that should be executed to throw the
exception. However, there is one implicit action not represented in
that expression; namely the call to `__throw`. This function takes
no arguments. If `setjmp`/`longjmp` exceptions are used, the
function `__sjthrow` is called instead. The normal GCC back end
uses the function `emit_throw` to generate this code; you can
examine this function to see what needs to be done.

**`LSHIFT_EXPR`

**`RSHIFT_EXPR`****
: These nodes represent left and right shifts, respectively. The first
operand is the value to shift; it will always be of integral type. The
second operand is an expression for the number of bits by which to
shift. Right shift should be treated as arithmetic, i.e., the
high-order bits should be zero-filled when the expression has unsigned
type and filled with the sign bit when the expression has signed type.
Note that the result is undefined if the second operand is larger
than or equal to the first operand's type size.

**`BIT_IOR_EXPR`

**`BIT_XOR_EXPR`

**`BIT_AND_EXPR`******
: These nodes represent bitwise inclusive or, bitwise exclusive or, and
bitwise and, respectively. Both operands will always have integral
type.

**`TRUTH_ANDIF_EXPR`

**`TRUTH_ORIF_EXPR`****
: These nodes represent logical and and logical or, respectively. These
operators are not strict; i.e., the second operand is evaluated only if
the value of the expression is not determined by evaluation of the first
operand. The type of the operands and that of the result are always of
`BOOLEAN_TYPE` or `INTEGER_TYPE`.

**`TRUTH_AND_EXPR`

**`TRUTH_OR_EXPR`

**`TRUTH_XOR_EXPR`******
: These nodes represent logical and, logical or, and logical exclusive or.
They are strict; both arguments are always evaluated. There are no
corresponding operators in C or C++, but the front end will sometimes
generate these expressions anyhow, if it can tell that strictness does
not matter. The type of the operands and that of the result are
always of `BOOLEAN_TYPE` or `INTEGER_TYPE`.

**`PLUS_EXPR`

**`MINUS_EXPR`

**`MULT_EXPR`******
: These nodes represent various binary arithmetic operations.
Respectively, these operations are addition, subtraction (of the second
operand from the first) and multiplication. Their operands may have
either integral or floating type, but there will never be case in which
one operand is of floating type and the other is of integral type.

The behavior of these operations on signed arithmetic overflow is
controlled by the `flag_wrapv` and `flag_trapv` variables.

**`RDIV_EXPR`**
: This node represents a floating point division operation.

**`TRUNC_DIV_EXPR`

**`FLOOR_DIV_EXPR`

**`CEIL_DIV_EXPR`

**`ROUND_DIV_EXPR`********
: These nodes represent integer division operations that return an integer
result. `TRUNC_DIV_EXPR` rounds towards zero, `FLOOR_DIV_EXPR`
rounds towards negative infinity, `CEIL_DIV_EXPR` rounds towards
positive infinity and `ROUND_DIV_EXPR` rounds to the closest integer.
Integer division in C and C++ is truncating, i.e. `TRUNC_DIV_EXPR`.

The behavior of these operations on signed arithmetic overflow, when
dividing the minimum signed integer by minus one, is controlled by the
`flag_wrapv` and `flag_trapv` variables.

**`TRUNC_MOD_EXPR`

**`FLOOR_MOD_EXPR`

**`CEIL_MOD_EXPR`

**`ROUND_MOD_EXPR`********
: These nodes represent the integer remainder or modulus operation.
The integer modulus of two operands `a` and `b` is
defined as `a - (a/b)*b` where the division calculated using
the corresponding division operator. Hence for `TRUNC_MOD_EXPR`
this definition assumes division using truncation towards zero, i.e.
`TRUNC_DIV_EXPR`. Integer remainder in C and C++ uses truncating
division, i.e. `TRUNC_MOD_EXPR`.

**`EXACT_DIV_EXPR`**
: The `EXACT_DIV_EXPR` code is used to represent integer divisions where
the numerator is known to be an exact multiple of the denominator. This
allows the backend to choose between the faster of `TRUNC_DIV_EXPR`,
`CEIL_DIV_EXPR` and `FLOOR_DIV_EXPR` for the current target.

**`ARRAY_REF`**
: These nodes represent array accesses. The first operand is the array;
the second is the index. To calculate the address of the memory
accessed, you must scale the index by the size of the type of the array
elements. The type of these expressions must be the type of a component of
the array. The third and fourth operands are used after gimplification
to represent the lower bound and component size but should not be used
directly; call `array_ref_low_bound` and `array_ref_element_size`
instead.

**`ARRAY_RANGE_REF`**
: These nodes represent access to a range (or “slice”) of an array. The
operands are the same as that for `ARRAY_REF` and have the same
meanings. The type of these expressions must be an array whose component
type is the same as that of the first operand. The range of that array
type determines the amount of data these expressions access.

**`LT_EXPR`

**`LE_EXPR`

**`GT_EXPR`

**`GE_EXPR`

**`EQ_EXPR`

**`NE_EXPR`************
: These nodes represent the less than, less than or equal to, greater
than, greater than or equal to, equal, and not equal comparison
operators. The first and second operand with either be both of integral
type or both of floating type. The result type of these expressions
will always be of integral or boolean type. These operations return
the result type's zero value for false, and the result type's one value
for true.

For floating point comparisons, if we honor IEEE NaNs and either operand
is NaN, then `NE_EXPR` always returns true and the remaining operators
always return false. On some targets, comparisons against an IEEE NaN,
other than equality and inequality, may generate a floating point exception.

**`ORDERED_EXPR`

**`UNORDERED_EXPR`****
: These nodes represent non-trapping ordered and unordered comparison
operators. These operations take two floating point operands and
determine whether they are ordered or unordered relative to each other.
If either operand is an IEEE NaN, their comparison is defined to be
unordered, otherwise the comparison is defined to be ordered. The
result type of these expressions will always be of integral or boolean
type. These operations return the result type's zero value for false,
and the result type's one value for true.

**`UNLT_EXPR`

**`UNLE_EXPR`

**`UNGT_EXPR`

**`UNGE_EXPR`

**`UNEQ_EXPR`

**`LTGT_EXPR`************
: These nodes represent the unordered comparison operators.
These operations take two floating point operands and determine whether
the operands are unordered or are less than, less than or equal to,
greater than, greater than or equal to, or equal respectively. For
example, `UNLT_EXPR` returns true if either operand is an IEEE
NaN or the first operand is less than the second. With the possible
exception of `LTGT_EXPR`, all of these operations are guaranteed
not to generate a floating point exception. The result
type of these expressions will always be of integral or boolean type.
These operations return the result type's zero value for false,
and the result type's one value for true.

**`MODIFY_EXPR`**
: These nodes represent assignment. The left-hand side is the first
operand; the right-hand side is the second operand. The left-hand side
will be a `VAR_DECL`, `INDIRECT_REF`, `COMPONENT_REF`, or
other lvalue.

These nodes are used to represent not only assignment with ``=`' but
also compound assignments (like ``+=`'), by reduction to ``=`'
assignment. In other words, the representation for ``i += 3`' looks
just like that for ``i = i + 3`'.

**`INIT_EXPR`**
: These nodes are just like `MODIFY_EXPR`, but are used only when a
variable is initialized, rather than assigned to subsequently.

**`COMPONENT_REF`**
: These nodes represent non-static data member accesses. The first
operand is the object (rather than a pointer to it); the second operand
is the `FIELD_DECL` for the data member. The third operand represents
the byte offset of the field, but should not be used directly; call
`component_ref_field_offset` instead.

**`COMPOUND_EXPR`**
: These nodes represent comma-expressions. The first operand is an
expression whose value is computed and thrown away prior to the
evaluation of the second operand. The value of the entire expression is
the value of the second operand.

**`COND_EXPR`**
: These nodes represent `?:` expressions. The first operand
is of boolean or integral type. If it evaluates to a nonzero value,
the second operand should be evaluated, and returned as the value of the
expression. Otherwise, the third operand is evaluated, and returned as
the value of the expression.

The second operand must have the same type as the entire expression,
unless it unconditionally throws an exception or calls a noreturn
function, in which case it should have void type. The same constraints
apply to the third operand. This allows array bounds checks to be
represented conveniently as `(i >= 0 && i < 10) ? i : abort()`.

As a GNU extension, the C language front-ends allow the second
operand of the `?:` operator may be omitted in the source.
For example, `x ? : 3` is equivalent to `x ? x : 3`,
assuming that `x` is an expression without side-effects.
In the tree representation, however, the second operand is always
present, possibly protected by `SAVE_EXPR` if the first
argument does cause side-effects.

**`CALL_EXPR`**
: These nodes are used to represent calls to functions, including
non-static member functions. The first operand is a pointer to the
function to call; it is always an expression whose type is a
`POINTER_TYPE`. The second argument is a `TREE_LIST`. The
arguments to the call appear left-to-right in the list. The
`TREE_VALUE` of each list node contains the expression
corresponding to that argument. (The value of `TREE_PURPOSE` for
these nodes is unspecified, and should be ignored.) For non-static
member functions, there will be an operand corresponding to the
`this` pointer. There will always be expressions corresponding to
all of the arguments, even if the function is declared with default
arguments and some arguments are not explicitly provided at the call
sites.

**`STMT_EXPR`**
: These nodes are used to represent GCC's statement-expression extension.
The statement-expression extension allows code like this:

```
          int f() { return ({ int j; j = 3; j + 7; }); }

```

In other words, an sequence of statements may occur where a single
expression would normally appear. The `STMT_EXPR` node represents
such an expression. The `STMT_EXPR_STMT` gives the statement
contained in the expression. The value of the expression is the value
of the last sub-statement in the body. More precisely, the value is the
value computed by the last statement nested inside `BIND_EXPR`,
`TRY_FINALLY_EXPR`, or `TRY_CATCH_EXPR`. For example, in:

```
          ({ 3; })

```

the value is `3` while in:

```
          ({ if (x) { 3; } })

```

there is no value. If the `STMT_EXPR` does not yield a value,
it's type will be `void`.

**`BIND_EXPR`**
: These nodes represent local blocks. The first operand is a list of
variables, connected via their `TREE_CHAIN` field. These will
never require cleanups. The scope of these variables is just the body
of the `BIND_EXPR`. The body of the `BIND_EXPR` is the
second operand.

**`LOOP_EXPR`**
: These nodes represent “infinite” loops. The `LOOP_EXPR_BODY`
represents the body of the loop. It should be executed forever, unless
an `EXIT_EXPR` is encountered.

**`EXIT_EXPR`**
: These nodes represent conditional exits from the nearest enclosing
`LOOP_EXPR`. The single operand is the condition; if it is
nonzero, then the loop should be exited. An `EXIT_EXPR` will only
appear within a `LOOP_EXPR`.

**`CLEANUP_POINT_EXPR`**
: These nodes represent full-expressions. The single operand is an
expression to evaluate. Any destructor calls engendered by the creation
of temporaries during the evaluation of that expression should be
performed immediately after the expression is evaluated.

**`CONSTRUCTOR`**
: These nodes represent the brace-enclosed initializers for a structure or
array. The first operand is reserved for use by the back end. The
second operand is a `TREE_LIST`. If the `TREE_TYPE` of the
`CONSTRUCTOR` is a `RECORD_TYPE` or `UNION_TYPE`, then
the `TREE_PURPOSE` of each node in the `TREE_LIST` will be a
`FIELD_DECL` and the `TREE_VALUE` of each node will be the
expression used to initialize that field.

If the `TREE_TYPE` of the `CONSTRUCTOR` is an
`ARRAY_TYPE`, then the `TREE_PURPOSE` of each element in the
`TREE_LIST` will be an `INTEGER_CST` or a `RANGE_EXPR` of
two `INTEGER_CST`s. A single `INTEGER_CST` indicates which
element of the array (indexed from zero) is being assigned to. A
`RANGE_EXPR` indicates an inclusive range of elements to
initialize. In both cases the `TREE_VALUE` is the corresponding
initializer. It is re-evaluated for each element of a
`RANGE_EXPR`. If the `TREE_PURPOSE` is `NULL_TREE`, then
the initializer is for the next available array element.

In the front end, you should not depend on the fields appearing in any
particular order. However, in the middle end, fields must appear in
declaration order. You should not assume that all fields will be
represented. Unrepresented fields will be set to zero.

**`COMPOUND_LITERAL_EXPR`**
: These nodes represent ISO C99 compound literals. The
`COMPOUND_LITERAL_EXPR_DECL_STMT` is a `DECL_STMT`
containing an anonymous `VAR_DECL` for
the unnamed object represented by the compound literal; the
`DECL_INITIAL` of that `VAR_DECL` is a `CONSTRUCTOR`
representing the brace-enclosed list of initializers in the compound
literal. That anonymous `VAR_DECL` can also be accessed directly
by the `COMPOUND_LITERAL_EXPR_DECL` macro.

**`SAVE_EXPR`**
: A `SAVE_EXPR` represents an expression (possibly involving
side-effects) that is used more than once. The side-effects should
occur only the first time the expression is evaluated. Subsequent uses
should just reuse the computed value. The first operand to the
`SAVE_EXPR` is the expression to evaluate. The side-effects should
be executed where the `SAVE_EXPR` is first encountered in a
depth-first preorder traversal of the expression tree.

**`TARGET_EXPR`**
: A `TARGET_EXPR` represents a temporary object. The first operand
is a `VAR_DECL` for the temporary variable. The second operand is
the initializer for the temporary. The initializer is evaluated and,
if non-void, copied (bitwise) into the temporary. If the initializer
is void, that means that it will perform the initialization itself.

Often, a `TARGET_EXPR` occurs on the right-hand side of an
assignment, or as the second operand to a comma-expression which is
itself the right-hand side of an assignment, etc. In this case, we say
that the `TARGET_EXPR` is “normal”; otherwise, we say it is
“orphaned”. For a normal `TARGET_EXPR` the temporary variable
should be treated as an alias for the left-hand side of the assignment,
rather than as a new temporary variable.

The third operand to the `TARGET_EXPR`, if present, is a
cleanup-expression (i.e., destructor call) for the temporary. If this
expression is orphaned, then this expression must be executed when the
statement containing this expression is complete. These cleanups must
always be executed in the order opposite to that in which they were
encountered. Note that if a temporary is created on one branch of a
conditional operator (i.e., in the second or third operand to a
`COND_EXPR`), the cleanup must be run only if that branch is
actually executed.

See `STMT_IS_FULL_EXPR_P` for more information about running these
cleanups.

**`AGGR_INIT_EXPR`**
: An `AGGR_INIT_EXPR` represents the initialization as the return
value of a function call, or as the result of a constructor. An
`AGGR_INIT_EXPR` will only appear as a full-expression, or as the
second operand of a `TARGET_EXPR`. The first operand to the
`AGGR_INIT_EXPR` is the address of a function to call, just as in
a `CALL_EXPR`. The second operand are the arguments to pass that
function, as a `TREE_LIST`, again in a manner similar to that of
a `CALL_EXPR`.

If `AGGR_INIT_VIA_CTOR_P` holds of the `AGGR_INIT_EXPR`, then
the initialization is via a constructor call. The address of the third
operand of the `AGGR_INIT_EXPR`, which is always a `VAR_DECL`,
is taken, and this value replaces the first argument in the argument
list.

In either case, the expression is void.

**`VA_ARG_EXPR`**
: This node is used to implement support for the C/C++ variable argument-list
mechanism. It represents expressions like `va_arg (ap, type)`.
Its `TREE_TYPE` yields the tree representation for `type` and
its sole argument yields the representation for `ap`.
