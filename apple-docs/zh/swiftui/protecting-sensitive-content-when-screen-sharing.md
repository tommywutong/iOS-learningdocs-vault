---
title: 在屏幕共享和远程控制处于活跃状态时保护敏感内容
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/protecting-sensitive-content-when-screen-sharing
source_url: 'https://developer.apple.com/documentation/swiftui/protecting-sensitive-content-when-screen-sharing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/protecting-sensitive-content-when-screen-sharing.json'
content_hash: 'sha256:7d3713a7c3d83651'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图配置](view-configuration.md)

# 在屏幕共享和远程控制处于活跃状态时保护敏感内容

<sub>文章</sub>

检测活跃的屏幕捕捉会话并作出适当响应，以保护你 App 中的敏感内容。

## 概述

屏幕共享和远程控制功能为人们的协作提供了实用的方式。随着屏幕共享越来越普遍，处理敏感数据的 App——例如银行、支付和医疗健康类 App——应当采取措施，在捕捉会话进行期间保护内容。

iOS 和 iPadOS 提供了一个内置 API，用于检测系统何时捕捉某个场景。请响应这一信号，并在你的 App 中采取主动措施，在任何捕捉会话期间保护敏感内容。

## 检测系统何时捕捉你 App 的内容

当屏幕捕捉会话处于活跃状态时——包括屏幕录制、镜像或远程控制——系统会更新场景的捕捉状态。在 SwiftUI 中使用 [`isSceneCaptured`](environmentvalues/isscenecaptured.md) 环境值，或在 UIKit 中使用 [`UITraitCollection.sceneCaptureState`](../uikit/uitraitcollection/scenecapturestate.md)，来观察这一状态。当状态发生变化时，相应地更新你的 UI——例如，把敏感视图替换为已屏蔽或占位的内容。

**SwiftUI**

```swift
struct AccountView: View {
    @Environment(\.isSceneCaptured) private var isSceneCaptured

    var body: some View {
        if isSceneCaptured {
            // Replace `RedactedContentView` with your redacted or placeholder view.
            RedactedContentView()
        } else {
            // Replace `SensitiveContentView` with your content view.
            SensitiveContentView()
        }
    }
}
```

**UIKit**

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    // Register to observe scene capture state changes.
    registerForTraitChanges([UITraitSceneCaptureState.self]) { (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateContentVisibility()
    }
    // Apply the initial state on load.
    updateContentVisibility()
}

func updateContentVisibility() {
    let isCaptured = traitCollection.sceneCaptureState != .notCaptured
    // Replace `accountNumberLabel` and `balanceLabel` with the sensitive UI elements you want to hide.
    accountNumberLabel.isHidden = isCaptured
    balanceLabel.isHidden = isCaptured
}
```

> [!note] 注意
> `sceneCaptureState` 不区分捕捉类型。屏幕录制、AirPlay 镜像和远程控制都会产生相同的信号。

## 响应捕捉会话

正确的响应取决于你 App 处理的数据的敏感程度，以及这些内容在捕捉会话期间被暴露时对人们可能造成的影响。显示金融账户详情或个人健康信息的 App 可能需要比一般 App 更强的保护。评估对使用你 App 的人们的适当保护级别，以确定当你的 App 检测到捕捉会话时如何响应：

- **告知当事人。** 显示横幅或 App 内通知，让人们知道他们的屏幕正在被共享。
- **隐藏或屏蔽敏感栏位。** 用占位文本或模糊覆盖层替换账号、余额、卡片详情和密码。「密码」App 就使用类似的模式来保护敏感内容不被截屏。
- **停用高风险操作。** 在捕捉处于活跃状态时，防止资金转账、密码显示或其他不可逆操作完成。

## 在保护与易用性之间取得平衡

[`UITraitCollection.sceneCaptureState`](../uikit/uitraitcollection/scenecapturestate.md) 会针对所有捕捉事件激活，包括录制教程或镜像到个人 Apple TV 这类日常使用。在决定如何响应时，请记住以下考虑因素：

- **有选择地应用保护。** 针对 App 中风险最高的区域，而不是大范围封锁功能。一刀切的 App 级锁定可能会让有正当屏幕共享需求的人们感到沮丧。
- **使用中性的措辞。** 避免使用暗示当事人正遭受攻击的文案。一条平静且信息明确的通知——例如「屏幕共享正在进行。本次会话期间部分内容受到保护。」——不那么令人惊慌，也更有效。
- **为你的受众权衡取舍。** 安全要求更严格的银行类 App 可能比一般 App 有理由采取更严格的限制行为。根据你 App 的具体风险状况设计你的响应。

## 另请参阅

### 屏蔽私密内容

- [针对全天候显示状态设计你的 App](../watchos-apps/designing-your-app-for-the-always-on-state.md) — 为持续显示定制你 watchOS App 的用户界面。
- [privacySensitive(_:)](<view/privacysensitive(__).md>) — 将视图标记为包含敏感的私密用户数据。
- [redacted(reason:)](<view/redacted(reason_).md>) — 添加一个对此视图层级结构应用屏蔽的理由。
- [unredacted()](<view/unredacted().md>) — 移除对此视图层级结构应用屏蔽的任何理由。
- [redactionReasons](environmentvalues/redactionreasons.md) — 当前应用到视图层级结构的屏蔽理由。
- [isSceneCaptured](environmentvalues/isscenecaptured.md) — 当前的捕捉状态。
- [RedactionReasons](redactionreasons.md) — 对屏幕上显示的数据应用屏蔽的理由。
