---
title: 在 Swift 中使用导入的 C 函数
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-imported-c-functions-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-imported-c-functions-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-imported-c-functions-in-swift.json'
content_hash: 'sha256:7c544edff4c46548'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md)

# 在 Swift 中使用导入的 C 函数

<sub>文章</sub>

了解如何调用在 C 头文件中声明的导入函数。

## 概述

Swift 会把 C 头文件中声明的任何函数都导入为 Swift 全局函数。

例如，考虑以下 C 函数声明：

```occ
int product(int multiplier, int multiplicand);
int quotient(int dividend, int divisor, int *remainder);

struct Point2D createPoint2D(float x, float y);
float distance(struct Point2D from, struct Point2D to);
```

Swift 导入它们的方式如下：

```swift
func product(_ multiplier: Int32, _ multiplicand: Int32) -> Int32
func quotient(_ dividend: Int32, _ divisor: Int32, _ remainder: UnsafeMutablePointer<Int32>) -> Int32

func createPoint2D(_ x: Float, _ y: Float) -> Point2D
func distance(_ from: Point2D, _ to: Point2D) -> Float
```

### 使用 CVaListPointer 调用变参函数

在 Swift 中，你可以使用 Swift 的 [getVaList(_:)](<getvalist(__).md>) 或 [withVaList(_:_:)](<withvalist(____).md>) 函数来调用 C 变参函数，例如 `vasprintf(_:_:_:)`。`withVaList(_:_:)` 函数接受一个 [CVarArg](cvararg.md) 值数组，并在闭包参数的函数体内提供一个 [CVaListPointer](cvalistpointer.md) 值，而 `getVaList(_:)` 函数则直接返回该值。无论使用哪个函数，你都把得到的 `CVaListPointer` 值作为 `va_list` 实参传给 C 变参函数。

例如，在 Swift 中调用 `vasprintf(_:_:_:)` 函数的方式如下：

```swift
func swiftprintf(format: String, arguments: CVarArg...) -> String? {
    return withVaList(arguments) { va_list in
        var buffer: UnsafeMutablePointer<Int8>? = nil
        return format.withCString { cString in
            guard vasprintf(&buffer, cString, va_list) != 0 else {
                return nil
            }

            return String(validatingUTF8: buffer!)
        }
    }
}
print(swiftprintf(format: "√2 ≅ %g", arguments: sqrt(2.0))!)
// 输出 "√2 ≅ 1.41421"
```

Swift 只导入以 `va_list` 接收参数的 C 变参函数。使用 `...` 语法接收变参的 C 函数不会被导入，因此无法通过 `CVarArg` 实参来调用。

### 调用带指针参数的函数

只要有可能，Swift 都会避免让你直接访问指针。不过在导入 C 函数参数时，Swift 会把指针参数映射为标准库的指针类型。下表用 `Type` 作为占位类型名来表示这些映射的语法。

对于返回类型、变量和实参，适用以下映射：

| C 语法 | Swift 语法 |
|---|---|
| `const Type *` | [UnsafePointer](unsafepointer.md)\<Type\> |
| `Type *` | [UnsafeMutablePointer](unsafemutablepointer.md)\<Type\> |

对于类类型，适用以下映射：

| C 语法 | Swift 语法 |
|---|---|
| `Type * const *` | [UnsafePointer](unsafepointer.md)\<Type\> |
| `Type * __strong *` | [UnsafeMutablePointer](unsafemutablepointer.md)\<Type\> |
| `Type **` | [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md)\<Type\> |

对于指向未定型的原始内存的指针，适用以下映射：

| C 语法 | Swift 语法 |
|---|---|
| `const void *` | [UnsafeRawPointer](unsaferawpointer.md) |
| `void *` | [UnsafeMutableRawPointer](unsafemutablerawpointer.md) |

C 函数指针会以采用 C 函数指针调用约定的闭包的形式导入到 Swift 中，用 `@convention(c)` 属性表示。例如，C 中类型为 `int (*)(void)` 的函数指针，导入 Swift 后就是 `@convention(c) () -> Int32`。

如果 C 指针所指向的值无法用 Swift 表示（例如不完整的结构体类型），该指针就会被导入为 `OpaquePointer`。

## 另请参阅

### C API

- [在 Swift 中使用导入的 C 结构体与联合体](using-imported-c-structs-and-unions-in-swift.md) —— 了解 Swift 如何表示导入的 C 结构体与联合体，包括带位域（bitfield）和未命名字段的类型。
- [在 Swift 中使用导入的 C 宏](using-imported-c-macros-in-swift.md) —— 将导入的 C 定义的宏用作常量。
