---
title: 将 Objective-C/Cocoa App 移植到 Windows 的选项 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/04/options-for-porting-objective-ccocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:d56e324db7838725'
translated: true
---

> 原文：[Options for porting Objective-C/Cocoa apps to Windows | Cocoa with Love](https://www.cocoawithlove.com/2010/04/options-for-porting-objective-ccocoa.html)　·　Cocoa with Love (Matt Gallagher)

将 Objective-C/Cocoa App 移植到 Windows 有几个不同的选项。每个选项都有不同的优势，并提供不同的能力。在这篇文章中，我将概述其中一些选项，以及它们的优缺点。

## 概述

在这篇文章中，我将探讨将 Objective-C/Cocoa App 移植到 Windows 可用的选项。当然还有其他编写旨在跨平台移植的编译程序的方法（Qt、WxWidgets、Java、纯命令行 C 等）以及大量本质上与平台无关的虚拟化环境（Java、Mono 等），但这是一个 Cocoa 博客，所以我将忽略所有这些。

一个警告：将软件从 Mac 移植到 Windows 很棘手，这篇文章并非旨在解决这些棘手情况。如果你决定将 Objective-C 程序移植到另一个平台，请做好心理准备：你需要通过命令行构建大量软件，追踪并非由你编写的库中的错误，并在各个阶段处理奇怪而神秘的错误信息。长期来看，跨多个平台维护一个共同的代码库是件好事，但初始设置阶段实际上可能比完全重写还要慢。

## 在 Windows 上重建 POSIX

在开始讨论将 Objective-C/Cocoa 程序移植到 Windows 之前，我需要先讨论目标环境。具体来说，就是让 Mac 上的 POSIX 层在 Windows 上运行的困难。

在 Mac 上被认为是“标准 C”的许多功能实际上超出了极简的标准 C 库的范围，而是 Mac 上 BSD 系统的一部分。TCP/IP 套接字、许多文件 I/O 调用、获取当前用户信息——这些都是 Mac 上源自 BSD 的 POSIX 层的特性。

移植到 Windows 时需要解决的第一个问题通常是如何替换这些源自 BSD 的功能。简而言之，你通常需要一个能在 Windows 上提供类似 POSIX 行为的 API。

通常，这涉及两种方法之一：Cygwin 或 MinGW。

### Cygwin

[Cygwin](http://www.cygwin.com/) 是两者中较为知名的，因为它旨在成为一个用户环境。它旨在在 Windows 之上重建一个完整的 POSIX 系统，并具有完全的 POSIX 兼容性。许多从 *nix 系统（Linux、UNIX 等）移植到 Windows 的 X-Windows App 都运行在 Cygwin 之上，因为它最接近提供与 *nix 系统的源代码级兼容性。

然而，Cygwin 也有一个缺点：如果你使用 Cygwin 编写项目，那么你的用户也必须安装 Cygwin。Cygwin 实际上并不是编写原生 Windows App 的方法，它是一种编写原生 Cygwin App 的方法（而 Cygwin 运行在 Windows 之上）。

### MinGW

Cygwin 的替代方案通常是 [MinGW](http://www.mingw.org/)。MinGW 不像 Cygwin 那样是一个用户环境。尽管 MSYS（一个轻量级的终端和用户系统）可以在 MinGW 上运行，但 MSYS 环境通常只供开发人员用于构建和测试 App，而不是给最终用户使用的。

在实现 POSIX 子系统方面，MinGW 采用了与 Cygwin 不同的理念：MinGW 试图实现 POSIX 系统中那些可以轻易映射到原生 Windows WIN32 API 调用的部分。这有一个巨大的优势，即你的目标用户除了 Windows 之外无需安装任何其他东西。不幸的是，这也意味着某些特性（如套接字）的行为会略有不同，因为它们会遵循原生的 Windows 行为，而不是标准的 POSIX 行为。

Cygwin 程序通常是在 Windows 上编译的，而 MinGW 则包含了对交叉编译的重要支持，因此你可以从不同的平台构建 Windows App。

## CoreFoundation

在 Windows 上编译 Objective-C 程序的最简化方法是使用 Apple 自己的 CoreFoundation API 和 Objective-C runtime，并为 Windows 编译它们。

CoreFoundation 和 Objective-C runtime 都是 Apple 在 APSL 许可下的开源项目：

- [CoreFoundation](http://www.opensource.apple.com/source/CF/)
- [CFNetwork (来自 Mac OS X 10.4 —](http://www.opensource.apple.com/source/CFNetwork/)[后续版本并非开源](http://whtconstruct.blogspot.com/2009/09/towards-reopened-cfnetwork.html))
- [CommonCrypto](http://www.opensource.apple.com/source/CommonCrypto/)
- [Objective-C runtime](http://www.opensource.apple.com/source/objc4/)
- [Security](http://www.opensource.apple.com/source/Security/)

该解决方案并非真正的“Cocoa”（它只是 CoreFoundation 的一个非常简单的子集和少数几个支持框架），但它确实有一个主要优势：高效、经过充分测试，并由 Apple 维护。

事实上，Apple 自己就有一份[关于如何使用这些文件在 Linux 和 Windows（通过 Cygwin）上编译的指南](http://developer.apple.com/opensource/cflite.html)。你也可以在 [CFLite](http://karaoke.kjams.com/wiki/CFLite) 上查看另一种设置流程。

### 优势

CoreFoundation 经过充分测试且编写高效。它还在 Mac 和 Windows 之间提供了高度的兼容性。

### 劣势

并非真正的 Cocoa；只有 CoreFoundation（没有 Foundation 或 AppKit）。旧版本的 CFNetwork。

从历史上看，许多人[对 APSL 的具体条款持有异议](http://www.gnu.org/philosophy/historical-apsl.html)。自由软件基金会（Free Software Foundation）已在 APSL 2.0 版本之后[撤回了他们的反对意见](http://www.gnu.org/philosophy/apsl.html)（尽管他们仍然希望它是一个 Copyleft 许可，但那是许可方的问题，而不是许可用户的问题）。

## GNUstep

[GNUstep](http://www.gnustep.org/) 是 OpenStep（后来演变为 Cocoa）最古老的开源实现。它历史悠久且相当稳定。你可以在 Linux、Windows（通过 Cygwin 或 Visual Studio）或 Mac 上构建 GNUstep App。

在 Windows 上开始使用 GNUstep 的最简单方法是使用 [GNUstep Windows Installer](http://www.gnustep.org/experience/Windows.html)。你需要安装 System、Core 和 Devel 组件才能开始编码。这样做的好处是，它会安装所有必需的 MSYS/MinGW 组件。关于安装过程的帮助，还有一份进一步的[Windows 安装指南](http://wiki.gnustep.org/index.php/Installation_on_Windows)。

### 优势

GNUstep 是一个完整的 App 框架，并且已经持续开发了十多年。它可以与大多数开发环境集成，并且可以在 Windows、Linux 和许多其他 *nix 系统上完整构建。

GNUstep 还有一个（相对）庞大的开发社区和大量的[开发人员文档](http://wiki.gnustep.org/index.php/Developer_Guides)（这在开源世界中实属罕见）。

### 劣势

任何为 GNUstep 编写的 App 都必须与 GNUstep 安装程序一起分发（因为必须存在整个 GNUstep 系统才能提供功能）。

GNUstep 更像是一个独立的操作系统（或至少是它自己的窗口系统（windowing system）），而不是现有操作系统内的一个工具包。GNUstep 在任何平台上都不使用原生的窗口绘制命令。

## Cocotron

[Cocotron](http://www.cocotron.org/) 于 2006 年首次发布。其主要目标是支持从 Mac 上的 Xcode 进行交叉编译，以编译到其他平台（主要是 Windows）。

这种从 Xcode 进行交叉编译是 Cocotron 的关键定义特性：即使部署目标是 Windows 或 Linux，你也必须在 Mac 上运行的 Xcode 中构建所有项目。然而，这意味着 Cocotron 的主要工作流程正好专注于将 Mac 程序移植到 Windows 这一任务。

Cocotron 的[安装](http://www.cocotron.org/Info/Getting_Started)是一个多步骤过程，但相对简单。

默认情况下，Cocotron 建议你直接在 Windows 上使用 [Insight-GDB](http://www.cocotron.org/Tools/Debugging/Insight-GDB)（一个在 MinGW 下运行的、对用户相当友好的 GDB 包装器）来[调试你的 Windows 产品](http://www.cocotron.org/Tools/Debugging/Insight-GDB)。

另一种调试方法是使用 XCXDB（[在此处下载 XCXDB 安装包](http://groups.google.com/group/cocotron-dev/files)）。这允许你从 Mac 上的 Xcode 远程调试到你的 Windows 机器，这样你就可以从 Xcode 处理所有的构建和调试。XCXDB 还有一个额外的好处，即它向 Xcode 添加了项目模板，使创建交叉编译项目变得更容易。

### 优势

从 Xcode 中的原始项目构建，并可能调试所有内容。该框架的设计初衷就是考虑从 Mac 移植到 Windows。

原生构建为 WIN32，这意味着最终产品的外观和感觉都像原生 Windows App，并且安装不依赖于安装另一个大型项目（AppKit、Foundation 和其他 .DLL 文件必须与可执行文件一起包含，但它们非常小）。

对 NIB 文件、CoreData、快速枚举（fast enumeration）、Objective-C 2.0 属性（properties）以及其他 GNUstep 中缺失、以外部包形式提供或仍在开发中的特性提供了简单、内置的支持。

旨在与 Mac OS X 达到源代码级兼容性，而这并非一定是 GNUstep 的目标。

### 劣势

到目前为止列出的选项中，最不成熟的一个。你可能会在底层遇到需要自己修复的错误。

虽然实现了大量功能，但你很可能很快就会碰到未实现的 API。某些类的重要部分根本没有实现。虽然接口存在，但当程序运行到 `NSUnimplementedMethod()` 时会导致运行时异常。

XCXDB 远程调试和 Insight 调试的当前状态不如 IDE 中的原生调试。

## 结论

如果你只是将命令行程序移植到 Windows，那么你会有很多选择——我列出的所有选项都能处理这种情况（尽管 CoreFoundation 并没有提供完整的 Foundation API）。

我选择使用 Cocotron 来实现当前 [ServeToMe 的 Windows 公开测试版](http://zqueue.com/servetome/index.html)，因为我认为 Cocotron 提供了将 Mac 图形用户界面 App 移植到 Windows 的最佳体验。能够从原始的 Xcode 项目构建和调试整个项目是我寻求的关键特性。然而，这并非没有问题。下周我将讨论我是如何使用 Cocotron 和 XCXDB 让 ServeToMe 运行起来的，以及我遇到的问题和解决方案。

尽管 Cocotron 相对于 GNUstep 不够成熟，并且缺少许多 API，但它能够使 Cocoa 项目在 Mac 上构建，并在 Windows 上一步完成部署和调试，这是一个巨大的优势。此外，底层使用原生 WIN32（尽管 WIN32 编写起来很烦人）对于最终用户来说比需要一个底层运行 Cygwin 的系统要好。

当然，如果你需要为 Linux 平台开发 Objective-C App，或者需要在 Mac 以外的平台上进行构建，那么你应该使用 GNUstep。虽然 Cocotron 对 Linux/X11 的支持正在进行中，但目前还没有真正准备好被主流采用。
