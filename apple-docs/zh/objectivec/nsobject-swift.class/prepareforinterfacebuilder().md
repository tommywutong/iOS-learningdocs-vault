---
title: prepareForInterfaceBuilder()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/prepareforinterfacebuilder()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/prepareforinterfacebuilder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/prepareforinterfacebuilder%28%29.json'
content_hash: 'sha256:600b4887efdad6fb'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# prepareForInterfaceBuilder()

<sub>实例方法</sub>

在 Interface Builder 中创建可设计对象时调用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func prepareForInterfaceBuilder()
```

## 讨论

当 Interface Builder 实例化带有 `IB_DESIGNABLE` 特性的类时，会调用此方法，告知所生成对象它是在设计时创建的。你可以在可设计类中实现此方法，并用它配置设计时外观。例如，你可以用该方法为自定义文本控件配置默认字符串。系统不会调用此方法；只有 Interface Builder 会调用它。

Interface Builder 会等到图中的所有对象都已创建并初始化后才调用此方法。因此，如果你的对象的运行时配置依赖于子视图或父视图，这些对象在调用此方法时应已存在。

此方法的实现必须在某处调用 `super`，以便父类可以执行自己的自定义设置。
