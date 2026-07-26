# Apple Documentation Archive 缺口侦察报告

- 侦察日期：2026-07-26
- 目标 vault：`/Users/tommywu/Desktop/翻译/vault`（只读，本次未写入、未执行任何 git 操作）
- 官方清单：`https://developer.apple.com/library/archive/navigation/library.json`（`Last-Modified: Fri, 30 Jan 2026 23:15:32 GMT`，1,348,294 字节）
- 缺口清单产物：`archive_gap.json`（1,098 条）
- 实际网络请求总数：**59**（在 60 上限内），每个请求间隔 1 秒

---

## 0. 结论速览

| 结论 | 内容 |
|---|---|
| 缺口总数 | **1,098** 份逻辑文档（library.json 5,219 − vault 4,121） |
| 最大单一缺口 | **Technical Notes 810 份，vault 收录 0 份，缺口率 100%** |
| 好消息 | 810 份 Technical Notes **全部仍在线**，HTTP 200、零重定向、服务端完整渲染 HTML |
| 坏消息 | Guides / Technical Q&As 缺口中的现代文档已被 Apple **301 迁移到新版 `/documentation/`**，归档 HTML 已不存在，新版是 JS 空壳 |
| 预估 HTML 页面数 | **约 2,500 – 3,300 页**（详见第 5 节） |
| 反爬 | robots.txt 未禁止 `/library/archive/`，无 Crawl-delay，无 Cloudflare，无 UA 校验（`Server: Apple` + Akamai CDN） |

---

## 1. type 数字码映射：**issue 的描述完全正确**

不需要靠 URL 前缀推测——`library.json` 自己就带着权威映射表，在 `topics[1]`（`"name": "Resource Types"`, `"id": "topic_group_0"`）里：

```
{'name': 'Articles',          'id': 'resourceType_12', 'key': '12'}
{'name': 'Getting Started',   'id': 'resourceType_9',  'key': '9'}
{'name': 'Guides',            'id': 'resourceType_3',  'key': '3'}
{'name': 'Release Notes',     'id': 'resourceType_7',  'key': '7'}
{'name': 'Sample Code',       'id': 'resourceType_5',  'key': '5'}
{'name': 'Technical Notes',   'id': 'resourceType_2',  'key': '2'}
{'name': 'Technical Q&As',    'id': 'resourceType_6',  'key': '6'}
{'name': 'Xcode Tasks',       'id': 'resourceType_15', 'key': '15'}
```

用 URL 路径前缀做的独立交叉验证也一致（每个 type 的 URL 前缀分布）：

| type | 名称 | 总数 | URL 前缀分布 |
|---|---|---|---|
| 5 | Sample Code | 1952 | `samplecode/` 1951, `LucidDreams/` 1 |
| 6 | Technical Q&As | 1519 | `qa/` 1519（100%） |
| 2 | Technical Notes | 810 | `technotes/` 809, `releasenotes/` 1 |
| 3 | Guides | 689 | `documentation/` 650, `referencelibrary/` 17, `featuredarticles/` 6, 其他 16 |
| 7 | Release Notes | 222 | `releasenotes/` 213, `documentation/` 6, 站外 3 |
| 9 | Getting Started | 22 | `referencelibrary/GettingStarted/` 22（100%） |
| 15 | Xcode Tasks | 3 | `recipes/`（`xcode_help-*`，确为 Xcode 帮助任务） |
| 12 | Articles | 2 | `featuredarticles/`（`StaticAnalysis`、`DoxygenXcode`） |

**额外发现的 schema 细节**（写抓取器时有用）：

- `topic` / `subtopic` 列是整数 **key**，需要查 `topics[2]`（`topic_group_52` = Topics）的 `contents[].key → name`；`subtopic` 是 `parent` 指向 `topic` 的子项。
- `framework` 列的 key 查 `topics[3]`（`topic_group_53` = Technologies），对应 vault frontmatter 的 `technology` 字段。
- `updateSize` 列是下标，查顶层 `updateSize` 数组：`['First Version','Content Update','Minor Change','']`。
- `release` 列在本次快照里恒为无意义值（顶层 `release` 只有 `{'0': ''}`）。
- 所有名称字段是 **HTML 转义过的**（`Technical Q&amp;As`、`&quot;New&quot; cdev Messages`），必须 `html.unescape`。

---

## 2. 匹配规则与缺口计算

### 2.1 先搞清 vault 的页面/文档关系

遍历 vault 全部 `.md`（跳过 `.git`、`.obsidian`）：

- 35,884 个 `.md` 文件
- 其中 **35,752 个带 YAML frontmatter**，132 个没有（`README.md` + `_indexes/**` 索引页，非内容页）
- **35,752 个页面 → 35,752 个互不相同的 `source_url`**（每页一个自己的 URL，不是共享前缀）
- **4,121 个互不相同的 `apple_id`** ← 这就是逻辑文档数，与 README 声明一致

结论：**`apple_id` 是文档级主键，`source_url` 是页面级主键**。同一份文档的所有页面共享 `apple_id`，各自有独立 `source_url`，例如：

```
documentation/Cocoa/Blocks Programming Topics/Blocks and Variables.md
  apple_id: TP40007502
  source_url: .../documentation/Cocoa/Conceptual/Blocks/Articles/bxVariables.html
documentation/Cocoa/Blocks Programming Topics/Conceptual Overview.md
  apple_id: TP40007502
  source_url: .../documentation/Cocoa/Conceptual/Blocks/Articles/bxOverview.html
```

vault 每页页数分布：min 1 / median 3 / mean 8.68 / max 1473（`WebObjects 4.5 Developer Documentation`）。

### 2.2 主匹配键：`apple_id`（推荐）

`library.json` 的 `id` 列与 vault frontmatter 的 `apple_id` 是同一命名空间：

```
library.json id 共 5219 个，全部唯一，无重复
vault apple_id 4121 个
vault ∩ library = 4121   ← 100% 命中
vault 有但 library 没有 = 0
library 有但 vault 没有 = 1098   ← 缺口
```

**4,121/4,121 全部命中、0 漏配、0 误配。** 这比 URL 匹配干净得多，建议抓取器直接用 `apple_id` 做去重/断点。

### 2.3 URL 匹配规则的抽样验证（按任务要求）

规范化规则：

```python
def norm(u):
    u = urljoin('https://developer.apple.com/library/archive/navigation/library.json', u)  # 相对 → 绝对
    u = u.split('#')[0]                          # 去锚点 #//apple_ref/doc/uid/...
    u = re.sub(r'^http://', 'https://', u)       # 协议归一
    u = re.sub(r'/(_index|index)\.html$', '/', u) # 去 _index.html / index.html
    return u.lower()                             # 仅用于比对，不可用于请求
```

- **20 条已收文档抽样：命中 20/20（100%）**
- 全量：4,121 份已收文档中 4,117 份（**99.9%**）的清单入口 URL 精确命中某个 vault 页面 URL
- 4 份漏配（false negative）：清单入口是目录形式，而 vault 只存了章节页，没存 landing 页。例如
  - `TP40000999` 清单 `.../webobjects/developing_smil_presentation/`，vault 只有 `.../reference/wosmilheadmeta.html` 等
  - `TP40013837`、`TP40014323`（Start Developing iOS Apps Today）同理
- 0 份误配（url 命中但 id 不在 vault）

**URL 匹配的 2 个坑（已实测）：**

1. **library.json 里存在别名条目**：2 份"缺口"文档的入口 URL 其实已被 vault 收录，但归属另一个 `apple_id`：
   - `DTS10002175` "Playing Compressed WAVE files…" → `qa/snd/snd08.html`，vault 里该 URL 归 `DTS10002174`
   - `DTS10001488` "What Does Extension Manager Turn Off?" → `qa/ops/ops07.html`，vault 里该 URL 归 `DTS10001487`
   - 这 2 条在 `archive_gap.json` 里已用 `"url_already_in_vault": true` 标记。
2. **URL 大小写敏感，不能拿 lower() 去请求**。实测：
   - `.../samplecode/softvdig/Introduction/Intro.html` → **200，0 次重定向**
   - `.../samplecode/softvdig/introduction/intro.html` → **200，但 2 次重定向**（服务器纠正大小写）
   - 抓取时必须用 `library.json` 的原始大小写，否则每页多消耗 2 个请求。

**建议**：`apple_id` 作主键做差集，`norm(url)` 作二次校验并标记别名冲突。`archive_gap.json` 已同时给出 `url`（原始大小写，可直接请求）和 `url_normalized`（仅比对用）。

---

## 3. 缺口统计

### 3.1 按 type

| type_code | 名称 | library | vault | **缺口** | 缺口率 |
|---:|---|---:|---:|---:|---:|
| 2 | **Technical Notes** | 810 | **0** | **810** | **100.0%** |
| 5 | Sample Code | 1952 | 1761 | 191 | 9.8% |
| 3 | Guides | 689 | 617 | 72 | 10.4% |
| 6 | Technical Q&As | 1519 | 1500 | 19 | 1.3% |
| 7 | Release Notes | 222 | 217 | 5 | 2.3% |
| 9 | Getting Started | 22 | 21 | 1 | 4.5% |
| 15 | Xcode Tasks | 3 | 3 | 0 | 0% |
| 12 | Articles | 2 | 2 | 0 | 0% |
| | **合计** | **5219** | **4121** | **1098** | **21.0%** |

`vault` 列的 `resource_type` 只有 4 种标签（Sample Code / QA / Guide / Release Note），说明原抓取器把 `referencelibrary`、`featuredarticles`、`recipes` 都归到了 Guide，而 **`technotes/` 这个目录在 vault 里根本不存在** —— 810 份 Technical Notes 是整类缺失，不是零散遗漏。这强烈提示原抓取器的种子列表压根没包含 `technotes/` 路径。

### 3.2 按 URL 路径前缀（缺口）

```
technotes         811
samplecode        191
documentation      56
qa                 19
http:  (站外)      11
releasenotes        6
referencelibrary    2
https: (站外)       1
featuredarticles    1
```

### 3.3 按 type × 平台（缺口，仅列 ≥5 的平台列）

| type | macOS | iOS | Xcode Dev Tools | iOS\|macOS | tvOS\|iOS\|macOS | watchOS\|iOS\|macOS | 其他 | 合计 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Technical Notes | 682 | 31 | 41 | 22 | 4 | 3 | 27 | **810** |
| Sample Code | 147 | 30 | 0 | 4 | 2 | 2 | 6 | **191** |
| Guides | 23 | 12 | 9 | 3 | 5 | 4 | 16 | **72** |
| Technical Q&As | 4 | 9 | 0 | 3 | 0 | 0 | 3 | **19** |
| Release Notes | 5 | 0 | 0 | 0 | 0 | 0 | 0 | **5** |
| Getting Started | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| **合计** | **862** | **82** | **50** | **32** | **11** | **9** | **52** | **1098** |

平台字段共出现 31 种组合（含 `iAd System JS|…`、`Safari (Mobile)` 等长尾）。缺口高度集中在 **macOS（862，78.5%）**——因为绝大多数 Technical Notes 是 Classic Mac OS / Carbon 时代的历史文档。

### 3.4 按 topic

749 条（68%）的 `topic` 为空，几乎全是 Technical Notes——归档系统没给 technotes 打 Topic 标签（它们只有 `book-assignments: {Type/Technical Note}`）。非空 topic 前几名：Audio/Video & Visual Effects 62、Cross Platform 36、Data Management 35、User Experience 33、General 32、Graphics & Animation 28、Xcode 26。

### 3.5 按发布年份（缺口）

跨度 **1985–2018**。峰值：1990(112)、2000(133)、2003(145)、2016(46)、2017(45)、2018(32)。

按"新旧"切分（这个切分直接决定可抓性，见第 4 节）：

| type | ≤2013（老，归档仍在） | 2014+（新，大概率已迁走） | 合计 |
|---|---:|---:|---:|
| Technical Notes | 731 | 79 | 810 |
| Sample Code | 142 | 49 | 191 |
| Guides | **28** | **44** | 72 |
| Technical Q&As | 6 | 13 | 19 |
| Release Notes | 5 | 0 | 5 |
| Getting Started | 0 | 1 | 1 |
| **合计** | **912** | **186** | **1098** |

---

## 4. 可抓性验证（实测 curl 证据）

UA 统一用 `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) … Chrome/120.0.0.0 Safari/537.36`，`-L --max-redirs 5/6`，每请求间隔 1 秒。

### 4.1 Technical Notes（810，缺口最大）→ 完全可抓 ✅

10 条抽样（5 条现代 `tnNNNN`、5 条 legacy `XX/xx_NN.html`）+ 6 条正文抓取，**全部 200、`nred=0`、`Content-Type: text/html`**：

```
tn_tb15  200|0|.../technotes/tb/tb_15.html      |17206|text/html
tn_ov03  200|0|.../technotes/ov/ov_03.html      |23920|text/html
tn_pr07  200|0|.../technotes/pr/pr_07.html      |12910|text/html
tn_1195  200|0|.../technotes/tn1195/_index.html |92504|text/html
tn_2258  200|0|.../technotes/tn2258/_index.html |23524|text/html
tn_2413  200|0|.../technotes/tn2413/_index.html |82466|text/html
TN_modern DTS10002935 :: 200|nred=0|.../technotes/tn/tn1095.html|39096
TN_modern DTS10002878 :: 200|nred=0|.../technotes/tn/tn1036.html|31685
TN_modern DTS40016603 :: 200|nred=0|.../technotes/tn2420/|1610      ← 见下方警告
TN_modern DTS10002851 :: 200|nred=0|.../technotes/tn/tn1009.html|30198
TN_modern DTS10002939 :: 200|nred=0|.../technotes/tn/tn1099.html|20397
TN_legacy DTS10002616 :: 200|nred=0|.../technotes/ov/ov_18.html|20759
TN_legacy DTS10002797 :: 200|nred=0|.../technotes/tb/tb_520.html|19114
TN_legacy DTS10002577 :: 200|nred=0|.../technotes/nw/nw_535.html|20774
TN_legacy DTS10002684 :: 200|nred=0|.../technotes/pt/pt_30.html|15141
TN_legacy DTS10002486 :: 200|nred=0|.../technotes/hw/hw_17.html|20313
```

**⚠️ 陷阱**：请求 `technotes/tn2420/`（裸目录）只返回 **1610 字节的空壳**；请求 `technotes/tn2420/_index.html` 返回 **30256 字节完整正文**。必须显式带 `_index.html`。

**内容是服务端完整渲染的**（不需要 JS）：17KB–92KB 的 HTML 里正文全在。只有 TOC 侧栏（`<nav id="tocContainer"><ul id="toc" role="tree"></ul></nav>`）和 zip 下载按钮是 JS 填的，正文不依赖 JS。

**URL 形态分布（810 份）**：

```
386  legacy  technotes/XX/xx_NN.html          (tb hw nw pt fl dv te pr ov qd me qt ic os im_errata ps cm)
207  flat    technotes/tn/tnNNNN.html
192  dir     technotes/tnNNNN/_index.html
 25  其他    technotes/tn20NN/tnNNNN.html      (如 tn2002/tn2067.html)
```

### 4.2 Sample Code（191）→ 老的可抓 ✅，2014+ 的部分已迁走 ⚠️

```
sc_softvdig  200|0|.../samplecode/softvdig/Introduction/Intro.html   | 8333|text/html
sc_scenekit  200|0|.../samplecode/scenekit-2017/Introduction/Intro.html|11816|text/html
SC DTS10000688 :: 200|.../samplecode/simpleJavaLauncher/Introduction/Intro.html|8121
SC DTS10000873 :: 200|.../samplecode/qtreadwritejpeg/Introduction/Intro.html   |8748
SC DTS10000855 :: 200|.../samplecode/qtcustombutton/Introduction/Intro.html    |8639
SC TP40017110 :: 200|nred=2|https://developer.apple.com/documentation/speech/recognizing-speech-in-live-audio|17248   ← 已迁移
```

6 条抽样中 5 条留在归档，1 条（2016 年的 `TP40017110`）已 301 迁移到新版文档。

### 4.3 Guides（72）→ **多数已迁移，最难 ❌**

6 条抽样，只有 1 条留在归档：

```
GUIDE TP40016994 :: 200|.../library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/Introduction.html|13953  ← 仍在归档
GUIDE TP40007072 :: 200|nred=1|https://developer.apple.com/documentation/uikit|17053                 ← 迁移
GUIDE TP40012026 :: 200|nred=1|https://developer.apple.com/documentation/walletpasses|16981          ← 迁移
GUIDE TP40007451 :: 200|nred=2|https://developer.apple.com/documentation/uikit/table-views|16978     ← 迁移
GUIDE TP40016265 :: 200|nred=2|https://developer.apple.com/documentation/safariservices/creating-a-content-blocker|17071 ← 迁移
GUIDE TP40015408 :: 404|nred=2|https://developer.apple.com/documentation/applenews/apple-news-format|15658  ← 迁移后 404，内容彻底没了
```

完整重定向链（`g_64bit.hdr`，`64-Bit Transition Guide for Cocoa Touch` / TP40013501）——**四级 301 链**，可见 Apple 反复搬家：

```
HTTP/1.1 301 Moved Permanently
Location: https://developer.apple.com/documentation/uikit/core_app/updating_your_app_from_32-bit_to_64-bit_architecture
HTTP/1.1 301 Moved Permanently
Location: /documentation/uikit/app_and_scenes/updating_your_app_from_32-bit_to_64-bit_architecture
HTTP/1.1 301 Moved Permanently
Location: /documentation/uikit/app_and_environment/updating_your_app_from_32-bit_to_64-bit_architecture
HTTP/1.1 301 Moved Permanently
Location: /documentation/uikit/updating-your-app-from-32-bit-to-64-bit-architecture
HTTP/1.1 200 OK
```

**落地页是 JS 空壳**：终点大小恒定在 16.9–17.6 KB，是 Swift-DocC 单页应用外壳，正文靠 `/data/documentation/....json` 异步取。用 curl 拿不到正文。

`book.json` 也一起被重定向了（`g_64bit_bookjson` 的 `url_effective` 同样落在 `/documentation/uikit/...`），所以对已迁移文档连分页清单都拿不到。

**44/72 份 Guides 是 2014+ 发布**，按抽样比例推断，这 44 份里绝大多数已迁移。名单（节选）：`App Programming Guide for iOS`、`Instruments User Guide`、`In-App Purchase Programming Guide`、`Configuration Profile Reference`、`Mobile Device Management Protocol Reference`、`QuickTime File Format Specification`、`Start Developing iOS Apps (Swift)`、`Xcode Overview`、`Debugging with Xcode`、`Apple News Format Reference` …（完整 44 条见 `archive_gap.json` 中 `type_code==3 && published>=2014`）。

### 4.4 Technical Q&As（19）→ 大部分已迁移 ⚠️

```
QA DTS40011341 :: 200|nred=2|https://developer.apple.com/documentation/xcode/diagnosing-issues-using-crash-reports-and-device-logs|17233
QA DTS40016604 :: 200|nred=2|https://developer.apple.com/documentation/spritekit/requesting-the-opengl-renderer|17140
QA DTS40014114 :: 200|nred=1|https://developer.apple.com/documentation/kernel/hardware_families/pci/implementing_a_pcie_kext_for_a_thunderbolt_device|17557
```

3/3 全部迁移。19 条中 13 条是 2014+，只有 6 条 ≤2013（其中 2 条是 1995/1996 的 legacy `qa/snd/snd08.html`、`qa/ops/ops07.html`，且这 2 条正是第 2.3 节说的别名条目——vault 其实已有该页面）。**实际值得抓的 Q&A 大概只有 3–5 条。**

### 4.5 Release Notes（5）→ 1 条已彻底 404

```
rn_hitoolbox 404|0|.../releasenotes/Carbon/HIToolboxOlderNotes.html|82988|text/html
```

注意：即使用**正确大小写**也是 404，说明 `TP40001014`（High Level Toolbox Release Notes 10.3 and earlier）的页面已被删除。返回体是 82,981 字节的 Apple 通用错误页：

```html
<title>Page Not Found - Apple Developer</title>
<h1>The page you're looking for can't be&nbsp;found.</h1>
```

**⚠️ 抓取器必须校验 HTTP 状态码**：Apple 的 404 页体积（~83 KB）比很多真实归档页还大，靠"响应体够大"判断成功会全军覆没。同时校验：`status == 200` **且** HTML 中存在 `<article id="contents"`。

另一条 `TP40004221`（QuickTime 7.1 Update Reference）3 次重定向后仍留在归档目录内，可抓。

### 4.6 站外 URL（12 条，全部高危）❌

缺口里有 12 条 URL 根本不指向 `developer.apple.com/library/archive/`：

```
type 3  TP40011382  App Store Review Guidelines            http://developer.apple.com/appstore/resources/approval/guidelines.html
type 3  TP40002023  Apple Remote Desktop Admin Guide 3.3   http://images.apple.com/server/docs/ARD_3_Admin_Guide_v3.3.pdf
type 3  TP40006825  Apple Style Guide                      https://help.apple.com/asg/mac/2013/
type 3  TP40011383  Mac App Store Review Guidelines        http://developer.apple.com/appstore/mac/resources/approval/guidelines.html
type 3  TP40002029  OS X Server Glossary                   http://manuals.info.apple.com/en_US/Mac_OS_X_Server_Glossary_v10.5.pdf
type 3  TP40004644  QuickTime 7.1 User's Guide             http://images.apple.com/quicktime/pdf/QuickTime7_User_Guide.pdf
type 3  TP40001991  Xserve RAID / RAID Admin 1.2           http://images.apple.com/server/docs/RAIDAdmin1.2_121406.pdf
type 3  TP40002019  Xserve User's Guide                    http://images.apple.com/server/docs/Xserve_User_Guide20080108.pdf
type 3  TP40012299  iAd Producer Help                      http://help.apple.com/iadproducer/mac/
type 7  TP40008111  WebObjects 5.2.1 Release Notes         http://docs.info.apple.com/article.html?artnum=75433
type 7  TP40008112  WebObjects 5.2.2 Release Notes         http://docs.info.apple.com/article.html?artnum=107649
type 7  TP40008113  WebObjects 5.2.3 Release Notes         http://docs.info.apple.com/article.html?artnum=107873
```

`images.apple.com` / `manuals.info.apple.com` / `docs.info.apple.com` 这些域名早已下线；其中 5 条是 PDF 而非 HTML。这 12 条建议直接标记 `unreachable`，不进抓取队列。

---

## 5. HTML 结构分析

### 5.1 稳定定位器：`<article id="contents">`（跨全部 type、跨两代模板）

**这是唯一需要记住的选择器。** 归档系统（`Generator: Gutenberg Static`）在 legacy 和现代模板上都用它包正文：

现代模板（tn2413）：
```html
<article id="contents" tabindex="0" role="main" class="dts_doc">
        <!-- CONTENTS -->
        <div id="pageNavigationLinks_top" class="pageNavigationLinks"></div>
        <a id="top" name="top"></a>
        <a id="INDEX" href="index.html" style="display:none;"></a>
        <a name="//apple_ref/doc/uid/DTS40016228-CH1-DontLinkElementID_2" title="Technical Note TN2413"></a>
        <div class="dtsDocNumber">Technical Note TN2413</div>
        <h1 id="pageTitle">In-App Purchase FAQ</h1>
        <p>This document provides answers to frequently asked questions about in-app purchase.</p>
        <div class="outerMiniTOC"> … <div class="nestedMiniTOC"> … </div></div>
```

Legacy 模板（tb_15，`<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">`，`<BODY>` 大写）：
```html
<article id="contents">
  <div id="technical">
    <a name="top"></a>
    <!-- top_of_header_marker_comment -->
    <!-- begin_header_information --><p><a href="http://developer.apple.com/">ADC Home</a> &gt; … </p>
      <div class="legacybox"><h1>Legacy Document…</h1></div>
    <!-- end_header_information -->
    <!-- top_of_titles_marker_comment -->
    <CENTER><table width="600" cellpadding="0" cellspacing="0" border="0">
      <tr><td align="left" scope="row"><h1>
        <div id="pagehead">Technical Note TB15</div>
        <div id="pageheadsub">&quot;New&quot; cdev Messages</div>
      </h1></td></tr></table></CENTER>
    <!-- bottom_of_titles_marker_comment -->
    <CENTER><table BORDER=0 CELLSPACING=1 WIDTH=600>…
```

### 5.2 两代模板的差异（Technical Notes 与 Guide 的对比答案）

| 维度 | Legacy technotes（`XX/xx_NN.html`，386 份） | 现代 technotes（`tnNNNN/`，`tn/tnNNNN.html`，424 份） | Guides / Sample Code |
|---|---|---|---|
| DOCTYPE | HTML 4.0 Transitional，`<BODY>` 大写 | `<!DOCTYPE html>` HTML5 | HTML5 |
| 正文容器 | `article#contents > div#technical` | `article#contents.dts_doc` | `article#contents` |
| 内部排版 | `<CENTER><table width="600">` 嵌套表格 + `<FONT>`，无语义标签 | 语义化 `<h1 id="pageTitle">` / `<p>` / `div.codesample` / `div.notebox` / `div.importantbox` / `div.tableholder` | 与现代 technotes 相同 |
| 标题位置 | `div#pagehead`（编号）+ `div#pageheadsub`（标题） | `div.dtsDocNumber` + `h1#pageTitle` | `h1#pageTitle` |
| `book.json` | **无**（`book-json` meta 缺失） | **有** | **有** |
| next/prev | **无** | 有 `<link id="next-page">`（technote 通常为空） | 有 `div.pageNavigationLinks > a.nextLink/.prevLink` |
| 页数 | 恒 1 页 | 恒 1 页（6/6 抽样 book.json 都是 1 个 section） | 多页 |
| 内容标记 | `<!-- begin_header_information -->` / `<!-- end_header_information -->` / `<!-- top_of_titles_marker_comment -->` 可用于裁掉导航噪音 | 无需裁剪，`div#legacyOuterWrapper` 是唯一噪音块 | 同 |

**结论：Technical Notes 比 Guide 简单得多**——单页、无分页导航、无 TOC 递归。代价是 legacy 那 386 份用的是 1990 年代表格排版，HTML→Markdown 转换质量会明显低于现代模板（表格嵌套、`<FONT>` 标签、图片是 `images/tnmenutop.gif` 这类布局装饰图，需要按文件名/尺寸过滤掉界面装饰图）。

### 5.3 `<head>` 里的结构化元数据（比解析正文更可靠）

现代模板的 `<head>` 直接给出了 frontmatter 所需的一切：

```html
<meta id="book-resource-type" name="book-resource-type" content="Technical Note">
<meta scheme="apple_ref" id="identifier" name="identifier" content="//apple_ref/doc/uid/DTS40016228">
<meta id="document-version" name="document-version" content="4.0.0">
<meta id="chapterId" name="chapterId" content="DTS40016228-CH1">
<meta id="date" name="date" content="2018-05-01">
<meta id="description" name="description" content="TN2413: provides answers to …">
<meta id="book-title" name="book-title" content="In-App Purchase FAQ">
<meta id="book-root" name="book-root" content="./">
<meta id="book-json" name="book-json" content="book.json">
<meta id="book-assignments" name="book-assignments" content="{Type/Technical Note}, {Technologies/Core Services Layer/StoreKit}">
<meta id="platforms" name="platforms" content="">
<meta id="resources-uri" name="resources-uri" content="../../Resources/1282">
<link id="book-index-page" rel="Start" href="index.html">
<link id="next-page" rel="Next" type="text/html" href="">
<link id="previous-page" rel="Prev" type="text/html" href="">
```

Legacy 模板也有一套（少 `book-json`、`date`、`chapterId`，多 `categories`）：
```html
<meta id="book-resource-type" name="book-resource-type" content="Technical Note">
<meta id="book-title" name="book-title" content="&quot;New&quot; cdev Messages">
<meta scheme="apple_ref" id="identifier" name="identifier" content="//apple_ref/doc/uid/DTS10002766">
<meta id="platforms" name="platforms" content="OS X">
<meta name="categories" content="Human Interface Toolbox">
<meta id="Generator" name="Generator" content="Gutenberg Static e43202ea08">
```

`book-assignments` 是 `{Type/…}, {Topic/…}, {Technologies/…}` 的三段式，可直接反解出 `resource_type` / `topic` / `technology`，**用不着回查 library.json**。

---

## 6. 多页文档的分页发现机制

### 6.1 首选：`book.json`（权威清单，一次请求拿全部页面）

`<meta id="book-json" content="book.json">` 指向 `<book-root>/book.json`。实测三例：

**Sample Code（`samplecode/softvdig/book.json`，1675 字节）：**
```json
{
  "sampleCode": "softvdig.zip",
  "shouldDisplayTOC": true,
  "uid": "DTS10000334",
  "type": "Conceptual Flow",
  "subtitle": "(Legacy)",
  "assignments": ["Type/Sample Code"],
  "version": "1.0.8",
  "isLegacyDocument": true,
  "title": "softvdig",
  "sections": [
    {"type":"chapter","title":"About softvdig","href":"Introduction/Intro.html#//apple_ref/doc/uid/DTS10000334-Intro-DontLinkElementID_2","isPart":false,"aref":"…"},
    {"type":"chapter","title":"MWPrefixRezPPC.h","href":"Listings/MWPrefixRezPPC_h.html#…"},
    {"type":"chapter","title":"softVdig.c","href":"Listings/softVdig_c.html#…"},
    {"type":"chapter","title":"softVdig.h","href":"Listings/softVdig_h.html#…"},
    {"type":"chapter","title":"softVdig.r","href":"Listings/softVdig_r.html#…"},
    {"type":"chapter","title":"Revision History","href":"History/History.html#…"}
  ]
}
```

**Technical Note（`technotes/tn2413/book.json`，494 字节）—— 单页：**
```json
{"version":"4.0.0","type":"TechNote","title":"In-App Purchase FAQ","uid":"DTS40016228",
 "shouldDisplayTOC": false, "technology":"StoreKit",
 "assignments":["Type/Technical Note","Technologies/Core Services Layer/StoreKit"],
 "sections":[{"type":"chapter","title":"In-App Purchase FAQ","href":"_index.html#//apple_ref/doc/uid/DTS40016228-CH1-DontLinkElementID_2","isPart":false}]}
```

**Guide（`documentation/Xcode/Conceptual/RN-Xcode-Archive/book.json`，118,525 字节）—— `sections` 递归嵌套：**
```json
{"assignments":["Type/Guide","Topic/Xcode"],"technology":"Xcode","type":"Conceptual Flow",
 "uid":"TP40016994","title":"Xcode Release Notes — Archive","version":"1.0.5",
 "sections":[
   {"type":"chapter","title":"Xcode Release Notes — Archive","href":"Chapters/Introduction.html#…-CH1-SW1",
    "sections":[
      {"type":"section","title":"Archive Chapters","href":"Chapters/Introduction.html#…-CH1-DontLinkElementID_1","sections":[]},
      {"type":"section","title":"Technical Support and Learning Resources","href":"Chapters/Introduction.html#…-CH1-DontLinkElementID_2","sections":[]}
    ]},
   {"type":"chapter","href":"Chapters/xc7_release_notes.html#…-CH5-SW1","sections":[ … 深度 3 嵌套 … ]},
   …6 个 chapter…
 ]}
```

**发现算法**：递归遍历 `sections[].href` → `href.split('#')[0]` → 去重 → 相对 `book-root` 解析成绝对 URL。注意 `sections` 可嵌套 3 层以上，且同一 HTML 文件会被多个 section 引用（section 只是页内锚点），所以**必须按 `#` 前的路径去重**，否则页数会虚高好几倍。

### 6.2 备选：页内 Next/Previous 链

`article#contents` 内的 `div.pageNavigationLinks`（`_top` 和 `_bottom` 各一份）：

```html
<div id="pageNavigationLinks_top" class="pageNavigationLinks">
    <a class='nextLink' rel='next' href='../Listings/MWPrefixRezPPC_h.html'>Next</a>
</div>
```

单页文档这个 div 是空的。`<head>` 里的 `<link id="next-page" rel="Next" href="">` 在 technote 上是空值，**不可靠**，请以 `a.nextLink` / `a.prevLink` 为准。

vault 里已收文档的 Markdown 也印证了原抓取器用的就是这条链（每页正文顶部保留了 `[Next](…)[Previous](…)`）。

**推荐做法**：`book.json` 为主（1 请求换全部页面清单，且带章节标题），`a.nextLink` 链式遍历作为 `book.json` 404 时的兜底（legacy 单页文档两者都不需要）。

---

## 7. 图片 / 附件 URL 规律

| 资源 | 规律 | 实测 |
|---|---|---|
| 正文插图（现代） | 页面所在目录下的 `Art/` 子目录，相对路径 | `technotes/tn1195/_index.html` 里 `<img src="Art/tn1195_001.jpg">` → `https://developer.apple.com/library/archive/technotes/tn1195/Art/tn1195_001.jpg` → **200, 3294 bytes, image/jpeg** |
| Guide 插图 | 章节页相对 `../Art/xxx.png` 或同级 `Art/` | 与 vault 现状一致（vault 存在 `attachments/` 目录，只有 png/jpg 内容图） |
| Legacy 布局装饰图 | `images/*.gif`（`tnmenutop.gif`、`tnmenubody.gif`、`closebutton.png`） | 纯界面装饰，**应过滤，不要下载** |
| 站点资源 | `<meta id="resources-uri" content="../../Resources/1282">` → CSS/JS，**不需要抓** | `Resources/1282/CSS/screen.css`、`Resources/1282/JavaScript/library.js` |
| Sample Code zip | `<book-root>/<book.json 的 sampleCode 值>` | `https://developer.apple.com/library/archive/samplecode/softvdig/softvdig.zip` → **200, 19294 bytes, application/zip** |

---

## 8. Sample Code：zip 还是 HTML？vault 现在怎么表达？

**两者都有，而 vault 只用了 HTML。**

- 归档页面（`samplecode/<Name>/Introduction/Intro.html`）是**服务端渲染的 HTML 说明页**，含 `h1#pageTitle`、`div.spec_sheet_info_box`（Last Revision / Build Requirements / Runtime Requirements 规格表）、`div.importantbox`（Retired Document 提示）、说明正文：

```html
<h1 id="pageTitle">softvdig</h1>
<div class="spec_sheet_info_box"><table cellspacing="0" class="specbox">
  <tr><td scope="row"><strong>Last Revision:</strong></td>
      <td><div class="zSharedSpecBoxHeadList">Version 1.0, 2003-08-29<br />First Version<br /></div></td></tr>
  <tr><td scope="row"><strong>Build Requirements:</strong></td><td>…</td></tr>
  <tr><td scope="row"><strong>Runtime Requirements:</strong></td><td>Carbon</td></tr>
</table></div>
<p>This sample code has been updated for QuickTime 5.0 SoftVDIG is a software-only video digitizer component. …</p>
```

- zip 下载按钮在 HTML 里是**空壳，href 由 JS 从 book.json 的 `sampleCode` 字段填**：
```html
<li id="downloadSample_button" style="display:none">
    <a id="Sample_link"><button id="Sample_button">Download Sample Code</button></a>
</li>
```
HTML 源码里 `grep '\.zip'` 结果为空 —— **必须读 book.json 才能拿到 zip 文件名**。

- **vault 里现有的 sample code 表达方式**（以 `samplecode/AccelerometerGraph/` 为例，共 12 个 `.md`）：

```
AccelerometerGraph.md                          ← Introduction/Intro.html（说明页，Next 指向 ReadMe）
ReadMe.txt.md                                  ← Listings/ReadMe_txt.html
AccelerometerGraph-AccelerometerFilter.h.md     ← Listings/AccelerometerGraph_AccelerometerFilter_h.html
AccelerometerGraph-AccelerometerFilter.m.md     ← Listings/AccelerometerGraph_AccelerometerFilter_m.html
…（每个源码文件一个 .md，来自 Listings/*.html 的语法高亮页）…
Document Revision History.md                    ← History/History.html
```

全 vault `samplecode/` 下：**0 个 `.zip` 文件、0 个 zip 链接**（`grep -rho 'https\?://[^ )"]*\.zip' samplecode/` 无输出），`attachments/` 目录只有 9 个、共 10 张 png。

**结论**：vault 的既定做法是**只抓 HTML（Intro + Listings/* 源码页 + History），不下载 zip**。补齐 191 份 Sample Code 应沿用同一策略，才能和现有 1,761 份保持格式一致。这也解释了为什么 Sample Code 平均 12.4 页/份 —— 页数 ≈ 源码文件数 + 2。

---

## 9. 工作量估算

### 9.1 页面数估算（依据：vault 35,752 页真实数据 + 6 份 technote book.json 实测）

vault 实测每份文档页数（这是最可靠的先验，因为就是同一批文档同一套模板）：

| vault resource_type | 文档数 | 页面数 | mean | 5% 截尾 mean | median | p90 | max |
|---|---:|---:|---:|---:|---:|---:|---:|
| Guide | 643 | 9,842 | 15.31 | **6.55** | 6 | 14 | 1473 |
| Sample Code | 1,761 | 21,868 | 12.42 | **9.90** | 8 | 24 | 222 |
| Release Note | 217 | 2,540 | 11.71 | **5.42** | 1 | 31 | 208 |
| QA | 1,500 | 1,502 | 1.00 | 1.00 | 1 | 1 | 2 |

mean 被 WebObjects 那几份巨型文档（1473 / 1104 / 1053 页）严重拉高，故用 **5% 截尾 mean**。

**Technical Notes 的乘数用直接证据而非先验**：抽样 6 份现代 technote 的 `book.json`（tn2058 / tn2190 / tn2235 / tn2288 / tn2328 / tn2413），**6/6 都只有 1 个 section、1 个唯一页面**；另外 386 份 legacy 和 207 份 flat 从 URL 形态就是单文件（`xx_NN.html` / `tn/tnNNNN.html`，无目录、无 book.json）。**乘数 = 1.0，置信度高。**

| type | 缺口文档数 | 页/份乘数 | 页面数 | 依据 |
|---|---:|---:|---:|---|
| Technical Notes | 810 | 1.0 | **810** | 6/6 book.json 实测 = 1 页；593/810 从 URL 形态即为单文件 |
| Sample Code | 191 | 9.9 | **1,891** | vault 1,761 份 Sample Code 截尾均值 |
| Guides | 72 | 6.55 | **472** | vault 643 份 Guide 截尾均值 |
| Release Notes | 5 | 5.42 | **27** | vault 217 份 Release Note 截尾均值 |
| Technical Q&As | 19 | 1.0 | **19** | vault 1,500 份 QA 实测 mean = 1.00 |
| Getting Started | 1 | ~50 | **50** | roadmap 类多章节文档 |
| **合计（场景 A：1098 份全部可达）** | **1,098** | | **≈ 3,270** | |

**场景 B（更现实）：扣掉已迁移/已 404 的文档。** 按第 3.5 节年份切分 + 第 4 节抽样命中率，假设 2014+ 的 Guides / Q&As / Sample Code 基本已迁移：

```
Technical Notes  810 × 1.0  =  810
Sample Code      142 × 9.9  = 1406   (只算 ≤2013 的)
Guides            28 × 6.55 =  183   (只算 ≤2013 的)
Technical Q&As     6 × 1.0  =    6
Release Notes      4 × 5.42 =   22   (扣掉已 404 的 TP40001014)
──────────────────────────────────
                            ≈ 2,430 页
```

**区间答案：约 2,400 – 3,300 个 HTML 页面**，最可能落在 **2,500 – 2,900**。

### 9.2 请求数与耗时

除页面本身，还要：
- `book.json`：约 500 次（只有现代模板需要；386 份 legacy technote 不需要）
- 图片：vault 现状是 35,752 页配 attachments 极少（samplecode 下仅 10 张），但 technotes 图片较多（tn1195 一页就 3 张）。估 **800 – 1,500 张**
- 重定向/404 探测的额外开销：约 200 次

**总请求量估计 4,000 – 5,500 次。** 按 1 请求/秒的礼貌速率 ≈ **70–90 分钟**；按 0.5 请求/秒 ≈ 2.5–3 小时。这是完全可控的规模，**不需要并发**。

---

## 10. 反爬与风险评估

### 10.1 robots.txt（全文，2026-07-26 实测）

```
# robots.txt for http://developer.apple.com/
User-agent: *
Disallow: /click/
Disallow: /cgi-bin/
Disallow: /survey/
Disallow: /temp/
Disallow: /search/
Disallow: /unsubscribe/
Disallow: /reference/

# Rules for Developer Forums
Disallow: /forums/create/question
Disallow: /forums/login
Disallow: /forums/preferences
Disallow: /forums/profile
Disallow: /forums/*?view
```

- **`/library/archive/` 未被禁止** ✅
- **无 `Crawl-delay` 指令**（自行控制在 1 req/s 即可）
- ⚠️ 注意 `Disallow: /reference/` —— 归档页面里有大量指向 `/reference/` 的历史链接，抓取器不要跟进这些链接。

### 10.2 服务端行为

- `Server: Apple`，经 Akamai CDN（`Via: … acdn/327.16648`，`X-Cache: miss, miss`，`CDNUUID: …`）
- **无 Cloudflare、无 JS challenge、无 cookie 门禁**
- **无 UA 检查**：同一个 Chrome UA 打了 59 个请求，全程没出现 403 / 429 / 验证码
- 59 个请求（含 1.3 MB 的 library.json）全部成功，**未观察到 rate limit**
- 归档页均带 `<meta name="ROBOTS" content="NOINDEX">`（legacy 是 `NOINDEX, NOFOLLOW`）—— 这是禁止搜索引擎收录，与本地归档抓取无关，但说明 Apple 把这些页当"保留但不推广"的内容

### 10.3 抓取难度分级

| 难度 | type | 数量 | 说明 |
|---|---|---:|---|
| **易** | Technical Notes（现代 `tnNNNN`） | 424 | 单页、`article#contents`、head meta 完备、book.json 确认单页。直接抓 `_index.html` 即可 |
| **中** | Technical Notes（legacy `XX/xx_NN.html`） | 386 | 抓取零风险（200/0 重定向），但 HTML→Markdown **转换质量**是主要挑战：HTML 4.0 表格排版、`<FONT>`、`<CENTER>`、装饰 GIF。需要用 `<!-- begin_header_information -->` / `<!-- top_of_titles_marker_comment -->` 注释标记裁剪，并按文件名过滤 `images/*.gif` |
| **中** | Sample Code（≤2013，142 份） | 142 | 需先取 book.json 再遍历 Listings/*，页数多（~10 页/份）但结构规整，与 vault 现有 1761 份完全同构 |
| **难** | Guides（≤2013，28 份） | 28 | book.json 递归嵌套需正确去重；个别是巨型文档（vault 里同类最大 1473 页），需要单独设上限保护 |
| **很难 / 不可行** | Guides（2014+，44 份）、Q&As（2014+，13 份）、Sample Code（2014+，49 份） | 106 | 已 301 迁移到 `/documentation/`，归档 HTML 与 book.json 都不再存在。落地页是 Swift-DocC JS 空壳（恒 ~17 KB），curl 拿不到正文。要抓只能改走 `/documentation/data/...json` DocC API，**那是另一套完全不同的数据模型和 Markdown 转换逻辑，不应混进这次任务** |
| **不可行** | 站外 URL（12 条）+ 已 404（TP40001014） | 13 | 域名下线 / 页面删除 / 是 PDF 而非 HTML |

### 10.4 最大的三个技术风险

1. **【最高】106 份现代文档已被 301 迁移到 Swift-DocC 新站，归档 HTML 彻底不存在。**
   证据：6 份 Guide 抽样 5 份迁移（含 1 份迁移后仍 404）、3 份 Q&A 抽样 3 份全迁移、`book.json` 请求本身也被重定向走。落地页体积恒定 16.9–17.6 KB 的 JS 空壳。
   影响：缺口从 1,098 实际收缩到约 **979 份可抓**（1098 − 106 已迁移 − 13 不可达）。
   缓解：抓取前先做一轮 `HEAD`（或 `curl -L -o /dev/null`）分类，把 `url_effective` 不在 `/library/archive/` 下的标为 `migrated`，单独出一份"需走 DocC API"的名单，不要在本次任务里硬啃。

2. **【高】404 伪装成成功：Apple 的"Page Not Found"页有 82,981 字节，比大多数真实归档页都大。**
   证据：`HIToolboxOlderNotes.html`（正确大小写）返回 `404` + 82,988 字节 + `<title>Page Not Found - Apple Developer</title>`。
   影响：任何"响应体够大就算成功"的启发式都会把 404 页当正文写进 vault，污染 4,121 份已有内容的同构性。
   缓解：**双重校验** —— `status_code == 200` **且** 响应 HTML 中含 `<article id="contents"`；再加一条 `<title>` 不含 `Page Not Found`。

3. **【中】URL 大小写敏感 + 裸目录返回空壳，两个坑都会静默产出错误结果。**
   证据：(a) `…/samplecode/softvdig/introduction/intro.html` → 200 但 2 次重定向纠正大小写；(b) `technotes/tn2420/` → 200 但只有 **1,610 字节空壳**，而 `technotes/tn2420/_index.html` → **30,256 字节完整正文**。
   影响：(a) 每页多 2 个请求，抓取时间翻倍并放大被限流风险；(b) 裸目录形式会写入一份"内容为空"的文档，且状态码是 200 无法靠状态码发现。
   缓解：必须使用 `library.json` 里的**原始大小写**（`archive_gap.json` 的 `url` 字段保留了原始大小写，`url_normalized` 只用于比对）；对以 `/` 结尾的 URL 强制补 `_index.html`；对正文长度设最小阈值（如 `article#contents` 内文本 < 500 字符则告警）。

**次级风险（值得记一笔）**：
- `book.json` 的 `sections` 递归嵌套且同一 HTML 被多个 section 引用，不按 `#` 前路径去重会导致页面数虚高数倍、重复抓取。
- library.json 存在 2 条别名条目（`DTS10002175`/`DTS10001488`），其入口 URL 已被 vault 用另一个 `apple_id` 收录，直接抓会产生重复内容页。已在 `archive_gap.json` 用 `url_already_in_vault: true` 标记。
- library.json 快照日期是 2026-01-30；如果 Apple 之后继续迁移，可抓比例只会更低，**越早抓越好**。

---

## 11. 产物说明：`archive_gap.json`

```json
{
  "meta": {
    "library_json": "https://developer.apple.com/library/archive/navigation/library.json",
    "library_json_last_modified": "Fri, 30 Jan 2026 23:15:32 GMT",
    "library_total": 5219, "vault_total": 4121, "gap_total": 1098,
    "match_key": "apple_id (library.json `id` == vault frontmatter `apple_id`); 4121/4121 matched, 0 unmatched",
    "type_code_map": {"2":"Technical Notes","3":"Guides","5":"Sample Code","6":"Technical Q&As","7":"Release Notes","9":"Getting Started","12":"Articles","15":"Xcode Tasks"}
  },
  "documents": [ … 1098 条，按 (type_code, name) 排序 … ]
}
```

每条 document 的字段：

| 字段 | 说明 |
|---|---|
| `name` | 文档标题（已 `html.unescape`） |
| `apple_id` | 主键，对应 vault frontmatter 的 `apple_id` |
| `type_code` / `type_name` | 数字码 + 含义（已用 library.json 自带映射表验证） |
| `platform` | 原始平台字符串（`macOS`、`watchOS\|tvOS\|iOS\|macOS` 等） |
| `topic` / `subtopic` | 已从 `topics[2]` 的 key 解析成名称 |
| `framework` | 已从 `topics[3]` 的 key 解析成名称（= vault 的 `technology`） |
| `url` | **绝对 URL，保留原始大小写，可直接请求**（含 `#//apple_ref/...` 锚点） |
| `url_normalized` | 小写去锚点去 `_index.html`，**仅用于比对，不要用来请求** |
| `url_path_prefix` | `technotes` / `samplecode` / `documentation` / … 便于分桶 |
| `published` / `display_date` | 发布日期 |
| `update_size` | `First Version` / `Content Update` / `Minor Change` |
| `url_already_in_vault` | `true` = 该入口 URL 已被 vault 以另一 `apple_id` 收录（仅 2 条），抓取前需人工确认 |

### 建议的抓取优先级

1. **P0 — Technical Notes 810 份**（100% 缺口、100% 在线、零重定向、单页、约 810 页）。收益/成本比最高，且能把 vault 从"缺一整类"补成完整。
2. **P1 — Sample Code ≤2013 的 142 份**（约 1,400 页），沿用 vault 既有"只抓 HTML 不抓 zip"策略。
3. **P2 — Guides ≤2013 的 28 份**（约 180 页）+ Release Notes 4 份 + Q&As 3–6 份。
4. **P3 / 单独立项 — 106 份已迁移到 `/documentation/` 的现代文档**，需要另写 DocC JSON API 抓取器。
5. **不抓 — 13 条站外 URL / 已删除页面**，直接在清单里标记 `unreachable`。
