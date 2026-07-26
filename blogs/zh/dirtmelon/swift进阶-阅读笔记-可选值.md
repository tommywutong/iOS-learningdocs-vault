---
title: 《Swift进阶》阅读笔记 - 可选值
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/advanced-swift-optional/'
original_language: zh
published: 2017-03-14
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0c76ba2df23f65d6'
translated: n/a
---

> 原文：[《Swift进阶》阅读笔记 - 可选值](https://dirtmelon.github.io/posts/advanced-swift-optional/)　·　dirtmelon

## 哨岗值

当返回一个“魔法数”来表示函数没有返回真实的值，这样的值称为“哨岗值”。哨岗值很容易产生问题，因为可能忘记检查哨岗值，并且不小心使用了它们。

## 通过枚举解决魔法数的问题

```swift
enum Optional<Wrapped> {
    case none
    case some(wrapped)
}
```

获取关联值的唯一方法是使用 switch 或者 if case 语句。和哨岗值不同，除非你显式地检查并解包，你是不可能意外地使用到一个 Optional 中的值的。

```swift
var array = ["one", "two", "three", "four"]
switch array.index(of: "four") {
case let idx?:
	  array.remove(at: idx)
default:
	  break
}
```

## 可选值概览

- if let 通常情况下可以使用if let来进行可选绑定：

```swift
var array = ["one", "two", "three", "four"]
if let idx = array.index(of: "four") {
	   array.remove(at: idx)
}

// 可选绑定跟布尔语句搭配
if let idx = array.index(of: "four"), idx != array.startIndex{
	  array.remove(at: idx)
}

// if语句绑定多个值，后面的绑定值可以调用之前成功解包的值来进行操作，每个let也可以跟一个布尔语句绑定
let urlString = "http://www.objc.io/logo.png"
if let url = URL(string: urlString),
	  let data = try?Data(contentsOf: url), url.pathExtension == "png",
	  let image = UIImage(data: data) {
    let view = UIImageView(image: image)
	// ...
}

// 也可以为if let提供前置条件进行检查
if segue.identifier == "showUserDetailsSegue",
	let userDetailVC = segue.destination
	as? UserDetailViewController {
	userDetailVC.screenName = "Hello"
}
```

- while let 表示遇到nil时终止循环。

```swift
// 跟布尔语句搭配
while let line = readLine(), !line.isEmpty {
	print(line)
}
```

- 双重可选值

一个可选值本身被另一个可选值包装起来。next()函数返回的是一个Optional\<Optional\>值。

```swift
let stringNumbers = ["1", "2", "three"]
let maybeInts = stringNumbers.map { Int($0) }

var iterator = maybeInts.makeIterator()
while let maybeInt = iterator.next() {
	  print(maybeInt)
}
/*
Optional(1)
Optional(2)
nil
*/

// if case 模式匹配
for case let i? in maybeInts {
	// i 将是 Int 值，而不是 Int?
	print(i, terminator: " ")
}

// 或者只对 nil 值进行循环
for case nil in maybeInts {
// 将对每个 nil 执行一次
print("No value")
}
```

- if var and while var

var也可以跟if，while和for搭配：

```swift
let number = "1"
if var i = Int(number) {
	i += 1
	print(i) // 2
}
print(number) // 1, i为值类型，不会改变原来的值。
```

- 解包后的作用域

使用guard let提早退出来避免if嵌套：

```swift
extension String {
	var fileExtension: String? {
		guard let period = characters.index(of: ".") else { return nil }
		let extensionRange = index(after: period)..<characters.endIndex
		return self[extensionRange]
	}
}
"hello.txt".fileExtension
```

等价于：

```swift
extension String {
	var fileExtension: String? {
		let period: String.Index
		if let idx = characters.index(of: ".") {
			period = idx
		} else {
			return nil
		}
		let extensionRange = index(after: period)..<characters.endIndex
		return self[extensionRange]
	}
}
```

在guard的else中必须离开当前的作用域，如return，fatalError，break或者continue等。如果没有的话，编译器会报错，因此应尽量使用guard。

- 可选链

> 在 Objective-C 中，对 nil 发消息什么都不会发生。Swift 里，我们可以通过“可选链 (optional chaining)”来达到同样的效果。

```swift
delegate?.callback()
```

- nil合并运算符

```swift
// 可用于提供默认值
let stringteger = "1"
let number = Int(stringteger) ?? 0

// 也可以进行链接
let i: Int? = nil
let j: Int? = nil
let k: Int? = 42
i ?? j ?? k // Optional(42) 
```

- 可选值map

可选值的map跟序列中的map不同之处在于，可选值的map只会操作一个值，就是该可选值中那个可能的值。可选值可以看作包含零个或者一个值的集合。 所以map要么不做处理，要么在有值的情况下进行转换：

```swift
extension Optional {
    func map<U>(transform: (Wrapped) -> U) -> U? {
        if let value = self {
            return transform(value)
        }
    return nil
    }
}
```

- 可选值判等

1. == 有一个接收两个可选值的版本：

```swift
func ==<T: Equatable>(lhs: T?, rhs: T?) -> Bool {
    switch (lhs, rhs) {
        case (nil, nil): return true
        case let (x?, y?): return x == y
        case (_?, nil), (nil, _?): return false
    }
}
```

_当你在使用一个非可选值时，如果需要匹配非可选值，Swift 会将它变成一个可选值然后使用_

1. Equatable 和 == 数组中 == 操作符需要数组元素遵守 Equatable 协议。
2. switch－case 匹配可选值 需要实现 Equatable 中的 ~= 运算符

## 强制解包的时机

> 当你能确定你的某个值不可能是 nil 时可以使用叹号，你应当会希望如果它不巧意外地是 nil 的话，这句程序直接挂掉。

### 改进强制解包的错误信息

```swift
infix operator !!
func !!<T>(wrapped: T?, failureText: @autoclosure () -> String) -> T {
	if let x = wrapped {
		return x
	}
	fatalError(failureText())
}

let s = "foo"
let i = Int(s) !! "Expecting integer, got \"\(s)\""
```

### 在调试版本中进行断言

在调试或者测试版本中进行断言，正式版本中提供默认值。

```swift
infix operator !?
func !?<T: ExpressibleByIntegerLiteral>(wrapped: T?, failureText: @autoclosure () -> String) -> T {
	  assert(wrapped != nil, failureText)
	  return wrapped ?? 0
}
```

ExpressibleByIntegerLiteral 改为 ExpressibleByArrayLiteral ，ExpressibleByStringLiteral则可以覆盖数组和字符串类型。

挂起操作有三种方式：

1. `fatalError` 无条件停止操作，可以接受一条信息
2. `assert` 会进行条件监测， `false` 时停止操作，正式版本中会被移除掉
3. `precondition` 跟 `assert` 比较类似，但是在正式版本中不会被移除
