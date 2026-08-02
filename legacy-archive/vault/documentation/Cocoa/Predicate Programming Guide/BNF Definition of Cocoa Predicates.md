---
title: 谓词编程指南
apple_id: TP40001789
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pBNF.html
archived_at: '2026-07-15T07:17:41.527886Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [谓词编程指南](Introduction.md)


[下一页](Document%20Revision%20History.md)[上一页](Predicate%20Format%20String%20Syntax.md)

# Cocoa 谓词的 BNF 定义

本文用巴科斯-诺尔范式（Backus-Naur Form）记法定义 Cocoa 谓词。


```
NSPredicate ::= NSComparisonPredicate | NSCompoundPredicate
    | "(" NSPredicate ")" | TRUEPREDICATE | FALSEPREDICATE 
```



```
NSCompoundPredicate ::= NSPredicate "AND" NSPredicate
    | NSPredicate "OR" NSPredicate
    | "NOT" NSPredicate
```



```
NSComparisonPredicate ::= expression operation expression
    | aggregate_qualifier NSComparisonPredicate
```


`CONTAINS` 和 `IN` 既可以作为聚合运算符，也可以作为字符串运算符，具体取决于其参数的类型。

```
operation ::= "=" | "!=" | "<" | ">" | "<=" | ">="
    | BETWEEN
    | aggregate_operations [ "[" string_options "]" ]

aggregate_operations ::= CONTAINS | IN | string_operations

string_operations ::= BEGINSWITH | ENDSWITH | LIKE | MATCHES

string_options ::= c | d | cd
```



```
aggregate_qualifier ::= ANY | ALL | NONE | SOME
```



```
expression ::= "(" expression ")"
    | binary_expression
    | function_expression
    | assignment_expression
    | index_expression
    | keypath_expression
    | value_expression
```



```
value_expression ::= literal_value | literal_aggregate
```



```
literal_value ::= string_value
    | numeric_value
    | predicate_argument
    | predicate_variable
    | NULL
    | TRUE
    | FALSE
    | SELF
```



```
string_value ::= "text" | 'text'
```



```
predicate_argument ::= "%" format_argument
```



```
format_argument ::= "@" | "%" | "K"
    printf style conversion character
```



```
predicate_variable ::= "$" identifier
```



```
keypath_expression ::= identifier | "@" identifier
    | expression "." expression
```



```
literal_aggregate ::= "{" [ expression [ "," expression ... ] ] "}"
```



```
index_expression ::= array_expression "[" integer_expression "]"
    | dictionary_expression   "[" expression "]"
    | aggregate_expression "[" FIRST "]" 
    | aggregate_expression "[" LAST "]" 
    | aggregate_expression "[" SIZE "]" 
```



```
aggregate_expression ::= array_expression | dictionary_expression
```



```
assignment_expression ::= predicate_variable ":=" expression
```



```
binary_expression ::= expression binary_operator expression
    | "-" expression
```



```
binary_operator ::= "+" | "-" | "*" | "/" | "**"
```



```
function_expression ::= function_name "(" [ expression [ "," expression ... ] ] ")"
```



```
function_name ::= "sum" | "count" | "min" | "max"
    | "average" | "median" | "mode" | "stddev"
    | "sqrt" | "log" | "ln" | "exp"
    | "floor" | "ceiling" | "abs" | "trunc"
    | "random" | "randomn" | "now"
```



```
array_expression ::= any expression that evaluates to an NSArray object
```



```
dictionary_expression ::= any expression that evaluates to an NSDictionary object
```



```
integer_expression ::= any expression that evaluates to an integral value
```



```
numeric_value ::= C style numeric constant
```



```
identifier ::= C style identifier | "#" reserved_word
```

[下一页](Document%20Revision%20History.md)[上一页](Predicate%20Format%20String%20Syntax.md)

