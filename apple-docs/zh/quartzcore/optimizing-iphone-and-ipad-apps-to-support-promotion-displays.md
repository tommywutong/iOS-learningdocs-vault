---
title: 优化 iPhone 和 iPad App 以支持 ProMotion 显示屏
framework: Core Animation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays
source_url: 'https://developer.apple.com/documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.json'
content_hash: 'sha256:cb03faa063bd8357'
translated: true
---

> 导航：[技术](../technologies.md) · [Core Animation](../quartzcore.md)

# 优化 iPhone 和 iPad App 以支持 ProMotion 显示屏

<sub>文章</sub>

通过请求首选刷新率并将动画与系统同步，改善 App 的视觉外观并节省电量。

## 概述

ProMotion 显示屏能够动态切换帧率，范围从 iPad Pro 上的 24Hz 到 120Hz，以及受支持的 iPhone 设备上的 10Hz 到 120Hz。你的 App 可以呈现流畅无缝的动画，并利用 ProMotion 显示屏中的省电机会。配备 ProMotion 显示屏的设备包括：

| iPhone | iPad |
|---|---|
| iPhone Air | iPad Pro 11 英寸 |
| iPhone 17 及后续机型 | iPad Pro 13 英寸 |
| iPhone 13 Pro 及后续机型 | iPad Pro 12.9 英寸（第 2 代及后续机型） |
| iPhone 13 Pro Max 及后续机型 | iPad Pro 10.5 英寸 |

你的 App 可能无需任何更改即可利用这些新的刷新率。某些框架的动画功能会自动为你处理帧节奏，包括：

- [UIKit](../uikit.md)
- [SwiftUI](../swiftui.md)
- [CAAnimation](caanimation.md)
- [SpriteKit](../spritekit.md)

如果你的 App 需要提供具有特殊时机的动画内容，你可以使用 [CADisplayLink](cadisplaylink.md) 来将你的绘制代码与显示屏刷新同步。在以下代码示例中，`DisplayLinkManager` 类通过创建并激活一个 display link 来处理帧更新：

```swift
class DisplayLinkManager {
    var displayLink: CADisplayLink?
    
    // 在回调函数中执行你的自定义动画。
    @objc func displayLinkCallback(sender: CADisplayLink) {
        //...
    }
    
    func createDisplayLink() {
        // 创建 display link。
        displayLink = CADisplayLink(target: self, selector: #selector(displayLinkCallback))

        // 你可以在激活前配置 display link。

        // 通过将其添加到主 runloop 中来激活你的 display link。
        displayLink.add(to: .current, forMode: .default)
    }
}
```

你可以为任何需要特殊时机以改善视觉外观或节省电量的 `CAAnimation` 动画提供时机提示。有关刷新率的更多信息，请观看 WWDC21 [Session 10147：为可变刷新率显示屏优化](https://developer.apple.com/videos/play/wwdc2021/10147/)。

## 了解刷新率

ProMotion 显示屏的行为与传统显示屏不同。系统将 ProMotion 显示屏的实际刷新率与你的 App 隔离——你无法强制 ProMotion 显示屏以任何特定速率显示你的内容。

从你的 App 的角度来看，ProMotion 显示屏的刷新率是 Core Animation 为整个显示屏渲染内容的速率。系统将渲染过程与显示硬件的刷新率同步，但显示硬件不一定会驱动渲染过程。

Core Animation 仲裁其在屏幕上呈现的动画，并确定任何特定时间的刷新率。你的 App 可以向 Core Animation 提供关于其动画首选的刷新率的提示。通过尽可能使用较低的刷新率来利用省电机会。较高的刷新率可能会导致显著的电力消耗。

配备 ProMotion 显示屏的设备可以使用以下刷新率和计时来呈现内容：

| 刷新率与计时 | iPhone | iPad Pro |
|---|---|---|
| 120Hz (8ms) | ✅ | ✅ |
| 80Hz (12ms) | ✅ |  |
| 60Hz (16ms) | ✅ | ✅ |
| 48Hz (20ms) | ✅ |  |
| 40Hz (25ms) | ✅ | ✅ |
| 30Hz (33ms) | ✅ | ✅ |
| 24Hz (41ms) | ✅ | ✅ |
| 20Hz (50ms) | ✅ |  |
| 16Hz (62ms) | ✅ |  |
| 15Hz (66ms) | ✅ |  |
| 12Hz (83ms) | ✅ |  |
| 10Hz (100ms) | ✅ |  |

显示屏刷新率可能因多种原因而改变，你的 App 在任何时候都不能假定特定的刷新率。

你的 App 中的自定义动画需要适应刷新率的变化。例如，在低电量模式或设备过热时，系统会禁用较快的刷新率。此外，当 UIKit 和 Core Animation 管理各种 GUI 元素时，Core Animation 可能会选择改变刷新率以提供增强的用户体验。

## 启用更快的 ProMotion 刷新率

除非你解锁完整的帧率范围，否则设备不会应用你的首选刷新率。具体来说，Core Animation 不会应用任何快于系统默认值的刷新率。要在你的 iPhone App 中为 [CADisplayLink](cadisplaylink.md) 回调和 [CAAnimation](caanimation.md) 动画启用你的 [preferredFrameRateRange](cadisplaylink/preferredframeraterange.md) 时机提示，请使用 Xcode 的 Info 面板将 `CADisableMinimumFrameDurationOnPhone` 键添加到你的 App 的信息属性列表（Info.plist）中，并设置布尔值为 `true`：

```plist
<key>CADisableMinimumFrameDurationOnPhone</key><true/>
```

如果你未启用此支持，Core Animation 将不会访问更高的帧率（高于 60Hz）。在这些情况下，其他动画或 GUI 操作可能会影响 Core Animation 调用你的 `CADisplayLink` 回调的速率。iPad Pro 不需要此特殊配置。

## 向 ProMotion 显示屏提供按时间驱动的内容

系统会自动为你处理 UIKit、SpriteKit、SwiftUI 和 [CAAnimation](caanimation.md) 动画的帧节奏。当你的 App 需要准确地呈现自定义内容时，向 [CADisplayLink](cadisplaylink.md) 或 `CAAnimation` 提供关于 App 首选刷新率的提示。

> [!important] 重要
> 请让你的 App 准备好以任何刷新率运行，而不仅仅是它通过 `CADisplayLink` 或 `CAAnimation` 请求的那些。

在指定首选帧率时，请为你的内容指定最佳的可行帧率。`CADisplayLink` 可能无法始终以该速率更新显示屏，但根据可用硬件和设备的当前状况，它会尝试提供尽可能接近的刷新率。

在 iOS 15 及更高版本中，系统为游戏提供 30Hz 和 60Hz 刷新率的特殊优先级，以确保最佳性能。要访问此特殊优先级，你的游戏需要使用 [CAFrameRateRange](caframeraterange.md) 结构设置 [preferredFrameRateRange](cadisplaylink/preferredframeraterange.md)，并且使用这些值中的一个或两个，如下所示：

```swift
// 30Hz 和 60Hz 刷新率会被赋予特殊优先级
let prioritizedFrameRateRange = CAFrameRateRange(minimum: 30,
                                                maximum: 60,
                                                preferred: 60)
displayLink.preferredFrameRateRange = prioritizedFrameRateRange
```

通过将 App 中 display link 的数量限制为达成目标所需的最小数量，来高效使用系统资源。将具有相似时机的动画分组到同一个 `CADisplayLink` 中，即使它们位于不同的视图中。

> [!important] 重要
> 不要使用定时器或其他未能与 Core Animation 显示屏刷新周期正确对齐的策略。

## 向 Core Animation 提供时机提示

使用 [CADisplayLink](cadisplaylink.md) 和 [CAAnimation](caanimation.md) API 的 App 可以提供关于它们首选刷新率的提示，而 Core Animation 会尝试满足这些偏好。你的 App 不能假定 Core Animation 会以任何特定的刷新率、甚至以请求的速率来调用你的 `CADisplayLink` 回调。

在 iOS 14 及更早版本中，你通过设置 [preferredFramesPerSecond](cadisplaylink/preferredframespersecond.md) 属性来提供首选刷新率。

```swift
func createDisplayLink() {
    // 创建 display link。
    displayLink = CADisplayLink(target: self, selector: #selector(displayLinkCallback))
    
    // 在 iOS 14 及更早版本中，通过设置 `preferredFramesPerSecond` 属性
    // 来配置你想要的刷新率。
    displayLink?.preferredFramesPerSecond = 30
    
    // 通过将 `CADisplayLink` 添加到主 runloop 中来激活它。
    displayLink?.add(to: .current, forMode: .default)
}
```

在 iOS 15 及更高版本中，你通过添加 [CAFrameRateRange](caframeraterange.md) 结构并设置 App 的 [minimum](caframeraterange/minimum.md)、[maximum](caframeraterange/maximum.md) 和 [preferred](caframeraterange/preferred-7l3ki.md) 刷新率来设置 [preferredFrameRateRange](cadisplaylink/preferredframeraterange.md)，如下所示：

```swift
func createDisplayLink() {
    // 创建 display link。
    displayLink = CADisplayLink(target: self, selector: #selector(displayLinkCallback))

    // 在 iOS 15 及更高版本中，使用 `preferredFrameRateRange` 来配置
    // 你想要的刷新率。
    displayLink?.preferredFrameRateRange = CAFrameRateRange(minimum: 10,
                                                            maximum: 60,
                                                            preferred: 30)
    
    // 通过将 `CADisplayLink` 添加到主 runloop 中来激活它。
    displayLink?.add(to: .current, forMode: .default)
}
```

下表提供了针对不同类型动画的一些建议帧率提示：

| 动画类型 | iOS 中的示例 | 帧率范围 | 备注 |
|---|---|---|---|
| 高冲击力动画 | 点击网格中的项目以展开至全屏，例如在“照片”App 中；第一人称、全动态游戏体验；或表单（sheet）呈现 | `CAFrameRateRange(minimum:80, maximum:120, preferred:120)` | 谨慎使用以最小化电量消耗 |
| Alpha 或颜色过渡；小幅度移动 | 开关或控制改变状态；进度指示器；模糊背景 | [CAFrameRateRange](caframeraterange.md).[CAFrameRateRangeDefault](caframeraterange/default.md) | 不需要更高的帧率来实现相同的视觉效果 |
| 小幅度、低速动画 | 时钟滴答；进度条 | `CAFrameRateRange(minimum:8, maximum:15, preferred:0),`  ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `CAFrameRateRange(minimum:15, maximum:24, preferred:0),`, 或  ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `CAFrameRateRange(minimum:30, maximum:48, preferred:0)` | 低速下看起来不错；有省电机会 |
| 所有其他情况 |  | [CAFrameRateRange](caframeraterange.md).[CAFrameRateRangeDefault](caframeraterange/default.md) |  |

为了获得流畅的外观，快速移动并穿过屏幕的对象受益于更高的刷新率。而较小的移动——例如原地旋转的图标——在较低的速率下可能看起来也不错。为了节省电量，请选择能够实现你期望视觉流的最低帧率。

> [!note] 注意
> 在请求最大帧率时要有选择性。如果你的动画请求 120Hz 但无法跟上，它可能渲染不佳。但同样的动画可能能够在较低的速率下保持稳定的节奏。

在设计和构建你的 App 时，请使用这些推荐的计时和原则，但也请在真实设备上进行你自己的测试，以确保你的动画看起来不错。

## 将你的内容与显示屏同步

每次 Core Animation 调用你的 App 的 [CADisplayLink](cadisplaylink.md) 回调时，它会在 [timestamp](cadisplaylink/timestamp.md) 和 [targetTimestamp](cadisplaylink/targettimestamp.md) 属性中报告当前刷新间隔的时机信息。当 Core Animation 调用你的 `CADisplayLink` 回调时，`timestamp` 等于当前刷新间隔的开始，而 `targetTimestamp` 等于该间隔的结束。在提供新内容时，`targetTimestamp` 是你为 Core Animation 渲染到设备显示屏的下一帧提交更改的截止时间。

> [!important] 重要
> 始终使用 `targetTimestamp` 来驱动你的 `CADisplayLink` 回调中提供的任何动画、物理或其他时间相关内容。

虽然 `timestamp` 反映了当前刷新间隔开始的时间，但该时间与 Core Animation 调用你的 `CADisplayLink` 回调的时间之间可能存在一些延迟。要计算你的 `CADisplayLink` 回调在 `targetTimestamp` 之前有多少时间来准备内容，请从 `targetTimestamp` 中减去 [CACurrentMediaTime](<cacurrentmediatime().md>) 返回的值。此 `CADisplayLink` 回调示例计算了为下一帧准备更新的可用时间：

```swift
// 计算可供 `CADisplayLink` 回调使用的工作时间。
@objc func displayLinkCallback(sender: CADisplayLink) {
    // 在这一时刻，有 `workingTime` 秒的时间可供生成
    // 下一帧的内容，以便 Core Animation 将其
    // 渲染到显示屏上。
    let workingTime = sender.targetTimestamp - CACurrentMediaTime()
    //...
}
```

> [!important] 重要
> 长时间的回调执行可能会阻止刷新间隔接收 `CADisplayLink` 回调。

如果 `CADisplayLink` 回调的完成时间超过了 `targetTimestamp`，则下一个刷新间隔不会收到回调。下次 Core Animation 调用你的 `CADisplayLink` 回调时，请为此情况提供恢复处理，以确保你的内容与显示屏正确同步。

> [!tip] 提示
> 使用 [presentsWithTransaction](cametallayer/presentswithtransaction.md) 来将你的动画与其他 Core Animation 或 UIKit 动画同步。

## 测试和验证显示屏性能

为了改善你的 App 与显示屏的同步，请在不同的系统条件下测试帧率变化。对提供给 [CADisplayLink](cadisplaylink.md) 的帧率提示所做的任何更改都将在下一次 `CADisplayLink` 回调中生效。

利用 API 的这一功能来测试你的 App 如何响应刷新率的即时变化。在你的 App 运行时，通过将 [preferredFrameRateRange](cadisplaylink/preferredframeraterange.md) 方法的 `maximum`、`minimum` 和 `preferred` 属性设置为相同的值，来提供不同的帧率提示。

为不同的刷新条件创建 `CADisplayLink` 回调测试，例如：

- 确保 `CADisplayLink` 回调在 ProMotion 显示屏允许的所有刷新率下都能正确运行。
- 验证 `CADisplayLink` 回调能够处理渐进的帧率变化以及突然的变化。
- 确保你的 `CADisplayLink` 回调不会使设备反复进出热状态模式，并因此导致由于热条件而发生的帧率变化。当设备过热时，系统可能会通过降低帧率来应对。

> [!important] 重要
> 你可以通过保持一致的绘制质量来避免不理想的功耗状况。在你的 `CADisplayLink` 回调中根据刷新率动态调整渲染质量可能会限制 GPU。为了避免振荡的反馈循环，请为不同的帧率使用不同的代码路径，并在真实设备上进行测试。
