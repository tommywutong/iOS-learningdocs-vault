---
title: Objective-C 中的方法名称
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/12/method-names-in-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0ee2d52ef99fc283'
translated: true
---

> 原文：[Method Names in Objective-C](https://oleb.net/blog/2010/12/method-names-in-objective-c/)　·　Ole Begemann

# Objective-C 中的方法名称

Apple 的 Cocoa 框架以其极长且描述性强的方法名称而闻名。举一个极端的例子，以下是一个用于以特定位图格式初始化 `NSBitmapImageRep` 实例的方法（仅适用于 Mac，不适用于 iOS）：

```
- (id)initWithBitmapDataPlanes:(unsigned char **)planes
                    pixelsWide:(NSInteger)width
                    pixelsHigh:(NSInteger)height
                 bitsPerSample:(NSInteger)bps
               samplesPerPixel:(NSInteger)spp
                      hasAlpha:(BOOL)alpha
                      isPlanar:(BOOL)isPlanar
                colorSpaceName:(NSString *)colorSpaceName
                  bitmapFormat:(NSBitmapFormat)bitmapFormat
                   bytesPerRow:(NSInteger)rowBytes
                  bitsPerPixel:(NSInteger)pixelBits
```

Objective-C（这门语言）以其语法帮助 Cocoa（框架）在追求所有框架中最长方法名称的道路上更进一步。冒号之前用于描述每个参数的文本并非命名参数，而是方法签名本身的重要组成部分。因此，上述方法的签名是：

```
initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:
```

描述性很强，不是吗？尽管 Cocoa 及其他框架中几乎所有方法都遵循这种模式，但在 Objective-C 中，所有描述方法参数的文本实际上都是可选的。所以，`CAMediaTimingFunction` 类中的以下方法拥有一个完全有效的名称：

```
+ (id)functionWithControlPoints:(float)c1x
                               :(float)c1y
                               :(float)c2x
                               :(float)c2y
```

因此，该方法的选择器（selector）是：

```
functionWithControlPoints::::
```

在我看来并不美观，但可行。现在事情变得真正奇怪起来了。既然我们可以省略从第二个参数及以后所有参数之前的文本，为什么不能同样省略第一个参数之前的文本呢？事实证明，我们完全可以做到这一点！

信不信由你，以下这些是有效的方法声明：

```
- (void):(id)param;
- (void):(id)param1 :(id)param2;
```

而这就是你向对象发送这些消息的方式：

```
[myObject :obj1];
[myObject :obj1 :obj2];
```

请永远不要在你自己的代码中使用这个知识。

**2010 年 12 月 19 日更新：** 碰巧，Stack Overflow 用户 [outis](http://stackoverflow.com/users/90527/outis) 前几天问了一个关于 Obj-C 消息名称的非常有趣的问题：[为什么 Objective-C 方法名称的最后一部分必须带参数？](http://stackoverflow.com/questions/4479967/why-must-the-last-part-of-an-objective-c-method-name-take-an-argument-when-there) 这些答案读起来很有意思，甚至 Objective-C 语言的设计者 Brad Cox 本人也回答了：[我当时只是没想到要脱离 Smalltalk 的关键字结构。](http://stackoverflow.com/questions/4479967/why-must-the-last-part-of-an-objective-c-method-name-take-an-argument-when-there/4485347#4485347)
