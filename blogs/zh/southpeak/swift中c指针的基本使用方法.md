---
title: Swift中C指针的基本使用方法
source: 南峰子 (southpeak)
source_key: southpeak
source_url: 'https://southpeak.github.io/2014/07/02/ios-swift-cpointer-1/'
original_language: zh
published: 2016-08-27
status: frozen
license: © 2017 南峰子（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fdf622f0751dc0d3'
translated: n/a
---

> 原文：[Swift中C指针的基本使用方法](https://southpeak.github.io/2014/07/02/ios-swift-cpointer-1/)　·　南峰子 (southpeak)

Swift尽可能避免让我们直接去访问指针。但当我们需要直接访问内存时，我们可以使用Swift提供的几种指针类型。在下面几个表中列出了各种情况下C类型指针语法与Swift语法对应关系，其中Type作为实际类型的占位符

对于函数参数，有以下对应关系

| C语法 | Swift语法 |
|---|---|
| const void * | CConstVoidPointer |
| void * | CMutableVoidPointer |
| const Type * | CConstPointer |
| Type * | CMutablePointer |

对于返回值，变量，二级以上的指针参数，有以下对应关系

| C语法 | Swift语法 |
|---|---|
| void * | COpaquePointer |
| Type * | UnsafePointer |

对于类类型，有以下对应关系

| C语法 | Swift语法 |
|---|---|
| Type _const_ | CConstPointer |
| Type ___strong_ | CMutablePointer |
| Type ** | AutoreleasingUnsafePointer |

下面简单介绍一下这几种类型的指针

## C可变指针

当我们声明一个包含CMutablePointer参数的指针时，可以接收以下类型的值

1. nil, 作为空指针传入
2. 一个CMutablePointer

  值
3. 一个in-out表达式，它的操作数是Type类型的左值。该表达式作为左值地址传入
4. 一个in-out Type[]值，它作为数组的首地址指针传入，且在调用时扩展了数据的生命周期

假如我们声明了如下一个函数：

```swift
func takesAMutablePointer(x: CMutablePointer<Float>) { /*...*/ }
```

那么我们可以用以下任何一种方式来调用

```plain
var x: Float = 0.0
var p: CMutablePointer<Float> = &x
var a: Float[] = [1.0, 2.0, 3.0]

takesAMutablePointer(nil)
takesAMutablePointer(p)
takesAMutablePointer(&x)
takesAMutablePointer(&a)
```

当声明一个包含CMutableVoidPointer参数的函数时，它可以接收与CMutablePointer相同的形参，其中Type为任意类型。需要注意的是如果直接传递CMutablePointer，目前的编译器会直接报编译错误

```swift
func takesAMutableVoidPointer(x: CMutableVoidPointer) { /* ... */ }

var x: Float = 0.0, y: Int = 0
var p: CMutablePointer<Float> = &x, q: CMutablePointer<Int> = &y
var a: Float[] = [1.0, 2.0, 3.0], b: Int[] = [1, 2, 3]

takesAMutableVoidPointer(nil)
//takesAMutableVoidPointer(p)	编辑错误:CMutablePointer<Float> is not convertible to CMutableVoidPointer
//takesAMutableVoidPointer(q)
takesAMutableVoidPointer(&x)
takesAMutableVoidPointer(&y)
takesAMutableVoidPointer(&a)
takesAMutableVoidPointer(&b)
```

## C常量指针

当我们声明一个带有CConstPointer参数的函数时，可以接收以下类型的值：

1. nil, 作为空指针传入
2. 一个CMutablePointer

  , CMutableVoidPointer, CConstPointer, CConstVoidPointer, 或者AutoreleasingUnsafePointer类型的值，如果需要则会转换成CConstPointer
3. 一个in-out表达式，它的操作数是Type类型的左值。该表达式作为左值地址传入
4. 一个in-out Type[]值，它作为数组的首地址指针传入，且在调用时扩展了数据的生命周期

假如我们声明如下函数:

```swift
func takesAConstPointer(x: CConstPointer<Float>) { /*...*/ }
```

那么我们可以用以下任何一种方式来调用

```swift
var x: Float = 0.0
var p: CConstPointer<Float> = nil

takesAConstPointer(nil)
takesAConstPointer(p)
takesAConstPointer(&x)
takesAConstPointer([1.0, 2.0, 3.0])
```

当声明一个包含CConstVoidPointer参数的函数时，它可以接收与CConstPointer相同的形参，其中Type为任意类型。

```swift
func takesAConstVoidPointer(x: CConstVoidPointer) { /* ... */ }

var x: Float = 0.0, y: Int = 0
var p:CConstPointer<Float> = nil, q: CConstPointer<Int> = nil

takesAConstVoidPointer(nil)
//takesAConstVoidPointer(p)
//takesAConstVoidPointer(q)
takesAConstVoidPointer(&x)
takesAConstVoidPointer(&y)
takesAConstVoidPointer([1.0, 2.0, 3.0])
takesAConstVoidPointer([1, 2, 3])
```

## AutoreleasingUnsafePointer

当我们声明一个带有AutoreleasingUnsafePointer参数的函数时，可以接收以下类型的值：

1. nil, 作为空指针传入
2. 一个AutoreleasingUnsafePointer

  值
3. 一个in-out表达式，其操作数是临时非所属(nonowning)缓冲区，存储了原始值的拷贝。缓冲区的地址被传递给调用函数，且在返回时，缓冲区的值被加载(loaded)、保留(retained)并重新指派(reassigned)给操作数

注意上面清单中不包含数组

如果我们声明了以下函数

```swift
func takesAnAutoreleasingUnsafePointer(x: AutoreleasingUnsafePointer<NSDate?>) { /*...*/ }
```

则可以用以下方式来调用

```swift
var x: NSDate? = nil
var p: AutoreleasingUnsafePointer<NSDate?> = nil

takesAnAutoreleasingUnsafePointer(nil)
takesAnAutoreleasingUnsafePointer(p)
takesAnAutoreleasingUnsafePointer(&x)
```

最后需要注意的是在Swift中，没有导入C函数指针。

参考文档：[Using Swift with Cocoa and Objective-C](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/BuildingCocoaApps/index.html)
