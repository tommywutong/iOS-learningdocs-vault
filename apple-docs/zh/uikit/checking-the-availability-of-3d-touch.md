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

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md) · [Tracking the force of 3D Touch events](tracking-the-force-of-3d-touch-events.md)

# 检查 3D Touch 的可用性

<sub>文章</sub>

在启用使用 3D Touch 的功能之前，检查设备是否支持 3D Touch。

## 概述

要确定设备是否支持 3D Touch，请检查任何采用 [UITraitEnvironment](uitraitenvironment.md) 协议的对象（例如 App 的视图和视图控制器）的 [forceTouchCapability](uitraitcollection/forcetouchcapability.md) 属性。以下代码展示了如何从视图控制器在加载时使用该属性来启用或禁用功能。使用 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 方法在 App 运行期间检测 3D Touch 可用性的更改。

```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
 
        // 检查特性集合以查看力度是否可用。
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

有关如何同时支持和不支持 3D Touch 来实现 App 的指南，请参阅 [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/)。
