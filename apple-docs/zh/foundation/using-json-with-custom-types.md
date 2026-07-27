---
title: 对自定类型使用 JSON
framework: Foundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [Xcode 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/using-json-with-custom-types
source_url: 'https://developer.apple.com/documentation/foundation/using-json-with-custom-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/using-json-with-custom-types.json'
content_hash: 'sha256:fce4f5311fe26a5c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Archives and Serialization](archives-and-serialization.md)

# 对自定类型使用 JSON

<sub>示例代码</sub>

使用 Swift 对 JSON 的支持，对 JSON 数据进行编码和解码，无论其结构如何。

## 概述

你从其他 App、服务和文件发送或接收的 JSON 数据，可能有多种不同的形态和结构。使用本示例中介绍的技术来处理外部 JSON 数据与你 App 模型类型之间的差异。

![](../../../attachments/bf619429955141ec0a25cf920d77fba3/using-json-with-custom-types-01@2x.png)

<sub>一张分为两个面板的图片，展示了两个相关的数据模型。左侧面板标题为「Your App's Model」，显示一个标为 app 的圆圈连接到一个思考气泡。气泡内，一个名为 Grocery Store 的标签指向一个包含苹果、香蕉和橙子图标的数组。第二个面板标题为「Service API's model」。它同样有一个 Grocery Store 标签，但这个标签指向一个数组，其中每个成员都是一个名为 Aisle 的垂直列表，其中包含多个名为 Shelf 的成员，每个成员都装着不同的水果。虽然 Aisle 1 元素包含的水果与第一个面板中显示的 App 模型相同，但 Aisle 2 包含了该 App 并不知道的其他水果。</sub>

本示例定义了一个简单的数据类型 `GroceryProduct`，并演示了如何从几种不同的 JSON 格式构造该类型的实例。

```swift
struct GroceryProduct: Codable {
    var name: String
    var points: Int
    var description: String?
}
```

该示例是一个 Xcode playground，你可以通过执行 playground 中的代码来与之交互。本文中的每一节都对应 playground 中的一个不同页面。

### 从数组中读取数据

利用 Swift 富有表现力的类型系统，避免手动遍历结构相同的对象集合。这个 playground 使用数组类型作为值，来演示如何处理如下这种结构的 JSON：

```swift
[
    {
        "name": "Banana",
        "points": 200,
        "description": "A banana grown in Ecuador."
    }
]
```

### 更改键名

学习如何将 JSON 键中的数据映射到自定类型的属性上，无论它们的名称是什么。例如，这个 playground 展示了如何将下面 JSON 中的 `"product_name"` 键映射到 `GroceryProduct` 上的 `name` 属性：

```swift
{
    "product_name": "Banana",
    "product_cost": 200,
    "description": "A banana grown in Ecuador."
}
```

自定映射使你能够将 Swift [API Design Guidelines](https://swift.org/documentation/api-design-guidelines/) 应用到 Swift 模型中的属性名称上，即使 JSON 键的名称与之不同。

### 访问嵌套数据

学习如何忽略代码中不需要的 JSON 结构和数据。这个 playground 使用一个中间类型来演示如何从如下所示的 JSON 中提取杂货产品，从而跳过不需要的数据和结构：

```swift
[
    {
        "name": "Home Town Market",
        "aisles": [
            {
                "name": "Produce",
                "shelves": [
                    {
                        "name": "Discount Produce",
                        "product": {
                            "name": "Banana",
                            "points": 200,
                            "description": "A banana that's perfectly ripe."
                        }
                    }
                ]
            }
        ]
    }
]
```

### 合并不同深度的数据

通过为 `Encodable` 和 `Decodable` 的协议要求编写自定实现，合并或分离来自 JSON 结构不同深度的数据。这个 playground 展示了如何从如下所示的 JSON 构造一个 `GroceryProduct` 实例：

```
{
    "Banana": {
        "points": 200,
        "description": "A banana grown in Ecuador."
    }
}
```

## 另请参阅

### JSON

- [JSONEncoder](jsonencoder.md) — 一个将数据类型的实例编码为 JSON 对象的对象。
- [JSONDecoder](jsondecoder.md) — 一个从 JSON 对象解码数据类型实例的对象。
- [JSONSerialization](jsonserialization.md) — 一个在 JSON 与等效 Foundation 对象之间进行转换的对象。

## 下载

- [UsingJSONWithCustomTypes.zip](https://docs-assets.developer.apple.com/published/111eb89d287b/UsingJSONWithCustomTypes.zip)
