---
title: Xcode LLDB RPC 服务器崩溃
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2021/11/22/fix-lldb-rpc-server-crash/'
original_language: en
published: 2021-11-22
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6d7e738fe244a18e'
translated: true
---

> 原文：[Xcode LLDB RPC server crash](https://www.jessesquires.com/blog/2021/11/22/fix-lldb-rpc-server-crash/)　·　Jesse Squires

几周前，我写了一篇[关于 Xcode 13 运行测试时出现离奇崩溃的文章](https://www.jessesquires.com/blog/2021/11/03/xcode-13-framework-test-fail/)。我刚刚发现了那篇文章中提到的一个问题的根本原因——_我认为_。至少，我找到了一个“修复方法”。该问题出现在运行单元测试时。有时完整的测试套件能够跑完，有时则不能，之后 LLDB 会崩溃。我的所有项目都会遇到这个问题。无论我做什么，似乎都无法避免崩溃，这快把我逼疯了。

澄清一下：Xcode 本身没有崩溃，只有 LLDB 崩溃。Xcode 会显示一个错误提示，内容如下：

> LLDB RPC 服务器已崩溃。你可能需要手动终止你的进程。崩溃日志位于 ~/Library/Logs/DiagnosticReports，文件名以 'lldb-rpc-server' 为前缀。请提交一个错误报告并附上最新的崩溃日志。

如果我点击“详细信息”查看更多内容，Xcode 会显示以下信息：

```
Could not launch “<TEST TARGET NAME>”
Domain: IDEDebugSessionErrorDomain
Code: 3
Failure Reason: The LLDB RPC server has crashed. You may need to manually terminate your process. The crash log is located in ~/Library/Logs/DiagnosticReports and has a prefix 'lldb-rpc-server'. Please file a bug and attach the most recent crash log.
User Info: {
    DVTRadarComponentKey = 855031;
    IDERunOperationFailingWorker = DBGLLDBLauncher;
    RawUnderlyingErrorMessage = "The LLDB RPC server has crashed. You may need to manually terminate your process. The crash log is located in ~/Library/Logs/DiagnosticReports and has a prefix 'lldb-rpc-server'. Please file a bug and attach the most recent crash log.";
}
--

Analytics Event: com.apple.dt.IDERunOperationWorkerFinished : {
    "device_model" = "MacBookPro16,2";
    "device_osBuild" = "12.0.1 (21A559)";
    "device_platform" = "com.apple.platform.macosx";
    "launchSession_schemeCommand" = Test;
    "launchSession_state" = 1;
    "launchSession_targetArch" = "x86_64";
    "operation_duration_ms" = 92;
    "operation_errorCode" = 3;
    "operation_errorDomain" = IDEDebugSessionErrorDomain;
    "operation_errorWorker" = DBGLLDBLauncher;
    "operation_name" = IDERunOperationWorkerGroup;
    "param_consoleMode" = 0;
    "param_debugger_attachToExtensions" = 0;
    "param_debugger_attachToXPC" = 1;
    "param_debugger_type" = 3;
    "param_destination_isProxy" = 0;
    "param_destination_platform" = "com.apple.platform.macosx";
    "param_diag_MainThreadChecker_stopOnIssue" = 0;
    "param_diag_MallocStackLogging_enableDuringAttach" = 0;
    "param_diag_MallocStackLogging_enableForXPC" = 0;
    "param_diag_allowLocationSimulation" = 1;
    "param_diag_gpu_frameCapture_enable" = 3;
    "param_diag_gpu_shaderValidation_enable" = 0;
    "param_diag_gpu_validation_enable" = 1;
    "param_diag_memoryGraphOnResourceException" = 0;
    "param_diag_queueDebugging_enable" = 1;
    "param_diag_runtimeProfile_generate" = 1;
    "param_diag_sanitizer_asan_enable" = 0;
    "param_diag_sanitizer_tsan_enable" = 0;
    "param_diag_sanitizer_tsan_stopOnIssue" = 0;
    "param_diag_sanitizer_ubsan_stopOnIssue" = 0;
    "param_diag_showNonLocalizedStrings" = 0;
    "param_diag_viewDebugging_enabled" = 1;
    "param_diag_viewDebugging_insertDylibOnLaunch" = 0;
    "param_install_style" = 0;
    "param_launcher_UID" = 2;
    "param_launcher_allowDeviceSensorReplayData" = 0;
    "param_launcher_kind" = 0;
    "param_launcher_style" = 0;
    "param_launcher_substyle" = 0;
    "param_runnable_appExtensionHostRunMode" = 0;
    "param_runnable_productType" = "com.apple.product-type.tool";
    "param_runnable_type" = 1;
    "param_testing_launchedForTesting" = 1;
    "param_testing_suppressSimulatorApp" = 0;
    "param_testing_usingCLI" = 0;
    "sdk_canonicalName" = "macosx12.0";
    "sdk_osVersion" = "12.0";
    "sdk_variant" = macos;
}
```

正如[之前提到的](https://www.jessesquires.com/blog/2021/11/03/xcode-13-framework-test-fail/)，我向 Apple 提交了 FB9738278。这是他们非常有用的回复：

> 看起来这是在重放机制（reproducers）中崩溃的，而重放机制已被禁用。你很可能创建了一个 `/AppleInternal` 目录，就像你在内部系统上操作一样。这是不受支持的。

鬼知道这是什么意思。我回复说我从未创建过 `/AppleInternal` 目录，完全不知道他们在说什么。你可能会觉得一个（看起来挺严重的）崩溃应该会得到更多关注。

不管怎样，昨晚我终于想出了一个新的可能原因。除了从 Xcode 12 升级到 Xcode 13 之外，我在机器上没做任何开发工具相关的更改，而问题就是在那之后开始出现的。我怀疑问题可能与我的 `~/.lldbinit` 文件有关——这是我对 LLDB 所做的唯一“修改”。

我安装了 [Chisel](https://github.com/facebook/chisel) 和 [Kaleidoscope](https://kaleidoscope.app) 的 `lldb_ksdiff`。我的 `~/.lldbinit` 导入了这些文件，然后包含了几条自定义命令。我决定尝试移除 Chisel——然后崩溃就_不再发生了_。我目前还不明白这是如何或为什么会这样——我对 Chisel 的实现细节了解不够——但我很高兴有了一个“修复方法”。我在 GitHub 上为 Chisel 提了一个 issue：[#298](https://github.com/facebook/chisel/issues/298)。

这些年来，调试工具已经足够完善，我平时不再频繁使用 Chisel，所以这不算什么大损失。如果需要实时调试，我总可以取消注释导入语句。我希望 Chisel 是真正的根本问题，而不是一个干扰项。我很好奇这个问题是否也影响了其他人——不过我觉得没有，因为如果这个问题很普遍，Twitter 上应该会有更多的抱怨声。
