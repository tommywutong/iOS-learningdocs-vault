---
title: Swift 日志
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/swift-log/'
original_language: en
published: 2020-03-26
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:f2b5ef7ef0a73122'
translated: true
---

> 原文：[Swift Logging](https://nshipster.com/swift-log/)　·　NSHipster (Mattt)

# [Swift Logging](https://nshipster.com/swift-log/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2020 年 3 月 26 日

2002 年，美国国会颁布了《萨班斯-奥克斯利法案》（[Sarbanes–Oxley Act](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act)），该法案针对当时安然（[Enron](https://en.wikipedia.org/wiki/Enron_scandal)）和 MCI WorldCom（[MCI WorldCom](https://en.wikipedia.org/wiki/MCI_Inc.#Accounting_scandals)）等公司的会计丑闻，引入了广泛的企业监管。该法案与 [PCI](https://en.wikipedia.org/wiki/PCI_DSS) 和 [HIPAA](https://en.wikipedia.org/wiki/HIPAA) 共同构成了从 [互联网泡沫](https://en.wikipedia.org/wiki/Dot-com_bubble) 中崛起的新一代 IT 公司的监管背景。

大约在同一时期，我们还看到了短暂、分布式基础设施的出现——即我们现在所说的 [“云计算”](https://en.wikipedia.org/wiki/Cloud_computing)——这种范式使系统更强大，但也更复杂。

为了解决 21 世纪在监管和后勤方面的双重挑战，我们的行业确立了围绕应用日志记录的最佳实践。许多相同的工具和标准至今仍在使用。

---

本周的 NSHipster，我们将探讨 [`SwiftLog`](https://github.com/apple/swift-log)：一个社区驱动的、用于 Swift 日志记录的开源标准。

它由 Swift 服务端社区开发，并得到了 [SSWG（Swift 服务端工作组）](https://swift.org/server/) 的认可，但其好处并不仅限于服务端使用。事实上，任何旨在从命令行运行的 Swift 代码都会从采用 `SwiftLog` 中受益。请继续阅读以了解如何使用。

---

一如既往，一个例子将有助于引导我们的讨论。本着透明和怀旧的精神，让我们想象编写一个 Swift 程序，用于审计一家 2000 年代财富 500 强公司的财务状况。

```
import Foundation

struct Auditor {
    func watch(_ directory: URL) throws { … }
    func cleanup() { … }
}

do {
    let auditor = Auditor()

    defer { auditor.cleanup() }
    try auditor.watch(directory: URL(string: "ftp://…/reports")!,
                     extensions: ["xls", "ods", "qdf"]) // poll for changes
} catch {
    print("error: \(error)")
}
```

一个 `Auditor` 类型轮询目录（一个 FTP 服务器，因为请记住：现在是 2003 年）的更改。每当添加、删除或更改文件时，都会审计其内容是否存在差异。如果发现任何财务异常，则使用 `print` 函数进行记录。连接到 FTP 或程序可能遇到的任何其他问题也是如此——所有内容都使用 `print` 记录。

非常简单。我们可以像这样从命令行运行它：

```
$ swift run audit
starting up...
ERROR: unable to reconnect to FTP

# (try again after restarting PC under our desk)

$ swift run audit
+ connected to FTP server
! accounting discrepancy in balance sheet 
** Quicken database corruption! **
^C
shutting down...
```

这样的程序在技术上可能是合规的，但它还有很大的改进空间：

- 首先，我们的输出没有任何关联的时间戳。无法知道问题是在一小时前还是上周被检测到的。
- 另一个问题是我们的输出缺乏任何连贯的结构。一眼看去，没有直接的方法可以将程序噪音与实际问题隔离开来。
- 最后——这主要是由于示例指定不足——目前尚不清楚此输出是如何处理的。这个输出去了哪里？如何收集、聚合和分析？

---

好消息是，所有这些问题（以及许多其他问题）都可以通过在项目中采用正式的日志记录基础架构来解决。

---

## 在你的 Swift 程序中采用 SwiftLog

将 `SwiftLog` 添加到现有的 Swift Package 中非常容易。你可以逐步集成它，而无需对你的代码进行任何根本性更改，并且可以在几分钟内使其工作。

### 将 swift-log 添加为 Package 依赖项

在你的 `Package.swift` 文件中，将 `swift-log` 添加为 Package 依赖项，并将 `Logging` 模块添加到目标的依赖项列表中。

```
// swift-tools-version:5.1

import PackageDescription

let package = Package(
    name: "Auditor2000",
    products: [
        .executable(name: "audit", targets: ["audit"])
    ],
    dependencies: [
        .package(url: "https://github.com/apple/swift-log.git", from: "1.2.0"),
    ],
    targets: [
        .target(name: "audit", dependencies: ["Logging"])
    ]
)
```

### 创建一个共享的全局 Logger

`Logger` 提供了两个初始化方法，其中较简单的一个接受单个 `label` 参数：

```
let logger = Logger(label: "com.NSHipster.Auditor2000")
```

在 [POSIX](https://en.wikipedia.org/wiki/POSIX) 系统中，程序操作三个预定义的 [流](https://en.wikipedia.org/wiki/Standard_streams)：

| 文件句柄 | 描述 | 名称 |
|---|---|---|
| 0 | `stdin` | 标准输入 |
| 1 | `stdout` | 标准输出 |
| 2 | `stderr` | 标准错误 |

默认情况下，`Logger` 使用内置的 `StreamLogHandler` 类型将记录的消息写入标准输出（`stdout`）。我们可以通过使用更复杂的初始化方法覆盖此行为，改为写入标准错误（`stderr`），该方法接受一个 `factory` 参数：一个闭包（closure），它接受一个单独的 `String` 参数（label）并返回一个符合 `LogHandler` 协议的对象。

```
let logger = Logger(label: "com.NSHipster.Auditor2000",
                    factory: StreamLogHandler.standardError)
```

### 用日志语句替换 Print 语句

将我们的 `logger` 声明为顶级常量，使我们可以在模块内的任何位置调用它。让我们重新审视我们的示例，并用新的记录器来美化它：

```
do {
    let auditor = Auditor()

    defer {
        logger.trace("Shutting down")
        auditor.cleanup()
    }

    logger.trace("Starting up")
    try auditor.watch(directory: URL(string: "ftp://…/reports")!,
                      extensions: ["xls", "ods", "qdf"]) // poll for changes
} catch {
    logger.critical("\(error)")
}
```

`trace`、`debug` 和 `critical` 方法以其各自的日志级别记录消息。`SwiftLog` 定义了七个级别，按严重性升序排列，从 `trace` 到 `critical`：

| Level | 描述 |
|---|---|
| `.trace` | 适用于仅在调试程序时包含信息的消息。 |
| `.debug` | 适用于通常仅在调试程序时才有用的消息。 |
| `.info` | 适用于信息性消息。 |
| `.notice` | 适用于非错误条件，但可能需要特殊处理的情况。 |
| `.warning` | 适用于非错误条件，但比 `.notice` 更严重的消息。 |
| `.error` | 适用于错误条件。 |
| `.critical` | 适用于通常需要立即关注的关键错误条件。 |

如果我们使用新的日志框架重新运行我们的 `audit` 示例，我们可以立即看到在日志行中清晰标记、不同严重性级别的好处：

```
$ swift run audit
2020-03-26T09:40:10-0700 critical: Couldn't connect to ftp://…

# (try again after plugging in loose ethernet cord)

$ swift run audit
2020-03-26T10:21:22-0700 warning: Discrepancy in balance sheet
2020-03-26T10:21:22-0700 error: Quicken database corruption
^C
```

除了标记消息之外——请不要误会，这本身就已经足够了——日志级别还提供了可配置的披露级别。请注意，使用 `trace` 方法记录的消息不会出现在示例输出中。这是因为 `Logger` 默认只显示记录为 `info` 或更高级别的消息。

你可以通过设置 `Logger` 的 `logLevel` 属性（property）来配置这一点。

```
var logger = Logger(label: "com.NSHipster.Auditor2000")
logger.logLevel = .trace
```

进行此更改后，示例输出将如下所示：

```
$ swift run audit
2020-03-25T09:40:00-0700 trace: Starting up
2020-03-26T09:40:10-0700 critical: Couldn't connect to ftp://…
2020-03-25T09:40:11-0700 trace: Shutting down

# (try again after plugging in loose ethernet cord)

$ swift run audit
2020-03-25T09:41:00-0700 trace: Starting up
2020-03-26T09:41:01-0700 debug: Connected to ftp://…/reports
2020-03-26T09:41:01-0700 debug: Watching file extensions ["xls", "ods", "qdf"]
2020-03-26T10:21:22-0700 warning: Discrepancy in balance sheet
2020-03-26T10:21:22-0700 error: Quicken database corruption
^C
2020-03-26T10:30:00-0700 trace: Shutting down
```

## 同时使用多个日志处理程序

回想一下我们在最初示例中的反对意见，剩下的唯一问题是实际如何处理这些日志。

根据 [12 Factor App（12 要素应用）](https://12factor.net/logs) 原则：

> ## XI. 日志
> 
> _[…]_
> 
> **12 要素应用从不关心其输出流的路由或存储。** 它不应尝试写入或管理日志文件。相反，每个正在运行的进程将其事件流无缓冲地写入 `stdout`。

跨分布式系统收集、路由、索引和分析日志通常需要一系列的开源库和商业产品。幸运的是，这些组件中的大多数都以 [syslog](https://en.wikipedia.org/wiki/Syslog) 消息作为通用货币进行交换——并且得益于 [这个由 Ian Partridge 开发的 Package](https://github.com/ianpartridge/swift-log-syslog)，Swift 也可以做到这一点。

话虽如此，很少有工程师能够从 [Splunk](https://www.splunk.com) 之类的工具中检索到这些信息并全身而退。对于我们这些凡人来说，我们可能更喜欢 [这个由 Will Lisac 开发的 Package](https://github.com/wlisac/swift-log-slack)，它将日志消息发送到 [Slack](https://slack.com)。

好消息是，我们可以同时使用两者，而无需通过使用 `Logging` 模块的另一个部分 `MultiplexLogHandler` 来更改调用站点记录消息的方式。

```
import struct Foundation.ProcessInfo
import Logging
import LoggingSyslog
import LoggingSlack

LoggingSystem.bootstrap { label in
    let webhookURL = URL(string:
        ProcessInfo.processInfo.environment["SLACK_LOGGING_WEBHOOK_URL"]!
    )!
    var slackHandler = SlackLogHandler(label: label, webhookURL: webhookURL)
    slackHandler.logLevel = .critical

    let syslogHandler = SyslogLogHandler(label: label)

    return MultiplexLogHandler([
        syslogHandler,
        slackHandler
    ])
}

let logger = Logger(label: "com.NSHipster.Auditor2000")
```

有了这一切，我们的系统将把所有内容以 syslog 格式记录到标准输出（`stdout`），然后可以由其他系统收集和分析。

---

但这种日志记录方法的真正优势在于，它可以扩展以满足任何环境的特定需求。你的系统不是将 syslog 写入 `stdout` 或 Slack 消息，而是可以发送电子邮件、打开 SalesForce 工单，或触发 webhook 来激活某些 IoT 设备。

以下是你可以通过编写自定义日志处理程序来扩展 `SwiftLog` 以满足你的需求的方法：

## 创建自定义日志处理程序

`LogHandler` 协议指定了可以由 `Logger` 注册为消息处理程序的类型所需满足的要求：

```
protocol LogHandler {
    subscript(metadataKey _: String) -> Logger.Metadata.Value? { get set }
    var metadata: Logger.Metadata { get set }

    var logLevel: Logger.Level { get set }

    func log(level: Logger.Level,
             message: Logger.Message,
             metadata: Logger.Metadata?,
             file: String, function: String, line: UInt)
}
```

在撰写本文的过程中，我创建了一个 [自定义处理程序](https://github.com/NSHipster/swift-log-github-actions)，用于格式化发送到 GitHub Actions 的日志消息，使其在 GitHub 的 UI 上像这样显示：

![](https://nshipster.com/assets/github-actions-ui-3fe079aeea203a7d579a873d74ef310d9d4cfb9522604675179a9ddb243756e0bd269aa4472ab82ccb9712f33f513aae528112cbabec46ad7b6072c329be00a4.png)

如果你有兴趣制作自己的日志处理程序，只需浏览 [这个项目的代码](https://github.com/NSHipster/swift-log-github-actions) 就可以学到很多东西。但我想在此指出几点有趣的地方：

### 条件性引导

在引导你的日志系统时，你可以定义一些关于如何配置的逻辑。例如，对于特定于某个 CI 供应商的日志格式化程序，你可能会检查环境看看你是在本地运行还是在 CI 上运行，并相应地进行调整。

```
import Logging
import LoggingGitHubActions
import struct Foundation.ProcessInfo

LoggingSystem.bootstrap { label in
    // 我们是否在 GitHub Actions 工作流中运行？
    if ProcessInfo.processInfo.environment["GITHUB_ACTIONS"] == "true" {
        return GitHubActionsLogHandler.standardOutput(label: label)
    } else {
        return StreamLogHandler.standardOutput(label: label)
    }
}
```

### 测试自定义日志处理程序

测试比最初预期的更具挑战性。我可能遗漏了一些明显的东西，但似乎没有办法对写入标准输出的文本进行断言。所以我这样做：

首先，创建一个接受 `TextOutputStream` 参数的 `internal` 初始化方法，并将其存储在一个 `private` 属性中。

```
public struct GitHubActionsLogHandler: LogHandler {
    private var outputStream: TextOutputStream

    internal init(outputStream: TextOutputStream) {
        self.outputStream = outputStream
    }

    …
}
```

然后，在测试目标中，创建一个采用 `TextOutputStream` 协议的类型，并将记录的消息收集到一个存储属性中，以供后续检查。通过使用声明了 `GitHubActionsLogHandler` 模块的 [`@testable import`](https://docs.swift.org/swift-book/LanguageGuide/AccessControl.html#ID5)，我们可以访问之前的那个 `internal` 初始化方法，并传递一个 `MockTextOutputStream` 实例来拦截记录的消息。

```
import Logging
@testable import LoggingGitHubActions

final class MockTextOutputStream: TextOutputStream {
    public private(set) var lines: [String] = []

    public init(_ body: (Logger) -> Void) {
        let logger = Logger(label: #file) { label in
            GitHubActionsLogHandler(outputStream: self)
        }

        body(logger)
    }

    // MARK: - TextOutputStream

    func write(_ string: String) {
        lines.append(string)
    }
}
```

有了这些部分，我们终于可以测试我们的处理程序是否按预期工作：

```
func testLogging() {
    var logLevel: Logger.Level?
    let expectation = MockTextOutputStream { logger in
        logLevel = logger.handler.logLevel

        logger.trace("🥱")
        logger.error("😱")
    }

    XCTAssertGreaterThan(logLevel!, .trace)
    XCTAssertEqual(expectation.lines.count, 1) // trace log is ignored
    XCTAssertTrue(expectation.lines[0].hasPrefix("::error "))
    XCTAssertTrue(expectation.lines[0].hasSuffix("::😱"))
}
```
