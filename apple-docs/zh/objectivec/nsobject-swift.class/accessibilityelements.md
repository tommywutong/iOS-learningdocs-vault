---
title: accessibilityElements
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityelements
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityelements.json'
content_hash: 'sha256:f53af275d1c05a99'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityElements

<sub>实例属性</sub>

辅助技术可访问的对象功能数组。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor var accessibilityElements: [Any]? { get set }
```

## 讨论

在 [NSObject](../nsobject-swift.class.md) 子类上设置此属性，用你希望 VoiceOver、Switch Control 和 Voice Control 等辅助技术与之交互的元素补充默认辅助功能元素层次结构。在实现返回的数组中，可以包含用户界面控件、文本、图像，或你希望使其可访问的自定义辅助功能元素。

系统会为你使用系统提供的 UI 构建的视图层次结构添加默认辅助功能元素。但当你需要以系统无法自动提供的方式使自定义视图可访问时，请使用此属性。例如，使用 Core Graphics 渲染的饼图可以将图表的每一片公开为单独的辅助功能元素：

```swift
// 实现自定义 Core Graphics 渲染的饼图。
class PieChartView: UIView {
    var slices: [Slice] = []
    // 创建辅助功能元素。
    func updateAccessibility() {
        isAccessibilityElement = false
        // 遍历图表切片。
        accessibilityElements = slices.map { slice in
            // 为该切片实例化自定义辅助功能元素。
            let element = UIAccessibilityElement(accessibilityContainer: self)
            element.accessibilityLabel = slice.label
            element.accessibilityValue = "\(slice.percentage)%"
            return element
        }
    }
    // 数据变化时刷新。
    func updateData(_ newSlices: [Slice]) {
        slices = newSlices
        updateAccessibility() 
    }
} 
```

这使饼图数据可供辅助技术使用。例如，VoiceOver 可以逐片轻扫图表切片，朗读每一片的标签和百分比值，而不是仅为整个图表提供单一且信息不足的描述。
