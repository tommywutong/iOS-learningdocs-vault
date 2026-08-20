---
title: 谓词编程指南
apple_id: TP40001789
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSpotlightComparison.html
archived_at: '2026-07-15T07:17:41.549686Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [谓词编程指南](Introduction.md)


[下一页](Predicate%20Format%20String%20Syntax.md)[上一页](Using%20Predicates.md)

# NSPredicate 与 Spotlight 查询字符串的比较

Spotlight 和 `NSPredicate` 类都实现了一套查询字符串语法，两者虽然相似，却在若干方面有所不同。只要只用到二者共有的那部分功能，一种查询字符串就可以转换成另一种形式。

`NSMetadataQuery` 类是 Spotlight 的 Cocoa 接口，它在 API 中使用了 `NSPredicate`。除此之外，Spotlight 与 `NSPredicate` 之间并无关联。Spotlight 的查询字符串语法与 `NSPredicate` 的查询字符串语法相似，但并不相同。只要你使用的语法是两套 API 都能理解的，就可以把一种查询字符串转换成另一种形式。Spotlight 的查询语法是 `NSPredicate` 查询语法的一个子集。关于 Spotlight 查询表达式语法的完整说明，参阅 [File Metadata Query Expression Syntax](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html#//apple_ref/doc/uid/TP40001849)；关于 `NSPredicate` 字符串语法的完整说明，参阅[谓词格式串语法](Predicate%20Format%20String%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojvfvjvomi)。

Spotlight 要求比较子句采用 `"KEY operator VALUE"` 的形式，不接受 `"VALUE operator KEY"`。而且，Spotlight 能接受作为 `VALUE` 的属性种类比 `NSPredicate` 所接受的更为有限。作为这一限制带来的部分结果，在 Spotlight 查询中你不必总是给字符串字面量加引号。当 `VALUE` 是字符串且不需要对它施加特殊运算符时，你可以省略引号。在 `NSPredicate` 查询字符串中你不能这么做，因为那样结果会有歧义。

在 Spotlight 中，表示查询不区分大小写和不区分变音符号的语法与 `NSPredicate` 的写法不同。在 Spotlight 中，你把标记附加在比较字符串的末尾（例如 `"myAttribute == 'foo'cd"`）。在 `NSPredicate` 字符串中，你使用 `like` 运算符，并把标记加在 "[]" 里作为前缀（例如 `"myAttribute like[cd] 'foo'"`）。两种情况下，`'cd'` 都表示不区分大小写且不区分变音符号。Spotlight 把修饰符放在值上，而 `NSPredicate` 把修饰符放在运算符上。

你不能把 `MDQuery` 的运算符用作 `NSPredicate` 对象 `"KEY operator VALUE"` 字符串中的 `VALUE`。例如，在 Spotlight 中你这样写一个“是……的子串”表达式：`"myAttribute = '*foo*'"`；而在 `NSPredicate` 字符串中你要用 `contains` 运算符，写成：`"myAttribute contains 'foo'"`。Spotlight 接受类似 glob 的表达式，`NSPredicate` 则使用另外的运算符。

如果你在比较表达式中用“`*`”作为左端的键，在 Spotlight 中它表示“该项中的任意键”，并且只能与 `==` 一起使用。在 `NSPredicate` 对象中，你只有配合 `NSMetadataQuery` 对象时才能使用这种表达式。

你可以从 Finder 中的一次搜索生成谓词格式串。执行一次搜索并保存它，然后选中你保存到的那个文件夹并选择“显示简介”——简介面板会显示出 Spotlight 所使用的查询。不过要注意，`NSPredicate` 格式串与 Finder 中存储的那个字符串之间存在细微差别。Finder 中的字符串可能形如下面这个例子。

```
(((* = "FooBar*"wcd) || (kMDItemTextContent = "FooBar*"cd))
    && (kMDItemContentType != com.apple.mail.emlx)
    && (kMDItemContentType != public.vcard))
```

通常，要把 Spotlight 查询转换成谓词格式串，你只需确保谓词不以 `*` 开头（`NSMetadataQuery` 在解析谓词时不支持这种写法）。此外，当你想使用通配符时，应该改用 `LIKE`，如下例所示。

```
((kMDItemTextContent LIKE[cd] "FooBar")
    && (kMDItemContentType != "com.apple.mail.emlx")
    && (kMDItemContentType != "public.vcard"))
```

[下一页](Predicate%20Format%20String%20Syntax.md)[上一页](Using%20Predicates.md)

