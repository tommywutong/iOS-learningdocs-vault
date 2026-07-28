---
title: 'Emerge Tools Blog | iOS 15 如何让你的 App 启动更快'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/iOS15LaunchTime'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2e5a448c17337870'
translated: true
---

> 原文：[Emerge Tools Blog | iOS 15 如何让你的 App 启动更快](https://www.emergetools.com/blog/posts/iOS15LaunchTime)　·　Emerge Tools Blog

# iOS 15 如何让你的 App 启动更快

2021 年 6 月 23 日

[Noah Martin](https://twitter.com/sond813)

iOS 性能 启动时间

![带有“iOS 15 启动时间发现”文字的图片](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog3.39576561.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

WWDC21 最引人入胜的特性深藏在 [Xcode 13 发布说明](https://developer.apple.com/documentation/xcode-release-notes/xcode-13-beta-release-notes)中：

> 所有部署目标为 macOS 12 或 iOS 15 或更高版本的程序和 `dylib` 现在都使用 chained fixups 格式。这使用了不同的 load command 和 LINKEDIT 数据，并且无法在较旧的操作系统版本上运行或加载。

目前还没有任何文档或讲座可供你进一步了解这项改动，但我们可以通过逆向工程来了解 Apple 在新操作系统上做了哪些不同的事情，以及它是否会对你的 App 有所帮助。首先，了解一下控制 App 启动的程序的一些背景知识。

## [了解 dyld](https://www.emergetools.com/blog/posts/iOS15LaunchTime#meet-dyld)

动态链接器（[dyld](https://www.emergetools.com/glossary/dyld)）是每个 App 的入口点。它负责让你的代码准备好运行，因此对 dyld 的任何改进都会改善 App 的启动时间是合情合理的。在调用 main、运行静态初始化器或设置 Objective-C 运行时环境之前，dyld 会执行 fixup。这些操作包括 rebase 和 bind，它们会修改 App 二进制文件中的指针，使其包含在运行时有效的地址。要查看这些操作是什么样的，你可以使用 `dyldinfo` 命令行工具。

```shell
% xcrun dyldinfo -rebase -bind Snapchat.app/Snapchat
rebase information (from compressed dyld info):
segment section          address     type
__DATA  __got            0x10748C0C8  pointer
...
bind information:
segment section address     type    addend dylib        symbol
__DATA  __const 0x107595A70 pointer 0      libswiftCore _$sSHMp
```

这意味着地址 `0x10748C0C8` 位于 `__DATA/__got` 中，需要移动一个常量值（称为 slide）。而地址 `0x107595A70` 位于 `__DATA/__const` 中，应指向在 `libswiftCore.dylib` 中找到的 Hashable[1] 的协议描述符。

dyld 使用 `LC_DYLD_INFO` load command 和 [`dyld_info_command`](https://developer.apple.com/documentation/kernel/dyld_info_command) 结构体来确定二进制文件中 rebase、bind 和[导出符号](https://github.com/qyang-nj/llios/blob/main/exported_symbol/README.md)[2] 的位置和大小。[Emerge](https://www.emergetools.com) 会解析这些数据，让你可视化它们对二进制大小的贡献，并建议使用链接器标志来减小它们：

![动态链接器内容的树图。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [一种新格式](https://www.emergetools.com/blog/posts/iOS15LaunchTime#a-new-format)

当我第一次将为 iOS 15 构建的 App 上传到 [Emerge](https://www.emergetools.com) 时，没有出现 dyld fixup 的可视化。这是因为缺少 `LC_DYLD_INFO_ONLY` load command，它已被 `LC_DYLD_CHAINED_FIXUPS` 和 `LC_DYLD_EXPORTS_TRIE` 取代。

```shell
% otool -l iOS14Example.app/iOS14Example | grep LC_DYLD
  cmd LC_DYLD_INFO_ONLY 

% otool -l iOS15Example.app/iOS15Example | grep LC_DYLD
  cmd LC_DYLD_CHAINED_FIXUPS
  cmd LC_DYLD_EXPORTS_TRIE
```

导出数据与之前完全相同，是一个 trie（前缀树），其中每个节点代表符号名称的一部分。

![显示 Wikipedia 的导出 trie 一部分的图示](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Wikipedia 的导出 trie 的一部分

iOS 15 中唯一的变化是，这些数据现在通过一个 [`linkedit_data_command`](https://developer.apple.com/documentation/kernel/linkedit_data_command) 引用，该命令包含第一个节点的偏移量。为了验证这一点，我编写了一个简短的 Swift App 来解析 iOS 15 二进制文件并打印每个符号：

## [Chaining](https://www.emergetools.com/blog/posts/iOS15LaunchTime#chaining)

真正的变化在于 `LC_DYLD_CHAINED_FIXUPS`。在 iOS 15 之前，rebase、bind 和 lazy bind 分别存储在不同的表中。现在，它们已组合成链（chain），指向链起始位置的指针包含在这个新的 load command 中：

![显示链的图示。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

App 二进制文件被分成多个段，每个段都包含一个 fixup 链，这些 fixup 可以是 bind 或 rebase（不再有 lazy bind）。二进制文件中的每个 64 位 rebase[3] 位置现在都编码了它指向的偏移量以及下一个 fixup 的偏移量，如下面的结构体所示：

[dyld_chained_ptr_64_rebase](https://developer.apple.com/documentation/kernel/dyld_chained_ptr_64_rebase)

```swift
struct dyld_chained_ptr_64_rebase
{
uint64_t    target    : 36,
          high8     :  8,
          reserved  :  7,    // 0s
          next      : 12,
          bind      :  1;    // Always 0 for a rebase
};
```

36 位用于指针 target，足以处理 2³⁶ = 64GB 的二进制文件，12 位用于提供下一个 fixup 的偏移量（步长为 4）。因此，它可以在 2¹² * 4 = 16kb 范围内（正好是 iOS 上的页面大小）指向任何位置。

这种非常紧凑的编码意味着遍历整个链的过程可以完全包含在二进制文件的现有大小内。**在我的测试中，超过 50% 的 dyld 数据对二进制大小的贡献被节省了，因为只需要保留少量元数据来指示每个页面上的第一个 fixup**。对于大型 Swift App 来说，最终结果是减少了超过 1MB 的大小。

此过程的源代码位于 [MachOLoaded.cpp](https://opensource.apple.com/source/dyld/dyld-851.27/dyld3/MachOLoaded.cpp.auto.html)，二进制布局在 `/usr/include/macho-o/fixup-chains.h` 中。

## [顺序很重要](https://www.emergetools.com/blog/posts/iOS15LaunchTime#order-matters)

要理解此更改背后的动机，我们必须注意 App 启动期间最昂贵的操作之一：页面错误（page fault）。当在 App 启动期间访问文件系统上的代码时，需要通过页面错误将其从文件加载到内存中。App 二进制文件中的每个 16kb 范围都映射到内存中的一个页面。一旦页面被修改，就需要在 App 运行期间一直留在 RAM 中（称为脏页）。iOS 通过压缩最近未使用的页面来优化这一点。

![显示 App 二进制文件中段的虚拟内存映射简化视图的图示](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F4.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

App 二进制文件中段的虚拟内存映射简化视图

在 App 启动时执行 fixup 需要更改 App 二进制文件中的地址，因此整个页面会被标记为脏页。让我们看看在 App 启动期间 fixup 使用了多少页面：

```shell
% xcrun dyldinfo -rebase Snapchat.app/Snapchat > rebases
% ruby -e 'puts IO.read("rebases").split("
").drop(2).map { |a| a.split(" ")[2].to_i(16) / 16384 }.uniq.count'
1554 

% xcrun dyldinfo -bind Snapchat.app/Snapchat > binds
450
```

使用表格式时，首先解析 rebase，然后解析 bind。这意味着 rebase 需要大量页面错误，并且最终大多受限于 IO[4]。另一方面，bind 访问了 rebase 所使用的 30% 的页面，实际上是对内存进行了第二次遍历。

现在，在 iOS 15 中，chained fixups 将每个内存页面的所有更改分组在一起。**Dyld 现在可以通过一次内存遍历更快地处理它们，同时完成 rebase 和 bind。** 这允许内存压缩器等操作系统功能利用这种已知的顺序，而无需在 bind 期间返回并解压缩旧的页面。由于这些更改，dyld 中的 rebase 函数变成了一个空操作（no-op）：

![来自 iOS 的代码片段](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog3%2F5.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[ImageLoaderMachOCompressed.cpp.auto](https://opensource.apple.com/source/dyld/dyld-851.27/src/ImageLoaderMachOCompressed.cpp.auto.html)

总的来说，此更改主要影响的是逆向工程 iOS 应用和探索动态链接器细节的人，但这也是一个很好的提醒，即底层的内存管理会影响你的 App 的性能。虽然此更改仅在你将 iOS 15 作为部署目标时才会生效，但请记住，你仍然可以做很多事情来优化 App 的启动时间：

- 减少[动态框架](https://www.emergetools.com/glossary/dynamic-frameworks)的数量
- 减小 App 大小，以便使用更少的内存页面
- 将代码移出 `+load` 和静态初始化器
- 使用[更少的类](https://medium.com/codestory/why-swift-reference-types-are-bad-for-app-startup-time-90fbb25237fc)
- 将工作推迟到绘制第一帧之后

---

[1] `dyldinfo` 中的符号是混淆后的，你可以使用 `xcrun swift-demangle '_$sSHMp'` 获取人类可读的名称。

[2] 导出是 bind 的第二部分。一个二进制文件绑定到从其依赖项导出的符号。

[3] 同样适用于 bind，指针实际上是 rebase 和 bind 的联合体（[dyld_chained_ptr_64_bind](https://developer.apple.com/documentation/kernel/dyld_chained_ptr_64_bind)），使用单个位来区分两者。Bind 还需要导入的符号名称，这里不讨论。

[4] https://asciiwwdc.com/2016/sessions/406
