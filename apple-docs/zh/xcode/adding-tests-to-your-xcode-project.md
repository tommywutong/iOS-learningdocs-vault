---
title: 向 Xcode 项目添加测试
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/adding-tests-to-your-xcode-project
source_url: 'https://developer.apple.com/documentation/xcode/adding-tests-to-your-xcode-project'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/adding-tests-to-your-xcode-project.json'
content_hash: 'sha256:edcfe8cf0fcbe3a5'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Testing](testing.md)

# 向 Xcode 项目添加测试

<sub>文章</sub>

包含用于构建测试代码的测试 target，以测试函数中的逻辑、检查集成问题、自动执行 UI 工作流程并测量性能。

## 概述

在 Xcode 16 及更高版本中创建新项目时，请从选项对话框的弹出式菜单中选取 Testing System，让 Xcode 使用测试 bundle 配置项目。

Xcode 包含两个测试框架：

- **[Swift Testing](../testing.md)** — 一个较新的现代测试框架，充分利用 Swift 编程语言强大且富有表现力的语言能力。编写测试所需维护的代码更少，并能提供更具可操作性的反馈。请将其用于直接调用代码的单元测试和集成测试。
- **[XCTest](../xctest.md)** — 一个广泛使用且成熟完善的测试框架，支持编写单元测试、集成测试、UI 测试和性能测试。

测试系统选项包括 Swift Test with XCTest UI Tests 和 XCTests for Unit and UI Tests。选好后，Xcode 会向项目添加两类测试 target：一个用于单元测试，名称以“Tests”结尾；另一个用于 UI 测试，名称以“UITests”结尾。你可以在 Project navigator 中找到与每个 target 对应的名称，以及一个可用于开始编写首批测试的模板文件。测试系统的选择会影响 Xcode 在单元测试文件模板中包含的主要框架。旧版 Xcode 会在创建新项目时启用 Include Tests 选项后包含这些 target，并提供使用 XCTest 的文件模板。

### 添加新的测试 target

如果需要为其他 target 添加测试，或想向现有 target 添加测试：

1. 选取 File \> New \> Target。
2. 在模板筛选栏中输入“Test”。
3. 选择 Unit Testing Bundle 或 UI Testing Bundle。
4. 点按 Next。
5. 填写选项。
6. 点按 Finish。

> [!note] 注意
> Swift Testing 和 XCTest 可以从同一测试 target 构建，并共存于同一测试 bundle 中。如果项目已经包含一个使用 XCTest 编写单元测试的测试 bundle，无需向项目添加新的 Unit Testing Bundle 即可开始使用 Swift Testing 编写单元测试。你可以向 target 添加使用 Swift Testing 的其他文件，并在时间允许时考虑转换旧测试。

### 编写单元测试

若要编写测试，请从测试 target 中选择测试文件，然后选择要为其编写单元测试的类型或函数。如果需要向 target 添加新的测试文件，请选取 File \> New \> New File From Template，然后选择 Swift Testing Unit Test 或 XCTest Unit Test，添加具有适当结构的测试文件。实现单元测试的测试函数按顺序包含以下三个步骤：

1. **准备（Arrange）** — 创建所测试代码路径使用的任何对象或数据结构。使用易于配置的“桩”替换复杂依赖项，确保测试能够快速运行并具有确定性。采用依赖注入和面向协议编程，可确保 App 中对象之间的关系足够灵活，以便用桩替代真实实现。
2. **执行（Act）** — 使用你在准备阶段配置的参数和属性，调用要测试的方法或函数。
3. **断言（Assert）** — 使用 Swift Testing 中的[预期和确认](../testing/expectations.md)，或 [XCTest](../xctest.md) 中的测试断言，将执行阶段所运行代码的行为与预期行为进行比较。任何条件为 false 的预期都会导致测试失败。

在 Swift Testing 中，测试函数只是添加了 `Test` 属性的普通 Swift 函数。它们可以是全局函数，也可以是类型中的方法。你还可以选择使用 `Suite` 属性标记包含测试函数的类型，以标识测试套件。可以将它们标记为 async 或 throws，也可以将它们隔离到全局 actor。

对于使用 XCTest 创建的测试，请创建 [XCTestCase](../xctest/xctestcase.md) 的子类来包含测试方法。向 `XCTestCase` 子类添加一个不接受参数、返回 `Void` 的方法，并让方法名称以“`test`”开头。

**Swift Testing**

```swift
struct MyAPITests {
    @Test func myAPIWorks() {
        // 准备：创建必要的依赖项。
        // 执行：使用上面创建的依赖项调用 myAPIWorks。
        #expect(/* … */, "The function didn't return the expected result")
    }
}
```

**XCTest**

```swift
class MyAPITests : XCTestCase {
    func testMyAPIWorks() {
        // 准备：创建必要的依赖项。
        // 执行：使用上面创建的依赖项调用我的 API。
        XCTAssertTrue(/* … */, "The function didn't return the expected result")
    }
}
```

覆盖多条路径并测试每种场景。例如，如果函数接收可选参数，请分别测试参数为 `nil` 和非 `nil` 值的情况。识别代码中的边界情况和逻辑分支，并编写单元测试覆盖这些情况的每种组合。若要使用 Swift Testing 测试项目中函数或方法的多条路径，请实现参数化测试函数。有关更多信息，请参阅[实现参数化测试](../testing/parameterizedtesting.md)。在 XCTest 中，每个单元测试都应断言项目中某个方法或函数的一条路径的预期行为。若要覆盖多条路径，请为每种场景编写一个测试。

有关使用 Swift Testing 定义测试的更多信息，请参阅[定义测试函数](../testing/definingtests.md)。有关使用 XCTest 定义测试的更多信息，请参阅[定义测试用例和测试方法](../xctest/defining-test-cases-and-test-methods.md)。

> [!note] 注意
> Swift 访问控制模型会阻止外部实体访问任何声明为 internal 的内容。若要从测试代码访问声明为 internal 的项目，请在编译测试代码需要访问的模块时启用 [Enable Testability](build-settings-reference.md#Enable-Testability)，并向该模块的 import 语句添加 `@testable` 属性。有关更多信息，请参阅[访问控制](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol/#Access-Levels-for-Unit-Test-Targets)。

### 编写集成测试

集成测试与单元测试非常相似，使用相同的 API，并遵循相同的准备—执行—断言模式。单元测试和集成测试之间的区别在于规模。单元测试只覆盖 App 逻辑中很小的一部分，而集成测试会检查更大子系统或类与函数组合的行为。在集成测试的准备步骤中，请扩大受测真实项目代码的范围，减少桩对象的使用。

与单元测试尝试覆盖每种不同条件或边界情况不同，集成测试用于断言组件在重要情况下能够协同工作以实现 App 目标。例如，测试从控制器收到的值是否正确存储在模型中，以及网络请求产生的错误是否传递到用户界面并由其呈现。

### 编写 UI 测试

UI 测试的工作方式与单元测试和集成测试不同。新文件所用的 XCTest UI Test 模板包含 UI 测试的常见起点。你可以在 [XCTestCase](../xctest/xctestcase.md) 子类中使用 XCTest 实现 App 的 UI 测试。UI 测试不会直接执行 App 代码，而是使用 App 的用户界面控件，确定用户能否使用 App 完成特定任务。

创建 UI 测试，以验证 App 能否响应用户交互完成任务，并且没有引入破坏 UI 控件行为的错误。复现真实用户活动的 UI 测试可以让你确信 App 能够用于其预定任务。例如，基于文稿的 App 的 UI 测试可以验证用户能否创建新文稿、编辑其内容，然后删除文稿。

若要在 `XCTestCase` 子类的方法中创建 UI 测试，请使用 Xcode 中的 Record UI Test 功能录制与 App 的交互。设计 UI 测试时，应复现一旦中断就会影响用户的最关键工作流程，并重放已报告的错误以避免回归。

![显示 Xcode 中 Record UI Tests 按钮的图像。](../../../attachments/af3223bfb6cc09fe1d5ff0a0d0ca9912/adding-tests-to-your-xcode-project-ui-record@2x.png)

录制用于运行受测功能的工作流程时，请使用测试断言函数，确保 UI 的最终状态符合根据录制交互期间所执行操作得出的预期。

```swift
class MyUITests: XCTestCase {
    let app = XCUIApplication()

    // MARK: - 设置与拆卸

    override func setUp() {
        super.setUp()
        // 在 UI 测试中，如果发生失败，最好立即停止测试。
        continueAfterFailure = false
        // UI 测试必须启动其测试的 App。在设置中执行此操作，确保 App 会为每个测试方法启动。
        XCUIApplication().launch()
    }

    override func tearDown() {
        // 在此处放置拆卸代码。测试运行器会在调用类中的每个测试方法后调用此方法。
        super.tearDown()
    }

    func testAddition() {
        // 执行 UI 操作以完成任务。
        // 检查预期的 UI 状态值。
        if let value = app.<ui_type>[<ui_identifier>].value as? String {
            XCTAssertTrue(value = /* … */, "The function didn't return the expected result")
        }
    }
}
```

如果 UI 测试模拟包含多个不同步骤的复杂工作流程，请使用 [XCTActivity](../xctest/xctactivity.md) 组织共享步骤并为其命名。创建辅助方法，以共享多个测试中使用的活动实现。

### 编写性能测试

编写性能测试，以收集执行某段代码期间的耗时、内存用量或写入数据量信息。XCTest 会多次运行代码并测量所请求的指标。你可以为指标设置基准预期；如果测量值明显差于基准，XCTest 会报告测试失败。

若要测试代码耗时，请在测试方法中调用 [measure(_:)](<../xctest/xctestcase/measure(__).md>)，并在 `measure(_:)` 的代码块参数中运行 App 代码。若要使用其他指标测量性能，包括内存用量和写入磁盘的数据量，请调用 [measure(metrics:block:)](<../xctest/xctestcase/measure(metrics_block_).md>)。

```swift
class PerformanceTests : XCTestCase {
    func testCodeIsFastEnough() {
        self.measure() {
          // 在此处放置对性能敏感的代码。
        }
    }
}
```

## 另请参阅

### 测试开发

- [更新现有代码库以适应单元测试](updating-your-existing-codebase-to-accommodate-unit-tests.md) — 移除组件之间的耦合，以提高测试覆盖率和可靠性。
- [确定测试覆盖了多少代码](determining-how-much-code-your-tests-cover.md) — 使用代码覆盖率，将新测试的开发重点放在缺少充分测试的区域。
- [将测试组织到测试计划中以改进代码评估](organizing-tests-to-improve-feedback.md) — 创建并配置测试计划，控制在软件工程流程的不同阶段从测试中收到的信息。
