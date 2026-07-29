---
title: '我的愿望：为 Objective-C 添加对象字面量语法'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/syntax-additions-for-object-literals-to-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:902eadbd59c09c74'
translated: true
---

> 原文：[My Wish: Syntax Additions to Objective-C for Object Literals](https://oleb.net/blog/2010/12/syntax-additions-for-object-literals-to-objective-c/)　·　Ole Begemann

# 我的愿望：为 Objective-C 添加对象字面量语法

我[写过](https://oleb.net/blog/2010/12/method-names-in-objective-c/)[之前](https://oleb.net/blog/2010/03/if-you-want-to-learn-cocoa/)谈到 Objective-C/Cocoa 世界中对清晰性优先于简洁性的偏好，导致方法签名异常之长。虽然我喜欢这种做法的表达能力，但在某些情况下，我认为语言可以在不牺牲任何东西的前提下更加简洁。大多数时候，这与常用对象（如 `NSNumber`、`NSArray` 和 `NSDictionary`）有关。我希望 Objective-C 能像字符串那样，包含一种快速定义这些类型的对象字面量（object literal）的语法。

Objective-C 已经支持使用语法 `@"Some string"` 来定义字符串字面量对象很长时间了（尽管并非从一开始就有：`@"..."` 并不是 Objective-C 原始实现的一部分）。那么，为什么不为其他对象字面量定义类似的语法呢？以下是我希望在语言未来版本中看到的语法：

| 新语法 | 等价于 |
|---|---|
| `@1` | `[NSNumber numberWithInteger:1]` |
| `@2.5f` | `[NSNumber numberWithFloat:2.5f]` |
| `@2.5` | `[NSNumber numberWithDouble:2.5]` |
| `@YES` | `[NSNumber numberWithBool:YES]` |
| `@[@"abc", @1, @2.5, @NO]` | `[NSArray arrayWithObjects:@"abc", [NSNumber numberWithInteger:1], [NSNumber numberWithDouble:2.5], [NSNumber numberWithBool:NO], nil]` |
| `@{ @"name": @"John Appleseed", @"age": @38 }` | `[NSDictionary dictionaryWithObjectsAndKeys: @"John Appleseed", @"name", [NSNumber numberWithInteger:38], @"age", nil]` |

作为语法补充如何影响代码外观的一个例子，考虑创建一个关键帧动画。目前：

```
CAKeyframeAnimation *animation = [CAKeyframeAnimation animationWithKeyPath:@"alpha"];
animation.values   = [NSArray arrayWithObjects:
                      [NSNumber numberWithFloat:1.0f],
                      [NSNumber numberWithFloat:0.8f],
                      [NSNumber numberWithFloat:0.0f],
                      nil];
animation.keyTimes = [NSArray arrayWithObjects:
                      [NSNumber numberWithFloat:0.0f],
                      [NSNumber numberWithFloat:0.6f],
                      [NSNumber numberWithFloat:1.0f],
                      nil];
[self.view.layer addAnimation:animation forKey:@"alpha"];
```

使用新语法后，在我看来可以写得更加清晰：

```
CAKeyframeAnimation *animation = [CAKeyframeAnimation animationWithKeyPath:@"alpha"];
animation.values   = @[@1.0f, @0.8f, @0.0f];
animation.keyTimes = @[@0.0f, @0.6f, @1.0f];
[self.view.layer addAnimation:animation forKey:@"alpha"];
```

**更新于 2011 年 1 月 14 日：** 来自读者的评论：

Jens Ayton：

> 允许在复合字面量内部省略 `@`，因为无论如何你也不能把原生类型放进去。另外，允许像 JavaScript 那样，让类似关键字的字典键不加引号。

Bavarious 提到了 Mike Ash 创建的一组用于简化集合创建的宏：[MACollectionUtilities](https://github.com/mikeash/MACollectionUtilities)。语法没那么漂亮，但易于实现。

我的同事 Christian 和 Alexis 建议再增加两种字面量：

- `@/…/` 用于 `NSRegularExpression`
- `@<>` 用于包含二进制内容（十六进制）的 `NSData`

---

**更新于 2012 年 5 月 10 日：** Stig Brautaset 向我指出，他[早在 2008 年就写过这个话题](http://skuggdev.wordpress.com/2008/08/25/objective-c-syntax-sugar-wish-list/)，并提出了非常相似的建议。谢谢你，Stig，我之前不知道！
