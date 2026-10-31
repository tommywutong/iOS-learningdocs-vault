---
title: 'Backyard Birds：使用 SwiftData 和小组件构建 App'
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, watchOS 10.2+, Xcode 15.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/backyard-birds-sample
source_url: 'https://developer.apple.com/documentation/swiftui/backyard-birds-sample'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/backyard-birds-sample.json'
content_hash: 'sha256:2f41c50e69ae8986'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [App 组织](app-organization.md)

# Backyard Birds：使用 SwiftData 和小组件构建 App

<sub>示例代码</sub>

创建一个具有持久化数据、可交互小组件和全新 App 内购买体验的 App。

## 概述

Backyard Birds 提供了一个丰富的环境，你可以在其中观察造访你后院花园的鸟类。你可以监控它们的水和食物供给，确保它们始终有新鲜的水和充足的食物，或者通过 App 内购买升级游戏，为鸟类提供更美味的食物。

该示例使用 [SwiftData](../swiftdata.md) 实现其数据模型以进行持久化，并借助 [`Observable`](../observation.md) 协议与 SwiftUI 无缝集成。游戏的小组件实现了 [App Intents](../appintents.md) 以支持可交互、可配置的小组件。App 内购买体验使用了 StoreKit 的 [`ProductView`](../storekit/productview.md) 和 [`SubscriptionStoreView`](../storekit/subscriptionstoreview.md)。

你可以在 [GitHub](https://github.com/apple/sample-backyard-birds) 上获取本示例的源代码。

> [!note] 注意
> 本示例代码项目关联 WWDC23 场次 102：[State of the Union](https://developer.apple.com/wwdc23/102/)。

### 配置示例代码项目

要让 Backyard Birds App 在你的设备上运行，请按照以下步骤操作：

1. 在 Xcode 15 或更高版本中打开该项目。
2. 编辑多平台 target 的 scheme，在 Options 标签页中，为 StoreKit 配置选择 `Store.storekit` 文件。
3. 对 watchOS target 的 scheme 重复上一步。
4. 选择顶层的 Backyard Birds 项目。
5. 对于所有 target，在 Signing & Capabilities 面板的 Team 菜单中选择你的团队，以便 Xcode 自动管理你的描述文件。

### 创建数据驱动的 App

该 App 通过使用 [`Model`](<../swiftdata/model().md>) 宏让模型对象遵循 [`PersistentModel`](../swiftdata/persistentmodel.md) 来定义其数据模型。将 [`Attribute`](<../swiftdata/attribute(__originalname_hashmodifier_).md>) 宏与 [`unique`](../swiftdata/schema/attribute/option/unique.md) 选项一起使用可确保 `id` 属性的唯一性。

```swift
@Model public class BirdSpecies {
    @Attribute(.unique) public var id: String
    public var naturalScale: Double
    public var isEarlyAccess: Bool
    public var parts: [BirdPart]
    
    @Relationship(deleteRule: .cascade, inverse: \Bird.species)
    public var birds: [Bird] = []
    
    public var info: BirdSpeciesInfo { BirdSpeciesInfo(rawValue: id) }
    
    public init(info: BirdSpeciesInfo, naturalScale: Double = 1, isEarlyAccess: Bool = false, parts: [BirdPart]) {
        self.id = info.rawValue
        self.naturalScale = naturalScale
        self.isEarlyAccess = isEarlyAccess
        self.parts = parts
    }
}
```

### 构建可交互的小组件

当后院的水和食物即将耗尽时，Backyard Birds 会通过呈现一个 [Button](button.md) 来补充后院的物资，从而显示可交互的小组件。该 App 的做法是在小组件的视图中放置一个 `Button`，并将一个 `ResupplyBackyardIntent` 实例传递给 [`init(intent:label:)`](<button/init(intent_label_).md>) 初始化方法：

```swift
Button(intent: ResupplyBackyardIntent(backyard: BackyardEntity(from: snapshot.backyard))) {
    Label("Refill Water", systemImage: "arrow.clockwise")
        .foregroundStyle(.secondary)
        .frame(maxWidth: .infinity)
        .padding(.vertical, 8)
        .padding(.horizontal, 12)
        .background(.quaternary, in: .containerRelative)
}
```

该 App 通过实现 [`WidgetConfigurationIntent`](../appintents/widgetconfigurationintent.md) 协议来支持小组件的配置：

```swift
struct BackyardWidgetIntent: WidgetConfigurationIntent {
    static let title: LocalizedStringResource = "Backyard"
    static let description = IntentDescription("Keep track of your backyards.")
    
    @Parameter(title: "Backyards", default: BackyardWidgetContent.all)
    var backyards: BackyardWidgetContent
    
    @Parameter(title: "Backyard")
    var specificBackyard: BackyardEntity?
    
    init(backyards: BackyardWidgetContent = .all, specificBackyard: BackyardEntity? = nil) {
        self.backyards = backyards
        self.specificBackyard = specificBackyard
    }
    
    init() {
    }
    
    static var parameterSummary: some ParameterSummary {
        When(\.$backyards, .equalTo, BackyardWidgetContent.specific) {
            Summary {
                \.$backyards
                \.$specificBackyard
            }
        } otherwise: {
            Summary {
                \.$backyards
            }
        }
    }
}
```

### 提供全新的 App 内购买体验

该示例 App 使用 [`ProductView`](../storekit/productview.md) 在商店货架上显示几种可供购买的不同鸟食升级。为了突出展示某个 App 内购买商品，该 App 使用了 [`.productViewStyle(.large)`](<view/productviewstyle(__).md>) 修饰符：

```swift
ProductView(id: product.id) {
    BirdFoodProductIcon(birdFood: birdFood, quantity: product.quantity)
        .bestBirdFoodValueBadge()
}
.padding(.vertical)
.background(.background.secondary, in: .rect(cornerRadius: 20))
.productViewStyle(.large)
```

Backyard Birds Pass 页面使用 [`SubscriptionStoreView`](../storekit/subscriptionstoreview.md) 视图显示可续订的订阅。该 App 使用 `PassMarketingContent` 视图作为 `SubscriptionStoreView` 的内容：

```swift
SubscriptionStoreView(
    groupID: passGroupID,
    visibleRelationships: showPremiumUpgrade ? .upgrade : .all
) {
    PassMarketingContent(showPremiumUpgrade: showPremiumUpgrade)
        #if !os(watchOS)
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
        #endif
}
```

## 另请参阅

### 创建 App

- [Destination Video](../visionos/destination-video.md) — 利用 SwiftUI 在多平台 App 中构建沉浸式媒体体验。
- [Hello World](../visionos/world.md) — 使用窗口、volume 和沉浸式空间向人们介绍地球。
- [Food Truck：构建 SwiftUI 多平台 App](food-truck-building-a-swiftui-multiplatform-app.md) — 为 Mac、iPad 和 iPhone 创建单一的代码库和 App target。
- [Fruta：使用 SwiftUI 构建功能丰富的 App](../appclip/fruta-building-a-feature-rich-app-with-swiftui.md) — 创建共享代码库，构建一个提供小组件和轻 App 的多平台 App。
- [迁移到 SwiftUI 生命周期](migrating-to-the-swiftui-life-cycle.md) — 在保留现有代码库的同时使用 SwiftUI 中基于场景的生命周期。
- [App](app.md) — 表示 App 的结构和行为的类型。

## 下载

- [BackyardBirdsBuildingAnAppWithSwiftDataAndWidgets.zip](https://docs-assets.developer.apple.com/published/7f06a68fb95e/BackyardBirdsBuildingAnAppWithSwiftDataAndWidgets.zip)
