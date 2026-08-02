---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Rough-GIMPLE-Grammar.html
archived_at: '2026-07-15T07:31:00.651173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [GIMPLE Example](GIMPLE-Example.md#apple-i5eu2ucmiuwuk6dbnvygyzi),
Up: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu)

---

#### 9.2.6 Rough GIMPLE Grammar


```swift
        function     : FUNCTION_DECL
                             DECL_SAVED_TREE -> compound-stmt

        compound-stmt: STATEMENT_LIST
                             members -> stmt

        stmt         : block
                     | if-stmt
                     | switch-stmt
                     | goto-stmt
                     | return-stmt
                     | resx-stmt
                     | label-stmt
                     | try-stmt
                     | modify-stmt
                     | call-stmt

        block        : BIND_EXPR
                             BIND_EXPR_VARS -> chain of DECLs
                             BIND_EXPR_BLOCK -> BLOCK
                             BIND_EXPR_BODY -> compound-stmt

        if-stmt      : COND_EXPR
                             op0 -> condition
                             op1 -> compound-stmt
                             op2 -> compound-stmt

        switch-stmt  : SWITCH_EXPR
                             op0 -> val
                             op1 -> NULL
                             op2 -> TREE_VEC of CASE_LABEL_EXPRs
                                 The CASE_LABEL_EXPRs are sorted by CASE_LOW,
                                 and default is last.

        goto-stmt    : GOTO_EXPR
                             op0 -> LABEL_DECL | val

        return-stmt  : RETURN_EXPR
                             op0 -> return-value

        return-value : NULL
                     | RESULT_DECL
                     | MODIFY_EXPR
                             op0 -> RESULT_DECL
                             op1 -> lhs

        resx-stmt    : RESX_EXPR

        label-stmt   : LABEL_EXPR
                             op0 -> LABEL_DECL

        try-stmt     : TRY_CATCH_EXPR
                             op0 -> compound-stmt
                             op1 -> handler
                     | TRY_FINALLY_EXPR
                             op0 -> compound-stmt
                             op1 -> compound-stmt

        handler      : catch-seq
                     | EH_FILTER_EXPR
                     | compound-stmt

        catch-seq    : STATEMENT_LIST
                             members -> CATCH_EXPR

        modify-stmt  : MODIFY_EXPR
                             op0 -> lhs
                             op1 -> rhs

        call-stmt    : CALL_EXPR
                             op0 -> val | OBJ_TYPE_REF
                             op1 -> call-arg-list

        call-arg-list: TREE_LIST
                             members -> lhs | CONST

        addr-expr-arg: ID
                     | compref

        addressable  : addr-expr-arg
                     | indirectref

        with-size-arg: addressable
                     | call-stmt

        indirectref  : INDIRECT_REF
                             op0 -> val

        lhs          : addressable
                     | bitfieldref
                     | WITH_SIZE_EXPR
                             op0 -> with-size-arg
                             op1 -> val

        min-lval     : ID
                     | indirectref

        bitfieldref  : BIT_FIELD_REF
                             op0 -> inner-compref
                             op1 -> CONST
                             op2 -> var

        compref      : inner-compref
                     | REALPART_EXPR
                             op0 -> inner-compref
                     | IMAGPART_EXPR
                             op0 -> inner-compref

        inner-compref: min-lval
                     | COMPONENT_REF
                             op0 -> inner-compref
                             op1 -> FIELD_DECL
                             op2 -> val
                     | ARRAY_REF
                             op0 -> inner-compref
                             op1 -> val
                             op2 -> val
                             op3 -> val
                     | ARRAY_RANGE_REF
                             op0 -> inner-compref
                             op1 -> val
                             op2 -> val
                             op3 -> val
                     | VIEW_CONVERT_EXPR
                             op0 -> inner-compref

        condition    : val
                     | RELOP
                             op0 -> val
                             op1 -> val

        val          : ID
                     | CONST

        rhs          : lhs
                     | CONST
                     | call-stmt
                     | ADDR_EXPR
                             op0 -> addr-expr-arg
                     | UNOP
                             op0 -> val
                     | BINOP
                             op0 -> val
                             op1 -> val
                     | RELOP
                             op0 -> val
                             op1 -> val
```
