# 模块 7：持久化、序列化、源码库与架构

> 把本地存储、模型转换、源码阅读和工程架构放进同一条实践链路。
> 对应仓库范围：数据与持久化、架构、测试与工程实践。中文正文优先，随后列出未翻译资料。

- [返回暑期计划知识地图](../summer.md)
- [查看全库主题地图](../topics.md)

## 学习步骤

| 步骤 | 内容 | 产出 |
|---|---|---|
| 7.1 | iOS 持久化选择：UserDefaults、文件目录、Keychain、SQLite/Core Data | 按敏感度、规模、查询、备份和可重建性做选择表 |
| 7.2 | 数据库最低要求：SQL CRUD、insert、事务、ACID、隔离、B/B+ 树、索引 | 一组 CRUD + transaction；B+ 树为何适合磁盘的图 |
| 7.3 | Protocol Buffers、JSON、XML 的语义与取舍 | 同一模型三种编码对比；手算一个简单 protobuf wire format |
| 7.4 | JSONModel 必看：从公开 API 追一条 JSON → Model 调用链 | 主调用链 + 属性元数据表 |
| 7.5 | YYModel：沿同一问题对照 Runtime、缓存与线程安全 | JSONModel / YYModel 结构化差异表 |
| 7.6 | SDWebImage 必看：下载、缓存命中、回调、图片解码、去重、取消、内存/磁盘策略 | `sd_setImage` 到 manager/downloader/cache 状态机 |
| 7.7 | 架构设计：MVC、MVVM、MVVM 双向绑定、设计模式复盘 | 同一列表页面 MVC/MVVM 结构图与数据流 |
| 7.8 | 综合小项目：URLSession → 模型转换 → 图片缓存 → 持久化 → UITableView | 可运行项目 + 10 分钟全链路讲解 |

## 计划指定材料

- [有效使用文件系统](../../apple-docs/zh/foundation/using-the-file-system-effectively.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/using-the-file-system-effectively.md) — 本仓库资料
- [UserDefaults](../../apple-docs/zh/foundation/userdefaults.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/userdefaults.md) — 本仓库资料
- [钥匙串服务](../../apple-docs/zh/security/keychain-services.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/security/keychain-services.md) — 本仓库资料
- [Core Data](../../apple-docs/zh/coredata.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/coredata.md) — 本仓库资料
- [计划材料](https://protobuf.dev/programming-guides/json/) — 第三方博客（未归档（protobuf.dev））
- [JSONSerialization](../../apple-docs/zh/foundation/jsonserialization.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/jsonserialization.md) — 本仓库资料
- [URL 加载系统](../../apple-docs/zh/foundation/url-loading-system.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/url-loading-system.md) — 本仓库资料
- [URLCache](../../apple-docs/zh/foundation/urlcache.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/urlcache.md) — 本仓库资料
- [计划材料](https://github.com/jsonmodel/jsonmodel) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://github.com/ibireme/YYModel) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://github.com/SDWebImage/SDWebImage) — GitHub 源码（待 clone 到 oss/）
- [SDWebImage实现分析](../../blogs/zh/southpeak/sdwebimage%E5%AE%9E%E7%8E%B0%E5%88%86%E6%9E%90.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/southpeak/sdwebimage%E5%AE%9E%E7%8E%B0%E5%88%86%E6%9E%90.md) — 本仓库资料
- [Core Data Overview](../../blogs/en/objcio/core-data-overview.md) · [原文网页](https://www.objc.io/issues/4-core-data/core-data-overview/) — 第三方博客
- [计划材料](https://www.sqlite.org/lang.html) — 第三方博客（未归档（sqlite.org））
- [计划材料](https://www.sqlite.org/lang_transaction.html) — 第三方博客（未归档（sqlite.org））
- [计划材料](https://www.sqlite.org/fileformat2.html) — 第三方博客（未归档（sqlite.org））
- [计划材料](https://xiaolincoding.com/interview/mysql.html) — 第三方博客（未归档（xiaolincoding.com））
- [计划材料](https://xiaolincoding.com/mysql/index/why_index_chose_bpuls_tree.html) — 第三方博客（未归档（xiaolincoding.com））
- [计划材料](https://xiaolincoding.com/mysql/index/page.html) — 第三方博客（未归档（xiaolincoding.com））
- [计划材料](https://github.com/halfrost/Halfrost-Field/blob/master/contents/iOS/Realm/Realm%E6%95%B0%E6%8D%AE%E5%BA%93%20%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E2%80%9C%E6%94%BE%E5%BC%83%E2%80%9D.md) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://www.bswanson.dev/blog/exploring-sqlite-internals/) — 第三方博客（未归档（bswanson.dev））
- [计划材料](https://www.cnblogs.com/huahuahu/p/sqlite-suo-yin-de-yuan-li-ji-ying-yong.html) — 第三方博客（未归档（cnblogs.com））
- [计划材料](https://www.rfc-editor.org/rfc/rfc8259) — 第三方博客（未归档（rfc-editor.org））
- [计划材料](https://www.w3.org/TR/xml/) — 第三方博客（未归档（w3.org））
- [计划材料](https://protobuf.dev/programming-guides/encoding/) — 第三方博客（未归档（protobuf.dev））
- [解密 Protobuf 线格式](../../blogs/zh/kreya/demystifying-the-protobuf-wire-format-kreya.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/kreya/demystifying-the-protobuf-wire-format-kreya.md) — 本仓库资料
- [解密 Protobuf 线格式（二）](../../blogs/zh/kreya/demystifying-the-protobuf-wire-format-part-2-kreya.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/blogs/zh/kreya/demystifying-the-protobuf-wire-format-part-2-kreya.md) — 本仓库资料
- [计划材料](https://victoriametrics.com/blog/go-protobuf/) — 第三方博客（未归档（victoriametrics.com））
- [计划材料](https://auth0.com/blog/beating-json-performance-with-protobuf/) — 第三方博客（未归档（auth0.com））
- [计划材料](https://knightsj.github.io/2017/02/22/JSONModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90/) — 第三方博客（未归档（knightsj.github.io））
- [计划材料](https://github.com/ibireme/YYModel/blob/master/YYModel/NSObject%2BYYModel.m) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://github.com/ibireme/YYModel/blob/master/YYModel/YYClassInfo.m) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://blog.csdn.net/game3108/article/details/52388089) — 第三方博客（未归档（blog.csdn.net））
- [计划材料](https://blog.csdn.net/Lu_Ca/article/details/114532423) — 第三方博客（未归档（blog.csdn.net））
- [计划材料](https://blog.itlee.top/2017/12/21/YYModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90%E4%B8%80/) — 第三方博客（未归档（blog.itlee.top））
- [计划材料](https://sdwebimage.github.io/) — 第三方博客（未归档（sdwebimage.github.io））
- [计划材料](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/UIImageView%2BWebCache.m) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDWebImageManager.m) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDImageCache.m) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDWebImageDownloader.m) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://www.cnblogs.com/zhangzhang-y/p/13584570.html) — 第三方博客（未归档（cnblogs.com））
- [计划材料](https://github.com/SDWebImage/SDWebImage/wiki/5.6-Code-Architecture-Analysis) — GitHub 源码（待 clone 到 oss/）
- [计划材料](https://looseyi.github.io/post/sourcecode-ios/source-code-sdweb-en1/) — 第三方博客（未归档（looseyi.github.io））
- [Model-View-Controller](../../legacy-archive/vault/documentation/General/Concepts%20in%20Objective-C%20Programming/Model-View-Controller.md) · [原文网页](https://github.com/XiyouMobile3G-iOS/apple-developer-archive-vault/blob/main/documentation/General/Concepts%20in%20Objective-C%20Programming/Model-View-Controller.md) — Apple 旧归档
- [Introduction to MVVM](../../blogs/en/objcio/introduction-to-mvvm.md) · [原文网页](https://www.objc.io/issues/13-architecture/mvvm/) — 第三方博客
- [计划材料](https://www.objc.io/issues/13-architecture/) — 第三方博客（未归档（objc.io））
- [计划材料](https://www.objc.io/books/app-architecture/) — 第三方博客（未归档（objc.io））
- [计划材料](https://blog.csdn.net/weixin_46818265/article/details/142442895) — 第三方博客（未归档（blog.csdn.net））
- [计划材料](https://www.jianshu.com/p/e59bb8f59302) — 第三方博客（未归档（jianshu.com））
- [URLSession](../../apple-docs/zh/foundation/urlsession.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/foundation/urlsession.md) — 本仓库资料
- [UITableView](../../apple-docs/zh/uikit/uitableview.md) · [原文网页](https://github.com/Biscoffee/apple-docs-vault/blob/main/apple-docs/zh/uikit/uitableview.md) — 本仓库资料

## 中文资料

共 88 份。包含译文和原生中文文章。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [huahuahu](../../blogs/snapshots/cnblogs.com/huahuahu.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/huahuahu.md) | 原生中文 |
| 计划核心 | [iOS 中 KVC 与 KVO 底层原理](../../blogs/snapshots/blog.csdn.net/ios-%E4%B8%AD-kvc-%E4%B8%8E-kvo-%E5%BA%95%E5%B1%82%E5%8E%9F%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/ios-%E4%B8%AD-kvc-%E4%B8%8E-kvo-%E5%BA%95%E5%B1%82%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 计划核心 | [iOS开发 -- KVO的实现原理与具体应用](../../blogs/snapshots/jianshu.com/ios%E5%BC%80%E5%8F%91-kvo%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E4%B8%8E%E5%85%B7%E4%BD%93%E5%BA%94%E7%94%A8.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/jianshu.com/ios%E5%BC%80%E5%8F%91-kvo%E7%9A%84%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E4%B8%8E%E5%85%B7%E4%BD%93%E5%BA%94%E7%94%A8.md) | 原生中文 |
| 计划核心 | [Protobuf 工作原理——数据编码的艺术](../../blogs/snapshots-zh/victoriametrics.com/how-protobuf-works-the-art-of-data-encoding.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/victoriametrics.com/how-protobuf-works-the-art-of-data-encoding.md) | 已翻译 |
| 计划核心 | [SDWebImage v5.6 架构](../../blogs/snapshots-zh/looseyi.github.io/the-architecture-of-sdwebimage-v5-6.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/looseyi.github.io/the-architecture-of-sdwebimage-v5-6.md) | 已翻译 |
| 计划核心 | [SDWebImage 实现原理与源码简析](../../blogs/snapshots/cnblogs.com/sdwebimage-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E4%B8%8E%E6%BA%90%E7%A0%81%E7%AE%80%E6%9E%90.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/cnblogs.com/sdwebimage-%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E4%B8%8E%E6%BA%90%E7%A0%81%E7%AE%80%E6%9E%90.md) | 原生中文 |
| 计划核心 | [SDWebImage 首页](../../blogs/snapshots-zh/sdwebimage.github.io/sdwebimage-home-documentation.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/sdwebimage.github.io/sdwebimage-home-documentation.md) | 已翻译 |
| 计划核心 | [YYModel内部实现原理](../../blogs/snapshots/blog.csdn.net/yymodel%E5%86%85%E9%83%A8%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/yymodel%E5%86%85%E9%83%A8%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86.md) | 原生中文 |
| 计划核心 | [YYModel源代码分析（一）整体介绍](../../blogs/snapshots/blog.csdn.net/yymodel%E6%BA%90%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90-%E4%B8%80-%E6%95%B4%E4%BD%93%E4%BB%8B%E7%BB%8D.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.csdn.net/yymodel%E6%BA%90%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90-%E4%B8%80-%E6%95%B4%E4%BD%93%E4%BB%8B%E7%BB%8D.md) | 原生中文 |
| 计划核心 | [从YYModel源码中可以学到什么：前篇](../../blogs/snapshots/blog.itlee.top/%E4%BB%8Eyymodel%E6%BA%90%E7%A0%81%E4%B8%AD%E5%8F%AF%E4%BB%A5%E5%AD%A6%E5%88%B0%E4%BB%80%E4%B9%88-%E5%89%8D%E7%AF%87.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/blog.itlee.top/%E4%BB%8Eyymodel%E6%BA%90%E7%A0%81%E4%B8%AD%E5%8F%AF%E4%BB%A5%E5%AD%A6%E5%88%B0%E4%BB%80%E4%B9%88-%E5%89%8D%E7%AF%87.md) | 原生中文 |
| 计划核心 | [使用方法](../../blogs/snapshots/knightsj.github.io/jsonmodel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots/knightsj.github.io/jsonmodel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90.md) | 原生中文 |
| 计划核心 | [全局安装 browserify 以便随时使用](../../blogs/snapshots-zh/auth0.com/beating-json-performance-with-protobuf.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/auth0.com/beating-json-performance-with-protobuf.md) | 已翻译 |
| 计划核心 | [探索 SQLite 的内部机制](../../blogs/snapshots-zh/bswanson.dev/exploring-sqlite-s-internals.md) | 网页快照 | 学习计划网页快照 | [中文](../../blogs/snapshots-zh/bswanson.dev/exploring-sqlite-s-internals.md) | 已翻译 |
| 官方资料 | [Core Data](../../apple-docs/zh/coredata.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata.md) | 已翻译 |
| 官方资料 | [Core Data 栈](../../apple-docs/zh/coredata/core-data-stack.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/core-data-stack.md) | 已翻译 |
| 官方资料 | [Mach-O 架构](../../apple-docs/zh/foundation/1495005-mach-o-architecture.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/1495005-mach-o-architecture.md) | 已翻译 |
| 官方资料 | [为 beta 测试和发布分发你的 App](../../apple-docs/zh/xcode/distributing-your-app-for-beta-testing-and-releases.md) | Apple 文档 | Apple · updates | [中文](../../apple-docs/zh/xcode/distributing-your-app-for-beta-testing-and-releases.md) | 已翻译 |
| 官方资料 | [关于 Apple File System](../../apple-docs/zh/foundation/about-apple-file-system.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/about-apple-file-system.md) | 已翻译 |
| 官方资料 | [向 Xcode 项目添加测试](../../apple-docs/zh/xcode/adding-tests-to-your-xcode-project.md) | Apple 文档 | Apple · updates | [中文](../../apple-docs/zh/xcode/adding-tests-to-your-xcode-project.md) | 已翻译 |
| 官方资料 | [在 Xcode 中使用 StoreKit 事务管理器测试 App 内购买项目](../../apple-docs/zh/xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/testing-in-app-purchases-with-storekit-transaction-manager-in-code.md) | 已翻译 |
| 官方资料 | [在 Xcode 中设置 StoreKit 测试](../../apple-docs/zh/xcode/setting-up-storekit-testing-in-xcode.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/setting-up-storekit-testing-in-xcode.md) | 已翻译 |
| 官方资料 | [在后台使用 Core Data](../../apple-docs/zh/coredata/using-core-data-in-the-background.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/using-core-data-in-the-background.md) | 已翻译 |
| 官方资料 | [在测试中模拟位置](../../apple-docs/zh/xcode/simulating-location-in-tests.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/simulating-location-in-tests.md) | 已翻译 |
| 官方资料 | [对自定类型使用 JSON](../../apple-docs/zh/foundation/using-json-with-custom-types.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/using-json-with-custom-types.md) | 已翻译 |
| 官方资料 | [将 App 从 32 位架构更新到 64 位架构](../../apple-docs/zh/uikit/updating-your-app-from-32-bit-to-64-bit-architecture.md) | Apple 文档 | Apple · UIKit | [中文](../../apple-docs/zh/uikit/updating-your-app-from-32-bit-to-64-bit-architecture.md) | 已翻译 |
| 官方资料 | [归档与序列化](../../apple-docs/zh/foundation/archives-and-serialization.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/archives-and-serialization.md) | 已翻译 |
| 官方资料 | [手动设置 Core Data 堆栈](../../apple-docs/zh/coredata/setting-up-a-core-data-stack-manually.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/setting-up-a-core-data-stack-manually.md) | 已翻译 |
| 官方资料 | [持久化历史记录](../../apple-docs/zh/coredata/persistent-history.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/persistent-history.md) | 已翻译 |
| 官方资料 | [持久化存储类型](../../apple-docs/zh/coredata/persistent-store-types.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/persistent-store-types.md) | 已翻译 |
| 官方资料 | [文件系统](../../apple-docs/zh/foundation/file-system.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/file-system.md) | 已翻译 |
| 官方资料 | [文件系统错误码](../../apple-docs/zh/foundation/file-system-error-codes.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/file-system-error-codes.md) | 已翻译 |
| 官方资料 | [更新现有代码库以适应单元测试](../../apple-docs/zh/xcode/updating-your-existing-codebase-to-accommodate-unit-tests.md) | Apple 文档 | Apple · updates | [中文](../../apple-docs/zh/xcode/updating-your-existing-codebase-to-accommodate-unit-tests.md) | 已翻译 |
| 官方资料 | [有效使用文件系统](../../apple-docs/zh/foundation/using-the-file-system-effectively.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/using-the-file-system-effectively.md) | 已翻译 |
| 官方资料 | [测试](../../apple-docs/zh/xcode/testing.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/testing.md) | 已翻译 |
| 官方资料 | [测试 beta 版操作系统](../../apple-docs/zh/xcode/testing-a-beta-os.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/testing-a-beta-os.md) | 已翻译 |
| 官方资料 | [测试与性能](../../apple-docs/zh/technologyoverviews/testing-and-performance.md) | Apple 文档 | Apple · Technology Overviews | [中文](../../apple-docs/zh/technologyoverviews/testing-and-performance.md) | 已翻译 |
| 官方资料 | [测试发布版本](../../apple-docs/zh/xcode/testing-a-release-build.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/testing-a-release-build.md) | 已翻译 |
| 官方资料 | [测试运行 App 时的本地化](../../apple-docs/zh/xcode/testing-localizations-when-running-your-app.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/testing-localizations-when-running-your-app.md) | 已翻译 |
| 官方资料 | [确定测试覆盖了多少代码](../../apple-docs/zh/xcode/determining-how-much-code-your-tests-cover.md) | Apple 文档 | Apple · updates | [中文](../../apple-docs/zh/xcode/determining-how-much-code-your-tests-cover.md) | 已翻译 |
| 官方资料 | [编写并运行性能测试](../../apple-docs/zh/xcode/writing-and-running-performance-tests.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/writing-and-running-performance-tests.md) | 已翻译 |
| 官方资料 | [编码、解码与序列化](../../apple-docs/zh/swift/encoding-decoding-and-serialization.md) | Apple 文档 | Apple · Swift | [中文](../../apple-docs/zh/swift/encoding-decoding-and-serialization.md) | 已翻译 |
| 官方资料 | [解读崩溃报告的 JSON 格式](../../apple-docs/zh/xcode/interpreting-the-json-format-of-a-crash-report.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/interpreting-the-json-format-of-a-crash-report.md) | 已翻译 |
| 官方资料 | [运行测试与解读结果](../../apple-docs/zh/xcode/running-tests-and-interpreting-results.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/running-tests-and-interpreting-results.md) | 已翻译 |
| 官方资料 | [通过将测试整理为测试计划来改进代码评估](../../apple-docs/zh/xcode/organizing-tests-to-improve-feedback.md) | Apple 文档 | Apple · xcode | [中文](../../apple-docs/zh/xcode/organizing-tests-to-improve-feedback.md) | 已翻译 |
| 官方资料 | [通过访问文件系统提升性能与稳定性](../../apple-docs/zh/foundation/improving-performance-and-stability-when-accessing-the-file-system.md) | Apple 文档 | Apple · Foundation | [中文](../../apple-docs/zh/foundation/improving-performance-and-stability-when-accessing-the-file-system.md) | 已翻译 |
| 官方资料 | [配置 Core Data 栈](../../apple-docs/zh/coredata/setting-up-a-core-data-stack.md) | Apple 文档 | Apple · Core Data | [中文](../../apple-docs/zh/coredata/setting-up-a-core-data-stack.md) | 已翻译 |
| 官方资料 | [Apple 文件系统的新功能](../../wwdc/zh/wwdc2019/710-what-s-new-in-apple-file-systems.md) | WWDC | Apple · WWDC2019 | [中文](../../wwdc/zh/wwdc2019/710-what-s-new-in-apple-file-systems.md) | 已翻译 |
| 官方资料 | [Core Data 新变化](../../wwdc/zh/wwdc2023/10186-what-s-new-in-core-data.md) | WWDC | Apple · WWDC2023 | [中文](../../wwdc/zh/wwdc2023/10186-what-s-new-in-core-data.md) | 已翻译 |
| 官方资料 | [Core Data 最佳实践](../../wwdc/zh/wwdc2018/224-core-data-best-practices.md) | WWDC | Apple · WWDC2018 | [中文](../../wwdc/zh/wwdc2018/224-core-data-best-practices.md) | 已翻译 |
| 官方资料 | [Core Data：细节与格言](../../wwdc/zh/wwdc2020/10017-core-data-sundries-and-maxims.md) | WWDC | Apple · WWDC2020 | [中文](../../wwdc/zh/wwdc2020/10017-core-data-sundries-and-maxims.md) | 已翻译 |
| 官方资料 | [优化 Core Data 和 CloudKit 的使用](../../wwdc/zh/wwdc2022/10119-optimize-your-use-of-core-data-and-cloudkit.md) | WWDC | Apple · WWDC2022 | [中文](../../wwdc/zh/wwdc2022/10119-optimize-your-use-of-core-data-and-cloudkit.md) | 已翻译 |
| 官方资料 | [使用 SwiftData 历史记录追踪模型变更](../../wwdc/zh/wwdc2024/10075-track-model-changes-with-swiftdata-history.md) | WWDC | Apple · WWDC2024 | [中文](../../wwdc/zh/wwdc2024/10075-track-model-changes-with-swiftdata-history.md) | 已翻译 |
| 官方资料 | [将 Core Data 与 CloudKit 配合使用](../../wwdc/zh/wwdc2019/202-using-core-data-with-cloudkit.md) | WWDC | Apple · WWDC2019 | [中文](../../wwdc/zh/wwdc2019/202-using-core-data-with-cloudkit.md) | 已翻译 |
| 官方资料 | [演进你的 Core Data 架构](../../wwdc/zh/wwdc2022/10120-evolve-your-core-data-schema.md) | WWDC | Apple · WWDC2022 | [中文](../../wwdc/zh/wwdc2022/10120-evolve-your-core-data-schema.md) | 已翻译 |
| 深度补充 | [Core Data 与数据库的区别 \| Cocoa with Love](../../blogs/zh/cocoawithlove/the-differences-between-core-data-and-a-database-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/the-differences-between-core-data-and-a-database-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Core Data：单行获取](../../blogs/zh/cocoawithlove/core-data-one-line-fetch-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/core-data-one-line-fetch-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [iOS JSON 模型转换库评测](../../blogs/zh/ibireme/ios-json-%E6%A8%A1%E5%9E%8B%E8%BD%AC%E6%8D%A2%E5%BA%93%E8%AF%84%E6%B5%8B.md) | 技术博客 | ibireme (郭曜源) | [中文](../../blogs/zh/ibireme/ios-json-%E6%A8%A1%E5%9E%8B%E8%BD%AC%E6%8D%A2%E5%BA%93%E8%AF%84%E6%B5%8B.md) | 原生中文 |
| 深度补充 | [Objective-C 内部探秘：类的架构](../../blogs/zh/alwaysprocessing/objective-c-internals-class-architecture-objective-c-has-an-unique-class-architecture-wher.md) | 技术博客 | Always Processing (Brian T. Kelley) | [中文](../../blogs/zh/alwaysprocessing/objective-c-internals-class-architecture-objective-c-has-an-unique-class-architecture-wher.md) | 已翻译 |
| 深度补充 | [使用非常大的分层数据集测试 Core Data \| Cocoa with Love](../../blogs/zh/cocoawithlove/testing-core-data-with-very-big-hierarchical-data-sets-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/testing-core-data-with-very-big-hierarchical-data-sets-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [在 Core Data 中立即传播删除操作](../../blogs/zh/cocoawithlove/propagate-deletes-immediately-in-core-data-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/propagate-deletes-immediately-in-core-data-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [性能测试: 替换 Core Data Key Paths](../../blogs/zh/cocoawithlove/performance-tests-replacing-core-data-key-paths-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/performance-tests-replacing-core-data-key-paths-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [测试任意指针是否为有效的对象指针 \| Cocoa with Love](../../blogs/zh/cocoawithlove/testing-if-an-arbitrary-pointer-is-a-valid-object-pointer-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/testing-if-an-arbitrary-pointer-is-a-valid-object-pointer-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [通过 HTTP 获取并解析 XML 或 JSON 的类](../../blogs/zh/cocoawithlove/classes-for-fetching-and-parsing-xml-or-json-via-http-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/classes-for-fetching-and-parsing-xml-or-json-via-http-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [速度测试: NSManagedObject ObjC-2.0 存取器](../../blogs/zh/cocoawithlove/speed-test-nsmanagedobject-objc-2-0-accessors-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [中文](../../blogs/zh/cocoawithlove/speed-test-nsmanagedobject-objc-2-0-accessors-cocoa-with-love.md) | 已翻译 |
| 深度补充 | [Android 中的 SQLite 数据库支持](../../blogs/zh/objccn/android-%E4%B8%AD%E7%9A%84-sqlite-%E6%95%B0%E6%8D%AE%E5%BA%93%E6%94%AF%E6%8C%81.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/android-%E4%B8%AD%E7%9A%84-sqlite-%E6%95%B0%E6%8D%AE%E5%BA%93%E6%94%AF%E6%8C%81.md) | 原生中文 |
| 深度补充 | [Core Data 概述](../../blogs/zh/objccn/core-data-%E6%A6%82%E8%BF%B0.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/core-data-%E6%A6%82%E8%BF%B0.md) | 原生中文 |
| 深度补充 | [Core Data 网络应用实例](../../blogs/zh/objccn/core-data-%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E5%AE%9E%E4%BE%8B.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/core-data-%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8%E5%AE%9E%E4%BE%8B.md) | 原生中文 |
| 深度补充 | [一个完整的 Core Data 应用](../../blogs/zh/objccn/%E4%B8%80%E4%B8%AA%E5%AE%8C%E6%95%B4%E7%9A%84-core-data-%E5%BA%94%E7%94%A8.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E4%B8%80%E4%B8%AA%E5%AE%8C%E6%95%B4%E7%9A%84-core-data-%E5%BA%94%E7%94%A8.md) | 原生中文 |
| 深度补充 | [用 SQLite 和 FMDB 替代 Core Data](../../blogs/zh/objccn/%E7%94%A8-sqlite-%E5%92%8C-fmdb-%E6%9B%BF%E4%BB%A3-core-data.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E7%94%A8-sqlite-%E5%92%8C-fmdb-%E6%9B%BF%E4%BB%A3-core-data.md) | 原生中文 |
| 深度补充 | [自定义 Core Data 迁移](../../blogs/zh/objccn/%E8%87%AA%E5%AE%9A%E4%B9%89-core-data-%E8%BF%81%E7%A7%BB.md) | 技术博客 | ObjC 中国 (objccn.io) | [中文](../../blogs/zh/objccn/%E8%87%AA%E5%AE%9A%E4%B9%89-core-data-%E8%BF%81%E7%A7%BB.md) | 原生中文 |
| 补充资料 | [Core Data 图书](../../blogs/zh/oleb/the-core-data-book.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/the-core-data-book.md) | 已翻译 |
| 补充资料 | [Core Data 并发调试](../../blogs/zh/oleb/core-data-concurrency-debugging.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/core-data-concurrency-debugging.md) | 已翻译 |
| 补充资料 | [Facebook iOS 应用架构的演进](../../blogs/zh/fbeng/the-evolution-of-facebook-s-ios-app-architecture.md) | 技术博客 | Meta Engineering — iOS | [中文](../../blogs/zh/fbeng/the-evolution-of-facebook-s-ios-app-architecture.md) | 已翻译 |
| 补充资料 | [Steve Jobs 谈文件系统](../../blogs/zh/oleb/steve-jobs-on-the-file-system.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/steve-jobs-on-the-file-system.md) | 已翻译 |
| 补充资料 | [Swift 中更好的 Core Data 模型](../../blogs/zh/jessesquires/better-core-data-models-in-swift.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/better-core-data-models-in-swift.md) | 已翻译 |
| 补充资料 | [Swift、Core Data 与单元测试](../../blogs/zh/jessesquires/swift-core-data-and-unit-testing.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/swift-core-data-and-unit-testing.md) | 已翻译 |
| 补充资料 | [《App Architecture》一书](../../blogs/zh/oleb/app-architecture-book.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/app-architecture-book.md) | 已翻译 |
| 补充资料 | [使用 SQLite Magellan 漏洞让 Chrome 70 崩溃](../../blogs/zh/worthdoingbadly/crash-chrome-70-with-the-sqlite-magellan-bug.md) | 技术博客 | worthdoingbadly (Zhuowei Zhang) | [中文](../../blogs/zh/worthdoingbadly/crash-chrome-70-with-the-sqlite-magellan-bug.md) | 已翻译 |
| 补充资料 | [初识Core Data(1)](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-1.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-1.md) | 原生中文 |
| 补充资料 | [初识Core Data(2)](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-2.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-2.md) | 原生中文 |
| 补充资料 | [初识Core Data(3)](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-3.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-3.md) | 原生中文 |
| 补充资料 | [初识Core Data(4)](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-4.md) | 技术博客 | 杨萧玉 | [中文](../../blogs/zh/yulingtianxia/%E5%88%9D%E8%AF%86core-data-4.md) | 原生中文 |
| 补充资料 | [启用强化运行时后 Mac 应用测试失败](../../blogs/zh/jessesquires/mac-app-tests-fail-with-hardened-runtime-enabled.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/mac-app-tests-fail-with-hardened-runtime-enabled.md) | 已翻译 |
| 补充资料 | [在 Swift 中使用 Core Data](../../blogs/zh/jessesquires/using-core-data-in-swift.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/using-core-data-in-swift.md) | 已翻译 |
| 补充资料 | [如何制作 Core Data SQLite 数据库的副本](../../blogs/zh/oleb/how-to-make-a-copy-of-a-core-data-sqlite-database.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/how-to-make-a-copy-of-a-core-data-sqlite-database.md) | 已翻译 |
| 补充资料 | [如何在 Swift 中更优雅地处理非可选 Core Data 属性](../../blogs/zh/jessesquires/how-to-more-gracefully-handle-non-optional-core-data-properties-in-swift.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/how-to-more-gracefully-handle-non-optional-core-data-properties-in-swift.md) | 已翻译 |
| 补充资料 | [支持 JSON Feed](../../blogs/zh/jessesquires/supporting-json-feed.md) | 技术博客 | Jesse Squires | [中文](../../blogs/zh/jessesquires/supporting-json-feed.md) | 已翻译 |
| 补充资料 | [检查 Core Data 特性](../../blogs/zh/oleb/inspecting-core-data-attributes.md) | 技术博客 | Ole Begemann | [中文](../../blogs/zh/oleb/inspecting-core-data-attributes.md) | 已翻译 |

## 未翻译资料

共 132 份。可能已有中文目录标题，但正文仍为英文。

| 优先级 | 文章 | 类型 | 来源 | 阅读 | 状态 |
|---|---|---|---|---|---|
| 计划核心 | [Core Data 概述](../../blogs/en/objcio/core-data-overview.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/core-data-overview.md) | 仅标题中文，正文待翻译 |
| 计划核心 | [MVVM 介绍](../../blogs/en/objcio/introduction-to-mvvm.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/introduction-to-mvvm.md) | 仅标题中文，正文待翻译 |
| 计划核心 | [可扩展标记语言（XML）1.0（第五版）](../../blogs/snapshots/w3.org/extensible-markup-language-xml-1-0-fifth-edition.md) | 网页快照 | 学习计划网页快照 | [英文](../../blogs/snapshots/w3.org/extensible-markup-language-xml-1-0-fifth-edition.md) | 仅标题中文，正文待翻译 |
| 官方资料 | [Adopting SwiftData for a Core Data app](../../apple-docs/en/coredata/adopting-swiftdata-for-a-core-data-app.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/adopting-swiftdata-for-a-core-data-app.md) | 待翻译 |
| 官方资料 | [architecture](../../apple-docs/en/kernel/architecture.md) | Apple 文档 | Apple · Kernel | [英文](../../apple-docs/en/kernel/architecture.md) | 待翻译 |
| 官方资料 | [Architecture Types](../../apple-docs/en/corefoundation/1537096-architecture-types.md) | Apple 文档 | Apple · Core Foundation | [英文](../../apple-docs/en/corefoundation/1537096-architecture-types.md) | 待翻译 |
| 官方资料 | [Calculating primitive visibility using depth testing](../../apple-docs/en/metal/calculating-primitive-visibility-using-depth-testing.md) | Apple 文档 | Apple · Metal | [英文](../../apple-docs/en/metal/calculating-primitive-visibility-using-depth-testing.md) | 待翻译 |
| 官方资料 | [Code Signing Architecture Flags](../../apple-docs/en/security/code-signing-architecture-flags.md) | Apple 文档 | Apple · Security | [英文](../../apple-docs/en/security/code-signing-architecture-flags.md) | 待翻译 |
| 官方资料 | [Common File System Resource Keys](../../apple-docs/en/corefoundation/common-file-system-resource-keys.md) | Apple 文档 | Apple · Core Foundation | [英文](../../apple-docs/en/corefoundation/common-file-system-resource-keys.md) | 待翻译 |
| 官方资料 | [Core Data Constants](../../apple-docs/en/coredata/core-data-constants.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/core-data-constants.md) | 待翻译 |
| 官方资料 | [Core Data model](../../apple-docs/en/coredata/core-data-model.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/core-data-model.md) | 待翻译 |
| 官方资料 | [Creating a Core Data model](../../apple-docs/en/coredata/creating-a-core-data-model.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/creating-a-core-data-model.md) | 待翻译 |
| 官方资料 | [Creating a Core Data Model for CloudKit](../../apple-docs/en/coredata/creating-a-core-data-model-for-cloudkit.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/creating-a-core-data-model-for-cloudkit.md) | 待翻译 |
| 官方资料 | [Defining test functions](../../apple-docs/en/testing/definingtests.md) | Apple 文档 | Apple · Swift Testing | [英文](../../apple-docs/en/testing/definingtests.md) | 待翻译 |
| 官方资料 | [Evaluating an app’s video color using video test equipment](../../apple-docs/en/avfoundation/evaluating-an-app-s-video-color-using-video-test-equipment.md) | Apple 文档 | Apple · AVFoundation | [英文](../../apple-docs/en/avfoundation/evaluating-an-app-s-video-color-using-video-test-equipment.md) | 待翻译 |
| 官方资料 | [Evaluating video using QuickTime test pattern files](../../apple-docs/en/avfoundation/evaluating-video-using-quicktime-test-pattern-files.md) | Apple 文档 | Apple · AVFoundation | [英文](../../apple-docs/en/avfoundation/evaluating-video-using-quicktime-test-pattern-files.md) | 待翻译 |
| 官方资料 | [Handling Different Data Types in Core Data](../../apple-docs/en/coredata/handling-different-data-types-in-core-data.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/handling-different-data-types-in-core-data.md) | 待翻译 |
| 官方资料 | [HPKEPublicKeySerialization Implementations](../../apple-docs/en/cryptokit/xwingmlkem768x25519/publickey/hpkepublickeyserialization-implementations.md) | Apple 文档 | Apple · Apple CryptoKit | [英文](../../apple-docs/en/cryptokit/xwingmlkem768x25519/publickey/hpkepublickeyserialization-implementations.md) | 待翻译 |
| 官方资料 | [HPKEPublicKeySerialization Implementations](../../apple-docs/en/cryptokit/curve25519/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | Apple 文档 | Apple · Apple CryptoKit | [英文](../../apple-docs/en/cryptokit/curve25519/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | 待翻译 |
| 官方资料 | [HPKEPublicKeySerialization Implementations](../../apple-docs/en/cryptokit/p256/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | Apple 文档 | Apple · Apple CryptoKit | [英文](../../apple-docs/en/cryptokit/p256/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | 待翻译 |
| 官方资料 | [HPKEPublicKeySerialization Implementations](../../apple-docs/en/cryptokit/p384/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | Apple 文档 | Apple · Apple CryptoKit | [英文](../../apple-docs/en/cryptokit/p384/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | 待翻译 |
| 官方资料 | [HPKEPublicKeySerialization Implementations](../../apple-docs/en/cryptokit/p521/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | Apple 文档 | Apple · Apple CryptoKit | [英文](../../apple-docs/en/cryptokit/p521/keyagreement/publickey/hpkepublickeyserialization-implementations.md) | 待翻译 |
| 官方资料 | [Linking Data Between Two Core Data Stores](../../apple-docs/en/coredata/linking-data-between-two-core-data-stores.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/linking-data-between-two-core-data-stores.md) | 待翻译 |
| 官方资料 | [Migrating a test from XCTest](../../apple-docs/en/testing/migratingfromxctest.md) | Apple 文档 | Apple · Swift Testing | [英文](../../apple-docs/en/testing/migratingfromxctest.md) | 待翻译 |
| 官方资料 | [Migrating your data model automatically](../../apple-docs/en/coredata/migrating-your-data-model-automatically.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/migrating-your-data-model-automatically.md) | 待翻译 |
| 官方资料 | [Mirroring a Core Data store with CloudKit](../../apple-docs/en/coredata/mirroring-a-core-data-store-with-cloudkit.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/mirroring-a-core-data-store-with-cloudkit.md) | 待翻译 |
| 官方资料 | [Modeling data](../../apple-docs/en/coredata/modeling-data.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/modeling-data.md) | 待翻译 |
| 官方资料 | [Persistent storage](../../apple-docs/en/swiftui/persistent-storage.md) | Apple 文档 | Apple · SwiftUI | [英文](../../apple-docs/en/swiftui/persistent-storage.md) | 待翻译 |
| 官方资料 | [Policy Database Constants](../../apple-docs/en/security/policy-database-constants.md) | Apple 文档 | Apple · Security | [英文](../../apple-docs/en/security/policy-database-constants.md) | 待翻译 |
| 官方资料 | [Reading CloudKit Records for Core Data](../../apple-docs/en/coredata/reading-cloudkit-records-for-core-data.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/reading-cloudkit-records-for-core-data.md) | 待翻译 |
| 官方资料 | [Recording UI automation for testing](../../apple-docs/en/xcuiautomation/recording-ui-automation-for-testing.md) | Apple 文档 | Apple · XCUIAutomation | [英文](../../apple-docs/en/xcuiautomation/recording-ui-automation-for-testing.md) | 待翻译 |
| 官方资料 | [Running tests serially or in parallel](../../apple-docs/en/testing/parallelization.md) | Apple 文档 | Apple · Swift Testing | [英文](../../apple-docs/en/testing/parallelization.md) | 待翻译 |
| 官方资料 | [Setting Up Core Data with CloudKit](../../apple-docs/en/coredata/setting-up-core-data-with-cloudkit.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/setting-up-core-data-with-cloudkit.md) | 待翻译 |
| 官方资料 | [Sharing Core Data objects between iCloud users](../../apple-docs/en/coredata/sharing-core-data-objects-between-icloud-users.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/sharing-core-data-objects-between-icloud-users.md) | 待翻译 |
| 官方资料 | [Syncing a Core Data Store with CloudKit](../../apple-docs/en/coredata/syncing-a-core-data-store-with-cloudkit.md) | Apple 文档 | Apple · Core Data | [英文](../../apple-docs/en/coredata/syncing-a-core-data-store-with-cloudkit.md) | 待翻译 |
| 官方资料 | [Testing a payment request](../../apple-docs/en/storekit/testing-a-payment-request.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-a-payment-request.md) | 待翻译 |
| 官方资料 | [Testing a product request](../../apple-docs/en/storekit/testing-a-product-request.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-a-product-request.md) | 待翻译 |
| 官方资料 | [Testing a successful transaction](../../apple-docs/en/storekit/testing-a-successful-transaction.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-a-successful-transaction.md) | 待翻译 |
| 官方资料 | [Testing ad attributions with a downloaded profile](../../apple-docs/en/storekit/testing-ad-attributions-with-a-downloaded-profile.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-ad-attributions-with-a-downloaded-profile.md) | 待翻译 |
| 官方资料 | [Testing age assurance in sandbox](../../apple-docs/en/storekit/testing-age-assurance-in-sandbox.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-age-assurance-in-sandbox.md) | 待翻译 |
| 官方资料 | [Testing an auto-renewable subscription](../../apple-docs/en/storekit/testing-an-auto-renewable-subscription.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-an-auto-renewable-subscription.md) | 待翻译 |
| 官方资料 | [Testing an interrupted purchase](../../apple-docs/en/storekit/testing-an-interrupted-purchase.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-an-interrupted-purchase.md) | 待翻译 |
| 官方资料 | [Testing and Debugging L4S in Your App](../../apple-docs/en/network/testing-and-debugging-l4s-in-your-app.md) | Apple 文档 | Apple · Network | [英文](../../apple-docs/en/network/testing-and-debugging-l4s-in-your-app.md) | 待翻译 |
| 官方资料 | [Testing and validating ad impression signatures and postbacks for SKAdNetwork](../../apple-docs/en/storekittest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md) | Apple 文档 | Apple · StoreKit Test | [英文](../../apple-docs/en/storekittest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork.md) | 待翻译 |
| 官方资料 | [Testing App Store server notifications](../../apple-docs/en/storekit/testing-app-store-server-notifications.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-app-store-server-notifications.md) | 待翻译 |
| 官方资料 | [Testing Ask to Buy in Xcode](../../apple-docs/en/storekit/testing-ask-to-buy-in-xcode.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-ask-to-buy-in-xcode.md) | 待翻译 |
| 官方资料 | [Testing asynchronous code](../../apple-docs/en/testing/testing-asynchronous-code.md) | Apple 文档 | Apple · Swift Testing | [英文](../../apple-docs/en/testing/testing-asynchronous-code.md) | 待翻译 |
| 官方资料 | [Testing at all stages of development with Xcode and the sandbox](../../apple-docs/en/storekit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md) | 待翻译 |
| 官方资料 | [Testing complete transactions](../../apple-docs/en/storekit/testing-complete-transactions.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-complete-transactions.md) | 待翻译 |
| 官方资料 | [Testing disabling auto-renew](../../apple-docs/en/storekit/testing-disabling-auto-renew.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-disabling-auto-renew.md) | 待翻译 |
| 官方资料 | [Testing failing subscription renewals and In-App Purchases](../../apple-docs/en/storekit/testing-failing-subscription-renewals-and-in-app-purchases.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-failing-subscription-renewals-and-in-app-purchases.md) | 待翻译 |
| 官方资料 | [Testing Family Sharing](../../apple-docs/en/storekit/testing-family-sharing.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-family-sharing.md) | 待翻译 |
| 官方资料 | [Testing fetching product identifiers](../../apple-docs/en/storekit/testing-fetching-product-identifiers.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-fetching-product-identifiers.md) | 待翻译 |
| 官方资料 | [Testing In-App Purchases in Xcode](../../apple-docs/en/storekit/testing-in-app-purchases-in-xcode.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-in-app-purchases-in-xcode.md) | 待翻译 |
| 官方资料 | [Testing In-App Purchases with sandbox](../../apple-docs/en/storekit/testing-in-app-purchases-with-sandbox.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-in-app-purchases-with-sandbox.md) | 待翻译 |
| 官方资料 | [Testing introductory offers](../../apple-docs/en/storekit/testing-introductory-offers.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-introductory-offers.md) | 待翻译 |
| 官方资料 | [Testing invalid product identifier handling](../../apple-docs/en/storekit/testing-invalid-product-identifier-handling.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-invalid-product-identifier-handling.md) | 待翻译 |
| 官方资料 | [Testing notifications using the Push Notification Console](../../apple-docs/en/usernotifications/testing-notifications-using-the-push-notification-console.md) | Apple 文档 | Apple · User Notifications | [英文](../../apple-docs/en/usernotifications/testing-notifications-using-the-push-notification-console.md) | 待翻译 |
| 官方资料 | [Testing promoted In-App Purchases](../../apple-docs/en/storekit/testing-promoted-in-app-purchases.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-promoted-in-app-purchases.md) | 待翻译 |
| 官方资料 | [Testing purchases made outside your app](../../apple-docs/en/storekit/testing-purchases-made-outside-your-app.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-purchases-made-outside-your-app.md) | 待翻译 |
| 官方资料 | [Testing refund requests](../../apple-docs/en/storekit/testing-refund-requests.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-refund-requests.md) | 待翻译 |
| 官方资料 | [Testing resubscribing from the subscriptions page](../../apple-docs/en/storekit/testing-resubscribing-from-the-subscriptions-page.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-resubscribing-from-the-subscriptions-page.md) | 待翻译 |
| 官方资料 | [Testing transaction observer code](../../apple-docs/en/storekit/testing-transaction-observer-code.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-transaction-observer-code.md) | 待翻译 |
| 官方资料 | [Testing transactions that use custom link tokens](../../apple-docs/en/storekit/testing-transactions-that-use-custom-link-tokens.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-transactions-that-use-custom-link-tokens.md) | 待翻译 |
| 官方资料 | [Testing win-back offers in the sandbox environment](../../apple-docs/en/storekit/testing-win-back-offers-in-the-sandbox-environment.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-win-back-offers-in-the-sandbox-environment.md) | 待翻译 |
| 官方资料 | [Testing win-back offers in Xcode](../../apple-docs/en/storekit/testing-win-back-offers-in-xcode.md) | Apple 文档 | Apple · StoreKit | [英文](../../apple-docs/en/storekit/testing-win-back-offers-in-xcode.md) | 待翻译 |
| 官方资料 | [Build robust and resumable file transfers](../../wwdc/en/wwdc2023/10006-build-robust-and-resumable-file-transfers.md) | WWDC | Apple · WWDC2023 | [英文](../../wwdc/en/wwdc2023/10006-build-robust-and-resumable-file-transfers.md) | 待翻译 |
| 官方资料 | [Explore the new system architecture of Apple silicon Macs](../../wwdc/en/wwdc2020/10686-explore-the-new-system-architecture-of-apple-silicon-macs.md) | WWDC | Apple · WWDC2020 | [英文](../../wwdc/en/wwdc2020/10686-explore-the-new-system-architecture-of-apple-silicon-macs.md) | 待翻译 |
| 官方资料 | [Sync files to the cloud with FileProvider on macOS](../../wwdc/en/wwdc2021/10182-sync-files-to-the-cloud-with-fileprovider-on-macos.md) | WWDC | Apple · WWDC2021 | [英文](../../wwdc/en/wwdc2021/10182-sync-files-to-the-cloud-with-fileprovider-on-macos.md) | 待翻译 |
| 官方资料 | [What’s New in File Management and Quick Look](../../wwdc/en/wwdc2019/719-what-s-new-in-file-management-and-quick-look.md) | WWDC | Apple · WWDC2019 | [英文](../../wwdc/en/wwdc2019/719-what-s-new-in-file-management-and-quick-look.md) | 待翻译 |
| 深度补充 | [Android 中的 SQLite 数据库支持](../../blogs/en/objcio/sqlite-database-support-in-android.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/sqlite-database-support-in-android.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [Combine 的 22 个简短测试 – 第 1 部分：协议 \| Cocoa with Love](../../blogs/en/cocoawithlove/22-short-tests-of-combine-part-1-protocols-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/22-short-tests-of-combine-part-1-protocols-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [Combine 的 22 个简短测试 – 第 2 部分：共享 \| Cocoa with Love](../../blogs/en/cocoawithlove/22-short-tests-of-combine-part-2-sharing-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/22-short-tests-of-combine-part-2-sharing-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [Combine 的 22 个简短测试 – 第 3 部分：异步 \| Cocoa with Love](../../blogs/en/cocoawithlove/22-short-tests-of-combine-part-3-asynchrony-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/22-short-tests-of-combine-part-3-asynchrony-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [iPhone 上的自动化用户界面测试](../../blogs/en/cocoawithlove/automated-user-interface-testing-on-the-iphone-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/automated-user-interface-testing-on-the-iphone-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [SwiftUI 应用架构基础：第一部分——通过迭代和集成进行编码](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-1-coding-through-iteration-and-integration-cocoa-w.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-1-coding-through-iteration-and-integration-cocoa-w.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [SwiftUI 应用架构基础：第三部分——模块分离的层](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-3-module-separated-layers-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-3-module-separated-layers-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [SwiftUI 应用架构基础：第二部分——SwiftUI 的自然模式](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-2-swiftui-s-natural-pattern-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-2-swiftui-s-natural-pattern-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [SwiftUI 应用架构基础：第四部分——服务](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-4-services-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/app-architecture-basics-in-swiftui-part-4-services-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [一个附带完整单元测试的 iPhone 示例应用](../../blogs/en/cocoawithlove/a-sample-iphone-application-with-complete-unit-tests-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/a-sample-iphone-application-with-complete-unit-tests-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [一个附带完整单元测试的 Mac 示例应用](../../blogs/en/cocoawithlove/a-sample-mac-application-with-complete-unit-tests-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/a-sample-mac-application-with-complete-unit-tests-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [使用 SQLite 和 FMDB 替代 Core Data](../../blogs/en/objcio/on-using-sqlite-and-fmdb-instead-of-core-data.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/on-using-sqlite-and-fmdb-instead-of-core-data.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [使用 XCTest 进行真实世界测试](../../blogs/en/objcio/real-world-testing-with-xctest.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/real-world-testing-with-xctest.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [单元测试](../../blogs/en/nshipster/unit-testing.md) | 技术博客 | NSHipster (Mattt) | [英文](../../blogs/en/nshipster/unit-testing.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [完整的 Core Data 应用程序](../../blogs/en/objcio/a-complete-core-data-application.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/a-complete-core-data-application.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [快照测试](../../blogs/en/objcio/snapshot-testing.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/snapshot-testing.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [无单元测试的应用程序开发质量控制](../../blogs/en/cocoawithlove/quality-control-in-application-development-without-unit-testing-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/quality-control-in-application-development-without-unit-testing-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [星期五问答 2011-07-22：编写单元测试](../../blogs/en/mikeash/friday-q-a-2011-07-22-writing-unit-tests.md) | 技术博客 | mikeash.com Friday Q&A | [英文](../../blogs/en/mikeash/friday-q-a-2011-07-22-writing-unit-tests.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [测试基于 Hashcash 的反垃圾邮件措施](../../blogs/en/mikeash/testing-hashcash-based-anti-spam-measures.md) | 技术博客 | mikeash.com Friday Q&A | [英文](../../blogs/en/mikeash/testing-hashcash-based-anti-spam-measures.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [测试并发应用](../../blogs/en/objcio/testing-concurrent-applications.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/testing-concurrent-applications.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [测试替身：Mock、Stub 及其他](../../blogs/en/objcio/test-doubles-mocks-stubs-and-more.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/test-doubles-mocks-stubs-and-more.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [测试视图控制器](../../blogs/en/objcio/testing-view-controllers.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/testing-view-controllers.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [用户界面测试](../../blogs/en/objcio/user-interface-testing.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/user-interface-testing.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [糟糕的测试实践](../../blogs/en/objcio/bad-testing-practices.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/bad-testing-practices.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [联网的 Core Data 应用程序](../../blogs/en/objcio/a-networked-core-data-application.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/a-networked-core-data-application.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [自定义 Core Data 迁移](../../blogs/en/objcio/custom-core-data-migrations.md) | 技术博客 | objc.io | [英文](../../blogs/en/objcio/custom-core-data-migrations.md) | 仅标题中文，正文待翻译 |
| 深度补充 | [随时间测试操作 \| Cocoa with Love](../../blogs/en/cocoawithlove/testing-actions-over-time-cocoa-with-love.md) | 技术博客 | Cocoa with Love (Matt Gallagher) | [英文](../../blogs/en/cocoawithlove/testing-actions-over-time-cocoa-with-love.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [2019 年 3 月 21 日 开源 Python 测试运行器，实现并行执行多个测试](../../blogs/en/fbeng/mar-21-2019-open-sourcing-python-test-runner-for-multiple-tests-in-parallel.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/mar-21-2019-open-sourcing-python-test-runner-for-multiple-tests-in-parallel.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [5 款最佳 API 测试工具 \| Kreya](../../blogs/en/kreya/5-best-api-testing-tools-kreya.md) | 技术博客 | Kreya Blog | [英文](../../blogs/en/kreya/5-best-api-testing-tools-kreya.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Airlock – Facebook 的移动端 A/B 测试框架](../../blogs/en/fbeng/airlock-facebook-s-mobile-a-b-testing-framework.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/airlock-facebook-s-mobile-a-b-testing-framework.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [API 设计中的心智模型](../../blogs/en/oleb/mental-models-in-api-design.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/mental-models-in-api-design.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Apple 对应用架构的看法](../../blogs/en/oleb/apple-s-take-on-app-architecture.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/apple-s-take-on-app-architecture.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [CGPath 命中测试](../../blogs/en/oleb/cgpath-hit-testing.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/cgpath-hit-testing.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Ellen Shapiro：由外而内——使用 UI 测试开始改进应用](../../blogs/en/oleb/ellen-shapiro-outside-in-using-ui-tests-to-start-improving-your-app.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/ellen-shapiro-outside-in-using-ui-tests-to-start-improving-your-app.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [iOS 的 Xcode UI 测试可靠性技巧](../../blogs/en/jessesquires/xcode-ui-testing-reliability-tips-for-ios.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/xcode-ui-testing-reliability-tips-for-ios.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [OpenAI 谈移动开发、预览与快照测试](../../blogs/en/emergetools/emerge-tools-blog-openai-on-mobile-development-previews-snapshot-testing.md) | 技术博客 | Emerge Tools Blog | [英文](../../blogs/en/emergetools/emerge-tools-blog-openai-on-mobile-development-previews-snapshot-testing.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [UI 测试 Peek 和 Pop](../../blogs/en/saagarjha/ui-testing-peek-and-pop.md) | 技术博客 | Saagar Jha | [英文](../../blogs/en/saagarjha/ui-testing-peek-and-pop.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [Xcode 16 中的 UI 测试改进](../../blogs/en/jessesquires/ui-testing-improvements-in-xcode-16.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/ui-testing-improvements-in-xcode-16.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [z/Architecture 工具链笔记](../../blogs/en/maskray/toolchain-notes-on-z-architecture.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/toolchain-notes-on-z-architecture.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [不使用 OCMock 进行测试和模拟](../../blogs/en/jessesquires/testing-and-mocking-without-ocmock.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/testing-and-mocking-without-ocmock.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [书评：测试驱动 iOS 开发](../../blogs/en/oleb/book-review-test-driven-ios-development.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/book-review-test-driven-ios-development.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [从归档文件中提取成员以满足 DSO 未定义符号](../../blogs/en/maskray/extract-an-archive-member-to-satisfy-a-dso-undef.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/extract-an-archive-member-to-satisfy-a-dso-undef.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [使用 Kreya 测试 API \| Kreya](../../blogs/en/kreya/testing-apis-with-kreya-kreya.md) | 技术博客 | Kreya Blog | [英文](../../blogs/en/kreya/testing-apis-with-kreya-kreya.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [使用 Kreya 测试 REST API \| Kreya](../../blogs/en/kreya/testing-rest-apis-with-kreya-kreya.md) | 技术博客 | Kreya Blog | [英文](../../blogs/en/kreya/testing-rest-apis-with-kreya-kreya.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [发布 Emerge 的 Android 性能测试套件](../../blogs/en/emergetools/emerge-tools-blog-announcing-emerge-s-android-performance-testing-suite.md) | 技术博客 | Emerge Tools Blog | [英文](../../blogs/en/emergetools/emerge-tools-blog-announcing-emerge-s-android-performance-testing-suite.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [在 UI 测试期间从 iOS 模拟器删除应用](../../blogs/en/jessesquires/deleting-your-app-from-the-ios-simulator-during-ui-tests.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/deleting-your-app-from-the-ios-simulator-during-ui-tests.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [基于 LLVM 的突变测试系统。征求意见](../../blogs/en/lowlevelbits/llvm-based-mutation-testing-system-request-for-comments-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/llvm-based-mutation-testing-system-request-for-comments-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [如何使用 Docker 在 Linux 上测试 Swift 包](../../blogs/en/oleb/how-to-test-a-swift-package-on-linux-using-docker.md) | 技术博客 | Ole Begemann | [英文](../../blogs/en/oleb/how-to-test-a-swift-package-on-linux-using-docker.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [如何在不使用 Xcode 项目的情况下测试 iOS Swift 包](../../blogs/en/jessesquires/how-to-test-an-ios-swift-package-without-an-xcode-project.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/how-to-test-an-ios-swift-package-without-an-xcode-project.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [如何（或如何不）测试你的 Mac 应用，并决定支持哪些 macOS 版本](../../blogs/en/jessesquires/how-to-test-your-mac-app-or-not-and-decide-which-versions-of-macos-to-support-or-not.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/how-to-test-your-mac-app-or-not-and-decide-which-versions-of-macos-to-support-or-not.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [工具链测试](../../blogs/en/maskray/toolchain-testing.md) | 技术博客 | MaskRay (宋方睿) | [英文](../../blogs/en/maskray/toolchain-testing.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [摆脱异步测试](../../blogs/en/lowlevelbits/getting-rid-of-asynchronous-tests-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/getting-rid-of-asynchronous-tests-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [突变测试：实现细节](../../blogs/en/lowlevelbits/mutation-testing-implementation-details-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/mutation-testing-implementation-details-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [管理大规模测试的资源](../../blogs/en/fbeng/managing-resources-for-large-scale-testing.md) | 技术博客 | Meta Engineering — iOS | [英文](../../blogs/en/fbeng/managing-resources-for-large-scale-testing.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [船舶工程](../../blogs/en/ciechanowski/naval-architecture-bartosz-ciechanowski.md) | 技术博客 | Bartosz Ciechanowski | [英文](../../blogs/en/ciechanowski/naval-architecture-bartosz-ciechanowski.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [被测系统](../../blogs/en/lowlevelbits/system-under-test-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/system-under-test-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [被测系统：FreeBSD](../../blogs/en/lowlevelbits/system-under-test-freebsd-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/system-under-test-freebsd-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [被测系统：GNU Make](../../blogs/en/lowlevelbits/system-under-test-gnu-make-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/system-under-test-gnu-make-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [被测系统：LLVM](../../blogs/en/lowlevelbits/system-under-test-llvm-low-level-bits.md) | 技术博客 | Low Level Bits (Alex Denisov) | [英文](../../blogs/en/lowlevelbits/system-under-test-llvm-low-level-bits.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [解决方法：运行框架项目测试后 Xcode 13 失败](../../blogs/en/jessesquires/workaround-xcode-13-failure-after-running-framework-project-tests.md) | 技术博客 | Jesse Squires | [英文](../../blogs/en/jessesquires/workaround-xcode-13-failure-after-running-framework-project-tests.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [通过单元测试覆盖率增强 Xcode 预览](../../blogs/en/emergetools/enhance-xcode-previews-with-unit-test-coverage.md) | 技术博客 | Emerge Tools Blog | [英文](../../blogs/en/emergetools/enhance-xcode-previews-with-unit-test-coverage.md) | 仅标题中文，正文待翻译 |
| 补充资料 | [通过快照测试捕获 API 回归 \| Kreya](../../blogs/en/kreya/catching-api-regressions-with-snapshot-testing-kreya.md) | 技术博客 | Kreya Blog | [英文](../../blogs/en/kreya/catching-api-regressions-with-snapshot-testing-kreya.md) | 仅标题中文，正文待翻译 |
