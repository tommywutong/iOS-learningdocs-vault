---
title: Swift 模块中的 API 污染
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/swift-api-pollution/'
original_language: en
published: 2019-02-18
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:35133f341949d581'
translated: true
---

> 原文：[API Pollution in Swift Modules](https://nshipster.com/swift-api-pollution/)　·　NSHipster (Mattt)

# [Swift 模块中的 API 污染](https://nshipster.com/swift-api-pollution/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2019 年 2 月 18 日

将模块导入 Swift 代码时，你会期待结果完全是增益性的。也就是说，获得新功能不该付出代价，至多只是 App bundle 的体积略有增加。

导入 `NaturalLanguage` 框架，*砰*的一声，你的 App 就能[识别文本语言](https://nshipster.com/nllanguagerecognizer/)；导入 `CoreMotion`，*嗖*的一声，App 就能[响应设备方向变化](https://nshipster.com/cmdevicemotion/)。但如果区分法语与日语的能力妨碍了 App 判断磁北方向，那就令人意外了。

这个特定例子并不真实（北海道的法语使用者可以松口气），但有些情况下 Swift 依赖会改变 App 的行为，*即使你没有直接使用它*。

本周会看看导入模块如何悄悄改变既有代码的行为，并分别为 API 提供者与 API 使用者提出预防和缓解建议。

## 模块污染

这是一个和 `<time.h>` 一样古老的故事：两个东西都叫 `Foo`，编译器必须决定怎么办。

几乎所有具有代码复用机制的语言，都必须以某种方式处理命名冲突。在 Swift 中，可以使用全限定名来区分模块 `A` 中声明的 `Foo` 类型（`A.Foo`）与模块 `B` 中的 `Foo` 类型（`B.Foo`）。不过 Swift 有一些独特特征，会让其他歧义逃过编译器检查；导入模块后，这可能改变既有行为。

### 运算符重载

在 Swift 中，当 `+` 的操作数是数组时，它表示拼接。一个数组加上另一个数组，结果是前一个数组的元素后接后一个数组的元素。

```
let oneTwoThree: [Int] = [1, 2, 3]
let fourFiveSix: [Int] = [4, 5, 6]
oneTwoThree + fourFiveSix // [1, 2, 3, 4, 5, 6]
```

查看该运算符在[标准库中的声明](https://github.com/apple/swift/blob/master/stdlib/public/core/Array.swift#L1318-L1324)，可以看到它由 `Array` 的非限定扩展提供：

```
extension Array {
  @inlinable public static func + (lhs: Array, rhs: Array) -> Array {}
}
```

Swift 编译器负责将 API 调用解析到相应实现。若一次调用匹配多个声明，编译器会选择其中最具体的声明。

为说明这一点，考虑 `Array` 的以下条件扩展：它为元素遵守 `Numeric` 的数组定义 `+`，执行逐成员相加：

```
extension Array where Element: Numeric {
    public static func + (lhs: Array, rhs: Array) -> Array {
        return Array(zip(lhs, rhs).map {$0 + $1})
    }
}

oneTwoThree + fourFiveSix // [5, 7, 9] 😕
```

因为 `Element: Numeric` 的要求比标准库中非限定的声明更具体，Swift 编译器会把 `+` 解析为这个函数。

这些新语义本身也许完全可接受，甚至更可取。但前提是你知道它们的存在。问题在于，只要*导入*了包含这种声明的模块，你就可能在毫不知情的情况下改变整个 App 的行为。

问题不限于语义，也可能因易用性便利而产生。

### 函数遮蔽

Swift 的函数声明可以为尾部参数指定默认实参，让调用者可以省略它们（尽管它们不一定是 `Optional`）。例如，顶层函数 [`dump(_:name:indent:maxDepth:maxItems:)`](https://developer.apple.com/documentation/swift/1539127-dump) 的参数数量颇为吓人：

```
@discardableResult func dump<T>(_ value: T, name: String? = nil, indent: Int = 0, maxDepth: Int = .max, maxItems: Int = .max) -> T
```

但得益于默认实参，只需指定第一个参数即可调用：

```
dump("🏭💨") // "🏭💨"
```

然而，方法签名重叠时，这种便利会造成困惑。

设想一个假想模块，它不了解内建的 `dump` 函数，于是定义了一个 `dump(_:)` 来打印字符串的 UTF-8 码元：

```
public func dump(_ string: String) {
    print(string.utf8.map {$0})
}
```

Swift 标准库中声明的 `dump` 函数，其第一个参数是非限定的泛型 `T`（实际上相当于 `Any`）。`String` 是更具体的类型，因此只要导入的 `dump(_:)` 可用，编译器就会选择它。

```
dump("🏭💨") // [240, 159, 143, 173, 240, 159, 146, 168]
```

与前一例不同，两个竞争声明之间似乎根本没有歧义。毕竟，开发者有什么理由认为自己的 `dump(_:)` 会与 `dump(_:name:indent:maxDepth:maxItems:)` 混淆？

这就引向最后一个例子，也许是最令人困惑的一个……

### 字符串插值污染

在 Swift 中，除了拼接外，也可以在字符串字面量中用插值组合两个字符串。

```
let name = "Swift"
let greeting = "Hello, \(name)!" // "Hello, Swift!"
```

从 Swift 的第一个版本起，这都成立。但 Swift 5 引入新的 [`ExpressibleByStringInterpolation`](https://nshipster.com/expressiblebystringinterpolation) 协议后，这一行为不再理所当然。

考虑对 `String` 默认插值类型作出的下列扩展：

```
extension DefaultStringInterpolation {
    public mutating func appendInterpolation<T>(_ value: T) where T: StringProtocol {
        self.appendInterpolation(value.uppercased() as TextOutputStreamable)
    }
}
```

`StringProtocol` 除了其他内容外还继承[ `TextOutputStreamable` 与 `CustomStringConvertible` 协议](https://swiftdoc.org/v4.2/protocol/stringprotocol/)，所以比插值 `String` 值时原本会调用的、[`DefaultStringInterpolation` 声明的 `appendInterpolation` 方法](https://github.com/apple/swift/blob/master/stdlib/public/core/StringInterpolation.swift#L63)更具体：

```
public struct DefaultStringInterpolation: StringInterpolationProtocol {
    @inlinable public mutating func appendInterpolation<T>(_ value: T)
        where T: TextOutputStreamable, T: CustomStringConvertible {}
}
```

编译器对“具体性”的判断再次令行为从预期变成意外。

若前面的声明可由 App 中任一模块访问，它就会改变所有字符串插值值的行为。

```
let greeting = "Hello, \(name)!" // "Hello, SWIFT!"
```

---

鉴于这门语言快速上升的发展轨迹，预计这些问题终会在某个时候得到解决并不算不合理。

但在此之前该怎么办？下面分别讨论 API 使用者与提供者可采用的策略。

---

## API 使用者的策略

作为 API 使用者，你在很多方面受制于导入依赖施加的约束。这本来*不该*是你要解决的问题，但至少仍有一些补救办法。

### 给编译器提示

通常，想让编译器做你想做的事，最有效的方法是显式把参数转换为匹配目标方法的类型。

回到前面的 `dump(_:)` 示例：将 `String` 向下转换为 `CustomStringConvertible`，就能让编译器把调用解析为标准库函数。

```
dump("🏭💨") // [240, 159, 143, 173, 240, 159, 146, 168]
dump("🏭💨" as CustomStringConvertible) // "🏭💨"
```

### ~~作用域导入声明~~

### Fork 依赖

如果其他办法都失败了，总可以亲自解决问题。

不喜欢第三方依赖的某种行为，就 fork 源码、删去不想要的部分，再使用那个版本。（也可以尝试促使对方接受上游修改。）

## API 提供者的策略

作为 API 的开发者，审慎周到地做出设计决策最终是你的责任。思考行为的更大后果时，请记住以下事项：

### 更谨慎地使用泛型约束

非限定的 `<T>` 泛型约束等同于 `Any`。若合理，请考虑让约束更具体，以降低与无关声明重叠的概率。

### 将核心功能与便利功能隔离

一般而言，代码应组织为各模块各自承担单一职责。

若合理，请考虑将模块所提供的类型和方法，与为改善内建类型易用性而提供的扩展分开打包。直到能够从模块中挑选所需行为前，若功能可能在下游引发问题，最好的选择是让使用者自行选择是否启用。

### 从一开始就避免冲突

当然，如果一开始就能有意识地避开冲突会很好……但这就涉及[“未知的未知”](https://en.wikipedia.org/wiki/There_are_known_knowns)，现在没有时间谈认识论。

因此，目前只需说：如果你意识到某件事*可能*造成冲突，一个不错的选择是完全避开它。

例如，若担心有人会因改变基础算术运算符的语义而不满，可以选择不同的运算符，如 `.+`：

```
infix operator .+: AdditionPrecedence

extension Array where Element: Numeric {
    static func .+ (lhs: Array, rhs: Array) -> Array {
        return Array(zip(lhs, rhs).map {$0 + $1})
    }
}

oneTwoThree + fourFiveSix // [1, 2, 3, 4, 5, 6]
oneTwoThree .+ fourFiveSix // [5, 7, 9]
```

---

作为开发者，我们或许不太习惯考虑决策的广泛影响。代码无形且没有重量，发布后甚至很容易忘记它的存在。

但在 Swift 中，决策会产生超出即时理解范围的影响，因此作为 API 的守护者，必须审慎地履行责任。
