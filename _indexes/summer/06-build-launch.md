# 模块 6：编译链接、Mach-O、dyld 与 App 启动

> 沿源文件、目标文件、Mach-O、链接器和 dyld 追到冷启动优化。
> 对应仓库范围：启动、链接与二进制、性能与调试。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 6.1 | 预处理、编译、汇编、静态链接；符号、重定位、链接错误 | `.m` → 预处理 → LLVM IR → 汇编 → 目标文件命令记录 |
| 6.2 | Mach-O header、load commands、segments/sections、symbol table | `file`、`otool`/`vtool`、`nm` 解剖最小 App 二进制 |
| 6.3 | 静态库、动态库、framework、XCFramework；链接时与运行时差异 | 同一模块做静态/动态产物，对比包体、符号和依赖 |
| 6.4 | dyld2 → dyld3 → dyld4；rebase/bind/fixups、shared cache、launch closure | 历史演进表，标出当前机制和旧版本背景 |
| 6.5 | App 冷启动：pre-main、runtime 初始化、UIKit/scene、首帧；`+load` 与静态初始化成本 | 启动阶段图 + Instruments App Launch 证据 |
| 6.6 | 启动优化实战：测量、假设、延后非关键任务、复测 | 一份启动 baseline，不接受“体感变快” |

## 计划指定材料

- [Xcode 构建过程揭秘](../../wwdc/zh/wwdc2018/415-behind-the-scenes-of-the-xcode-build-process.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/wwdc/zh/wwdc2018/415-behind-the-scenes-of-the-xcode-build-process.md) — 本仓库资料
- [mach-o](../../apple-docs/zh/kernel/mach-o.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/kernel/mach-o.md) — 本仓库资料
- [Introduction](../../legacy-archive/vault/documentation/Developer%20Tools/Dynamic%20Library%20Programming%20Topics/Introduction.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Developer%20Tools/Dynamic%20Library%20Programming%20Topics/Introduction.md) — Apple 旧归档
- [链接加速：缩短构建和启动时间](../../wwdc/zh/wwdc2022/110362-link-fast-improve-build-and-launch-times.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/wwdc/zh/wwdc2022/110362-link-fast-improve-build-and-launch-times.md) — 本仓库资料
- [缩短你的 App 的启动时间](../../apple-docs/zh/xcode/reducing-your-app-s-launch-time.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/xcode/reducing-your-app-s-launch-time.md) — 本仓库资料
- [优化 App 启动](../../wwdc/zh/wwdc2019/423-optimizing-app-launch.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/wwdc/zh/wwdc2019/423-optimizing-app-launch.md) — 本仓库资料
- [Friday Q&A 2009-11-06：链接与安装名称](../../blogs/zh/mikeash/friday-q-a-2009-11-06-linking-and-install-names.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2009-11-06-linking-and-install-names.md) — 本仓库资料
- [计划材料](https://segmentfault.com/a/1190000047731614) — 第三方博客（未归档（segmentfault.com））
- [Friday Q&A 2012-11-30：让我们构建一个 Mach-O 可执行文件](../../blogs/zh/mikeash/friday-q-a-2012-11-30-let-s-build-a-mach-o-executable.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2012-11-30-let-s-build-a-mach-o-executable.md) — 本仓库资料
- [计划材料](https://developer.apple.com/forums/thread/715385) — Apple 其它
- [计划材料](https://pewpewthespells.com/blog/static_and_dynamic_libraries.html) — 第三方博客（未归档（pewpewthespells.com））
- [计划材料](https://bpoplauschi.github.io/2021/10/24/Intro-to-static-and-dynamic-libraries-frameworks.html) — 第三方博客（未归档（bpoplauschi.github.io））
- [计划材料](https://engineering.monday.com/is-there-such-a-thing-as-a-static-framework/) — 第三方博客（未归档（engineering.monday.com））
- [计划材料](https://github.com/apple-oss-distributions/dyld) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://ddeville.me/2014/04/dynamic-linking/) — 第三方博客（未归档（ddeville.me））
- [计划材料](https://blog.allegro.tech/2018/05/Static-linking-vs-dyld3.html) — 第三方博客（未归档（blog.allegro.tech））
- [计划材料](https://huang-libo.github.io/posts/App-Startup-Time-dyld/) — 第三方博客（未归档（huang-libo.github.io））
- [计划材料](https://zhuanlan.zhihu.com/p/597864788) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [计划材料](https://blog.jacobstechtavern.com/p/static-dynamic-mergeable-oh-my) — 第三方博客（未归档（blog.jacobstechtavern.com））
- [计划材料](https://www.avanderlee.com/optimization/launch-time-performance-optimization/) — 第三方博客（未归档（avanderlee.com））
- [计划材料](https://tech.meituan.com/2018/12/06/waimai-ios-optimizing-startup.html) — 第三方博客（未归档（tech.meituan.com））
- [计划材料](https://mp.weixin.qq.com/s/Drmmx5JtjG3UtTFksL6Q8Q) — 第三方博客（未归档（mp.weixin.qq.com））
- [iOS 15 如何让你的 App 启动更快](../../blogs/zh/emergetools/emerge-tools-blog-how-ios-15-makes-your-app-launch-faster.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/emergetools/emerge-tools-blog-how-ios-15-makes-your-app-launch-faster.md) — 本仓库资料
- [顺序文件如何减少 App 启动时间](../../blogs/zh/emergetools/emerge-tools-blog-how-order-files-reduce-app-startup-time.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/emergetools/emerge-tools-blog-how-order-files-reduce-app-startup-time.md) — 本仓库资料
- [Facebook iOS App 架构的演进](../../blogs/zh/fbeng/the-evolution-of-facebook-s-ios-app-architecture.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/fbeng/the-evolution-of-facebook-s-ios-app-architecture.md) — 本仓库资料

## 中文资料

共 69 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [App 启动时间：提升性能的 7 个技巧](../../blogs/snapshots-zh/avanderlee.com/app-launch-time-7-tips-to-increase-performance.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/avanderlee.com/app-launch-time-7-tips-to-increase-performance.md) | 已翻译 |
| 计划核心 | [iOS（及 macOS）静态与动态库和框架简介](../../blogs/snapshots-zh/bpoplauschi.github.io/introduction-to-static-vs-dynamic-libraries-and-frameworks-on-ios-and-macos.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/bpoplauschi.github.io/introduction-to-static-vs-dynamic-libraries-and-frameworks-on-ios-and-macos.md) | 已翻译 |
| 计划核心 | [Podfile](../../blogs/snapshots/segmentfault.com/ios-%E7%BC%96%E8%AF%91%E9%93%BE%E6%8E%A5%E4%B8%8E-mach-o-%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90-%E9%9D%99%E6%80%81%E5%BA%93-%E5%8A%A8%E6%80%81%E5%BA%93%E5%8E%9F%E7%90%86%E5%89%96%E6%9E%90-%E5%88%B0%E5%B7%A5%E7%A8%8B%E5%8C%96%E5%AE%9E%E8%B7%B5.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/segmentfault.com/ios-%E7%BC%96%E8%AF%91%E9%93%BE%E6%8E%A5%E4%B8%8E-mach-o-%E6%B7%B1%E5%BA%A6%E8%A7%A3%E6%9E%90-%E9%9D%99%E6%80%81%E5%BA%93-%E5%8A%A8%E6%80%81%E5%BA%93%E5%8E%9F%E7%90%86%E5%89%96%E6%9E%90-%E5%88%B0%E5%B7%A5%E7%A8%8B%E5%8C%96%E5%AE%9E%E8%B7%B5.md) | 原生中文 |
| 计划核心 | [【WWDC17】优化 APP 启动（dyld 2 -> dyld 3）](../../blogs/snapshots/huang-libo.github.io/wwdc17-%E4%BC%98%E5%8C%96-app-%E5%90%AF%E5%8A%A8-dyld-2-dyld-3.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/huang-libo.github.io/wwdc17-%E4%BC%98%E5%8C%96-app-%E5%90%AF%E5%8A%A8-dyld-2-dyld-3.md) | 原生中文 |
| 计划核心 | [存在所谓的静态框架吗？](../../blogs/snapshots-zh/engineering.monday.com/is-there-such-a-thing-as-a-static-framework-monday-ai-engineering.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/engineering.monday.com/is-there-such-a-thing-as-a-static-framework-monday-ai-engineering.md) | 已翻译 |
| 计划核心 | [库的链接](../../blogs/snapshots-zh/ddeville.me/dynamic-linking-on-ios.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/ddeville.me/dynamic-linking-on-ios.md) | 已翻译 |
| 计划核心 | [美团外卖iOS App冷启动治理](../../blogs/snapshots/tech.meituan.com/%E7%BE%8E%E5%9B%A2%E5%A4%96%E5%8D%96ios-app%E5%86%B7%E5%90%AF%E5%8A%A8%E6%B2%BB%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/tech.meituan.com/%E7%BE%8E%E5%9B%A2%E5%A4%96%E5%8D%96ios-app%E5%86%B7%E5%90%AF%E5%8A%A8%E6%B2%BB%E7%90%86.md) | 原生中文 |
| 计划核心 | [静态、动态、可合并，天哪！](../../blogs/snapshots-zh/blog.jacobstechtavern.com/static-dynamic-mergeable-oh-my.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/blog.jacobstechtavern.com/static-dynamic-mergeable-oh-my.md) | 已翻译 |
| 计划核心 | [静态库与动态库](../../blogs/snapshots-zh/pewpewthespells.com/static-and-dynamic-libraries.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/pewpewthespells.com/static-and-dynamic-libraries.md) | 已翻译 |
| 计划核心 | [静态链接 vs dyld3](../../blogs/snapshots-zh/blog.allegro.tech/static-linking-vs-dyld3.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/blog.allegro.tech/static-linking-vs-dyld3.md) | 已翻译 |
| 官方资料 | [BinaryInteger 实现](../../apple-docs/zh/swift/uint8/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/uint8/binaryinteger-implementations.md) | 已翻译 |
| 官方资料 | [BinaryInteger 实现](../../apple-docs/zh/swift/int8/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/int8/binaryinteger-implementations.md) | 已翻译 |
| 官方资料 | [BinaryInteger 实现](../../apple-docs/zh/swift/int128/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/int128/binaryinteger-implementations.md) | 已翻译 |
| 官方资料 | [mach-o](../../apple-docs/zh/kernel/mach-o.md) | Apple 文档 | Apple · Kernel | [中文](../../apple-docs/zh/kernel/mach-o.md) | 已翻译 |
| 官方资料 | [Mach-O 架构](../../apple-docs/zh/foundation/1495005-mach-o-architecture.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/1495005-mach-o-architecture.md) | 已翻译 |
| 官方资料 | [以 Swift 包的形式分发二进制框架](../../apple-docs/zh/xcode/distributing-binary-frameworks-as-swift-packages.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/distributing-binary-frameworks-as-swift-packages.md) | 已翻译 |
| 官方资料 | [关于 App 启动序列](../../apple-docs/zh/uikit/about-the-app-launch-sequence.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/about-the-app-launch-sequence.md) | 已翻译 |
| 官方资料 | [减小着色器库的二进制大小](../../apple-docs/zh/metal/minimizing-the-binary-size-of-a-shader-library.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/minimizing-the-binary-size-of-a-shader-library.md) | 已翻译 |
| 官方资料 | [创建多平台二进制框架捆绑包](../../apple-docs/zh/xcode/creating-a-multi-platform-binary-framework-bundle.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/creating-a-multi-platform-binary-framework-bundle.md) | 已翻译 |
| 官方资料 | [定义启动环境和库约束](../../apple-docs/zh/security/defining-launch-environment-and-library-constraints.md) | Apple 文档 | Apple · Security | [中文](../../apple-docs/zh/security/defining-launch-environment-and-library-constraints.md) | 已翻译 |
| 官方资料 | [应用启动环境与库约束](../../apple-docs/zh/security/applying-launch-environment-and-library-constraints.md) | Apple 文档 | Apple · Security | [中文](../../apple-docs/zh/security/applying-launch-environment-and-library-constraints.md) | 已翻译 |
| 官方资料 | [应用程序二进制接口](../../apple-docs/zh/xcode/application-binary-interfaces.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/application-binary-interfaces.md) | 已翻译 |
| 官方资料 | [指定你的 App 的启动画面](../../apple-docs/zh/xcode/specifying-your-apps-launch-screen.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/specifying-your-apps-launch-screen.md) | 已翻译 |
| 官方资料 | [编译与链接 Metal 动态库](../../apple-docs/zh/metal/compiling-and-linking-metal-dynamic-libraries.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/compiling-and-linking-metal-dynamic-libraries.md) | 已翻译 |
| 官方资料 | [缩短你的 App 的启动时间](../../apple-docs/zh/xcode/reducing-your-app-s-launch-time.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/reducing-your-app-s-launch-time.md) | 已翻译 |
| 官方资料 | [识别二进制依赖项](../../apple-docs/zh/xcode/identifying-binary-dependencies.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/identifying-binary-dependencies.md) | 已翻译 |
| 官方资料 | [Swift 中的二进制框架](../../wwdc/zh/wwdc2019/416-binary-frameworks-in-swift.md) | WWDC | Apple · WWDC2019 | [中文](../../wwdc/zh/wwdc2019/416-binary-frameworks-in-swift.md) | 已翻译 |
| 官方资料 | [优化 App 启动](../../wwdc/zh/wwdc2019/423-optimizing-app-launch.md) | WWDC | Apple · WWDC2019 | [中文](../../wwdc/zh/wwdc2019/423-optimizing-app-launch.md) | 已翻译 |
| 官方资料 | [把二进制框架以 Swift package 的形式分发](../../wwdc/zh/wwdc2020/10147-distribute-binary-frameworks-as-swift-packages.md) | WWDC | Apple · WWDC2020 | [中文](../../wwdc/zh/wwdc2020/10147-distribute-binary-frameworks-as-swift-packages.md) | 已翻译 |
| 官方资料 | [链接加速：缩短构建和启动时间](../../wwdc/zh/wwdc2022/110362-link-fast-improve-build-and-launch-times.md) | WWDC | Apple · WWDC2022 | [中文](../../wwdc/zh/wwdc2022/110362-link-fast-improve-build-and-launch-times.md) | 已翻译 |
| 深度补充 | [dyld：OS X 上的动态链接](../../blogs/zh/mikeash/dyld-dynamic-linking-on-os-x.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/dyld-dynamic-linking-on-os-x.md) | 已翻译 |
| 深度补充 | [Message-ID 与 iOS 和 macOS 上的 Mail.app 深度链接](../../blogs/zh/nshipster/message-id-and-mail-app-deep-linking-on-ios-and-macos.md) | 技术博客 | NSHipster (Mattt) | [中文](../../blogs/zh/nshipster/message-id-and-mail-app-deep-linking-on-ios-and-macos.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-11-06：链接与安装名称](../../blogs/zh/mikeash/friday-q-a-2009-11-06-linking-and-install-names.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-11-06-linking-and-install-names.md) | 已翻译 |
| 深度补充 | [星期五问答 2012-11-30：让我们构建一个 Mach-O 可执行文件](../../blogs/zh/mikeash/friday-q-a-2012-11-30-let-s-build-a-mach-o-executable.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2012-11-30-let-s-build-a-mach-o-executable.md) | 已翻译 |
| 深度补充 | [星期五问答 2017-07-28：一个 Swift 二进制编码器](../../blogs/zh/mikeash/friday-q-a-2017-07-28-a-binary-coder-for-swift.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2017-07-28-a-binary-coder-for-swift.md) | 已翻译 |
| 深度补充 | [Mach-O 可执行文件](../../blogs/zh/objccn/mach-o-%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/mach-o-%E5%8F%AF%E6%89%A7%E8%A1%8C%E6%96%87%E4%BB%B6.md) | 原生中文 |
| 补充资料 | [[objc 解析]: dyld 共享缓存中的选择器唯一化](../../blogs/zh/sealiesoftware/objc-explain-selector-uniquing-in-the-dyld-shared-cache.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-selector-uniquing-in-the-dyld-shared-cache.md) | 已翻译 |
| 补充资料 | [AArch32 链接器笔记](../../blogs/zh/maskray/linker-notes-on-aarch32.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/linker-notes-on-aarch32.md) | 已翻译 |
| 补充资料 | [AArch64 上的链接器笔记](../../blogs/zh/maskray/linker-notes-on-aarch64.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/linker-notes-on-aarch64.md) | 已翻译 |
| 补充资料 | [iOS 15 如何让你的 App 启动更快](../../blogs/zh/emergetools/emerge-tools-blog-how-ios-15-makes-your-app-launch-faster.md) | 技术博客 | Emerge Tools Blog | [中文](../../blogs/zh/emergetools/emerge-tools-blog-how-ios-15-makes-your-app-launch-faster.md) | 已翻译 |
| 补充资料 | [iOS 16 如何让你的 App 启动更快](../../blogs/zh/emergetools/emerge-tools-blog-how-ios-16-makes-your-app-launch-faster.md) | 技术博客 | Emerge Tools Blog | [中文](../../blogs/zh/emergetools/emerge-tools-blog-how-ios-16-makes-your-app-launch-faster.md) | 已翻译 |
| 补充资料 | [iOS 上的 App 启动序列](../../blogs/zh/oleb/the-app-launch-sequence-on-ios.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/the-app-launch-sequence-on-ios.md) | 已翻译 |
| 补充资料 | [LLD 与 GNU 链接器兼容性差异](../../blogs/zh/maskray/lld-and-gnu-linker-incompatibilities.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/lld-and-gnu-linker-incompatibilities.md) | 已翻译 |
| 补充资料 | [lld 中的 RISC-V 链接器松弛](../../blogs/zh/maskray/risc-v-linker-relaxation-in-lld.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/risc-v-linker-relaxation-in-lld.md) | 已翻译 |
| 补充资料 | [NSArray 二分查找](../../blogs/zh/oleb/nsarray-binary-search.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/nsarray-binary-search.md) | 已翻译 |
| 补充资料 | [Power ISA 链接器笔记](../../blogs/zh/maskray/linker-notes-on-power-isa.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/linker-notes-on-power-isa.md) | 已翻译 |
| 补充资料 | [Swift 编译器诊断](../../blogs/zh/oleb/swift-compiler-diagnostics.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/swift-compiler-diagnostics.md) | 已翻译 |
| 补充资料 | [x86 链接器笔记](../../blogs/zh/maskray/linker-notes-on-x86.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/linker-notes-on-x86.md) | 已翻译 |
| 补充资料 | [与依赖相关的链接器选项](../../blogs/zh/maskray/dependency-related-linker-options.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/dependency-related-linker-options.md) | 已翻译 |
| 补充资料 | [从 dyld 共享缓存中提取库](../../blogs/zh/worthdoingbadly/extracting-libraries-from-dyld-shared-cache.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [中文](../../blogs/zh/worthdoingbadly/extracting-libraries-from-dyld-shared-cache.md) | 已翻译 |
| 补充资料 | [使用 dyld Interposing 进行代码注入](../../blogs/zh/emergetools/emerge-tools-blog-code-injection-with-dyld-interposing.md) | 技术博客 | Emerge Tools Blog | [中文](../../blogs/zh/emergetools/emerge-tools-blog-code-injection-with-dyld-interposing.md) | 已翻译 |
| 补充资料 | [动态链接对应用有害，静态链接对应用也有害](../../blogs/zh/belkadan/dynamic-linking-is-bad-for-apps-and-static-linking-is-also-bad-for-apps.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/dynamic-linking-is-bad-for-apps-and-static-linking-is-also-bad-for-apps.md) | 已翻译 |
| 补充资料 | [可重定位链接](../../blogs/zh/maskray/relocatable-linking.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/relocatable-linking.md) | 已翻译 |
| 补充资料 | [如何调试通过推送通知或 URL 处理程序启动的 App](../../blogs/zh/oleb/how-to-debug-an-app-that-was-launched-by-push-notification-or-url-handler.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/how-to-debug-an-app-that-was-launched-by-push-notification-or-url-handler.md) | 已翻译 |
| 补充资料 | [常數空間反轉二叉樹與仿莫里斯法後序遍歷](../../blogs/zh/maskray/%E5%B8%B8%E6%95%B8%E7%A9%BA%E9%96%93invert-binary-tree%E8%88%87%E4%BB%BFmorris%E6%B3%95%E5%BE%8C%E5%BA%8F%E9%81%8D%E6%AD%B7.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/%E5%B8%B8%E6%95%B8%E7%A9%BA%E9%96%93invert-binary-tree%E8%88%87%E4%BB%BFmorris%E6%B3%95%E5%BE%8C%E5%BA%8F%E9%81%8D%E6%AD%B7.md) | 已翻译 |
| 补充资料 | [弱链接](../../blogs/zh/belkadan/weak-linking.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/weak-linking.md) | 已翻译 |
| 补充资料 | [探索链接器输出中的 section 布局](../../blogs/zh/maskray/exploring-the-section-layout-in-linker-output.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/exploring-the-section-layout-in-linker-output.md) | 已翻译 |
| 补充资料 | [的阴暗面 RISC-V 链接器松弛](../../blogs/zh/maskray/the-dark-side-of-risc-v-linker-relaxation.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/the-dark-side-of-risc-v-linker-relaxation.md) | 已翻译 |
| 补充资料 | [编译器、汇编器和链接器中的长分支](../../blogs/zh/maskray/long-branches-in-compilers-assemblers-and-linkers.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/long-branches-in-compilers-assemblers-and-linkers.md) | 已翻译 |
| 补充资料 | [解析 Mach-O 文件](../../blogs/zh/lowlevelbits/parsing-mach-o-files-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [中文](../../blogs/zh/lowlevelbits/parsing-mach-o-files-low-level-bits.md) | 已翻译 |
| 补充资料 | [解释 GNU 风格的链接器选项](../../blogs/zh/maskray/explain-gnu-style-linker-options.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/explain-gnu-style-linker-options.md) | 已翻译 |
| 补充资料 | [调试 dyld](../../blogs/zh/lowlevelbits/debugging-dyld-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [中文](../../blogs/zh/lowlevelbits/debugging-dyld-low-level-bits.md) | 已翻译 |
| 补充资料 | [通用应用 ≠ 通用二进制](../../blogs/zh/oleb/universal-app-universal-binary.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/universal-app-universal-binary.md) | 已翻译 |
| 补充资料 | [重温 iOS 上的 App 启动序列](../../blogs/zh/oleb/revisiting-the-app-launch-sequence-on-ios.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/revisiting-the-app-launch-sequence-on-ios.md) | 已翻译 |
| 补充资料 | [链接器中的分析与自省选项](../../blogs/zh/maskray/analysis-and-introspection-options-in-linkers.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/analysis-and-introspection-options-in-linkers.md) | 已翻译 |
| 补充资料 | [链接器兼容性与“User-Agent”问题](../../blogs/zh/maskray/linker-compatibility-and-the-user-agent-problem.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/linker-compatibility-and-the-user-agent-problem.md) | 已翻译 |
| 补充资料 | [链接器垃圾回收](../../blogs/zh/maskray/linker-garbage-collection.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/linker-garbage-collection.md) | 已翻译 |
| 补充资料 | [链接器笔记：PE/COFF](../../blogs/zh/maskray/linker-notes-on-pe-coff.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/linker-notes-on-pe-coff.md) | 已翻译 |
| 补充资料 | [面向 Objective-C 开发者的编译器警告](../../blogs/zh/oleb/compiler-warnings-for-objective-c-developers.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/compiler-warnings-for-objective-c-developers.md) | 已翻译 |

## 未翻译资料

共 62 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 官方资料 | [Binary Integer Operators](../../apple-docs/en/swift/binary-integer-operators.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/binary-integer-operators.md) | 待翻译 |
| 官方资料 | [BinaryFloatingPoint Implementations](../../apple-docs/en/swift/binaryfloatingpoint/binaryfloatingpoint-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/binaryfloatingpoint/binaryfloatingpoint-implementations.md) | 待翻译 |
| 官方资料 | [BinaryFloatingPoint Implementations](../../apple-docs/en/swift/float16/binaryfloatingpoint-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/float16/binaryfloatingpoint-implementations.md) | 待翻译 |
| 官方资料 | [BinaryFloatingPoint Implementations](../../apple-docs/en/swift/float80/binaryfloatingpoint-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/float80/binaryfloatingpoint-implementations.md) | 待翻译 |
| 官方资料 | [BinaryFloatingPoint Implementations](../../apple-docs/en/swift/float/binaryfloatingpoint-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/float/binaryfloatingpoint-implementations.md) | 待翻译 |
| 官方资料 | [BinaryFloatingPoint Implementations](../../apple-docs/en/swift/double/binaryfloatingpoint-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/double/binaryfloatingpoint-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/uint64/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint64/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/uint/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/int16/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int16/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/int32/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int32/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/uint32/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint32/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/int/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/binaryinteger/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/binaryinteger/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/int64/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/int64/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/uint16/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint16/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [BinaryInteger Implementations](../../apple-docs/en/swift/uint128/binaryinteger-implementations.md) | Apple 文档 | Apple · Swift | [英文](../../apple-docs/en/swift/uint128/binaryinteger-implementations.md) | 待翻译 |
| 官方资料 | [Build a responsive camera app that launches quickly](../../apple-docs/en/avfoundation/build-a-responsive-camera-app-that-launches-quickly.md) | Apple 文档 | Apple · AVFoundation | [英文](../../apple-docs/en/avfoundation/build-a-responsive-camera-app-that-launches-quickly.md) | 待翻译 |
| 官方资料 | [Compiling binary archives from a custom configuration script](../../apple-docs/en/metal/compiling-binary-archives-from-a-custom-configuration-script.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/compiling-binary-archives-from-a-custom-configuration-script.md) | 待翻译 |
| 官方资料 | [Constraining a tool’s launch environment](../../apple-docs/en/security/constraining-a-tool%27s-launch-environment.md) | Apple 文档 | Apple · Security | [英文](../../apple-docs/en/security/constraining-a-tool%27s-launch-environment.md) | 待翻译 |
| 官方资料 | [Creating binary archives from device-built pipeline state objects](../../apple-docs/en/metal/creating-binary-archives-from-device-built-pipeline-state-objects.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/creating-binary-archives-from-device-built-pipeline-state-objects.md) | 待翻译 |
| 官方资料 | [Customizing a document-based app’s launch experience](../../apple-docs/en/uikit/customizing-a-document-based-app-s-launch-experience.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/customizing-a-document-based-app-s-launch-experience.md) | 待翻译 |
| 官方资料 | [Launch options dictionary keys](../../apple-docs/en/mapkit/launch-options-dictionary-keys.md) | Apple 文档 | Apple · MapKit | [英文](../../apple-docs/en/mapkit/launch-options-dictionary-keys.md) | 待翻译 |
| 官方资料 | [Launching your app from a Live Activity](../../apple-docs/en/activitykit/launching-your-app-from-a-live-activity.md) | Apple 文档 | Apple · ActivityKit | [英文](../../apple-docs/en/activitykit/launching-your-app-from-a-live-activity.md) | 待翻译 |
| 官方资料 | [Linking Data Between Two Core Data Stores](../../apple-docs/en/coredata/linking-data-between-two-core-data-stores.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/linking-data-between-two-core-data-stores.md) | 待翻译 |
| 官方资料 | [Linking to specific app scenes from your widget or Live Activity](../../apple-docs/en/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity.md) | Apple 文档 | Apple · WidgetKit | [英文](../../apple-docs/en/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity.md) | 待翻译 |
| 官方资料 | [Manipulating Metal binary archives](../../apple-docs/en/metal/manipulating-metal-binary-archives.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/manipulating-metal-binary-archives.md) | 待翻译 |
| 官方资料 | [Metal binary archives](../../apple-docs/en/metal/metal-binary-archives.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/metal-binary-archives.md) | 待翻译 |
| 官方资料 | [Preserving your app’s model data across launches](../../apple-docs/en/swiftdata/preserving-your-apps-model-data-across-launches.md) | Apple 文档 | Apple · SwiftData | [英文](../../apple-docs/en/swiftdata/preserving-your-apps-model-data-across-launches.md) | 待翻译 |
| 官方资料 | [Preserving your app’s UI across launches](../../apple-docs/en/uikit/preserving-your-app-s-ui-across-launches.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/preserving-your-app-s-ui-across-launches.md) | 待翻译 |
| 官方资料 | [Responding to the launch of your app](../../apple-docs/en/uikit/responding-to-the-launch-of-your-app.md) | Apple 文档 | Apple · UIKit | [英文](../../apple-docs/en/uikit/responding-to-the-launch-of-your-app.md) | 待翻译 |
| 官方资料 | [Testing ad attributions with a downloaded profile](../../apple-docs/en/storekit/testing-ad-attributions-with-a-downloaded-profile.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-ad-attributions-with-a-downloaded-profile.md) | 待翻译 |
| 深度补充 | [Mach-O 可执行文件](../../blogs/en/objcio/mach-o-executables.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/mach-o-executables.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [UIApplicationDelegate launchOptions](../../blogs/en/nshipster/uiapplicationdelegate-launchoptions.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/uiapplicationdelegate-launchoptions.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [优化 iPhone 上超大表格的加载 \| Cocoa with Love](../../blogs/en/cocoawithlove/optimizing-the-loading-of-a-very-large-table-on-the-iphone-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/optimizing-the-loading-of-a-very-large-table-on-the-iphone-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [启动参数与环境变量](../../blogs/en/nshipster/launch-arguments-br-environment-variables.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/launch-arguments-br-environment-variables.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [在 macOS Sierra 上编译 Mac OS 8 应用程序](../../blogs/en/cocoawithlove/compiling-a-mac-os-8-application-on-macos-sierra-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/compiling-a-mac-os-8-application-on-macos-sierra-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [星期五问答 2011-04-15：编译时技巧与窍门](../../blogs/en/mikeash/friday-q-a-2011-04-15-compile-time-tips-and-tricks.md) | 技术博客 | mikeash.com Friday Q&A | [英文](../../blogs/en/mikeash/friday-q-a-2011-04-15-compile-time-tips-and-tricks.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [星期五问答 2013-06-28：编译器 Bug 剖析](../../blogs/en/mikeash/friday-q-a-2013-06-28-anatomy-of-a-compiler-bug.md) | 技术博客 | mikeash.com Friday Q&A | [英文](../../blogs/en/mikeash/friday-q-a-2013-06-28-anatomy-of-a-compiler-bug.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [编译器](../../blogs/en/objcio/the-compiler.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/the-compiler.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [72 小时内上线 Celebrate Pride](../../blogs/en/fbeng/72-hours-to-launch-celebrate-pride.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/72-hours-to-launch-celebrate-pride.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Apple 禁止 iPhone 开发使用交叉编译器](../../blogs/en/oleb/apple-bans-cross-compilers-for-iphone-development.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/apple-bans-cross-compilers-for-iphone-development.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Compiling Ruby. 第 1 部分：编译器与解释器](../../blogs/en/lowlevelbits/compiling-ruby-part-1-compilers-vs-interpreters-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/compiling-ruby-part-1-compilers-vs-interpreters-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Compiling Ruby. 第 3 部分：MLIR 与编译](../../blogs/en/lowlevelbits/compiling-ruby-part-3-mlir-and-compilation-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/compiling-ruby-part-3-mlir-and-compilation-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [GCC 13.3.0 误编译 LLVM](../../blogs/en/maskray/gcc-13-3-0-miscompiles-llvm.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/gcc-13-3-0-miscompiles-llvm.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Hackerrank FP Compilers 题目](../../blogs/en/maskray/hackerrank-fp-compilers%E9%A2%98%E7%9B%AE.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/hackerrank-fp-compilers%E9%A2%98%E7%9B%AE.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [iOS 上的受限即时编译](../../blogs/en/saagarjha/jailed-just-in-time-compilation-on-ios.md) | 技术博客 | Saagar Jha | [英文](../../blogs/en/saagarjha/jailed-just-in-time-compilation-on-ios.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [优化 Facebook iOS 启动时间](../../blogs/en/fbeng/optimizing-facebook-for-ios-start-time.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/optimizing-facebook-for-ios-start-time.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [使用 Clang API 编译 C++](../../blogs/en/maskray/compiling-c-with-the-clang-api.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/compiling-c-with-the-clang-api.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [修改条件/决策覆盖（MC/DC）及编译器实现](../../blogs/en/maskray/modified-condition-decision-coverage-mc-dc-and-compiler-implementations.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/modified-condition-decision-coverage-mc-dc-and-compiler-implementations.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [在 Xcode 9 中测量 Swift 编译时间](../../blogs/en/jessesquires/measuring-swift-compile-times-in-xcode-9.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/measuring-swift-compile-times-in-xcode-9.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [如何学习编译器：LLVM 版](../../blogs/en/lowlevelbits/how-to-learn-compilers-llvm-edition-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/how-to-learn-compilers-llvm-edition-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [学习编译器和 LLVM 的资源](../../blogs/en/jessesquires/resources-for-learning-about-compilers-and-llvm.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/resources-for-learning-about-compilers-and-llvm.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [将 Metal 着色器位码编译为 x86 和 ARM 汇编](../../blogs/en/worthdoingbadly/compile-metal-shader-bitcode-to-x86-and-arm-assembly.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [英文](../../blogs/en/worthdoingbadly/compile-metal-shader-bitcode-to-x86-and-arm-assembly.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [我的小优化：编译器是魔法](../../blogs/en/belkadan/my-little-optimization-the-compiler-is-magic.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [英文](../../blogs/en/belkadan/my-little-optimization-the-compiler-is-magic.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [所以你想成为（编译器的）巫师](../../blogs/en/belkadan/so-you-want-to-be-a-compiler-wizard.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [英文](../../blogs/en/belkadan/so-you-want-to-be-a-compiler-wizard.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [教程——在 QEMU 中模拟 iOS 内核直至 launchd 和用户空间](../../blogs/en/worthdoingbadly/tutorial-emulate-an-ios-kernel-in-qemu-up-to-launchd-and-userspace.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [英文](../../blogs/en/worthdoingbadly/tutorial-emulate-an-ios-kernel-in-qemu-up-to-launchd-and-userspace.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [深入探讨 Clang 的源文件编译](../../blogs/en/maskray/a-deep-dive-into-clang-s-source-file-compilation.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/a-deep-dive-into-clang-s-source-file-compilation.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [用 Storyboard 替换启动图像](../../blogs/en/oleb/replacing-launch-images-with-storyboards.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/replacing-launch-images-with-storyboards.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [编译器](../../blogs/en/belkadan/compilers.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [英文](../../blogs/en/belkadan/compilers.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [编译器输出文件](../../blogs/en/maskray/compiler-output-files.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/compiler-output-files.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [编译器驱动与交叉编译](../../blogs/en/maskray/compiler-driver-and-cross-compilation.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/compiler-driver-and-cross-compilation.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [预编译头文件](../../blogs/en/maskray/precompiled-headers.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/precompiled-headers.md) | 仅标题中文，正文待翻译 |
