---
title: 从代码生成日志消息
framework: os
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/generating-log-messages-from-your-code
source_url: 'https://developer.apple.com/documentation/os/generating-log-messages-from-your-code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/generating-log-messages-from-your-code.json'
content_hash: 'sha256:467bcc61ccb2ae4d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# 从代码生成日志消息

<sub>文章</sub>

记录有用的调试与分析信息，并在消息中包含动态内容。

## 概述

在代码的合适位置插入日志消息，供之后诊断问题时使用。通常，你会用日志消息来做以下事情：

- 在函数和重要任务的开始和结束处写一条消息。
- 为任何感兴趣的事件写一条消息。
- 发生重大错误时写一条消息。
- 为函数中重要或异常的操作写消息。例如，记录很少被执行到的代码路径。
- 在多步骤任务的每一步之前写一条消息。

消息可以不只是静态字符串。统一日志系统允许你在消息中包含来自 App 的自定义数据，并对这些数据进行格式化，让它们更易读。就像 `fprintf` 一样，你可以把字符串、数字、Objective-C 对象以及来自 App 的其他自定义数据类型直接放进日志消息里。当数据类型包含敏感用户信息时，系统提供了隐私选项，可以在不损失任何过滤能力的情况下隐藏实际值。

### 创建日志对象来组织消息

日志对象负责收集与 App 特定部分相关的消息。生成日志消息时，你要么直接使用、要么配合使用一个你创建的日志对象。你创建哪种日志对象，取决于你用 Swift 还是 Objective-C 编写代码。

- 在 Swift 中，创建一个 [Logger](logger.md) 结构体，并用它的方法生成日志消息。
- 在 Objective-C 中，创建一个 [OSLog](oslog.md) 对象，并把它传给日志记录函数。

为了防止你在诊断问题时，系统显示的日志消息数量多到让人难以招架，每个日志对象都包含两个自定义字符串，帮你过滤掉不相关的消息。创建日志对象时，你要指定这两个字符串，用与你的 App 相关的值：

- 子系统字符串用于标识 App 内一个较大的功能区域。例如，如果你的 App 会衍生出额外的进程，你可能会为每个进程使用不同的字符串。子系统字符串使用反向 DNS 表示法，例如 `com.example.myapp`。
- 分类字符串用于标识给定子系统中某个特定的组件或模块。例如，你可能会为 App 的用户界面、数据模型和网络代码分别定义不同的字符串。这些字符串可以采用你想用的任何约定。

如果你不需要过滤消息，[Logger](logger.md) 和 [OSLog](oslog.md) 提供了一个用于存储消息的默认日志。你可以用这个默认日志来记录那些不需要指定子系统和分类的消息。

### 为每条消息选择合适的日志级别

日志级别定义了某条特定消息的严重程度和重要性，每次记录消息时你都要指定一个日志级别值。你选择的日志级别决定了系统如何处理该消息。系统最初会把所有消息存储在内存中，并把严重程度较高的日志级别的消息写入磁盘。下表按严重程度递增的顺序列出了各个日志级别。

| 日志级别 | 是否持久化到磁盘 | 说明 |
|---|---|---|
| Debug | 否 | 捕获开发期间产生的详细信息，这些信息只在调试代码时有用。 |
| Info | 仅当用 log 工具收集时 | 捕获对排查问题有帮助、但非必需的信息。 |
| Notice（默认） | 是，存储量有上限 | 捕获排查问题所必需的信息。例如，捕获可能导致失败的信息。 |
| Error | 是，存储量有上限 | 捕获代码执行期间出现的错误。如果存在活动对象，系统会捕获相关进程链的信息。 |
| Fault | 是，存储量有上限 | 捕获代码中故障和 bug 的相关信息。如果存在活动对象，系统会捕获相关进程链的信息。 |

通常情况下，系统只把 debug 和 info 消息存储在内存里，但你可以用 `log` 命令行工具把 info 消息写入磁盘。对于其他类型的消息，系统会把它们压缩后写入磁盘上的数据存储区。当该数据存储区超出预定大小时，系统会清除旧消息，为新消息腾出空间。

> [!note] 注意
> 你可以使用工具或自定义配置描述文件，覆盖每个日志级别的默认存储行为。有关具体做法，参见 [Customizing Logging Behavior While Debugging](customizing-logging-behavior-while-debugging.md)。

日志级别的严重程度会影响系统记录信息的速度。debug 日志的开销非常低，因为系统只把它们存储在内存里。故障和其他严重程度更高的消息会带来更多开销，因为系统通常需要捕获额外信息，并把所有这些信息都写入磁盘。

### 生成一条日志消息

要生成一条日志消息：

- 在 Swift 中，在 macOS 11 及更高版本上调用 [Logger](logger.md) 结构体的相应方法。在更早版本的 macOS 上，调用 `os_log(_:log:type:)`，或调用其他以 [OSLog](oslog.md) 对象为参数的相关日志记录函数。
- 在 Objective-C 代码中，调用 [os_log](os_log.md)，或调用以 [os_log_t](os-log-t.md) 类型为参数的等效函数。

最简单的日志消息类型只包含静态文本。你可以用这类消息报告特定事件，或者在任何不需要在消息中包含程序变量的场合使用。下面的示例展示了几种记录纯静态文本消息的方式。前两个示例把消息添加到默认日志，第三个示例则把一条错误消息添加到自定义日志对象。

```swift
// Log a message to the default log and default log level.os_log(OS_LOG_DEFAULT, "This is a default message.");
    
// Log a message to the default log and debug log level
os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG, "This is a debug message.");
    
// Log an error to a custom log object.
os_log_t customLog = os_log_create("com.your_company.your_subsystem", "your_category_name");
os_log_with_type(customLog, OS_LOG_TYPE_ERROR, "An error occurred!");

```

### 在日志消息中包含自定义数据值

消息字符串里可以包含程序变量的内容。具体怎么包含这些变量，取决于你使用的编程语言：

- 在 Swift 中，向消息字符串添加形如 `\(variableName)` 的插值变量。
- 在 Objective-C 中，添加格式字符串说明符，例如 `%@` 和 `%d`。

下面的示例展示了几条包含不同类型变量的日志消息。在 macOS 11 及更高版本上，可以直接在消息字符串里把 Swift 变量指定为插值。否则，就使用格式字符串说明符和一个可变参数列表来指定值。要在 Objective-C 中记录来自指针的原始字节，使用 `%.*P` 格式修饰符。

```swift
os_log_t customLog = os_log_create("com.your_company.your_subsystem", "your_category_name");
int itemCount = [self getItemCount];
NSString* selectedColor = [self getSelectedColor];
char* pointer = "Hello world";
    
os_log(customLog, "The array contains %d items", itemCount);
os_log(customLog, "The user selected the color %@", selectedColor);

// Log raw bytes from a pointer.
os_log(customLog, "%.*P", 11, pointer);
```

### 在消息字符串中格式化自定义值

统一日志系统会按照默认设置格式化 Swift 插值变量，但你也可以对变量应用自定义格式，让它们更易读。具体来说，你可以：

- 指定变量的宽度，并在该空间内对齐变量的文本。
- 把整数格式化为[十进制](oslogintegerformatting/decimal.md)、[十六进制](oslogintegerformatting/hex.md)或[八进制](oslogintegerformatting/octal.md)数字。
- 用[定点](oslogfloatformatting/fixed.md)、[十六进制](oslogfloatformatting/hex.md)、[指数](oslogfloatformatting/exponential.md)或[混合](oslogfloatformatting/hybrid.md)记数法格式化浮点数。
- 把布尔值格式化为 true/false 或 yes/no 字符串。
- 指定浮点数的精度。
- 指定数字的最小位数。
- 指定数字是否包含显式的正负号。
- 记录指针中包含的二进制数据。

要为插值指定格式化选项，包含相应的格式参数和值。在下面的示例中，第一条日志消息包含对齐参数，用于设置列宽以及该列内的对齐方式。第二条日志消息把一个浮点数格式化为包含额外精度位数，并在正数前加上正号。第三条日志消息把一个布尔值格式化为对某个问题的 yes/no 回答。

```swift
let shapeType: String = getShapeType()
let selectedColor: String = getSelectedColor()
let bigNumber = 1.0234e30
let theAnswer = true

// Apply custom formatting to variables.
customLog.debug("Shape type: \(shapeType, align: .right(columns: 15)) Color: \(selectedColor, align: .left(columns: 10))")
customLog.info("The big number is \(bigNumber, format: .exponential(precision: 10, explicitPositiveSign: true, uppercase: false) )")
customLog.debug("The answer is \(theAnswer, format: .answer)")
```

除了上述格式化选项之外，统一日志系统还支持自定义的格式修饰符。在 Swift 中，用 `format` 参数指定它们。在 Objective-C 中，使用形如 `%{value_type}d` 的修饰符。每个修饰符都会按对应的具体类型格式化数据。要格式化二进制数据类型，使用 `%.*P` 说明符，并把字节总数和指针作为参数传给函数。下表列出了内置的格式说明符。

| 值类型 | 自定义说明符 | 示例输出 |
|---|---|---|
| `time_t` | `%{time_t}d` | `2016-01-12 19:41:37` |
| `timeval` | `%{timeval}.*P` | `2016-01-12 19:41:37.774236` |
| `timespec` | `%{timespec}.*P` | `2016-01-12 19:41:37.2382382823` |
| `errno` | `%{errno}d` | `Broken pipe` |
| `iec-bytes` | `%{iec-bytes}d` | `2.64 MiB` |
| `bitrate` | `%{bitrate}d` | `123 kbps` |
| `iec-bitrate` | `%{iec-bitrate}d` | `118 Kibps` |
| `uuid_t` | `%{uuid_t}.*16P` ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `%{uuid_t}.*P` | `10742E39-0657-41F8-AB99-878C5EC2DCAA` |

下面的示例展示了如何格式化自定义比特率和一个 UUID 结构体。

```objc
os_log_t customLog = os_log_create("com.your_company.your_subsystem", "your_category_name");
int baudRate = [self getBaudRate];
uuid_t* uuid = [self getItemUUID];

os_log(customLog, "The baud rate is %{bitrate}d", baudRate);
os_log(customLog, "The UUID is %{uuid}.*P", (int)sizeof(uuid_t), uuid);
```

有关格式化值时可用选项的信息，参见 [OSLogStringAlignment](oslogstringalignment.md)、[OSLogIntegerFormatting](oslogintegerformatting.md)、[OSLogFloatFormatting](oslogfloatformatting.md)、[OSLogBoolFormat](oslogboolformat.md)、[OSLogInt32ExtendedFormat](oslogint32extendedformat.md) 和 [OSLogPointerFormat](oslogpointerformat.md)。

### 从日志消息中隐去敏感用户数据

包含敏感用户数据的日志消息会给用户带来潜在的问题，因为任何能访问日志或用户计算机的人都能看到这些信息。为保护用户隐私，尽量把日志消息限制为你自己定义的静态字符串和数字。如果必须在消息中包含动态生成的数据，就要隐去任何包含敏感用户信息的值。

统一日志系统使用隐私选项来隐藏或显示消息里的插值变量。默认情况下，系统不会隐去整数、浮点数和布尔值，但会隐去动态字符串和复杂动态对象的内容。要让一个私有值重新变为公开，在消息字符串或插值变量中用相应的修饰符配置该变量的隐私性。例如，下面的代码展示了如何用 [public](oslogprivacy/public.md) 修饰符让一个动态字符串重新可见：

```swift
// Make the smoothie name visible, because it’s not sensitive data.
os_log_t customLog = os_log_create("com.your_company.your_subsystem", "your_category_name");
os_log(customLog, "Smoothie name: %{public}s ", smoothieName);
```

当你知道某个变量可能包含敏感用户信息时，像下面的示例这样，显式地把它标记为 [private](oslogprivacy/private.md)：

```swift
int userAge = getUserAge();
os_log_t customLog = os_log_create("com.your_company.your_subsystem", "your_category_name");

// Hide the user’s age in the log entry. 
os_log(customLog, "User's age: %{private}d ", userAge);
```

要诊断某些问题，你可能需要识别出几条日志消息是否都指向同一份用户数据。例如，在诊断某个特定用户账户的问题时，你可能想看到与该账号相关的所有日志消息。为了在保留这种能力的同时仍然保护用户隐私，用 [OSLogPrivacy.Mask.hash](oslogprivacy/mask/hash.md) 值配置你的隐私设置，如下面的示例所示：

```swift
// Hide the user’s account number, but include a hash mask to allow
// the correlation of this log message with others for the same account.
os_log_t customLog = os_log_create("com.your_company.your_subsystem", "your_category_name");
os_log(customLog, "Start transaction for account: %{mask.hash}d ", accountNumber);
```

包含 [OSLogPrivacy.Mask.hash](oslogprivacy/mask/hash.md) 选项，会用一个对当前进程唯一的哈希值取代通用的隐去文本。[OSLogPrivacy.Mask.hash](oslogprivacy/mask/hash.md) 值与被隐去的值一一对应，但不提供任何能识别该值本身的信息。

## 另请参阅

### 基础

- [Viewing Log Messages](viewing-log-messages.md) — 使用各种工具获取日志信息。
- [Customizing Logging Behavior While Debugging](customizing-logging-behavior-while-debugging.md) — 控制记录哪些日志事件。
