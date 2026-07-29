---
title: 使用指针参数调用函数
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/calling-functions-with-pointer-parameters
source_url: 'https://developer.apple.com/documentation/swift/calling-functions-with-pointer-parameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/calling-functions-with-pointer-parameters.json'
content_hash: 'sha256:a70414a574a97ca9'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [手动内存管理](manual-memory-management.md)

# 使用指针参数调用函数

<sub>文章</sub>

在调用以指针作为参数的函数时，使用隐式指针转换或桥接。

## 概述

在调用以指针作为参数的函数时，你可以通过隐式转换来传递兼容的指针类型，或者通过隐式桥接来传递指向变量或数组内容的指针。

### 传递常量指针作为参数

当调用声明为接受 `UnsafePointer<Type>` 参数的函数时，你可以传递以下任意一种：

- `UnsafePointer<Type>`、`UnsafeMutablePointer<Type>` 或 `AutoreleasingUnsafeMutablePointer<Type>` 类型的值，它们会根据需要隐式转换为 `UnsafePointer<Type>`。
- 一个 `String` 值，前提是 `Type` 为 `Int8` 或 `UInt8`。该字符串会自动以 UTF8 格式转换并放入一个零结尾的缓冲区，然后将指向该缓冲区的指针传递给函数。
- 一个包含 `Type` 类型的可变变量、属性或下标引用的 in-out 表达式，该表达式会作为指针传递给左侧标识符的地址。
- 一个 `[Type]` 值，该值作为指针传递给数组的起始位置。

你传递给函数的指针只在函数调用期间保证有效。请勿在函数返回后继续持有并使用该指针。

以下示例展示了调用接受常量指针的函数的不同方式：

```swift
func takesAPointer(_ p: UnsafePointer<Float>) {
    // ...
}

var x: Float = 0.0
takesAPointer(&x)
takesAPointer([1.0, 2.0, 3.0])
```

当调用接受 `UnsafeRawPointer` 参数的函数时，你可以传递与 `UnsafePointer<Type>` 相同的操作数，但 `Type` 可以是任意类型。

以下示例展示了调用接受常量原始指针的函数的不同方式：

```swift
func takesARawPointer(_ p: UnsafeRawPointer?)  {
    // ...
}

var x: Float = 0.0, y: Int = 0
takesARawPointer(&x)
takesARawPointer(&y)
takesARawPointer([1.0, 2.0, 3.0] as [Float])
let intArray = [1, 2, 3]
takesARawPointer(intArray)
takesARawPointer("How are you today?")
```

### 传递可变指针作为参数

当调用声明为接受 `UnsafeMutablePointer<Type>` 参数的函数时，你可以传递以下任意一种：

- `UnsafeMutablePointer<Type>` 类型的值。
- 一个 `Type` 类型的 in-out 表达式，其中包含可变变量、属性或下标引用，该表达式会作为指针传递给可变值的地址。
- 一个 `[Type]` 类型的 in-out 表达式，其中包含可变变量、属性或下标引用，该表达式会作为指针传递给数组的起始位置，并且其生命周期会延长至函数调用结束。

以下示例展示了调用接受可变指针的函数的不同方式：

```swift
func takesAMutablePointer(_ p: UnsafeMutablePointer<Float>) {
    // ...
}

var x: Float = 0.0
var a: [Float] = [1.0, 2.0, 3.0]
takesAMutablePointer(&x)
takesAMutablePointer(&a)
```

当调用声明为接受 `UnsafeMutableRawPointer` 参数的函数时，你可以传递与 `UnsafeMutablePointer<Type>` 相同的操作数，但 `Type` 可以是任意类型。

以下示例展示了调用接受可变原始指针的函数的不同方式：

```swift
func takesAMutableRawPointer(_ p: UnsafeMutableRawPointer?)  {
    // ...
}

var x: Float = 0.0, y: Int = 0
var a: [Float] = [1.0, 2.0, 3.0], b: [Int] = [1, 2, 3]
takesAMutableRawPointer(&x)
takesAMutableRawPointer(&y)
takesAMutableRawPointer(&a)
takesAMutableRawPointer(&b)
```

### 传递自动释放指针作为参数

当调用声明为接受 `AutoreleasingUnsafeMutablePointer<Type>` 参数的函数时，你可以传递以下任意一种：

- `AutoreleasingUnsafeMutablePointer<Type>` 类型的值。
- 一个 in-out 表达式，其中包含 `Type` 类型的可变变量、属性或下标引用。操作数的值会被按位复制到一个临时的非拥有缓冲区中。该缓冲区的地址被传递给被调用方，返回时，缓冲区中的值会被加载、保留并重新赋值给操作数。

与其他指针类型不同，你不能将数组作为隐式桥接参数传递。

### 传递函数指针作为参数

当调用接受 C 函数指针参数的函数时，你可以传递一个顶层 Swift 函数、一个闭包（closure）字面量、一个使用 `@convention(c)` 特性（attribute）声明的闭包，或者 `nil`。只要闭包的参数列表或主体中没有引用泛型类型参数，你也可以传递泛型类型或泛型方法的闭包属性。

以 Core Foundation 的 `CFArrayCreateMutable(_:_:_:)` 函数为例。`CFArrayCreateMutable(_:_:_:)` 函数接受一个 `CFArrayCallBacks` 结构体，该结构体使用函数指针回调进行初始化：

```swift
func customCopyDescription(_ p: UnsafeRawPointer?) -> Unmanaged<CFString>? {
    // 返回一个 Unmanaged<CFString>? 值
}

var callbacks = CFArrayCallBacks(
    version: 0,
    retain: nil,
    release: nil,
    copyDescription: customCopyDescription,
    equal: { (p1, p2) -> DarwinBoolean in
        // 返回 Bool 值
    }
)
var mutableArray = CFArrayCreateMutable(nil, 0, &callbacks)
```

在这个示例中，`CFArrayCallBacks` 初始化方法将 `nil` 值作为 `retain` 和 `release` 参数的值，将 `customCopyDescription(_:)` 函数作为 `customCopyDescription` 参数的值，并将一个闭包字面量作为 `equal` 参数的值。

> [!note] 注意
> 只有使用 C 函数引用调用约定的 Swift 函数类型才能用于函数指针参数。与 C 函数指针类似，带有 `@convention(c)` 特性的 Swift 函数类型不会捕获其周围作用域的上下文。
