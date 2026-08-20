---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Function-Bodies.html
archived_at: '2026-07-15T07:31:01.937736Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Function Basics](Function-Basics.md#apple-iz2w4y3unfxw4lkcmfzwsy3t),
Up: [Functions](Functions.md#apple-iz2w4y3unfxw44y)

---

#### 9.6.2 Function Bodies

A function that has a definition in the current translation unit will
have a non-`NULL` `DECL_INITIAL`. However, back ends should not make
use of the particular value given by `DECL_INITIAL`.

The `DECL_SAVED_TREE` macro will give the complete body of the
function.

##### 9.6.2.1 Statements

There are tree nodes corresponding to all of the source-level
statement constructs, used within the C and C++ frontends. These are
enumerated here, together with a list of the various macros that can
be used to obtain information about them. There are a few macros that
can be used with all statements:

**`STMT_IS_FULL_EXPR_P`**
: In C++, statements normally constitute “full expressions”; temporaries
created during a statement are destroyed when the statement is complete.
However, G++ sometimes represents expressions by statements; these
statements will not have `STMT_IS_FULL_EXPR_P` set. Temporaries
created during such statements should be destroyed when the innermost
enclosing statement with `STMT_IS_FULL_EXPR_P` set is exited.

Here is the list of the various statement nodes, and the macros used to
access them. This documentation describes the use of these nodes in
non-template functions (including instantiations of template functions).
In template functions, the same nodes are used, but sometimes in
slightly different ways.

Many of the statements have substatements. For example, a `while`
loop will have a body, which is itself a statement. If the substatement
is `NULL_TREE`, it is considered equivalent to a statement
consisting of a single `;`, i.e., an expression statement in which
the expression has been omitted. A substatement may in fact be a list
of statements, connected via their `TREE_CHAIN`s. So, you should
always process the statement tree by looping over substatements, like
this:

```
     void process_stmt (stmt)
          tree stmt;
     {
       while (stmt)
         {
           switch (TREE_CODE (stmt))
             {
             case IF_STMT:
               process_stmt (THEN_CLAUSE (stmt));
               /* More processing here.  */
               break;

             ...
             }

           stmt = TREE_CHAIN (stmt);
         }
     }
```

In other words, while the `then` clause of an `if` statement
in C++ can be only one statement (although that one statement may be a
compound statement), the intermediate representation will sometimes use
several statements chained together.

**`ASM_EXPR`**
: Used to represent an inline assembly statement. For an inline assembly
statement like:

```
          asm ("mov x, y");

```

The `ASM_STRING` macro will return a `STRING_CST` node for
`"mov x, y"`. If the original statement made use of the
extended-assembly syntax, then `ASM_OUTPUTS`,
`ASM_INPUTS`, and `ASM_CLOBBERS` will be the outputs, inputs,
and clobbers for the statement, represented as `STRING_CST` nodes.
The extended-assembly syntax looks like:

```
          asm ("fsinx %1,%0" : "=f" (result) : "f" (angle));

```

The first string is the `ASM_STRING`, containing the instruction
template. The next two strings are the output and inputs, respectively;
this statement has no clobbers. As this example indicates, “plain”
assembly statements are merely a special case of extended assembly
statements; they have no cv-qualifiers, outputs, inputs, or clobbers.
All of the strings will be `NUL`-terminated, and will contain no
embedded `NUL`-characters.

If the assembly statement is declared `volatile`, or if the
statement was not an extended assembly statement, and is therefore
implicitly volatile, then the predicate `ASM_VOLATILE_P` will hold
of the `ASM_EXPR`.
`ASM_USES` and `ASM_LABEL` are for CW assembly syntax only,
providing REG_USE and label declaration information inside `ASM_EXPR`
tree.

**`BREAK_STMT`**
: Used to represent a `break` statement. There are no additional
fields.

**`CASE_LABEL_EXPR`**
: Use to represent a `case` label, range of `case` labels, or a
`default` label. If `CASE_LOW` is `NULL_TREE`, then this is a
`default` label. Otherwise, if `CASE_HIGH` is `NULL_TREE`, then
this is an ordinary `case` label. In this case, `CASE_LOW` is
an expression giving the value of the label. Both `CASE_LOW` and
`CASE_HIGH` are `INTEGER_CST` nodes. These values will have
the same type as the condition expression in the switch statement.

Otherwise, if both `CASE_LOW` and `CASE_HIGH` are defined, the
statement is a range of case labels. Such statements originate with the
extension that allows users to write things of the form:

```
          case 2 ... 5:

```

The first value will be `CASE_LOW`, while the second will be
`CASE_HIGH`.

**`CLEANUP_STMT`**
: Used to represent an action that should take place upon exit from the
enclosing scope. Typically, these actions are calls to destructors for
local objects, but back ends cannot rely on this fact. If these nodes
are in fact representing such destructors, `CLEANUP_DECL` will be
the `VAR_DECL` destroyed. Otherwise, `CLEANUP_DECL` will be
`NULL_TREE`. In any case, the `CLEANUP_EXPR` is the
expression to execute. The cleanups executed on exit from a scope
should be run in the reverse order of the order in which the associated
`CLEANUP_STMT`s were encountered.

**`CONTINUE_STMT`**
: Used to represent a `continue` statement. There are no additional
fields.

**`CTOR_STMT`**
: Used to mark the beginning (if `CTOR_BEGIN_P` holds) or end (if
`CTOR_END_P` holds of the main body of a constructor. See also
`SUBOBJECT` for more information on how to use these nodes.

**`DECL_STMT`**
: Used to represent a local declaration. The `DECL_STMT_DECL` macro
can be used to obtain the entity declared. This declaration may be a
`LABEL_DECL`, indicating that the label declared is a local label.
(As an extension, GCC allows the declaration of labels with scope.) In
C, this declaration may be a `FUNCTION_DECL`, indicating the
use of the GCC nested function extension. For more information,
see [Functions](Functions.md#apple-iz2w4y3unfxw44y).

**`DO_STMT`**
: Used to represent a `do` loop. The body of the loop is given by
`DO_BODY` while the termination condition for the loop is given by
`DO_COND`. The condition for a `do`-statement is always an
expression.

**`EMPTY_CLASS_EXPR`**
: Used to represent a temporary object of a class with no data whose
address is never taken. (All such objects are interchangeable.) The
`TREE_TYPE` represents the type of the object.

**`EXPR_STMT`**
: Used to represent an expression statement. Use `EXPR_STMT_EXPR` to
obtain the expression.

**`FOR_STMT`**
: Used to represent a `for` statement. The `FOR_INIT_STMT` is
the initialization statement for the loop. The `FOR_COND` is the
termination condition. The `FOR_EXPR` is the expression executed
right before the `FOR_COND` on each loop iteration; often, this
expression increments a counter. The body of the loop is given by
`FOR_BODY`. Note that `FOR_INIT_STMT` and `FOR_BODY`
return statements, while `FOR_COND` and `FOR_EXPR` return
expressions.

**`GOTO_EXPR`**
: Used to represent a `goto` statement. The `GOTO_DESTINATION` will
usually be a `LABEL_DECL`. However, if the “computed goto” extension
has been used, the `GOTO_DESTINATION` will be an arbitrary expression
indicating the destination. This expression will always have pointer type.

**`HANDLER`**
: Used to represent a C++ `catch` block. The `HANDLER_TYPE`
is the type of exception that will be caught by this handler; it is
equal (by pointer equality) to `NULL` if this handler is for all
types. `HANDLER_PARMS` is the `DECL_STMT` for the catch
parameter, and `HANDLER_BODY` is the code for the block itself.

**`IF_STMT`**
: Used to represent an `if` statement. The `IF_COND` is the
expression.

If the condition is a `TREE_LIST`, then the `TREE_PURPOSE` is
a statement (usually a `DECL_STMT`). Each time the condition is
evaluated, the statement should be executed. Then, the
`TREE_VALUE` should be used as the conditional expression itself.
This representation is used to handle C++ code like this:

```
          if (int i = 7) ...

```

where there is a new local variable (or variables) declared within the
condition.

The `THEN_CLAUSE` represents the statement given by the `then`
condition, while the `ELSE_CLAUSE` represents the statement given
by the `else` condition.

**`LABEL_EXPR`**
: Used to represent a label. The `LABEL_DECL` declared by this
statement can be obtained with the `LABEL_EXPR_LABEL` macro. The
`IDENTIFIER_NODE` giving the name of the label can be obtained from
the `LABEL_DECL` with `DECL_NAME`.

**`RETURN_STMT`**
: Used to represent a `return` statement. The `RETURN_EXPR` is
the expression returned; it will be `NULL_TREE` if the statement
was just

```
          return;

```

**`SUBOBJECT`**
: In a constructor, these nodes are used to mark the point at which a
subobject of `this` is fully constructed. If, after this point, an
exception is thrown before a `CTOR_STMT` with `CTOR_END_P` set
is encountered, the `SUBOBJECT_CLEANUP` must be executed. The
cleanups must be executed in the reverse order in which they appear.

**`SWITCH_STMT`**
: Used to represent a `switch` statement. The `SWITCH_STMT_COND`
is the expression on which the switch is occurring. See the documentation
for an `IF_STMT` for more information on the representation used
for the condition. The `SWITCH_STMT_BODY` is the body of the switch
statement. The `SWITCH_STMT_TYPE` is the original type of switch
expression as given in the source, before any compiler conversions.

**`TRY_BLOCK`**
: Used to represent a `try` block. The body of the try block is
given by `TRY_STMTS`. Each of the catch blocks is a `HANDLER`
node. The first handler is given by `TRY_HANDLERS`. Subsequent
handlers are obtained by following the `TREE_CHAIN` link from one
handler to the next. The body of the handler is given by
`HANDLER_BODY`.

If `CLEANUP_P` holds of the `TRY_BLOCK`, then the
`TRY_HANDLERS` will not be a `HANDLER` node. Instead, it will
be an expression that should be executed if an exception is thrown in
the try block. It must rethrow the exception after executing that code.
And, if an exception is thrown while the expression is executing,
`terminate` must be called.

**`USING_STMT`**
: Used to represent a `using` directive. The namespace is given by
`USING_STMT_NAMESPACE`, which will be a NAMESPACE_DECL. This node
is needed inside template functions, to implement using directives
during instantiation.

**`WHILE_STMT`**
: Used to represent a `while` loop. The `WHILE_COND` is the
termination condition for the loop. See the documentation for an
`IF_STMT` for more information on the representation used for the
condition.

The `WHILE_BODY` is the body of the loop.
