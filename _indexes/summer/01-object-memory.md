# 模块 1：对象模型与进程内存地图

> 从虚拟地址空间、对象布局和 isa 链建立 Objective-C 对象模型。
> 对应仓库范围：Objective-C Runtime、内存与 ARC。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 1.1 | 进程虚拟地址空间；代码段、全局/静态区、堆、栈；对象通常在哪里 | 一张“iOS 进程内存地图”，注明“五区”是教学抽象，不是内核唯一真实划分 |
| 1.2 | `NSObject` 实例布局、`objc_object`、`isa`、`objc_class`、class / metaclass | 实例 → 类 → 元类、类 → 父类、元类 → 父元类结构图 |
| 1.3 | 继承链：类、父类、元类、根元类；`object_getClass` 与 `class_getSuperclass` | LLDB 输出记录，解释每一步为什么这样走 |
| 1.4 | `isMemberOfClass:` / `isKindOfClass:` 在实例对象和类对象上的差异 | 8 组判断题，必须沿链推导，不背结果表 |
| 1.5 | Tagged Pointer 与内存对齐 | 短/长 `NSString`、小/大 `NSNumber` 地址、class、`malloc_size` 对照表 |

## 计划指定材料

- [内存与虚拟内存](../../legacy-archive/zh/documentation/Darwin/Kernel%20Programming%20Guide/Memory%20and%20Virtual%20Memory.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Darwin/Kernel%20Programming%20Guide/Memory%20and%20Virtual%20Memory.md) — Apple 旧归档
- [关于 Objective-C](../../legacy-archive/zh/documentation/Cocoa/Programming%20with%20Objective-C/About%20Objective-C.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Programming%20with%20Objective-C/About%20Objective-C.md) — Apple 旧归档
- [Objective-C 运行时的进展](../../wwdc/zh/wwdc2020/10163-advancements-in-the-objective-c-runtime.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/wwdc/zh/wwdc2020/10163-advancements-in-the-objective-c-runtime.md) — 本仓库资料
- [计划材料](https://developer.apple.com/documentation/objectivec/nsobject) — Apple 现行文档（未归档）
- [Objective-C 内部探秘：类的架构](../../blogs/zh/alwaysprocessing/objective-c-internals-class-architecture-objective-c-has-an-unique-class-architecture-wher.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/alwaysprocessing/objective-c-internals-class-architecture-objective-c-has-an-unique-class-architecture-wher.md) — 本仓库资料
- [Objective-C 内部实现：isa 指针的多种用途](../../blogs/zh/alwaysprocessing/objective-c-internals-the-many-uses-of-isa-the-objective-c-runtime-optimizes-performance-b.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/alwaysprocessing/objective-c-internals-the-many-uses-of-isa-the-objective-c-runtime-optimizes-performance-b.md) — 本仓库资料
- [Objective-C 内部机制：Tagged Pointer 对象](../../blogs/zh/alwaysprocessing/objective-c-internals-tagged-pointer-objects-tagged-pointer-objects-a-private-runtime-feat.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/alwaysprocessing/objective-c-internals-tagged-pointer-objects-tagged-pointer-objects-a-private-runtime-feat.md) — 本仓库资料
- [大小问题：iOS 虚拟内存探究](../../blogs/zh/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md) — 本仓库资料
- [Friday Q&A 2010-01-15：Objective-C 中的栈对象与堆对象](../../blogs/zh/mikeash/friday-q-a-2010-01-15-stack-and-heap-objects-in-objective-c.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2010-01-15-stack-and-heap-objects-in-objective-c.md) — 本仓库资料
- [计划材料](https://juejin.cn/post/6963188936508178469) — 第三方博客（未归档（juejin.cn））
- [Objective-C 内部实现：类图实现](../../blogs/zh/alwaysprocessing/objective-c-internals-class-graph-implementation-a-brief-look-at-the-objective-c-runtime-s.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/alwaysprocessing/objective-c-internals-class-graph-implementation-a-brief-look-at-the-objective-c-runtime-s.md) — 本仓库资料
- [计划材料](https://draven.co/isa/) — 第三方博客（未归档（draven.co））
- [计划材料](https://blog.devtang.com/2013/10/15/objective-c-object-model/) — 第三方博客（未归档（blog.devtang.com））
- [什么是 Objective-C 中的元类？ | Cocoa with Love](../../blogs/zh/cocoawithlove/what-is-a-meta-class-in-objective-c-cocoa-with-love.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/cocoawithlove/what-is-a-meta-class-in-objective-c-cocoa-with-love.md) — 本仓库资料
- [Friday Q&A 2014-07-18：探索 Swift 内存布局](../../blogs/zh/mikeash/previous.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/previous.md) — 本仓库资料
- [[objc explain]：非指针 isa](../../blogs/zh/sealiesoftware/objc-explain-non-pointer-isa.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/sealiesoftware/objc-explain-non-pointer-isa.md) — 本仓库资料
- [计划材料](https://github.com/apple-oss-distributions/objc4) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://www.cnblogs.com/xgao/p/11277935.html) — 第三方博客（未归档（cnblogs.com））
- [计划材料](https://www.0daybug.com/posts/9972ffa7/index.html) — 第三方博客（未归档（0daybug.com））
- [计划材料](https://roadmap.isylar.com/iOS/Knowledge/RuntimeCls.html) — 第三方博客（未归档（roadmap.isylar.com））
- [计划材料](https://clang.llvm.org/docs/AttributeReference.html#aligned) — 第三方博客（未归档（clang.llvm.org））
- [Friday Q&A 2012-07-27：构建 Tagged Pointer](../../blogs/zh/mikeash/tagged-pointers.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/tagged-pointers.md) — 本仓库资料
- [Friday Q&A 2015-07-31：Tagged Pointer Strings](../../blogs/zh/mikeash/friday-q-a-2015-07-31-tagged-pointer-strings.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2015-07-31-tagged-pointer-strings.md) — 本仓库资料
- [计划材料](https://blog.devtang.com/2014/05/30/understand-tagged-pointer/) — 第三方博客（未归档（blog.devtang.com））
- [计划材料](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/) — 第三方博客（未归档（blog.timac.org））

## 中文资料

共 69 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [iOS 内存分区-- 栈、堆、全局区、常量区、代码区](../../blogs/snapshots/juejin.cn/ios-%E5%86%85%E5%AD%98%E5%88%86%E5%8C%BA-%E6%A0%88-%E5%A0%86-%E5%85%A8%E5%B1%80%E5%8C%BA-%E5%B8%B8%E9%87%8F%E5%8C%BA-%E4%BB%A3%E7%A0%81%E5%8C%BA.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/juejin.cn/ios-%E5%86%85%E5%AD%98%E5%88%86%E5%8C%BA-%E6%A0%88-%E5%A0%86-%E5%85%A8%E5%B1%80%E5%8C%BA-%E5%B8%B8%E9%87%8F%E5%8C%BA-%E4%BB%A3%E7%A0%81%E5%8C%BA.md) | 原生中文 |
| 计划核心 | [isKindOfClass & isMemberOfClass 的分析](../../blogs/snapshots/0daybug.com/iskindofclass-ismemberofclass-%E7%9A%84%E5%88%86%E6%9E%90.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/0daybug.com/iskindofclass-ismemberofclass-%E7%9A%84%E5%88%86%E6%9E%90.md) | 原生中文 |
| 计划核心 | [【OC底层】isMemberOfClass、isKindOfClass原理分析](../../blogs/snapshots/cnblogs.com/oc%E5%BA%95%E5%B1%82-ismemberofclass-iskindofclass%E5%8E%9F%E7%90%86%E5%88%86%E6%9E%90.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/oc%E5%BA%95%E5%B1%82-ismemberofclass-iskindofclass%E5%8E%9F%E7%90%86%E5%88%86%E6%9E%90.md) | 原生中文 |
| 计划核心 | [免责声明](../../blogs/snapshots-zh/blog.timac.org/testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/blog.timac.org/testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object.md) | 已翻译 |
| 官方资料 | [Core Data 栈](../../apple-docs/zh/coredata/core-data-stack.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/core-data-stack.md) | 已翻译 |
| 官方资料 | [为稀疏纹理分配内存](../../apple-docs/zh/metal/assigning-memory-to-sparse-textures.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/assigning-memory-to-sparse-textures.md) | 已翻译 |
| 官方资料 | [优化内存性能](../../apple-docs/zh/uikit/optimizing-memory-performance.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/optimizing-memory-performance.md) | 已翻译 |
| 官方资料 | [使用已释放的内存](../../apple-docs/zh/xcode/use-of-deallocated-memory.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/use-of-deallocated-memory.md) | 已翻译 |
| 官方资料 | [使用超出作用域的栈内存](../../apple-docs/zh/xcode/use-of-out-of-scope-stack-memory.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/use-of-out-of-scope-stack-memory.md) | 已翻译 |
| 官方资料 | [内存](../../apple-docs/zh/kernel/iokit_fundamentals/memory.md) | Apple 文档 | Apple · Kernel | [中文](../../apple-docs/zh/kernel/iokit_fundamentals/memory.md) | 已翻译 |
| 官方资料 | [内存分配选项](../../apple-docs/zh/foundation/1539826-memory-allocation-options.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/1539826-memory-allocation-options.md) | 已翻译 |
| 官方资料 | [内存堆](../../apple-docs/zh/metal/memory-heaps.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/memory-heaps.md) | 已翻译 |
| 官方资料 | [内存管理函数](../../apple-docs/zh/foundation/memory-management-functions.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/memory-management-functions.md) | 已翻译 |
| 官方资料 | [减小 Metal App 的内存占用空间](../../apple-docs/zh/metal/reducing-the-memory-footprint-of-metal-apps.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/reducing-the-memory-footprint-of-metal-apps.md) | 已翻译 |
| 官方资料 | [减少 App 的内存使用](../../apple-docs/zh/xcode/reducing-your-app-s-memory-use.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/reducing-your-app-s-memory-use.md) | 已翻译 |
| 官方资料 | [函数返回后使用栈内存](../../apple-docs/zh/xcode/use-of-stack-memory-after-function-return.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/use-of-stack-memory-after-function-return.md) | 已翻译 |
| 官方资料 | [分析 Metal App 的内存使用情况](../../apple-docs/zh/xcode/analyzing-the-memory-usage-of-your-metal-app.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/analyzing-the-memory-usage-of-your-metal-app.md) | 已翻译 |
| 官方资料 | [分析内存使用情况](../../apple-docs/zh/xcode/analyzing-memory-usage.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/analyzing-memory-usage.md) | 已翻译 |
| 官方资料 | [响应低内存警告](../../apple-docs/zh/xcode/responding-to-low-memory-warnings.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/responding-to-low-memory-warnings.md) | 已翻译 |
| 官方资料 | [响应内存警告](../../apple-docs/zh/uikit/responding-to-memory-warnings.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/responding-to-memory-warnings.md) | 已翻译 |
| 官方资料 | [将网站数据获取到内存中](../../apple-docs/zh/foundation/fetching-website-data-into-memory.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/fetching-website-data-into-memory.md) | 已翻译 |
| 官方资料 | [尽早诊断内存、线程和崩溃问题](../../apple-docs/zh/xcode/diagnosing-memory-thread-and-crash-issues-early.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/diagnosing-memory-thread-and-crash-issues-early.md) | 已翻译 |
| 官方资料 | [已释放内存的重复释放](../../apple-docs/zh/xcode/deallocation-of-deallocated-memory.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/deallocation-of-deallocated-memory.md) | 已翻译 |
| 官方资料 | [手动内存管理](../../apple-docs/zh/swift/manual-memory-management.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/manual-memory-management.md) | 已翻译 |
| 官方资料 | [手动设置 Core Data 堆栈](../../apple-docs/zh/coredata/setting-up-a-core-data-stack-manually.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/setting-up-a-core-data-stack-manually.md) | 已翻译 |
| 官方资料 | [收集内存使用信息](../../apple-docs/zh/xcode/gathering-information-about-memory-use.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/gathering-information-about-memory-use.md) | 已翻译 |
| 官方资料 | [未分配内存的释放](../../apple-docs/zh/xcode/deallocation-of-nonallocated-memory.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/deallocation-of-nonallocated-memory.md) | 已翻译 |
| 官方资料 | [未对齐指针](../../apple-docs/zh/xcode/misaligned-pointer.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/misaligned-pointer.md) | 已翻译 |
| 官方资料 | [根据 GPU 内存带宽权衡进行调整](../../apple-docs/zh/metal/adjusting-for-gpu-memory-bandwidth-tradeoffs.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/adjusting-for-gpu-memory-bandwidth-tradeoffs.md) | 已翻译 |
| 官方资料 | [测量 GPU 对内存带宽的使用](../../apple-docs/zh/xcode/measuring-the-gpus-use-of-memory-bandwidth.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/measuring-the-gpus-use-of-memory-bandwidth.md) | 已翻译 |
| 官方资料 | [管理稀疏纹理内存](../../apple-docs/zh/metal/managing-sparse-texture-memory.md) | Apple 文档 | Apple · Metal | [中文](../../apple-docs/zh/metal/managing-sparse-texture-memory.md) | 已翻译 |
| 官方资料 | [调查内存访问崩溃](../../apple-docs/zh/xcode/investigating-memory-access-crashes.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/investigating-memory-access-crashes.md) | 已翻译 |
| 官方资料 | [进行更改以减少内存使用](../../apple-docs/zh/xcode/making-changes-to-reduce-memory-use.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/making-changes-to-reduce-memory-use.md) | 已翻译 |
| 官方资料 | [通过 jetsam 事件报告识别高内存使用情况](../../apple-docs/zh/xcode/identifying-high-memory-use-with-jetsam-event-reports.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/identifying-high-memory-use-with-jetsam-event-reports.md) | 已翻译 |
| 官方资料 | [配置 Core Data 栈](../../apple-docs/zh/coredata/setting-up-a-core-data-stack.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/setting-up-a-core-data-stack.md) | 已翻译 |
| 官方资料 | [采用类型感知内存分配](../../apple-docs/zh/xcode/adopting-type-aware-memory-allocation.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/adopting-type-aware-memory-allocation.md) | 已翻译 |
| 官方资料 | [防止内存使用衰退](../../apple-docs/zh/xcode/preventing-memory-use-regressions.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/preventing-memory-use-regressions.md) | 已翻译 |
| 官方资料 | [iOS 内存深入详解](../../wwdc/zh/wwdc2018/416-ios-memory-deep-dive.md) | WWDC | Apple · WWDC2018 | [中文](../../wwdc/zh/wwdc2018/416-ios-memory-deep-dive.md) | 已翻译 |
| 官方资料 | [使用 Swift 改善内存使用与性能](../../wwdc/zh/wwdc2025/312-improve-memory-usage-and-performance-with-swift.md) | WWDC | Apple · WWDC2025 | [中文](../../wwdc/zh/wwdc2025/312-improve-memory-usage-and-performance-with-swift.md) | 已翻译 |
| 官方资料 | [分析堆内存](../../wwdc/zh/wwdc2024/10173-analyze-heap-memory.md) | WWDC | Apple · WWDC2024 | [中文](../../wwdc/zh/wwdc2024/10173-analyze-heap-memory.md) | 已翻译 |
| 官方资料 | [检测和诊断内存问题](../../wwdc/zh/wwdc2021/10180-detect-and-diagnose-memory-issues.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10180-detect-and-diagnose-memory-issues.md) | 已翻译 |
| 官方资料 | [通过内存完整性强制增强 App 的安全性](../../wwdc/zh/meet-with-apple/206-secure-your-app-with-memory-integrity-enforcement.md) | WWDC | Apple · MEET-WITH-APPLE | [中文](../../wwdc/zh/meet-with-apple/206-secure-your-app-with-memory-integrity-enforcement.md) | 已翻译 |
| 深度补充 | [Objective-C 中的元类是什么？ \| Cocoa with Love](../../blogs/zh/cocoawithlove/what-is-a-meta-class-in-objective-c-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/what-is-a-meta-class-in-objective-c-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Objective-C 内部实现：isa 指针的多种用途](../../blogs/zh/alwaysprocessing/objective-c-internals-the-many-uses-of-isa-the-objective-c-runtime-optimizes-performance-b.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/objective-c-internals-the-many-uses-of-isa-the-objective-c-runtime-optimizes-performance-b.md) | 已翻译 |
| 深度补充 | [Objective-C 内部机制：Tagged Pointer 对象](../../blogs/zh/alwaysprocessing/objective-c-internals-tagged-pointer-objects-tagged-pointer-objects-a-private-runtime-feat.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/objective-c-internals-tagged-pointer-objects-tagged-pointer-objects-a-private-runtime-feat.md) | 已翻译 |
| 深度补充 | [Tagged pointers](../../blogs/zh/mikeash/tagged-pointers.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/tagged-pointers.md) | 已翻译 |
| 深度补充 | [内存和线程安全的自定义属性方法 \| Cocoa with Love](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [在 Swift 中使用堆栈跟踪追踪任务 \| Cocoa with Love](../../blogs/zh/cocoawithlove/tracking-tasks-with-stack-traces-in-swift-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/tracking-tasks-with-stack-traces-in-swift-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [大小问题：iOS 虚拟内存探究](../../blogs/zh/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-06-19：Mac OS X 进程内存统计](../../blogs/zh/mikeash/friday-q-a-2009-06-19-mac-os-x-process-memory-statistics.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-06-19-mac-os-x-process-memory-statistics.md) | 已翻译 |
| 深度补充 | [星期五问答 2010-01-15：Objective-C 中的栈对象与堆对象](../../blogs/zh/mikeash/friday-q-a-2010-01-15-stack-and-heap-objects-in-objective-c.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2010-01-15-stack-and-heap-objects-in-objective-c.md) | 已翻译 |
| 深度补充 | [星期五问答 2012-02-17：环形缓冲区和镜像内存：第二部分](../../blogs/zh/mikeash/friday-q-a-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.md) | 已翻译 |
| 深度补充 | [星期五问答 2012-04-13：Nib 内存管理](../../blogs/zh/mikeash/friday-q-a-2012-04-13-nib-memory-management.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2012-04-13-nib-memory-management.md) | 已翻译 |
| 深度补充 | [星期五问答 2012-05-04：PLCrashReporter 与使用 DWARF 展开堆栈，第二部分](../../blogs/zh/mikeash/friday-q-a-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.md) | 已翻译 |
| 深度补充 | [星期五问答 2012-12-28：加载一个内存字节时会发生什么](../../blogs/zh/mikeash/friday-q-a-2012-12-28-what-happens-when-you-load-a-byte-of-memory.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2012-12-28-what-happens-when-you-load-a-byte-of-memory.md) | 已翻译 |
| 深度补充 | [星期五问答 2014-05-23：受 Heartbleed 启发的偏执型内存分配器](../../blogs/zh/mikeash/friday-q-a-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.md) | 已翻译 |
| 深度补充 | [星期五问答 2014-08-29：Swift 内存转储](../../blogs/zh/mikeash/friday-q-a-2014-08-29-swift-memory-dumping.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2014-08-29-swift-memory-dumping.md) | 已翻译 |
| 深度补充 | [星期五问答 2015-05-29：Objective-C 运行时的并发内存释放](../../blogs/zh/mikeash/friday-q-a-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.md) | 已翻译 |
| 深度补充 | [星期五问答 2015-07-31：标记指针字符串](../../blogs/zh/mikeash/friday-q-a-2015-07-31-tagged-pointer-strings.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2015-07-31-tagged-pointer-strings.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 类与元类](../../blogs/zh/sealiesoftware/objc-explain-classes-and-metaclasses.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-classes-and-metaclasses.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 非指针 isa](../../blogs/zh/sealiesoftware/objc-explain-non-pointer-isa.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-non-pointer-isa.md) | 已翻译 |
| 补充资料 | [iOS 上的自动内存泄漏检测](../../blogs/zh/fbeng/automatic-memory-leak-detection-on-ios.md) | 技术博客 | Meta Engineering — iOS | [中文](../../blogs/zh/fbeng/automatic-memory-leak-detection-on-ios.md) | 已翻译 |
| 补充资料 | [Objective-C 对象模型](../../blogs/zh/leichunfeng/objective-c-%E5%AF%B9%E8%B1%A1%E6%A8%A1%E5%9E%8B.md) | 技术博客 | 雷纯锋 | [中文](../../blogs/zh/leichunfeng/objective-c-%E5%AF%B9%E8%B1%A1%E6%A8%A1%E5%9E%8B.md) | 原生中文 |
| 补充资料 | [Swift Runtime: 堆对象](../../blogs/zh/belkadan/the-swift-runtime-heap-objects.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/the-swift-runtime-heap-objects.md) | 已翻译 |
| 补充资料 | [内存泄漏：一个 Xcode 侦探故事](../../blogs/zh/emergetools/emerge-tools-blog-the-memory-leak-an-xcode-detective-story.md) | 技术博客 | Emerge Tools Blog | [中文](../../blogs/zh/emergetools/emerge-tools-blog-the-memory-leak-an-xcode-detective-story.md) | 已翻译 |
| 补充资料 | [在不将图像加载到内存的情况下访问图像属性](../../blogs/zh/oleb/accessing-image-properties-without-loading-the-image-into-memory.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/accessing-image-properties-without-loading-the-image-into-memory.md) | 已翻译 |
| 补充资料 | [垃圾回收器与栈抽屉](../../blogs/zh/belkadan/garbage-collectors-and-stack-drawers.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/garbage-collectors-and-stack-drawers.md) | 已翻译 |
| 补充资料 | [栈展开](../../blogs/zh/maskray/stack-unwinding.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/stack-unwinding.md) | 已翻译 |
| 补充资料 | [栈遍历：空间与时间的权衡](../../blogs/zh/maskray/stack-walking-space-and-time-trade-offs.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/stack-walking-space-and-time-trade-offs.md) | 已翻译 |

## 未翻译资料

共 0 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
