---
title: '( ) -> ( ) · sunnyxx的技术博客'
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/10/14/fp-essential/'
original_language: zh
published: 2014-10-14
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:deac80baae91ed47'
translated: n/a
---

> 原文：[( ) -> ( ) · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/10/14/fp-essential/)　·　sunnyxx (孙源)

# ( ) -\> ( )

2014年10月14日

# 我是前言

`() -> ()`不是什么表情符号，而是一种高度抽象的编程范式，它表示了一个函数式的编程思想，即`值`的变化过程。本文将从`swift`语言入手分析，元组，函数，闭包等的设计对它进行解释，并阐释swift语言设计的大局观。随后分享一个`Reactive Cocoa`作者的Talk中的编程思想。

# 编程的核心

编程的无非两件事，`数据`和`运算`。  
放在计算机硬件，是内存和CPU；  
放在C语言，是结构体和函数（基本类型本质上就是一个只有一个字段的结构体）；  
放在面向对象的语言，是类和消息；  
放在函数式语言，就是值和函数了

如果用`()`表示数据，`->`表示运算，也是醉了

# 从Swift说起

## -\>表示运算过程

熟悉swift的同学肯定能联想到swift中函数的表示方法

```swift
func foo(number: Int) -> Int {
    return 1
}
let f = foo // f的类型为 (Int) -> Int
```

把参数通通去掉之后就成了`() -> ()`

```swift
func foo () -> () {
    // ...
}
```

像好多吐槽swift语法的人一样，起初我也不理解为什么用这么个奇葩的`->`来表示返回值，其实它并非表示返回值，而是表示`运算过程`，从入参到返回值的过程。按这个思路来看，把返回值写在函数声明前面倒是有点说不通了。

## 元组表示所有的值

再来说说这个`()`，在swift里面表示元组（tuple），值得一提的是，swift里面任何值都是一个tuple，且一共有三种Tuple：

- **0-Tuple**表示空值，也就是`Void` （Void是`()`的别名）
- **1-Tuple**表示任意一个类型的实例（Int、String、对象、枚举等等），也就是说`Int`其实是一个`(Int)`，`String`是一个`(String)`，以此类推，所以有下面的写法：

  ```swift
  var i: Int = 1
  i.0.0.0.0.0.0 // 1
  var a = ["A", "B", "C"]
  a.0.0.0.0.0.0 // ["A", "B", "C"]
  ```
- **N-Tuple**表示两个以上值的组合，如`(2, "B")`

## func是一种特殊的block

一开始我认为block是一种特殊的func，后来发现反过来理解更加合理。

```swift
class Foo {
    func bar(i: Int) {
       // ...
    }
}
var f = Foo.bar
```

其中f的类型为`Foo -> (Int) -> ()`，用括号结合一下更好理解：`Foo -> (Int -> ())`，外层传入一个Foo的实例，返回值是一个`(Int) -> ()`的函数

知道这一点，上面的方法用一个block也能轻松搞定：

```swift
var bar = {(f: Foo) -> (Int) -> () in
    return {(i: Int) in
        // ...
    }
}
```

所以说，一个`func`只是在一个`class`（或struct、enum）作用域中一个特殊的block罢了，隐式的被传入了第一层的`self`参数而已。再多想一步，假如外部有一个全局变量，在`func`中是可以访问，多么像block的捕获外部变量呢。

## swift函数式世界观

讲到这儿，swift中的`数据`+`运算`就可以被抽象成：`() -> ()`了，一切结构、函数、block，各种调用，本质上都可以被归纳成**从一个元组经过运算得到另一个元组的过程**，这不就是`函数式编程`么。  
当然，这个思想也不孤单，`java script`中也用`=>`来表示相同的概念

# Reactive Cocoa作者谈未来

说完了swift，再来说`Reactive Cocoa`  
RAC可以说是对objc语言和runtime机制使用最深刻的开源库之一了，可见作者对水平。他的`《The Future of Reactive Cocoa》`的Talk很有趣，pdf可以从[这个git地址下载](https://github.com/jspahrsummers/the-future-of-reactivecocoa)

他把函数式编程中的Event分成：

- Observer（Push）: `Event -> ()`
- Obserable（Push）: `(Event -> ()) -> ()`
- Enumerator（Pull）: `() -> Event`
- Enumerable（Pull）: `() -> (() -> Event)`

先不说具体含义，这个抽象范式的表示方法就与上面提到一致。熟悉RAC的同学将会对上面精简的概括叫绝。  
拿第二个，Obserable来说，这就是RAC中的`RACSignal`，后面的范式表示这个Event可以串联起来（当返回值的也是一个同样结构的函数时）：  
`(Event1 -> ()) -> (Event2 -> ()) ->...-> (EventN -> ()) -> ()`

## 不寻常意义的Enumerator

这里的Enumerator不是通常意义上的`for-in`语句中使用的枚举器，而是代表了一种`延时计算`的思想：不到最后一刻，这个值一直不被计算出来，向它套用的函数也都将延时到最后才依次计算。其实swift在语言基本库中就实现了它，名为`LazyBidirectionalCollection`，如一个字典：

```swift
var dict = ["A": 1, "B": 2]
var generator = dict.keys.map({$0.lowercaseString}).generate()
generator.next()! // "b" （这里进行一次计算）
generator.next()! // "a" （这里进行后一次计算）
```

# 跑题了，往回拉拉

`()`表示任意的值  
`->`表示运算过程  
所以`() -> ()`表示一个任意的函数

函数作为一等公民，可以作为值进行传递，所以上面的范式中的值也可以是函数，于是衍生出  
`(() -> ()) -> ()`或`() -> (() -> ())`

这就是函数式编程

# Reference

[https://medium.com/swift-programming/facets-of-swift-part-2-tuples-4bfe58d21abf](https://medium.com/swift-programming/facets-of-swift-part-2-tuples-4bfe58d21abf)  
[https://github.com/jspahrsummers/the-future-of-reactivecocoa](https://github.com/jspahrsummers/the-future-of-reactivecocoa)
