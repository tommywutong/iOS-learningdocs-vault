---
title: 'validateValue(_:forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/validatevalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:839a557d09b024f7'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validateValue(_:forKey:)

<sub>实例方法</sub>

指示由给定指针指定的值对于由给定键标识的属性是否有效，或能否变为有效。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws
```

## 参数

- `ioValue` — 指向由 `inKey` 标识的属性的新值的指针。此方法可以修改或替换该值以使其有效。

- `inKey` — 接收者某个属性的名称。该键必须指定属性或一对一关系。

## 讨论

在 Swift 中，若值无效，此方法会抛出错误。在 Objective-C 中，它返回布尔值。

此函数的默认实现会在接收者的类中搜索具有特定签名的特定于属性的验证函数，从而允许该函数决定验证结果。要被找到，特定于属性的验证函数必须向 Objective-C 公开，必须按模式 `validate<InKey>` 命名，必须接受单个可选的 `AnyObject` 指针参数，并且必须抛出。例如，对于名为 `someString` 的属性，验证函数为：

```swift
@objc func validateSomeString(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws {
    // Test, and possibly replace the value here; or throw an error
}
```

若你定义了此类函数，则当被要求验证相应属性时，[- validateValue:forKey:error:](<validatevalue(__forkey_).md>) 的默认实现会调用它，从而允许你的函数更改输入值或抛出错误。

若某个属性不存在此类函数，[- validateValue:forKey:error:](<validatevalue(__forkey_).md>) 会返回 [YES](../yes.md) 而不采取任何其他操作。换句话说，默认情况下，若你未为给定属性显式提供验证函数，则一般验证调用会成功。

> [!note] 注意
> 此处描述的验证通常仅在 Objective-C 中使用。在 Swift 中，属性验证更惯用地通过依赖编译器对可选值和强类型检查的支持来处理，同时使用内置的 `willSet` 和 `didSet` 属性观察器来测试任何运行时 API 约定，如 [The Swift Programming Language (Swift 4.1)](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/index.html#//apple_ref/doc/uid/TP40014097) 的 [Property Observers](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/Properties.html#//apple_ref/doc/uid/TP40014097-CH14-ID262) 部分所述。

有关更多信息，请参阅 [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i) 中的 [Adding Validation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Validation.html#//apple_ref/doc/uid/20002173)。

## 另请参阅

### 验证

- [- validateValue:forKeyPath:error:](<validatevalue(__forkeypath_).md>) — 指示由给定指针指定的值相对于接收者、对于给定键路径是否无效。
