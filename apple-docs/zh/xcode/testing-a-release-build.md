---
title: 测试发布版本
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/testing-a-release-build
source_url: 'https://developer.apple.com/documentation/xcode/testing-a-release-build'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/testing-a-release-build.json'
content_hash: 'sha256:b55fed34102bbb08'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [分发](distribution.md)

# 测试发布版本

<sub>文章</sub>

在模拟的用户环境中运行你的 App，以发现和识别部署错误。

## 概述

为确保你的 App 在部署中正常工作，请在提交 App 或 App 更新以供审核，或分发给企业用户之前，在各种条件下测试你的发布版本（release build）。为了捕获开发过程中可能不会出现的常见错误或边界情况，请考虑开发环境调试构建（debug build）与用户环境发布构建之间的差异，如下所示。

![](../../../attachments/3b599c4e9dab6ada95c47be8fdfc26d2/testing-a-release-build-1@2x.png)

<sub>比较 App 运行的两种环境（开发环境与用户环境）的示意图。底部是一个标题为“开发环境”的框，其中包含一个标记为“调试构建”的节点。顶部是一个标题为“用户环境”的框，其中包含一个流程图，从标记为“发布构建”的节点开始。从根节点流出两个节点：左侧节点标记为“企业或 Ad Hoc 签名”，右侧节点标记为“App Store 签名”。从左侧节点流出一个节点，标记为“企业或 Ad Hoc”。从右侧节点流出三个节点；左侧节点显示为“TestFlight”，中间节点显示为“App Review”，右侧节点显示为“App Store”。</sub>

App 可能在特定用户的设备上因各种原因表现出不同的行为。不同的设备和操作系统版本提供不同的软件功能，而 App 更新涉及数据迁移、钥匙串访问或全新安装 App 时不存在的默认数据。在设备电量不足、系统内存有限或网络不可用时，可能会导致功能被禁用、帧率受限制或其他延迟。Xcode 允许开发构建和发布构建设置不同，并禁用了看门狗超时。

### 创建 Xcode 归档

要测试你的 App 用户所经历的确切条件，请创建一个发布构建。在你的 Xcode 项目 scheme 编辑器中，将运行目标设置为某个设备，并将归档任务调整为 Release 配置。

![](../../../attachments/ded54c375ee52453d7e0090450c5956e/testing-a-release-build-2@2x.png)

<sub>Xcode 项目 scheme 编辑器的屏幕截图。左侧的导览列表反映已选择了“归档”任务。右侧的详细信息窗格显示了运行目标设置为通用的“任意 iOS 设备”设置。构建配置选择菜单反映了选定的“Release”选项。</sub>

然后，在 Xcode 的“Product”菜单中选择“Archive”选项。归档构建完成后，将显示 Organizer。有关创建 App 归档的更多信息，请参阅[为 Beta 测试和发布分发你的 App](distributing-your-app-for-beta-testing-and-releases.md)。

Xcode 会将 App 归档保存在磁盘上，以便你以后可以引用特定的构建，例如，在 App 通过 Beta 测试后将构建提交给 App Review。归档的分发工作流程提供了几种测试 App 的方法：

- **TestFlight** — TestFlight 自动化了 App 分发和提交流程，以减少将错误构建提交给 App Review 的可能性。要通过 TestFlight 分发 App 归档，请选择归档窗格中的“App Store Connect”选项。有关 TestFlight 的更多信息，请参阅[为 Beta 测试和发布分发你的 App](distributing-your-app-for-beta-testing-and-releases.md)。
- **Ad Hoc** — 要手动将你的 App 分发给测试人员，例如通过电子邮件向他们发送 .ipa 文件，请选择归档窗格中的“Ad Hoc”选项。有关更多信息，请参阅[向已注册设备分发你的 App](distributing-your-app-to-registered-devices.md)。
- **企业分发** — 企业分发与 Ad Hoc 分发类似，不同之处在于你从归档窗格中选择“Enterprise”选项。Xcode 会为企业 App 分发查找不同的代码签名身份，其中包含有效的企业分发证书。
- **开发** — 开发分发方法使用你的开发凭据对发布构建进行签名。如果你无法访问团队分发身份，此选项可启用测试。调试器可以附加到使用开发凭据签名的发布构建，但请注意，它可能会掩盖看门狗超时。

对于除 TestFlight 之外的所有分发方法，请选择以下选项以提高发现仅在发布构建中出现的 Bug 的几率：

- 将“App Thinning”设置为“所有兼容设备变体”。

分发后你可以访问 App 归档，以调试用户报告的错误。如果问题未在 Beta 测试中出现，请参考崩溃日志和 App 日志来追踪原因；请参阅[使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md)。要尝试重现该问题，请检查崩溃日志中的构建版本（请参阅[检查崩溃报告中的字段](examining-the-fields-in-a-crash-report.md)中的“Version”字段），并测试来自具有匹配版本的 App 归档的发布构建。

### 比较构建配置设置

Xcode 项目的构建设置支持基于活动构建配置的不同值。默认的构建配置是 Debug 和 Release，项目 scheme 会分别将它们映射到“运行”任务和“归档”任务。由于归档任务创建发布构建，因此发布构建的行为可能与开发人员在调试器中运行的构建在构建设置方面有所不同。

默认情况下，大多数构建设置在两种配置中是一致的。要检查差异，请仔细检查目标的构建设置。当某个设置在配置之间变化时，Xcode 会显示“<多个值>”。要查看每个值，请展开该设置的展开三角形。

![](../../../attachments/c6de41d1a11b5a9e8f3c4356aeb13dc1/testing-a-release-build-4@2x.png)

<sub>Xcode 项目构建设置的屏幕截图。“Packaging”部分已展开，显示了一个选中的设置，标题为“Info.plist File”。“Info.plist File”构建设置已展开，显示了两条子设置。上面的子设置标题为“Debug”，值为“MyApp/Info.plist”。下面的子设置标题为“Release”，值为“MyApp/Info-Release.plist”。</sub>

为了确保 App 的行为在构建配置之间按预期有所不同，请花点时间考虑每个差异在每个设置上的全部影响。在上图中，App 为发布构建定义了一个不同的 `Info.plist`。

### 断开调试器

当 Xcode 启动 App 时，它会启用一个调试器，这会创建一些与用户体验不同的差异：

- Xcode 调试器会禁用看门狗终止，这可能会阻止测试人员在 Xcode 中运行 App 时观察到挂起问题。检查看门狗终止的最简单方法是从开发机器上断开设备，然后从主屏幕启动 App。有关看门狗终止的更多信息，请参阅[处理看门狗终止](addressing-watchdog-terminations.md)。
- Xcode 的调试器会阻止 App 被挂起，因此请从主屏幕启动你的 App 以测试后台进程。例如，NSURLSession 实现了后台会话，但当 App 在 Xcode 调试器中运行时，后台会话永远不会运行。

### 测试全新安装和 App 更新

Xcode 在开发期间通过增量更新 App 来优化构建和安装。因此，随着你的 App 代码在开发期间的更改，由先前构建创建的过时存储数据可能会残留，除非你完全清除先前的安装。即使 App 可能不再创建这些过时数据，访问这些数据也可能导致 App 在测试期间的行为与用户体验的不同。为了防止这种临时依赖性，请在开发期间移除 App，以确保 Xcode 安装全新构建。当你移除 App 时，请选择同时移除 App 的先前数据。

有两个例外：

- 只要组中的任一 App 已安装，系统就会保留设备上的 App Group 数据。要从 App Group 容器中移除可能过时的测试数据，请移除所有共享该组的 App。
- 即使你删除 App 后，系统也会在设备上保留 App 的钥匙串数据。要清除钥匙串，请使用 [SecItemDelete(_:)](<../security/secitemdelete(__).md>)。如果你创建了一个用于移除钥匙串数据的独立实用工具，则该实用工具和 App 需要共享相同的应用程序标识符。

如果发布构建更新了你 App 的先前版本，则某些用户的设备上可能已安装该先前版本。当你的 App 更新旨在支持由先前版本创建的数据时，请测试 App 更新以防止任何衰退。例如，如果更新的 App 更改了文件格式或迁移了先前数据（例如，使用 Core Data 迁移；请参阅[自动迁移你的数据模型](../coredata/migrating-your-data-model-automatically.md)），请测试 App 更新场景以确保新 App 正确处理先前 App 数据。

### 在各种设备和操作系统版本上运行 App

错误可能仅出现在特定设备、特定操作系统版本或两者的特定组合上。为确保一致的用户体验，请在你 App 支持的大范围设备和操作系统版本上进行测试。

在诊断用户报告的问题时，请注意用户的设备和操作系统版本。请参阅[检查崩溃报告中的字段](examining-the-fields-in-a-crash-report.md)中的 `Hardware Model` 和 `OS Version`。要重现用户报告的问题，请维护一个涵盖不同设备型号和操作系统版本的强大测试设备套件。虽然可以在模拟器（Simulator）中运行发布构建，但请将模拟器视为用户不会使用的独立设备。因此，始终在真实设备上测试发布构建。

> [!tip] 提示
> 提高你的 App 的部署目标会减少需要测试的设备型号和操作系统版本的组合数量。如果测试所有组合难以管理，你可以通过提高部署目标来减少你的 App 支持的设备数量，从而也减少需要测试的设备数量。

### 检查文件系统访问权限

在 macOS 上，根据其用户帐户权限，用户可能具有不同级别的文件系统访问权限。测试用户帐户权限在你的 App 中所造成差异的一种方法是以访客用户身份运行 App。在访达的“显示简介”窗格中，访客用户的文件系统权限属于 `everyone` 类别。默认情况下，`everyone` 的文件系统访问级别与默认的管理员访问级别不同。

![](../../../attachments/8e7c3fd5a1931e74c61ef09a4bd549d0/testing-a-release-build-5@2x.png)

<sub>文件“显示简介”窗格的屏幕截图。“共享与权限”部分已展开，显示了一个包含两列（“名称”和“权限”）的表格。该表格包含三行数据。第一行显示名称为“johnas (Me)”，权限为“读与写”。第二行显示名称为“staff”，权限为“只读”。第三行显示名称为“everyone”，权限为“只读”。</sub>

### 确保网络兼容性

调试构建通常在开发期间的隔离网络中运行，而发布构建则访问为 App 用户服务的各种网络。你的 App 可能在某个特定网络中出现问题，而在另一个网络中没有，例如由于网络拥塞或网络类型（如 IPv6 与 IPv4）的原因。

- 如果开发人员和 Beta 测试者在 IPv4 网络中运行 App，请务必也测试 IPv6 连接，以捕获任何与 DNS64 或 NAT64 相关的潜在问题。
- 要在 iOS 上模拟缓慢或不可靠的互联网连接，你可以使用 Network Link Conditioner。通过“设置”App >“开发者”>“Network Link Conditioner”选项启用此功能。
- 要调试高级 HTTP 问题，请使用 HTTP 调试代理运行你的发布构建；请参阅[选择网络调试工具](../network/choosing-a-network-debugging-tool.md)。对于低级问题，如 TCP 连接或 DNS 故障，请检查网络级活动以查找原因；请参阅[记录数据包跟踪](../network/recording-a-packet-trace.md)。
- 要调试丢失的网络连接，请通过查看你的服务器端日志来确保网络连接能够到达目的地且沿途没有中断。对于私有网络，请考虑防火墙配置、网络代理或负载均衡器可能造成的阻塞。

某些网络错误是不可避免的，例如在服务器或网络停机期间。确保你的 App 在网络运行异常时为用户提供清晰的操作说明。

### 启用省电模式

设备的行为可能因电池电量、自充满电后经过的时间或设备电池是否正在充电而异。例如，Core Location 允许 App 请求所需的精度（[desiredAccuracy](../corelocation/cllocationmanager/desiredaccuracy.md)），但根据设备电池电量，其精度可能会低于你的 App 请求的值。或者，如果并发的 App 或系统进程请求高精度，Core Location 可能提供比请求更高的精度，这可能会更快地消耗设备电池。要观察可能因电池电量较低或 Core Location 精度低于 App 预期而导致的 App 错误，请在以下任意省电模式下进行测试：

- 在 macOS 上，在未连接电源的 Macbook 上运行 App。
- 在 iOS 或 iPadOS 上，在“设置”>“电池”中启用“低电量模式”。

为确保设备处于低电量模式，请检查电池指示器是否为黄色。

### 最小化内存使用

用户的设备在运行时可能比测试人员拥有更少的内存，原因可能是硬件规格不同或设备同时运行的 App 数量不同。为了模拟各种用户环境，测试人员需要改变你的 App 可用的内存量。限制可用内存的一种方法是打开其他 App。在 macOS 上，你可以使用“活动监视器”来观察内存统计信息。“物理内存”和“已使用内存”值之间的差值等于系统的可用内存。

![](../../../attachments/e029e917c5ea55c34954721b1b19ed15/testing-a-release-build-6@2x.png)

<sub>“活动监视器”App 的屏幕截图。中央是一个列表，显示正在运行的进程及其内存使用情况。底部是一个统计信息窗格，以 GB 为单位汇总指标，例如“物理内存”和“已使用内存”。</sub> 因内存耗尽而崩溃的 App 会生成一种不同的崩溃报告，称为 jetsam 事件报告。要检查并分析 jetsam 事件，请参阅[使用 jetsam 事件报告识别高内存使用](identifying-high-memory-use-with-jetsam-event-reports.md)。

内存可用性的不稳定特性使得难以判断你的 App 发生 jetsam 事件的可能性。防止运行时内存耗尽的一个好策略是使用 Instruments 或 MetricKit 主动最小化你的 App 的内存需求。有关更多信息，请参阅[减少 App 的内存使用](reducing-your-app-s-memory-use.md)。

### 支持用户定义的输入

由于用户提供的数据变化范围很广，支持打开用户文件的 App 需要预料到不常见的场景，例如损坏或过大的数据。为了确保良好的用户体验，请测试损坏的文件和不支持的文件。

例如，如果你的 App 加载用户定义的图像，请测试加载非常大的图像。当今常见的图像格式会压缩像素数据，但大多数系统只能显示未压缩的数据。从文件加载图像所需的 RAM 空间可能比文件在磁盘上的大小高出几个数量级。你可以使用以下公式计算图像在 RAM 中所需的字节数：_宽 x 高 x 4_ 字节/像素。一个 4K 分辨率（3840 x 2160 像素）的 JPG 文件在磁盘上大约为 1.5 兆字节。要计算内存中的大小，请将图像尺寸相乘得到像素数，再乘以每像素 4 个字节。

_3840 x 2160 \* 4 B = 33,177,600 B_

除以 1024^2 转换为兆字节。

_33,177,600 B / 1024^2 B/MB = 31.64 MB_

要计算图像在内存中放大的百分比，请将内存中的大小（31.64 MB）除以磁盘上的大小（1.5 MB）。

_31.64 MB / 1.5 MB = 内存中放大 21.1 倍_

为防止文件大小不支持，请通过拒绝打开超过你定义的分辨率的文件来强制限制大小。

再举一个例子，如果你的 App 加载用户通讯录，请测试极端情况以最大化测试覆盖率。例如，你的 App 需要测试大量联系人、没有联系人，以及包含极少数据（或无数据）的联系人。

### 测试语言和区域

用你的 App 支持的每一种语言和区域来测试你的 App。要查看你的 App 的本地化信息，请参阅[添加对语言和区域的支持](https://developer.apple.com/documentation/xcode/adding-support-for-languages-and-regions)。

如果你的 App 处理日期或时间，请确保你的 App 能够处理其支持的所有语言和区域中所有可能的日期格式。用户的“区域”偏好设置决定了操作系统提供给 App 的日期格式。当用户更改其区域时，系统会更改其提供给 App 的每个 [NSDate](../foundation/nsdate.md) 的格式。

测试时请使用 12 小时制区域、24 小时制区域、被覆盖为使用 24 小时制的 12 小时制区域，以及被覆盖为使用 12 小时制的 24 小时制区域。此外，请使用公历和非公历（如农历或阴阳历），以及使用拉丁数字和非拉丁数字（如阿拉伯数字）的区域进行测试。要在设备上设置区域或日历：

- 在 iOS 上，使用“设置”>“通用”>“语言与地区”。
- 在 macOS 上，使用“系统设置”>“通用”>“语言与地区”。

要了解更多关于测试语言和区域的信息，请参阅[在运行你的 App 时测试本地化](https://developer.apple.com/documentation/xcode/testing-localizations-when-running-your-app)。

### 隔离持续存在的问题

对于仅在发布构建中持续出现的问题，请通过提交[技术支持事件](https://developer.apple.com/support/technical/)，创建 Apple 开发者技术支持（DTS）案例。为便于审查该问题，请向 DTS 提供：

- 关于问题的详细信息以及你为重现或解决错误所采取的步骤
- 对于崩溃，请提供包含人类可读函数引用的日志；请参阅[获取崩溃报告和诊断日志](acquiring-crash-reports-and-diagnostic-logs.md)
- 你正在测试的 App 归档的构建 UUID

要检索归档 App 的构建 UUID，请运行终端命令：

```bash
% dwarfdump -u /Path/To/YourApp.xcarchive/Products/Applications/YourApp.app/YourApp
```

## 另请参阅

### 测试

- [测试 Beta 版操作系统](testing-a-beta-os.md) — 通过测试 Beta 版操作系统（OS）版本来管理你的 App 中意外的差异。
