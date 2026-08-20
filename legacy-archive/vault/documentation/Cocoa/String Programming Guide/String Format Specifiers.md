---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/formatSpecifiers.html
archived_at: '2026-07-15T07:19:33.202284Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Reading%20Strings%20From%20and%20Writing%20Strings%20To%20Files%20and%20URLs.md)[上一页](Formatting%20String%20Objects.md)

# 字符串格式说明符

本文汇总了字符串格式化方法和函数所支持的格式说明符（format specifier）。

`NSString` 格式化方法和 CFString 格式化函数所支持的格式说明符遵循 [IEEE printf 规范](http://www.opengroup.org/onlinepubs/009695399/functions/printf.html)；[表 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denrvfvjvona) 汇总了这些说明符。注意，你还可以使用“`n$`”形式的位置说明符，例如 `%1$@ %2$s`。更多细节请参阅 [IEEE printf 规范](http://www.opengroup.org/onlinepubs/009695399/functions/printf.html)。这些格式说明符同样可以用于 `NSLog` 函数。

__表 1__  `NSString` 格式化方法和 CFString 格式化函数所支持的格式说明符

| 说明符 | 说明 |
| --- | --- |
| `%@` | Objective-C 对象；如果该对象实现了 `descriptionWithLocale:`，则打印该方法返回的字符串，否则打印 `description` 返回的字符串。也适用于 `CFTypeRef` 对象，此时返回 `CFCopyDescription` 函数的结果。 |
| `%%` | `'%'` 字符。 |
| `%d`、`%D` | 有符号 32 位整数（`int`）。 |
| `%u`、`%U` | 无符号 32 位整数（`unsigned int`）。 |
| `%x` | 无符号 32 位整数（`unsigned int`），以十六进制打印，使用数字 0–9 和小写字母 a–f。 |
| `%X` | 无符号 32 位整数（`unsigned int`），以十六进制打印，使用数字 0–9 和大写字母 A–F。 |
| `%o`、`%O` | 无符号 32 位整数（`unsigned int`），以八进制打印。 |
| `%f` | 64 位浮点数（`double`）。 |
| `%e` | 64 位浮点数（`double`），以科学计数法打印，用小写字母 e 引出指数部分。 |
| `%E` | 64 位浮点数（`double`），以科学计数法打印，用大写字母 E 引出指数部分。 |
| `%g` | 64 位浮点数（`double`）；当指数小于 –4 或大于等于精度时按 `%e` 的样式打印，否则按 `%f` 的样式打印。 |
| `%G` | 64 位浮点数（`double`）；当指数小于 –4 或大于等于精度时按 `%E` 的样式打印，否则按 `%f` 的样式打印。 |
| `%c` | 8 位无符号字符（`unsigned char`）。 |
| `%C` | 16 位 UTF-16 码元（`unichar`）。 |
| `%s` | 以 null 结尾的 8 位无符号字符数组。由于 `%s` 说明符会让这些字符按系统默认编码来解释，其结果可能不确定，对于从右到左书写的语言尤其如此。例如在从右到左（RTL）的情况下，当字符本身方向性不强时，`%s` 会插入方向标记。因此最好避免使用 `%s`，而是显式指定编码。 |
| `%S` | 以 null 结尾的 16 位 UTF-16 码元数组。 |
| `%p` | void 指针（`void *`），以十六进制打印，使用数字 0–9 和小写字母 a–f，并带有前导 `0x`。 |
| `%a` | 64 位浮点数（`double`），以科学计数法打印，带前导 `0x`，小数点前有一位十六进制数字，用小写的 `p` 引出指数部分。 |
| `%A` | 64 位浮点数（`double`），以科学计数法打印，带前导 `0X`，小数点前有一位十六进制数字，用大写的 `P` 引出指数部分。 |
| `%F` | 64 位浮点数（`double`），以十进制记数法打印。 |

__表 2__  `NSString` 格式化方法和 CFString 格式化函数所支持的长度修饰符

| 长度修饰符 | 说明 |
| --- | --- |
| `h` | 长度修饰符，指定其后的 `d`、`o`、`u`、`x` 或 `X` 转换说明符作用于 `short` 或 `unsigned short` 参数。 |
| `hh` | 长度修饰符，指定其后的 `d`、`o`、`u`、`x` 或 `X` 转换说明符作用于 `signed char` 或 `unsigned char` 参数。 |
| `l` | 长度修饰符，指定其后的 `d`、`o`、`u`、`x` 或 `X` 转换说明符作用于 `long` 或 `unsigned long` 参数。 |
| `ll`、`q` | 长度修饰符，指定其后的 `d`、`o`、`u`、`x` 或 `X` 转换说明符作用于 `long long` 或 `unsigned long long` 参数。 |
| `L` | 长度修饰符，指定其后的 `a`、`A`、`e`、`E`、`f`、`F`、`g` 或 `G` 转换说明符作用于 `long double` 参数。 |
| `z` | 长度修饰符，指定其后的 `d`、`o`、`u`、`x` 或 `X` 转换说明符作用于 `size_t`。 |
| `t` | 长度修饰符，指定其后的 `d`、`o`、`u`、`x` 或 `X` 转换说明符作用于 `ptrdiff_t`。 |
| `j` | 长度修饰符，指定其后的 `d`、`o`、`u`、`x` 或 `X` 转换说明符作用于 `intmax_t` 或 `uintmax_t` 参数。 |

OS X 使用了若干数据类型——`NSInteger`、`NSUInteger`、`CGFloat` 和 `CFIndex`——以便在 32 位和 64 位环境中用一致的方式表示数值。在 32 位环境中，`NSInteger` 和 `NSUInteger` 分别定义为 `int` 和 `unsigned int`。在 64 位环境中，`NSInteger` 和 `NSUInteger` 分别定义为 `long` 和 `unsigned long`。为了免于根据平台使用不同的 printf 风格类型说明符，你可以使用表 3 中列出的说明符。注意，某些情况下你可能需要对数值做强制类型转换。

__表 3__  各数据类型对应的格式说明符

| 类型 | 格式说明符 | 注意事项 |
| --- | --- | --- |
| `NSInteger` | `%ld` 或 `%lx` | 把值强制转换为 `long`。 |
| `NSUInteger` | `%lu` 或 `%lx` | 把值强制转换为 `unsigned long`。 |
| `CGFloat` | `%f` 或 `%g` | 格式化时 `%f` 对 float 和 double 都适用；但扫描时请注意下面介绍的技巧。 |
| `CFIndex` | `%ld` 或 `%lx` | 与 `NSInteger` 相同。 |
| 指针 | `%p` 或 `%zx` | `%p` 会在输出开头加上 `0x`。如果你不想要它，就使用 `%zx` 并且不做类型转换。 |

下面的例子演示了如何用 `%ld` 格式化 `NSInteger`，以及如何使用强制类型转换。

```objc
NSInteger i = 42;
printf("%ld\n", (long)i);
```

除了表 3 中提到的注意事项之外，扫描时还有一种额外情况：你必须区分 `float` 和 `double` 这两种类型。对 float 应使用 `%f`，对 double 应使用 `%lf`。如果你需要对 `CGFloat` 使用 `scanf`（或它的某个变体），请改用 `double`，再把这个 `double` 复制给 `CGFloat`。

```objc
CGFloat imageWidth;
double tmp;
sscanf (str, "%lf", &tmp);
imageWidth = tmp;
```

要记住很重要的一点：无论在 32 位还是 64 位平台上，`%lf` 都不能正确表示 `CGFloat`。这一点与 `%ld` 不同，`%ld` 在所有情况下都适用于 `long`。

[下一页](Reading%20Strings%20From%20and%20Writing%20Strings%20To%20Files%20and%20URLs.md)[上一页](Formatting%20String%20Objects.md)

