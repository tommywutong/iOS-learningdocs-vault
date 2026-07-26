# Apple 开源 / Swift Evolution / Swift Forums 归档可行性侦察报告

侦察日期：2026-07-26
所有数字来自实际 API 调用（GitHub REST、Discourse JSON、curl HEAD/GET），未 clone 任何仓库。

---

## 0. 一页结论

| 来源 | 可归档 | 许可证 | 建议方式 | 优先级 | 压缩后体积 |
|---|---|---|---|---|---|
| apple-oss-distributions/objc4 | 是 | APSL 2.0 | 单 tag 快照（tarball） | P0 | 0.6 MB |
| apple-oss-distributions/dyld（含 `doc/`） | 是 | APSL 2.0 | 单 tag 快照 | P0 | 1.6 MB |
| swiftlang/swift-evolution | 是 | Apache-2.0 + Runtime Exception | 浅克隆整仓 + `evolution.json` | P0 | 3.3 MB |
| swiftlang/swift `docs/` | 是 | Apache-2.0 + RLE | sparse checkout 只取 `docs/` | P0 | ~2.5 MB |
| llvm/llvm-project `clang/docs/` | 是 | Apache-2.0 with LLVM Exceptions | sparse checkout 只取 `clang/docs/` | P0 | ~1.5 MB |
| libdispatch / libplatform / libpthread | 是 | Apache-2.0（前两个）/ APSL 2.0（libpthread） | 单 tag 快照 | P1 | 合计 ~1.2 MB |
| libmalloc / libclosure | 是 | APSL 2.0（file header） | 单 tag 快照 | P1 | ~0.8 MB |
| CF（已冻结在 2021） | 是 | APSL 2.0 | 单 tag 快照 CF-1153.18 | P1 | 1.0 MB |
| forums.swift.org 关键长帖 | 是 | **无开放许可，最麻烦** | `/raw/<id>` 抓纯 markdown，本地私有 | P1 | 每帖 0.1–0.4 MB |
| xnu | 是但很大 | APSL 2.0 | **不建议整仓**，只留 tag 号 + 按需线上看 | P2 | 单 tag ~20 MB |
| WebKit/Documentation | 是 | 仓库无 LICENSE 文件（风险） | 只挑 3–5 篇，注明出处链接 | P3 | ~2 MB（去掉图片） |

---

## 1. Apple 开源仓库（github.com/apple-oss-distributions）

### 1.1 是什么

`apple-oss-distributions` 组织建于 2021-10-04，是 Apple 官方 OSS 代码分发的**唯一现役渠道**。
组织实测数据：

- **公开仓库数：509**
- 全部仓库 GitHub 报告体积合计：**8 801 800 KB ≈ 8.39 GB**（含历史）
- 许可证识别分布（GitHub 自动识别，仅参考）：`none` 352 个、`NOASSERTION` 135 个、GPL-2.0 17 个、BSD-4-Clause 2、Apache-2.0 2、Vim 1
  - 注意：`none` / `NOASSERTION` **不代表没许可证**，大量是 APSL 2.0（GitHub 的 licensee 识别不了 `APPLE_LICENSE` 文件），见 §1.5。

### 1.2 与 iOS 底层学习直接相关的仓库（实测元数据）

`size` 列为 GitHub 报告的仓库体积（KB，含全部历史）；`snapshot` 为 main 分支所有 blob 之和（KB，即单版本源码解压体积）。

| 仓库 | size (KB) | main 文件数 | snapshot (KB) | tag 数 | GitHub license 字段 | 实际许可证 | 最近推送 |
|---|---|---|---|---|---|---|---|
| **objc4** | 4 761 | 408 | 3 059 | 50 | NOASSERTION | APSL 2.0（`APPLE_LICENSE`） | 2026-04-21 |
| **dyld** | 13 474 | 482 | 8 517 | 77 | NOASSERTION | APSL 2.0 | 2026-06-18 |
| **libdispatch** | 3 735 | 223 | 2 894 | 56 | Apache-2.0 | Apache-2.0（`LICENSE`, 11358 B） | 2026-04-21 |
| **libplatform** | 281 | 134 | 559 | 30 | Apache-2.0 | Apache-2.0 | 2026-06-18 |
| **libpthread** | 777 | 205 | 1 101 | 40 | none | **APSL 2.0（只在文件头，仓库根无 LICENSE 文件）** | 2026-04-21 |
| **libclosure**（Blocks runtime） | 294 | 137 | 564 | 40+ | none | APSL 2.0（文件头） | — |
| **libmalloc** | 19 525 | 218 | 2 676 | — | none | APSL 2.0（文件头） | — |
| **libunwind** | 1 318 | 98 | 703 | — | none | APSL 2.0（文件头） | — |
| **CF**（CoreFoundation） | 2 055 | 166 | 5 259 | 42 | NOASSERTION | APSL 2.0（`APPLE_LICENSE`, 20108 B） | **2021-10-06（已冻结）** |
| **Libc** | 8 241 | 1 497 | 8 716 | 81 | NOASSERTION | APSL 2.0 | 2026-06-18 |
| **xnu** | 177 648 | 6 113（tag) | **84 848** | 155 | NOASSERTION | APSL 2.0 | 2026-06-18 |
| **launchd** | 702 | — | — | — | none | APSL（老代码，10.9 时代） | — |
| **IOKitUser** | 2 664 | — | — | — | NOASSERTION | APSL 2.0 | — |
| **Security** | 81 480 | — | — | — | none | APSL 2.0 | — |
| **distribution-macOS**（清单仓） | 482 | — | — | **166** | none | 无（只有 submodule 元数据） | — |
| **distribution-iOS**（清单仓） | 70 | 4 | — | 130 | none | 无 | **已废弃，tag 只到 iPhone OS 3.x / SDK beta** |

对照用户学习计划的映射：

- ObjC runtime（`struct objc_object`、`class_data_bits_t`、`weak_register_no_lock`、`objc_autoreleasePoolPush`、`lookUpImpOrForward`）→ **objc4**
- 内存管理（malloc / nano zone / MALLOC_ 环境变量）→ **libmalloc**
- Blocks ABI 实现（`_Block_copy`、`Block_byref`）→ **libclosure**（Clang 的 `Block-ABI-Apple.rst` 是规范，libclosure 是实现，两者配对读）
- GCD / 锁（`dispatch_queue_t`、`os_unfair_lock`、信号量）→ **libdispatch** + **libplatform**（`os_unfair_lock` 实现在 libplatform）+ **libpthread**（`pthread_mutex`、`pthread_rwlock`）
- RunLoop（`__CFRunLoopRun`、mode、source0/1/timer/observer）→ **CF**（唯一来源，但已冻结）
- Mach-O / dyld / 启动优化（`start` → `prepare` → `runAllInitializersForMain` → `notifyObjCInit`）→ **dyld**
- 内核侧（Mach port、vm_map、thread、`mach_absolute_time`）→ **xnu**
- 异常 / unwind → **libunwind** + objc4 的 `objc-exception.mm`

### 1.3 版本策略（实测）

**三层结构，都值得利用：**

1. **tag = Apple 内部项目版本号**，不是 OS 版本号。格式 `<项目名>-<主版本>[.<次>.<修订>]`：
   - objc4：`objc4-951.7`、`objc4-951.1`、`objc4-950`、`objc4-940.4`、`objc4-928.3`…（共 50 个）
   - dyld：`dyld-1378`、`dyld-1376.6`、`dyld-1340`…（77 个）
   - libdispatch：`libdispatch-1542.100.32`（56 个）
   - CF：`CF-1153.18`（最新，42 个）
   - xnu：`xnu-12377.121.6`（155 个）
   - libmalloc：`libmalloc-812.100.31`
2. **main 分支 = 逐次发布的快照序列，每个 release 一个 commit**。objc4 的 main 只有 **35 个 commit**，commit message 就是版本号本身（`objc4-951.1`、`objc4-950`、`objc4-940.4`…）。**没有真实开发历史**——Apple 内部用自己的 VCS，GitHub 上只是"投放"。
   > 这个发现很重要：**"clone 全部历史"其实几乎不花额外成本**（objc4 全历史 4.7 MB，只比单快照 3.06 MB 大一点），因为历史本来就只有 35 个版本快照。
3. **`rel/*` 分支 = 长期维护线**。objc4 有 `rel/objc4-267`、`rel/objc4-371`、`rel/objc4-437`、`rel/objc4-493`、`rel/objc4-532`、`rel/objc4-709`、`rel/objc4-750`、`rel/objc4-781`、`rel/objc4-838`、`rel/objc4-906`、`rel/objc4-912`、`rel/objc4-928`、`rel/objc4-951` 共 13 条。

**OS 版本 ↔ 项目版本的映射怎么查？** → 用 `apple-oss-distributions/distribution-macOS`（482 KB，916 star，166 个 tag，从 `os-x-109` 到 `macos-265`）。它是一个**纯 submodule 清单仓**：每个 tag 上，`.gitmodules`（17 KB）列出全部项目的仓库地址，而 tree 里 `commit` 类型的条目就是该 OS 版本对应的**精确 SHA**。实测 `macos-265`（macOS 26.5）：

```
dyld        fd8d0c4d52320ebf64db34f3cb280310d905c5ae
libclosure  3668b0837f47be3cc1c404fb5e360f4ff178ca13
libdispatch 701f4d1a24ae9c6863901bbbb22624b7d1b87321
libmalloc   c49dafa25f1efe8607701ae6014a663ad2ee437f
libplatform b7ed7cf5cf7dd12b98672435db2225a860f199d8
libpthread  1f4f5265b319111142f1bf3a27d4484ef5a98314
objc4       ebfe77e64331034c867285a95d3ac205203291d5
xnu         ac9718fb1af618d5ce8678d0dc6e8a58f252216f
```

**⚠️ `distribution-iOS` 是死的**：只有 4 个文件、tag 最新是 `iphone-313` / `iphone-sdkb8`（iPhone OS 3.1.3 时代）。**没有 iOS ↔ 项目版本的官方清单**。实践中用 macOS 同代版本近似（macOS 26.x ≈ iOS 26.x，objc4/dyld/libdispatch 在 iOS 和 macOS 上是同一份源码）。

> **归档建议**：把 `distribution-macOS` 整仓浅 clone（482 KB，含全部 166 个 tag）**优先级仅次于 objc4**。它是"OS 版本 → 源码版本"的唯一权威索引，而且极小。同时把 `git ls-tree macos-265` 的输出以文本形式存一份，防止将来清单仓也变动。

### 1.4 归档策略对比（三选一）

| 策略 | 做法 | objc4 实测体积 | dyld | 全套 8 个核心库 | 优点 | 缺点 |
|---|---|---|---|---|---|---|
| **A. 整仓全历史** | `git clone --no-single-branch` | 4.7 MB | 13.5 MB | ~40 MB（不含 xnu/Libc） | 能 `git log -S` 跨版本 diff 函数演化；能看 `rel/*` 老版本（objc4-750 = iOS 12） | 略大；xnu 173 MB / Libc 8 MB / libmalloc 19 MB 拉高总量 |
| **B. 单 tag 快照** | 下 `codeload.github.com/.../tar.gz/refs/tags/<tag>` | **0.62 MB**（objc4-951.1 压缩后） | **1.63 MB**（dyld-1378） | ~6 MB 压缩 | 最小；干净；无 `.git` 噪音 | 丢失跨版本对比能力（学 ObjC runtime 恰恰很需要——"这个字段是哪版加的"） |
| **C. 只提取点名文件** | sparse-checkout 或 API 拉单文件 | **1.21 MB / 39 个文件**（未压缩） | — | — | 最精准 | 收益极小：objc4 全量快照才 3.06 MB，省不下多少，却会漏掉 `objc-os.h`、汇编 `objc-msg-arm64.s` 之类的关联文件 |

**结论：推荐 A（整仓浅历史 clone）用于 objc4 / dyld / libdispatch / libplatform / libpthread / libclosure / CF / libunwind；xnu、Libc、libmalloc、Security 用 B（单 tag）或干脆不本地化。**

理由：
- objc4 的"全历史"只有 35 个 commit，成本几乎为零，却换来 `git log -p -- runtime/objc-weak.mm` 这种"看某函数怎么演化"的能力——这正好对冲用户担心的"改版/改名找不到"。
- 策略 C 得不偿失。objc4 用户点名的关键文件实测清单（39 个文件 1.21 MB）：
  ```
  runtime/objc-object.h            50 008    ← struct objc_object, isa, retain/release 内联
  runtime/objc-runtime-new.h      115 042    ← class_data_bits_t, objc_class, cache_t, method_t
  runtime/objc-runtime-new.mm     339 258    ← lookUpImpOrForward, realizeClass, attachCategories
  runtime/objc-weak.mm             16 308    ← weak_register_no_lock, weak_entry_t
  runtime/objc-weak.h              5 296
  runtime/NSObject.mm             78 837    ← objc_autoreleasePoolPush/Pop, AutoreleasePoolPage, SideTable
  runtime/objc-private.h           43 003
  runtime/objc-cache.mm            54 153    ← cache_t::insert, 缓存扩容
  runtime/objc-class.mm            38 481
  runtime/objc-msg-arm64.s         24 142    ← objc_msgSend 汇编快速路径
  runtime/objc-internal.h          56 985
  runtime/runtime.h                71 465    ← 公开 API 注释最密集
  runtime/objc-abi.h               21 283
  runtime/objc-exception.mm        39 314
  runtime/objc-initialize.mm       36 980    ← +initialize 时序
  runtime/objc-loadmethod.mm       12 584    ← +load 时序
  runtime/objc-os.h                15 453    ← 平台原语、锁
  runtime/objc-config.h            13 368
  runtime/llvm-DenseMap.h          43 311    ← objc4 内部抄的 LLVM 容器
  ... 及 objc-block-trampolines / objc-sel / hashtable2 等
  ```
  整个 `runtime/` 目录 91 个文件，占 objc4 快照绝大部分。**直接留整个 objc4 就好，不要做文件级挑选。**

### 1.5 值得单独提取的文档

| 位置 | 内容 | 体积 | 价值 |
|---|---|---|---|
| **`dyld/doc/`** | `dyld4.md` (17 KB)、`CacheLayout.md` (17 KB)、`CacheBuilder.md` (4.4 KB)、`PatchTable.md` (7.7 KB)、`PrebuiltLoaderSet_Policy.md` (6.2 KB)、`Allocator.md` (7.4 KB)、`rst/dyld_usage.rst`、`tracing/dyld.codes`+`dyld.plist`、`man/man1`+`man3` | ~65 KB | **★★★★★ 全网最好的 dyld4 设计文档，且几乎没人转载。启动优化学习的一手资料。** |
| **`objc4/ReleaseNotes.rtf`** | Apple 官方逐版本 runtime 变更说明 | 19 KB | ★★★★ 直接告诉你"哪版改了什么"，配合 tag 用 |
| **`objc4/runtime/*.h` 注释** | `runtime.h`(71 KB)、`objc-internal.h`(57 KB)、`objc-abi.h`(21 KB) | 150 KB | ★★★★ 注释密度高于任何博客 |
| **`libdispatch/man/`** | dispatch 全套 man page | — | ★★★★ 官方语义定义（比 developer.apple.com 的文档更精确） |
| **`libdispatch/dispatch/` + `os/`** | 公开头文件，注释极密 | — | ★★★★ |
| **`libdispatch/PATCHES`** | 17.5 KB，Swift 社区对 libdispatch 的改动列表 | — | ★★ |
| **`libpthread/man/` + `lldbmacros/`** | man page + LLDB 调试脚本 | — | ★★★ `lldbmacros` 可以直接用来调试锁 |
| **`xnu/doc/` 与 `libmalloc/man/`** | 未细查（xnu 太大，本次只取元数据） | — | ★★ |

### 1.6 许可证（**实际读了 LICENSE 文件**）

**APSL 2.0（Apple Public Source License Version 2.0, August 6, 2003）** — objc4 / dyld / CF / Libc / xnu / IOKitUser 的根目录 `APPLE_LICENSE`（19 829 B，CF 是 20 108 B），首行确认：

```
APPLE PUBLIC SOURCE LICENSE
Version 2.0 - August 6, 2003
```

**实读第 2 节的关键条款：**

- **2.1 未修改代码**：可以 "use, reproduce, display, perform, internally distribute within Your organization, and **Externally Deploy** verbatim, unmodified copies"，商用非商用均可。条件：
  - (a) **必须保留全部版权声明、专有声明、免责声明，以及所有指向本许可证的声明**；
  - (b) **每一份你分发的 Covered Code 源码和文档，都必须附带一份本许可证副本**，且不得附加任何限制接收方权利的条款。
- **2.2 修改代码**：额外要求 (b) 在每个被改文件里加 Exhibit A 声明 + 显著标注"你改了这个文件及改动日期"；(c) 若 External Deploy 修改版，必须以 APSL 把修改后源码提供给接收方或公开，期限为"部署期间 或 首次部署起 12 个月"取长者。
- **2.3** 若只以二进制形式 External Deploy，必须显著声明源码可依本许可证取得，并给出获取途径。

**⇒ 对用户仓库的实际含义：**

1. **私有仓库归档：完全没问题。** 私有仓不构成 "External Deploy"（APSL 定义 External Deploy 大致是"向组织外的第三方分发或部署"），甚至连 2.1 都用不上——纯个人/组织内部使用是明确允许的。
2. **如果将来公开这个仓库**：仍然允许，但**必须**：
   - 把 `APPLE_LICENSE` 原文一起放进去（**不要只写 "APSL 2.0" 四个字，要放全文**）；
   - 不删任何源文件头部的 `@APPLE_LICENSE_HEADER_START@ ... END@` 块；
   - 如果你在归档的源码里加了笔记/注释（这很可能会做！），那就构成 Modification，需要在改动文件里标注"已修改 + 日期"。
   - **强烈建议：把笔记写在单独文件里（如 `notes/objc4-951-weak.md`），源码目录保持逐字节原样。** 这样永远停留在 2.1 的"unmodified copies"，规避 2.2 的全部额外义务。
3. **Apache-2.0 的 libdispatch / libplatform**（`LICENSE` 11 358 B = 标准 Apache 2.0）：比 APSL 宽松得多，公开也只需保留 LICENSE + NOTICE + 改动标注。
4. **⚠️ libpthread / libclosure / libmalloc / libunwind 根目录没有 LICENSE 文件**。实读 `libpthread/src/pthread.c` 头部确认是 APSL 2.0：
   ```
   * @APPLE_LICENSE_HEADER_START@
   * ... subject to the Apple Public Source License Version 2.0 ...
   * http://www.opensource.apple.com/apsl/
   ```
   另外 `libpthread` 还混有 **Open Software Foundation (OSF) 1991–1997 的版权**（Mach 血统）——多重许可，转发时更要保留原文件头。**这几个库如果要公开转发，请自己补一份 APSL 全文并说明来源。**
5. `apple-oss-distributions` 里另有 17 个 **GPL-2.0** 仓库（bash、gnutar 等）—— 与本次学习主题无关，**不要顺手一起归档**，避免把 GPL 传染进个人仓库的心智负担。

### 1.7 注意事项

- **CF 已死**：最后 commit `2021-10-06`，最新 tag `CF-1153.18`（≈ macOS 12 / iOS 15）。之后 Apple **不再公开 CoreFoundation 源码**。学 RunLoop 只能基于这份 2021 快照 + 逆向 + `swiftlang/swift-corelibs-foundation`（26.9 MB，Apache-2.0，含 CoreFoundation 的一个分叉，但已被 Swift 重写，不能当 Apple 现行实现读）。
  → **CF-1153.18 必须现在就归档**，这是"以后找不到"风险最高的一个（虽然仓库现在还在，但它是唯一已经停更的关键库）。
- **objc4 的 main 布局在近版本变了**：现在根目录同时有 `runtime/`（老位置）和 `ObjectiveC/` / `ObjectiveCTests/`（新的 Swift overlay / 测试计划），还多了 `objc.sln`、`prebuild.bat`、`version.rc`（Windows 支持）。老博客里的路径可能对不上。
- **xnu 不建议本地整仓**：GitHub 报告 177 MB（含历史），单 tag 未压缩 **82.86 MB / 6 113 个文件**，tarball 下载 120 秒才拉到 10.9 MB（codeload 对 xnu 很慢）。用户学 Mach/内核只需要少量头文件（`osfmk/mach/*.h`、`bsd/sys/*.h`），建议**只归档需要的头文件目录 + 记下 tag 号**。
- **codeload 直链可用**：`https://codeload.github.com/apple-oss-distributions/<repo>/tar.gz/refs/tags/<tag>`。实测 objc4-951.1 = 637 628 B，dyld-1378 = 1 633 422 B，libdispatch-1542.100.32 = 638 255 B，CF-1153.18 = 1 024 202 B。
- **不用 `git clone --depth 1`**：如 §1.3 所述全历史本来就很小，depth 1 反而丢掉了 objc4 最有价值的"版本 diff"能力。

---

## 2. Swift Evolution

### 2.1 是什么 / 现在在哪（已核实）

**组织已改名**：`github.com/apple/swift-evolution` → **301 重定向到 `github.com/swiftlang/swift-evolution`**（`gh api /repos/apple/swift-evolution` 返回的 `full_name` 直接就是 `swiftlang/swift-evolution`）。老链接仍可用但应该按新名字归档。

- 仓库：`swiftlang/swift-evolution`，size **15 772 KB**，default branch `main`，15 863 star
- 相关卫星仓：`swiftlang/swift-evolution-metadata-extractor`（4 645 KB，Apache-2.0，"JSON metadata generator for Swift Evolution dashboard"）

### 2.2 规模（实测 git tree）

- **`proposals/*.md`：565 份**，合计 **9 921 211 B ≈ 9.46 MB**
- 仓库 main 全部 blob：597 个文件 / **10 692 315 B ≈ 10.2 MB**
- **`visions/`：10 个文件**，是整个仓库最值钱的部分（比单个提案更宏观）：
  ```
  approachable-concurrency.md   33 714   ← Swift 6.2 并发易用性愿景，必读
  memory-safety.md              25 438   ← 内存安全愿景，必读
  macros.md                     42 123
  swift-testing.md              50 723
  using-c++-from-swift.md       57 188
  using-swift-from-c++.md       30 922
  embedded-swift.md             16 684
  networking.md                 14 519
  webassembly.md                13 225
  resources/（目录）
  ```
- 其他：`process.md`（32 KB，Evolution 流程本身）、`commonly_proposed.md`（9.8 KB，"这些别再提了"清单）、`policies/`、`releases/`（4 个文件，按 Swift 版本归类的提案索引）、`proposal-templates/`
- **整仓 main tarball 实测 3 338 400 B ≈ 3.18 MB**（压缩后）

### 2.3 官方状态索引 / JSON 数据源（已实测）

- ❌ **旧端点 `https://download.swift.org/swift-evolution/proposals.json` 已废弃**。实测返回 HTTP 200 但内容是 305 字节的错误 JSON：
  ```json
  { "message": "Not Found",
    "reason": "The proposals.json file has been obsoleted and replaced by
               https://download.swift.org/swift-evolution/v1/evolution.json.
               See https://forums.swift.org/t/swift-evolution-metadata-transition/71387 ...",
    "status": "404" }
  ```
- ✅ **现役端点：`https://download.swift.org/swift-evolution/v1/evolution.json`** — HTTP 200，**800 408 B ≈ 782 KB**，无需鉴权。
- ❌ `https://data.swift.org/swift-evolution/v1/evolution.json` → 403（不是这个域）
- 结构：顶层 `{commit, creationDate, implementationVersions, proposals, schemaVersion, toolVersion}`，`proposals` 数组 **538 条**（比 md 文件少，因为 md 里含模板/非 SE 文件）。每条含 `id`、`title`、`summary`（一段摘要！）、`authors`、`reviewManagers`、`status.{state,version}`、`link`（md 文件名）、`sha`、`trackingBugs`、`discussions`（**指向 Swift Forums 讨论帖的链接**，可作为 §3 抓取的种子）。
- **状态分布（实测统计）**：`implemented` 446、`rejected` 36、`returnedForRevision` 20、`accepted` 20、`activeReview` 8、`withdrawn` 7、`previewing` 1。

> 归档金点子：`evolution.json` 里的 `discussions` 字段 = 官方维护的"提案 ↔ 论坛帖"映射表。抓论坛不用手工找帖，直接从这里取 URL。

### 2.4 许可证（实读 `LICENSE.txt`, 11 757 B）

**Apache License 2.0 + Runtime Library Exception**。实读尾部：

```
## Runtime Library Exception to the Apache 2.0 License: ##

    As an exception, if you use this Software to compile your source code and
    portions of this Software are embedded into the binary product as a result,
    you may redistribute such product without providing attribution as would
    otherwise be required by Sections 4(a), 4(b) and 4(d) of the License.
```

⇒ **可以直接、逐字归档，也可以公开转发**。义务只有：保留 LICENSE、保留版权/NOTICE、若修改则标注改动。比 APSL 省心得多。这是本次侦察里**许可证最友好**的来源。

### 2.5 建议归档方式

1. `git clone --depth 50 https://github.com/swiftlang/swift-evolution.git`（3.2 MB 量级）
2. 额外定期抓 `evolution.json`（782 KB）并**带日期存档**（`evolution-2026-07-26.json`），因为它是唯一能告诉你"某提案被后续哪个提案取代/修订"的机器可读源。
3. 单独把 `visions/` 拷成一个显眼目录——这 10 篇是"读了就懂设计意图"的东西，别埋在 565 份提案里。

**优先级：P0**（体积小、许可证友好、内容质量最高）

### 2.6 注意事项

- 提案 markdown 里含大量 GitHub 相对链接（`../visions/x.md`）和 `\(...)` 数学式，离线渲染需要注意。
- 提案的"当前有效状态"不在 md 里而在 `evolution.json` / GitHub 的 README dashboard，**只存 md 会丢状态**（比如 SE-0338 后来被 SE-0461 改掉）。
- `apple/swift-evolution` 老 URL 目前仍重定向，但**归档时把 remote 写成 `swiftlang/...`**。

---

## 3. Swift Forums（forums.swift.org）

### 3.1 是什么 / 有 API 吗（已实测验证）

标准 **Discourse**，JSON API 完全可用，**无需 API key**：

| 端点 | 实测结果 |
|---|---|
| `GET /t/<slug>/<id>.json` | ✅ 200，`application/json`。实测 `/t/swift-evolution-metadata-transition/71387.json` = 36 903 B |
| `GET /t/<id>.json`（省略 slug 也行） | ✅ 200。实测 `/t/54206.json` = **157 847 B** |
| `GET /t/<id>.json?page=2` | ✅ 200，92 555 B，返回 post_number 21–40 |
| `GET /categories.json` | ✅ 200，51 827 B，含全部板块 + topic_count |
| `GET /search.json?q=<query>&order:likes` | ✅ 200，~55 KB，返回 `topics`/`posts`/`users`/`categories` |
| **`GET /raw/<topic_id>`** | ✅ 200，**147 002 B**，返回**纯 markdown 原文**（`作者 \| 时间 \| #楼号` + 正文），每页 100 楼 |
| `GET /raw/<topic_id>?page=2` | ✅ 200，111 552 B |
| `GET /sitemap.xml` | 存在（robots.txt 里声明） |

**关键发现：`/raw/<id>` 是最佳抓取方式。**
以 topic 54206（269 楼、49 291 词）为例：
- `.json` 方式：`chunk_size = 20`，需要 **14 次请求**，每次 ~90–160 KB → **约 1.4 MB JSON**（含大量 HTML `cooked` 冗余、avatar URL、actions_summary）
- `/raw/` 方式：每页 100 楼 → 只需 **3 次请求**，约 **147 + 112 + ~80 ≈ 340 KB 纯文本**
- **体积省 4×，请求数省 4.7×，而且直接是 markdown，适合放进笔记仓库。**

### 3.2 robots.txt（实读全文）

```
User-agent: mauibot / semrushbot / ahrefsbot / blexbot / seo spider
Disallow: /

User-agent: *
Disallow: /admin/
Disallow: /auth/
Disallow: /assets/js/browser-update*.js
Disallow: /email/
Disallow: /session
Disallow: /user-api-key
Disallow: /*?api_key*
Disallow: /*?*api_key*
Disallow: /badges
Disallow: /my
Disallow: /search        ← ⚠️
Disallow: /tag/*/l
Disallow: /g
Disallow: /t/*/*.rss     ← 只禁 RSS
Disallow: /c/*.rss

Sitemap: https://forums.swift.org/sitemap.xml
```

**解读：**
- ✅ **`/t/...` 和 `/raw/...` 没有被 Disallow** —— 抓取具体帖子是 robots 允许的。
- ⚠️ **`/search` 被 Disallow**。`search.json` 严格说落在 `/search` 前缀下。**用它做一次性人工探索没问题（本报告就这么做的），但不要写成定时爬虫。** 更合规的做法：从 `evolution.json` 的 `discussions` 字段或从 `sitemap.xml` 拿 topic ID，而不是循环打 search。
- 没有 `Crawl-delay` 指令，但**礼貌起见自加 1–2 秒间隔**。Discourse 默认对匿名请求有速率限制（约 60 req/min），超了会 429。

### 3.3 许可证 / 法律状态 ⚠️ 本次侦察最需要注意的一点

- **forums.swift.org 的帖子内容没有任何开放许可证声明**。Discourse 默认版权归各发帖人。Swift 项目的 Apache-2.0 只覆盖代码仓库，**不覆盖论坛发言**。
- ⇒ **可以为个人学习抓取并存到私有仓库**（合理使用/研究目的），但：
  - **绝对不要把抓来的论坛内容公开发布或再分发**；
  - 归档时**必须保留原帖 URL、作者名、时间戳**（`/raw/` 输出天然带这三样，很方便）；
  - 私有仓库里建议在目录顶层放一个 `PROVENANCE.md`，写明"以下内容抓自 forums.swift.org，版权归原作者，仅供个人学习，禁止再分发"。
- 这是与 §1（APSL，可有条件公开）、§2（Apache-2.0，可公开）**性质完全不同**的一类。建议在仓库里物理隔离：`sources/apache/`、`sources/apsl/`、`private-notes/forums/`（后者进 `.gitignore` 的公开分支，或干脆整仓保持私有）。

### 3.4 板块概况（实测 `categories.json`）

| ID | slug | topics | posts |
|---|---|---|---|
| 15 | **swift-users** | 14 070 | 88 339 |
| 3 | site-feedback | 281 | 1 587 |
| 43 | server | 153 | 1 012 |
| 24 | general-announce | 133 | 1 445 |
| 25 | related-projects | 198 | 985 |
| 66 | community-showcase | 585 | 3 512 |
| 92 | swift-documentation | 72 | 374 |
| 84 | swift-website | 53 | 493 |
| 122 | platform | 6 | 111 |
| 120 | ecosystem | 18 | 21 |
| 110 | contributor-experience | 9 | 28 |
| **18** | **evolution** | **0**（!） | 0 |
| **16** | **development** | 5 | 9 |

**注意：`evolution`(18) 和 `development`(16) 的 topic_count 是 0/5 —— 因为它们是"父容器"，真实内容全在子板块里**（`evolution/pitches`、`evolution/proposal-reviews`、`evolution/announce`、`development/compiler`、`development/concurrency` 等），而 `categories.json` 默认不展开 subcategory_list。抓取时要用 `/c/evolution/pitches/<id>.json` 逐个子板块拉。

**最有价值的板块（按底层学习）**：
1. `evolution/pitches` — 设计讨论最深的地方
2. `evolution/proposal-reviews` — 每个 SE 提案的 review 帖，含核心开发者对权衡的解释
3. `development/compiler` + `development/concurrency` — 编译器/并发运行时实现细节
4. `swift-users` — 量最大但信噪比最低，**不建议整板块抓**

### 3.5 十个高价值长帖（实测 topic id + 楼层数）

| # | topic | 楼层 | URL | 为什么值得 |
|---|---|---|---|---|
| 1 | A roadmap for improving Swift performance predictability: ARC improvements and ownership control | **269** | https://forums.swift.org/t/54206 | Joe Groff 写的 ARC/所有权总路线图，49 291 词。**理解 ARC 优化器为什么会插/删 retain-release 的最佳单篇** |
| 2 | Swift Concurrency Roadmap | 168 | https://forums.swift.org/t/41611 | 整个 Swift Concurrency 的顶层设计文档 + 讨论，async/await 全家桶的起点 |
| 3 | On the road to Swift 6 | 176 | https://forums.swift.org/t/32862 | 语言演进的取舍全景，含所有权/内存模型的早期决策 |
| 4 | Low-Level Atomic Operations | 145 | https://forums.swift.org/t/34683 | 原子操作 + 内存序（acquire/release/relaxed）的设计讨论，学锁与无锁必读 |
| 5 | [Pitch] Move Function + "Use After Move" Diagnostic | 219 | https://forums.swift.org/t/53983 | 移动语义/生命周期结束的编译器实现细节 |
| 6 | Vector, a fixed-size array | **271** | https://forums.swift.org/t/75264 | 固定大小存储、内存布局、noncopyable 泛型的长跑讨论 |
| 7 | [Prospective Vision] Improving the approachability of data-race safety | 183 | https://forums.swift.org/t/76183 | Swift 6.2 并发默认隔离的完整论证（对应 SE-0461/0466） |
| 8 | [Pitch] Noncopyable (or "move-only") structs and enums | 121 | https://forums.swift.org/t/61903 | `~Copyable` 的语义地基 |
| 9 | Swift Performance | 139 | https://forums.swift.org/t/28776 | 早期但极经典，讲清 Swift 值语义/CoW/ARC 的性能模型 |
| 10 | [Pitch] Synchronous Mutual Exclusion Lock | 56 | https://forums.swift.org/t/69889 | `Mutex` 的设计（对应 SE-0433），和 `os_unfair_lock` / GCD 的对比讨论 |

**加分候选（也很值，凑够 15 条抓一批）：**

| topic | 楼层 | URL | 主题 |
|---|---|---|---|
| Modify accessors | 304 | https://forums.swift.org/t/31872 | `_modify`/coroutine accessor，借用语义源头（对应 SE-0507） |
| [Pitch] Observation | 112 | https://forums.swift.org/t/62051 | Observation 的实现机制（对应 SE-0395） |
| [Pitch] Reflection | 61 | https://forums.swift.org/t/61438 | Swift 运行时元数据/反射，可与 objc runtime 对照 |
| Support custom executors in Swift Concurrency | 55 | https://forums.swift.org/t/44425 | actor executor ↔ GCD queue 的桥接（对应 SE-0392/0417） |
| [Pitch] Region Based Isolation | 15（短但密） | https://forums.swift.org/t/67888 | 区域隔离（对应 SE-0414） |
| Safely sending non-`Sendable` values across isolation domains | 24 | https://forums.swift.org/t/66566 | `sending` 参数的推导 |
| Noncopyable Generics in Swift: a code walkthrough | 48 | https://forums.swift.org/t/70862 | 编译器实现走查 |
| An Informal Introduction to Move-Only Types | 28 | https://forums.swift.org/t/61358 | 入门版所有权解释 |
| Cooperative pool deadlock when calling into an opaque subsystem | 32 | https://forums.swift.org/t/70685 | **协作线程池死锁的真实案例**，GCD 线程爆炸的现代版 |
| [Prospective vision] Optional Strict Memory Safety for Swift | 72 | https://forums.swift.org/t/75090 | 内存安全愿景（对应 SE-0458） |

### 3.6 抓取难度与体积

- **难度：低**。无鉴权、无 JS 渲染、无 Cloudflare 挑战。`curl` 直出即可。
- **体积估算**（用 `/raw/` 方式）：
  - 平均一楼约 **1.3 KB** 纯文本（54206：147 002 B / 100 楼 ≈ 1.47 KB/楼）
  - 上表 20 个帖子合计约 **2 400 楼 → ≈ 3.2 MB 纯 markdown**
  - 若扩到"`evolution/pitches` + `evolution/proposal-reviews` 全量"：这两个板块加起来数千帖、十万量级楼层 → **约 150–300 MB**，且需数小时（受速率限制）。**不建议全量。**
- **推荐方案：种子驱动的小规模抓取**
  1. 从 `evolution.json` 提取 `discussions[].link`（官方维护的提案↔帖子映射）
  2. 只抓 §2.7 必读名单那 25 个提案对应的 pitch + review 帖 ≈ 50 个帖子
  3. 加上 §3.5 的 20 个"路线图/愿景"长帖
  4. 用 `/raw/<id>?page=N`，请求间隔 1.5 s
  5. **总计约 70 个帖子 / ~250 次请求 / ≈ 10–15 MB markdown**，一次跑完不到 10 分钟
- **⚠️ 帖子会被编辑**。归档时记录抓取日期；`/t/<id>.json` 的 `post_stream.posts[].updated_at` 可用于增量更新判断。

**优先级：P1**（价值极高但许可证受限，且需要自己写脚本）

---

## 4. 顺带考察：Clang / LLVM / WebKit / opensource.apple.com

### 4.1 Clang 官方文档（用户已在读的那批）★★★★★

- **仓库**：`llvm/llvm-project`，路径 **`clang/docs/`**
- **规模**：整仓 **4 220 365 KB ≈ 4.02 GB**（❌ 绝对不要整仓 clone）；但 **`clang/docs/` 只有 107 个文件 / 5 838 118 B ≈ 5.57 MB**（含少量图片）
- **用户已在读的三篇，实测存在且体积如下**：
  ```
  clang/docs/Block-ABI-Apple.rst              33 817 B   ← Blocks ABI 规范（配 libclosure 读）
  clang/docs/AutomaticReferenceCounting.rst  119 175 B   ← ARC 语言规范，全网最权威
  clang/docs/AttributeReference.rst           （在 107 个文件内）
  ```
- **强烈建议顺手加上的同系列**：
  ```
  clang/docs/BlockLanguageSpec.rst            13 085 B   ← Blocks 语言层规范
  clang/docs/PointerAuthentication.md         79 073 B   ← arm64e PAC，学 Mach-O/启动/安全必读
  clang/docs/ObjectiveCLiterals.rst           22 480 B
  clang/docs/ThreadSafetyAnalysis.md          37 166 B   ← 学锁时的静态分析视角
  clang/docs/ThreadSanitizer.md               15 740 B
  clang/docs/MemorySanitizer.md               10 126 B
  ```
- **许可证（实读 `LICENSE.TXT`）**：第 2 行明确
  ```
  The LLVM Project is under the Apache License v2.0 with LLVM Exceptions:
  ```
  ⇒ **Apache-2.0 with LLVM Exceptions**。可自由归档、可公开转发，义务同 Apache-2.0。
- **建议归档方式**：sparse checkout，**不要整仓 clone**
  ```
  git clone --filter=blob:none --sparse --depth 1 https://github.com/llvm/llvm-project.git
  cd llvm-project && git sparse-checkout set clang/docs
  ```
  落地 ~5.6 MB（若剔掉 `.png/.svg` 约 1.5 MB 纯文本）。
- **优先级：P0**（用户已经在读，且是 Blocks/ARC 的规范级一手资料）

### 4.2 Swift 编译器文档 `swiftlang/swift/docs/` ★★★★★（本次意外收获）

- 整仓 `swiftlang/swift` = **1 366 144 KB ≈ 1.3 GB**（❌ 别整仓 clone）
- **`docs/` 目录：243 个文件 / 10 332 KB ≈ 10.1 MB**
- 与用户学习主题直接相关的（实测文件名 + 体积）：
  ```
  docs/OwnershipManifesto.md              69 717 B  ★★★★★ 所有权模型总纲（比任何 SE 提案都全）
  docs/SIL/ARCOptimization.md             29 711 B  ★★★★★ ARC 优化器怎么工作
  docs/SIL/Ownership.md                   47 748 B  ★★★★★ SIL 层所有权规则
  docs/Runtime.md                         14 146 B  ★★★★  Swift runtime 接口
  docs/ABIStabilityManifesto.md           57 523 B  ★★★★  ABI 稳定性（对照 ObjC 的 fragile ivar 问题）
  docs/ABI/TypeMetadata.rst               35 228 B  ★★★★  类型元数据布局（对照 objc_class）
  docs/ABI/TypeLayout.rst                 11 130 B  ★★★★
  docs/ABI/Mangling.rst                   78 253 B  ★★★   符号修饰（读 crash log / nm 输出必备）
  docs/ABI/CallingConvention.rst          58 136 B  ★★★★  含 self/error 寄存器约定
  docs/ABI/CallingConventionSummary.rst   13 064 B
  docs/ABI/KeyPaths.md                    13 357 B
  docs/SIL/SIL.md                         79 719 B
  docs/SIL/Instructions.md               214 558 B  （参考手册，按需查）
  docs/HighLevelSILOptimizations.rst      18 422 B
  ```
- **许可证**：仓库整体 Apache-2.0（+ Runtime Library Exception），与 swift-evolution 相同。✅ 自由归档
- **建议**：sparse checkout `docs/`，约 2.5 MB 压缩后。**优先级 P0** —— 这批文档解释"为什么 ARC 会这样优化"，和 objc4 源码是互补关系，用户的学习计划里似乎还没覆盖到。

### 4.3 WebKit ★☆（与 iOS 底层关系弱）

- `WebKit/WebKit` = **12 785 668 KB ≈ 12.2 GB**，GitHub license 字段 `none`（实际是 LGPL-2.1 + BSD 混合，Source 各子目录各自带 header）。**❌ 不要碰。**
- 文档不在主仓（主仓无 `Documentation/` 目录，404）。文档独立仓：**`WebKit/Documentation`**
  - 112 个文件 / **45 508 KB ≈ 44.4 MB**（大头是截图）
  - **仓库根目录没有 LICENSE 文件** ⚠️（只有 `README.md`、`mkdocs.yml`、`docs/`）。README 说内容"collected from Trac, GitHub Wiki, and WebKit source code markdown files" —— **来源混杂、许可不明，公开转发风险高**
  - 与用户主题相关的少数几篇：
    ```
    docs/Deep Dive/MemoryManagement.md          ← WebKit 的 RefPtr/Ref/WeakPtr 智能指针体系
    docs/Deep Dive/Libpas/Libpas.md             ← libpas 内存分配器（可与 libmalloc 对照）
    docs/Deep Dive/Libpas/Internals.md
    docs/Deep Dive/JSC/JavaScriptCore.md        ← JSC 架构
    docs/Deep Dive/JSC/JSCObjectAccessOptimization.md  ← inline cache，可与 objc method cache 对照
    docs/Deep Dive/Architecture/WebKit2.md      ← 多进程架构（IPC / XPC）
    docs/Getting Started/Introduction.md
    ```
  - WebKit 组织其他仓库：`explainers`(29 MB)、`standards-positions`(2.4 MB)、`WebKit-http`(7.8 GB, 老仓)、`WebKit-integration`(12 GB)
- **建议**：**不归档整仓**。只把上面 5–7 篇 markdown 单独保存，并在文件头注明原始 URL 与抓取日期，标为"许可不明，仅个人参考，勿转发"。**优先级 P3**
- 注：`apple-oss-distributions` 里也有 `WebKit`(835 MB) 和 `WebCore`(413 MB) —— 是历史投放，同样不建议归档。

### 4.4 opensource.apple.com —— 还在，但**已经完全变成 GitHub 的跳板**（重要发现）

实测 HTTP 追踪：

| URL | 结果 |
|---|---|
| `https://opensource.apple.com/` | 200，10 848 B。页面只有三个 Featured Projects（Swift / Container / WebKit）+ 一个 Releases 入口 |
| `https://opensource.apple.com/releases/` | 200，8 017 B。**内容由 JS 动态加载**（HTML 里只有 "Loading Releases.."），文案明确说"download the open source code ... from their respective **GitHub** pages" |
| `https://opensource.apple.com/apsl/` | 200，26 624 B。**APSL 全文仍在这里托管**（源码文件头引用的就是这个 URL） |
| `https://opensource.apple.com/tarballs/` | 200 → **最终 URL = `https://github.com/apple-oss-distributions/`** |
| `https://opensource.apple.com/tarballs/objc4/` | 200 → **最终 URL = `https://github.com/apple-oss-distributions/objc4/tags`** |
| `https://opensource.apple.com/tarballs/objc4/objc4-818.2.tar.gz` | 200 → **最终 URL = `https://codeload.github.com/apple-oss-distributions/objc4/tar.gz/refs/tags/objc4-818.2`** |
| `https://opensource.apple.com/source/objc4/` | **404**（旧的在线源码浏览器已彻底下线） |
| `https://opensource.apple.com/releases.json` / `/api/releases` | 404 |

**结论：**
1. `opensource.apple.com` 与 `apple-oss-distributions` 是**同一套数据**：前者是门面 + 一层 301/302 重定向层，后者是唯一实际存储。
2. **没有任何 GitHub 上没有的东西**。历史上的 `/source/<proj>/` 在线浏览器（那个能直接点开 `objc-weak.mm` 的老页面）**已 404 下线**，`/tarballs/` 全部重定向到 codeload。
3. 唯一值得单独存的：**`https://opensource.apple.com/apsl/` 的 APSL 2.0 全文**（26 KB）—— 因为所有 APSL 源码文件头都引用这个 URL，万一将来它挂了，你手上要有一份。不过 objc4 等仓库根目录的 `APPLE_LICENSE` 内容一致，存那份也行。
4. 好消息：**老版本的 tarball 仍然拿得到**（`tarballs/objc4/objc4-818.2.tar.gz` → 200），因为 GitHub tags 里保留了历史。所以"想看 iOS 12 时代的 objc4-750"是可行的：直接用 tag。

---

## 5. 必读短名单

### 5.1 Swift Evolution 必读 25 份（含状态，实测自 `evolution.json`）

URL 格式统一为 `https://github.com/swiftlang/swift-evolution/blob/main/<link>`；网页版可读 `https://www.swift.org/swift-evolution/#?id=SE-XXXX`。

#### A. 内存 / ARC / 内存模型（5 份）

| 编号 | 状态 | 标题 | 文件 | 一句话理由 |
|---|---|---|---|---|
| **SE-0176** | implemented | Enforce Exclusive Access to Memory | `proposals/0176-enforce-exclusive-access-to-memory.md` | 独占访问（law of exclusivity）是 Swift 内存模型的地基，也是 `inout` 别名崩溃的根源解释 |
| **SE-0282** | implemented | Clarify the Swift memory consistency model | `proposals/0282-atomics.md` | Swift 正式采纳 C/C++ 内存一致性模型；学锁/无锁/`memory_order` 的官方定义 |
| **SE-0410** | implemented | Low-Level Atomic Operations | `proposals/0410-atomics.md` | `Atomic<T>` + 全部 memory ordering，对照 `os_unfair_lock`/`OSAtomic` |
| **SE-0481** | implemented | `weak let` | `proposals/0481-weak-let.md` | 弱引用的不可变形式；配合 objc4 的 `objc-weak.mm` 理解 weak 表机制 |
| **SE-0458** | implemented | Opt-in Strict Memory Safety Checking | `proposals/0458-strict-memory-safety.md` | `@unsafe`/`unsafe` 表达式，Swift 对"不安全内存操作"的边界划定 |

#### B. 所有权 / 借用 / noncopyable（6 份）

| 编号 | 状态 | 标题 | 文件 | 理由 |
|---|---|---|---|---|
| **SE-0366** | implemented | `consume` operator to end the lifetime of a variable binding | `proposals/0366-move-function.md` | 显式结束生命周期 = 手动干预 ARC 的官方入口 |
| **SE-0377** | implemented | `borrowing` and `consuming` parameter ownership modifiers | `proposals/0377-parameter-ownership-modifiers.md` | 参数所有权三态（borrow/consume/inout），理解 retain/release 何时被省略 |
| **SE-0390** | implemented | Noncopyable structs and enums | `proposals/0390-noncopyable-structs-and-enums.md` | `~Copyable` 语义地基；RAII 式资源管理 |
| **SE-0427** | implemented | Noncopyable Generics | `proposals/0427-noncopyable-generics.md` | 泛型系统如何容纳不可复制类型 |
| **SE-0447** | implemented | Span: Safe Access to Contiguous Storage | `proposals/0447-span-access-shared-contiguous-storage.md` | 用借用替代 `UnsafeBufferPointer`，是"安全地看内存"的现代答案 |
| **SE-0507** | implemented | Borrow and Mutate Accessors | `proposals/0507-borrow-accessors.md` | `_read`/`_modify` 的正式化，属性访问零拷贝的实现基础 |

#### C. Swift Concurrency 核心（9 份）

| 编号 | 状态 | 标题 | 文件 | 理由 |
|---|---|---|---|---|
| **SE-0296** | implemented | Async/await | `proposals/0296-async-await.md` | 起点。协程/挂起点/续体的语义定义 |
| **SE-0300** | implemented | Continuations for interfacing async tasks with synchronous code | `proposals/0300-continuation.md` | 桥接 GCD 回调 ↔ async 的唯一正规通道，理解挂起底层 |
| **SE-0302** | implemented | `Sendable` and `@Sendable` closures | `proposals/0302-concurrent-value-and-concurrent-closures.md` | 数据竞争检查的类型系统基础 |
| **SE-0304** | implemented | Structured concurrency | `proposals/0304-structured-concurrency.md` | Task 树、取消传播、优先级继承 —— 对照 GCD 的"无结构"设计 |
| **SE-0306** | implemented | Actors | `proposals/0306-actors.md` | actor 隔离与串行执行器；理解为什么 actor ≠ serial queue |
| **SE-0316** | implemented | Global actors | `proposals/0316-global-actors.md` | `@MainActor` 的语义，对照 main queue/RunLoop |
| **SE-0297** | implemented | Concurrency Interoperability with Objective-C | `proposals/0297-concurrency-objc.md` | **ObjC 学习者必读**：completion handler ↔ async 的自动桥接规则 |
| **SE-0317** | implemented | `async let` bindings | `proposals/0317-async-let.md` | 子任务的最轻量形式 |
| **SE-0337** | implemented | Incremental migration to concurrency checking | `proposals/0337-support-incremental-migration-to-concurrency-checking.md` | `@preconcurrency` 的语义；老 ObjC 代码库迁移的官方路径 |

#### D. 并发运行时 / 执行器（对应 GCD 知识）（3 份）

| 编号 | 状态 | 标题 | 文件 | 理由 |
|---|---|---|---|---|
| **SE-0392** | implemented | Custom Actor Executors | `proposals/0392-custom-actor-executors.md` | **把 actor 跑在自己的 `DispatchQueue` 上** —— GCD 和 Swift Concurrency 的接缝在这里 |
| **SE-0417** | implemented | Task Executor Preference | `proposals/0417-task-executor-preference.md` | 协作线程池 vs 自定义线程池的选择机制 |
| **SE-0433** | implemented | Synchronous Mutual Exclusion Lock | `proposals/0433-mutex.md` | 官方 `Mutex`；与 `os_unfair_lock`/`NSLock`/`pthread_mutex` 直接对比 |

#### E. 隔离模型的现代演进（3 份，理解 Swift 6.2 行为必读）

| 编号 | 状态 | 标题 | 文件 | 理由 |
|---|---|---|---|---|
| **SE-0414** | implemented | Region based Isolation | `proposals/0414-region-based-isolation.md` | 区域隔离让非 Sendable 值也能安全跨隔离域传递，是 Swift 6 可用性的关键 |
| **SE-0461** | implemented | Run nonisolated async functions on the caller's actor by default | `proposals/0461-async-function-isolation.md` | **推翻了 SE-0338 的默认行为** —— 只读老提案会得到过时结论 |
| **SE-0466** | implemented | Control default actor isolation inference | `proposals/0466-control-default-actor-isolation.md` | `-default-isolation MainActor`，Swift 6.2 "approachable concurrency" 的开关 |

#### F. Observation（2 份）

| 编号 | 状态 | 标题 | 文件 | 理由 |
|---|---|---|---|---|
| **SE-0395** | implemented | Observation | `proposals/0395-observability.md` | `@Observable` 宏的机制；替代 KVO，可与 ObjC KVO 的 isa-swizzling 实现对照 |
| **SE-0475** | implemented | Transactional Observation of Values | `proposals/0475-observed.md` | `Observations` async sequence，观察 + 并发的结合 |

> 备选（如果想凑到 30）：**SE-0327**（On Actors and Initialization，actor 初始化期的隔离洞）、**SE-0371**（Isolated synchronous deinit，`deinit` 里的隔离——ARC + 并发交叉点）、**SE-0412**（Strict concurrency for global variables，全局变量/单例的线程安全，对照 `dispatch_once`）、**SE-0420**（Inheritance of actor isolation，`#isolation`）、**SE-0431**（`@isolated(any)`）、**SE-0338**（读它是为了知道 SE-0461 改掉了什么）。
> 状态提醒：**SE-0506（Advanced Observation Tracking）和 SE-0532、SE-0515 目前是 `accepted` 未 implemented**，SE-0533 已 `rejected`。

### 5.2 Vision 文档必读 2 份（比提案更值）

| 文件 | 体积 | 理由 |
|---|---|---|
| `visions/approachable-concurrency.md` | 33 714 B | **Swift 6.2 并发所有变化的总纲**。读了它，SE-0461/0466/0414 全都串起来了 |
| `visions/memory-safety.md` | 25 438 B | Swift 内存安全的分类学（时间安全/空间安全/初始化安全/类型安全/线程安全），SE-0458 的背景 |

### 5.3 Swift 编译器文档必读 5 篇（`swiftlang/swift/docs/`）

| 文件 | 体积 | 理由 |
|---|---|---|
| `docs/OwnershipManifesto.md` | 69 717 B | 所有权模型的原始总纲，SE-0366/0377/0390 都是它的分期落地 |
| `docs/SIL/ARCOptimization.md` | 29 711 B | **ARC 优化器的实际算法**。用户学"为什么这里没有 retain"的终极答案 |
| `docs/SIL/Ownership.md` | 47 748 B | SIL 层的 owned/guaranteed/unowned 值约定 |
| `docs/Runtime.md` | 14 146 B | Swift runtime 的入口函数清单（对照 objc4 的 `_objc_init`） |
| `docs/ABI/TypeMetadata.rst` | 35 228 B | Swift 类型元数据布局，与 `objc_class` / `class_ro_t` 直接对照 |

### 5.4 Clang 文档必读 4 篇（`llvm/llvm-project/clang/docs/`）

| 文件 | 体积 | 理由 |
|---|---|---|
| `AutomaticReferenceCounting.rst` | 119 175 B | **ARC 的语言规范本体**（ownership qualifier、bridged cast、`objc_precise_lifetime`…）。用户已在读 ✅ |
| `Block-ABI-Apple.rst` | 33 817 B | Blocks 的二进制布局（`Block_literal_1`、`Block_byref`、flags）。**必须和 `libclosure/Block_private.h` 配对读** |
| `BlockLanguageSpec.rst` | 13 085 B | Blocks 语言层规范（`__block` 语义），补 ABI 文档的上半层 |
| `PointerAuthentication.md` | 79 073 B | arm64e 指针认证。学 Mach-O/dyld/crash 分析的现代必需品，中文资料几乎全错 |

---

## 6. 最终归档方案与体积

### 6.1 推荐目录结构（按许可证隔离）

```
apple-developer-docs-vault/
├── LICENSES/
│   ├── APSL-2.0.txt                  ← 从 objc4/APPLE_LICENSE 或 opensource.apple.com/apsl/ 取
│   ├── Apache-2.0.txt
│   └── Apache-2.0-with-LLVM-Exceptions.txt
├── PROVENANCE.md                     ← 每个来源的 URL / 版本 / tag / 抓取日期 / 许可证
│
├── sources-apsl/                     ← APSL 2.0：可公开但必须带全文许可证 + 不改文件
│   ├── objc4/                        (git, 全历史 35 commits + 13 个 rel/* 分支)   4.7 MB
│   ├── dyld/                         (git, 全历史)                              13.5 MB
│   ├── CF/                           (git, 冻结在 CF-1153.18)                    2.1 MB
│   ├── libpthread/  libclosure/  libmalloc/  libunwind/                        ~22 MB
│   └── snapshots/                    ← 老版本 tarball（如 objc4-750 = iOS 12）   按需
│
├── sources-apache/                   ← Apache-2.0：最自由
│   ├── libdispatch/                  (git 全历史)                                3.7 MB
│   ├── libplatform/                                                             0.3 MB
│   ├── swift-evolution/              (depth 50)                                  3.5 MB
│   ├── swift-docs/                   (sparse: swiftlang/swift → docs/)          ~2.5 MB
│   └── clang-docs/                   (sparse: llvm-project → clang/docs/)       ~5.6 MB
│
├── indexes/
│   ├── distribution-macOS/           (git, 166 tags — OS↔版本映射)               0.5 MB
│   ├── evolution-2026-07-26.json     (782 KB, 带日期存档)
│   └── oss-version-map.md            ← 手工整理：iOS/macOS 版本 → objc4/dyld/... tag
│
├── private-forums/                   ← ⚠️ 无开放许可，禁止公开/再分发
│   ├── README-LEGAL.md
│   └── t-54206-arc-ownership-roadmap.md  等 ~70 个帖子              ~10-15 MB
│
└── notes/                            ← 你自己的笔记，永远不要写进 sources-* 里
```

### 6.2 体积预估

| 分组 | 内容 | 磁盘占用 |
|---|---|---|
| APSL 核心源码（含 git 历史） | objc4 + dyld + CF + libpthread + libclosure + libmalloc + libunwind | **≈ 42 MB** |
| Apache 源码 + 文档 | libdispatch + libplatform + swift-evolution + swift/docs + clang/docs | **≈ 16 MB** |
| 索引 | distribution-macOS + evolution.json | **≈ 1.3 MB** |
| Swift Forums（70 帖，纯 markdown） | | **≈ 12 MB** |
| WebKit 精选 5–7 篇 | | **≈ 1 MB** |
| **小计（推荐方案）** | | **≈ 72 MB** |
| （可选）Libc 单 tag | | +8.7 MB |
| （可选）xnu 单 tag 解压 | | +83 MB |
| （可选）xnu 只取 `osfmk/mach/*.h` + `bsd/sys/*.h` | | **+~3 MB（推荐这个）** |
| **含 xnu 头文件的现实总量** | | **≈ 84 MB** |

72–84 MB 对一个 git 仓库完全舒适。**不要把 xnu / Libc / Security / WebKit 整仓拉进来**，否则会从 84 MB 直接跳到 1 GB+。

### 6.3 具体命令（供执行阶段参考）

```bash
# APSL 核心（全历史，因为历史本来就只有几十个版本快照）
for r in objc4 dyld CF libpthread libclosure libmalloc libunwind; do
  git clone --no-single-branch https://github.com/apple-oss-distributions/$r.git sources-apsl/$r
done

# Apache 源码
for r in libdispatch libplatform; do
  git clone https://github.com/apple-oss-distributions/$r.git sources-apache/$r
done

# Swift Evolution（注意是 swiftlang，不是 apple）
git clone --depth 50 https://github.com/swiftlang/swift-evolution.git sources-apache/swift-evolution
curl -sSL https://download.swift.org/swift-evolution/v1/evolution.json \
  -o indexes/evolution-$(date +%F).json

# Swift 编译器文档（sparse，避开 1.3 GB 主仓）
git clone --filter=blob:none --sparse --depth 1 \
  https://github.com/swiftlang/swift.git sources-apache/swift-docs
git -C sources-apache/swift-docs sparse-checkout set docs

# Clang 文档（sparse，避开 4 GB 主仓）
git clone --filter=blob:none --sparse --depth 1 \
  https://github.com/llvm/llvm-project.git sources-apache/clang-docs
git -C sources-apache/clang-docs sparse-checkout set clang/docs

# OS ↔ 版本映射索引
git clone https://github.com/apple-oss-distributions/distribution-macOS.git indexes/distribution-macOS
git -C indexes/distribution-macOS ls-tree macos-265 > indexes/macos-265-versions.txt

# xnu 只取需要的头文件（不要整仓）
git clone --filter=blob:none --sparse --depth 1 \
  --branch xnu-12377.121.6 https://github.com/apple-oss-distributions/xnu.git sources-apsl/xnu-headers
git -C sources-apsl/xnu-headers sparse-checkout set osfmk/mach bsd/sys EXTERNAL_HEADERS

# 论坛（示例：抓一个帖子，注意 1.5s 间隔）
curl -sSL "https://forums.swift.org/raw/54206"        -o private-forums/t-54206-p1.md
sleep 1.5
curl -sSL "https://forums.swift.org/raw/54206?page=2" -o private-forums/t-54206-p2.md
```

### 6.4 三条最重要的许可证注意事项

1. **APSL 2.0 要求"每份分发都附带许可证全文 + 不删文件头声明"。** 私有仓库归档无义务；一旦公开，必须原文照搬 `APPLE_LICENSE` 并保留所有 `@APPLE_LICENSE_HEADER_START@` 块。**⇒ 把笔记写在 `notes/` 里，绝不在 `sources-apsl/` 的源文件上加注释**，这样永远算 §2.1「unmodified copies」，避免触发 §2.2 的"标注每处改动 + 12 个月公开修改源码"义务。
2. **libpthread / libclosure / libmalloc / libunwind 根目录没有 LICENSE 文件**（GitHub 也识别不出），实际是 APSL 2.0 且 libpthread 还混有 OSF/Mach 的旧版权。**归档时自己补一份 `APSL-2.0.txt` 并在 `PROVENANCE.md` 里注明**，否则将来自己都说不清这堆代码是什么许可。
3. **forums.swift.org 的内容没有任何开放许可，版权归各发帖人。** 可以为个人学习抓进私有仓库，**但绝不能公开或再分发**。物理隔离到 `private-forums/`，并保留每帖的 URL + 作者 + 时间戳（`/raw/` 输出天然带这三样）。

---

## 附：本次侦察实际发出的请求约 75 次（GitHub REST ~50，curl/WebFetch ~25），未 clone 任何仓库。
