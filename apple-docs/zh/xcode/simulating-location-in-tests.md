---
title: 在测试中模拟位置
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/simulating-location-in-tests
source_url: 'https://developer.apple.com/documentation/xcode/simulating-location-in-tests'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/simulating-location-in-tests.json'
content_hash: 'sha256:a200ebaac965edda'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Testing](testing.md)

# 在测试中模拟位置

<sub>文章</sub>

在处理与位置相关的代码时，提升测试的可靠性和覆盖率。

## 概述

当你能够控制被测代码的所有输入时，自动化测试最为可靠。测试与位置 API 打交道的代码时，请为坐标和位置使用具体的值，这样测试结果就不会取决于运行测试的设备的实际所在位置。

用不同的模拟位置测试你的代码，以提高位置处理代码的测试覆盖率。

### 模拟静态设备位置

如果你的 App 使用 [Core Location](../corelocation.md) 或 [MapKit](../mapkit.md)，被测 App 的行为可能会取决于设备的位置。请将你的测试计划配置为模拟一个预定的位置，以便测试能以可重复的输入运行。要在测试计划中设置模拟位置，请按下面的步骤操作：

1. 打开 Xcode。
2. 依次选择 Product \> Test Plan \> Edit Test Plan。
3. 在测试计划编辑器面板中，选择 Configuration。
4. 在 Localization 下，点击 Simulated Location，并从菜单中选择一个位置。

有关配置测试计划的更多信息，请参阅[通过将测试组织成测试计划来改进代码评估](organizing-tests-to-improve-feedback.md)。

> [!note] 注意
> 当你在 Xcode 中设置了模拟位置后，位置的变化只对测试包中运行的代码生效。UI 自动化测试是与作为独立进程运行的你的 App 通信的，因此在这类测试中，你的 App 不会使用该模拟位置。要在 UI 自动化测试中模拟位置，请参阅下面的 "为 UI 自动化设置模拟位置" 一节。

### 回放先前录制的行程

通过把模拟位置设置为一个 GPX 文件，来测试你的 App 中处理设备位置变化的功能。测试运行期间，Xcode 会使用该 GPX 文件回放一段行程，更新设备的模拟位置、海拔和速度，以还原所录制的行程。要把一个 GPX 文件添加到你的工作区，请按下面的步骤操作：

1. 打开 Xcode。
2. 依次选择 Product \> Test Plan \> Edit Test Plan。
3. 在测试计划编辑器面板中，选择 Configuration。
4. 在 Localization 下，点击 Simulated Location，选择 Add GPX File to Workspace。
5. 定位到你的 GPX 文件，点击 Add。

Xcode 会使用所添加的 GPX 文件在测试中模拟位置。你可以添加多个 GPX 文件，并在测试计划配置的 Simulated Location 设置中进行切换。

### 为单元测试构造位置

在测试你的 App 的位置处理逻辑时，你不需要使用 [CLLocationManager](../corelocation/cllocationmanager.md) 或获取设备的位置。你可以在测试中用已知的坐标经纬度值构造 [CLLocationCoordinate2D](../corelocation/cllocationcoordinate2d.md) 实例。把这些实例传给被测代码，并验证你的代码在给定值下的行为是否符合预期。

### 为 UI 自动化设置模拟位置

在你的 UI 自动化测试中，通过把共享的 [XCUIDevice](../xctest/xcuidevice.md) 位置设置为一个 [XCUILocation](../xctest/xcuilocation.md) 实例来更新模拟设备位置。

```swift
import XCTest
import CoreLocation

final class SampleAppTests: XCTestCase {

  func testExample() throws {
    XCUIDevice.shared.location = XCUILocation(location: CLLocation(latitude: 37.334886, longitude: -122.008988))
	// 启动你的 App 并运行测试。
  }
}
```
