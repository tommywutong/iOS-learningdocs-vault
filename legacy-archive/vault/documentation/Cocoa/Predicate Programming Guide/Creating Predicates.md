---
title: 谓词编程指南
apple_id: TP40001789
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pCreating.html
archived_at: '2026-07-15T07:17:41.539291Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [谓词编程指南](Introduction.md)


[下一页](Using%20Predicates.md)[上一页](Introduction.md)

# 创建谓词

在 Cocoa 中创建谓词有三种方式：使用格式串、直接在代码中创建，以及通过谓词模板创建。

你可以使用 `NSPredicate` 类中形如 `predicateWithFormat…` 的类方法，直接从字符串创建谓词。你把谓词定义成一个字符串，其中可以选择性地使用变量替换。运行时会先执行变量替换（如果有的话），然后解析得到的字符串，创建出相应的谓词对象和表达式对象。下面的例子创建了一个包含两个比较谓词的复合谓词。

```objc
NSPredicate *predicate = [NSPredicate
    predicateWithFormat:@"(lastName like[cd] %@) AND (birthday > %@)",
            lastNameSearchString, birthdaySearchDate];
```

（在这个例子中，`like[cd]` 是加了修饰符的 “like” 运算符，表示不区分大小写且不区分变音符号。）关于字符串语法的完整说明以及全部可用运算符的列表，请参阅[谓词格式串语法](Predicate%20Format%20String%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojvfvbuuqseijeegqq)。

谓词字符串解析器对空白字符不敏感，对关键字不区分大小写，并且支持嵌套的括号表达式。它还支持 `printf` 风格的格式说明符（例如 `%x` 和 `%@`）——参阅 [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943)。变量用 `$` 表示（例如 `$VARIABLE_NAME`）——详见[使用谓词模板创建谓词](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojtfuzdcojwgm4q)。

解析器不做任何语义类型检查。它会尽最大努力猜测并创建合适的表达式，但仍有可能产生运行时错误——尤其是在使用替换变量（substitution variable）的情况下。

这种方式通常最适合用于预先定义好的查询条件，不过变量替换也带来了相当大的灵活性。这项技术的缺点在于，你必须小心不要在字符串里引入错误——因为直到运行时你才会发现这些错误。

字符串常量在表达式中必须加引号——单引号和双引号都可以，但必须正确配对（也就是说，双引号（`"`）不能与单引号（`'`）配对）。如果你用 `%@` 做变量替换（例如 `firstName like %@`），引号会自动为你加上。如果你在格式串中直接写字符串常量，就必须自己加引号，如下例所示。

```objc
NSPredicate *predicate = [NSPredicate
    predicateWithFormat:@"lastName like[c] \"S*\""];
```

使用通配符（wildcard）时，你必须把自动加引号这一点考虑进去——你必须在替换之前就把通配符加到变量里，如下例所示。

```objc
NSString *prefix = @"prefix";
NSString *suffix = @"suffix";
NSPredicate *predicate = [NSPredicate
    predicateWithFormat:@"SELF like[c] %@",
    [[prefix stringByAppendingString:@"*"] stringByAppendingString:suffix]];
BOOL ok = [predicate evaluateWithObject:@"prefixxxxxxsuffix"];
```

在这个例子中，变量替换产生的谓词字符串是 `SELF LIKE[c] "prefix*suffix"`，`ok` 的值为 `YES`。相比之下，下面这段代码得到的谓词字符串是 `SELF LIKE[c] "prefix" * "suffix"`，对该谓词求值会产生运行时错误：

```objc
predicate = [NSPredicate
    predicateWithFormat:@"SELF like[c] %@*%@", prefix, suffix];
ok = [predicate evaluateWithObject:@"prefixxxxxxsuffix"];
```

最后，下面这段代码会导致运行时解析错误（`Unable to parse the format string "SELF like[c] %@*"`）。

```objc
predicate = [NSPredicate
    predicateWithFormat:@"SELF like[c] %@*", prefix];
```

你还应当注意格式串中的变量替换与变量表达式之间的区别。下面这段代码创建的谓词，其右端是一个变量表达式。

```objc
predicate = [NSPredicate
    predicateWithFormat:@"lastName like[c] $LAST_NAME"];
```

关于变量表达式的更多内容，请参阅[使用谓词模板创建谓词](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojtfuzdcojwgm4q)。

如下面的例子所示，你可以这样指定布尔值并测试其相等性：

```objc
NSPredicate *newPredicate =
    [NSPredicate predicateWithFormat:@"anAttribute == %@", [NSNumber numberWithBool:aBool]];
NSPredicate *testForTrue =
    [NSPredicate predicateWithFormat:@"anAttribute == YES"];
```


由于字符串变量在用 `%@` 替换进格式串时会被加上引号，你_不能_用 `%@` 来指定动态的属性名——如下例所示。

```objc
NSString *attributeName = @"firstName";
NSString *attributeValue = @"Adam";
NSPredicate *predicate = [NSPredicate predicateWithFormat:@"%@ like %@",
        attributeName, attributeValue];
```

这种情况下，谓词格式串的求值结果是 `"firstName" like "Adam"`。

如果你想指定动态的属性名，就要在格式串中使用 `%K`，如下面这段代码所示。

```objc
predicate = [NSPredicate predicateWithFormat:@"%K like %@",
        attributeName, attributeValue];
```

这种情况下，谓词格式串的求值结果是 `firstName like "Adam"`（注意 `firstName` 周围没有引号）。

你可以直接在代码中创建谓词实例和表达式实例。`NSComparisonPredicate` 和 `NSCompoundPredicate` 分别提供了便捷方法，让你能轻松地创建比较谓词和复合谓词。`NSComparisonPredicate` 提供了一系列运算符，从简单的相等性测试到自定义函数都有。

下面的例子演示如何创建一个谓词来表示 `(revenue >= 1000000) and (revenue < 100000000)`。注意两个比较谓词使用的是同一个左端表达式。

```objc
NSExpression *lhs = [NSExpression expressionForKeyPath:@"revenue"];

NSExpression *greaterThanRhs = [NSExpression expressionForConstantValue:[NSNumber numberWithInt:1000000]];
NSPredicate *greaterThanPredicate = [NSComparisonPredicate
    predicateWithLeftExpression:lhs
    rightExpression:greaterThanRhs
    modifier:NSDirectPredicateModifier
    type:NSGreaterThanOrEqualToPredicateOperatorType
    options:0];

NSExpression *lessThanRhs = [NSExpression expressionForConstantValue:[NSNumber numberWithInt:100000000]];
NSPredicate *lessThanPredicate = [NSComparisonPredicate
    predicateWithLeftExpression:lhs
    rightExpression:lessThanRhs
    modifier:NSDirectPredicateModifier
    type:NSLessThanPredicateOperatorType
    options:0];

NSCompoundPredicate *predicate = [NSCompoundPredicate andPredicateWithSubpredicates:
    @[greaterThanPredicate, lessThanPredicate]];
```

这项技术的缺点应该一目了然——你可能得写很多代码。它的优点是不容易出现拼写错误和其他排版错误（这类错误往往要到运行时才会被发现），而且它可能比依赖字符串解析更快。

当谓词的创建过程本身就是动态的时候（例如在一个谓词构建器中），这项技术最为有用。

谓词模板在易用但容易出错的格式串方案与代码量大的纯编码方案之间提供了一个不错的折中。谓词模板其实就是一个包含变量表达式的谓词。（如果你在使用 Core Data 框架，可以用 Xcode 的设计工具把用于获取请求（fetch request）的谓词模板加入你的模型——参阅 Managed Object Models。）下面的例子用格式串创建了一个谓词，其右端是一个变量表达式。

```objc
NSPredicate *predicateTemplate = [NSPredicate
    predicateWithFormat:@"lastName like[c] $LAST_NAME"];
```

这等价于像下例那样直接创建变量表达式。

```objc
NSExpression *lhs = [NSExpression expressionForKeyPath:@"lastName"];

NSExpression *rhs = [NSExpression expressionForVariable:@"LAST_NAME"];

NSPredicate *predicateTemplate = [NSComparisonPredicate
    predicateWithLeftExpression:lhs
    rightExpression:rhs
    modifier:NSDirectPredicateModifier
    type:NSLikePredicateOperatorType
    options:NSCaseInsensitivePredicateOption];
```

要创建一个可用于对对象求值的有效谓词，你需要使用 `NSPredicate` 的 `predicateWithSubstitutionVariables:` 方法，传入一个包含待替换变量的字典。（注意，该字典必须为谓词中指定的所有变量都提供键值对。）

```objc
NSPredicate *predicate = [predicateTemplate predicateWithSubstitutionVariables:
    [NSDictionary dictionaryWithObject:@"Turner" forKey:@"LAST_NAME"]];
```

这个例子返回的新谓词是 `lastName LIKE[c] "Turner"`。

由于替换用的字典必须为谓词中指定的所有变量都提供键值对，如果你想匹配空值，就必须在字典里提供一个空值，如下例所示。

```objc
NSPredicate *predicate = [NSPredicate
    predicateWithFormat:@"date = $DATE"];
predicate = [predicate predicateWithSubstitutionVariables:
    [NSDictionary dictionaryWithObject:[NSNull null] forKey:@"DATE"]];
```

这个例子构造出的谓词是 `date == <null>`。

区分格式串中不同类型的值非常重要。另外还要注意，给变量（或替换变量字符串）加上单引号或双引号，会导致 `%@`、`%K` 或 `$variable` 在格式串中被当作字面量看待，从而阻止任何替换发生。

__`@"attributeName == %@"`__：这个谓词检查键 `attributeName` 的值是否与运行时作为参数传给 `predicateWithFormat:` 的对象 `%@` 的值相同。注意 `%@` 可以是任何 description 在谓词中有效的对象的占位符，例如 `NSDate`、`NSNumber`、`NSDecimalNumber` 或 `NSString` 的实例。

__`@"%K == %@"`__：这个谓词检查键 `%K` 的值是否与对象 `%@` 的值相同。这两个变量都在运行时作为参数传给 `predicateWithFormat:`。

__`@"name IN $NAME_LIST"`__：这是一个谓词模板，用于检查键 `name` 的值是否在变量 `$NAME_LIST`（不带引号）中，该变量在运行时通过 `predicateWithSubstitutionVariables:` 提供。

__`@"'name' IN $NAME_LIST"`__：这是一个谓词模板，用于检查常量值 `'name'`（注意字符串两侧的引号）是否在变量 `$NAME_LIST` 中，该变量在运行时通过 `predicateWithSubstitutionVariables:` 提供。

__`@"$name IN $NAME_LIST"`__：这是一个谓词模板，它期望 `$NAME` 和 `$NAME_LIST` 两者的值都通过 `predicateWithSubstitutionVariables:` 替换进来。

__`@"%K == '%@'"`__：这个谓词检查键 `%K` 的值是否等于字符串字面量 “`%@`“（注意 `%@` 两侧的单引号）。键名 `%K` 在运行时作为参数传给 `predicateWithFormat:`。

[下一页](Using%20Predicates.md)[上一页](Introduction.md)

