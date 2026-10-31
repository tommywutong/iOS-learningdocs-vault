---
title: 'Food Truck：构建 SwiftUI 多平台 App'
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, Xcode 14.3+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/food-truck-building-a-swiftui-multiplatform-app
source_url: 'https://developer.apple.com/documentation/swiftui/food-truck-building-a-swiftui-multiplatform-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/food-truck-building-a-swiftui-multiplatform-app.json'
content_hash: 'sha256:fac0f3ec54689c93'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [App 组织](app-organization.md)

# Food Truck：构建 SwiftUI 多平台 App

<sub>示例代码</sub>

为 Mac、iPad 和 iPhone 创建单一的代码库和 App target。

## 概述

使用 Food Truck 这款 App，餐车经营者可以跟踪订单、了解最受欢迎的菜单单品，并查看目的地的天气。这个示例使用新的 [NavigationSplitView](navigationsplitview.md) 来管理 App 的视图，使用 [Layout](layout.md) 来显示主界面和待处理订单，使用 [Swift Charts](../charts.md) 来显示趋势，并使用 [WeatherService](../weatherkit/weatherservice.md) 来获取天气数据。Food Truck 还实现了实时活动（Live Activities）：通过 [ActivityKit](../activitykit.md) 在锁定屏幕上显示订单准备的剩余时间，并通过 [DynamicIsland](../widgetkit/dynamicisland.md) 在主屏幕上显示。

你可以在 [GitHub](https://github.com/apple/sample-food-truck) 上获取这个示例的源代码。

> [!note] 注意
> 本示例代码项目关联 WWDC22 场次 [110492: State of the Union](https://developer.apple.com/wwdc22/110492/)。

Food Truck 示例项目包含两种类型的 App target：

- 可以使用[个人团队](https://help.apple.com/xcode/mac/11.4/#/dev17411c009)签名构建的简单 App target。这个 App 在模拟器（Simulator）中运行，只需一个标准 Apple ID 即可安装到设备上。它包含 App 内购买和一个小组件扩展，让用户可以把小组件添加到 iOS 主屏幕或 macOS 通知中心。
- 功能完整的 Food Truck All App target。完整 App 可在模拟器中运行，也可在具有 Apple Developer 会员资格的设备上运行。它还支持创建并使用通行密钥（passkey）登录。

### 配置示例代码项目

要在没有 Apple Developer 账户的情况下配置 Food Truck App，请按照以下步骤操作：

1. 在 Food Truck target 的 Signing & Capabilities 面板中，点击 Add Account 并使用你的 Apple ID 登录。
2. 在 Food Truck 和 Widgets target 的团队菜单中选择 Your Name (Personal Team)。
3. 构建并运行你的 App。
4. 在 iOS 和 iPadOS 设备上，前往设置 \> 通用 \> VPN 与设备管理，并信任你的开发者证书。

要配置 Food Truck All App 使其可在你的设备上运行，请按照以下步骤操作：

1. 使用 Xcode 14.3 或更高版本打开这个示例。
2. 选择顶层的 Food Truck 项目。
3. 对于所有 target，在 Signing & Capabilities 面板的 Team 菜单中选择你的团队，以便 Xcode 自动管理你的描述文件。
4. 添加 Associated Domains 功能，并使用 `webcredentials` 服务指定你的域名。有关 `webcredentials` 服务的更多信息，参见[关联域 Entitlement](../bundleresources/entitlements/com.apple.developer.associated-domains.md)。
5. 确保你的域名下的 `.well-known` 目录中存在 `apple-app-site-association`（AASA）文件，并且该文件包含此 App 的 App ID 在 `webcredentials` 服务下的条目。有关 `apple-app-site-association` 文件的更多信息，参见[支持关联域](../xcode/supporting-associated-domains.md)。
6. 在 `AccountManager.swift` 文件中，将所有出现的 `example.com` 替换为你的域名。

> [!note] 注意
> 要使用示例中的天气预报功能，你需要执行额外步骤来配置 WeatherKit（如下方「为 WeatherKit 配置项目」一节所述），否则示例会检测到错误并改用项目中包含的静态数据。

### 创建多平台 App

Food Truck 是一个多平台 App，没有用于在 macOS 或 iOS 上运行的单独 target。相反，只有一个 App target，同时为 macOS、iPadOS 和 iOS 构建。

### 定义默认的导览目的地

这个示例的导览界面由一个带有 `Sidebar` 视图的 [NavigationSplitView](navigationsplitview.md) 和一个 [NavigationStack](navigationstack.md) 组成：

```swift
NavigationSplitView {
    Sidebar(selection: $selection)
} detail: {
    NavigationStack(path: $path) {
        DetailColumn(selection: $selection, model: model)
    }
}
```

App 启动时，示例会把 `TruckView` 作为默认视图呈现。`Panel` 枚举编码了用户可以在边栏中选择的视图，这些视图也会相应地显示在详情视图中。与 `TruckView` 对应的值是 `.truck`，App 将其设为默认选择。

```swift
@State private var selection: Panel? = Panel.truck
```

### 构建动态布局

在 Truck 视图中，New Orders 面板显示最近的五个订单，每个订单显示一个 `DonutStackView`，即甜甜圈缩略图的对角线叠放。通过 [Layout](layout.md) 协议，App 可以定义 `DiagonalDonutStackLayout`，把甜甜圈缩略图排布成对角线布局。该布局的 [placeSubviews(in:proposal:subviews:cache:)](<layout/placesubviews(in_proposal_subviews_cache_).md>) 实现会计算甜甜圈的位置。

```swift
for index in subviews.indices {
    switch (index, subviews.count) {
    case (_, 1):
        subviews[index].place(
            at: center,
            anchor: .center,
            proposal: ProposedViewSize(size)
        )
        
    case (_, 2):
        let direction = index == 0 ? -1.0 : 1.0
        let offsetX = minBound * direction * 0.15
        let offsetY = minBound * direction * 0.20
        subviews[index].place(
            at: CGPoint(x: center.x + offsetX, y: center.y + offsetY),
            anchor: .center,
            proposal: ProposedViewSize(CGSize(width: size.width * 0.7, height: size.height * 0.7))
        )
    case (1, 3):
        subviews[index].place(
            at: center,
            anchor: .center,
            proposal: ProposedViewSize(CGSize(width: size.width * 0.65, height: size.height * 0.65))
        )
        
    case (_, 3):
        let direction = index == 0 ? -1.0 : 1.0
        let offsetX = minBound * direction * 0.15
        let offsetY = minBound * direction * 0.23
        subviews[index].place(
            at: CGPoint(x: center.x + offsetX, y: center.y + offsetY),
            anchor: .center,
            proposal: ProposedViewSize(CGSize(width: size.width * 0.7, height: size.height * 0.65))
        )
```

### 显示热门单品图表

这个示例包含多个图表。最受欢迎的单品显示在 `TopFiveDonutsView` 上。该图表在 `TopDonutSalesChart` 中实现，使用 [BarMark](../charts/barmark.md) 构建条形图。

```swift
Chart {
    ForEach(sortedSales) { sale in
        BarMark(
            x: .value("Donut", sale.donut.name),
            y: .value("Sales", sale.sales)
        )
        .cornerRadius(6, style: .continuous)
        .foregroundStyle(.linearGradient(colors: [Color("BarBottomColor"), .accentColor], startPoint: .bottom, endPoint: .top))
        .annotation(position: .top, alignment: .top) {
            Text(sale.sales.formatted())
                .padding(.vertical, 4)
                .padding(.horizontal, 8)
                .background(.quaternary.opacity(0.5), in: Capsule())
                .background(in: Capsule())
                .font(.caption)
        }
    }
}
```

图表的 _x_ 轴显示的标签包含与每个数据点对应的单品名称和缩略图。

```swift
.chartXAxis {
    AxisMarks { value in
        AxisValueLabel {
            let donut = donutFromAxisValue(for: value)
            VStack {
                DonutView(donut: donut)
                    .frame(height: 35)
                    
                Text(donut.name)
                    .lineLimit(2, reservesSpace: true)
                    .multilineTextAlignment(.center)
            }
            .frame(idealWidth: 80)
            .padding(.horizontal, 4)
            
        }
    }
}
```

### 获取天气预报

App 在 Truck 视图的 Forecast 面板中显示预测温度曲线图。App 从 [WeatherKit](../weatherkit.md) 框架获取这些数据。

```swift
.task(id: city.id) {
    for parkingSpot in city.parkingSpots {
        do {
            let weather = try await WeatherService.shared.weather(for: parkingSpot.location)
            condition = weather.currentWeather.condition
            willRainSoon = weather.minuteForecast?.contains(where: { $0.precipitationChance >= 0.3 })
            cloudCover = weather.currentWeather.cloudCover
            temperature = weather.currentWeather.temperature
            symbolName = weather.currentWeather.symbolName
            
            let attribution = try await WeatherService.shared.attribution
            attributionLink = attribution.legalPageURL
            attributionLogo = colorScheme == .light ? attribution.combinedMarkLightURL : attribution.combinedMarkDarkURL
            
            if willRainSoon == false {
                spot = parkingSpot
                break
            }
        } catch {
            print("Could not gather weather information...", error.localizedDescription)
            condition = .clear
            willRainSoon = false
            cloudCover = 0.15
        }
    }
}
```

### 为 WeatherKit 配置项目

WeatherKit 中 [WeatherService](../weatherkit/weatherservice.md) 实例的数据需要为 Food Truck All target 进行额外配置。如果你不配置 WeatherKit，示例会检测到错误并改用项目中的静态数据。

1. 在 [Provisioning Portal](https://developer.apple.com/account/resources/certificates/list) 上创建一个唯一的 App ID，并在 App Services 标签页中选择 WeatherKit 服务。
2. 在 Xcode 中，对于 Signing & Capabilities 标签页上的 Food Truck All target，把 bundle ID 改成与第 1 步中的 App ID 相同，并添加 WeatherKit 功能。
3. 对于 Signing & Capabilities 标签页上的 Widgets target，修改 bundle ID，使 `.Widgets` 之前的部分与 Food Truck All target 的 bundle ID 相同。
4. 等待 30 分钟，让服务注册你的 App 的 bundle ID。
5. 构建并运行 Food Truck All target。

### 使用实时活动跟踪准备时间

这个 App 让餐车经营者可以跟踪订单准备时间，该时间保证不超过 60 秒。为此，App 在订单详情界面上为 `placed` 状态的订单实现了一个工具栏按钮。轻点这个按钮会把订单状态改为 `preparing`，并创建一个 [Activity](../activitykit/activity.md) 实例来启动实时活动，在 iPhone 锁定屏幕上显示倒计时和订单详情。

```swift
let timerSeconds = 60
let activityAttributes = TruckActivityAttributes(
    orderID: String(order.id.dropFirst(6)),
    order: order.donuts.map(\.id),
    sales: order.sales,
    activityName: "Order preparation activity."
)

let future = Date(timeIntervalSinceNow: Double(timerSeconds))

let initialContentState = TruckActivityAttributes.ContentState(timerRange: Date.now...future)

let activityContent = ActivityContent(state: initialContentState, staleDate: Calendar.current.date(byAdding: .minute, value: 2, to: Date())!)

do {
    let myActivity = try Activity<TruckActivityAttributes>.request(attributes: activityAttributes, content: activityContent,
        pushType: nil)
    print(" Requested MyActivity live activity. ID: \(myActivity.id)")
    postNotification()
} catch let error {
    print("Error requesting live activity: \(error.localizedDescription)")
}
```

这个 App 还实现了 [DynamicIsland](../widgetkit/dynamicisland.md)，在 iPhone 14 Pro 机型的灵动岛（Dynamic Island）上显示与锁定屏幕相同的信息。

```swift
DynamicIsland {
    DynamicIslandExpandedRegion(.leading) {
        ExpandedLeadingView()
    }

    DynamicIslandExpandedRegion(.trailing, priority: 1) {
        ExpandedTrailingView(orderNumber: context.attributes.orderID, timerInterval: context.state.timerRange)
            .dynamicIsland(verticalPlacement: .belowIfTooWide)
    }
} compactLeading: {
    Image("IslandCompactIcon")
        .padding(4)
        .background(.indigo.gradient, in: ContainerRelativeShape())
       
} compactTrailing: {
    Text(timerInterval: context.state.timerRange, countsDown: true)
        .monospacedDigit()
        .foregroundColor(Color("LightIndigo"))
        .frame(width: 40)
} minimal: {
    Image("IslandCompactIcon")
        .padding(4)
        .background(.indigo.gradient, in: ContainerRelativeShape())
}
.contentMargins(.trailing, 32, for: .expanded)
.contentMargins([.leading, .top, .bottom], 6, for: .compactLeading)
.contentMargins(.all, 6, for: .minimal)
.widgetURL(URL(string: "foodtruck://order/\(context.attributes.orderID)"))
```

再次轻点同一个按钮会把状态改为 `complete`，并结束实时活动。这会把实时活动从锁定屏幕和灵动岛中移除。

```swift
Task {
    for activity in Activity<TruckActivityAttributes>.activities {
        // 检查这是否是与该订单相关联的活动。
        if activity.attributes.orderID == String(order.id.dropFirst(6)) {
            await activity.end(nil, dismissalPolicy: .immediate)
        }
    }
}
```

## 另请参阅

### 创建 App

- [Destination Video](../visionos/destination-video.md) — 利用 SwiftUI 在多平台 App 中构建沉浸式媒体体验。
- [Hello World](../visionos/world.md) — 使用窗口、体积和沉浸式空间向人们介绍地球。
- [Backyard Birds：使用 SwiftData 和小组件构建 App](backyard-birds-sample.md) — 创建一个具有持久化数据、可交互小组件和全新 App 内购买体验的 App。
- [Fruta：使用 SwiftUI 构建功能丰富的 App](../appclip/fruta-building-a-feature-rich-app-with-swiftui.md) — 创建共享代码库，构建一个提供小组件和轻 App 的多平台 App。
- [迁移到 SwiftUI 生命周期](migrating-to-the-swiftui-life-cycle.md) — 在 SwiftUI 中使用基于场景（scene）的生命周期，同时保留你现有的代码库。
- [App](app.md) — 一种表示 App 结构和行为的类型。

## 下载

- [FoodTruckBuildingASwiftUIMultiplatformApp.zip](https://docs-assets.developer.apple.com/published/dd9087d16d30/FoodTruckBuildingASwiftUIMultiplatformApp.zip)
