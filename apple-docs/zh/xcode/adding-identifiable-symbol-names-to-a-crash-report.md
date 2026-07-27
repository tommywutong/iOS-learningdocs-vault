---
title: 为崩溃报告添加可识别的符号名称
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/adding-identifiable-symbol-names-to-a-crash-report
source_url: 'https://developer.apple.com/documentation/xcode/adding-identifiable-symbol-names-to-a-crash-report'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/adding-identifiable-symbol-names-to-a-crash-report.json'
content_hash: 'sha256:32bceea4bf6a188d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md)

# 为崩溃报告添加可识别的符号名称

<sub>文章</sub>

用与你 App 代码相对应的函数名和行号，替换崩溃报告中的十六进制地址。

## 概述

当某个 App 崩溃时，操作系统会收集有关该 App 在崩溃时正在做什么的诊断信息。崩溃报告中最重要的部分之一，是以十六进制地址形式报告的线程调用栈回溯（backtrace）。你需要将这些线程调用栈回溯转换成源代码中可读的函数名和行号，这个过程称为 _符号化（symbolication）_，然后使用这些信息来理解你的 App 为什么会崩溃。在很多情况下，Xcode 中的 Crashes organizer 会替你[自动对崩溃报告进行符号化](https://help.apple.com/xcode/mac/current/#/dev709125d2e)。

### 判断崩溃报告是否已符号化

要使用崩溃报告诊断某个 App 问题，你需要一份完全符号化或部分符号化的崩溃报告。未经符号化的崩溃报告很少有用。

完全符号化的崩溃报告在调用栈回溯的每一帧上都有函数名，而不是十六进制内存地址。每一帧代表当前在某个特定线程上运行的一次函数调用，展示了你 App 崩溃那一刻，来自你 App 和操作系统框架中正在执行的各个函数。完全符号化的崩溃报告能为你提供关于该崩溃的最多信息。一旦你拿到一份完全符号化的崩溃报告，请查阅 [Analyzing a crash report](analyzing-a-crash-report.md) 了解如何确定崩溃的根源。

以下是一份完全符号化的崩溃报告示例：

```other
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   libswiftCore.dylib                0x00000001bd38da70 specialized _fatalErrorMessage+ 2378352 (_:_:file:line:flags:) + 384
1   libswiftCore.dylib                0x00000001bd38da70 specialized _fatalErrorMessage+ 2378352 (_:_:file:line:flags:) + 384
2   libswiftCore.dylib                0x00000001bd15958c _ArrayBuffer._checkInoutAndNativeTypeCheckedBounds+ 66956 (_:wasNativeTypeChecked:) + 200
3   libswiftCore.dylib                0x00000001bd15c814 Array.subscript.getter + 88
4   TouchCanvas                       0x00000001022cbfa8 Line.updateRectForExistingPoint(_:) (in TouchCanvas) + 656
5   TouchCanvas                       0x00000001022c90b0 Line.updateWithTouch(_:) (in TouchCanvas) + 464
6   TouchCanvas                       0x00000001022e7374 CanvasView.updateEstimatedPropertiesForTouches(_:) (in TouchCanvas) + 708
7   TouchCanvas                       0x00000001022df754 ViewController.touchesEstimatedPropertiesUpdated(_:) (in TouchCanvas) + 304
8   TouchCanvas                       0x00000001022df7e8 @objc ViewController.touchesEstimatedPropertiesUpdated(_:) (in TouchCanvas) + 120
9   UIKitCore                         0x00000001b3da6230 forwardMethod1 + 136
10  UIKitCore                         0x00000001b3da6230 forwardMethod1 + 136
11  UIKitCore                         0x00000001b3e01e24 -[_UIEstimatedTouchRecord dispatchUpdateWithPressure:stillEstimated:] + 340
```

部分符号化的崩溃报告中，调用栈回溯的部分帧有函数名，另一些帧则是十六进制地址。根据崩溃的类型以及调用栈回溯中哪些帧被符号化，部分符号化的崩溃报告可能已经包含足够理解该崩溃的信息。不过，你仍然应该[在 Xcode 中符号化崩溃报告](adding-identifiable-symbol-names-to-a-crash-report.md#Symbolicate-the-crash-report-in-Xcode)，让报告变得完全符号化，这样你才能完整地理解该崩溃。

以下是一份部分符号化的崩溃报告示例：

```other
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   libswiftCore.dylib                0x00000001bd38da70 specialized _fatalErrorMessage+ 2378352 (_:_:file:line:flags:) + 384
1   libswiftCore.dylib                0x00000001bd38da70 specialized _fatalErrorMessage+ 2378352 (_:_:file:line:flags:) + 384
2   libswiftCore.dylib                0x00000001bd15958c _ArrayBuffer._checkInoutAndNativeTypeCheckedBounds+ 66956 (_:wasNativeTypeChecked:) + 200
3   libswiftCore.dylib                0x00000001bd15c814 Array.subscript.getter + 88
4   TouchCanvas                       0x00000001022cbfa8 0x1022c0000 + 49064
5   TouchCanvas                       0x00000001022c90b0 0x1022c0000 + 37040
6   TouchCanvas                       0x00000001022e7374 0x1022c0000 + 160628
7   TouchCanvas                       0x00000001022df754 0x1022c0000 + 128852
8   TouchCanvas                       0x00000001022df7e8 0x1022c0000 + 129000
9   UIKitCore                         0x00000001b3da6230 forwardMethod1 + 136
10  UIKitCore                         0x00000001b3da6230 forwardMethod1 + 136
11  UIKitCore                         0x00000001b3e01e24 -[_UIEstimatedTouchRecord dispatchUpdateWithPressure:stillEstimated:] + 340
```

未经符号化的崩溃报告，包含的是已加载二进制映像中可执行代码的十六进制地址。这类报告的调用栈回溯中不包含任何函数名。由于未经符号化的崩溃报告很少有用，请[在 Xcode 中符号化崩溃报告](adding-identifiable-symbol-names-to-a-crash-report.md#Symbolicate-the-crash-report-in-Xcode)。

以下是一份未经符号化的崩溃报告示例：

```other
Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   libswiftCore.dylib                0x00000001bd38da70 0x1bd149000 + 2378352
1   libswiftCore.dylib                0x00000001bd38da70 0x1bd149000 + 2378352
2   libswiftCore.dylib                0x00000001bd15958c 0x1bd149000 + 66956
3   libswiftCore.dylib                0x00000001bd15c814 0x1bd149000 + 79892
4   TouchCanvas                       0x00000001022cbfa8 0x1022c0000 + 49064
5   TouchCanvas                       0x00000001022c90b0 0x1022c0000 + 37040
6   TouchCanvas                       0x00000001022e7374 0x1022c0000 + 160628
7   TouchCanvas                       0x00000001022df754 0x1022c0000 + 128852
8   TouchCanvas                       0x00000001022df7e8 0x1022c0000 + 129000
9   UIKitCore                         0x00000001b3da6230 0x1b3348000 + 10871344
10  UIKitCore                         0x00000001b3da6230 0x1b3348000 + 10871344
11  UIKitCore                         0x00000001b3e01e24 0x1b3348000 + 11247140
```

### 在 Xcode 中符号化崩溃报告

Xcode 是符号化崩溃报告的首选方式，因为它会一次性使用你 Mac 上所有可用的 `dSYM` 文件。对于一些特殊的调试场景——例如你在 Xcode 调试器中有一份未经符号化的栈回溯，却没有完整的崩溃报告——你可以[使用命令行符号化崩溃报告](adding-identifiable-symbol-names-to-a-crash-report.md#Symbolicate-the-crash-report-with-the-command-line)来逐帧符号化。

要在 Xcode 中进行符号化，请点按 [Devices and Simulators 窗口](https://help.apple.com/xcode/mac/current/#/dev85c64ec79)中的 Device Logs 按钮，然后将崩溃报告文件拖放到设备日志列表中。

> [!important] 重要
> 崩溃报告必须具有 `.crash` 文件扩展名。如果某份崩溃报告没有文件扩展名，或者具有 `.txt` 之类的其他文件扩展名，请在符号化之前将其重命名为 `.crash` 扩展名。

如果该崩溃报告没有被符号化，或者只被部分符号化，说明 Xcode 无法定位到匹配的符号信息，你需要通过以下方式获取符号信息：

- 如果操作系统的框架没有被符号化，你需要与崩溃报告中记录的操作系统版本相匹配的设备符号信息。要解决这个问题，请参阅[获取设备符号信息](adding-identifiable-symbol-names-to-a-crash-report.md#Acquire-device-symbol-information)。
- 如果你 App、App 扩展或框架对应的帧没有被符号化，你需要使用聚焦（Spotlight）找到现有的 `dSYM` 文件。要解决这个问题，请参阅[使用聚焦查找 dSYM](adding-identifiable-symbol-names-to-a-crash-report.md#Locate-a-dSYM-using-Spotlight)。如果你的 App 使用了由第三方构建的框架，你可能需要向该框架的提供方索要 `dSYM` 文件。

一旦你拿到一份完全符号化的崩溃报告，请查阅 [Analyzing a crash report](analyzing-a-crash-report.md) 来确定该崩溃的根源。

### 获取设备符号信息

要让崩溃报告中来自操作系统框架的符号变得可识别，你需要从某台设备收集系统框架的符号。对于 iOS、iPadOS、tvOS、visionOS 和 watchOS App，Xcode 会自动从你连接到 Mac 的每台设备中拷贝操作系统符号。对于 macOS 和 Mac Catalyst App，请在一个 macOS 版本与崩溃报告中所列 macOS 版本相匹配的 Mac 上，使用 Xcode 对崩溃日志进行符号化。

系统框架的符号是特定于操作系统版本和设备 CPU 架构的。例如，运行 iOS 13.1.0 的 iPhone 所对应的符号，与运行 iOS 13.1.2 的同一台 iPhone 所对应的符号并不相同。如果你的 App 运行在支持多种 CPU 架构（例如 `arm64` 和 `arm64e`）的操作系统版本上，一台 `arm64` 架构的设备只会包含该操作系统框架 `arm64` 版本的符号；而不会有 `arm64e` 设备上操作系统框架的符号。

### 使用聚焦查找 dSYM

要判断你符号化某个二进制文件的十六进制地址所需的 `dSYM` 文件，是否存在于你的 Mac 上：

1. 在调用栈回溯中找到一个没有被符号化的帧。记下第二列中的二进制映像名称。
2. 在崩溃报告底部的二进制映像列表中，查找具有该名称的二进制映像。该列表包含了崩溃发生时加载到该进程中的每个二进制映像的构建 UUID。使用 `grep` 命令行工具在二进制映像列表中查找该条目：

  ```other
  % grep --after-context=1000 "Binary Images:" <Path to Crash Report> | grep <Binary Name>
  ```

从二进制映像部分获取到构建 UUID 之后：

1. 将该二进制映像的构建 UUID 转换为一个 32 字符的字符串，按 8-4-4-4-12 分组，用连字符分隔（`XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`）。所有字母都必须大写。
2. 使用 `mdfind` 命令行工具查询（包括引号）该构建 UUID：

  ```other
  % mdfind "com_apple_xcode_dsym_uuids == <UUID>"
  ```

如果聚焦找到了与该构建 UUID 对应的 `dSYM` 文件，`mdfind` 会打印出该 `dSYM` 文件的路径。

![一份崩溃报告，其中高亮了使用 mdfind 命令查找 dSYM 文件所需的信息。](../../../attachments/d6a714a368a5151118ff291b7c3ab963/adding-identifiable-symbol-names-to-a-crash-report-1@2x.png)

使用这个示例中的信息，查找 `dSYM` 的命令是：

```other
% grep --after-context=1000 "Binary Images:" <Path to Crash Report> | grep TouchCanvas
0x1022c0000 - 0x1022effff TouchCanvas arm64  <9cc89c5e55163f4ab40c5821e99f05c6>

% mdfind "com_apple_xcode_dsym_uuids == 9CC89C5E-5516-3F4A-B40C-5821E99F05C6"
```

找到 `dSYM` 文件后，请[核对构建 UUID](adding-identifiable-symbol-names-to-a-crash-report.md#Match-build-UUIDs)，确认其构建 UUID 与该二进制映像的构建 UUID 相匹配。确认构建 UUID 匹配之后，再[在 Xcode 中符号化崩溃报告](adding-identifiable-symbol-names-to-a-crash-report.md#Symbolicate-the-crash-report-in-Xcode)，或[使用命令行符号化崩溃报告](adding-identifiable-symbol-names-to-a-crash-report.md#Symbolicate-the-crash-report-with-the-command-line)。

如果聚焦没有找到匹配的 `dSYM`，`mdfind` 就不会打印任何内容，此时你需要：

- 确认你是否仍然保留着崩溃所对应的那个 App 版本的 Xcode 归档。如果你已经没有这份归档，就无法符号化该版本 App 的栈帧。为了将来避免这个问题，请在发布 App 新版本时保留该版本的 Xcode 归档。这样你之后就能够为你 App 的新版本符号化崩溃报告。
- 确保 Xcode 归档位于聚焦能够找到的位置，例如你 macOS 的主目录。
- 确认你的构建生成了调试信息。参阅 [Building your app to include debugging information](building-your-app-to-include-debugging-information.md)。

### 核对构建 UUID

如果你有一个二进制文件或 `dSYM`，认为可以用来符号化某份崩溃报告，请使用 `dwarfdump` 命令确认它们的构建 UUID 是否匹配。如果构建 UUID 彼此不匹配，或者与崩溃报告 Binary Images 部分列出的构建 UUID 不匹配，你就不能用这些文件来符号化该崩溃报告。

```other
% dwarfdump --uuid <PathToDSYMFile>/Contents/Resources/DWARF/<BinaryName>
% dwarfdump --uuid <PathToBinary>
```

### 使用命令行符号化崩溃报告

对于一些特殊的调试场景——例如符号化 LLDB 命令行提供的部分调用栈回溯——你可以使用 `atos` 命令来符号化崩溃报告。如果符号信息可用，`atos` 命令会将十六进制地址转换为源代码中可识别的函数名和行号。要使用 `atos` 进行符号化：

1. 在调用栈回溯中找到你想要符号化的帧。记下第二列中的二进制映像名称，以及第三列中的地址。
2. 在崩溃报告底部的二进制映像列表中，查找具有该名称的二进制映像。记下该二进制映像的架构和加载地址。
3. 找到该二进制文件对应的 `dSYM` 文件。如果你不知道 `dSYM` 文件位于何处，请参阅[使用聚焦查找 dSYM](adding-identifiable-symbol-names-to-a-crash-report.md#Locate-a-dSYM-using-Spotlight)，找到与该二进制映像构建 UUID 相匹配的 `dSYM` 文件。
4. 使用前面步骤中收集到的信息，代入公式，用 `atos` 符号化调用栈回溯中的地址：

```other
% atos -arch <BinaryArchitecture> -o <PathToDSYMFile>/Contents/Resources/DWARF/<BinaryName>  -l <LoadAddress> <AddressesToSymbolicate>
```

> [!note] 注意
> `dSYM` 文件是包含调试符号文件的 macOS bundle。调用 `atos` 时，你必须提供该 bundle 内部这个文件的路径，而不能只提供外层 `dSYM` bundle 的路径。

举个例子，看看这份崩溃报告中高亮的部分：

![一份崩溃报告，其中高亮了使用 atos 符号化某一帧所需的信息。](../../../attachments/8bfc0ce425495f4fad7e0e498094b48c/adding-identifiable-symbol-names-to-a-crash-report-2@2x.png)

使用这个示例中的信息，完整的 `atos` 命令及其输出为：

```other
% atos -arch arm64 -o TouchCanvas.app.dSYM/Contents/Resources/DWARF/TouchCanvas -l 0x1022c0000 0x00000001022df754
ViewController.touchesEstimatedPropertiesUpdated(_:) (in TouchCanvas) + 304
```

一旦你通过 `atos` 拿到了至少部分符号化的崩溃报告，请查阅 [Analyzing a crash report](analyzing-a-crash-report.md) 获取用于确定该崩溃根源的信息。

## 另请参阅

### 崩溃报告

- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md) — 在崩溃报告中找出能识别常见问题的模式，并根据该模式调查问题。
- [Analyzing a crash report](analyzing-a-crash-report.md) — 在崩溃报告中找出有助于你诊断问题的线索。
- [Examining the fields in a crash report](examining-the-fields-in-a-crash-report.md) — 了解崩溃报告的结构，以及每个字段所包含的信息。
- [Interpreting the JSON format of a crash report](interpreting-the-json-format-of-a-crash-report.md) — 了解系统在崩溃报告的 JSON 中包含的各个对象的结构和属性。
- [Understanding the exception types in a crash report](understanding-the-exception-types-in-a-crash-report.md) — 了解异常类型能告诉你哪些有关 App 崩溃原因的信息。
