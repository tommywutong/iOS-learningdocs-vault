---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Types.html
archived_at: '2026-07-15T07:31:00.973596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Scopes](Scopes.md#apple-knrw64dfom),
Previous: [Tree overview](Tree-overview.md#apple-krzgkzjnn53gk4twnfsxo),
Up: [Trees](Trees.md#apple-krzgkzlt)

---

### 8.3 Types

All types have corresponding tree nodes. However, you should not assume
that there is exactly one tree node corresponding to each type. There
are often several nodes each of which correspond to the same type.

For the most part, different kinds of types have different tree codes.
(For example, pointer types use a `POINTER_TYPE` code while arrays
use an `ARRAY_TYPE` code.) However, pointers to member functions
use the `RECORD_TYPE` code. Therefore, when writing a
`switch` statement that depends on the code associated with a
particular type, you should take care to handle pointers to member
functions under the `RECORD_TYPE` case label.

In C++, an array type is not qualified; rather the type of the array
elements is qualified. This situation is reflected in the intermediate
representation. The macros described here will always examine the
qualification of the underlying element type when applied to an array
type. (If the element type is itself an array, then the recursion
continues until a non-array type is found, and the qualification of this
type is examined.) So, for example, `CP_TYPE_CONST_P` will hold of
the type `const int ()[7]`, denoting an array of seven `int`s.

The following functions and macros deal with cv-qualification of types:

**`CP_TYPE_QUALS`**
: This macro returns the set of type qualifiers applied to this type.
This value is `TYPE_UNQUALIFIED` if no qualifiers have been
applied. The `TYPE_QUAL_CONST` bit is set if the type is
`const`-qualified. The `TYPE_QUAL_VOLATILE` bit is set if the
type is `volatile`-qualified. The `TYPE_QUAL_RESTRICT` bit is
set if the type is `restrict`-qualified.

**`CP_TYPE_CONST_P`**
: This macro holds if the type is `const`-qualified.

**`CP_TYPE_VOLATILE_P`**
: This macro holds if the type is `volatile`-qualified.

**`CP_TYPE_RESTRICT_P`**
: This macro holds if the type is `restrict`-qualified.

**`CP_TYPE_CONST_NON_VOLATILE_P`**
: This predicate holds for a type that is `const`-qualified, but
_not_ `volatile`-qualified; other cv-qualifiers are ignored as
well: only the `const`-ness is tested.

**`TYPE_MAIN_VARIANT`**
: This macro returns the unqualified version of a type. It may be applied
to an unqualified type, but it is not always the identity function in
that case.

A few other macros and functions are usable with all types:

**`TYPE_SIZE`**
: The number of bits required to represent the type, represented as an
`INTEGER_CST`. For an incomplete type, `TYPE_SIZE` will be
`NULL_TREE`.

**`TYPE_ALIGN`**
: The alignment of the type, in bits, represented as an `int`.

**`TYPE_NAME`**
: This macro returns a declaration (in the form of a `TYPE_DECL`) for
the type. (Note this macro does _not_ return a
`IDENTIFIER_NODE`, as you might expect, given its name!) You can
look at the `DECL_NAME` of the `TYPE_DECL` to obtain the
actual name of the type. The `TYPE_NAME` will be `NULL_TREE`
for a type that is not a built-in type, the result of a typedef, or a
named class type.

**`CP_INTEGRAL_TYPE`**
: This predicate holds if the type is an integral type. Notice that in
C++, enumerations are _not_ integral types.

**`ARITHMETIC_TYPE_P`**
: This predicate holds if the type is an integral type (in the C++ sense)
or a floating point type.

**`CLASS_TYPE_P`**
: This predicate holds for a class-type.

**`TYPE_BUILT_IN`**
: This predicate holds for a built-in type.

**`TYPE_PTRMEM_P`**
: This predicate holds if the type is a pointer to data member.

**`TYPE_PTR_P`**
: This predicate holds if the type is a pointer type, and the pointee is
not a data member.

**`TYPE_PTRFN_P`**
: This predicate holds for a pointer to function type.

**`TYPE_PTROB_P`**
: This predicate holds for a pointer to object type. Note however that it
does not hold for the generic pointer to object type `void *`. You
may use `TYPE_PTROBV_P` to test for a pointer to object type as
well as `void *`.

**`same_type_p`**
: This predicate takes two types as input, and holds if they are the same
type. For example, if one type is a `typedef` for the other, or
both are `typedef`s for the same type. This predicate also holds if
the two trees given as input are simply copies of one another; i.e.,
there is no difference between them at the source level, but, for
whatever reason, a duplicate has been made in the representation. You
should never use `==` (pointer equality) to compare types; always
use `same_type_p` instead.

Detailed below are the various kinds of types, and the macros that can
be used to access them. Although other kinds of types are used
elsewhere in G++, the types described here are the only ones that you
will encounter while examining the intermediate representation.

**`VOID_TYPE`**
: Used to represent the `void` type.

**`INTEGER_TYPE`**
: Used to represent the various integral types, including `char`,
`short`, `int`, `long`, and `long long`. This code
is not used for enumeration types, nor for the `bool` type. Note
that GCC's `CHAR_TYPE` node is _not_ used to represent
`char`. The `TYPE_PRECISION` is the number of bits used in
the representation, represented as an `unsigned int`. (Note that
in the general case this is not the same value as `TYPE_SIZE`;
suppose that there were a 24-bit integer type, but that alignment
requirements for the ABI required 32-bit alignment. Then,
`TYPE_SIZE` would be an `INTEGER_CST` for 32, while
`TYPE_PRECISION` would be 24.) The integer type is unsigned if
`TYPE_UNSIGNED` holds; otherwise, it is signed.

The `TYPE_MIN_VALUE` is an `INTEGER_CST` for the smallest
integer that may be represented by this type. Similarly, the
`TYPE_MAX_VALUE` is an `INTEGER_CST` for the largest integer
that may be represented by this type.

**`REAL_TYPE`**
: Used to represent the `float`, `double`, and `long
double` types. The number of bits in the floating-point representation
is given by `TYPE_PRECISION`, as in the `INTEGER_TYPE` case.

**`COMPLEX_TYPE`**
: Used to represent GCC built-in `__complex__` data types. The
`TREE_TYPE` is the type of the real and imaginary parts.

**`ENUMERAL_TYPE`**
: Used to represent an enumeration type. The `TYPE_PRECISION` gives
(as an `int`), the number of bits used to represent the type. If
there are no negative enumeration constants, `TYPE_UNSIGNED` will
hold. The minimum and maximum enumeration constants may be obtained
with `TYPE_MIN_VALUE` and `TYPE_MAX_VALUE`, respectively; each
of these macros returns an `INTEGER_CST`.

The actual enumeration constants themselves may be obtained by looking
at the `TYPE_VALUES`. This macro will return a `TREE_LIST`,
containing the constants. The `TREE_PURPOSE` of each node will be
an `IDENTIFIER_NODE` giving the name of the constant; the
`TREE_VALUE` will be an `INTEGER_CST` giving the value
assigned to that constant. These constants will appear in the order in
which they were declared. The `TREE_TYPE` of each of these
constants will be the type of enumeration type itself.

**`BOOLEAN_TYPE`**
: Used to represent the `bool` type.

**`POINTER_TYPE`**
: Used to represent pointer types, and pointer to data member types. The
`TREE_TYPE` gives the type to which this type points. If the type
is a pointer to data member type, then `TYPE_PTRMEM_P` will hold.
For a pointer to data member type of the form ``T X::*`',
`TYPE_PTRMEM_CLASS_TYPE` will be the type `X`, while
`TYPE_PTRMEM_POINTED_TO_TYPE` will be the type `T`.

**`REFERENCE_TYPE`**
: Used to represent reference types. The `TREE_TYPE` gives the type
to which this type refers.

**`FUNCTION_TYPE`**
: Used to represent the type of non-member functions and of static member
functions. The `TREE_TYPE` gives the return type of the function.
The `TYPE_ARG_TYPES` are a `TREE_LIST` of the argument types.
The `TREE_VALUE` of each node in this list is the type of the
corresponding argument; the `TREE_PURPOSE` is an expression for the
default argument value, if any. If the last node in the list is
`void_list_node` (a `TREE_LIST` node whose `TREE_VALUE`
is the `void_type_node`), then functions of this type do not take
variable arguments. Otherwise, they do take a variable number of
arguments.

Note that in C (but not in C++) a function declared like `void f()`
is an unprototyped function taking a variable number of arguments; the
`TYPE_ARG_TYPES` of such a function will be `NULL`.

**`METHOD_TYPE`**
: Used to represent the type of a non-static member function. Like a
`FUNCTION_TYPE`, the return type is given by the `TREE_TYPE`.
The type of `*this`, i.e., the class of which functions of this
type are a member, is given by the `TYPE_METHOD_BASETYPE`. The
`TYPE_ARG_TYPES` is the parameter list, as for a
`FUNCTION_TYPE`, and includes the `this` argument.

**`ARRAY_TYPE`**
: Used to represent array types. The `TREE_TYPE` gives the type of
the elements in the array. If the array-bound is present in the type,
the `TYPE_DOMAIN` is an `INTEGER_TYPE` whose
`TYPE_MIN_VALUE` and `TYPE_MAX_VALUE` will be the lower and
upper bounds of the array, respectively. The `TYPE_MIN_VALUE` will
always be an `INTEGER_CST` for zero, while the
`TYPE_MAX_VALUE` will be one less than the number of elements in
the array, i.e., the highest value which may be used to index an element
in the array.

**`RECORD_TYPE`**
: Used to represent `struct` and `class` types, as well as
pointers to member functions and similar constructs in other languages.
`TYPE_FIELDS` contains the items contained in this type, each of
which can be a `FIELD_DECL`, `VAR_DECL`, `CONST_DECL`, or
`TYPE_DECL`. You may not make any assumptions about the ordering
of the fields in the type or whether one or more of them overlap. If
`TYPE_PTRMEMFUNC_P` holds, then this type is a pointer-to-member
type. In that case, the `TYPE_PTRMEMFUNC_FN_TYPE` is a
`POINTER_TYPE` pointing to a `METHOD_TYPE`. The
`METHOD_TYPE` is the type of a function pointed to by the
pointer-to-member function. If `TYPE_PTRMEMFUNC_P` does not hold,
this type is a class type. For more information, see see [Classes](Classes.md#apple-inwgc43tmvzq).

**`UNION_TYPE`**
: Used to represent `union` types. Similar to `RECORD_TYPE`
except that all `FIELD_DECL` nodes in `TYPE_FIELD` start at
bit position zero.

**`QUAL_UNION_TYPE`**
: Used to represent part of a variant record in Ada. Similar to
`UNION_TYPE` except that each `FIELD_DECL` has a
`DECL_QUALIFIER` field, which contains a boolean expression that
indicates whether the field is present in the object. The type will only
have one field, so each field's `DECL_QUALIFIER` is only evaluated
if none of the expressions in the previous fields in `TYPE_FIELDS`
are nonzero. Normally these expressions will reference a field in the
outer object using a `PLACEHOLDER_EXPR`.

**`UNKNOWN_TYPE`**
: This node is used to represent a type the knowledge of which is
insufficient for a sound processing.

**`OFFSET_TYPE`**
: This node is used to represent a pointer-to-data member. For a data
member `X::m` the `TYPE_OFFSET_BASETYPE` is `X` and the
`TREE_TYPE` is the type of `m`.

**`TYPENAME_TYPE`**
: Used to represent a construct of the form `typename T::A`. The
`TYPE_CONTEXT` is `T`; the `TYPE_NAME` is an
`IDENTIFIER_NODE` for `A`. If the type is specified via a
template-id, then `TYPENAME_TYPE_FULLNAME` yields a
`TEMPLATE_ID_EXPR`. The `TREE_TYPE` is non-`NULL` if the
node is implicitly generated in support for the implicit typename
extension; in which case the `TREE_TYPE` is a type node for the
base-class.

**`TYPEOF_TYPE`**
: Used to represent the `__typeof__` extension. The
`TYPE_FIELDS` is the expression the type of which is being
represented.

There are variables whose values represent some of the basic types.
These include:

**`void_type_node`**
: A node for `void`.

**`integer_type_node`**
: A node for `int`.

**`unsigned_type_node.`**
: A node for `unsigned int`.

**`char_type_node.`**
: A node for `char`.

It may sometimes be useful to compare one of these variables with a type
in hand, using `same_type_p`.
