# 模块 3：Runtime：消息发送、转发、Category、KVO

> 沿方法查找、转发、Category、关联对象和 KVC/KVO 建立运行时行为地图。
> 对应仓库范围：Objective-C Runtime、架构、测试与工程实践。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 3.1 | `objc_msgSend`、方法缓存、慢速查找、super 查找 | 方法查找流程图；缓存命中/未命中路径说明 |
| 3.2 | 动态方法解析、备用接收者、完整转发；“三次机会”的关系 | 消息发送与转发总流程图；解释动态方法决议为什么可能发生两次 |
| 3.3 | Method Swizzling：实现、正确姿势、继承风险、调用原实现 | 一个只交换当前类实现的实验；列出不该使用 swizzling 的场景 |
| 3.4 | Category 编译产物、加载、方法覆盖；Extension；关联对象与关联策略 | `category_t`、attach、关联对象哈希 map 结构图 |
| 3.5 | `+load` 与 `+initialize`：触发时机、顺序、并发、分类行为 | 父类/子类/两个分类实验输出，不背固定顺序 |
| 3.6 | KVC 查找规则、集合运算；KVO 自动通知、动态子类、isa-swizzling | KVC 搜索流程；KVO 前后真实 class 打印 |
| 3.7 | 通知、单例、代理、target-action、block 回调、常见设计模式 | “一对一/一对多/可回传/可拦截/耦合度”通信方式对比表 |

## 计划指定材料

- [消息传递](../../legacy-archive/zh/documentation/Cocoa/Objective-C%20Runtime%20Programming%20Guide/Messaging.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Objective-C%20Runtime%20Programming%20Guide/Messaging.md) — Apple 旧归档
- [计划材料](https://developer.apple.com/documentation/objectivec/objective-c_runtime) — Apple 现行文档（未归档）
- [Friday Q&A 2009-03-13：Objective-C 运行时简介](../../blogs/zh/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md) — 本仓库资料
- [Friday Q&A 2017-06-30：深入剖析 ARM64 上的 objc_msgSend](../../blogs/zh/mikeash/friday-q-a-2017-06-30-dissecting-objc-msgsend-on-arm64.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2017-06-30-dissecting-objc-msgsend-on-arm64.md) — 本仓库资料
- [Friday Q&A 2009-03-27：Objective-C 消息转发](../../blogs/zh/mikeash/friday-q-a-2009-03-27-objective-c-message-forwarding.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2009-03-27-objective-c-message-forwarding.md) — 本仓库资料
- [方法调配](../../blogs/zh/nshipster/method-swizzling.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/nshipster/method-swizzling.md) — 本仓库资料
- [分类与扩展](../../legacy-archive/zh/documentation/Cocoa/The%20Objective-C%20Programming%20Language/Categories%20and%20Extensions.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/The%20Objective-C%20Programming%20Language/Categories%20and%20Extensions.md) — Apple 旧归档
- [Objective-C 内部实现：关联引用](../../blogs/zh/alwaysprocessing/objective-c-internals-associated-references-a-comparison-of-apple-s-associated-references-.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/alwaysprocessing/objective-c-internals-associated-references-a-comparison-of-apple-s-associated-references-.md) — 本仓库资料
- [键值编码编程指南](../../legacy-archive/zh/documentation/Cocoa/Key-Value%20Coding%20Programming%20Guide/index.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Key-Value%20Coding%20Programming%20Guide/index.md) — Apple 旧归档
- [键值观察编程指南简介](../../legacy-archive/zh/documentation/Cocoa/Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md) — Apple 旧归档
- [键值观察实现细节](../../legacy-archive/zh/documentation/Cocoa/Key-Value%20Observing%20Programming%20Guide/Key-Value%20Observing%20Implementation%20Details.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Key-Value%20Observing%20Programming%20Guide/Key-Value%20Observing%20Implementation%20Details.md) — Apple 旧归档
- [Cocoa 设计模式](../../legacy-archive/vault/documentation/Cocoa/Cocoa%20Fundamentals%20Guide/Cocoa%20Design%20Patterns.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/Cocoa/Cocoa%20Fundamentals%20Guide/Cocoa%20Design%20Patterns.md) — Apple 旧归档
- [通知中心](../../apple-docs/zh/foundation/notificationcenter.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/notificationcenter.md) — 本仓库资料
- [Delegates and Data Sources](../../legacy-archive/vault/documentation/General/Concepts%20in%20Objective-C%20Programming/Delegates%20and%20Data%20Sources.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/General/Concepts%20in%20Objective-C%20Programming/Delegates%20and%20Data%20Sources.md) — Apple 旧归档
- [计划材料](https://ridiculousfish.com/blog/posts/objc_msgsend.html) — 第三方博客（未归档（ridiculousfish.com））
- [计划材料](https://zhongwuzw.github.io/2018/04/21/iOS%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgSend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84/) — 第三方博客（未归档（zhongwuzw.github.io））
- [计划材料](https://kingcos.me/posts/2019/objc_msgsend/) — 第三方博客（未归档（kingcos.me））
- [计划材料](https://www.cnblogs.com/developer-ios/p/4948803.html) — 第三方博客（未归档（cnblogs.com））
- [计划材料](https://draveness.me/ao.html) — 第三方博客（未归档（draveness.me））
- [关联对象](../../blogs/zh/nshipster/associated-objects.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/nshipster/associated-objects.md) — 本仓库资料
- [计划材料](https://www.cnblogs.com/huanying2000/p/13938350.html) — 第三方博客（未归档（cnblogs.com））
- [计划材料](https://www.cnblogs.com/junhuawang/p/14304756.html) — 第三方博客（未归档（cnblogs.com））
- [键值观察](../../blogs/zh/nshipster/key-value-observing.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/nshipster/key-value-observing.md) — 本仓库资料
- [计划材料](https://www.neroxie.com/2019/07/12/KVC%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/) — 第三方博客（未归档（neroxie.com））
- [计划材料](https://zhuanlan.zhihu.com/p/587704697) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [计划材料](https://blog.csdn.net/zhoupengju/article/details/53129436) — 第三方博客（未归档（blog.csdn.net））
- [计划材料](https://huberyyang.com/2018/04/13/KVO%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/) — 第三方博客（未归档（huberyyang.com））
- [Friday Q&A 2012-03-02: 正确实现键值观察：第二轮](../../blogs/zh/mikeash/friday-q-a-2012-03-02-key-value-observing-done-right-take-2.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/mikeash/friday-q-a-2012-03-02-key-value-observing-done-right-take-2.md) — 本仓库资料
- [Communication Patterns](../../blogs/en/objcio/communication-patterns.md) · [原文网页](https://www.objc.io/issues/7-foundation/communication-patterns/) — 第三方博客
- [计划材料](https://blog.csdn.net/weixin_38633659/article/details/149066468) — 第三方博客（未归档（blog.csdn.net））
- [计划材料](https://www.cnblogs.com/iOS-Blog/archive/2013/02/21/2920926.html) — 第三方博客（未归档（cnblogs.com））
- [计划材料](https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/) — 第三方博客（未归档（coderjtao.github.io））
- [计划材料](https://www.cnblogs.com/wujy/p/5825690.html) — 第三方博客（未归档（cnblogs.com））
- [Foundation: NSNotificationCenter](../../blogs/zh/southpeak/foundation-nsnotificationcenter.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/southpeak/foundation-nsnotificationcenter.md) — 本仓库资料

## 中文资料

共 84 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [6种iOS开发中常用的设计模式](../../blogs/snapshots/blog.csdn.net/6%E7%A7%8Dios%E5%BC%80%E5%8F%91%E4%B8%AD%E5%B8%B8%E7%94%A8%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/6%E7%A7%8Dios%E5%BC%80%E5%8F%91%E4%B8%AD%E5%B8%B8%E7%94%A8%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.md) | 原生中文 |
| 计划核心 | [define SUPPORT_INDEXED_ISA 1](../../blogs/snapshots/kingcos.me/%E6%B5%85%E5%B0%9D-objc-msgsend.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/kingcos.me/%E6%B5%85%E5%B0%9D-objc-msgsend.md) | 原生中文 |
| 计划核心 | [iOS Category原理探寻](../../blogs/snapshots/cnblogs.com/ios-category%E5%8E%9F%E7%90%86%E6%8E%A2%E5%AF%BB.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/ios-category%E5%8E%9F%E7%90%86%E6%8E%A2%E5%AF%BB.md) | 原生中文 |
| 计划核心 | [ios method swizzling](../../blogs/snapshots/cnblogs.com/ios-method-swizzling.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/ios-method-swizzling.md) | 原生中文 |
| 计划核心 | [iOS-+load和+initialize方法调用时机](../../blogs/snapshots/cnblogs.com/ios-load%E5%92%8C-initialize%E6%96%B9%E6%B3%95%E8%B0%83%E7%94%A8%E6%97%B6%E6%9C%BA.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/ios-load%E5%92%8C-initialize%E6%96%B9%E6%B3%95%E8%B0%83%E7%94%A8%E6%97%B6%E6%9C%BA.md) | 原生中文 |
| 计划核心 | [iOS开发那些事-iOS常用设计模式–委托模式](../../blogs/snapshots/cnblogs.com/ios%E5%BC%80%E5%8F%91%E9%82%A3%E4%BA%9B%E4%BA%8B-ios%E5%B8%B8%E7%94%A8%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F-%E5%A7%94%E6%89%98%E6%A8%A1%E5%BC%8F.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/ios%E5%BC%80%E5%8F%91%E9%82%A3%E4%BA%9B%E4%BA%8B-ios%E5%B8%B8%E7%94%A8%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F-%E5%A7%94%E6%89%98%E6%A8%A1%E5%BC%8F.md) | 原生中文 |
| 计划核心 | [iOS知识小集之为什么objc_msgSend()是用汇编实现的](../../blogs/snapshots/zhongwuzw.github.io/ios%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgsend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/zhongwuzw.github.io/ios%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgsend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84.md) | 原生中文 |
| 计划核心 | [KVC实现原理](../../blogs/snapshots/neroxie.com/kvc%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/neroxie.com/kvc%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 计划核心 | [KVO实现原理](../../blogs/snapshots/huberyyang.com/kvo%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/huberyyang.com/kvo%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 计划核心 | [KVO的实现原理](../../blogs/snapshots/blog.csdn.net/kvo%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/kvo%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 计划核心 | [objc_msgSend](../../blogs/snapshots-zh/ridiculousfish.com/objc-msgsend.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/ridiculousfish.com/objc-msgsend.md) | 已翻译 |
| 计划核心 | [你真的了解NSNotificationCenter吗？](../../blogs/snapshots/cnblogs.com/%E4%BD%A0%E7%9C%9F%E7%9A%84%E4%BA%86%E8%A7%A3nsnotificationcenter%E5%90%97.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/%E4%BD%A0%E7%9C%9F%E7%9A%84%E4%BA%86%E8%A7%A3nsnotificationcenter%E5%90%97.md) | 原生中文 |
| 计划核心 | [关联对象 AssociatedObject 完全解析 - 面向信仰编程](../../blogs/snapshots/draveness.me/%E5%85%B3%E8%81%94%E5%AF%B9%E8%B1%A1-associatedobject-%E5%AE%8C%E5%85%A8%E8%A7%A3%E6%9E%90-%E9%9D%A2%E5%90%91%E4%BF%A1%E4%BB%B0%E7%BC%96%E7%A8%8B.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/draveness.me/%E5%85%B3%E8%81%94%E5%AF%B9%E8%B1%A1-associatedobject-%E5%AE%8C%E5%85%A8%E8%A7%A3%E6%9E%90-%E9%9D%A2%E5%90%91%E4%BF%A1%E4%BB%B0%E7%BC%96%E7%A8%8B.md) | 原生中文 |
| 计划核心 | [底层初窥——NSNotificationCenter](../../blogs/snapshots/coderjtao.github.io/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5-nsnotificationcenter.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/coderjtao.github.io/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5-nsnotificationcenter.md) | 原生中文 |
| 官方资料 | [Objective-C Runtime](../../apple-docs/zh/objectivec.md) | Apple 文档 | Apple · Objective-C Runtime | [中文](../../apple-docs/zh/objectivec.md) | 已翻译 |
| 官方资料 | [Objective-C 运行时](../../apple-docs/zh/objectivec/objective-c-runtime.md) | Apple 文档 | Apple · Objective-C Runtime | [中文](../../apple-docs/zh/objectivec/objective-c-runtime.md) | 已翻译 |
| 官方资料 | [Objective-C 运行时实用工具](../../apple-docs/zh/foundation/objective-c-runtime-utilities.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/objective-c-runtime-utilities.md) | 已翻译 |
| 官方资料 | [在 Swift 中使用 Objective-C 运行时特性](../../apple-docs/zh/swift/using-objective-c-runtime-features-in-swift.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/using-objective-c-runtime-features-in-swift.md) | 已翻译 |
| 官方资料 | [在 Swift 中使用键值观察](../../apple-docs/zh/swift/using-key-value-observing-in-swift.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/using-key-value-observing-in-swift.md) | 已翻译 |
| 官方资料 | [在运行时检查实时资源](../../apple-docs/zh/xcode/inspecting-live-resources-at-runtime.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/inspecting-live-resources-at-runtime.md) | 已翻译 |
| 官方资料 | [处理 Swift 运行时错误引发的崩溃](../../apple-docs/zh/xcode/addressing-crashes-from-swift-runtime-errors.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/addressing-crashes-from-swift-runtime-errors.md) | 已翻译 |
| 官方资料 | [外观属性选择器标记](../../apple-docs/zh/uikit/appearance-property-selector-tag.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/appearance-property-selector-tag.md) | 已翻译 |
| 官方资料 | [对象运行时](../../apple-docs/zh/foundation/object-runtime.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/object-runtime.md) | 已翻译 |
| 官方资料 | [延长你的 App 的后台运行时间](../../apple-docs/zh/uikit/extending-your-app-s-background-execution-time.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/extending-your-app-s-background-execution-time.md) | 已翻译 |
| 官方资料 | [强化运行时](../../apple-docs/zh/security/hardened-runtime.md) | Apple 文档 | Apple · Security | [中文](../../apple-docs/zh/security/hardened-runtime.md) | 已翻译 |
| 官方资料 | [配置强化运行时](../../apple-docs/zh/xcode/configuring-the-hardened-runtime.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/configuring-the-hardened-runtime.md) | 已翻译 |
| 官方资料 | [键值编码异常名称](../../apple-docs/zh/objectivec/key-value-coding-exception-names.md) | Apple 文档 | Apple · Objective-C Runtime | [中文](../../apple-docs/zh/objectivec/key-value-coding-exception-names.md) | 已翻译 |
| 官方资料 | [Objective-C 运行时的进展](../../wwdc/zh/wwdc2020/10163-advancements-in-the-objective-c-runtime.md) | WWDC | Apple · WWDC2020 | [中文](../../wwdc/zh/wwdc2020/10163-advancements-in-the-objective-c-runtime.md) | 已翻译 |
| 官方资料 | [改善 App 体积与运行时性能](../../wwdc/zh/wwdc2022/110363-improve-app-size-and-runtime-performance.md) | WWDC | Apple · WWDC2022 | [中文](../../wwdc/zh/wwdc2022/110363-improve-app-size-and-runtime-performance.md) | 已翻译 |
| 深度补充 | [Cocoa 中的 5 种键值编码方法](../../blogs/zh/cocoawithlove/5-key-value-coding-approaches-in-cocoa-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/5-key-value-coding-approaches-in-cocoa-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [objc_msgSend 的新原型](../../blogs/zh/mikeash/objc-msgsend-s-new-prototype.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/objc-msgsend-s-new-prototype.md) | 已翻译 |
| 深度补充 | [Objective-C 中的消息与消息转发](../../blogs/zh/ibireme/objective-c-%E4%B8%AD%E7%9A%84%E6%B6%88%E6%81%AF%E4%B8%8E%E6%B6%88%E6%81%AF%E8%BD%AC%E5%8F%91.md) | 技术博客 | ibireme (郭曜源) | [中文](../../blogs/zh/ibireme/objective-c-%E4%B8%AD%E7%9A%84%E6%B6%88%E6%81%AF%E4%B8%8E%E6%B6%88%E6%81%AF%E8%BD%AC%E5%8F%91.md) | 原生中文 |
| 深度补充 | [Objective-C 内部实现：关联引用](../../blogs/zh/alwaysprocessing/objective-c-internals-associated-references-a-comparison-of-apple-s-associated-references-.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/objective-c-internals-associated-references-a-comparison-of-apple-s-associated-references-.md) | 已翻译 |
| 深度补充 | [Swift 与 Objective-C 运行时](../../blogs/zh/nshipster/swift-the-objective-c-runtime.md) | 技术博客 | NSHipster (Mattt) | [中文](../../blogs/zh/nshipster/swift-the-objective-c-runtime.md) | 已翻译 |
| 深度补充 | [一个键值观察包装器](../../blogs/zh/cocoawithlove/a-key-value-observing-wrapper-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/a-key-value-observing-wrapper-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [关联对象](../../blogs/zh/nshipster/associated-objects.md) | 技术博客 | NSHipster (Mattt) | [中文](../../blogs/zh/nshipster/associated-objects.md) | 已翻译 |
| 深度补充 | [在 Mobile Orchard 的 Objective-C Runtime 播客节目](../../blogs/zh/mikeash/objective-c-runtime-podcast-episode-at-mobile-orchard.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/objective-c-runtime-podcast-episode-at-mobile-orchard.md) | 已翻译 |
| 深度补充 | [方法调配](../../blogs/zh/nshipster/method-swizzling.md) | 技术博客 | NSHipster (Mattt) | [中文](../../blogs/zh/nshipster/method-swizzling.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-03-13：Objective-C Runtime 入门](../../blogs/zh/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-03-20：Objective-C 消息发送](../../blogs/zh/mikeash/friday-q-a-2009-03-20-objective-c-messaging.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-03-20-objective-c-messaging.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-03-27：Objective-C 消息转发](../../blogs/zh/mikeash/friday-q-a-2009-03-27-objective-c-message-forwarding.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-03-27-objective-c-message-forwarding.md) | 已翻译 |
| 深度补充 | [星期五问答 2009-04-24：使用 LLVM 生成代码，第二部分：快速 Objective-C 转发](../../blogs/zh/mikeash/friday-q-a-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.md) | 已翻译 |
| 深度补充 | [星期五问答 2010-11-19：运行时创建类的乐趣与收益](../../blogs/zh/mikeash/friday-q-a-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.md) | 已翻译 |
| 深度补充 | [星期五问答 2012-03-02：正确实现键值观察：第二版](../../blogs/zh/mikeash/friday-q-a-2012-03-02-key-value-observing-done-right-take-2.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2012-03-02-key-value-observing-done-right-take-2.md) | 已翻译 |
| 深度补充 | [星期五问答 2012-11-16：让我们构建 objc_msgSend](../../blogs/zh/mikeash/friday-q-a-2012-11-16-let-s-build-objc-msgsend.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2012-11-16-let-s-build-objc-msgsend.md) | 已翻译 |
| 深度补充 | [星期五问答 2013-02-08：让我们构建键值编码](../../blogs/zh/mikeash/friday-q-a-2013-02-08-let-s-build-key-value-coding.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2013-02-08-let-s-build-key-value-coding.md) | 已翻译 |
| 深度补充 | [星期五问答 2015-05-29：Objective-C 运行时的并发内存释放](../../blogs/zh/mikeash/friday-q-a-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2015-05-29-concurrent-memory-deallocation-in-the-objective-c-runtime.md) | 已翻译 |
| 深度补充 | [星期五问答 2017-06-30：剖析 ARM64 上的 objc_msgSend](../../blogs/zh/mikeash/friday-q-a-2017-06-30-dissecting-objc-msgsend-on-arm64.md) | 技术博客 | mikeash.com Friday Q&A | [中文](../../blogs/zh/mikeash/friday-q-a-2017-06-30-dissecting-objc-msgsend-on-arm64.md) | 已翻译 |
| 深度补充 | [键值编码与观察](../../blogs/zh/objcio/key-value-coding-and-observing.md) | 技术博客 | objc.io | [中文](../../blogs/zh/objcio/key-value-coding-and-observing.md) | 已翻译 |
| 深度补充 | [键值观察](../../blogs/zh/nshipster/key-value-observing.md) | 技术博客 | NSHipster (Mattt) | [中文](../../blogs/zh/nshipster/key-value-observing.md) | 已翻译 |
| 补充资料 | [[objc 解析]: dyld 共享缓存中的选择器唯一化](../../blogs/zh/sealiesoftware/objc-explain-selector-uniquing-in-the-dyld-shared-cache.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-selector-uniquing-in-the-dyld-shared-cache.md) | 已翻译 |
| 补充资料 | [[objc 解析]: objc_msgSend_fpret](../../blogs/zh/sealiesoftware/objc-explain-objc-msgsend-fpret.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-objc-msgsend-fpret.md) | 已翻译 |
| 补充资料 | [[objc 解析]: objc_msgSend_stret](../../blogs/zh/sealiesoftware/objc-explain-objc-msgsend-stret.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-objc-msgsend-stret.md) | 已翻译 |
| 补充资料 | [[objc 解析]: objc_msgSend_vtable](../../blogs/zh/sealiesoftware/objc-explain-objc-msgsend-vtable.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-objc-msgsend-vtable.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 你在 objc_msgSend() 中崩溃了](../../blogs/zh/sealiesoftware/objc-explain-so-you-crashed-in-objc-msgsend.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-so-you-crashed-in-objc-msgsend.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 向 nil 发送消息的返回值](../../blogs/zh/sealiesoftware/objc-explain-return-value-of-message-to-nil-f96179.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-return-value-of-message-to-nil-f96179.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 向 nil 发送消息的返回值](../../blogs/zh/sealiesoftware/objc-explain-return-value-of-message-to-nil.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-return-value-of-message-to-nil.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 所以你在 objc_msgSend() 中崩溃了：iPhone 5s 版](../../blogs/zh/sealiesoftware/objc-explain-so-you-crashed-in-objc-msgsend-iphone-5s-edition.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-so-you-crashed-in-objc-msgsend-iphone-5s-edition.md) | 已翻译 |
| 补充资料 | [[objc 解析]: 所以你在 objc_msgSend() 中崩溃了：iPhone 版](../../blogs/zh/sealiesoftware/objc-explain-so-you-crashed-in-objc-msgsend-iphone-edition.md) | 技术博客 | Hamster Emporium (Greg Parker) | [中文](../../blogs/zh/sealiesoftware/objc-explain-so-you-crashed-in-objc-msgsend-iphone-edition.md) | 已翻译 |
| 补充资料 | [Associated Object 与 Dealloc](../../blogs/zh/yulingtianxia/associated-object-%E4%B8%8E-dealloc.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/associated-object-%E4%B8%8E-dealloc.md) | 原生中文 |
| 补充资料 | [objc category的秘密](../../blogs/zh/sunnyxx/objc-category%E7%9A%84%E7%A7%98%E5%AF%86-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 技术博客 | sunnyxx (孙源) | [中文](../../blogs/zh/sunnyxx/objc-category%E7%9A%84%E7%A7%98%E5%AF%86-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 原生中文 |
| 补充资料 | [objc kvo简单探索](../../blogs/zh/sunnyxx/objc-kvo%E7%AE%80%E5%8D%95%E6%8E%A2%E7%B4%A2-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 技术博客 | sunnyxx (孙源) | [中文](../../blogs/zh/sunnyxx/objc-kvo%E7%AE%80%E5%8D%95%E6%8E%A2%E7%B4%A2-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 原生中文 |
| 补充资料 | [Objective-C Associated Objects 的实现原理](../../blogs/zh/leichunfeng/objective-c-associated-objects-%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 技术博客 | 雷纯锋 | [中文](../../blogs/zh/leichunfeng/objective-c-associated-objects-%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 补充资料 | [Objective-C Category 的实现原理](../../blogs/zh/leichunfeng/objective-c-category-%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 技术博客 | 雷纯锋 | [中文](../../blogs/zh/leichunfeng/objective-c-category-%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 补充资料 | [Objective-C Message Throttle and Debounce](../../blogs/zh/yulingtianxia/objective-c-message-throttle-and-debounce.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/objective-c-message-throttle-and-debounce.md) | 原生中文 |
| 补充资料 | [Objective-C Method Swizzling](../../blogs/zh/yulingtianxia/objective-c-method-swizzling.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/objective-c-method-swizzling.md) | 原生中文 |
| 补充资料 | [Objective-C Method Swizzling 的最佳实践](../../blogs/zh/leichunfeng/objective-c-method-swizzling-%E7%9A%84%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5.md) | 技术博客 | 雷纯锋 | [中文](../../blogs/zh/leichunfeng/objective-c-method-swizzling-%E7%9A%84%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5.md) | 原生中文 |
| 补充资料 | [Objective-C Runtime](../../blogs/zh/yulingtianxia/objective-c-runtime.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/objective-c-runtime.md) | 原生中文 |
| 补充资料 | [Objective-C Runtime 运行时之一：类与对象](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%B8%80-%E7%B1%BB%E4%B8%8E%E5%AF%B9%E8%B1%A1.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%B8%80-%E7%B1%BB%E4%B8%8E%E5%AF%B9%E8%B1%A1.md) | 原生中文 |
| 补充资料 | [Objective-C Runtime 运行时之三：方法与消息](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%B8%89-%E6%96%B9%E6%B3%95%E4%B8%8E%E6%B6%88%E6%81%AF.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%B8%89-%E6%96%B9%E6%B3%95%E4%B8%8E%E6%B6%88%E6%81%AF.md) | 原生中文 |
| 补充资料 | [Objective-C Runtime 运行时之二：成员变量与属性](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%BA%8C-%E6%88%90%E5%91%98%E5%8F%98%E9%87%8F%E4%B8%8E%E5%B1%9E%E6%80%A7.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%BA%8C-%E6%88%90%E5%91%98%E5%8F%98%E9%87%8F%E4%B8%8E%E5%B1%9E%E6%80%A7.md) | 原生中文 |
| 补充资料 | [Objective-C Runtime 运行时之五：协议与分类](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%BA%94-%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%88%86%E7%B1%BB.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E4%BA%94-%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%88%86%E7%B1%BB.md) | 原生中文 |
| 补充资料 | [Objective-C Runtime 运行时之六：拾遗](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E5%85%AD-%E6%8B%BE%E9%81%97.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E5%85%AD-%E6%8B%BE%E9%81%97.md) | 原生中文 |
| 补充资料 | [Objective-C Runtime 运行时之四：Method Swizzling](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E5%9B%9B-method-swizzling.md) | 技术博客 | 南峰子 (southpeak) | [中文](../../blogs/zh/southpeak/objective-c-runtime-%E8%BF%90%E8%A1%8C%E6%97%B6%E4%B9%8B%E5%9B%9B-method-swizzling.md) | 原生中文 |
| 补充资料 | [Objective-C 消息发送与转发机制原理](../../blogs/zh/yulingtianxia/objective-c-%E6%B6%88%E6%81%AF%E5%8F%91%E9%80%81%E4%B8%8E%E8%BD%AC%E5%8F%91%E6%9C%BA%E5%88%B6%E5%8E%9F%E7%90%86.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/objective-c-%E6%B6%88%E6%81%AF%E5%8F%91%E9%80%81%E4%B8%8E%E8%BD%AC%E5%8F%91%E6%9C%BA%E5%88%B6%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 补充资料 | [Swift 中的运行时多态](../../blogs/zh/belkadan/run-time-polymorphism-in-swift.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/run-time-polymorphism-in-swift.md) | 已翻译 |
| 补充资料 | [Swift 运行时](../../blogs/zh/belkadan/swift-runtime.md) | 技术博客 | Belkadan (Jordan Rose, 前 Swift 编译器工程师) | [中文](../../blogs/zh/belkadan/swift-runtime.md) | 已翻译 |
| 补充资料 | [启用强化运行时后 Mac 应用测试失败](../../blogs/zh/jessesquires/mac-app-tests-fail-with-hardened-runtime-enabled.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/mac-app-tests-fail-with-hardened-runtime-enabled.md) | 已翻译 |
| 补充资料 | [神经病院objc runtime入院考试](../../blogs/zh/sunnyxx/%E7%A5%9E%E7%BB%8F%E7%97%85%E9%99%A2objc-runtime%E5%85%A5%E9%99%A2%E8%80%83%E8%AF%95-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 技术博客 | sunnyxx (孙源) | [中文](../../blogs/zh/sunnyxx/%E7%A5%9E%E7%BB%8F%E7%97%85%E9%99%A2objc-runtime%E5%85%A5%E9%99%A2%E8%80%83%E8%AF%95-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 原生中文 |
| 补充资料 | [绕过 objc_msgSend](../../blogs/zh/saagarjha/bypassing-objc-msgsend.md) | 技术博客 | Saagar Jha | [中文](../../blogs/zh/saagarjha/bypassing-objc-msgsend.md) | 已翻译 |
| 补充资料 | [重识 Objective-C Runtime - Smalltalk 与 C 的融合](../../blogs/zh/sunnyxx/%E9%87%8D%E8%AF%86-objective-c-runtime-smalltalk-%E4%B8%8E-c-%E7%9A%84%E8%9E%8D%E5%90%88-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 技术博客 | sunnyxx (孙源) | [中文](../../blogs/zh/sunnyxx/%E9%87%8D%E8%AF%86-objective-c-runtime-smalltalk-%E4%B8%8E-c-%E7%9A%84%E8%9E%8D%E5%90%88-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 原生中文 |
| 补充资料 | [重识 Objective-C Runtime - 看透 Type 与 Value](../../blogs/zh/sunnyxx/%E9%87%8D%E8%AF%86-objective-c-runtime-%E7%9C%8B%E9%80%8F-type-%E4%B8%8E-value-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2-b558a0.md) | 技术博客 | sunnyxx (孙源) | [中文](../../blogs/zh/sunnyxx/%E9%87%8D%E8%AF%86-objective-c-runtime-%E7%9C%8B%E9%80%8F-type-%E4%B8%8E-value-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2-b558a0.md) | 原生中文 |
| 补充资料 | [重识 Objective-C Runtime - 看透 Type 与 Value](../../blogs/zh/sunnyxx/%E9%87%8D%E8%AF%86-objective-c-runtime-%E7%9C%8B%E9%80%8F-type-%E4%B8%8E-value-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 技术博客 | sunnyxx (孙源) | [中文](../../blogs/zh/sunnyxx/%E9%87%8D%E8%AF%86-objective-c-runtime-%E7%9C%8B%E9%80%8F-type-%E4%B8%8E-value-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) | 原生中文 |
| 补充资料 | [Objective-C runtime机制(7)——SideTables, SideTable, weak_table, weak_entry_t](../../blogs/snapshots/blog.csdn.net/objective-c-runtime%E6%9C%BA%E5%88%B6-7-sidetables-sidetable-weak-table-weak-entry-t.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/objective-c-runtime%E6%9C%BA%E5%88%B6-7-sidetables-sidetable-weak-table-weak-entry-t.md) | 原生中文 |

## 未翻译资料

共 3 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [通信模式](../../blogs/en/objcio/communication-patterns.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/communication-patterns.md) | 仅标题中文，正文待翻译 |
| 官方资料 | [Predefined CFCharacterSet Selector Values](../../apple-docs/en/corefoundation/predefined_cfcharacterset_selector_values.md) | Apple 文档 | Apple · Core Foundation | [英文](../../apple-docs/en/corefoundation/predefined_cfcharacterset_selector_values.md) | 待翻译 |
| 补充资料 | [使用内核扩展更改 macOS 的运行时间](../../blogs/en/worthdoingbadly/changing-macos-s-uptime-with-a-kernel-extension.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [英文](../../blogs/en/worthdoingbadly/changing-macos-s-uptime-with-a-kernel-extension.md) | 仅标题中文，正文待翻译 |
