---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/GTY-Options.html
archived_at: '2026-07-15T07:31:00.005731Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [GGC Roots](GGC-Roots.md#apple-i5duglksn5xxi4y),
Up: [Type Information](Type-Information.md#apple-kr4xazjnjfxgm33snvqxi2lpny)

---

### 18.1 The Inside of a `GTY(())`

Sometimes the C code is not enough to fully describe the type
structure. Extra information can be provided with `GTY` options
and additional markers. Some options take a parameter, which may be
either a string or a type name, depending on the parameter. If an
option takes no parameter, it is acceptable either to omit the
parameter entirely, or to provide an empty string as a parameter. For
example, `GTY ((skip))` and `GTY ((skip ("")))` are
equivalent.

When the parameter is a string, often it is a fragment of C code. Four
special escapes may be used in these strings, to refer to pieces of
the data structure being marked:

**`%h`**
: The current structure.

**`%1`**
: The structure that immediately contains the current structure.

**`%0`**
: The outermost structure that contains the current structure.

**`%a`**
: A partial expression of the form `[i1][i2]...` that indexes
the array item currently being marked.

For instance, suppose that you have a structure of the form

```
     struct A {
       ...
     };
     struct B {
       struct A foo[12];
     };
```

and `b` is a variable of type `struct B`. When marking
``b.foo[11]`', `%h` would expand to ``b.foo[11]`',
`%0` and `%1` would both expand to ``b`', and `%a`
would expand to ``[11]`'.

As in ordinary C, adjacent strings will be concatenated; this is
helpful when you have a complicated expression.

```
     GTY ((chain_next ("TREE_CODE (&%h.generic) == INTEGER_TYPE"
                       " ? TYPE_NEXT_VARIANT (&%h.generic)"
                       " : TREE_CHAIN (&%h.generic)")))
```

The available options are:

**`length ("`expression`")`**
: There are two places the type machinery will need to be explicitly told
the length of an array. The first case is when a structure ends in a
variable-length array, like this:

```
          struct rtvec_def GTY(()) {
            int num_elem;		/* number of elements */
            rtx GTY ((length ("%h.num_elem"))) elem[1];
          };

```

In this case, the `length` option is used to override the specified
array length (which should usually be `1`). The parameter of the
option is a fragment of C code that calculates the length.

The second case is when a structure or a global variable contains a
pointer to an array, like this:

```
          tree *
            GTY ((length ("%h.regno_pointer_align_length"))) regno_decl;

```

In this case, `regno_decl` has been allocated by writing something like

```swift
            x->regno_decl =
              ggc_alloc (x->regno_pointer_align_length * sizeof (tree));

```

and the `length` provides the length of the field.

This second use of `length` also works on global variables, like:

```

       static GTY((length ("reg_base_value_size")))
         rtx *reg_base_value;
```


**`skip`**
: If `skip` is applied to a field, the type machinery will ignore it.
This is somewhat dangerous; the only safe use is in a union when one
field really isn't ever used.

**`desc ("`expression`")`

**`tag ("`constant`")`

**`default`******
: The type machinery needs to be told which field of a `union` is
currently active. This is done by giving each field a constant
`tag` value, and then specifying a discriminator using `desc`.
The value of the expression given by `desc` is compared against
each `tag` value, each of which should be different. If no
`tag` is matched, the field marked with `default` is used if
there is one, otherwise no field in the union will be marked.

In the `desc` option, the “current structure” is the union that
it discriminates. Use `%1` to mean the structure containing it.
There are no escapes available to the `tag` option, since it is a
constant.

For example,

```
          struct tree_binding GTY(())
          {
            struct tree_common common;
            union tree_binding_u {
              tree GTY ((tag ("0"))) scope;
              struct cp_binding_level * GTY ((tag ("1"))) level;
            } GTY ((desc ("BINDING_HAS_LEVEL_P ((tree)&%0)"))) xscope;
            tree value;
          };

```

In this example, the value of BINDING_HAS_LEVEL_P when applied to a
`struct tree_binding *` is presumed to be 0 or 1. If 1, the type
mechanism will treat the field `level` as being present and if 0,
will treat the field `scope` as being present.

**`param_is (`type`)`

**`use_param`****
: Sometimes it's convenient to define some data structure to work on
generic pointers (that is, `PTR`) and then use it with a specific
type. `param_is` specifies the real type pointed to, and
`use_param` says where in the generic data structure that type
should be put.

For instance, to have a `htab_t` that points to trees, one would
write the definition of `htab_t` like this:

```
          typedef struct GTY(()) {
            ...
            void ** GTY ((use_param, ...)) entries;
            ...
          } htab_t;

```

and then declare variables like this:

```
            static htab_t GTY ((param_is (union tree_node))) ict;

```


**`param`n`_is (`type`)`

**`use_param`n****
: In more complicated cases, the data structure might need to work on
several different types, which might not necessarily all be pointers.
For this, `param1_is` through `param9_is` may be used to
specify the real type of a field identified by `use_param1` through
`use_param9`.

**`use_params`**
: When a structure contains another structure that is parameterized,
there's no need to do anything special, the inner structure inherits the
parameters of the outer one. When a structure contains a pointer to a
parameterized structure, the type machinery won't automatically detect
this (it could, it just doesn't yet), so it's necessary to tell it that
the pointed-to structure should use the same parameters as the outer
structure. This is done by marking the pointer with the
`use_params` option.

**`deletable`**
: `deletable`, when applied to a global variable, indicates that when
garbage collection runs, there's no need to mark anything pointed to
by this variable, it can just be set to `NULL` instead. This is used
to keep a list of free structures around for re-use.

**`if_marked ("`expression`")`**
: Suppose you want some kinds of object to be unique, and so you put them
in a hash table. If garbage collection marks the hash table, these
objects will never be freed, even if the last other reference to them
goes away. GGC has special handling to deal with this: if you use the
`if_marked` option on a global hash table, GGC will call the
routine whose name is the parameter to the option on each hash table
entry. If the routine returns nonzero, the hash table entry will
be marked as usual. If the routine returns zero, the hash table entry
will be deleted.

The routine `ggc_marked_p` can be used to determine if an element
has been marked already; in fact, the usual case is to use
`if_marked ("ggc_marked_p")`.

**`maybe_undef`**
: When applied to a field, `maybe_undef` indicates that it's OK if
the structure that this fields points to is never defined, so long as
this field is always `NULL`. This is used to avoid requiring
backends to define certain optional structures. It doesn't work with
language frontends.

**`nested_ptr (`type`, "`to expression`", "`from expression`")`**
: The type machinery expects all pointers to point to the start of an
object. Sometimes for abstraction purposes it's convenient to have
a pointer which points inside an object. So long as it's possible to
convert the original object to and from the pointer, such pointers
can still be used. type is the type of the original object,
the to expression returns the pointer given the original object,
and the from expression returns the original object given
the pointer. The pointer will be available using the `%h`
escape.

**`chain_next ("`expression`")`

**`chain_prev ("`expression`")`****
: It's helpful for the type machinery to know if objects are often
chained together in long lists; this lets it generate code that uses
less stack space by iterating along the list instead of recursing down
it. `chain_next` is an expression for the next item in the list,
`chain_prev` is an expression for the previous item. For singly
linked lists, use only `chain_next`; for doubly linked lists, use
both. The machinery requires that taking the next item of the
previous item gives the original item.

**`reorder ("`function name`")`**
: Some data structures depend on the relative ordering of pointers. If
the precompiled header machinery needs to change that ordering, it
will call the function referenced by the `reorder` option, before
changing the pointers in the object that's pointed to by the field the
option applies to. The function must take four arguments, with the
signature ``void *, void *, gt_pointer_operator, void *`'.
The first parameter is a pointer to the structure that contains the
object being updated, or the object itself if there is no containing
structure. The second parameter is a cookie that should be ignored.
The third parameter is a routine that, given a pointer, will update it
to its correct new value. The fourth parameter is a cookie that must
be passed to the second parameter.

PCH cannot handle data structures that depend on the absolute values
of pointers. `reorder` functions can be expensive. When
possible, it is better to depend on properties of the data, like an ID
number or the hash of a string instead.

**`special ("`name`")`**
: The `special` option is used to mark types that have to be dealt
with by special case machinery. The parameter is the name of the
special case. See `gengtype.c` for further details. Avoid
adding new special cases unless there is no other alternative.
