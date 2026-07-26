---
title: iOS 中集合遍历方法的比较和技巧 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/04/30/ios_iterator/'
original_language: zh
published: 2014-04-30
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e1f2643e66ae736f'
translated: n/a
---

> 原文：[iOS 中集合遍历方法的比较和技巧 · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/04/30/ios_iterator/)　·　sunnyxx (孙源)

# iOS 中集合遍历方法的比较和技巧

2014年4月30日

# [#我是前言](#我是前言)我是前言

集合的遍历操作是开发中最常见的操作之一，从C语言经典的for循环到利用多核cpu的优势进行遍历，开发中ios有若干集合遍历方法，本文通过研究和测试比较了各个操作方法的效率和优略势，并总结几个使用集合遍历时的小技巧。

---

# [#ios中常用的遍历运算方法](#ios中常用的遍历运算方法)ios中常用的遍历运算方法

遍历的目的是获取集合中的某个对象或执行某个操作，所以能满足这个条件的方法都可以作为备选：

- 经典for循环
- 《nshipster介绍NSFastEnumeration的文章》
- makeObjectsPerformSelector
- kvc集合运算符
- enumerateObjectsUsingBlock
- enumerateObjectsWithOptions(NSEnumerationConcurrent)
- dispatch_apply

---

# [#实验](#实验)实验

## [#实验条件](#实验条件)实验条件

测试类如下：

```objc
@interface Sark : NSObject
@property (nonatomic) NSInteger number;
- (void)doSomethingSlow; // sleep(0.01)
@end
```

实验从两个方面来评价：

1. 分别使用有 100 个对象和 1000000 个对象的 NSArray，只取对象，不执行操作，测试遍历速度
2. 方法，测试遍历中多任务运行速度

实验使用`CFAbsoluteTimeGetCurrent()`记录时间戳来计算运行时间，单位秒。  
运行在 iPhone5 真机（双核cpu）

## [#实验数据](#实验数据)实验数据

100对象遍历操作：

```objc
经典for循环 - 0.001355
for in (NSFastEnumeration) - 0.002308
makeObjectsPerformSelector - 0.001120
kvc集合运算符(@sum.number) - 0.004272
enumerateObjectsUsingBlock - 0.001145
enumerateObjectsWithOptions(NSEnumerationConcurrent) - 0.001605
dispatch_apply(Concurrent) - 0.001380
```

1000000对象遍历操作：

```objc
经典for循环 - 1.246721
for in (NSFastEnumeration) - 0.025955
makeObjectsPerformSelector - 0.068234
kvc集合运算符(@sum.number) - 21.677246
enumerateObjectsUsingBlock - 0.586034
enumerateObjectsWithOptions(NSEnumerationConcurrent) - 0.722548
dispatch_apply(Concurrent) - 0.607100
```

100对象遍历执行一个很费时的操作：

```objc
经典for循环 - 1.106567
for in (NSFastEnumeration) - 1.102643
makeObjectsPerformSelector - 1.103965
kvc集合运算符(@sum.number) - N/A
enumerateObjectsUsingBlock - 1.104888
enumerateObjectsWithOptions(NSEnumerationConcurrent) - 0.554670
dispatch_apply(Concurrent) - 0.554858
```

---

## [#值得注意的](#值得注意的)值得注意的

- 的遍历速度非常之快，但小规模的遍历并不明显（还没普通for循环快）
- 运算很大规模的集合时，效率明显下降（100万的数组离谱的21秒多），同时占用了大量内存和cpu
- 和

  的遍历执行可以利用到多核cpu的优势（实验中在双核cpu上效率基本上x2）

---

# [#遍历实践Tips](#遍历实践Tips)遍历实践Tips

## [#倒序遍历](#倒序遍历)倒序遍历

`NSArray`和`NSOrderedSet`都支持使用`reverseObjectEnumerator`倒序遍历，如：

```objc
NSArray *strings = @[@"1", @"2", @"3"];
for (NSString *string in [strings reverseObjectEnumerator]) {
    NSLog(@"%@", string);
}
```

这个方法只在循环第一次被调用，所以也不必担心循环每次计算的问题。

同时，使用`enumerateObjectsWithOptions:NSEnumerationReverse`也可以实现倒序遍历：

```objc
[array enumerateObjectsWithOptions:NSEnumerationReverse usingBlock:^(Sark *sark, NSUInteger idx, BOOL *stop) {
    [sark doSomething];
}];
```

## [#使用block同时遍历字典key，value](#使用block同时遍历字典key，value)使用block同时遍历字典key，value

block版本的字典遍历可以同时取key和value（forin只能取key再手动取value），如：

```objc
NSDictionary *dict = @{@"a": @"1", @"b": @"2"};
[dict enumerateKeysAndObjectsUsingBlock:^(id key, id obj, BOOL *stop) {
    NSLog(@"key: %@, value: %@", key, obj);
}];
```

## [#对于耗时且顺序无关的遍历，使用并发版本](#对于耗时且顺序无关的遍历，使用并发版本)对于耗时且顺序无关的遍历，使用并发版本

```objc
[array enumerateObjectsWithOptions:NSEnumerationConcurrent usingBlock:^(Sark *sark, NSUInteger idx, BOOL *stop) {
    [sark doSomethingSlow];
}];
```

遍历执行block会分配在多核cpu上执行（底层很可能就是gcd的并发queue），对于耗时的任务来说是很值得这么做的，而且在以后cpu升级成更多核心后不用改代码也可以享受带来的好处。同时，对于遍历的外部是保持同步的（遍历都完成后才继续执行下一行），猜想内部大概是gcd的dispatch_group或者信号量控制。

## [#代码可读性和效率的权衡](#代码可读性和效率的权衡)代码可读性和效率的权衡

虽然说上面的测试结果表明，在集合内元素不多时，经典for循环的效率要比forin要高，但是从代码可读性上来看，就远不如forin看着更顺畅；同样的还有kvc的集合运算符，一些内置的操作以`keypath`的方式声明，相比自己用for循环实现，一行代码就能搞定，清楚明了，还省去了重复工作；在framework中增加了集合遍历的block支持后，对于需要index的遍历再也不需要经典for循环的写法了。

---

# [#References](#References)References

[http://nshipster.com/enumerators/](http://nshipster.com/enumerators/)  
[http://iosdevelopertips.com/objective-c/fast-enumeration-on-the-iphone.html](http://iosdevelopertips.com/objective-c/fast-enumeration-on-the-iphone.html)

---

原创文章，转载请注明源地址，[blog.sunnyxx.com](http://blog.sunnyxx.com)
