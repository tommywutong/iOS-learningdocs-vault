# 中文 iOS 底层技术内容源 · 甄别报告

调研日期：2026-07-26
调研方式：逐站实际访问（首页/归档页/sitemap/RSS 探测）+ GitHub API 元数据 + 抽样读全文验证"一手/二手"
样本请求数：约 120 次（含 HTTP HEAD 探测与 GitHub API），已控制在预算内

**本报告的核心筛选规则（先说结论）**

> 中文 iOS 底层文章的第一杀手不是抄袭，是**不标源码版本号**。
> 凡是贴 `struct objc_class` / `isa_t` 位域 / `CFRunLoop` 结构体却不说"这是 objc4-XXX / CF-XXXX"的文章，一律降级。
> 归档时必须同时归档 **RetVal/objc-runtime**（可编译可断点的 objc4）作为事实基准，否则读到的每一篇 runtime 文章都无法验证。

---

## 1. 总表

### 1.1 具名个人博客

| 来源 | URL | 作者 | 最近更新 | 成系列 | 一手/二手 | GitHub 源仓库 | RSS / sitemap | 可抓性 | 优先级 |
|---|---|---|---|---|---|---|---|---|---|
| Draveness / 冰霜之外 | https://draven.co （draveness.me 301→） | Draveness | 2022-03（iOS 内容止于 2017） | ✅ 极强，objc 源码 10 篇 + 每个三方库一个系列 | **一手**（自加打印跑 LLDB） | ✅ **Draveness/analyze** 8081★ | `/feed.xml` ✅ `/sitemap.xml` ✅ 534 loc | 高（但建议直接 clone） | ★★★★★ |
| 唐巧的技术博客 | https://blog.devtang.com | 唐巧 | **2026-07-23（活跃，但已转 AI/创业）** | 部分（iOS 老文 2012-2016） | 混合（早期一手，多为经验总结） | ❌ 未找到 | `/atom.xml` ✅ 288KB 全文 · `/sitemap.xml` ✅ | 高 | ★★★ |
| 南峰子…不，sunnyxx | https://blog.sunnyxx.com | sunnyxx / 孙源 | **2016-08-13（停更 10 年）** | ✅ 重识 ObjC Runtime 2 篇 + 多篇独立硬文 | **强一手**（自解析 ivar layout / 读汇编） | ⚠️ sunnyxx/blog-hexo、hexo-blog-source（0★，未验证内容） | `/atom.xml` ✅ 362KB · `/sitemap.xml` ✅ | 高 | ★★★★★ 抢救 |
| ibireme's blog | https://blog.ibireme.com | ibireme / 郭曜源 | **技术文 2016-01-16，末篇 2017-09-01（停更）** | ❌ 非连载，但每篇都是重量级 | **极强一手**（自跑 benchmark、自查 issue 推翻旧结论） | ❌ **无**（自建 WordPress） | `/feed/` ⚠️ 仅最近几篇 · `/sitemap.xml` ✅ | 中（只能爬 HTML） | ★★★★★ **最紧急** |
| 冰霜之地 Halfrost-Field | https://halfrost.com | halfrost | 仓库 **2026-07-26 活跃**；iOS 部分止于 2018 | ✅（但 iOS 只 ~10 篇） | 一手 | ✅ **halfrost/Halfrost-Field** 13210★ | ❌ index.xml 301 循环 · sitemap.xml **0 字节** | 站点差 / 仓库满分 | ★★★（iOS 部分 ★★） |
| 戴铭的博客 | https://ming1016.github.io | 戴铭 / starming | **2026-02-23（活跃）** | ✅ 多主题长文 | 一手为主，**汇总成分不低** | ✅ **ming1016/study** 3903★（StarmingBlog/） | `/atom.xml` ✅ **1.27MB 全文=全站** · sitemap 404 | 高 | ★★★★ |
| Dirtmelon | https://dirtmelon.github.io | dirtmelon | **2022-01-19（停更）** ~45 篇 | ✅ Promises 3 / IGListKit 5 / Texture / PhotoKit | 一手（源码逐类读） | ✅ **dirtmelon/dirtmelon.github.io** | `/feed.xml` ✅ · `/sitemap.xml` ✅ | 高 | ★★★★ |
| 玉令天下的博客 | https://yulingtianxia.com | 杨萧玉 | **2022-12-12（停更）** ~110 篇 | ✅ BlockHook 6 篇 / DartNative 10+ 篇 / CoreData 3 篇 | **极强一手**（写的就是自己的开源库） | ✅ **yulingtianxia/yulingtianxia.github.io** | `/atom.xml` ✅ 313KB · `/sitemap.xml` ✅ 121 loc | 高 | ★★★★★ |
| 南峰子的技术博客 | https://southpeak.github.io | 南峰子 | **2017-01-16（停更 9 年）** 86 篇 | ✅ iOS 知识小集 9 期 / UIKit 系列 | **大部分二手（翻译）** | ✅ **southpeak/southpeak.github.com** 19★ | ❌ atom.xml 404 · ❌ sitemap 404 | 中 | ★★ |
| Aha Edmond | https://looseyi.github.io | Edmond / looseyi | **2021-11-13（停更）** ~25 篇 | ✅ CocoaPods 源码 9 篇 | 一手，但**主题不对口** | ⚠️ looseyi/looseyi.github.io（未确认源码/产物） | ❌ atom.xml 404 · `/sitemap.xml` ✅ | 中 | ★★ |
| kingcos / Perspective | https://kingcos.me | kingcos | 站点 **2025-03 活跃（已转 AI）**；iOS 内容止于 2019-12 | ✅ Focus / Practice / Studying 三大系列 | **一手，且每篇标 Release Notes 版本表** | ✅ **kingcos/Perspective** 182★ 纯 markdown | ❌ feed/atom 404 · `/sitemap.xml` ✅ 27KB | 仓库满分 | ★★★★★ **性价比第一** |
| Zhongwu | https://zhongwuzw.github.io | zhongwuzw | **2020-09-24（停更）** | 部分（Flutter/RN 内部原理） | 一手 | ✅ zhongwuzw/zhongwuzw.github.io | ⚠️ atom.xml **200 但 0 字节（坏）** · sitemap 404 | 低 | ★★ |

### 1.2 大厂 / 组织

| 来源 | URL | 最近更新 | 成系列 | 一手/二手 | 仓库 | 可抓性 | 优先级 |
|---|---|---|---|---|---|---|---|
| 美团技术团队 | https://tech.meituan.com （/tags/ios.html） | 站点活跃 | ✅ 启动/渲染/监控/架构四条线 | 一手 | ❌ | ★★★★★ 静态 Hexo + archives | ★★★★★（⚠️ 正文本次未能直连验证） |
| 微信终端开发团队（腾讯云镜像） | https://cloud.tencent.com/developer/column/1362 | **111 篇** | ✅ Matrix 内存/卡顿/耗电三部曲 | **教科书级一手** | — | ★★★★ 正文实测可抓 | ★★★★★ |
| Tencent/matrix wiki | `git clone https://github.com/Tencent/matrix.wiki.git` | 本体 push 2024-07-23 | ✅ 中文原理文档 5+ 篇 | 一手 | ✅ 12028★ | ★★★★★ git clone | ★★★★★ |
| 字节跳动技术团队 | https://juejin.cn/team/6930545192860647431/posts | 活跃 | 无 iOS 底层系列 | — | ❌ | ★★ | ★★ |
| 滴滴 DoraemonKit | https://github.com/didi/DoraemonKit | 2025-08-12 | 工具文档 | 一手 | ✅ 20412★ | ★★★★★ | ★★★ |
| 阿里/淘系 | tech.taobao.org · blog.csdn.net/Taobaojishu | — | **无 iOS 底层系列** | — | ❌ | ★★ | ★ |
| B站/快手/网易 | 分散于专栏+公众号 | — | **无 iOS 底层系列** | — | ❌ | ★★ | ★ |

### 1.3 开源笔记 / 周报 / 译本

| 仓库 | ★ | 最后 push | 性质 | 优先级 |
|---|---|---|---|---|
| **Draveness/analyze** (= iOS-Source-Code-Analyze) | 8081 | 2021-11-14 | objc + 三方库源码分析全集 | ★★★★★ |
| **SwiftOldDriver/iOS-Weekly**（老司机周报） | 4992 | **2026-07-19 活跃** | 带人工点评的索引，Reports/2018…2026 | ★★★★★ |
| **RetVal/objc-runtime** | 1830 | 2024-03-16 | 可编译可断点的 objc4（**事实基准工具**） | ★★★★★ |
| **kingcos/Perspective** | 182 | 2019-12-01 | 主题最对口的纯 markdown 笔记 | ★★★★★ |
| **SwiftGGTeam/the-swift-programming-language-in-chinese** | 21178 | **2026-04-08 活跃** | Apple 官方 Swift 书中文版，**中文术语事实标准** | ★★★★★ |
| **SwiftGGTeam/swiftgg-trans-plugin**（Twine） | 186 | 2024-12-19 | Apple 官方文档双语对照插件（**用户项目的同类上游**） | ★★★★★ |
| **objccn/articles** | 2094 | **2021-11-02 停更** | objc.io 期刊完整中文版 | ★★★★★ 抢救 |
| **Tencent/matrix (+wiki)** | 12028 | 2024-07-23 | 微信 APM 源码 + 中文原理 | ★★★★★ |
| **Desgard/iOS-Source-Probe** | 915 | **2018-08-08 停更** | Runtime / **mach-o / fishhook** / Foundation / UIKit | ★★★☆ |
| **ming1016/study** | 3903 | 2026-02-23 | 博客源码 + 自写解释器实验 | ★★★★ |
| **ming1016/SwiftPamphletApp** | 2567 | 2025-08-16 | "戴铭的小册子"，活的知识手册 | ★★★★ |
| **zhangferry/iOSWeeklyLearning**（摸鱼周报） | 359 | **2023-07-24 停更**，99 期 | 2021-2023 中文 iOS 生态切片 | ★★★★ 抢救 |
| **Tim9Liu9/TimLiu-iOS** | 11684 | 2025-12-29 | 三方库/博客**索引**（不是内容） | ★★★ 当种子清单 |
| **didi/DoraemonKit** | 20412 | 2025-08-12 | 工具 + 中文文档 | ★★★ |
| **xitu/gold-miner**（掘金翻译计划） | 34327 | **2024-04-17 基本停更** | 海量译文，**质量方差大** | ★★ 按需单篇 |
| **ChenYilong/iOSInterviewQuestions** | 9533 | 2026-01-27 | 面试题祖师爷，**答案陈旧** | ⚠️ 见排除清单 |
| SunshineBrother/JHBlog | 1414 | 2021-07-29 | 个人晋级笔记，汇总性质 | ★★ |
| LeoMobileDeveloper/Blogs | 1601 | 2022-08-19 | 个人心得，跨技术栈 | ★★ |
| ChenYilong/ParseSourceCodeStudy | 2851 | 2019-09-16 | 分析已停服的 Facebook Parse | ✗ 价值消失 |

---

## 2. 强烈推荐归档（详细说明）

### 2.1 Draveness/analyze — 中文 iOS 源码分析的天花板 ★★★★★

- **站点**：draveness.me **301 重定向到 draven.co**（归档要用 draven.co，老域名只是跳转）。站点在线，最近一篇 2022-03-19，但**内容早已完全转向 Go / Kubernetes / 分布式系统**。iOS 部分是 2015-2017 写的，**至今全部在线可访问**（实测 `/isa/` `/message/` `/rr/` `/autoreleasepool/` 均 200）。
- **最有价值的系列**：`contents/objc/` 10 篇，是中文圈唯一成体系读完 objc4 的系列：
  - 从 NSObject 的初始化了解 isa
  - 从源代码看 ObjC 中消息的发送
  - 深入解析 ObjC 中方法的结构
  - 你真的了解 load 方法么？ / 懒惰的 initialize 方法
  - 黑箱中的 retain 和 release / 自动释放池的前世今生
  - 关联对象 AssociatedObject 完全解析 / 对象是如何初始化的 / 上古时代 ObjC 中哈希表的实现
- 另有完整的三方库系列（**每一个都是用户学习计划里的主题**）：`AFNetworking`(5) `SDWebImage` `AsyncDisplayKit`(4，含《从 Auto Layout 的布局算法谈性能》《提升 iOS 界面的渲染性能》《预加载与智能预加载》) `FBRetainCycleDetector`(retain-cycle 1/2/3) `fishhook` `Masonry` `ReactiveObjC` `BlocksKit`(2) `libextobjc` `KVOController` `ProtocolKit` `IQKeyboardManager` `MBProgressHUD` `DKNightVersion` `CocoaPods` `architecture`
- **一手判断依据（我读了 `/isa/` 全文）**：
  1. 开篇明确声明实验环境："因为 ObjC 的 runtime 只能在 Mac OS 下才能编译，所以文章中的代码都是在 Mac OS，也就是 `x86_64` 架构下运行的，对于在 arm64 中运行的代码会特别说明。"——**会主动声明架构差异的中文作者极少**。
  2. 他在 `_class_createInstanceFromZone` 里**自己加打印**，得到一批类指针的十六进制值，据此论证"所有类指针十六进制地址最后一位都为 8 或 0"，从而验证 `isa.shiftcls = (uintptr_t)cls >> 3` 的合法性。
  3. 自己把 `NSObject` 实例的 isa 打成 64 位二进制串（`0000000001011101100000000000000100000000001110101110000011111001`），逐位标出 `shiftcls`，跟 `[NSObject class] >> 3` 比对。
  → 这是自己跑实验 + 自己读源码，不是转述。
- **⚠️ 版本过时（必须在归档元数据里标注）**：文中 `isa_t` 的第一个位域叫 **`indexed`**，这是 **objc4-680（2016）** 的字段名；现行 objc4 已改名 **`nonpointer`**，`extra_rc` 位宽、`has_sidetable_rc` 语义、arm64e 的指针认证（PAC）都已变化。**归档时打标签 `objc4-680 时代 / 需与 RetVal/objc-runtime 对照`。**
- **RSS**：https://draven.co/feed.xml **sitemap**：https://draven.co/sitemap.xml（534 条 loc）
- **GitHub 源仓库（重点）**：**`Draveness/analyze`** — 8081★，最后 push 2021-11-14，103MB。`iOS-Source-Code-Analyze` 是同一个 repo 的别名（他文章里自己写的"关注仓库：iOS-Source-Code-Analyze"就指向它）。`contents/` 下按库分目录、纯 Markdown、含 `images/`。
  → **归档方式：直接 `git clone`，不要爬网页。** 网页版图片走 `img.draven.co` CDN 且 markdown 里的图片 URL 有拼接 bug（实测正文里出现 `![NSObject](https://img.draven.co/... + NSObject Copy + @Draveness.png)` 这种坏链接），仓库里的原始 markdown 更干净。

### 2.2 ibireme（郭曜源）— 最紧急，因为无源仓库且已停更 10 年 ★★★★★

- **站点**：https://blog.ibireme.com 在线（WordPress）。**技术文最后一篇 2016-01-16，全站最后一篇 2017-09-01（一篇日本旅游日记）。停更 9-10 年。**
- **文章量级**：技术文约 15-20 篇，但**篇均价值是本报告最高的**。
- **最有价值的（按用户学习计划排序）**：
  1. **《深入理解 RunLoop》** 2015-05-18 https://blog.ibireme.com/2015/05/18/runloop/ — 中文 RunLoop 的唯一权威源，从 CFRunLoop 源码入手，讲清 mode / source / timer / observer，以及 Apple 如何用 RunLoop 实现自动释放池、延迟回调、触摸事件、屏幕刷新。**用户学 RunLoop 只需要这一篇 + Apple 文档。**
  2. **《iOS 保持界面流畅的技巧》** 2015-11-12 https://blog.ibireme.com/2015/11/12/smooth_user_interfaces_for_ios/ — 屏幕成像/CPU-GPU 分工/离屏渲染/异步绘制/预排版，附一个开源微博列表实现。
  3. **《移动端图片格式调研》** 2015-11-02 https://blog.ibireme.com/2015/11/02/mobile_image_benchmark/
  4. **《不再安全的 OSSpinLock》** 2016-01-16 https://blog.ibireme.com/2016/01/16/spinlock_is_unsafe_in_ios/
  5. 《YYCache 设计思路》2015-10-26、《iOS JSON 模型转换库评测》2015-10-23、《iOS 处理图片的一些小 Tip》2015-11-02
- **一手判断依据**：
  - 《移动端图片格式调研》全篇是**他自己跑的 benchmark 数据表**（不同格式的编解码耗时、体积、内存）。
  - 《不再安全的 OSSpinLock》的缘起写在正文第一句："昨天有位开发者在 Github 上给我提了一个 issue（YYModel#43），里面指出 OSSpinLock 在新版 iOS 中已经不能再保证安全了……我仔细查了一下相关资料，确认了这个让人不爽的 bug。"——**这是自己收到真实 bug 报告后追查并纠正结论**。
  - 《iOS 处理图片的一些小 Tip》里给的是可验证的实现细节链（`CGImageSourceCreateWithData` 的 `ShouldCache` 在 64 位设备默认开启 / `NSKeyedArchiver` 内部调 `UIImagePNGRepresentation` 所以最贵 / 判断图片格式的函数直接指向 `YYImageCoder.m#L1066-L1141` 自己的代码行号）。
  → 他是 YYKit/YYText/YYCache/YYImage/YYModel/YYAsyncLayer 的作者，文章就是这些库的设计文档。**一手性无可争议。**
- **元层面的价值**：《不再安全的 OSSpinLock》本身就是"纠正过时结论"的范本。用户学 GCD/锁时应该先读它，然后就有免疫力去识别那些仍在推荐 OSSpinLock 的旧文。
- **RSS**：https://blog.ibireme.com/feed/（8.9KB，⚠️ **只含最近几篇，不是全站**）**sitemap**：https://blog.ibireme.com/sitemap.xml（1.8KB，应为 sitemap index）
- **GitHub 源仓库：没有。** 自建 WordPress，无 markdown 源。
  → **这是本报告里最需要立刻主动镜像的来源**：停更 10 年 + 无源仓库 + 域名续费全凭作者个人意愿 + RSS 不全量。**建议按 sitemap 逐页抓 HTML + 转 markdown + 存图片，尽快做。**
- **⚠️ 部分结论需标注时代**：《iOS 保持界面流畅的技巧》里的手动预排版、`YYAsyncLayer` 异步绘制方案，在 iOS 13+ 的 `UICollectionViewCompositionalLayout`、SwiftUI、ProMotion 可变刷新率下部分已被官方方案覆盖。**原理仍然正确，具体建议要打折。**

### 2.3 kingcos/Perspective — 性价比第一 ★★★★★

- **站点**：https://kingcos.me 在线且活跃（最近 2025-03），但**内容已转向 AI**（xiaozhi-esp32 服务端/端侧源码分析、OpenManus 源码分析）。iOS 内容全部产出于 2017-2019。
- **iOS 内容全在 `kingcos/Perspective` 仓库**（182★，最后 push 2019-12-01，纯 Markdown，按目录分类）。**这份目录几乎就是用户学习计划的镜像**：
  - `Posts/Focus/`：`NSObject_in_iOS` `Objects_in_Obj-C` `Category_in_Obj-C` `KVC_in_iOS` `KVO_in_iOS` **`dyld_shared_cache`** **`iOS_App_Start_up`** **`Link_Map_File_in_Xcode`** `UIViewController_Life_Cycle` `AFNetworking` `Swift_Selector` `Swift_Properties` `Swift_Autoclosure` `alloc_init_vs_new_in_Obj-C`
  - `Posts/Practice/`：**`+load_in_iOS`** **`+initialize_in_iOS`** **`Locks_in_iOS`** **`Multithread_Techs_in_iOS`** `Weakly_Collections` `ivar_Access_Control_in_Obj-C` `NSCoding_in_iOS` `Type_Introspection_and_Reflection` `CI_Practice_in_iOS`
  - `Posts/Studying/`：**`MacOSX_and_iOS_Internals`**（读《Mac OS X and iOS Internals》的笔记 —— 这本书正是 Mach-O/dyld/内核那一块的圣经）、`ICS_15-213`（CSAPP 课）、`Effective_Objective-C_2.0`、`Programming_from_the_Ground_Up`、`WWDC`
  - `Posts/Translation/`：**`About_the_App_Launch_Sequence`** **`URL_Loading_System`** `Uncovering_SourceKit` `Designating_Nullability_in_Objective-C_APIs` `Performing_One-Time_Setup_for_Your_App` → **这几篇是 Apple 官方文档/技术文的中文翻译，对用户自己的翻译项目有直接的术语参考价值。**
- **一手判断依据（也是最强的可信度信号）**：他每篇开头都有一张 **`Release Notes` 表格**，列 `Date | Notes`，以及"代码版本 / 主要语言 / 主要框架"。我在他 2025 年的 AI 文章里也看到同样格式（"代码版本：release 0.1.6，主要语言：Python"）。**在中文技术博客里，主动标注被分析代码的版本号是极少数行为**，恰好解决了本报告开篇提出的第一杀手问题。
- **RSS**：feed.xml / atom.xml 均 404；**sitemap**：https://kingcos.me/sitemap.xml ✅（27KB）
- **归档方式**：`git clone https://github.com/kingcos/Perspective`（很小，纯 markdown）。他现在的博客产物在 `kingcos/kingcos.github.io`（push 2026-03，含 `/perspective` 目录），但 markdown 源就在 Perspective 仓库里。

### 2.4 yulingtianxia（杨萧玉）— Method Swizzling + 启动优化的一手源 ★★★★★

- **站点**：https://yulingtianxia.com 在线，**最后一篇 2022-12-12（停更 3.5 年）**。sitemap 121 条 loc，约 110 篇文章（2014 至今）。
- **最有价值的**：
  1. **《Objective-C Method Swizzling》** 2017-04-17 https://yulingtianxia.com/blog/2017/04/17/Objective-C-Method-Swizzling/ — 中文圈关于 swizzling 各种陷阱（继承链、`+load` 时机、`_cmd`、多次交换、`class_addMethod` 兜底）最严谨的一篇。
  2. **《App Order Files》** 2019-09-01 https://yulingtianxia.com/blog/2019/09/01/App-Order-Files/ — **二进制重排 / order file / 启动优化的中文一手源，比后来疯传的抖音那批转述文更早、更硬。**（见排除清单第 8 条）
  3. **BlockHook 六部曲**（2019-2020）：with-Struct / with-Private-Data / with-Invocation(1,2) / with-Revocation / and-Memory-Safety
  4. 《Hook Objective-C Block with Libffi》2018-02-28、《Track Block Arguments of Objective-C Method》2018-03-31
  5. DartNative / dart_native 系列 10+ 篇（2019-2022，Flutter↔Native 互调、跨语言内存管理）
- **一手判断依据**：BlockHook 是**他本人写的开源库**，那六篇文章就是设计文档；libffi hook block 是他自己造的轮子；《BlockHook and Memory Safety》里列的三个问题（"微信项目使用 BlockHook 时的 MRC 兼容问题 / GlobalBlock 在某些场景下的 VM Protection 没有写权限 / 如何检测带有 Private Data 的 block"）是**在微信真实工程里踩出来的**。DartNative 同理，他是作者，且诚实写了《Flutter 官方终于出手了，DartNative 将何去何从?》讨论自己项目被官方方案挤压。
- **RSS**：https://yulingtianxia.com/atom.xml ✅（313KB，全文输出）**sitemap**：https://yulingtianxia.com/sitemap.xml ✅
- **GitHub 源仓库**：**`yulingtianxia/yulingtianxia.github.io`**（4★，push 2022-12-11，98MB）✅ 含 markdown 源。

### 2.5 sunnyxx（孙源）— 停更 10 年，最该抢救 ★★★★★

- **站点**：https://blog.sunnyxx.com 在线，**最后一篇 2016-08-13。停更整 10 年。** 首页 16 篇，`/archive/` 是 404（GitHub Pages 404 页），但 `atom.xml` 362KB 说明全文输出且基本覆盖全站。
- **最有价值的**：
  - **《重识 Objective-C Runtime》2 篇**（2016-08-13）：`看透 Type 与 Value` / `Smalltalk 与 C 的融合` — 这是从语言设计层面讲 runtime，视角和 Draveness 的"逐行读源码"互补。
  - **《Objective-C Class Ivar Layout 探索》**（2015-09-13）— 中文圈唯一讲清 ivar layout 的文章，直接关系到 ARC 下 strong/weak ivar 的内存布局。
  - **《ARC 对 self 的内存管理》**（2015-01-17）
  - **《优化 UITableViewCell 高度计算的那些事》**（2015-05-17）— 与 ibireme 的《保持界面流畅》一条线。
  - **《Clang Attributes 黑魔法小记》**（2016-05-14）、《巧用 Class Extension 分离接口依赖》、《2015 Objective-C 新特性》、《一个丝滑的全屏滑动返回手势》、《巧用多字符 Char 常量》、《实现一个 TODO 宏》
- **一手判断依据**：Ivar Layout 那篇是自己调 `class_getIvarLayout` 拿到字节串再手工解码；《ARC 对 self 的内存管理》是自己看汇编/objc 源码得出结论；他是 objc.io 中文版（objccn.io）的早期核心译者之一，也是 `sunnyxx/libffi-iOS`、`XXNibBridge` 的作者。**在中文 iOS 圈他是被引用方，不是引用方。**
- **RSS**：https://blog.sunnyxx.com/atom.xml ✅（362KB）**sitemap**：https://blog.sunnyxx.com/sitemap.xml ✅（7.5KB）
- **GitHub 源仓库**：⚠️ `sunnyxx/sunnyxx.github.io` **404**（用了自建域名的 Pages）；但有 `sunnyxx/blog-hexo`（0★，push 2016-09-01）和 `sunnyxx/hexo-blog-source`（0★，push 2016-04-08）两个 hexo 源码仓库。**我只读了 API 元数据，没有 clone 验证里面有没有 `source/_posts`——请实际 clone 确认。**
- **紧急度**：他本人已长期不在中文技术圈活动（GitHub 最后活动 2020），域名随时可能不续。**优先用 atom.xml 全量落地。**

### 2.6 dirtmelon — 三方库源码阅读的扎实笔记 ★★★★

- **站点**：https://dirtmelon.github.io **最后一篇 2022-01-19《iOS 工程建设》。停更。** 归档页可数出约 45 篇（2016-07 起）。
- **成系列**：Promises 三部曲（介绍 / Objective-C 实现 / Swift 实现，2021-11~12）、IGListKit 五部曲（开篇 / SectionController / Adapter / Updater&Diff / 完结篇，2020-11~2021-02）、Texture 系列（基本概念 / Layout / 开发笔记）、PhotoKit 系列（概览 / 使用 / 与 iCloud 图片）、《Web 性能权威指南》读书笔记 3 篇、《数据结构与算法之美》笔记 3 篇、《Swift 进阶》笔记 2 篇
- **命中用户学习计划的单篇**：
  - **`FBAllocationTracker`**（2021-11-02）— 查找存活 ObjC 对象，内存管理主题
  - **`Aspects`**（2020-03-07）— AOP / runtime hook
  - **`Objective-C Direct Methods`**（2021-06-22）— 少见地讲了 Clang 13 的 `__attribute__((objc_direct))`，**是本报告里最"新"的 runtime 内容**
  - `Swift 与指针`（2020-05）、`MemorySafety`（2020-09）、`Swift 与 Objective-C 互操作中的 Optional`（2020-07）、`URL-loading-system`（2019-11）
- **一手判断依据**：逐类逐方法读源码型。如 IGListKit 那篇明确写"IGListAdapter 在初始化时提供了一个 `id<IGListUpdatingDelegate> updater` 参数……"，`Objective-C Direct Methods` 直接给出 LLVM commit 链接（`llvm/llvm-project@d4e1ba3`）和对应 Xcode 版本。**引用具体 commit 是很强的一手信号。**
- **主题偏向提示**：他读的是**三方库**，不是系统底层。对 runtime/内存有帮助（Aspects/FBAllocationTracker/Direct Methods），对 RunLoop / Mach-O / dyld 帮助不大。
- **RSS**：https://dirtmelon.github.io/feed.xml ✅ **sitemap**：https://dirtmelon.github.io/sitemap.xml ✅
- **GitHub 源仓库**：`dirtmelon/dirtmelon.github.io`（0★，push 2022-01-27，7.4MB，Hugo 源码）✅

### 2.7 ming1016（戴铭）— 当地图用，不当单一权威 ★★★★

- **站点**：https://ming1016.github.io **活跃**（最近 2026-02-23《Ioser 铭（iOS开发2015-2025）》）。但 2024-2026 的内容大量偏向 SwiftUI / AI / 个人知识管理 / 动漫，技术密度下降。
- **最有价值的**：他的 iOS 底层长文集中在 2015-2021（《深入剖析 iOS 性能优化》《iOS 界面渲染流程分析》《iOS App 启动优化》《如何设计一个 iOS App 的架构》），以及 `ming1016/study` 仓库里自己写的实验项目：`OCInterpreter`（ObjC 解释器）、`LispToC`、`QuickJS`、`ArchitectureOCDemo`、`Slides`。
- **一手 vs 二手**：一手为主（他确实在滴滴/字节做过 iOS 架构，自己写解释器和 JS 引擎接入），但**写作风格是"大而全的知识整理"**——一篇文章横跨十几个主题、每个主题几段，段落间来源不总是标清。**汇总/二手成分不低。** 适合当"我该学哪些东西"的地图，不适合当某个具体结论的唯一依据。
- **RSS**：https://ming1016.github.io/atom.xml ✅ **1.27MB 全文输出 ≈ 全站**（sitemap 404，但有 atom 就够）
- **GitHub 源仓库**：`ming1016/study`（3903★，push 2026-02-23，574MB ⚠️ 很大）里的 `StarmingBlog/`（hexo 源码，含 `source/_posts`）✅；另有 `ming1016/SwiftPamphletApp`（2567★，"戴铭的小册子"，SwiftUI+SwiftData 写的活知识手册）值得单独归档。

### 2.8 唐巧 blog.devtang.com — 只抢救老文 ★★★

- **站点非常活跃**（2026-07-23），但**已经不是 iOS 技术博客了**：最近 10 篇是《梁文锋四小时投资人会议有感》《黑洞足迹-AI 时代的一人 App》《用 CLIProxyAPI 把 Codex 变成 OpenAI 兼容 API》《如何写一篇 AI 味很重的文章》《北京四环骑行一日游》……
- **值得的是 2012-2016 的 iOS 老文**（《谈 Objective-C Block 的实现》《iOS 开发中的 Runtime》《iOS 开发中的 KVO》《如何提高 iOS 开发效率》等）。这些在他早期是相当有影响力的入门-进阶桥梁。
- **一手/二手**：混合。《谈 Objective-C Block 的实现》是自己 `clang -rewrite-objc` 出来逐段分析，一手；但多数是经验总结/工程实践科普，不是源码级。
- **RSS**：https://blog.devtang.com/atom.xml ✅ **288KB 全文输出** **sitemap**：https://blog.devtang.com/sitemap.xml ✅（194KB）
- **GitHub 源仓库**：**未找到**（`tangqiao/blog.devtang.com` 404）。
- **归档策略**：用 atom.xml + sitemap 全量拿一次，然后**只保留 2012-2016 的 iOS 技术文**，其余（AI/创业/骑行）不入库。不需要持续订阅。

---

## 3. 大厂技术博客

### 3.1 微信 / 腾讯 — 本次调研最大的发现 ★★★★★

**关键结论：WeMobileDev 公众号的文章在腾讯云开发者社区有官方镜像专栏，公众号不可抓的问题在这里被绕开了。**

- **镜像专栏**：**https://cloud.tencent.com/developer/column/1362 「微信终端开发团队的专栏」**
  - 实测：**111 篇文章**，55.8 万阅读，524 订阅
  - 我实测抓取了其中一篇的**完整正文**（见下），确认 `cloud.tencent.com/developer/article/{id}` 是可稳定抓取的静态正文页
- **Matrix 三部曲（最有价值，正是用户"UIKit 渲染与性能 / 内存管理"主题的工业级材料）**：
  1. **《Matrix-iOS 内存监控》** https://cloud.tencent.com/developer/article/1427932 ✅ 已实测全文可抓
  2. **《Matrix-iOS 卡顿监控》** https://cloud.tencent.com/developer/article/1427933
  3. **《Matrix-iOS 耗电监控》** https://cloud.tencent.com/developer/article/1483621
- **一手判断依据（我读了《内存监控》全文，这是教科书级证据）**：
  - 发现路径是真实的偶然："16 年 9 月底为了解决 iOS10 nano crash，研究了 libmalloc 源码，**无意中发现**这几个接口"（`malloc_logger` / `__syscall_logger` 函数指针）。
  - 有自己的工程权衡与理由：放弃 sqlite 改用**伸展树（Splay Tree）**，理由是"大部分情况下内存申请很快又被释放，如 autoreleased 对象、临时变量；而 OC 对象申请内存后紧接着会更新它所属 Category"——**用局部性原理反推数据结构选择**。
  - 有自己测的数字：微信启动 10 秒内创建 80 万对象、释放 50 万；backtrace 平均栈长 35，**后缀压缩后降到 5 以内，压缩率 42%**；iPhone6Plus 上 CPU 占用 <13%，内存 20MB（mmap）。
  - 有线上业务指标：**FOOM 率 2017 年初 3% → 0.67%，前台卡死率 0.6% → 0.3%，解决 30 多处内存问题。**
  - **诚实列出四类误判**（`ApplicationState` 不准 / 群控类外挂 / CrashReport 组件自身 crash 未回调 / 前台卡死被 watchdog `0x8badf00d` 强杀），并说明"这方法只能减少误判概率，并不能彻底解决"。**愿意写自己方案的局限，是一手工程文最可靠的指纹。**
  - 还给出了绕过私有 API 的降级方案（改 `malloc_default_zone` 返回的 `malloc_zone_t` 函数指针 / 虚拟内存只能靠 fishhook），说明作者真的踩过审核。
- **Tencent/matrix GitHub wiki — 可以直接 git clone（重要）**：
  ```
  git clone https://github.com/Tencent/matrix.wiki.git
  ```
  实测 clone 成功，中文页面包括：
  `Matrix-for-iOS-macOS-卡顿监控原理.md` · `Matrix-for-iOS-macOS-异步堆栈回溯.md` · `Matrix-for-iOS-macOS-耗电监控原理.md` · `Matrix-for-iOS-macOS-数据格式说明.md` · `Matrix-for-iOS-macOS-配置说明.md` · `Matrix-for-iOS-macOS.md` · `About macOS & iOS symbol.md` · `Matrix-常见问题.md`
- **本体仓库**：`Tencent/matrix` 12028★，**最后 push 2024-07-23（⚠️ 已近两年未更新）**。
- **可抓性**：cloud.tencent.com ★★★★（有 SPA 外壳但正文可抓）；matrix.wiki ★★★★★（git）；mp.weixin.qq.com ★（见排除清单）

### 3.2 美团技术团队 tech.meituan.com ★★★★★（⚠️ 正文未验证）

- **⚠️ 重要声明：本次调研无法直连 tech.meituan.com。** curl、两个不同的抓取工具、WebFetch 全部失败（TLS handshake timeout / `Socket is closed` / 返回 0 字节），重试多次。判断是**本环境网络问题，不是站点下线**（搜索引擎索引正常、URL 结构完好）。**下面的标题/日期/URL 来自搜索结果元数据，正文我没读过，请在能直连的网络下复核。**
- **为什么它是国内大厂里最值得抓的**：静态 Hexo 站、永久链接格式 `/{YYYY}/{MM}/{DD}/{slug}.html`、有标签页和全站归档、无登录墙。
  - iOS 入口：https://tech.meituan.com/tags/ios.html
  - 相关标签：`/tags/客户端.html`、`/tags/性能优化.html`
  - 全站归档：https://tech.meituan.com/archives/
- **最有价值的（iOS 底层 / 性能向）**：
  1. **《美团外卖 iOS App 冷启动治理》** 2018-12-06 https://tech.meituan.com/2018/12/06/waimai-ios-optimizing-startup.html — 进程创建 / pre-main / dyld / `+load` 的中文经典启动优化文，正对用户的"Mach-O/dyld/启动优化"主题
  2. **《美团开源 Graver 框架：用"雕刻"诠释 iOS 端 UI 界面的高效渲染》** 2018-12-20 https://tech.meituan.com/2018/12/20/waimai-graver.html — 全程异步化的 UI 渲染，与 ibireme《保持界面流畅》、Draveness 的 ASDK 系列构成一条完整线
  3. **《移动端性能监控方案 Hertz》** 2016-12-19 https://tech.meituan.com/2016/12/19/hertz.html — FPS / CPU / 内存 / 卡顿 / 页面加载 / 网络流量全链路
  4. 《美团外卖终端容器无关化研发框架》 2021-11-11 https://tech.meituan.com/2021/11/11/meituan-waimai-containerless-framework.html
  5. 《境外业务性能优化实践》 2018-01-19
- **成系列程度**：不是连载，但同一标签下能自然凑出"启动 / 渲染 / 监控 / 架构"四条线。
- **时代提示**：核心几篇是 2016-2018，早于 iOS 15 的 dyld4、早于 `DYLD_PRINT_STATISTICS` 被 `os_signpost` 取代、早于 Xcode 的 App Launch template。**原理有效，工具链和数字要打折。**

### 3.3 字节跳动 / 抖音 ★★（无独立站，且最有名的贡献被二手淹没）

- **没有独立技术站。** 官方出口：
  - 掘金团队号 **https://juejin.cn/team/6930545192860647431/posts（字节跳动技术团队）**
  - 公众号"字节跳动技术团队"
  - 零散知乎长文，如《字节跳动现象级 App 十年成长史，移动端基础建设与组织演进之路》https://zhuanlan.zhihu.com/p/568519376（InfoQ《卓越技术团队访谈录》系列，讲移动端基建与组织演进，可读性好但偏管理视角）
- **⚠️ 二进制重排的溯源问题（重要）**：抖音 iOS 团队最广为人知的技术贡献是**二进制重排（Clang 插桩 `-fsanitize-coverage=func,trace-pc-guard` + order file）**，但**我无法定位到一个稳定的官方原文 URL**。现在能搜到的全是二手转述：CSDN、`juejin.cn/post/7004450888681013256`、`cloud.tencent.com/developer/article/1814588`、`cloud.tencent.com/developer/article/1894414`、InfoQ 转载、以及若干个人博客。
  → **这是"高价值原创被二手淹没"的典型案例。**
  → **对策：用杨萧玉《App Order Files》（2019-09-01，yulingtianxia.com）作为该主题的一手源**——时间更早、有明确作者、有稳定 URL、有 GitHub 源仓库。
- **可抓性**：掘金团队号可抓但需处理分页和反爬；公众号不可靠。**不建议为字节建抓取流水线。**

### 3.4 滴滴 ★★★

- 主要产出是工具：**`didi/DoraemonKit`**（20412★，push 2025-08-12），仓库内有较完整的中文文档（性能检测、内存泄漏、卡顿、日志、UI 走查）。
- 技术文散落在公众号"滴滴技术"，无稳定镜像。
- 间接产出：sunnyxx 曾任职滴滴，其博客可视为该体系的一部分。
- **归档方式**：只 clone 仓库文档，不追公众号。

### 3.5 阿里 / 淘系 ★

- 官方出口**分散且没有一个干净的静态站**：`tech.taobao.org`（大淘宝技术）、CSDN 官号 `blog.csdn.net/Taobaojishu`、知乎专栏、掘金"淘系技术"、`developer.aliyun.com`。
- **iOS 底层向的成系列内容：没找到。** 阿里的公开输出重心是 Web/前端/中台/AI/音视频。iOS 侧的经典材料（手淘客户端架构演进、Weex、《iOS 高级调试 & 逆向》相关）多以分享 PPT 或已失效旧文形式存在。
- 阿里对中文 iOS 底层的真实贡献主要在**书**（《Objective-C 高级编程》《iOS 高级调试与逆向工程》的引进/翻译）和开源库文档，不在博客。
- **结论：不建议投入。**

### 3.6 B站 / 快手 / 网易 ★

- 都**没有稳定的独立 iOS 技术站**：B站在 `bilibili.com/read` 专栏 + 公众号"哔哩哔哩技术"；快手在掘金"快手大前端"；网易在网易数帆/网易游戏学院。
- **iOS 底层成系列内容：均未找到。** 三家公开内容以音视频、直播、Web、大数据、游戏引擎为主。
- **结论：不值得建抓取流水线，遇到具体好文单篇快照即可。**

### 3.7 大厂总判断

> **只有两家值得建立稳定抓取：美团（静态站 + 永久链接）和微信（腾讯云镜像专栏 + matrix.wiki 可 git clone）。**
> 其余大厂按"遇到好文单篇快照"处理，不建订阅、不建爬虫。

---

## 4. 开源笔记仓库 / 周报 / 译本项目

### 4.1 必装的"事实基准"工具：RetVal/objc-runtime ★★★★★

- `RetVal/objc-runtime` — 1830★，**push 2024-03-16（维护中）**，"A debuggable objc runtime"。
- 这不是文章，但**它是本报告里唯一能让用户自己判断"某篇中文 runtime 文章是否过时"的东西**：可编译、可下断点、可改 `isa_t` 位域打印。
- **强烈建议连同 Draveness/analyze 一起归档，并在归档索引里写明"读 Draveness/sunnyxx/kingcos 的 runtime 文章时对照此仓库"。** 补充 `opensource.apple.com` 上的 objc4 各版本 tar 包做历史对照。

### 4.2 成体系的中文 iOS 开源笔记仓库

| 仓库 | 质量判断 |
|---|---|
| **Draveness/analyze** 8081★ / 2021-11 | **值得，最高优先**。见 §2.1。纯 markdown，`contents/{objc,fishhook,AFNetworking,SDWebImage,AsyncDisplayKit,FBRetainCycleDetector,Masonry,ReactiveObjC,BlocksKit,libextobjc,KVOController,ProtocolKit,IQKeyboardManager,MBProgressHUD,DKNightVersion,CocoaPods,architecture,Blog,Database,Redis,Ruby,Rails,rack}` |
| **Desgard/iOS-Source-Probe** 915★ / **2018-08 停更** | **值得，量小读得完**。GitBook 结构（`book.json` + `SUMMARY.md`）。目录：`Objective-C/{Foundation, Runtime, SDWebImage, UIKit}`、**`C/{fishhook, mach-o}`**、`Swift/Swift Probe - Optional.md`。**`C/mach-o` 和 `C/fishhook` 两块正中用户的"Mach-O/dyld"主题**，中文圈讲 Mach-O 的成体系内容很少。⚠️ 停更 8 年，Swift 部分只有 1 篇。 |
| **kingcos/Perspective** 182★ / 2019-12 | **值得，性价比第一**。见 §2.3。 |
| **ming1016/study** 3903★ / 2026-02 | **值得**（`StarmingBlog/` 是博客源；`OCInterpreter`/`LispToC`/`QuickJS` 是他自己的实验项目）。⚠️ 574MB，建议 `--depth 1` 或只取 `StarmingBlog/source/_posts`。 |
| **ming1016/SwiftPamphletApp** 2567★ / 2025-08 | **值得**。"戴铭的小册子"，SwiftUI + SwiftData + Swift Concurrency 写的 macOS 应用，内容是活的 Swift 知识手册。 |
| **Tim9Liu9/TimLiu-iOS** 11684★ / 2025-12 | **只当种子清单**。它是"iOS 开发常用三方库、插件、知名博客等等"的**索引**，本身没有内容。用它去发现我这份报告没覆盖到的源，别当学习材料。 |
| SunshineBrother/JHBlog 1414★ / 2021-07 | **不推荐**。"我的初级到中级的晋级之路"，汇总性质强，内容与 CSDN 上流传的底层原理笔记高度同质，来源标注不清。 |
| LeoMobileDeveloper/Blogs 1601★ / 2022-08 | **可选**。个人心得，跨 iOS/Swift/RN/Python，深度中等，不成体系。 |
| ChenYilong/iOSInterviewQuestions 9533★ / 2026-01 | ⚠️ **谨慎，见排除清单第 9 条。** |
| ChenYilong/ParseSourceCodeStudy 2851★ / 2019-09 | ✗ 分析的是**已停止服务的 Facebook Parse**，价值已归零。 |

### 4.3 周报 / Newsletter（本身就是索引，归档价值高）

- **老司机技术 iOS 周报 · `SwiftOldDriver/iOS-Weekly`** — 4992★，**最后 push 2026-07-19（本周还在更新）**，106MB
  - 仓库结构：`Reports/{2018,2019,2020,2021,2022,2023,2024,2025,2026}/`（9 个年份目录）+ `Posts/` + `Contributors/` + `docs/` + `Report template.md` + `scripts/`
  - **这是本报告里最推荐的"持续输入源"**：每期都有主题分类（文章 / 工具 / 代码 / 内容推荐）+ **人工点评**。归档它 = 免费拿到一份跨 8 年、持续更新、带评注的中文+英文 iOS 优质内容白名单。
  - **建议：把它设成后续发现新源的主输入，每期扫一遍中文条目，只把有一手信号的加入归档。**
- **iOS 摸鱼周报 · `zhangferry/iOSWeeklyLearning`** — 359★，**最后 push 2023-07-24（停更）**，出到 **第 99 期**（`WeeklyLearning/iOSWeeklyLearning_99.md`）
  - 仓库还有 `Articles/`、`Interview/`、`Employment/`、`CategorySummary/`（按主题的汇总）、`Resources/`
  - **停更但值得抢救**：99 期是 2021-2023 中文 iOS 生态的完整切片，`CategorySummary/` 尤其省事。
- **播客**：老司机团队的播客内容主要在小宇宙 / Apple Podcasts，**没有稳定文本稿**。归档投入产出比低，**不建议做**（周报已经覆盖了同一批人的内容筛选）。

### 4.4 中文译本项目 — 对用户自己的 Apple 文档翻译项目直接有用 ★★★★★

这一节请用户特别注意：**不要重新发明术语表。**

1. **`SwiftGGTeam/the-swift-programming-language-in-chinese`** — **21178★，最后 push 2026-04-08，活跃维护**
   - Apple 官方《The Swift Programming Language》的中文版。
   - **它是中文 Apple 文档翻译的事实标准术语库。** 用户的翻译项目应该直接对齐它的译法（如 optional / closure / protocol / associated type / actor / existential 等核心词的中译），否则会和整个中文社区的用词割裂。
2. **`SwiftGGTeam/swiftgg-trans-plugin`（Twine by SwiftGG）** — 186★，push 2024-12-19
   - 官方描述："a browser extension that simplifies learning and understanding Apple's official documentation. It offers **bilingual translation of English content in Apple's documentation using community-provided localized content**."
   - **这几乎就是用户项目的同类/上游。** 强烈建议先读它的实现：语料是怎么组织的、怎么和 Apple 文档的 DOM/DocC 结构对齐、社区贡献的本地化内容存成什么格式。**可能直接复用它的语料。**
3. **`objccn/articles`** — 2094★，**最后 push 2021-11-02（停更）**；站点 https://objccn.io **仍 200 在线**
   - objc.io 期刊的"完整、准确、优雅的中文翻译版本"。译者阵容包括 sunnyxx、onevcat 等，是中文圈翻译质量口碑最高的项目之一。
   - **停更但必须归档**：objc.io 期刊里的 **The Runtime / Concurrency / Animations / Testing / Backchannel** 几期，至今仍是这些主题最好的中文材料。
4. **`xitu/gold-miner`（掘金翻译计划）** — 34327★，**最后 push 2024-04-17（基本停更）**
   - 体量巨大，iOS 板块有大量 raywenderlich / Swift by Sundell / objc.io 译文。
   - ⚠️ **质量方差极大**（多译者、review 松紧不一，很多是新手译者练手）。**按需单篇取用，绝不把整仓当权威，也不适合拿来对齐术语。**
5. `SwiftGGTeam/Accessibility-Programming-Guide-for-iOS`（125★，2017-07 停更）、`SwiftGGTeam/Developing-iOS-9-Apps-with-Swift`（868★，2017-04 停更）— 仅历史价值。

---

## 5. 不建议归档（及原因）

> 这一节和推荐一样重要。中文 iOS 内容的问题不是"少"，是"同一份错误被复制了一万遍"。

### 5.1 blog.csdn.net 的 iOS 底层内容（整体） ✗

- **抄袭最严重的池子。** 同一篇《iOS 底层原理 - Runtime》能在 CSDN 上找到几十个近乎逐字相同的版本，源头往往是某培训机构的课件笔记，层层转抄后作者信息完全丢失。
- **技术性危险**：大量文章直接贴 `struct objc_class` / `isa_t` 定义却**不标 objc4 版本**，读者无法判断它对应哪个系统版本。这类文章会让用户建立错误的"当前事实"认知。
- **工程性障碍**：登录墙、复制限制、正文遮挡、广告注入、后台可改文（归档快照与现状会不一致）。
- **策略**：只保留学习计划里**已点名的具体 URL**，逐条快照（HTML + 正文 markdown + 抓取日期 + 原作者声明段），并**强制打标签 `二手 / 待核对`**。不做站点级爬取，不做作者级订阅。

### 5.2 jianshu.com ✗

同 5.1，且**失效率最高**（作者迁移到掘金/删号导致文章 404），平台自身在萎缩。已点名的 URL 立刻快照，之后不再新增。

### 5.3 cnblogs.com 的 iOS 内容 ✗

博客园主体是 .NET / Java 生态，iOS 内容少、旧、多为转载。用户学习计划里 cnblogs 被引 9 次，但那大概率是 MySQL/操作系统方向（配合 xiaolincoding 的 10 次）。**iOS 方向不值得。**

### 5.4 mp.weixin.qq.com（公众号）✗ —— 明确的风险提示

- **技术上几乎无法稳定抓取**：链接常带临时 token、需要 wx 环境的 UA/Referer、图片有防盗链（`referer` 校验，直链取图会 403）、大量正文是图片、有验证码墙。
- **失效即彻底消失**：公众号文章被作者/平台删除后**没有 archive.org 兜底**（Wayback 对 mp.weixin 覆盖极差）。
- **明确结论：如果某个高价值内容只存在于公众号，那它随时会消失，而且你抓不住它。**
- **对策优先级**：
  1. 先找腾讯云开发者社区的官方镜像专栏（微信团队的就在 `column/1362`，111 篇）
  2. 找掘金团队号 / 知乎专栏 / InfoQ 转载
  3. 找作者本人博客（很多大厂工程师会同步到个人站）
  4. 实在只有公众号：**人工"打印为 PDF" + 正文手动转 markdown，立刻落地。别指望脚本，别拖。**

### 5.5 southpeak.github.io 的译文部分 ✗（区别于它的"知识小集"）

- **不是抄袭**（每篇都规范标注了原文出处与作者），但**是二手**。
- 证据：首页第一篇开头就是"本文由 Ellen Shapiro 发表于 raywenderlich，原文地址是 https://www.raywenderlich.com/138547/getting-started-with-rxswift-and-rxcocoa"；归档页里 `Getting Started With RxSwift and RxCocoa`、`JavaScriptCore Tutorial for iOS`、`Perfect smooth scrolling in UITableViews`、`Secret of Swift Performance Part 1/2`、`UIKit: UIControl`、`UIKit: UIImage` 全是英文原标题。
- **危险点**：这些英文原文（尤其 raywenderlich 的教程）在过去 9 年被更新过多轮，而这个中文快照停在 2017-01 且永不再更。**读原文的现行版本，不要读 2017 年的中文快照。**
- **例外：《iOS 知识小集》9 期（2016）和 UIKit 头文件解读系列是他的一手内容**，如果归档 southpeak，只挑这两组。

### 5.6 任何不标注源码版本号的 runtime / RunLoop / dyld 文章 ✗

**这是最实用的一条筛选规则，也是本报告最想让用户带走的东西。**

举例说明危险性有多普遍——**连本报告最推荐的文章都有这个问题**：

> Draveness《从 NSObject 的初始化了解 isa》里 `isa_t` 的第一个位域叫 **`indexed`**：
> ```c
> struct { uintptr_t indexed : 1; uintptr_t has_assoc : 1; uintptr_t has_cxx_dtor : 1;
>          uintptr_t shiftcls : 44; uintptr_t magic : 6; ... };
> ```
> 那是 **objc4-680（2016）** 的写法。现行 objc4 已改名 **`nonpointer`**，`extra_rc` 位宽变了、`has_sidetable_rc` 语义变了、arm64e 加了指针认证（PAC），`ISA_MASK` 也不同。

所以：
- **凡是给了源码版本号的 → 可信度 +1，归档时把版本号写进元数据。**
- **凡是没给版本号的 → 降级，或直接排除。**
- **凡是要读中文 runtime 文章的 → 必须同时开着 `RetVal/objc-runtime` 或 opensource.apple.com 对应版本对照。**
- 反面参考：`kingcos/Perspective` 每篇都有 `Release Notes` 版本表 —— 这就是应该被奖励的写法。

### 5.7 "OSSpinLock 性能最好"这一整类锁性能对比文 ✗ —— 结论过时且危险

- 2013-2015 年间有一张被疯狂转载的"iOS 各种锁性能对比柱状图"，结论是 `OSSpinLock` 最快。**这个结论现在是危险的**：优先级反转会导致高优先级线程忙等低优先级线程，实际会死锁；Apple 已 deprecate `OSSpinLock`。
- 纠正它的一手文就是 **ibireme《不再安全的 OSSpinLock》(2016-01-16)**。
- **规则：凡是推荐 OSSpinLock 的文章一律排除**，除非明确标注为"反例 / 历史对照"归档。
- 正确的现代替代：`os_unfair_lock` / `pthread_mutex` / `NSLock` / `dispatch_semaphore`，以及 Swift Concurrency 下的 actor。

### 5.8 抖音/字节"二进制重排"的转述文（CSDN / 掘金 / 腾讯云 / InfoQ 那一批）✗

- 具体点名（这些是搜索该主题时排在最前的）：`blog.csdn.net/nogodoss2018/article/details/125387894`、`juejin.cn/post/7004450888681013256`、`cloud.tencent.com/developer/article/1814588`、`cloud.tencent.com/developer/article/1894414`、`infoq.cn/article/p9ge3zudhlrrrfw4hvrp` 及若干个人博客镜像。
- 问题：层层转抄，Clang 插桩的编译选项（`-fsanitize-coverage=func,trace-pc-guard`）、`__sanitizer_cov_trace_pc_guard_init` 的实现细节、order file 里符号名的 C++/Swift mangling 处理、以及"重排后如何验证 page fault 真的降了"这些关键点被写错或省略。
- **替代：杨萧玉《App Order Files》(2019-09-01) https://yulingtianxia.com/blog/2019/09/01/App-Order-Files/** —— 更早、有明确作者、有稳定 URL、有 GitHub 源仓库。

### 5.9 ChenYilong/iOSInterviewQuestions ⚠️ 归档为"语料"，不是"教材"

- 9533★，最后 push 2026-01-27，仍在维护。它是中文 iOS 面试题的祖师爷，传播极广。
- **但不适合当学习材料**：
  1. 面试题体例天生鼓励"背结论"，与用户"读源码 + 自己做实验"的学习方式冲突。
  2. 相当一部分答案写于 2015-2016（weak 的 sidetable 实现、`@property` 修饰符、runtime 消息转发），未随 objc4 更新，仍是老结论。
  3. **它被无数 CSDN / 简书文章二次抄袭**，造成"错误答案的病毒式传播"——用户在别处看到的很多"标准答案"其实源头就是这里。
- **正确用法**：归档它作为"**中文 iOS 圈流行说法的语料库 / 对照组**"。当用户在 CSDN 上看到某个说法，可以来这里确认是不是同一个源头，从而识别抄袭链。**绝不当教材。**
- 同作者的 `ChenYilong/ParseSourceCodeStudy`（2851★，2019-09）分析已停服的 Facebook Parse，**价值已归零，不归档**。

### 5.10 halfrost.com 站点本身（区别于其 GitHub 仓库）✗

- 实测：`halfrost.com/index.xml` **301 重定向到自己（`/index.xml/`，循环）**；`halfrost.com/sitemap.xml` **HTTP 200 但返回 0 字节**；首页是 SPA 搜索框（抓下来只有"Enter some keywords in the search box above… We couldn't find any results"）；`/post/` **404（GitHub Pages 404 页）**。
- **爬这个站只会拿到一堆 404 和空壳。**
- **正确做法：`git clone https://github.com/halfrost/Halfrost-Field`**（13210★，仍在活跃更新）。
- 另外：`halfrost/halfrost.github.io` 的描述已被作者改成"🚫 这里是冰霜曾经写博客的地方"——**别抓那个域名。**
- 补充判断：**Halfrost-Field 的 iOS 部分对用户收益有限**。`contents/iOS/ObjC/` 只有 4 篇（`objc_runtime_isa_class` / `objc_runtime_objc_msgsend` / `objc_life` / `how_to_use_runtime`），`Block/` 2 篇，其余是 RAC、Realm、CoreData、AutoLayout Profiling、Cordova/Weex/Vue（2016-2018 的技术选型文，已过时）。仓库现在的重心是 Go / 算法 / 系统设计。

### 5.11 zhongwuzw.github.io/atom.xml ✗（坏的 feed）

- 实测：HTTP **200 但 Content-Length = 0**。这是一个坏掉的 feed，订阅它永远拿不到东西。`sitemap.xml` 404。
- 若要归档只能爬 HTML；但该站**停更于 2020-09-24**，且主题是 Flutter / React Native 内部原理（`Flutter InheritedWidget实现原理` 等），**与用户当前的 ObjC runtime / RunLoop / Mach-O 计划相关度低**。
- **建议：现在跳过。等用户学到 RN/Flutter 混合栈再回来。**（他本人是 React Native core contributor，届时价值会显现。）

### 5.12 looseyi.github.io ✗（主题不对口，不是质量问题）

- 质量没问题（源码阅读型一手，CocoaPods 9 篇成体系），但**主题偏 Ruby 工具链 / CocoaPods / Xcode 工程文件 / WWDC 笔记**，与用户的 runtime / 内存 / RunLoop / Mach-O 主题基本不重叠。唯一沾边的是《📒个人备忘 - 队列、GCD、线程基础》，而它自己标了"个人备忘"。
- 停更于 2021-11-13，`atom.xml` 404（只有 sitemap）。
- **建议：等用户学"工程化 / 组件化 / 二进制化"时再归档，现在不占位。**

---

## 6. 我没能验证的地方（请复核）

1. **tech.meituan.com 的正文 —— 最大的空白。** 本环境三种方式（curl / 两个抓取工具 / WebFetch）全部失败（TLS handshake timeout、`Socket is closed`、返回 0 字节），重试多次。§3.2 里所有标题/日期/URL 均来自搜索引擎元数据，**我没读过任何一篇美团文章的正文**。需要在能直连的网络下复核：那 4-5 篇是否还在线、正文是否完整、`/tags/ios.html` 到底有多少篇。

2. **抖音/字节"二进制重排"原始文的官方 URL** —— 反复搜索只找到二手转述，未能定位官方原文。可能只存在于公众号，或已下架。**如果用户能找到，请补上并作为该主题的一手源。**

3. **B站 / 快手 / 网易 / 阿里的 iOS 内容** —— 我是通过搜索 + 官方站点入口做的判断（"无成系列 iOS 底层内容"），**没有逐页翻完它们的专栏分页**。可能漏掉个别好文；但可以确定没有值得建流水线的"系列"。

4. **sunnyxx 的博客源仓库能否 clone 到完整 markdown** —— `sunnyxx/blog-hexo`(2016-09) 和 `sunnyxx/hexo-blog-source`(2016-04) 都是 0★，我**只读了 GitHub API 元数据，没有实际 clone**，不确定里面有没有 `source/_posts/`。请实际 clone 验证；如果没有，就只能靠 `atom.xml`（362KB 全文）。

5. **looseyi/looseyi.github.io 是 Hugo 源码还是构建产物** —— 2168KB，只看了元数据。

6. **文章级的段落抄袭比对没有做。** 我对"一手/二手"的判断依据是可观察的一手信号：是否声明实验环境/架构、是否有自己跑的 LLDB/打印输出、是否有自己测的 benchmark 数字、是否有线上业务指标、是否写的是自己的开源库、是否引用具体 commit/源码行号、是否诚实列出方案局限。每一条判断在 §2/§3 里都给了具体引文。
   **但我没有做大规模的段落级相似度比对**（那需要抓全部正文 + 与英文原文逐段对齐，请求量远超 120 次预算）。所以"一手"的准确含义是"**有明确的一手证据**"，不是"已证明不含任何转述"。

7. **RSS feed 是否全量，是用 HTTP 响应大小粗判的**，没有逐个解析 feed 计数：
   - 判为"全文/全站"：devtang `atom.xml` 288KB、sunnyxx 362KB、yulingtianxia 313KB、ming1016 **1.27MB**
   - 判为"仅最近几篇"：ibireme `/feed/` 8.9KB、dirtmelon `feed.xml` 6.3KB
   请在实际归档时验证条目数。

8. **`cloud.tencent.com/developer/column/1362` 的 111 篇里有多少是 iOS** —— 我确认了专栏存在（111 篇 / 55.8 万阅读 / 524 订阅）并**实测抓到了 1 篇 iOS 文章的完整正文**，但**没有翻完分页做 iOS / Android / 小程序 / mars 网络库的分类统计**。实际 iOS 相关篇数可能明显少于 111。

9. **`Draveness/analyze` 与网页版的内容是否完全一致** —— 我列了仓库目录和网页 sitemap，两边都覆盖了 objc 系列和三方库系列，但没有做逐篇 diff。仓库最后 push 2021-11，站点最后更新 2022-03，理论上仓库可能少最后几篇（都是 K8s 内容，与 iOS 无关）。

10. **`Tencent/matrix` 停更影响** —— 本体最后 push 2024-07-23（近两年无更新）。wiki 的中文原理文档更早。**Matrix 的方案在 iOS 17/18/26 上是否还成立（尤其 `malloc_logger` 私有接口、`__syscall_logger`、后台 CPU 采样策略）我没有验证。** 归档时按"2019-2024 的工程方案"标注。

---

## 附：给归档流水线的具体建议

**第一批（立刻做，因为会消失）**
1. `blog.ibireme.com` —— 停更 10 年 + **无 GitHub 源仓库** + RSS 不全量。按 sitemap 逐页爬 HTML + 转 markdown + 下载图片。**最紧急。**
2. `blog.sunnyxx.com` —— 停更 10 年，先试 clone `sunnyxx/blog-hexo`，失败就用 `atom.xml` 全量。
3. 学习计划里已点名的所有 CSDN / 简书 / 知乎 URL —— 逐条快照，打 `二手/待核对` 标签。
4. 任何只存在于 `mp.weixin.qq.com` 的文章 —— 人工 PDF + 手转 markdown。

**第二批（git clone，最干净）**
```
Draveness/analyze                  # 8081★  objc 源码 10 篇 + 三方库全集
kingcos/Perspective                # 182★   主题最对口，标了版本
yulingtianxia/yulingtianxia.github.io
dirtmelon/dirtmelon.github.io
Desgard/iOS-Source-Probe           # 915★   含 mach-o / fishhook
RetVal/objc-runtime                # 1830★  事实基准工具，必装
Tencent/matrix  +  Tencent/matrix.wiki.git
SwiftOldDriver/iOS-Weekly          # 持续输入源
zhangferry/iOSWeeklyLearning       # 99 期，抢救
objccn/articles                    # objc.io 中文版，抢救
SwiftGGTeam/the-swift-programming-language-in-chinese   # 术语基准
SwiftGGTeam/swiftgg-trans-plugin   # 用户项目的同类上游，先读它
ming1016/study --depth 1           # 只取 StarmingBlog/source/_posts
southpeak/southpeak.github.com     # 只挑「iOS 知识小集」9 期 + UIKit 系列
```

**第三批（RSS / sitemap 抓取）**
- `https://draven.co/sitemap.xml`（534 loc，只取 iOS 相关，见 §2.1 列表）
- `https://blog.devtang.com/atom.xml`（只留 2012-2016 iOS 老文）
- `https://ming1016.github.io/atom.xml`（1.27MB 全文）
- `https://tech.meituan.com/tags/ios.html` + `/tags/客户端.html` + `/tags/性能优化.html`（⚠️ 先解决直连）
- `https://cloud.tencent.com/developer/column/1362`（翻分页，筛出 iOS 篇）

**每条归档记录建议带的元数据**
```
url / 作者 / 发布日期 / 抓取日期 /
一手或二手（+ 依据一句话）/
被分析的源码版本（objc4-XXX / CF-XXXX / dyld-XXX，没有就写 UNVERSIONED）/
过时风险（无 / 部分 / 高）/
是否有更权威的一手替代（填 URL）
```
`UNVERSIONED` + `过时风险=高` 的条目，在阅读清单里默认折叠。
