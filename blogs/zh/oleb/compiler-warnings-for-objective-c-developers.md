---
title: 面向 Objective-C 开发者的编译器警告
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/04/compiler-warnings-for-objective-c-developers/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d854839ee320589a'
translated: true
---

> 原文：[Compiler Warnings for Objective-C Developers](https://oleb.net/blog/2013/04/compiler-warnings-for-objective-c-developers/)　·　Ole Begemann

# 面向 Objective-C 开发者的编译器警告

编译器警告是开发者最得力的工具之一。编译器不仅能提醒你明显的错误（比如忘了实现的某个方法）；它还能识别出许多代码模式——这些代码虽然语法正确，但潜在危险（如 `signed`/`unsigned` 转换）或干脆就是错的（如格式字符串中不匹配的格式说明符（format specifier））。

[Clang 编译器前端（Clang compiler frontend）](http://clang.llvm.org)和 Apple 默认的 Xcode 项目模板都启用了默认的警告集，其设计既能警告代码中的许多可能错误，又不会用海量误报（false positives）来烦你。这些默认设置为了与大型遗留代码库（legacy codebases）良好配合，启用的警告往往较为保守。不过，它们并非新项目的最佳选择。相反，你应该尽可能多地启用警告。

# 尽可能多地启用警告

为了充分利用编译器能提供的所有帮助，你必须编辑项目的构建设置（Build Settings）并启用更多警告。大多数警告类型在 Xcode 的构建设置 UI 中都有展示，因此你可以逐个启用额外的警告（既可以针对整个项目，也可以按 target 进行）。快速帮助检查器（Quick Help Inspector）可以帮助解释每个警告的用途。构建设置 UI 中警告有多个区域，请务必查看所有标有“Apple LLVM compiler - Warnings – …”的区域。

[![在 Xcode 的构建设置中配置编译器警告](https://oleb.net/media/xcode-build-settings-compiler-warnings.png)](https://oleb.net/media/xcode-build-settings-compiler-warnings.png)

<sub>在 Xcode 的构建设置中配置编译器警告。快速帮助检查器中包含每个警告标志的文档。</sub>

但还有一种更好（也更面向未来）的方法：与其逐个启用你想要的警告，我认为更好的做法是从 _所有_（或几乎所有）警告都启用开始，然后有选择地禁用你主动选择忽略的少数几种警告。这样，你就可以确信即便现有的项目也能从日益强大的代码分析中获益——随着编译器每个版本都变得更智能，新警告也在不断增加。例如，Xcode 4.6（使用 LLVM 3.2）就增加了[几个](https://twitter.com/SlaunchaMan/status/295968911705395200)[新](https://useyourloaf.com/blog/2013/03/03/xcode-4-dot-6-recommended-build-settings.html)警告。^[1](#fn:1)

缺点（这真的是缺点吗？）是你无法通过几次点击鼠标就完成这样的设置。相反，你必须将一个或多个自定义构建标志添加到 ~~Other C Flags~~Other Warning Flags 构建设置中（把它们放在 Other C Flags 里也行，但 Other Warning Flags 是更合适的位置）。编译器标志 `-W…` 让你可以启用或禁用特定的警告以及预定义的集合。你可以根据需要包含任意多个 `-W…` 选项。例如，标志 `-Wall -Wno-unused-variable` 告诉编译器：“启用‘所有’警告（关于‘所有’的含义见下文），但不要对未使用的变量发出警告”。

[![在 Xcode 的构建设置中编辑 Other C Flags](https://oleb.net/media/xcode-build-settings-other-c-flags.png)](https://oleb.net/media/xcode-build-settings-other-c-flags.png)

<sub>通过在 Other C Flags 中添加 `-W…` 选项来自定义编译器的警告级别。</sub>

**2013 年 12 月 13 日更新：** 读者 Michael Hackett 指出，即使在构建设置中包含了自定义警告标志，Xcode 仍会观察勾选/未勾选的警告，并将相应的 Clang 标志添加到其构建命令中。但是，像 `-Wall -Wextra` 这样的自定义警告标志会在构建命令的较后位置添加，因此似乎会覆盖其他标志。这种做法虽不完美，但有效。

# All 并不等于 Everything

好吧，你决定从启用全套警告开始。正确的 `-W…` 咒语是什么？这个问题的答案可能比你想象的更复杂。LLVM 开发者之一 Chandler Carruth 在 [Programmers Stack Exchange 上的一个出色回答](http://programmers.stackexchange.com/a/124574)中对此进行了解释。Clang 中有几个重要的警告标志分组：

- `-Wall`：这听起来像是 _所有_ 警告的集合，但实际上它只涵盖了可用警告的一个子集。用 Carruth 的话来说，编译器开发者对这些警告的价值和低误报率有很高的信心。这个标志将提供相当激进的警告级别，可能会指出代码中一系列默认设置未能捕获的潜在错误。同时，`-Wall` 被设计为即使在遗留代码库中也很少产生误报，这就是为什么一些关键警告被排除在这个分组之外的原因。
- `-Wextra`：这个分组包含的警告可能与 `-Wall` 中的一样有用，但可能触发更高的误报率或引起普遍的哲学上的异议。`-Wsign-compare` 标志就是一个很好的例子，当比较有符号整数与无符号类型时，它就会发出警告。由于许多大型代码库到处都有这种用法（而且在大多数情况下并非 bug），将这一标志包含在 `-Wall` 中会产生大量你可能不想看到的警告。

  请注意，`-Wextra` **不**包含 `-Wall`。如果你两者都需要，则必须在 Other C Flags 中同时指定两者。与 `-Wall`（部分由于历史原因，它是一个基本稳定的分组）不同，随着新的有用警告被添加到 Clang 中，它们会被包含在 `-Wextra` 中。
- `-Weverything`：这是神奇的咒语，实际上会启用 Clang 中的**每一条**警告，包括那些可能仍在开发中、带有 bug 的警告。不要在你的代码上使用它。它严格针对 Clang 开发者或用于探索存在哪些警告。

# 我应该启用哪些警告？

我建议你从 `-Wall` 和 `-Wextra` 开始，特别是对于新项目。然后在此基础之上进行。构建你的项目，看看会出现哪些警告。修复那些暴露了代码中实际问题的警告。

如果你遇到了某个特定想要压制的警告，请查看构建日志（build log）。编译器会告诉你它发出的每个警告的名称（例如本例中的 `-Wunused-variable`）。你可以使用这个名称在项目中有选择地禁用（使用 `-Wno-unused-variable`）或启用这个特定的警告。根据我的经验，你最终想要禁用的警告列表会非常短（可能不超过几条）。

[![展示编译器警告的 Xcode 构建日志](https://oleb.net/media/xcode-build-log-warning-name.png)](https://oleb.net/media/xcode-build-log-warning-name.png)

<sub>Xcode 在构建日志中显示它发出的每个警告的内部名称（此处为 `-Wunused-variable`）。</sub>

# 临时禁用警告

你应该始终致力于一个零警告构建的项目。一个留有未修复编译器警告的代码库是开发者粗心的表现。

如果你只想禁用目标中一个或多个特定文件的警告（例如，因为你使用了第三方库的源代码，并且不想修复该代码中的警告），你也可以在逐个文件的基础上包含 `-W…` 标志。只需切换到 Build Phases 标签页，在 Compile Sources 区域中，将选项添加到相关文件的 Compiler Flags 字段。

要针对一小段代码而不是整个文件禁用警告，Clang 支持以下 `#pragma` 语句：

```
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wsign-compare"

int i = 100;
unsigned int u = 200;
if (i < u) {  // no warning
  ...
}

#pragma clang diagnostic pop
```

# 将警告视为错误

许多开发者喜欢指示编译器将警告视为错误，因为这样可以阻止构建成功，哪怕只有一个警告未处理。要在 Xcode 中做到这一点，请在构建设置中勾选相应的复选框，或在 Other C Flags 中包含 `-Werror`。

就我个人而言，我不使用这个设置，因为我觉得它在开发过程中很烦人。像“未使用的变量”这样的警告在调试期间完全没问题，但如果把它们视为错误，就会造成比应有水平更多的工作量。然而，这并不意味着我容忍“真实”构建中存在未处理的警告。仅在发布版本和持续集成服务器（continuous integration server，如果有的话）上激活 `-Werror` 是一个很好的折衷方案。

请注意，还有 `-Werror=foo`（允许你仅将特定警告视为错误）和 `-Wno-error=foo`（在启用了 `-Werror` 的情况下，将特定警告视为简单警告而不是错误），用于更精细的控制。

1. Xcode 4 有一个迁移助手（migration assistant），可以自动更新遗留项目的构建设置以包含新的默认警告。当你尝试在新版本的 Xcode 中使用旧设置构建项目时，它会以构建警告的形式自动弹出。这很有帮助，但不能保证你会捕获新编译器版本的所有新能力。助手只会将你的项目更新到 Apple 推荐的设置，这些设置可能适合也可能不适合你的项目（而且 Xcode 的构建设置 UI 甚至没有展示所有可用的编译器警告）。[↩︎](#fnref:1)
