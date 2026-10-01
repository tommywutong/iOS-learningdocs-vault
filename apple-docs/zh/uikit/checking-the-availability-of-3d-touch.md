---
title: 检查 3D Touch 的可用性
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/checking-the-availability-of-3d-touch
source_url: 'https://developer.apple.com/documentation/uikit/checking-the-availability-of-3d-touch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/checking-the-availability-of-3d-touch.json'
content_hash: 'sha256:834e850c132849de'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [触摸、按压和手势](touches-presses-and-gestures.md) · [跟踪 3D Touch 事件的力度](tracking-the-force-of-3d-touch-events.md)

# 检查 3D Touch 的可用性

<sub>文章</sub>

在启用使用 3D Touch 的功能之前，先检查设备是否支持它。

## 概述

要判断设备上是否可用 3D Touch，检查任何遵循 [UITraitEnvironment](uitraitenvironment.md) 协议的对象——例如你的 App 的视图和视图控制器——的 [forceTouchCapability](uitraitcollection/forcetouchcapability.md) 属性。下面的代码展示了如何在加载时用这个属性从你的视图控制器启用或禁用功能。使用 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 方法检测你的 App 运行期间 3D Touch 可用性的变化。

```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
 
        // 检查特性集合，看力度是否可用。
        if self.traitCollection.forceTouchCapability == .available {
            // 启用 3D Touch 功能
        } else {
            // 回退到其他非 3D Touch 功能。
        }
    }
 
    override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
        // 更新 App 的 3D Touch 支持。
        if self.traitCollection.forceTouchCapability == .available {
            // 启用 3D Touch 功能
        } else {
            // 回退到其他非 3D Touch 功能。
        }
    }
}
```

关于如何在有和无 3D Touch 支持两种情况下实现你的 App，参见 [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/)。
