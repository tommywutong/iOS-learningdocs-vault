# 模块 2：所有权、ARC、weak、属性与 Block

> 把内存管理关键字还原为所有权关系、编译器变换和运行时数据结构。
> 对应仓库范围：内存与 ARC、Block 与闭包。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 2.1 | MRC ownership rules；`retain/release/autorelease`；ARC 删除了什么代码 | 同一段代码的 MRC/ARC 两版，逐行标注谁拥有对象 |
| 2.2 | ARC 的编译期与运行期协作：`objc_retain`、`objc_release`、返回值优化、对象销毁路径 | `clang -S -emit-llvm -fobjc-arc` 调用点记录；ARC 责任边界图 |
| 2.3 | 属性关键字：`strong/copy/weak/assign/unsafe_unretained/atomic/nonatomic/readwrite/readonly` | 属性关键字决策表，包含 setter 语义、适用对象、风险、线程安全边界 |
| 2.4 | 深浅拷贝、`NSCopying`、`NSMutableString` strong/copy、delegate weak、Block copy | 四组属性选择实验 |
| 2.5 | weak 引入、本质、SideTable、weak table、注册、读取、销毁置 nil | `objc_storeWeak` → 注册 → 读取 → `clearDeallocating` 时序图 |
| 2.6 | Block ABI、descriptor、invoke、global / stack / malloc Block、调用流程 | `clang -rewrite-objc` 对照无捕获和有捕获 Block |
| 2.7 | Block 捕获：自动变量、静态变量、对象、`__block`；ARC 下复制与释放 | 四种捕获实验 + 捕获前后内存图 |
| 2.8 | Block 循环引用、weak-strong dance、判空规范和竞态边界 | 修复 3 个循环引用例子；写出安全调用模板并解释限制 |

## 计划指定材料

- [内存管理策略](../../legacy-archive/zh/documentation/Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/Memory%20Management%20Policy.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Advanced%20Memory%20Management%20Programming%20Guide/Memory%20Management%20Policy.md) — Apple 旧归档
- [计划材料](https://clang.llvm.org/docs/AutomaticReferenceCounting.html) — 第三方博客（未归档（clang.llvm.org））
- [封装数据](../../legacy-archive/zh/documentation/Cocoa/Programming%20with%20Objective-C/Encapsulating%20Data.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Programming%20with%20Objective-C/Encapsulating%20Data.md) — Apple 旧归档
- [NSCopying](../../apple-docs/zh/foundation/nscopying.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/nscopying.md) — 本仓库资料
- [引言](../../legacy-archive/zh/documentation/Cocoa/Blocks%20Programming%20Topics/Introduction.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Blocks%20Programming%20Topics/Introduction.md) — Apple 旧归档
- [Block 与变量](../../legacy-archive/zh/documentation/Cocoa/Blocks%20Programming%20Topics/Blocks%20and%20Variables.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Blocks%20Programming%20Topics/Blocks%20and%20Variables.md) — Apple 旧归档
- [使用 Block](../../legacy-archive/zh/documentation/Cocoa/Programming%20with%20Objective-C/Working%20with%20Blocks.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Programming%20with%20Objective-C/Working%20with%20Blocks.md) — Apple 旧归档
- [计划材料](https://clang.llvm.org/docs/Block-ABI-Apple.html) — 第三方博客（未归档（clang.llvm.org））
- [Objective-C 内部实现：Retain](../../blogs/zh/alwaysprocessing/objective-c-internals-retain-objective-c-memory-is-managed-through-a-reference-counting-sc.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/alwaysprocessing/objective-c-internals-retain-objective-c-memory-is-managed-through-a-reference-counting-sc.md) — 本仓库资料
- [Friday Q&A 2011-09-30: 自动引用计数（Automatic Reference Counting）](../../blogs/zh/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md) — 本仓库资料
- [Friday Q&A 2008-12-26：Blocks 初探](../../blogs/zh/mikeash/friday-q-a-2008-12-26.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2008-12-26.md) — 本仓库资料
- [计划材料](https://www.jianshu.com/p/809a9bca597f) — 第三方博客（未归档（jianshu.com））
- [计划材料](https://draven.co/rr/) — 第三方博客（未归档（draven.co））
- [计划材料](https://draven.co/autoreleasepool/) — 第三方博客（未归档（draven.co））
- [黑幕背后的Autorelease](../../blogs/zh/sunnyxx/%E9%BB%91%E5%B9%95%E8%83%8C%E5%90%8E%E7%9A%84autorelease-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/sunnyxx/%E9%BB%91%E5%B9%95%E8%83%8C%E5%90%8E%E7%9A%84autorelease-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) — 本仓库资料
- [Friday Q&A 2011-09-02：让我们构建 NSAutoreleasePool](../../blogs/zh/mikeash/friday-q-a-2011-09-02-let-s-build-nsautoreleasepool.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2011-09-02-let-s-build-nsautoreleasepool.md) — 本仓库资料
- [ARC下dealloc过程及.cxxdestruct的探究](../../blogs/zh/sunnyxx/arc%E4%B8%8Bdealloc%E8%BF%87%E7%A8%8B%E5%8F%8A-cxx-destruct%E7%9A%84%E6%8E%A2%E7%A9%B6-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/sunnyxx/arc%E4%B8%8Bdealloc%E8%BF%87%E7%A8%8B%E5%8F%8A-cxx-destruct%E7%9A%84%E6%8E%A2%E7%A9%B6-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) — 本仓库资料
- [Value Objects](../../blogs/en/objcio/value-objects.md) · [原文网页](https://www.objc.io/issues/7-foundation/value-objects/) — 第三方博客
- [Objective-C 引用计数原理](../../blogs/zh/yulingtianxia/objective-c-%E5%BC%95%E7%94%A8%E8%AE%A1%E6%95%B0%E5%8E%9F%E7%90%86.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/yulingtianxia/objective-c-%E5%BC%95%E7%94%A8%E8%AE%A1%E6%95%B0%E5%8E%9F%E7%90%86.md) — 本仓库资料
- [计划材料](https://cloud.tencent.com/developer/article/2303898) — 第三方博客（未归档（cloud.tencent.com））
- [计划材料](https://github.com/pro648/tips/wiki/iOS%E4%B8%AD%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7%E6%97%B6%E7%9A%84atomic%E3%80%81nonatomic%E3%80%81copy%E3%80%81assign%E3%80%81strong%E3%80%81weak%E7%AD%89%E5%87%A0%E4%B8%AA%E7%89%B9%E6%80%A7%E7%9A%84%E5%8C%BA%E5%88%AB) — GitHub 源码（待 clone 到 oss/）
- [Friday Q&A 2010-07-16：Objective-C 中的归零弱引用](../../blogs/zh/mikeash/my-friday-q-a-post-this-week.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/my-friday-q-a-post-this-week.md) — 本仓库资料
- [计划材料](https://github.com/Desgard/iOS-Source-Probe/blob/master/Objective-C/Runtime/weak%20%E5%BC%B1%E5%BC%95%E7%94%A8%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F.md) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://blog.csdn.net/u013378438/article/details/82790332) — 第三方博客（未归档（blog.csdn.net））
- [计划材料](https://www.uiimage.com/post/blog/ios/sidetables/) — 第三方博客（未归档（uiimage.com））
- [计划材料](https://verdagon.dev/blog/surprising-weak-refs) — 第三方博客（未归档（verdagon.dev））
- [Friday Q&A 2017-09-22：Swift 4 弱引用](../../blogs/zh/mikeash/friday-q-a-2017-09-22-swift-4-weak-references.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2017-09-22-swift-4-weak-references.md) — 本仓库资料
- [计划材料](https://github.com/apple-oss-distributions/objc4/blob/main/runtime/objc-weak.mm) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://github.com/Desgard/iOS-Source-Probe/blob/master/Objective-C/Runtime/%E6%B5%85%E8%B0%88%20block%EF%BC%881%EF%BC%89%20-%20clang%20%E6%94%B9%E5%86%99%E5%90%8E%E7%9A%84%20block%20%E7%BB%93%E6%9E%84.md) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://www.jianshu.com/p/f0870fa95aac) — 第三方博客（未归档（jianshu.com））
- [计划材料](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=12) — 第三方博客（未归档（informit.com））
- [计划材料](https://github.com/Desgard/iOS-Source-Probe/blob/master/Objective-C/Runtime/%E6%B5%85%E8%B0%88%20block%EF%BC%882%EF%BC%89%20-%20%E6%88%AA%E8%8E%B7%E5%8F%98%E9%87%8F%E6%96%B9%E5%BC%8F.md) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://halfrost.com/ios_block/) — 第三方博客（未归档（halfrost.com））
- [计划材料](https://luohs.github.io/2017/05/31/20170531/) — 第三方博客（未归档（luohs.github.io））
- [计划材料](https://github.com/draveness/analyze/blob/master/contents/FBRetainCycleDetector/iOS%20%E4%B8%AD%E7%9A%84%20block%20%E6%98%AF%E5%A6%82%E4%BD%95%E6%8C%81%E6%9C%89%E5%AF%B9%E8%B1%A1%E7%9A%84.md) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://lvv.me/posts/2022/08/13_weak_strong_dance/) — 第三方博客（未归档（lvv.me））
- [计划材料](https://dhoerl.wordpress.com/2013/04/23/i-finally-figured-out-weakself-and-strongself/) — 第三方博客（未归档（dhoerl.wordpress.com））
- [计划材料](https://bytes.vokal.io/objc-block-capture-weakself/) — 第三方博客（未归档（bytes.vokal.io））
- [计划材料](https://medium.com/fantageek/understanding-weak-and-strong-in-objective-c-d17ba4c2c297) — 第三方博客（未归档（medium.com））

## 中文资料

共 78 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [Big Nerd Ranch Advanced Mac OS X 编程：Block](../../blogs/snapshots-zh/informit.com/big-nerd-ranch-advanced-mac-os-x-programming-blocks.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/informit.com/big-nerd-ranch-advanced-mac-os-x-programming-blocks.md) | 已翻译 |
| 计划核心 | [Block的三种类型:__NSGlobalBlock,__NSStackBlock,__NSMallocBlock](../../blogs/snapshots/jianshu.com/block%E7%9A%84%E4%B8%89%E7%A7%8D%E7%B1%BB%E5%9E%8B-nsglobalblock-nsstackblock-nsmallocblock.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/jianshu.com/block%E7%9A%84%E4%B8%89%E7%A7%8D%E7%B1%BB%E5%9E%8B-nsglobalblock-nsstackblock-nsmallocblock.md) | 原生中文 |
| 计划核心 | [iOS block底层原理分析(1)--循环引用](../../blogs/snapshots/jianshu.com/ios-block%E5%BA%95%E5%B1%82%E5%8E%9F%E7%90%86%E5%88%86%E6%9E%90-1-%E5%BE%AA%E7%8E%AF%E5%BC%95%E7%94%A8.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/jianshu.com/ios-block%E5%BA%95%E5%B1%82%E5%8E%9F%E7%90%86%E5%88%86%E6%9E%90-1-%E5%BE%AA%E7%8E%AF%E5%BC%95%E7%94%A8.md) | 原生中文 |
| 计划核心 | [iOS内存管理（四）-strong&copy&weak底层分析](../../blogs/snapshots/cloud.tencent.com/ios%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86-%E5%9B%9B-strong-copy-weak%E5%BA%95%E5%B1%82%E5%88%86%E6%9E%90.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cloud.tencent.com/ios%E5%86%85%E5%AD%98%E7%AE%A1%E7%90%86-%E5%9B%9B-strong-copy-weak%E5%BA%95%E5%B1%82%E5%88%86%E6%9E%90.md) | 原生中文 |
| 计划核心 | [Objective-C runtime机制(7)——SideTables, SideTable, weak_table, weak_entry_t](../../blogs/snapshots/blog.csdn.net/objective-c-runtime%E6%9C%BA%E5%88%B6-7-sidetables-sidetable-weak-table-weak-entry-t.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/objective-c-runtime%E6%9C%BA%E5%88%B6-7-sidetables-sidetable-weak-table-weak-entry-t.md) | 原生中文 |
| 计划核心 | [weak-strong dance 的注意事项](../../blogs/snapshots/lvv.me/weak-strong-dance-%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/lvv.me/weak-strong-dance-%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9.md) | 原生中文 |
| 计划核心 | [令人惊讶的弱引用实现：Swift、Obj-C、C++、Rust 和 Vale](../../blogs/snapshots-zh/verdagon.dev/surprising-weak-ref-implementations-swift-obj-c-c-rust-and-vale.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/verdagon.dev/surprising-weak-ref-implementations-swift-obj-c-c-rust-and-vale.md) | 已翻译 |
| 计划核心 | [我终于搞明白了 weakSelf 和 strongSelf](../../blogs/snapshots-zh/dhoerl.wordpress.com/i-finally-figured-out-weakself-and-strongself.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/dhoerl.wordpress.com/i-finally-figured-out-weakself-and-strongself.md) | 已翻译 |
| 计划核心 | [深入理解"weak-strong dance"](../../blogs/snapshots/luohs.github.io/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3-weak-strong-dance.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/luohs.github.io/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3-weak-strong-dance.md) | 原生中文 |
| 计划核心 | [深入研究 Block 捕获外部变量和 __block 实现原理](../../blogs/snapshots/halfrost.com/%E6%B7%B1%E5%85%A5%E7%A0%94%E7%A9%B6-block-%E6%8D%95%E8%8E%B7%E5%A4%96%E9%83%A8%E5%8F%98%E9%87%8F%E5%92%8C-block-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/halfrost.com/%E6%B7%B1%E5%85%A5%E7%A0%94%E7%A9%B6-block-%E6%8D%95%E8%8E%B7%E5%A4%96%E9%83%A8%E5%8F%98%E9%87%8F%E5%92%8C-block-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 官方资料 | [Safari 发行说明](../../apple-docs/zh/safari-release-notes.md) | Apple 文档 | Apple · updates | [中文](../../apple-docs/zh/safari-release-notes.md) | 已翻译 |
| 官方资料 | [为 beta 测试和发布分发你的 App](../../apple-docs/zh/xcode/distributing-your-app-for-beta-testing-and-releases.md) | Apple 文档 | Apple · updates | [中文](../../apple-docs/zh/xcode/distributing-your-app-for-beta-testing-and-releases.md) | 已翻译 |
| 官方资料 | [在 App 的 Beta 版本中包含供测试人员参考的说明](../../apple-docs/zh/xcode/including-notes-for-testers-with-a-beta-release-of-your-app.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/including-notes-for-testers-with-a-beta-release-of-your-app.md) | 已翻译 |
| 官方资料 | [测试发布版本](../../apple-docs/zh/xcode/testing-a-release-build.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/testing-a-release-build.md) | 已翻译 |
| 官方资料 | [Swift 中的 ARC：基础与进阶](../../wwdc/zh/wwdc2021/10216-arc-in-swift-basics-and-beyond.md) | WWDC | Apple · WWDC2021 | [中文](../../wwdc/zh/wwdc2021/10216-arc-in-swift-basics-and-beyond.md) | 已翻译 |
| 深度补充 | [Assign、retain、copy：Obj-C 属性访问器的陷阱](../../blogs/zh/cocoawithlove/assign-retain-copy-pitfalls-in-obj-c-property-accessors-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/assign-retain-copy-pitfalls-in-obj-c-property-accessors-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Autorelease 很快](../../blogs/zh/mikeash/autorelease-is-fast.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/autorelease-is-fast.md) | 已翻译 |
| 深度补充 | [block 代理](../../blogs/zh/mikeash/block-proxying.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/block-proxying.md) | 已翻译 |
| 深度补充 | [block 的实现方式（及其后果） \| Cocoa with Love](../../blogs/zh/cocoawithlove/how-blocks-are-implemented-and-the-consequences-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/how-blocks-are-implemented-and-the-consequences-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [blocks](../../blogs/zh/mikeash/blocks.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/blocks.md) | 已翻译 |
| 深度补充 | [Blocks 的丑陋面：显式声明和类型转换 \| Cocoa with Love](../../blogs/zh/cocoawithlove/the-ugly-side-of-blocks-explicit-declarations-and-casting-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/the-ugly-side-of-blocks-explicit-declarations-and-casting-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [GCD 不是 Block，Block 不是 GCD](../../blogs/zh/mikeash/gcd-is-not-blocks-blocks-are-not-gcd.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/gcd-is-not-blocks-blocks-are-not-gcd.md) | 已翻译 |
| 深度补充 | [NSMapTable：不仅仅是用于弱指针的 NSDictionary \| Cocoa with Love](../../blogs/zh/cocoawithlove/nsmaptable-more-than-an-nsdictionary-for-weak-pointers-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/nsmaptable-more-than-an-nsdictionary-for-weak-pointers-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [objc 中的 block](../../blogs/zh/ibireme/objc-%E4%B8%AD%E7%9A%84-block.md) | 技术博客 | ibireme (郭曜源) | [中文](../../blogs/zh/ibireme/objc-%E4%B8%AD%E7%9A%84-block.md) | 原生中文 |
| 深度补充 | [Objective-C 内部实现：release](../../blogs/zh/alwaysprocessing/objective-c-internals-release-although-release-is-just-the-logical-inverse-of-retain-its-i.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/objective-c-internals-release-although-release-is-just-the-logical-inverse-of-retain-its-i.md) | 已翻译 |
| 深度补充 | [Objective-C 内部实现：Retain](../../blogs/zh/alwaysprocessing/objective-c-internals-retain-objective-c-memory-is-managed-through-a-reference-counting-sc.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/objective-c-internals-retain-objective-c-memory-is-managed-through-a-reference-counting-sc.md) | 已翻译 |
| 深度补充 | [Objective-C 弱类型的一个重大缺陷](../../blogs/zh/cocoawithlove/a-big-weakness-in-objective-c-s-weak-typing-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/a-big-weakness-in-objective-c-s-weak-typing-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [StreamToMe iPhone 应用已发布](../../blogs/zh/cocoawithlove/streamtome-iphone-app-released-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/streamtome-iphone-app-released-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Swift 中的引用计数释放](../../blogs/zh/cocoawithlove/reference-counted-releases-in-swift-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/reference-counted-releases-in-swift-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [XCTestCase /XCTestExpectation / measureBlock()](../../blogs/zh/nshipster/xctestcase-br-xctestexpectation-br-measureblock.md) | 技术博客 | NSHipster (Mattt) | [中文](../../blogs/zh/nshipster/xctestcase-br-xctestexpectation-br-measureblock.md) | 已翻译 |
| 深度补充 | [俄语中的 Blocks 和 GCD](../../blogs/zh/mikeash/blocks-and-gcd-in-russian.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/blocks-and-gcd-in-russian.md) | 已翻译 |
| 深度补充 | [内存和线程安全的自定义属性方法 \| Cocoa with Love](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/memory-and-thread-safe-custom-property-methods-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [将 block 转换为函数指针](../../blogs/zh/mikeash/converting-blocks-into-function-pointers.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/converting-blocks-into-function-pointers.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-08-14：实用 Blocks](../../blogs/zh/mikeash/friday-q-a-2009-08-14-practical-blocks.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-08-14-practical-blocks.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-10-16：创建基于 Blocks 的对象系统](../../blogs/zh/mikeash/friday-q-a-2009-10-16-creating-a-blocks-based-object-system.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-10-16-creating-a-blocks-based-object-system.md) | 已翻译 |
| 深度补充 | [星期五问答 2010-04-30：处理保留循环](../../blogs/zh/mikeash/friday-q-a-2010-04-30-dealing-with-retain-cycles.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2010-04-30-dealing-with-retain-cycles.md) | 已翻译 |
| 深度补充 | [星期五问答 2010-07-30：CoreFoundation 对象的置零弱引用](../../blogs/zh/mikeash/friday-q-a-2010-07-30-zeroing-weak-references-to-corefoundation-objects.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2010-07-30-zeroing-weak-references-to-corefoundation-objects.md) | 已翻译 |
| 深度补充 | [星期五问答 2011-06-03：Objective-C Blocks 对比 C++0x Lambdas：开战！](../../blogs/zh/mikeash/friday-q-a-2011-06-03-objective-c-blocks-vs-c-0x-lambdas-fight.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2011-06-03-objective-c-blocks-vs-c-0x-lambdas-fight.md) | 已翻译 |
| 深度补充 | [星期五问答 2011-09-02：让我们构建 NSAutoreleasePool](../../blogs/zh/mikeash/friday-q-a-2011-09-02-let-s-build-nsautoreleasepool.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2011-09-02-let-s-build-nsautoreleasepool.md) | 已翻译 |
| 深度补充 | [星期五问答 2011-09-16：让我们构建引用计数](../../blogs/zh/mikeash/friday-q-a-2011-09-16-let-s-build-reference-counting.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2011-09-16-let-s-build-reference-counting.md) | 已翻译 |
| 深度补充 | [星期五问答 2011-09-30：自动引用计数](../../blogs/zh/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md) | 已翻译 |
| 深度补充 | [星期五问答 2011-11-11：构建记忆化 Block 代理](../../blogs/zh/mikeash/friday-q-a-2011-11-11-building-a-memoizing-block-proxy.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2011-11-11-building-a-memoizing-block-proxy.md) | 已翻译 |
| 深度补充 | [星期五问答 2014-05-09：当自动释放不是自动释放时](../../blogs/zh/mikeash/friday-q-a-2014-05-09-when-an-autorelease-isn-t.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2014-05-09-when-an-autorelease-isn-t.md) | 已翻译 |
| 深度补充 | [星期五问答 2015-12-11：Swift 弱引用](../../blogs/zh/mikeash/friday-q-a-2015-12-11-swift-weak-references.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2015-12-11-swift-weak-references.md) | 已翻译 |
| 深度补充 | [星期五问答 2017-09-22：Swift 4 弱引用](../../blogs/zh/mikeash/friday-q-a-2017-09-22-swift-4-weak-references.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2017-09-22-swift-4-weak-references.md) | 已翻译 |
| 深度补充 | [更多关于 Autorelease 的乐趣](../../blogs/zh/mikeash/more-fun-with-autorelease.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/more-fun-with-autorelease.md) | 已翻译 |
| 深度补充 | [用引用计数的结构体打破 Swift](../../blogs/zh/cocoawithlove/breaking-swift-with-reference-counted-structs-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/breaking-swift-with-reference-counted-structs-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [避免保留循环的规则](../../blogs/zh/cocoawithlove/rules-to-avoid-retain-cycles-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/rules-to-avoid-retain-cycles-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [所有权宣言 - Swift 官方文章 Ownership Manifesto 译文评注版](../../blogs/zh/onevcat/%E6%89%80%E6%9C%89%E6%9D%83%E5%AE%A3%E8%A8%80-swift-%E5%AE%98%E6%96%B9%E6%96%87%E7%AB%A0-ownership-manifesto-%E8%AF%91%E6%96%87%E8%AF%84%E6%B3%A8%E7%89%88.md) | 技术博客 | onevcat (王巍/喵神) | [中文](../../blogs/zh/onevcat/%E6%89%80%E6%9C%89%E6%9D%83%E5%AE%A3%E8%A8%80-swift-%E5%AE%98%E6%96%B9%E6%96%87%E7%AB%A0-ownership-manifesto-%E8%AF%91%E6%96%87%E8%AF%84%E6%B3%A8%E7%89%88.md) | 原生中文 |
| 补充资料 | [[objc 解析]: 异常与自动释放池](../../blogs/zh/sealiesoftware/objc-explain-exceptions-and-autorelease-pools.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-exceptions-and-autorelease-pools.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 弱导入类](../../blogs/zh/sealiesoftware/objc-explain-weak-import-classes.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-weak-import-classes.md) | 已翻译 |
| 补充资料 | [Apple 已（部分）解除 Beta 版本的 NDA](../../blogs/zh/oleb/apple-has-partly-lifted-the-nda-for-beta-releases.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/apple-has-partly-lifted-the-nda-for-beta-releases.md) | 已翻译 |
| 补充资料 | [BlockHook and Memory Safety](../../blogs/zh/yulingtianxia/blockhook-and-memory-safety.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/blockhook-and-memory-safety.md) | 原生中文 |
| 补充资料 | [ccls 0.20181225 发布](../../blogs/zh/maskray/ccls-0-20181225-release.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/ccls-0-20181225-release.md) | 已翻译 |
| 补充资料 | [GitHub 技巧：关注版本发布](../../blogs/zh/jessesquires/github-tip-watching-releases.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/github-tip-watching-releases.md) | 已翻译 |
| 补充资料 | [Hook Objective-C Block with Libffi](../../blogs/zh/yulingtianxia/hook-objective-c-block-with-libffi.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/hook-objective-c-block-with-libffi.md) | 原生中文 |
| 补充资料 | [Nimble 10.0 发布](../../blogs/zh/jessesquires/nimble-10-0-released.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/nimble-10-0-released.md) | 已翻译 |
| 补充资料 | [Objective-C Autorelease Pool 的实现原理](../../blogs/zh/leichunfeng/objective-c-autorelease-pool-%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 技术博客 | 雷纯锋 | [中文](../../blogs/zh/leichunfeng/objective-c-autorelease-pool-%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 补充资料 | [Quick 5.0 发布](../../blogs/zh/jessesquires/quick-5-0-released.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/quick-5-0-released.md) | 已翻译 |
| 补充资料 | [Swift 发布版本有主题](../../blogs/zh/oleb/swift-releases-have-themes.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/swift-releases-have-themes.md) | 已翻译 |
| 补充资料 | [你必须手动注销基于 block 的 NotificationCenter 观察者吗？](../../blogs/zh/oleb/do-you-have-to-manually-unregister-block-based-notificationcenter-observers.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/do-you-have-to-manually-unregister-block-based-notificationcenter-observers.md) | 已翻译 |
| 补充资料 | [使用 GitHub Actions 自动化合并发布分支到主分支](../../blogs/zh/jessesquires/automate-merging-release-branches-into-your-main-branch-with-github-actions.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/automate-merging-release-branches-into-your-main-branch-with-github-actions.md) | 已翻译 |
| 补充资料 | [在 Flutter 中玩转 Objective-C Block](../../blogs/zh/yulingtianxia/%E5%9C%A8-flutter-%E4%B8%AD%E7%8E%A9%E8%BD%AC-objective-c-block.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/%E5%9C%A8-flutter-%E4%B8%AD%E7%8E%A9%E8%BD%AC-objective-c-block.md) | 原生中文 |
| 补充资料 | [在 Release 和 Beta 版 Xcode 之间切换](../../blogs/zh/jessesquires/quickly-switching-between-xcodes.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/quickly-switching-between-xcodes.md) | 已翻译 |
| 补充资料 | [在 Swift 中，用于初始化存储属性的自执行匿名闭包里的 self 是什么类型？](../../blogs/zh/jessesquires/what-type-is-self-in-a-swift-self-executing-anonymous-closure-used-to-initialize-a-stored-.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/what-type-is-self-in-a-swift-self-executing-anonymous-closure-used-to-initialize-a-stored-.md) | 已翻译 |
| 补充资料 | [在不将图像加载到内存的情况下访问图像属性](../../blogs/zh/oleb/accessing-image-properties-without-loading-the-image-into-memory.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/accessing-image-properties-without-loading-the-image-into-memory.md) | 已翻译 |
| 补充资料 | [在（Objective-）C 中构建基于 block 的对象系统](../../blogs/zh/oleb/building-a-blocks-based-object-system-in-objective-c.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/building-a-blocks-based-object-system-in-objective-c.md) | 已翻译 |
| 补充资料 | [将 App Store 上的 App 设置为特定发布日期时，它会在什么时间发布？](../../blogs/zh/oleb/at-what-time-is-an-app-released-on-the-app-store-when-set-to-a-specific-release-date.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/at-what-time-is-an-app-released-on-the-app-store-when-set-to-a-specific-release-date.md) | 已翻译 |
| 补充资料 | [弱符号](../../blogs/zh/maskray/weak-symbol.md) | 技术博客 | MaskRay (宋方睿) | [中文](../../blogs/zh/maskray/weak-symbol.md) | 已翻译 |
| 补充资料 | [弱链接](../../blogs/zh/belkadan/weak-linking.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/weak-linking.md) | 已翻译 |
| 补充资料 | [比较发布分支策略](../../blogs/zh/jessesquires/comparing-release-branch-strategies.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/comparing-release-branch-strategies.md) | 已翻译 |
| 补充资料 | [自制 Objective-C 弱导入](../../blogs/zh/sealiesoftware/do-it-yourself-objective-c-weak-import.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/do-it-yourself-objective-c-weak-import.md) | 已翻译 |
| 补充资料 | [自动引用计数](../../blogs/zh/belkadan/automatic-reference-counting.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/automatic-reference-counting.md) | 已翻译 |
| 补充资料 | [追踪 Objective-C Block 代码定义的位置](../../blogs/zh/yulingtianxia/%E8%BF%BD%E8%B8%AA-objective-c-block-%E4%BB%A3%E7%A0%81%E5%AE%9A%E4%B9%89%E7%9A%84%E4%BD%8D%E7%BD%AE.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/%E8%BF%BD%E8%B8%AA-objective-c-block-%E4%BB%A3%E7%A0%81%E5%AE%9A%E4%B9%89%E7%9A%84%E4%BD%8D%E7%BD%AE.md) | 原生中文 |
| 补充资料 | [追踪 Objective-C 方法中的 Block 参数对象](../../blogs/zh/yulingtianxia/%E8%BF%BD%E8%B8%AA-objective-c-%E6%96%B9%E6%B3%95%E4%B8%AD%E7%9A%84-block-%E5%8F%82%E6%95%B0%E5%AF%B9%E8%B1%A1.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/%E8%BF%BD%E8%B8%AA-objective-c-%E6%96%B9%E6%B3%95%E4%B8%AD%E7%9A%84-block-%E5%8F%82%E6%95%B0%E5%AF%B9%E8%B1%A1.md) | 原生中文 |
| 补充资料 | [黑幕背后的Autorelease](../../blogs/zh/sunnyxx/%E9%BB%91%E5%B9%95%E8%83%8C%E5%90%8E%E7%9A%84autorelease-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 技术博客 | sunnyxx (孙源) | [中文](../../blogs/zh/sunnyxx/%E9%BB%91%E5%B9%95%E8%83%8C%E5%90%8E%E7%9A%84autorelease-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 原生中文 |
| 补充资料 | [Autorelease 实现原理探析](../../blogs/snapshots-zh/matteogobbi.github.io/autorelease-under-the-hood.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/matteogobbi.github.io/autorelease-under-the-hood.md) | 已翻译 |
| 补充资料 | [Objective-C之Autorelease Pool底层实现原理记录（双向链表）以及在Runloop中是如何参与进去的](../../blogs/snapshots/blog.csdn.net/objective-c%E4%B9%8Bautorelease-pool%E5%BA%95%E5%B1%82%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E8%AE%B0%E5%BD%95-%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8-%E4%BB%A5%E5%8F%8A%E5%9C%A8runloop%E4%B8%AD%E6%98%AF%E5%A6%82%E4%BD%95%E5%8F%82%E4%B8%8E%E8%BF%9B%E5%8E%BB%E7%9A%84.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/objective-c%E4%B9%8Bautorelease-pool%E5%BA%95%E5%B1%82%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E8%AE%B0%E5%BD%95-%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8-%E4%BB%A5%E5%8F%8A%E5%9C%A8runloop%E4%B8%AD%E6%98%AF%E5%A6%82%E4%BD%95%E5%8F%82%E4%B8%8E%E8%BF%9B%E5%8E%BB%E7%9A%84.md) | 原生中文 |

## 未翻译资料

共 18 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [值对象](../../blogs/en/objcio/value-objects.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/value-objects.md) | 仅标题中文，正文待翻译 |
| 官方资料 | [App Store Connect API Release Notes](../../apple-docs/en/appstoreconnectapi/app-store-connect-api-release-notes.md) | Apple 文档 | Apple · App Store Connect API | [英文](../../apple-docs/en/appstoreconnectapi/app-store-connect-api-release-notes.md) | 待翻译 |
| 官方资料 | [Implementing order-independent transparency with image blocks](../../apple-docs/en/metal/implementing-order-independent-transparency-with-image-blocks.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/implementing-order-independent-transparency-with-image-blocks.md) | 待翻译 |
| 官方资料 | [iOS & iPadOS Release Notes](../../apple-docs/en/ios-ipados-release-notes.md) | Apple 文档 | Apple · updates | [英文](../../apple-docs/en/ios-ipados-release-notes.md) | 待翻译 |
| 官方资料 | [macOS Release Notes](../../apple-docs/en/macos-release-notes.md) | Apple 文档 | Apple · updates | [英文](../../apple-docs/en/macos-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 1 release notes](../../apple-docs/en/storekit/skadnetwork-1-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-1-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 2 release notes](../../apple-docs/en/storekit/skadnetwork-2-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-2-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 2.1 release notes](../../apple-docs/en/storekit/skadnetwork-2-1-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-2-1-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 2.2 release notes](../../apple-docs/en/storekit/skadnetwork-2-2-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-2-2-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 3 release notes](../../apple-docs/en/storekit/skadnetwork-3-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-3-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork 4 release notes](../../apple-docs/en/storekit/skadnetwork-4-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-4-release-notes.md) | 待翻译 |
| 官方资料 | [SKAdNetwork release notes](../../apple-docs/en/storekit/skadnetwork-release-notes.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/skadnetwork-release-notes.md) | 待翻译 |
| 官方资料 | [tvOS Release Notes](../../apple-docs/en/tvos-release-notes.md) | Apple 文档 | Apple · updates | [英文](../../apple-docs/en/tvos-release-notes.md) | 待翻译 |
| 官方资料 | [visionOS Release Notes](../../apple-docs/en/visionos-release-notes.md) | Apple 文档 | Apple · updates | [英文](../../apple-docs/en/visionos-release-notes.md) | 待翻译 |
| 官方资料 | [watchOS Release Notes](../../apple-docs/en/watchos-release-notes.md) | Apple 文档 | Apple · updates | [英文](../../apple-docs/en/watchos-release-notes.md) | 待翻译 |
| 官方资料 | [Xcode Release Notes](../../apple-docs/en/xcode-release-notes.md) | Apple 文档 | Apple · updates | [英文](../../apple-docs/en/xcode-release-notes.md) | 待翻译 |
| 补充资料 | [不屏蔽广告是不道德的吗？](../../blogs/en/oleb/is-it-immoral-to-not-block-ads.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/is-it-immoral-to-not-block-ads.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [弱 AVL 树](../../blogs/en/maskray/weak-avl-tree.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/weak-avl-tree.md) | 仅标题中文，正文待翻译 |
