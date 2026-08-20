---
title: 测试与性能
framework: Technology Overviews
symbol_kind: article
role: article
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/technologyoverviews/testing-and-performance
source_url: 'https://developer.apple.com/documentation/technologyoverviews/testing-and-performance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/technologyoverviews/testing-and-performance.json'
content_hash: 'sha256:1add1f04d3ec904a'
translated: true
---

> 导航：[技术](../technologies.md) · [技术概览](../technologyoverviews.md) · [工具与分发](tools-and-distribution.md)

# 测试与性能

通过测试并定期收集性能指标，发现并修复代码中的潜在问题。

在开发过程中测试代码并分析其性能，可以将你的项目提升到新的水平。一套全面的测试有助于验证你的代码按预期运行，而性能指标则帮助你判断你的 App 是否高效地使用了资源。当你定期收集测试和性能数据时，你就能及早发现问题，并有时间加以解决。

## 为你的项目创建测试计划

[测试计划（test plan）](../xcode/organizing-tests-to-improve-feedback.md)是各种规模的团队开发过程中必不可少的组成部分。一个测试计划包含以下几个要素：

- [单元测试](testing-and-performance.md#Write-unit-tests-for-your-code)，用于验证某个类型或功能的各个行为。
- [UI 测试](testing-and-performance.md#Test-interactions-with-your-apps-interface)，用于验证你的 App 如何响应与界面的直接交互。
- 测试套件（test suite），即测试分组，用于一同验证某个特定类型或功能。
- 测试包（test bundle），即测试套件的集合，用于验证你的整个代码库。

在 Xcode 中，[向你的项目添加测试包](../xcode/adding-tests-to-your-xcode-project.md)，并用它来创建你的初始测试和测试套件。每个测试包都有一个关联的目标（target），你在运行测试之前会构建并运行该目标。你可以在每次构建目标时运行测试，也可以仅在特定时间运行它们。例如，你可能只在你向源代码管理系统提交更改之前运行测试。

Xcode 项目中的测试导航器（Test navigator）面板会显示你项目的整体测试计划，以及来自所有测试包的测试。[从 Xcode 或命令行运行你的测试计划](../xcode/running-tests-and-interpreting-results.md)，并在向项目提交任何代码更改之前验证结果。通过在 [Xcode Cloud](../xcode/xcode-cloud.md) 中运行测试计划来自动化你的测试。

## 为你的代码编写单元测试

单元测试（unit test）是一个运行部分代码并判断该代码是否产生预期结果的函数。你可以为 App 创建任意数量的单元测试，并用它们来验证特定类型或功能的行为。例如，一个测试可能验证自定义对象是否正确添加了数据，而另一个测试则验证删除过程。

要为你的代码编写单元测试，请[向你的项目添加一个测试包](../xcode/adding-tests-to-your-xcode-project.md)，并将其配置为使用 [Swift Testing](../testing.md) 或 [XCTest](../xctest.md) 框架。这两个框架都为编写单元测试函数和检查预期结果提供代码级别的支持。[Swift Testing](../testing.md) 提供了强大且富有表现力的工具来声明和管理你的单元测试，是测试 Swift 代码的绝佳选择。对你创建的任何 UI 测试，以及你用 Swift、Objective-C 和其他基于 C 的语言编写的代码，请使用 [XCTest](../xctest.md)。要测试 App 的 App 内购买（In-App Purchase）代码，除了其中一个框架外，还需包含 [StoreKit Test](../storekittest.md) 框架。

以下示例展示了在 [Swift Testing](../testing.md) 和 [XCTest](../xctest.md) 中相同的单元测试。Swift Testing 使用基于宏的方法来[标记测试函数](../testing/definingtests.md)，从而生成简短易读的测试代码。创建专用的 XCTest 类型，并使用它们来[定义你的测试用例](../xctest/defining-test-cases-and-test-methods.md)。

**Swift Testing**

```swift
@Test func checkNewEmptyTable() {
    let table = Table()
    #expect(table.rowCount == 0)
    #expect(table.ColumnCount == 0)
}
```

**XCTest**

```swift
class TableValidationTests: XCTestCase {
    /// 验证一个新的 table 实例的行数和列数均为零。
    func testEmptyTableRowAndColumnCount() {
        let table = Table()
        XCTAssertEqual(table.rowCount, 0, "Row count was not zero.")
        XCTAssertEqual(table.columnCount, 0, "Column count was not zero.")
    }
}
```

在 Xcode 项目窗口的测试导航器（Test navigator）面板中查看你项目的单元测试。使用此面板可以随时运行单个单元测试或一组单元测试。或者，也可以从包含测试代码的源窗口中直接运行测试。要为你的测试收集性能指标，请在 Instruments 中运行它们。

在决定创建哪些测试时，应混合包含预期结果为“通过”和“不通过”的测试。验证代码是否正确处理了数据很重要，但验证你的 App 能否正确处理边界条件或错误数据也很重要。例如，你可能会故意用错误的数据运行一个测试，以验证你的代码返回了适当的错误。

## 测试与 App 界面的交互

UI 测试可以验证 App 界面的代码是否产生了预期结果。这些测试模拟与 App 界面的直接交互，并捕获结果供你检查。与单元测试类似，你使用 UI 测试来测试 App 中的特定工作流（workflow）。例如，一个测试可能会打开一个数据录入表单，用特定值填充各个字段，并验证你的代码是否正确处理了数据。

在[UI 测试包](../xcode/adding-tests-to-your-xcode-project.md)中创建 UI 测试，并使用 [XCTest](../xctest.md) 和 [XCUIAutomation](../xcuiautomation.md) 框架来编写它们。XCTest 提供用于创建测试的类型，而 XCUIAutomation 则与 App 的[辅助功能（accessibility）支持](../accessibility.md)协同工作，为你提供对界面中的视图（view）和其他元素的引用。

Xcode 提供了一种方法来[记录与 App 的交互](../xcuiautomation/recording-ui-automation-for-testing.md)，并将其转换为 UI 测试函数的代码。记录一组交互后，增强生成的代码以检查 App 的值或状态。根据需要重写转录的 UI 交互，使你的测试更加健壮。

在你的测试计划中，在你 App 支持的各种设备和语言上运行 UI 测试。不同的配置有助于你发现可能未曾预料到的问题。例如，在不同设备上进行测试可以显示你的 UI 未正确适配的地方。类似地，用不同语言进行测试可以发现[国际化（internationalization）](../xcode/localization.md)问题。

## 采用持续集成与持续交付策略

为了尽早发现错误，请定期运行测试并分析结果。[Xcode Cloud](../xcode/about-continuous-integration-and-delivery-with-xcode-cloud.md) 是一个与 Xcode、TestFlight 和 App Store Connect 集成的持续集成与持续交付（CI/CD）系统。使用它可以[创建工作流（workflow）](../https_/developer.apple.com/videos/play/wwdc2023/10278.md)，自动在 iCloud 中构建你的项目并运行测试。例如，一个工作流可能每当开发者合并拉取请求（pull request）时就构建并运行你的测试。你可以指定测试期间使用的不同设备和语言，甚至可以运行自定义脚本来处理项目特定的操作。

对于 UI 测试，你可以配置 Xcode Cloud，使其在每次运行测试时捕获视频。如果某个特定测试失败，可以使用这些视频作为诊断失败的第一步。使用 Xcode Cloud 收集的其他信息来检查你的 UI，并定位特定测试失败的位置。

## 收集和分析性能指标

效率指的是最大化你的 App 执行的工作量，同时最小化其对内存、电池和其他系统资源的使用。提高代码效率有助于其运行更快、使用更少内存、耗电更少。这些调整有助于改善人们使用你的 App 的整体体验。

Instruments 可以[捕获关于代码正在执行什么操作以及正在使用什么资源的实时洞察信息](../xcode/improving-your-app-s-performance.md)。收集一组基准性能指标后，定期捕获新组以确定性能是提升还是下降了。使用 Instruments 收集关于以下方面的数据：

- 你的 App [启动（launch）](../xcode/reducing-your-app-s-launch-time.md)所需的时间。
- 你的 App [使用的内存量](../xcode/reducing-your-app-s-memory-use.md)以及如何使用这些内存。
- [SwiftUI 视图（view）](../xcode/understanding-and-improving-swiftui-performance.md)更新其内容的频率。
- 你的代码[导致 CPU 停滞](../xcode/addressing-cpu-bottlenecks.md) 或低效运行的位置。
- 你的 App 在等待文件、线程（thread）、网络数据或其他资源时[被阻塞（blocked）](../xcode/improving-app-responsiveness.md)所花费的时间。
- 你的 App 图形代码[卡顿（hitch）](../xcode/understanding-hitches-in-your-app.md)或[挂起（hang）](../xcode/understanding-hangs-in-your-app.md)的位置。
- 你的 App 运行时所[消耗的电量](../xcode/reducing-your-app-s-battery-use.md)。
- 你的 App 并发任务（task）的效率。

你可以将 Instruments 与你创建的用于验证 App 行为的相同测试一起运行，也可以构建自定义测试来收集特定功能的性能指标。对你的代码进行采样以识别潜在问题，并根据需要切换到[处理器跟踪（processor trace）](../xcode/analyzing-cpu-usage-with-processor-trace.md)，以查看代码在 CPU 中运行时执行的确切分支集。
