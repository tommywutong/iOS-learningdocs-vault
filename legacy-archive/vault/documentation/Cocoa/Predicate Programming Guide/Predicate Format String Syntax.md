---
title: 谓词编程指南
apple_id: TP40001789
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html
archived_at: '2026-07-15T07:17:41.556065Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [谓词编程指南](Introduction.md)


[下一页](BNF%20Definition%20of%20Cocoa%20Predicates.md)[上一页](Comparison%20of%20NSPredicate%20and%20Spotlight%20Query%20Strings.md)

# 谓词格式串语法

本文介绍谓词字符串的语法，以及谓词解析器的若干特性。

解析器所接受的字符串与传给正则表达式引擎的字符串表达式并不相同。本文介绍的是解析器的文本语法，而不是正则表达式引擎的语法。

谓词字符串解析器对空白字符不敏感，对关键字不区分大小写，并且支持嵌套的括号表达式。解析器不做语义类型检查。

变量用美元符号（`$`）标记（例如 `$VARIABLE_NAME`）。问号（`?`）不是有效的解析器记号。

格式串支持 `printf` 风格的格式说明符，例如 `%x`（参阅 [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943)）。其中两个重要的格式说明符是 `%@` 和 `%K`。

- `%@` 是可变参数替换，代表一个对象值——通常是字符串、数字或日期。
- `%K` 是可变参数替换，代表一个键路径（key path）。

当字符串变量通过 `%@` 格式说明符替换进字符串时，它们会被加上引号。如果你想指定动态的属性名，就要在格式串中使用 `%K`，如下例所示。

```objc
NSString *attributeName  = @"firstName";
NSString *attributeValue = @"Adam";
NSPredicate *predicate   = [NSPredicate predicateWithFormat:@"%K like %@",
        attributeName, attributeValue];
```

这种情况下，谓词格式串的求值结果是 `firstName like "Adam"`。

给变量（或替换变量字符串）加上单引号或双引号，会导致 `%@`、`%K` 或 `$variable` 在格式串中被当作字面量看待，从而阻止任何替换发生。在下面的例子中，谓词格式串的求值结果是 `firstName like "%@"`（注意 `%@` 两侧的单引号）。

```objc
NSString *attributeName = @"firstName";
NSString *attributeValue = @"Adam";
NSPredicate *predicate = [NSPredicate predicateWithFormat:@"%K like '%@'",
        attributeName, attributeValue];
```


__`=`, `==`__：左端表达式等于右端表达式。

__`>=`, `=>`__：左端表达式大于或等于右端表达式。

__`<=`, `=<`__：左端表达式小于或等于右端表达式。

__`>`__：左端表达式大于右端表达式。

__`<`__：左端表达式小于右端表达式。

__`!=`, `<>`__：左端表达式不等于右端表达式。

__`BETWEEN`__：左端表达式介于右端指定的两个值之间，或等于其中任意一个值。

右端是一个含两个值的数组（必须用数组来指定顺序），给出上界和下界。例如 `1 BETWEEN { 0 , 33 }` 或 `$INPUT BETWEEN { $LOWER, $UPPER }`。

在 Objective-C 中，你可以像下例这样创建一个 BETWEEN 谓词：

```objc
NSPredicate *betweenPredicate =
    [NSPredicate predicateWithFormat: @"attributeName BETWEEN %@", @[@1, @10]];
```

它创建的谓词匹配 `( ( 1 <= attributeValue ) && ( attributeValue <= 10 ) )`，如下例所示：

```objc
NSPredicate *betweenPredicate =
    [NSPredicate predicateWithFormat: @"attributeName BETWEEN %@", @[@1, @10]];

NSDictionary *dictionary = @{ @"attributeName" : @5 };

BOOL between = [betweenPredicate evaluateWithObject:dictionary];
if (between) {
    NSLog(@"between");
}
```


__`TRUEPREDICATE`__：求值结果恒为 `TRUE` 的谓词。

__`FALSEPREDICATE`__：求值结果恒为 `FALSE` 的谓词。

__`AND`, `&&`__：逻辑与。

__`OR`, `||`__：逻辑或。

__`NOT`, `!`__：逻辑非。

字符串比较默认区分大小写、区分变音符号。你可以在方括号中使用关键字符 `c` 和 `d` 来修饰运算符，分别指定不区分大小写和不区分变音符号，例如 `firstName BEGINSWITH[cd] $FIRST_NAME`。

__`BEGINSWITH`__：左端表达式以右端表达式开头。

__`CONTAINS`__：左端表达式包含右端表达式。

__`ENDSWITH`__：左端表达式以右端表达式结尾。

__`LIKE`__：左端表达式等于右端表达式：允许使用 `?` 和 `*` 作为通配符，其中 `?` 匹配 `1` 个字符，`*` 匹配 `0` 个或多个字符。

__`MATCHES`__：左端表达式按照 ICU v3 的 `regex` 风格比较等于右端表达式（更多细节参阅 ICU 用户指南中的[正则表达式](http://icu.sourceforge.net/userguide/regexp.html)一节）。

__`UTI-CONFORMS-TO`__：该运算符的左端参数是一个表达式，其求值结果是你想匹配的统一类型标识符（UTI）。右端参数也是一个求值结果为 UTI 的表达式。如果左端表达式返回的 UTI 符合右端表达式返回的 UTI，则比较结果为 `TRUE`。关于哪些类型符合某个给定类型，参阅 _[Uniform Type Identifiers Reference](../../Miscellaneous/Uniform%20Type%20Identifiers%20Reference/Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjx)_ 中的 [System-Declared Uniform Type Identifiers](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Articles/System-DeclaredUniformTypeIdentifiers.html#//apple_ref/doc/uid/TP40009259)。要了解如何声明对自定义 UTI 的符合性，参阅 _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_ 中的 [Declaring New Uniform Type Identifiers](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_declare/understand_utis_declare.html#//apple_ref/doc/uid/TP40001319-CH204)。

子句 `A UTI-CONFORMS-TO B` 与像下面这样调用 [UTTypeConformsTo](https://developer.apple.com/documentation/coreservices/1444079-uttypeconformsto) 方法的结果相同：

```c
UTTypeConformsTo (A, B)
```

在对 app 扩展项（类型为 [NSExtensionItem](https://developer.apple.com/documentation/foundation/nsextensionitem)）中的附件求值时，你可以使用类似下面这样的语句：

```
SUBQUERY (
    extensionItems,
    $extensionItem,
    SUBQUERY (
        $extensionItem.attachments,
        $attachment,
        ANY $attachment.registeredTypeIdentifiers UTI-CONFORMS-TO "com.adobe.pdf" ```  ``` 
    ).@count == $extensionItem.attachments.@count
).@count == 1
```

__`UTI-EQUALS`__：该运算符的左端参数是一个表达式，其求值结果是你想匹配的统一类型标识符（UTI）。右端参数也是一个求值结果为 UTI 的表达式。如果左端表达式返回的 UTI 等于右端表达式返回的 UTI，则比较结果为 `TRUE`。

子句 `A UTI-EQUALS B` 与像下面这样调用 [UTTypeEqual](https://developer.apple.com/documentation/coreservices/1447783-uttypeequal) 方法的结果相同：

```c
UTTypeEqual (A, B)
```

参阅 `UTI-CONFORMS-TO` 条目中的代码示例，把其中的运算符替换掉即可同样适用于 `UTI-EQUALS` 运算符。

__`ANY`, `SOME`__：指定后续表达式中的任意一个元素。例如 `ANY children.age < 18`。

__`ALL`__：指定后续表达式中的全部元素。例如 `ALL children.age < 18`。

__`NONE`__：指定后续表达式中没有任何元素满足条件。例如 `NONE children.age < 18`。它在逻辑上等价于 `NOT (ANY ...)`。

__`IN`__：等价于 SQL 的 IN 运算，左端必须出现在右端指定的集合中。

例如 `name IN { 'Ben', 'Melissa', 'Nick' }`。该集合可以是数组、集合或字典——若是字典，则使用它的各个值。

在 Objective-C 中，你可以像下例这样创建一个 IN 谓词：

```objc
NSPredicate *inPredicate =
            [NSPredicate predicateWithFormat: @"attribute IN %@", aCollection];
```

其中 `aCollection` 可以是 `NSArray`、`NSSet`、`NSDictionary` 的实例，也可以是相应可变类的实例。

__`array[index]`__：指定数组 `array` 中位于给定索引处的元素。

__`array[FIRST]`__：指定数组 `array` 中的第一个元素。

__`array[LAST]`__：指定数组 `array` 中的最后一个元素。

__`array[SIZE]`__：指定数组 `array` 的大小。

__C 风格标识符__：任何不是保留字的 C 风格标识符。

__#symbol__ ：用于把保留字转义成用户标识符。

__[\]{octaldigit}{3}__：用于转义一个八进制数（`\` 后跟 3 位八进制数字）。

__[\][xX]{hexdigit}{2}__：用于转义一个十六进制数（`\x` 或 `\X` 后跟 2 位十六进制数字）。

__[\][uU]{hexdigit}{4}__：用于转义一个 Unicode 数值（`\u` 或 `\U` 后跟 4 位十六进制数字）。

单引号和双引号产生相同的效果，但它们彼此之间不能配对结束。例如，`"abc"` 和 `'abc'` 是相同的，而 `"a'b'c"` 则等价于 `a`、`'b'`、`c` 三者以空格分隔的串接。

__`FALSE`, `NO`__：逻辑假。

__`TRUE`, `YES`__：逻辑真。

__`NULL`, `NIL`__：空值。

__`SELF`__：代表正在被求值的对象。

__`"text"`__：字符串。

__`'text'`__：字符串。

__以逗号分隔的字面量数组__：例如 `{ 'comma', 'separated', 'literal', 'array' }`。

__标准整数与定点数记法__：例如 `1`、`27`、`2.71828`、`19.75`。

__带指数的浮点数记法__：例如 `9.2e-5`。

__`0x`__：用于表示十六进制数字序列的前缀。

__`0o`__：用于表示八进制数字序列的前缀。

__`0b`__：用于表示二进制数字序列的前缀。

以下词汇是保留字：

`AND`, `OR`, `IN`, `NOT`, `ALL`, `ANY`, `SOME`, `NONE`, `LIKE`, `CASEINSENSITIVE`, `CI`, `MATCHES`, `CONTAINS`, `BEGINSWITH`, `ENDSWITH`, `BETWEEN`, `NULL`, `NIL`, `SELF`, `TRUE`, `YES`, `FALSE`, `NO`, `FIRST`, `LAST`, `SIZE`, `ANYKEY`, `SUBQUERY`, `FETCH`, `CAST`, `TRUEPREDICATE`, `FALSEPREDICATE`, `UTI-CONFORMS-TO`, `UTI-EQUALS`,

[下一页](BNF%20Definition%20of%20Cocoa%20Predicates.md)[上一页](Comparison%20of%20NSPredicate%20and%20Spotlight%20Query%20Strings.md)

