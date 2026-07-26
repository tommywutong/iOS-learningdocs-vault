---
title: 解读崩溃报告的 JSON 格式
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/interpreting-the-json-format-of-a-crash-report
source_url: 'https://developer.apple.com/documentation/xcode/interpreting-the-json-format-of-a-crash-report'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/interpreting-the-json-format-of-a-crash-report.json'
content_hash: 'sha256:8d60358be72f9fec'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md)

# 解读崩溃报告的 JSON 格式

<sub>文章</sub>

了解系统包含在崩溃报告 JSON 中的各个对象的结构与属性。

## 概述

从 iOS 15 和 macOS 12 开始，生成崩溃报告的 App 会将数据以 JSON 格式存储在扩展名为 `.ips` 的文件中。像 Console 这样用于查看这些文件的工具，会转换这些 JSON，使其更易于阅读和理解。转换后的内容使用的是 [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md) 一文中描述的字段名。请参阅以下信息，了解系统用于这些崩溃报告的 JSON 结构，以及数据如何映射到转换后内容中所使用的字段名。

典型的 JSON 解析器期望文件正文中只有一个 JSON 对象。而崩溃报告的 IPS 文件包含两个 JSON 对象：一个包含关于该报告事件的 IPS 元数据的对象，以及一个包含崩溃报告数据的对象。解析该文件时，先从第一行提取元数据对象的 JSON。如果元数据对象的 `bug_type` 属性为 `309`（崩溃报告的日志类型），你就可以从剩余的文本中提取崩溃报告数据的 JSON。

下面的示例将崩溃报告的内容读取到一个字典中：

```swift
    do {
        let content = try String(contentsOfFile: filePath, encoding: String.Encoding.utf8)

        /// 读取第一行，即元数据对象，存入字典。
        let metadataRange = content.lineRange(for: ..<content.startIndex)
        let metadataJSON = content[metadataRange].data(using: .utf8)
        let metadata = try JSONSerialization.jsonObject(with: metadataJSON!) as! Dictionary<String, Any>

        /// 检查元数据的 `bug_type` 属性是否为类型 `309`，即崩溃报告的日志类型。
        let logType = "\(metadata["bug_type"] ?? "(unknown)")"
        guard logType == "309" else {
            // 处理该错误。        
            fatalError("Log type \(logType) is not a crash report.")
        }

        /// 读取文件的剩余部分，即崩溃报告对象，存入字典。
        let reportRange = content.lineRange(for: metadataRange.upperBound..<content.endIndex)
        let reportJSON = content[reportRange].data(using: .utf8)
        let report = try JSONSerialization.jsonObject(with: reportJSON!) as! Dictionary<String, Any>

        return report
    } catch {
        // 处理该错误。
        fatalError("*** An error occurred while reading the crash report: \(error.localizedDescription) ***")
    }
```

崩溃报告数据由与操作系统版本、Bundle、Store、异常、终止、线程、帧以及二进制镜像相关的其他对象组成。以下概述了所有这些对象的属性。

### IPS 元数据

IPS 元数据对象包含以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `name` | String | 该报告所对应进程的名称。通常是该进程的可执行文件名。 |
| `bug_type` | String | 该报告所捕获日志类型的标识符。本文所述崩溃报告的类型为 `309`。你可能会遇到其他类型，例如 `288` 就是一个 stackshot。 |
| `bundleID` | String | 该报告所对应进程的 Bundle 标识符；参见 [CFBundleIdentifier](../bundleresources/information-property-list/cfbundleidentifier.md)。 |
| `build_version` | String | 该报告所对应进程的 Bundle 版本字符串；参见 [CFBundleVersion](../bundleresources/information-property-list/cfbundleversion.md)。 |
| `incident_id` | String | 该报告的唯一标识符。任何两份报告都不会共用同一个标识符。 |
| `platform` | Number | 一个数字，标识该进程运行所在的平台。这些值的含义请参阅 [Platforms](interpreting-the-json-format-of-a-crash-report.md#Platforms)。 |
| `timestamp` | String | 日志系统为报告跟踪生成的日期和时间。请使用崩溃报告对象中的 `procLaunch` 和 `captureTime` 属性来确定该进程的启动和终止时间。 |

### 崩溃报告

崩溃报告对象可以包含以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `asi` | Dictionary | 额外的、特定于 App 的日志记录。该对象的属性包括一个日志字符串数组。更多信息，请参阅 [Diagnostic messages](examining-the-fields-in-a-crash-report.md#Diagnostic-messages)。在转换后的报告中，它出现在 Application Specific Information 下。 |
| `bundleInfo` | Dictionary | 发生崩溃的进程的 Bundle 信息。关于该对象属性的说明，请参阅 [Bundle info](interpreting-the-json-format-of-a-crash-report.md#Bundle-info)。 |
| `captureTime` | String | 崩溃发生的日期和时间。在转换后的报告中，它出现在 Date/Time 下。 |
| `coalitionID` | String | 包含该进程的联盟（coalition）的 ID。进程联盟用于跟踪一组相关进程的资源使用情况，例如支持某个 API 功能、供某个 App 使用的操作系统进程。大多数进程（包括 App 扩展）都会各自形成自己的联盟。在转换后的报告中，它出现在 Coalition 下。 |
| `coalitionName` | String | 包含该进程的联盟的名称。更多详情，参见上文关于 `coalitionID` 的描述。 |
| `cpuType` | String | 发生崩溃的进程所使用的 CPU 架构。取值为 ARM-64、ARM、X86-64 或 X86 之一。在转换后的报告中，它出现在 Code Type 下。 |
| `crashReporterKey` | String | 一个经过匿名化处理的、按设备划分的标识符。来自同一设备的两份报告包含相同的值。抹掉设备后，该标识符会重置。在转换后的报告中，它出现在 CrashReporter Key 下。 |
| `DTAppStoreToolsBuild` | String | 用于编译你 App 的 bitcode、并将你 App 瘦身为特定设备变体的 Xcode 版本。在转换后的报告中，它出现在 AppStoreTools 下。 |
| `exception` | Dictionary | 关于该进程如何终止的信息。关于该对象属性的说明，请参阅 [Exception](interpreting-the-json-format-of-a-crash-report.md#Exception)。 |
| `faultingThread` | Number | 发生崩溃的线程的索引。`threads` 数组中该索引处的对象包含了关于该线程的信息，例如其寄存器的状态。关于该对象属性的说明，请参阅 [Threads](interpreting-the-json-format-of-a-crash-report.md#Threads)。 |
| `incident` | String | 该报告的唯一标识符。任何两份报告都不会共用同一个标识符。在转换后的报告中，它出现在 Incident Identifier 下。 |
| `isCorpse` | Boolean | 一个布尔值，如果崩溃并非源自硬件陷阱（trap）——即该进程是被操作系统显式终止的，或者该进程调用了 `abort()`——则该值为 `true`。在转换后的报告中，它以 EXC_CORPSE_NOTIFY 的形式出现在 Exception Note 下。 |
| `isNonFatal` | String | 一个布尔值，如果该进程并未终止（因为引发该崩溃报告的问题并非致命的），则该值为 `true`。在转换后的报告中，它以 NON-FATAL CONDITION（这_并非_崩溃）的形式出现在 Exception Note 下。 |
| `isSimulated` | String | 一个布尔值，如果该进程并未崩溃、但操作系统随后可能已请求终止该进程，则该值为 `true`。在转换后的报告中，它以 SIMULATED（这_并非_崩溃）的形式出现在 Exception Note 下。 |
| `lastExceptionBacktrace` | String | 发生崩溃的进程的回溯信息，记录了发生某个语言异常的线程上正在运行的代码。关于该对象属性的说明，请参阅 [Threads](interpreting-the-json-format-of-a-crash-report.md#Threads)。在转换后的报告中，它出现在 Last Exception Backtrace 下。 |
| `modelCode` | String | 该进程运行所在的具体设备型号。在转换后的报告中，它出现在 Hardware Model 下。 |
| `osVersion` | Dictionary | 该进程运行所在操作系统的版本信息。关于该对象属性的说明，请参阅 [OS version](interpreting-the-json-format-of-a-crash-report.md#OS-version)。在转换后的报告中，它出现在 OS Version 下。 |
| `parentPid` | Number | 启动发生崩溃的进程的那个进程的标识符。在转换后的报告中，它出现在 Parent Process 下、进程名称后的方括号中。 |
| `parentProc` | String | 启动发生崩溃的进程的那个进程的名称。在转换后的报告中，它出现在 Parent Process 下。 |
| `pid` | Number | 发生崩溃的进程的标识符。在转换后的报告中，它出现在 Process 下、括号前的文本中。 |
| `procLaunch` | String | 该进程启动的日期和时间。在转换后的报告中，它出现在 Launch Time 下。 |
| `procName` | String | 发生崩溃的进程的可执行文件名。在转换后的报告中，它出现在 Process 下、括号前的文本中。 |
| `procPath` | String | 该可执行文件在磁盘上的位置。为保护隐私，macOS 会将可识别用户身份的路径部分替换为占位符值。在转换后的报告中，它出现在 Path 下。 |
| `procRole` | String | 该进程在终止时被赋予的任务角色；参见 [task_role_t](../kernel/task_role_t.md)。在转换后的报告中，它出现在 Role 下。 |
| `storeInfo` | Dictionary | 发生崩溃的进程的 Store 信息。关于该对象属性的说明，请参阅 [Store info](interpreting-the-json-format-of-a-crash-report.md#Store-info)。 |
| `termination` | Dictionary | 关于一个进程被另一个进程终止的信息。关于该对象属性的说明，请参阅 [Termination](interpreting-the-json-format-of-a-crash-report.md#Termination)。 |
| `threads` | Dictionary | 发生崩溃的进程的回溯信息，记录了该进程终止时每个线程上正在运行的代码。关于该对象属性的说明，请参阅 [Threads](interpreting-the-json-format-of-a-crash-report.md#Threads)。每个线程的回溯都会出现在各自的小节中。 |
| `translated` | Boolean | 一个布尔值，对于在 Apple 芯片上通过 Rosetta 转译运行 X86-64 指令的进程，该值为 `true`。 |
| `uptime` | Number | 系统自启动以来运行的时间，单位为秒。在转换后的报告中，它出现在 Time Awake Since Boot 下。 |
| `usedImages` | Array | 该数组中的每个字典条目都包含关于进程终止时已加载的一个二进制镜像的信息，例如 App 的可执行文件和系统框架。关于该对象属性的说明，请参阅 [Binary images](interpreting-the-json-format-of-a-crash-report.md#Binary-images)。在转换后的报告中，它出现在 Binary Images 下。 |
| `version` | Number | 崩溃报告的 schema 版本。 |
| `vmSummary` | String | 该进程正在使用的虚拟内存概要。类似于执行 `vmmap <pid> --summary` 得到的输出。在转换后的报告中，它出现在 VM Region Summary 下。 |
| `vmregioninfo` | String | 由于内存访问问题导致终止时，关于虚拟内存区域的信息。在转换后的报告中，它出现在 VM Region Info 下。 |

### Platforms

`platform` 的数值包括：

- `1` 表示 macOS
- `2` 表示 iOS（包括在 Apple 芯片 macOS 上运行的 iOS App）
- `3` 表示 tvOS
- `4` 表示 watchOS
- `6` 表示 Mac Catalyst
- `7` 表示 iOS 模拟器
- `8` 表示 tvOS 模拟器
- `9` 表示 watchOS 模拟器

### OS version

报告在一个对象中包含操作系统版本信息，该对象可以包含以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `build` | String | 操作系统的构建号。在转换后的报告中，它出现在 OS Version 下的括号内。 |
| `isEmbedded` | Boolean | 一个布尔值，如果该操作系统面向嵌入式平台，则该值为 `true`。 |
| `releaseType` | String | 发布版本的类型：正式版本为 `User`，预发布版本为 `Beta`。在转换后的报告中，它出现在 Release Type 下。 |
| `train` | String | 一个包含平台和操作系统版本号的字符串。在转换后的报告中，它出现在 OS Version 下。 |

### Bundle info

报告在一个对象中包含 Bundle 信息，该对象具有以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `CFBundleIdentifier` | String | 发生崩溃的进程的 Bundle 标识符。在转换后的报告中，它出现在 Identifier 下。 |
| `CFBundleShortVersionString` | String | 发生崩溃的进程的（简短形式）Bundle 版本字符串；参见 [CFBundleShortVersionString](../bundleresources/information-property-list/cfbundleshortversionstring.md)。在转换后的报告中，它出现在 Version 下。 |
| `CFBundleVersion` | String | 发生崩溃的进程的 Bundle 版本；参见 [CFBundleVersion](../bundleresources/information-property-list/cfbundleversion.md)。在转换后的报告中，它出现在 Version 下。 |

### Store info

报告在一个对象中包含 Store 信息，该对象具有以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `applicationVariant` | String | App 精简（app thinning）生成的、你 App 的具体变体。在转换后的报告中，它出现在 App Variant 下。 |
| `deviceIdentifierForVendor` | String | 发生崩溃的 App 的设备与供应商组合的唯一标识符。来自同一供应商、同一设备的 App 的两份报告包含相同的值。该字段仅在 App 的 TestFlight 构建中存在，用以取代 CrashReporter Key 字段。在转换后的报告中，它出现在 Beta Identifier 下。 |
| `itemID` | String | Apple 标识符，是 Store 中各个条目的唯一记录。 |

### Exception

报告在一个对象中包含异常信息，该对象具有以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `codes` | String | 针对处理器的、关于该异常的信息，编码为一个或多个 64 位十六进制数。在转换后的报告中，它出现在 Exception Codes 下。 |
| `message` | String | 从异常代码中提取出的、额外的人类可读信息。在转换后的报告中，它出现在 Exception Message 下。 |
| `signal` | String | BSD 终止信号；参见 [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)。在转换后的报告中，它以括号内文本的形式出现在 Exception Type 下。 |
| `subtype` | String | 该异常代码的人类可读描述。在转换后的报告中，它出现在 Exception Subtype 下。 |
| `type` | String | 终止该进程的 Mach 异常的名称；参见 [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)。在转换后的报告中，它以括号前文本的形式出现在 Exception Type 下。 |

更多信息，请参阅 [Exception information](examining-the-fields-in-a-crash-report.md#Exception-information)。

> [!note] 注意
> 这里的异常信息，并不是指 Objective-C 或 C++ 中由某个 API 或语言特性抛出的语言异常。崩溃报告会单独记录语言异常信息。

### Termination

报告在一个对象中包含终止信息，该对象可以包含以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `byPid` | Number | 发起终止的进程的标识符。在转换后的报告中，它以方括号中数字的形式出现在 Terminating Process 下、发起终止的进程名称之后。 |
| `byProc` | String | 发起终止的进程的名称。在转换后的报告中，它出现在 Terminating Process 下、方括号中 PID 之前。 |
| `code` | Number | 系统用来标识终止原因的代码，或系统使用的 BSD 终止信号。关于可能的原因代码列表，请参阅 [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md)。在转换后的报告中，它出现在 Termination Reason 下。 |
| `flags` | Number | 发起终止的进程为该进程如何终止所设置的选项。 |
| `indicator` | String | 该终止代码的人类可读描述（如果有的话）。在转换后的报告中，它出现在 Termination Reason 下。 |
| `namespace` | String | 系统用来对终止原因进行分类的命名空间。在转换后的报告中，它出现在 Termination Reason 下。 |

关于如何使用这些信息的详情，请参阅 [Exception information](examining-the-fields-in-a-crash-report.md#Exception-information)。

JSON 将数值存储为十进制数。系统存储在 `code` 属性中的值，是要以十六进制形式查看的；参见 [Convert numeric values to hexadecimal numbers](interpreting-the-json-format-of-a-crash-report.md#Convert-numeric-values-to-hexadecimal-numbers)。

### Threads

报告在若干对象中包含线程信息，这些对象可以包含以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `frames` | Array | 一个字典数组，描述该线程回溯中的每一帧。栈帧按调用顺序排列，其中第 0 帧是执行停止时正在执行的函数。第 1 帧是调用第 0 帧函数的函数，依此类推。关于该对象属性的说明，请参阅 [Frames](interpreting-the-json-format-of-a-crash-report.md#Frames)。 |
| `id` | Number | 该线程的索引编号。 |
| `queue` | String | 一个字符串，用于标识发生崩溃的线程所属的调度队列（如果适用）。在转换后的报告中，它出现在每个线程回溯上方的标签中、Dispatch Queue 下。 |
| `threadState` | Dictionary | 该线程 CPU 寄存器及其值的 JSON 表示，以及进程终止时其他有用的运行时数据。该对象的结构和属性取决于 `flavor`。在格式化报告中，它出现在所有线程回溯之后的独立小节中。 |
| `triggered` | Boolean | 一个布尔值，如果该线程是引发崩溃的线程，则该值为 `true`。在转换后的报告中，它以 Triggered by Thread 的形式出现。 |

关于如何使用这些信息的详情，请参阅 [Backtraces](examining-the-fields-in-a-crash-report.md#Backtraces) 和 [Thread state](examining-the-fields-in-a-crash-report.md#Thread-state)。

JSON 中帧和线程状态对象里的内存地址数字均以十进制数字表示。要以更常见的十六进制形式查看这些字段中的数字，请参阅 [Convert numeric values to hexadecimal numbers](interpreting-the-json-format-of-a-crash-report.md#Convert-numeric-values-to-hexadecimal-numbers)。

### Frames

报告在若干对象中包含关于帧的信息，这些对象具有以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `imageIndex` | Number | 包含该回溯中此帧正在执行的代码的二进制镜像的索引。`usedImages` 数组中该索引处的对象包含关于该镜像的信息。关于该对象属性的说明，请参阅 [Binary images](interpreting-the-json-format-of-a-crash-report.md#Binary-images)。 |
| `imageOffset` | Number | 从二进制镜像起始位置到当前指令的字节偏移量。如果将该值与二进制镜像列表中的 `base` 值相加，就能得到正在执行的指令的运行时内存地址。对于每个回溯中的第 0 帧，这是进程终止时线程上正在执行的机器指令的地址。对于其他栈帧，这是控制权返回到该栈帧后即将执行的第一条机器指令的地址。这个运行时内存地址就是格式化报告的回溯中，出现在每一帧旁边的值。 |
| `symbol` | String | 在完全符号化的崩溃报告中，这是正在执行的函数的名称。 |
| `symbolLocation` | Number | 距离正在执行指令的入口点的字节数。这就是格式化报告的回溯中，出现在每一帧旁边“+”号之后的值。 |

关于如何使用这些信息的详情，请参阅 [Backtraces](examining-the-fields-in-a-crash-report.md#Backtraces)。

JSON 中内存位置和偏移量的数字均以十进制数字表示。要将这些字段中的数字转换为更常见的十六进制形式，请参阅 [Convert numeric values to hexadecimal numbers](interpreting-the-json-format-of-a-crash-report.md#Convert-numeric-values-to-hexadecimal-numbers)。

### Binary images

报告在若干对象中包含关于进程终止时已加载的二进制镜像的信息，这些对象具有以下属性：

| 键 | 类型 | 描述 |
|---|---|---|
| `arch` | String | 操作系统加载到该进程中的二进制镜像所对应的 CPU 架构。 |
| `base` | Number | 该二进制镜像的加载地址。这是转换后报告中所显示的、已加载镜像内存地址范围的起始位置。 |
| `name` | String | 二进制文件的名称。 |
| `path` | String | 该二进制文件在磁盘上的路径。为保护隐私，macOS 会将可识别用户身份的路径部分替换为占位符值。 |
| `size` | Number | 该镜像的大小。如果将该值与 `base` 值相加，就能得到转换后报告中所显示的、已加载镜像内存地址范围的结束位置。 |
| `source` | String | 一个字符，用于表示该二进制镜像的区域类型：`P`（进程）、`S`（共享缓存）、`C`（共享缓存库）、`K`（内核）、`U`（内核缓存）、`T`（内核 text exec）、`A`（绝对地址）。 |
| `uuid` | String | 一个构建 UUID，唯一标识该二进制镜像，在对崩溃报告进行符号化时，可用它来定位对应的 `dSYM` 文件。更多信息，请参阅 [Building your app to include debugging information](building-your-app-to-include-debugging-information.md)。 |

关于如何使用这些信息的详情，请参阅 [Binary images](examining-the-fields-in-a-crash-report.md#Binary-images)。

### 将数值转换为十六进制数

JSON 将数值存储为十进制数。其中许多数值（例如错误代码和内存地址），在转换后的报告中会以十六进制数的形式出现，以便于理解。

你可以使用以下代码，根据 JSON 中的十进制表示打印出数字的十六进制表示。

```swift
import Foundation

let decimal = 2343432205

print(String(format: "0x%lx", decimal))
// 打印“0x8badf00d”。
```

## 另请参阅

### Crash reports

- [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md) — 将崩溃报告中的十六进制地址替换为与你 App 代码相对应的函数名和行号。
- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md) — 在崩溃报告中查找能识别常见问题的模式，并根据该模式调查问题。
- [Analyzing a crash report](analyzing-a-crash-report.md) — 在崩溃报告中找出有助于诊断问题的线索。
- [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md) — 了解崩溃报告的结构，以及每个字段所包含的信息。
- [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md) — 了解异常类型能告诉你哪些关于你 App 崩溃原因的信息。
