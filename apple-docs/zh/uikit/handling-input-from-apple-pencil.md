---
title: 处理来自 Apple Pencil 的输入
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-input-from-apple-pencil
source_url: 'https://developer.apple.com/documentation/uikit/handling-input-from-apple-pencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-input-from-apple-pencil.json'
content_hash: 'sha256:0b40df3e2193a112'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Apple Pencil 交互](apple-pencil-interactions.md)

# 处理来自 Apple Pencil 的输入

了解如何检测并响应来自 Apple Pencil 的触摸。

## 概述

UIKit 报告来自 Apple Pencil 的触摸的方式，与报告用户手指触摸的方式相同。具体来说，UIKit 会传递一个 [UITouch](uitouch.md) 对象，其中包含触摸在你的 App 中的位置。不过，源自 Apple Pencil 的触摸对象包含额外信息，包括 Apple Pencil 的方位角、高度角，以及在其笔尖记录到的压力大小。

![](../../../attachments/346399f07002dc4ec8bcf9cb91af19b4/media-3004388@2x.png)

<sub>一张插图，说明在屏幕上使用 Apple Pencil 时，方位角（左侧所示）和高度角（右侧所示）是如何确定的。</sub>

由于 Apple Pencil 是一个独立的设备，Apple Pencil 采集高度角、方位角和压力值的时间，与这些值被报告给你的 App 的时间之间存在延迟。因此，UIKit 最初可能会为这些属性提供 _估计_ 值，随后再提供真实值。如果你使用 Apple Pencil 的高度角、方位角或压力信息，就必须显式处理这些估计属性。

> [!note] 注意
> 与 Apple Pencil 配合使用的设备最高可以 240 Hz 的频率报告触摸。由于 UIKit 通常以大约 60 Hz 的频率报告触摸，任何额外的触摸都会被合并成代表最后位置的单次触摸。有关如何获取额外触摸数据的信息，请参阅[使用合并触摸获取高保真输入](getting-high-fidelity-input-with-coalesced-touches.md)。

### 处理估计属性

当 UIKit 只有某个属性值的估计值时，它会在对应 [UITouch](uitouch.md) 对象的 [estimatedPropertiesExpectingUpdates](uitouch/estimatedpropertiesexpectingupdates.md) 属性中包含一个标志。处理触摸事件时，检查该属性，以确定你稍后是否需要更新触摸信息。

当一个触摸对象包含估计属性时，UIKit 还会在 [estimationUpdateIndex](uitouch/estimationupdateindex.md) 属性中提供一个值。使用该值作为键，存入你维护的字典中，以便稍后识别该触摸。将该键对应的值设为你用来存储触摸信息的 App 专属对象。当 UIKit 稍后报告真实值时，使用该索引查找你的 App 专属对象，并用真实值替换估计值。

以下代码展示了某个捕获触摸数据的 App 中的 `addSamples` 方法。对每个触摸，该方法都会创建一个包含触摸信息的自定 `StrokeSample` 对象。如果触摸的压力值只是一个估计值，`registerForEstimates` 方法会以 [estimationUpdateIndex](uitouch/estimationupdateindex.md) 属性中的值作为键，将该样本缓存到字典中。

```swift
var estimates: [NSNumber: StrokeSample]
 
func addSamples(for touches: [UITouch]) {
   if let stroke = strokeCollection?.activeStroke {
      for touch in touches {
         if touch == touches.last {
            let sample = StrokeSample(point: touch.location(in: self), 
                                 forceValue: touch.force)
            stroke.add(sample: sample)
            registerForEstimates(touch: touch, sample: sample)
         } else {
            let sample = StrokeSample(point: touch.location(in: self), 
                                 forceValue: touch.force, coalesced: true)
            stroke.add(sample: sample)
            registerForEstimates(touch: touch, sample: sample)
         }
      }
      self.setNeedsDisplay()
   }
}
 
func registerForEstimates(touch : UITouch, sample : StrokeSample) {
   if touch.estimatedPropertiesExpectingUpdates.contains(.force) {
      estimates[touch.estimationUpdateIndex!] = sample
   }
}
```

当 UIKit 收到某个触摸的实际值时，它会调用你的响应者或手势识别器的 [- touchesEstimatedPropertiesUpdated:](<uiresponder/touchesestimatedpropertiesupdated(__).md>) 方法。使用该方法，将估计数据替换为 UIKit 提供的真实值。

以下代码展示了 [- touchesEstimatedPropertiesUpdated:](<uiresponder/touchesestimatedpropertiesupdated(__).md>) 方法的一个示例，它会更新前面代码示例中创建的缓存 `StrokeSample` 对象的压力值。该方法使用 [estimationUpdateIndex](uitouch/estimationupdateindex.md) 属性中的值，从 `estimates` 字典中获取 `StrokeSample` 对象，然后更新压力值，并将该样本从字典中移除。

```swift
override func touchesEstimatedPropertiesUpdated(_ touches: Set<UITouch>) {
   for touch in touches {
      // If the force value is no longer an estimate, update it.
      if !touch.estimatedPropertiesExpectingUpdates.contains(.force) {
         let index = touch.estimationUpdateIndex!
         var sample = estimates[index]
         sample?.force = touch.force
 
         // Remove the key and value from the dictionary.
         estimates.removeValue(forKey: index)
      }
   }
}
```

## 主题

### 相关文章

- [计算 Apple Pencil 的垂直压力](computing-the-perpendicular-force-of-apple-pencil.md) — 调整 Apple Pencil 报告的压力值，使其与 3D Touch 压力值保持一致。

## 另请参阅

### 基础

- [处理来自 Apple Pencil 的双击](../applepencil/handling-double-taps-from-apple-pencil.md) — 检测并响应用户在 Apple Pencil 上做出的双击。
- [处理来自 Apple Pencil 的捏压](../applepencil/handling-squeezes-from-apple-pencil.md) — 检测并响应用户在 Apple Pencil Pro 上做出的捏压。
