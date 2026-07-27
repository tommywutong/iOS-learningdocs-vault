---
title: 配置多平台 App
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-a-multiplatform-app-target
source_url: 'https://developer.apple.com/documentation/xcode/configuring-a-multiplatform-app-target'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-a-multiplatform-app-target.json'
content_hash: 'sha256:444c2fbb73bd3d45'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 配置多平台 App

<sub>文章</sub>

在单个 App target 中跨平台共享项目设置和代码。

## 概述

多平台 App 可将 App 体验扩展到你支持的每一个其他平台。你可以使用单个多平台 target，跨平台共享 App 的项目设置和代码。

在 Xcode 中，_App target_ 指定 App 的套装标识符和显示名称等项目设置信息，以及哪些源代码文件属于该 App。默认情况下，共用多平台 target 的 App 会共享项目设置，因此你只需设置一次。你可以根据各个平台的需要调整项目设置。

要创建包含多平台 target 的新项目，请在从模板创建项目时选择 Multiplatform 作为平台。有关更多信息，请参阅[为 App 创建 Xcode 项目](creating-an-xcode-project-for-an-app.md)。

在开发多平台 App 或将现有 target 合并为多平台 target 时，请检查 App，以确定构建配置、框架可用性和 API 可用性方面的差异。

> [!note] 注意
> iOS、iPadOS、macOS、tvOS 和 visionOS App 可以共用单个 target。watchOS App 仍使用独立的 target。

### 评估 App 共享的项目设置和代码

如果你想将现有 App 引入新平台，请考虑你在已支持平台上使用的技术，以及计划为其构建 App 的其他平台。如果计划使用的技术和项目设置有大量重叠，多平台 App target 会很合适。否则，请为每个平台使用独立 target。例如，如果现有 App 使用 SwiftUI，并且你计划在新平台上也使用 SwiftUI，请使用一个多平台 target。不过，如果现有 App 使用 UIKit，而你希望在 Mac 上使用 AppKit，请使用独立 target。

如果你的 App 已支持多个平台，并且多个 target 共享大量代码和配置，请考虑将它们合并为单个 target。尤其是使用 SwiftUI 开发 App 时，你的 App target 很可能已经共享了许多相同的代码和配置。你可以使用单个 `App` 结构体为每个平台定义 SwiftUI App 生命周期。

如果你的 App 支持多个平台，而特定于平台的 target 并不共享太多代码或配置，可以继续使用独立 target。

### 配置 target 支持的目的位置

要向 target 添加目的位置，请点按 Supported Destinations 下方的添加按钮（+），然后从弹出式菜单中选择目的位置。根据 App 已支持的平台，添加按钮会显示一组不同的、可添加到当前 target 的目的位置。要从 target 中移除目的位置，请选择该目的位置，然后点按移除按钮（-）。

![](../../../attachments/0d669eb4746a6ac4ad515384d4e81620/configuring-a-multiplatform-app-target-1@2x.png)

<sub>Xcode target 编辑器区域的截图。在 General Settings 下，Supported Destinations 列表显示 iPhone 和 iPad，后面是一个加号按钮。</sub>

如果要向 target 添加 Mac 或 Apple Vision 目的位置，请从 Mac 或 Apple Vision 菜单中选择与你希望提供的体验相匹配的目的位置类型：

- ****Mac**** — 如果要创建新的 Mac App，请选择此选项。你可以使用由 AppKit 和 SwiftUI 支持的 macOS SDK 中的所有功能和 API。此选项是多平台 App 的默认选项。
- ****Mac Catalyst**** — 如果要将现有 iPad App 引入 Mac，请选择此选项。系统会针对 Mac 调整 App 中标准 UIKit 界面元素的外观。你可能需要更改 App 布局以采纳 Mac Catalyst。
- ****Apple Vision**** — 如果要为 Apple Vision Pro 创建新 App 或修改现有 App，请选择此选项。你可以使用由 RealityKit 和 SwiftUI 支持的 visionOS SDK 中的所有功能和 API。此选项是多平台 App 的默认选项。
- ****Designed for iPad**** — 选择此选项，可在配备 Apple 芯片的 Mac 或 Apple Vision Pro 上运行未经修改的 iPad App。App 在 Apple 芯片或 Apple Vision Pro 上运行时，标准 UIKit 界面元素会保持原有外观。此选项是 iPad App 的默认 Mac 或 Apple Vision 目的位置类型。

### 自定项目设置

添加多个平台后，你可以针对所支持的一个或多个平台自定项目设置和构建配置。可以按平台或构建配置为构建设置添加条件。

例如，将“Mobile”附加到 iOS 构建的显示名称。在项目编辑器中选择项目，然后点按 Build Settings 标签页。在构建设置编辑器的右上角，在过滤字段中输入 `display` 以快速找到 [CFBundleDisplayName](../bundleresources/information-property-list/cfbundledisplayname.md) 键。在该键下方、要改变的构建配置旁边（例如默认的 Debug 或 Release 配置），点按添加按钮（+）。然后从 Any SDK 弹出式菜单中选择 iOS 平台，并在右侧输入替代显示名称。

![Xcode 的截图，其中显示用于配置 App 显示名称的弹出窗口。](../../../attachments/dafd865f17cea40573b1abcc766ac292/configuring-a-multiplatform-app-target-2@2x.png)

同样，你也可以改变构建配置的其他键，例如将“Beta”附加到 beta 构建的显示名称。

有关更改 target 和平台构建设置的更多信息，请参阅[配置 target 的构建设置](configuring-the-build-settings-of-a-target.md)。要添加构建配置，请参阅[向项目添加构建配置文件](adding-a-build-configuration-file-to-your-project.md)。

### 通过添加条件语句解决构建问题

添加其他平台也可能暴露 App 中的构建时问题。要解决这些问题，请在使用平台特有 API 或框架的代码周围插入条件语句。例如，在 iOS 和 iPadOS 中包含 AR 体验的 App 很可能包含使用 ARKit 的代码。ARKit 在 macOS 或 tvOS 中不可用，因此你需要分离使用平台特有 API 或框架的代码。

构建项目时，Xcode 会识别这类构建时问题。要尝试在新平台上构建，请在方案菜单中选择与你所添加平台对应的新运行目的位置。如果 Xcode 发现任何问题，请逐一导览到这些问题，并使用以下步骤加以解决。

**处理不可用的框架。** 如果某个框架在一个平台上不可用，请使用 `canImport` 条件语句包围相应的 import：

```swift
#if canImport(ARKit)
import ARKit
#endif
```

**处理不可用的 API。** 跨多个平台可用的框架中，可能有类型、方法或枚举 case 等个别符号仅限一部分平台使用。要解决这些可用性问题，请使用 `#if os` 平台编译条件语句包围相关代码：

```swift
Toggle(isOn: $isOn) {
    Text("Show Holidays calendar")
}
#if os(macOS)
.toggleStyle(.checkbox)
#endif
```

如果整个文件都特定于某个平台，可以将其从不适用的平台中完全移除。在项目编辑器中选择 target，然后点按 Build Phases 标签页。在源文件行的 Compile Sources 下，取消选中 Any Supported Platform，并从 Filters 列的弹出式菜单中选择相应平台。

![](../../../attachments/f893fe28f346ef28ea79174c0a5623c7/configuring-a-multiplatform-app-target-3@2x.png)

<sub>Xcode 的截图，其中显示源文件的平台选择弹出窗口。当前选择包含两个平台，并提供用于包括或排除 iOS 或 macOS 的复选框。</sub>

### 针对各平台自定 App 体验

添加平台特有的视图和功能，确保 App 的用户界面和体验符合每个平台的需要。例如，有些 Mac App 包含一个菜单栏附加项，即使该 App 不是最前方的 App，该附加项也会显示。以下代码仅在场景（scene）的 macOS 版本中添加 `MenuBarExtra` 实例：

```swift
var body: some Scene {
    WindowGroup {
        PrimaryView()
    }
    #if os(macOS)
    MenuBarExtra("Inspect", systemImage: "eyedropper") {
        VStack {
            Button("Action One") {
                // ...
            }
            Button("Action Two") {
                // ...
            }
        }
    }
    #endif
}
```

有关设计指导，请参阅[人机界面指南](https://developer.apple.com/design/human-interface-guidelines/)。

## 另请参阅

### 基础

- [在项目中配置新 target](configuring-a-new-target-in-your-project.md) — 配置项目以构建新产品，并添加该产品所需的代码和资源。
