# 学习计划点名文章 · 逐篇快照报告

> 由 `tools/snapshot.py` 生成于 2026-07-27 08:25。
> 覆盖范围：学习计划里点名、且**未被整站归档覆盖**的「平台单篇 + 单次引用小站」文章。
> 不整站抓的理由见 `meta/recon/CHINESE_SOURCES.md`：CSDN / 简书 / 博客园上同一篇
> Runtime 文章有几十个逐字雷同的版本；而只被引用一次的小站，为一篇文章配一套抓取规则不划算。

## 1. 总账

| 项 | 数 |
|---|---:|
| 目标 URL | 108 |
| 　平台单篇 | 41 |
| 　单次引用小站 | 67 |
| **快照成功** | **86** |
| 　中文 | 56 |
| 　英文 | 30 |
| **失败** | **22** |

失败按原因：

| 原因 | 条数 |
|---|---:|
| robots 禁止 | 17 |
| 抓取失败 | 4 |
| 内容不是目标文章（人工核实） | 1 |

## 2. 失败清单（需人工补救）

- **robots 禁止**：站点的 `robots.txt` 明确拒绝（对所有爬虫 `Disallow: /`，或点名
  禁止 `ClaudeBot`）。这类**不绕过**，请在浏览器里手动打开另存。
- **抓取失败**：域名已失效、站点返回 4xx/5xx、或有 JS 挑战（WAF）。已按 2 秒间隔
  重试过、并尝试过 http↔https 互换与跟随 `<meta refresh>`。
- **找不到正文容器 / 正文过短**：抓到了 HTML 但结构不认识，**没有硬塞容器**，
  避免写出一个正文丢失却看起来成功的文件。

### robots 禁止（17 条）

| 计划位置 | URL | 详情 |
|---|---|---|
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 10｜用一个小项目证明知识连接起来了（对应 全阶段串联） | https://baijiahao.baidu.com/s?id=1670083688956388773&wfr=spider&for=pc | robots.txt 对所有爬虫 Disallow: / |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 2｜离屏渲染先学定义，再看触发条件（对应 W5-02） | https://www.hackingwithswift.com/articles/155/advanced-uiview-shadow-effects-using-shadowpath | robots.txt 点名禁止 ['claudebot']：Disallow: / |
| 第四周：线程、GCD、Operation 与锁 / Day 4｜Operation 是“可管理的任务图”（对应 W3-05） | https://ioscoachfrank.com/chaining-nsoperations.html | robots.txt 点名禁止 ['claudebot']：Disallow: / |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01） | https://jinxuebin.cn/2019/06/AutoReleasePool%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E6%8E%A2%E7%A9%B6/ | robots.txt 点名禁止 ['claudebot']：Disallow: / |
| 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16） | https://medium.com/fantageek/understanding-weak-and-strong-in-objective-c-d17ba4c2c297 | robots.txt 点名禁止 ['amazonbot', 'applebot-extended', 'bytespider', 'claudebot', 'facebookbot', 'googleother', 'gptbot', 'meta-externalagent']：Disallow: / |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01） | https://medium.com/ios-os-x-development/understanding-cocoa-and-cocoa-touch-responder-chain-12fe558ebe97 | robots.txt 点名禁止 ['amazonbot', 'applebot-extended', 'bytespider', 'claudebot', 'facebookbot', 'googleother', 'gptbot', 'meta-externalagent']：Disallow: / |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 5｜生命周期必须按场景观测（对应 W5-06） | https://medium.com/@dhrumilraval212/mastering-the-uiviewcontroller-lifecycle-a-senior-developers-deep-dive-4cc8082cd3d6 | robots.txt 点名禁止 ['amazonbot', 'applebot-extended', 'bytespider', 'claudebot', 'facebookbot', 'googleother', 'gptbot', 'meta-externalagent']：Disallow: / |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 4｜先建立 baseline，再谈列表优化（对应 W6-09） | https://medium.com/jike-engineering/asyncdisplaykit%E4%BB%8B%E7%BB%8D-%E4%B8%80-6b871d29e005 | robots.txt 点名禁止 ['amazonbot', 'applebot-extended', 'bytespider', 'claudebot', 'facebookbot', 'googleother', 'gptbot', 'meta-externalagent']：Disallow: / |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 4｜先建立 baseline，再谈列表优化（对应 W6-09） | https://medium.com/@iosengineering/better-uitableviews-pt-1-performance-a76dcd76d772 | robots.txt 点名禁止 ['amazonbot', 'applebot-extended', 'bytespider', 'claudebot', 'facebookbot', 'googleother', 'gptbot', 'meta-externalagent']：Disallow: / |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 1｜RunLoop 先学“一轮发生什么”（对应 W4-02） | https://meldstudio.co/blog/macos-cfrunloop-internals-scheduling-high-precision-timers-and-recurring-tasks/ | robots.txt 点名禁止 ['claudebot']：Disallow: / |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 5｜把 Runtime 初始化放进 App 冷启动（对应 W6-08） | https://mp.weixin.qq.com/s/Drmmx5JtjG3UtTFksL6Q8Q | robots.txt 对所有爬虫 Disallow: / |
| 第一周：对象、类与所有权的地基 / Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06） | https://roadmap.isylar.com/iOS/Knowledge/RuntimeCls.html | robots.txt 对所有爬虫 Disallow: / |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 4｜先建立 baseline，再谈列表优化（对应 W6-09） | https://www.swiftcafe.io/post/asdk | robots.txt 点名禁止 ['claudebot']：Disallow: / |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09） | https://zhuanlan.zhihu.com/p/587704697 | robots.txt 对所有爬虫 Disallow: / |
| 第四周：线程、GCD、Operation 与锁 / Day 6｜锁的学习方式是“按约束选择”（对应 W3-11） | https://zhuanlan.zhihu.com/p/587418305 | robots.txt 对所有爬虫 Disallow: / |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 5｜集合先学稳定语义，再看某版本实现（对应 W6-10） | https://zhuanlan.zhihu.com/p/25063245 | robots.txt 对所有爬虫 Disallow: / |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08） | https://zhuanlan.zhihu.com/p/597864788 | robots.txt 对所有爬虫 Disallow: / |

### 抓取失败（4 条）

| 计划位置 | URL | 详情 |
|---|---|---|
| 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16） | https://bytes.vokal.io/objc-block-capture-weakself/ | network HTTP 502, 0 字节；已查 Web Archive：无快照，记为不可归档 |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01） | https://devyang.space/2019/05/05/autoreleasepool/ | network HTTP 502, 0 字节；已查 Web Archive：无快照，记为不可归档 |
| 第二周：weak、属性关键字与 Block / Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06） | https://www.uiimage.com/post/blog/ios/sidetables/ | network HTTP 502, 0 字节；已查 Web Archive：无快照，记为不可归档 |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08） | https://zhangbuhuai.com/post/layer-geometry-in-ios.html | http-403 HTTP 403, 548 字节；已查 Web Archive：无快照，记为不可归档 |

### 内容不是目标文章（人工核实）（1 条）

| 计划位置 | URL | 详情 |
|---|---|---|
| 第六周：UIKit 渲染、UITableView 与性能 / Day 2｜离屏渲染先学定义，再看触发条件（对应 W5-02） | https://blog.fearcat.in/a?ID=01750-5926f776-644b-465e-8d4d-d6c7b854e533 | 原站已消失：blog.fearcat.in 现在是广告导流页，整页只有一张追踪像素和一条「Do Not Sell or Share My Personal Information」，没有正文；已查 Web Archive（archive.org/wayback/available）——这个 URL 没有任何快照，记为不可归档 |

## 3. 体检

**「抓取成功」不等于「内容正确」。** 下面三项是逐条检查的结果，不是只报成功数。

### 3.1 最短的一批条目（正文 < 800 字符：0 条）

**没有任何一篇落在 800 字符以下。** 但「零命中」本身不能当结论——上一次报告零失败、正文却全丢，就是这么来的。所以把**最短的 12 篇**逐条打开读了正文，判定见下表；短是因为文章本来就短，还是因为抓漏了，只能人眼分辨。

| 字符 | 中文字符 | 代码块 | 域名 | 标题 | 人工判定 |
|---:|---:|---:|---|---|---|
| 1024 | 496 | 0 | cnblogs.com | [深入ObjC GCD中的dispatch group工作原理。](https://www.cnblogs.com/bbqzsl/p/5287970.html) | **真短文** — 作者开篇即声明「尽量不帖代码，力求用 UML 图来说明工作流」，正文是 dispatch group 五个函数的活动图讲解，完整 |
| 1029 | 218 | 1 | blog.csdn.net | [iOS 中 KVC 与 KVO 底层原理](https://blog.csdn.net/weixin_46818265/article/details/142442895) | **真短文** — KVC/KVO 笔记体短文，本质代码+两张原理图+应用场景列全，结尾自然 |
| 1050 | 624 | 0 | juejin.cn | [iOS 内存分区-- 栈、堆、全局区、常量区、代码区](https://juejin.cn/post/6963188936508178469) | **真短文** — 栈/堆/全局区/常量区/代码区五个分区逐条讲完，收在「其他相关」补充点上，完整 |
| 1233 | 241 | 1 | cloud.tencent.com | [iOS内存管理（四）-strong&copy&weak底层分析](https://cloud.tencent.com/developer/article/2303898) | **真短文** — 以截图为主的笔记体，objc_setProperty 四种组合列全了，图片链接都在 |
| 1405 | 337 | 5 | lvv.me | [weak-strong dance 的注意事项](https://lvv.me/posts/2022/08/13_weak_strong_dance/) | **真短文** — 5 个代码块齐全，讲的就是 weak-strong dance 一个点 |
| 1507 | 514 | 0 | joeshang.github.io | [理解 anchorPoint，position，frame 的关系](https://joeshang.github.io/2014-12-19-understand-anchorpoint-position-frame/) | **真短文** — 从 bounds/center 讲到 anchorPoint 的完整推导，结尾自然 |
| 1816 | 484 | 0 | zhongwuzw.github.io | [iOS知识小集之为什么objc_msgSend()是用汇编实现的](https://zhongwuzw.github.io/2018/04/21/iOS%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgSend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84/) | **真短文** — 「知识小集」系列本来就是一问一答的短篇 |
| 1903 | 365 | 1 | stevenwuzheng.com | [runloop 和线程有什么关系？ - stevenwu](http://stevenwuzheng.com/archives/runloop%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB) | **真短文** — 经 Web Archive 取回（原站证书失效）。pthread 与 RunLoop 一一对应关系，一段 _CFRunLoopGet 源码，结尾自然收束 |
| 1905 | 0 | 0 | sdwebimage.github.io | [SDWebImage Home \| Documentation](https://sdwebimage.github.io/) | **真短文** — 计划链接的就是 DocC 文档首页本身（Overview + 子框架索引），不是文章 |
| 2039 | 584 | 1 | blog.csdn.net | [YYModel内部实现原理](https://blog.csdn.net/Lu_Ca/article/details/114532423) | **真短文** — YYModel 用 objc_msgSend 而非 KVC 赋值的源码笔记，Json↔Model 双向流程讲完，结尾有作者免责声明，完整 |
| 2139 | 755 | 0 | huberyyang.com | [KVO实现原理](https://huberyyang.com/2018/04/13/KVO%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/) | **真短文** — 经 Web Archive 取回（原域名已转卖为博彩站）。KVO 实现原理短文，正文完整 |
| 2159 | 574 | 3 | jianshu.com | [Block的三种类型:__NSGlobalBlock,__NSStackBl](https://www.jianshu.com/p/f0870fa95aac) | **真短文** — 三种 Block 类型各给一段代码，3 个代码块完整 |

### 3.2 疑似导航栏 / 登录提示 / 反爬页（全量扫描，命中 0 条）

全量扫描无命中。扫描的特征词：验证码 / 请先登录 / 页面不存在 / Just a moment / Enable JavaScript / Access denied 等。

### 3.3 中文站的中文字符占比（异常 0 条）

判为中文的 56 篇里，**散文部分**（剔掉围栏代码块）的中文字符占比 < 15% 算异常——正文只剩英文样板的典型症状。不剔代码块的话，源码解析类的中文长文会被大面积误报。

无异常。

中文篇的散文中文字符数：中位 1735，最小 197，最大 37007。
英文篇字符数：中位 16505，最小 1905，最大 141395。

## 4. 成功清单（按学习计划顺序）

| 计划位置 | 标题 | 域名 | 语言 | 字符 | 本地文件 |
|---|---|---|---|---:|---|
| 第一周：对象、类与所有权的地基 / Day 1｜先分清“地址空间”，不要一上来背 isa（对应 W1-10） | [iOS 内存分区-- 栈、堆、全局区、常量区、代码区](https://juejin.cn/post/6963188936508178469) | juejin.cn | zh | 1050 | `blogs/snapshots/juejin.cn/ios-内存分区-栈-堆-全局区-常量区-代码区.md` |
| 第一周：对象、类与所有权的地基 / Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06） | [【OC底层】isMemberOfClass、isKindOfClass原理分析](https://www.cnblogs.com/xgao/p/11277935.html) | cnblogs.com | zh | 2617 | `blogs/snapshots/cnblogs.com/oc底层-ismemberofclass-iskindofclass原理分析.md` |
| 第一周：对象、类与所有权的地基 / Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06） | [isKindOfClass & isMemberOfClass 的分析](https://www.0daybug.com/posts/9972ffa7/index.html) | 0daybug.com | zh | 3537 | `blogs/snapshots/0daybug.com/iskindofclass-ismemberofclass-的分析.md` |
| 第一周：对象、类与所有权的地基 / Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06） | [Testing if an arbitrary pointer is a valid O](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/) | blog.timac.org | en | 17011 | `blogs/snapshots/blog.timac.org/testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object.md` |
| 第二周：weak、属性关键字与 Block / Day 1｜先把属性翻译成所有权关系（对应 W2-07、W2-08、W2-09） | [iOS内存管理（四）-strong&copy&weak底层分析](https://cloud.tencent.com/developer/article/2303898) | cloud.tencent.com | zh | 1233 | `blogs/snapshots/cloud.tencent.com/ios内存管理-四-strong-copy-weak底层分析.md` |
| 第二周：weak、属性关键字与 Block / Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06） | [Objective-C runtime机制(7)——SideTables, SideTa](https://blog.csdn.net/u013378438/article/details/82790332) | blog.csdn.net | zh | 23467 | `blogs/snapshots/blog.csdn.net/objective-c-runtime机制-7-sidetables-sidetable-weak-table-weak-entry-t.md` |
| 第二周：weak、属性关键字与 Block / Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06） | [Surprising Weak-Ref Implementations: Swift, ](https://verdagon.dev/blog/surprising-weak-refs) | verdagon.dev | en | 17678 | `blogs/snapshots/verdagon.dev/surprising-weak-ref-implementations-swift-obj-c-c-rust-and-vale.md` |
| 第二周：weak、属性关键字与 Block / Day 3｜先看 Block 是什么，再谈捕获（对应 W2-12、W2-13、W2-15） | [Block的三种类型:__NSGlobalBlock,__NSStackBlock,__](https://www.jianshu.com/p/f0870fa95aac) | jianshu.com | zh | 2159 | `blogs/snapshots/jianshu.com/block的三种类型-nsglobalblock-nsstackblock-nsmallocblock.md` |
| 第二周：weak、属性关键字与 Block / Day 3｜先看 Block 是什么，再谈捕获（对应 W2-12、W2-13、W2-15） | [Big Nerd Ranch Advanced Mac OS X Programming](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=12) | informit.com | en | 26925 | `blogs/snapshots/informit.com/big-nerd-ranch-advanced-mac-os-x-programming-blocks.md` |
| 第二周：weak、属性关键字与 Block / Day 4｜在结构体基础上研究捕获与复制（对应 W2-10、W2-11） | [深入研究 Block 捕获外部变量和 __block 实现原理](https://halfrost.com/ios_block/) | halfrost.com | zh | 27208 | `blogs/snapshots/halfrost.com/深入研究-block-捕获外部变量和-block-实现原理.md` |
| 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16） | [iOS block底层原理分析(1)--循环引用](https://www.jianshu.com/p/809a9bca597f) | jianshu.com | zh | 9669 | `blogs/snapshots/jianshu.com/ios-block底层原理分析-1-循环引用.md` |
| 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16） | [深入理解"weak-strong dance"](https://luohs.github.io/2017/05/31/20170531/) | luohs.github.io | zh | 5082 | `blogs/snapshots/luohs.github.io/深入理解-weak-strong-dance.md` |
| 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16） | [weak-strong dance 的注意事项](https://lvv.me/posts/2022/08/13_weak_strong_dance/) | lvv.me | zh | 1405 | `blogs/snapshots/lvv.me/weak-strong-dance-的注意事项.md` |
| 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16） | [I finally figured out weakSelf and strongSel](https://dhoerl.wordpress.com/2013/04/23/i-finally-figured-out-weakself-and-strongself/) | dhoerl.wordpress.com | en | 3827 | `blogs/snapshots/dhoerl.wordpress.com/i-finally-figured-out-weakself-and-strongself.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 1｜把方法调用还原为“查找行为”（对应 W1-03） | [objc_msgSend](https://ridiculousfish.com/blog/posts/objc_msgsend.html) | ridiculousfish.com | en | 12111 | `blogs/snapshots/ridiculousfish.com/objc-msgsend.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 1｜把方法调用还原为“查找行为”（对应 W1-03） | [iOS知识小集之为什么objc_msgSend()是用汇编实现的](https://zhongwuzw.github.io/2018/04/21/iOS%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgSend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84/) | zhongwuzw.github.io | zh | 1816 | `blogs/snapshots/zhongwuzw.github.io/ios知识小集之为什么objc-msgsend-是用汇编实现的.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 1｜把方法调用还原为“查找行为”（对应 W1-03） | [浅尝 objc_msgSend](https://kingcos.me/posts/2019/objc_msgsend/) | kingcos.me | zh | 40191 | `blogs/snapshots/kingcos.me/浅尝-objc-msgsend.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 2｜有了方法查找，才学习 Swizzling（对应 W4-04） | [ios method swizzling](https://www.cnblogs.com/developer-ios/p/4948803.html) | cnblogs.com | zh | 4971 | `blogs/snapshots/cnblogs.com/ios-method-swizzling.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 3｜Category 是编译产物，关联对象是运行期旁路（对应 W4-05、W4-06） | [关联对象 AssociatedObject 完全解析 - 面向信仰编程](https://draveness.me/ao.html) | draveness.me | zh | 19471 | `blogs/snapshots/draveness.me/关联对象-associatedobject-完全解析-面向信仰编程.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 3｜Category 是编译产物，关联对象是运行期旁路（对应 W4-05、W4-06） | [iOS Category原理探寻](https://www.cnblogs.com/huanying2000/p/13938350.html) | cnblogs.com | zh | 3952 | `blogs/snapshots/cnblogs.com/ios-category原理探寻.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 4｜用加载时机把 Category、load、initialize 串起来（对应 W5-07） | [iOS-+load和+initialize方法调用时机](https://www.cnblogs.com/junhuawang/p/14304756.html) | cnblogs.com | zh | 9957 | `blogs/snapshots/cnblogs.com/ios-load和-initialize方法调用时机.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09） | [KVC实现原理](https://www.neroxie.com/2019/07/12/KVC%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/) | neroxie.com | zh | 5008 | `blogs/snapshots/neroxie.com/kvc实现原理.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09） | [KVO的实现原理](https://blog.csdn.net/zhoupengju/article/details/53129436) | blog.csdn.net | zh | 2164 | `blogs/snapshots/blog.csdn.net/kvo的实现原理.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09） | [KVO实现原理](https://huberyyang.com/2018/04/13/KVO%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/) | huberyyang.com | zh | 2139 | `blogs/snapshots/huberyyang.com/kvo实现原理.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07） | [6种iOS开发中常用的设计模式](https://blog.csdn.net/weixin_38633659/article/details/149066468) | blog.csdn.net | zh | 6886 | `blogs/snapshots/blog.csdn.net/6种ios开发中常用的设计模式.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07） | [iOS开发那些事-iOS常用设计模式–委托模式](https://www.cnblogs.com/iOS-Blog/archive/2013/02/21/2920926.html) | cnblogs.com | zh | 4126 | `blogs/snapshots/cnblogs.com/ios开发那些事-ios常用设计模式-委托模式.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07） | [底层初窥——NSNotificationCenter](https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/) | coderjtao.github.io | zh | 10440 | `blogs/snapshots/coderjtao.github.io/底层初窥-nsnotificationcenter.md` |
| 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07） | [你真的了解NSNotificationCenter吗？](https://www.cnblogs.com/wujy/p/5825690.html) | cnblogs.com | zh | 6592 | `blogs/snapshots/cnblogs.com/你真的了解nsnotificationcenter吗.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04） | [<pthread.h>](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html) | pubs.opengroup.org | en | 28806 | `blogs/snapshots/pubs.opengroup.org/pthread-h.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04） | [runloop 和线程有什么关系？ - stevenwu](http://stevenwuzheng.com/archives/runloop%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB) | stevenwuzheng.com | zh | 1903 | `blogs/snapshots/stevenwuzheng.com/runloop-和线程有什么关系-stevenwu.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04） | [iOS 多线程：『pthread、NSThread』详尽总结](https://bujige.net/blog/iOS-Complete-learning-pthread-and-NSThread.html) | bujige.net | zh | 10592 | `blogs/snapshots/bujige.net/ios-多线程-pthread-nsthread-详尽总结.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 3｜GCD 从四格矩阵开始，再扩 API（对应 W3-06） | [细说 GCD（Grand Central Dispatch）如何用](https://ming1016.github.io/2016/01/13/how-to-use-gcd/) | ming1016.github.io | zh | 33237 | `blogs/snapshots/ming1016.github.io/细说-gcd-grand-central-dispatch-如何用.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 3｜GCD 从四格矩阵开始，再扩 API（对应 W3-06） | [深入ObjC GCD中的dispatch group工作原理。](https://www.cnblogs.com/bbqzsl/p/5287970.html) | cnblogs.com | zh | 1024 | `blogs/snapshots/cnblogs.com/深入objc-gcd中的dispatch-group工作原理.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 3｜GCD 从四格矩阵开始，再扩 API（对应 W3-06） | [Grand Central Dispatch](https://dirtmelon.github.io/Knowledge/iDev/Multithreading/Grand-Central-Dispatch.html) | dirtmelon.github.io | zh | 14892 | `blogs/snapshots/dirtmelon.github.io/grand-central-dispatch.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 4｜Operation 是“可管理的任务图”（对应 W3-05） | [NSOperation Subclassing](https://nsprogrammer.github.io/jekyll/update/2021/07/02/nsoperation.html) | nsprogrammer.github.io | en | 16540 | `blogs/snapshots/nsprogrammer.github.io/nsoperation-subclassing.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 4｜Operation 是“可管理的任务图”（对应 W3-05） | [NSOperation and NSOperationQueue To Improve ](https://shakuro.com/blog/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios) | shakuro.com | en | 3792 | `blogs/snapshots/shakuro.com/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios-shakuro.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 6｜锁的学习方式是“按约束选择”（对应 W3-11） | [OSSpinLock Is Unsafe](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/) | mjtsai.com | en | 5989 | `blogs/snapshots/mjtsai.com/osspinlock-is-unsafe.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 6｜锁的学习方式是“按约束选择”（对应 W3-11） | [对iOS中自旋锁与优先级反转（Priority inversion）的理解](https://juejin.cn/post/7070416276564213791) | juejin.cn | zh | 2190 | `blogs/snapshots/juejin.cn/对ios中自旋锁与优先级反转-priority-inversion-的理解.md` |
| 第四周：线程、GCD、Operation 与锁 / Day 6｜锁的学习方式是“按约束选择”（对应 W3-11） | [Protecting Critical Sections](https://solarana.dev/2018/04/15/protecting-critical-sections/) | solarana.dev | en | 16505 | `blogs/snapshots/solarana.dev/protecting-critical-sections.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 1｜RunLoop 先学“一轮发生什么”（对应 W4-02） | [Dive into CFRunLoop](https://suelan.github.io/2021/02/13/20210213-dive-into-runloop-ios/) | suelan.github.io | en | 19746 | `blogs/snapshots/suelan.github.io/dive-into-cfrunloop.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 1｜RunLoop 先学“一轮发生什么”（对应 W4-02） | [一份走心的runloop源码分析](https://www.jianshu.com/p/aa0fae8c491b) | jianshu.com | zh | 49933 | `blogs/snapshots/jianshu.com/一份走心的runloop源码分析.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 1｜RunLoop 先学“一轮发生什么”（对应 W4-02） | [Run Loop 记录与源码注释(作者Kylin)](https://www.desgard.com/iOS-Source-Probe/Objective-C/Foundation/Run%20Loop%20%E8%AE%B0%E5%BD%95%E4%B8%8E%E6%BA%90%E7%A0%81%E6%B3%A8%E9%87%8A.html) | desgard.com | zh | 28599 | `blogs/snapshots/desgard.com/run-loop-记录与源码注释-作者kylin.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03） | [Matrix-iOS 卡顿监控](https://cloud.tencent.cn/developer/article/1427933) | cloud.tencent.cn | zh | 4114 | `blogs/snapshots/cloud.tencent.cn/matrix-ios-卡顿监控.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03） | [Runloop 源码笔记：如何实现高可用的卡顿监控](https://ai-chan.top/code/Runloop%E4%B8%8E%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7/) | ai-chan.top | zh | 16003 | `blogs/snapshots/ai-chan.top/runloop-源码笔记-如何实现高可用的卡顿监控.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03） | [iOS 卡顿监测方案总结](https://cloud.tencent.com/developer/article/1895911) | cloud.tencent.com | zh | 13053 | `blogs/snapshots/cloud.tencent.com/ios-卡顿监测方案总结.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01） | [Objective-C之Autorelease Pool底层实现原理记录（双向链表）以及](https://blog.csdn.net/Deft_MKJing/article/details/82947706) | blog.csdn.net | zh | 8247 | `blogs/snapshots/blog.csdn.net/objective-c之autorelease-pool底层实现原理记录-双向链表-以及在runloop中是如何参与进去的.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01） | [Autorelease - Under the Hood](http://matteogobbi.github.io/blog/2014/09/28/autorelease-under-the-hood/) | matteogobbi.github.io | en | 8181 | `blogs/snapshots/matteogobbi.github.io/autorelease-under-the-hood.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01） | [iOS Responder Chain: UIResponder, UIEvent, U](https://swiftrocks.com/understanding-the-ios-responder-chain) | swiftrocks.com | en | 14359 | `blogs/snapshots/swiftrocks.com/ios-responder-chain-uiresponder-uievent-uicontrol-and-uses.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01） | [The Amazing Responder Chain](https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/) | cocoanetics.com | en | 18391 | `blogs/snapshots/cocoanetics.com/the-amazing-responder-chain.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01） | [iOS之深入解析事件传递的响应链](https://bbs.huaweicloud.com/blogs/331365) | bbs.huaweicloud.com | zh | 8198 | `blogs/snapshots/bbs.huaweicloud.com/ios之深入解析事件传递的响应链.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 5｜生命周期必须按场景观测（对应 W5-06） | [UIKit View Lifecycle - viewIsAppearing](https://useyourloaf.com/blog/uikit-view-lifecycle-viewisappearing/) | useyourloaf.com | en | 3980 | `blogs/snapshots/useyourloaf.com/uikit-view-lifecycle-viewisappearing.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08） | [理解 anchorPoint，position，frame 的关系](https://joeshang.github.io/2014-12-19-understand-anchorpoint-position-frame/) | joeshang.github.io | zh | 1507 | `blogs/snapshots/joeshang.github.io/理解-anchorpoint-position-frame-的关系.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08） | [iOS中的图形变换](http://www.samirchen.com/graphic-transform-in-ios/) | samirchen.com | zh | 20954 | `blogs/snapshots/samirchen.com/ios中的图形变换.md` |
| 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08） | [iOS：重识Transform和frame](https://www.jianshu.com/p/e1fec2f92c63) | jianshu.com | zh | 2741 | `blogs/snapshots/jianshu.com/ios-重识transform和frame.md` |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 2｜离屏渲染先学定义，再看触发条件（对应 W5-02） | [iOS Performance tips (I): Drawing shadows](http://angelolloqui.com/blog/30-iOS-Performance-tips-I-Drawing-shadows) | angelolloqui.com | en | 8433 | `blogs/snapshots/angelolloqui.com/ios-performance-tips-i-drawing-shadows.md` |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 2｜离屏渲染先学定义，再看触发条件（对应 W5-02） | [[iOS] CALayer与UIView（以及离屏渲染浅谈）](https://www.jianshu.com/p/e6d44ca9c103) | jianshu.com | zh | 13398 | `blogs/snapshots/jianshu.com/ios-calayer与uiview-以及离屏渲染浅谈.md` |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 4｜先建立 baseline，再谈列表优化（对应 W6-09） | [UITableView 流畅度优化实践](https://blog.aberlt.com/2017/12/30/UITableView-%E6%B5%81%E7%95%85%E5%BA%A6%E4%BC%98%E5%8C%96%E5%AE%9E%E8%B7%B5/) | blog.aberlt.com | zh | 5350 | `blogs/snapshots/blog.aberlt.com/uitableview-流畅度优化实践.md` |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 5｜集合先学稳定语义，再看某版本实现（对应 W6-10） | [NSMutableArray原理揭露](http://blog.joyingx.me/2015/05/03/NSMutableArray%20%E5%8E%9F%E7%90%86%E6%8F%AD%E9%9C%B2/) | blog.joyingx.me | zh | 19688 | `blogs/snapshots/blog.joyingx.me/nsmutablearray原理揭露.md` |
| 第六周：UIKit 渲染、UITableView 与性能 / Day 5｜集合先学稳定语义，再看某版本实现（对应 W6-10） | [普通可变数组](https://www.laoqingcai.com/ios-nsmutablearray/) | laoqingcai.com | zh | 11352 | `blogs/snapshots/laoqingcai.com/普通可变数组.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 1｜从一份源文件走到目标文件（对应 W1-07） | [iOS 编译链接与 Mach-O 深度解析：静态库、动态库原理剖析，到工程化实践](https://segmentfault.com/a/1190000047731614) | segmentfault.com | zh | 190125 | `blogs/snapshots/segmentfault.com/ios-编译链接与-mach-o-深度解析-静态库-动态库原理剖析-到工程化实践.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 3｜静态/动态不是文件后缀问答（对应 W1-09） | [Static and Dynamic Libraries](https://pewpewthespells.com/blog/static_and_dynamic_libraries.html) | pewpewthespells.com | en | 15317 | `blogs/snapshots/pewpewthespells.com/static-and-dynamic-libraries.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 3｜静态/动态不是文件后缀问答（对应 W1-09） | [Introduction to Static vs Dynamic libraries ](https://bpoplauschi.github.io/2021/10/24/Intro-to-static-and-dynamic-libraries-frameworks.html) | bpoplauschi.github.io | en | 10647 | `blogs/snapshots/bpoplauschi.github.io/introduction-to-static-vs-dynamic-libraries-and-frameworks-on-ios-and-macos.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 3｜静态/动态不是文件后缀问答（对应 W1-09） | [Is there such a thing as a static framework?](https://engineering.monday.com/is-there-such-a-thing-as-a-static-framework/) | engineering.monday.com | en | 7836 | `blogs/snapshots/engineering.monday.com/is-there-such-a-thing-as-a-static-framework-monday-ai-engineering.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08） | [Dynamic linking on iOS](https://ddeville.me/2014/04/dynamic-linking/) | ddeville.me | en | 30251 | `blogs/snapshots/ddeville.me/dynamic-linking-on-ios.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08） | [Static linking vs dyld3](https://blog.allegro.tech/2018/05/Static-linking-vs-dyld3.html) | blog.allegro.tech | en | 18743 | `blogs/snapshots/blog.allegro.tech/static-linking-vs-dyld3.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08） | [【WWDC17】优化 APP 启动（dyld 2 -> dyld 3）](https://huang-libo.github.io/posts/App-Startup-Time-dyld/) | huang-libo.github.io | zh | 16594 | `blogs/snapshots/huang-libo.github.io/wwdc17-优化-app-启动-dyld-2-dyld-3.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08） | [Static, Dynamic, Mergeable, oh, my!](https://blog.jacobstechtavern.com/p/static-dynamic-mergeable-oh-my) | blog.jacobstechtavern.com | en | 16434 | `blogs/snapshots/blog.jacobstechtavern.com/static-dynamic-mergeable-oh-my.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 5｜把 Runtime 初始化放进 App 冷启动（对应 W6-08） | [App Launch Time: 7 tips to increase performa](https://www.avanderlee.com/optimization/launch-time-performance-optimization/) | avanderlee.com | en | 13149 | `blogs/snapshots/avanderlee.com/app-launch-time-7-tips-to-increase-performance.md` |
| 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 5｜把 Runtime 初始化放进 App 冷启动（对应 W6-08） | [美团外卖iOS App冷启动治理](https://tech.meituan.com/2018/12/06/waimai-ios-optimizing-startup.html) | tech.meituan.com | zh | 12986 | `blogs/snapshots/tech.meituan.com/美团外卖ios-app冷启动治理.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 2｜有了存储场景，再补数据库最低原理（对应 W6-15、W6-16） | [Exploring SQLite's Internals](https://www.bswanson.dev/blog/exploring-sqlite-internals/) | bswanson.dev | en | 24609 | `blogs/snapshots/bswanson.dev/exploring-sqlite-s-internals.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 2｜有了存储场景，再补数据库最低原理（对应 W6-15、W6-16） | [huahuahu](https://www.cnblogs.com/huahuahu/p/sqlite-suo-yin-de-yuan-li-ji-ying-yong.html) | cnblogs.com | zh | 4510 | `blogs/snapshots/cnblogs.com/huahuahu.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09） | [Extensible Markup Language (XML) 1.0 (Fifth ](https://www.w3.org/TR/xml/) | w3.org | en | 141395 | `blogs/snapshots/w3.org/extensible-markup-language-xml-1-0-fifth-edition.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09） | [How Protobuf Works—The Art of Data Encoding](https://victoriametrics.com/blog/go-protobuf/) | victoriametrics.com | en | 20789 | `blogs/snapshots/victoriametrics.com/how-protobuf-works-the-art-of-data-encoding.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09） | [Beating JSON performance with Protobuf](https://auth0.com/blog/beating-json-performance-with-protobuf/) | auth0.com | en | 32453 | `blogs/snapshots/auth0.com/beating-json-performance-with-protobuf.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 4｜JSONModel 只追一条主链（对应 W6-03） | [JSONModel源码解析](https://knightsj.github.io/2017/02/22/JSONModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90/) | knightsj.github.io | zh | 28854 | `blogs/snapshots/knightsj.github.io/jsonmodel源码解析.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04） | [YYModel源代码分析（一）整体介绍](https://blog.csdn.net/game3108/article/details/52388089) | blog.csdn.net | zh | 4820 | `blogs/snapshots/blog.csdn.net/yymodel源代码分析-一-整体介绍.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04） | [YYModel内部实现原理](https://blog.csdn.net/Lu_Ca/article/details/114532423) | blog.csdn.net | zh | 2039 | `blogs/snapshots/blog.csdn.net/yymodel内部实现原理.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04） | [从YYModel源码中可以学到什么：前篇](https://blog.itlee.top/2017/12/21/YYModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90%E4%B8%80/) | blog.itlee.top | zh | 7043 | `blogs/snapshots/blog.itlee.top/从yymodel源码中可以学到什么-前篇.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 6｜SDWebImage 第一遍只看成功路径（对应 W6-05） | [SDWebImage Home \| Documentation](https://sdwebimage.github.io/) | sdwebimage.github.io | en | 1905 | `blogs/snapshots/sdwebimage.github.io/sdwebimage-home-documentation.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 6｜SDWebImage 第一遍只看成功路径（对应 W6-05） | [SDWebImage 实现原理与源码简析](https://www.cnblogs.com/zhangzhang-y/p/13584570.html) | cnblogs.com | zh | 18394 | `blogs/snapshots/cnblogs.com/sdwebimage-实现原理与源码简析.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 7｜第二遍才看性能与取消（对应 W6-05、W6-09） | [The Architecture of SDWebImage v5.6](https://looseyi.github.io/post/sourcecode-ios/source-code-sdweb-en1/) | looseyi.github.io | en | 49782 | `blogs/snapshots/looseyi.github.io/the-architecture-of-sdwebimage-v5-6.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 8｜架构是前七天代码的职责重排（对应 W6-06、W6-07） | [iOS 中 KVC 与 KVO 底层原理](https://blog.csdn.net/weixin_46818265/article/details/142442895) | blog.csdn.net | zh | 1029 | `blogs/snapshots/blog.csdn.net/ios-中-kvc-与-kvo-底层原理.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 8｜架构是前七天代码的职责重排（对应 W6-06、W6-07） | [iOS开发 -- KVO的实现原理与具体应用](https://www.jianshu.com/p/e59bb8f59302) | jianshu.com | zh | 7881 | `blogs/snapshots/jianshu.com/ios开发-kvo的实现原理与具体应用.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 9｜网络基础放到 URLSession 下面分层（对应 W6-02、W6-11、W6-12） | [TCP 三次握手和四次挥手（传输层）](https://javaguide.cn/cs-basics/network/tcp-connection-and-disconnection.html) | javaguide.cn | zh | 11327 | `blogs/snapshots/javaguide.cn/tcp-三次握手和四次挥手-传输层.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 9｜网络基础放到 URLSession 下面分层（对应 W6-02、W6-11、W6-12） | [详解 TCP 三次握手、四次挥手，附带精美图解和超高频面试题](https://segmentfault.com/a/1190000022410446) | segmentfault.com | zh | 6658 | `blogs/snapshots/segmentfault.com/详解-tcp-三次握手-四次挥手-附带精美图解和超高频面试题.md` |
| 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 10｜用一个小项目证明知识连接起来了（对应 全阶段串联） | [Open Data Structures](https://opendatastructures.org/) | opendatastructures.org | en | 3609 | `blogs/snapshots/opendatastructures.org/open-data-structures.md` |

## 5. 纪律记录

- 每个请求间隔 2 秒，全程单线程顺序抓取。
- 抓取前逐域名查 `robots.txt`，并单独检查 `ClaudeBot` / `anthropic-ai` 段（见 `tools/blog.py` 的 `robots_allows`）。被禁的直接跳过，不绕过。
- 探不到正文容器的记为失败写进上面的清单，**没有硬塞容器**。
- 未改动 `meta/blog_sources.json` 与 `blogs/{en,zh}/` 下的既有内容。
- 「抓取失败」重试过两轮（默认 UA、`--browser-ua`）后仍失败、以及内容判定为
  「原站已下线 / 内容不对」的条目，额外查过 `archive.org/wayback/available`：
  能取到快照的换成 Web Archive 版本（成功清单/短文表里标注「经 Web Archive 取回」），
  查无快照的照实记为不可归档，不臆造内容。
- `massicotte.org`、`casatwy.com`、`blog.devtang.com` 三站点名禁止 AI 爬虫，
  本轮检查过学习计划引用的 URL 里没有这三个域名，无需处理，也未曾抓取。

