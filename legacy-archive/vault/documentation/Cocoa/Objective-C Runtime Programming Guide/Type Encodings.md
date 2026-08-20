---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html
archived_at: '2026-07-15T07:17:29.397666Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 运行时编程指南](Introduction.md)


[下一页](Declared%20Properties.md)[上一页](Message%20Forwarding.md)

# 类型编码

为了协助运行时（runtime）系统，编译器会把每个方法的返回值类型和参数类型编码成一个字符串，并把该字符串与方法选择器关联起来。它所使用的这套编码方案在其他场合也很有用，因此通过 `@encode()` 编译器指令对外公开。给定一个类型说明，`@encode()` 会返回一个对该类型进行编码的字符串。这个类型可以是像 `int` 这样的基本类型、指针、带标签的结构体或联合体，也可以是类名——实际上，任何能作为 C 的 `sizeof()` 运算符参数的类型都可以。

```objc
char *buf1 = @encode(int **);
char *buf2 = @encode(struct key);
char *buf3 = @encode(Rectangle);
```

下表列出了各种类型编码。请注意，其中很多与你为归档或分发而对对象进行编码时所用的编码是重合的。不过，这里列出的编码中有一些是你在编写编码器（coder）时不能使用的，而另有一些你在编写编码器时可能想用的编码却不会由 `@encode()` 生成。（关于为归档或分发而编码对象的更多信息，参见 Foundation 框架参考中的 [NSCoder](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSCoder/Description.html#//apple_ref/occ/cl/NSCoder) 类说明。）

__表 6-1__  Objective-C 类型编码

| 编码 | 含义 |
| --- | --- |
| `c` | 一个 `char` |
| `i` | 一个 `int` |
| `s` | 一个 `short` |
| `l` | 一个 `long`  在 64 位程序中，`l` 仍被当作 32 位量处理。 |
| `q` | 一个 `long long` |
| `C` | 一个 `unsigned char` |
| `I` | 一个 `unsigned int` |
| `S` | 一个 `unsigned short` |
| `L` | 一个 `unsigned long` |
| `Q` | 一个 `unsigned long long` |
| `f` | 一个 `float` |
| `d` | 一个 `double` |
| `B` | 一个 C++ 的 `bool` 或 C99 的 `_Bool` |
| `v` | 一个 `void` |
| `*` | 一个字符串（`char *`） |
| `@` | 一个对象（无论是静态类型的还是声明为 `id` 的） |
| `#` | 一个类对象（`Class`） |
| `:` | 一个方法选择器（`SEL`） |
| [_array type_] | 一个数组 |
| {_name=type..._} | 一个结构体 |
| (_name_=_type..._) | 一个联合体 |
| `b`num | 一个 _num_ 位的位域 |
| `^`type | 一个指向 _type_ 的指针 |
| `?` | 一个未知类型（该编码的用途之一是表示函数指针） |

数组的类型编码用方括号括起来；数组中元素的个数紧跟在左方括号之后、数组类型之前。例如，一个含有 12 个 `float` 指针的数组会被编码成：

```
[12^f]
```

结构体用花括号指定，联合体用圆括号指定。先列出结构体标签，随后是一个等号，再依次列出结构体各字段的编码。例如，下面这个结构体

```c
typedef struct example {
    id   anObject;
    char *aString;
    int  anInt;
} Example;
```

会被编码成这样：

```
{example=@*i}
```

无论传给 `@encode()` 的是所定义的类型名（`Example`）还是结构体标签（`example`），得到的编码都相同。结构体指针的编码携带着关于该结构体字段的等量信息：

```
^{example=@*i}
```

不过，再多一层间接就会去掉内部的类型说明：

```
^^{example}
```

对象的处理方式与结构体相同。例如，把 `NSObject` 类名传给 `@encode()` 会得到这样的编码：

```
{NSObject=#}
```

`NSObject` 类只声明了一个实例变量 `isa`，其类型为 Class。

请注意，虽然 `@encode()` 指令不会返回它们，但当类型限定符被用于在协议中声明方法时，运行时系统会使用表 6-2 中列出的这些额外编码。

__表 6-2__  Objective-C 方法编码

| 编码 | 含义 |
| --- | --- |
| `r` | `const` |
| `n` | `in` |
| `N` | `inout` |
| `o` | `out` |
| `O` | `bycopy` |
| `R` | `byref` |
| `V` | `oneway` |

[下一页](Declared%20Properties.md)[上一页](Message%20Forwarding.md)

