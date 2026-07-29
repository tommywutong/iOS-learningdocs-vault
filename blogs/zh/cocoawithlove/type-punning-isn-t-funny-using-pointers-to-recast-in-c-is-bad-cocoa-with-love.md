---
title: '类型双关并不有趣：在 C 中通过指针进行类型重转是有害的。| Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/04/using-pointers-to-recast-in-c-is-bad.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c1e4fb1b20dfa4bc'
translated: true
---

> 原文：[Type punning isn't funny: Using pointers to recast in C is bad. | Cocoa with Love](https://www.cocoawithlove.com/2008/04/using-pointers-to-recast-in-c-is-bad.html)　·　Cocoa with Love (Matt Gallagher)

一种常见的 C 语言重新解释数据类型的技术有可能导致恼人的 bug。Apple 知道这一点，这就是为什么 `NSRectToCGRect` 的实现（正确地）没有做文档声称的事情。我将展示一种在你自己的代码中安全执行重解释转换的技术。

Apple 的 [函数 `NSRectToCGRect` 的文档](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/index.html) 声称其实现如下：

```objc
CGRect NSRectToCGRect(NSRect nsrect) {
   return (*(CGRect *)&(nsrect));
}
```

如果你见过很多 C 代码，你可能以前见过这种方法。你不能通过直接转换一个结构体到另一个结构体来重解释——即使它们有相同的字段——所以常见的做法是通过创建一个指针并转换该指针来重解释。

其含义是 `NSRectToCGRect` 在不改变包含的数据的情况下，将一个 `NSRect` 重解释为 `CGRect`。

虽然隐含的功能是准确的，但显示的实现却不是。实际上，该函数看起来是这样的：

```objc
NS_INLINE CGRect NSRectToCGRect(NSRect nsrect) {
    union _ {NSRect ns; CGRect cg;};
    return ((union _ *)&nsrect)->cg;
}
```

为什么有差异？为什么要费心创建一个联合体？为什么你不能简单地通过指针进行转换？

## 类型双关（Type punning）

尽管通过指针进行转换很常见，但它实际上是一种不良实践，并且是有潜在风险的代码。由于类型双关，通过指针进行转换可能会引入 bug。

> **类型双关（Type punning）**  
>  一种 [指针别名（pointer aliasing）](http://en.wikipedia.org/wiki/Pointer_alias) 形式，其中两个指针指向内存中的同一位置，但将该位置表示为不同的类型。编译器会将两个“双关”视为无关的指针。类型双关有可能导致通过两个指针访问的任何数据出现依赖问题。

大多数时候，类型双关不会引起任何问题。它被 C 标准视为未定义行为，但通常会按你期望的方式工作。

除非你试图通过优化从代码中榨取更多性能。具体来说，如果你在 Xcode 中打开“_Enforce Strict Aliasing_”（在 GCC 中即为 `-fstrict_aliasing`），你就有可能遇到不可预测和错误的行为。启用严格别名后，编译器可能会以错误的顺序执行操作，或者完全省略某些指令。

需要明确的是，这些 bug 只有在你**解引用**两个指针（或以其他方式访问其共享数据）于同一个作用域或函数内时才会发生。仅仅创建一个指针应该是安全的。

## 一个双关 bug 的例子

在 `NSRectToCGRect` 函数存在之前，我有一些代码如下：

```objc
NSRect ellipseBounds;
ellipseBounds.origin.x = 0;
ellipseBounds.origin.y = 0;
ellipseBounds.size.width = WIDGET_SIZE - 1.0;
ellipseBounds.size.height = WIDGET_SIZE - 1.0;
ellipseBounds = NSInsetRect(ellipseBounds, 4, 4);

CGContextAddEllipseInRect(context, *(CGRect *)&ellipseBounds);
CGContextFillPath(context);
```

这段代码创建并设置了一个 `NSRect`，然后在用它之前将其重解释为 `CGRect`。

在这个例子中，启用了 `-fstrict_aliasing` 时，GCC 选择将 `NSInsetRect` 的执行顺序排在 `CGContextAddEllipseInRect` 调用_之后_，因为当指向 `ellipseBounds` 的指针被解引用为不同类型时，两者之间的依赖关系被类型双关破坏了。

## 联合体解决了问题

这个问题的传统解决方案，即允许代码在启用 `-fstrict_aliasing` 时正确运行，是使用联合体（union）。如 `NSRectToCGRect` 代码所示，联合体应包含源类型和目标类型，你只需先设置或转换为源类型，然后从目标类型读取。

根据 C 标准，任何涉及类型双关的行为都是实现相关的。因此，从“标准”意义上讲，使用联合体并不一定能解决问题。根据标准，如果你在联合体中为一个字段设置了数据，则必须从同一个字段读取回来。

幸运的是，GCC 明确允许不同的做法。取自 GCC 文档：

> 从联合体中读取不同于最近写入的那个成员（即“类型双关”）是一种常见做法。即使启用了 `-fstrict-aliasing`，只要内存是通过联合体类型访问的，类型双关也是允许的。

太好了。

## 安全地重解释你自己的数据的宏

非常简单：

```objc
#define UNION_CAST(x, destType) \
   (((union {__typeof__(x) a; destType b;})x).b)
```

> 此示例现在包含了 Daniel Néri 在评论中建议的 `__typeof__`。

因此，你可以将一个名为 `myFloat` 的 `float` 变量转换为 `int`，如下所示：

```objc
int myInt = UNION_CAST(myFloat, int);
```

你可能会注意到，我没有费心使用内联函数，我没有给联合体命名，也没有在转换前创建指向该值的指针。Apple 的 `NSRectToCGRect` 函数做了这些事，但它们是不必要的。不过，由于编译器应该会优化掉额外的工作，Apple 代码中的函数、额外指针和解引用应该不会造成影响。

## 结论

创建指向一个值的指针，然后将该指针转换为新类型，是我见过的在 C 中重解释数据最常见的方式。尽管它很普遍，但你不应该这样做。始终通过联合体进行你的重解释转换。如果你曾经试图通过编译器选项来榨取性能，这可能会为你省去很多麻烦。
