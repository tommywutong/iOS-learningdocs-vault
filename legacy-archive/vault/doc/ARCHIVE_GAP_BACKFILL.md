# Archive Gap 回填报告

> Phase 2 更新：这里记录的 148 份剩余缺口已经继续审计和补救，当前恢复
> **114/148**，仍有 **34** 份无可验证旧正文。详见
> [`ARCHIVE_GAP_PHASE2.md`](ARCHIVE_GAP_PHASE2.md) 和
> [`ARCHIVE_GAP_PHASE2_SOURCES.json`](ARCHIVE_GAP_PHASE2_SOURCES.json)。

本次补入的 798 份 Technical Note、145 份 Sample Code 等共 950 份文档（3,743 页），
是原抓取器**种子清单漏掉的分类**——`developer.apple.com/library/archive` 的
`library.json` 里本来就有它们，其中 `technotes/` 整个分类此前一份都没收。

抓取与格式核对在一个独立的私有工作仓库里完成，那边逆向出了本仓库转换器的
字节级行为（`markdownify` + BeautifulSoup 后端，以及 8 项选项和 4 条自定义
预处理），据此保证新页面与既有 35,884 页在 frontmatter、导航行、pager、
文件名 sanitize 上完全同形。本报告只保留能在本仓库内自行复核的部分：
每一项检查的样本数与不合规数、判定理由、以及移入前后的死链对比。

> 输入：950 份文档 / 3,743 页 / 1,145 张插图
> 基线：main @ 85515b558（35,884 个 `.md`）
> 索引层生成器是反推的，**先只喂旧文档重建现有索引、逐字节比对通过后**才带新文档写盘（见阶段 3）

---

## 阶段 0 · 移入前基线

| 项 | 数 |
|---|---|
| `.md` 文件 | 35,884 |
| 全部文件 | 45,244 |
| 相对链接总数 | 382,313 |
| **死链（相对链接指向的文件不存在）** | **5,964**，分布在 1,648 个文件 |
| 图片文件 | 9,355；被 `![]( … )` 引用 5,085；**孤儿 4,270（45.6%）** |

死链最集中的文件：`documentation/Apple Applications/Safari HTML Reference/Supported Attributes.md`（277 条）、
`documentation/Quick Time/QuickTime 7 Update Guide/New Functions, Data Types, and Constants in QuickTime 7.md`（206 条）。
**这 5,964 条死链是移入前就存在的，与本次回填无关。**

---

## 阶段 1 · 格式核对（3,743 个产物文件逐项比对）

校验脚本：`work/validate_staging.py` + `work/vaultlib.py`（在 scratchpad，未纳入仓库）。
每一项都给出「样本数 / 不合规数」。

### 1.1 全部通过的检查（不合规 = 0）

| 检查项 | 样本 |
|---|---|
| UTF-8 无 BOM | 3,743 |
| LF 换行（无 CR） | 3,743 |
| 有 YAML frontmatter | 3,743 |
| **frontmatter 9 键齐全且顺序固定**（`title, apple_id, resource_type, platform, topic, technology, published, source_url, archived_at`） | 3,743 |
| **frontmatter 能被 `yaml.safe_dump(sort_keys=False, allow_unicode=True)` 字节复现**（含单引号规则与 80 列折行） | 3,743 |
| **空值写成 `topic: null`（裸字面量）** | 2,101 |
| **空值写成 `technology: null`** | 2,860 |
| `published` 为 `'YYYY-MM-DD'` | 3,743 |
| `archived_at` 为 ISO8601 + 6 位微秒 + `Z` | 3,743 |
| `title` 从不用双引号 | 3,743 |
| `platform` token 全部在旧仓库的 11 个已知 token 内 | 3,743 |
| `platform` 书写顺序符合 §1.3 的全序 | 3,743 |
| `source_url` 前缀为 `https://developer.apple.com/library/archive/` | 3,743 |
| 导航行紧接 frontmatter、前缀 `> 导航：` | 3,743 |
| 导航行段数 ∈ {2, 3}（从不 4 段） | 3,743 |
| **`../` 深度 == 路径目录层数**（两段各自校验） | 3,743 × 2 |
| 第二段标签 == 顶层目录名（英文，不写「文档」） | 3,743 |
| 第三段标签 == 本页 frontmatter `title` | 2,793 |
| 第三段链接 == 同目录入口页且文件存在，且 == 抓取清单的 `rels[0]` | 2,793 |
| 入口页/单页 2 段、其余 3 段 | 3,743 |
| nav 后紧跟两个空行 | 3,743 |
| 页首 pager 形态 `[Next]( … )[Previous]( … )`，无空格无分隔符 | 2,936 |
| 页尾 pager 与页首内容完全相同 | 2,936 |
| 有 pager 的文件以 `\n\n` 结尾 | 2,936 |
| 文件名 stem ≤ 80（含消歧后缀 ≤ 82） | 3,743（实测 max = 80） |
| 文件名不含 `sanitize()` 应剥离的字符（`_ * # < > : " / \ | ? [ ]`），例外是 HTML stem 派生名 | 3,743 |
| 文件名/目录名不以空格、`.`、`-` 结尾 | 3,743 |
| 无 Obsidian wiki 链接 | 3,743 |
| **无退化图片行（裸 `!` / `!!`）** —— 规范 §12 #12 的已知 bug 未被复现 | 3,743 |
| **无空的 GitHub alert 块** —— §12 #14 的已知 bug 未被复现 | 3,743 |
| 图片路径以 `attachments/` 开头（`attachments/` 在文档目录下一层） | 555 |
| 锚点前缀恒为 `apple-` | 99 |
| 文档目录名 == `sanitize(frontmatter title)` | 950/950 |

`_indexes/`、`README.md`、`_unindexed/index.md` 按规范不参与 frontmatter 校验。

### 1.2 不合规项 —— 逐条判断

#### (a) 相对链接的百分号编码：21 条不是 `urllib.parse.quote()` 的结果 → **旧仓库同类问题，照抄不改**

不合规的目标串：`@first` `@last` `@next` `@previous`（各 1）、`\.0`（14）、`void*`、
`repeatElement([SCNParticleSystem(`、`repeatElement(SCNAudioSource(`。
涉及 4 个文件（`documentation/Xcode/Xcode Release Notes — Archive/Xcode 7 Release Notes.md`、
`samplecode/Fox 2- SceneKit WWDC 2017 sample code/Swift-Shared-GameController.swift.md`、
`technotes/C++ Tips and Tricks for Mac OS X.md`、
`technotes/tn2002/About the Keynote 1.x XML File Format (APXL Schema)/tn2067.md`）。

**判断依据**：旧仓库有 **33 条 / 16 种**同类串，其中 `@next`（7 次）、`@previous`（5 次）与本次完全同源
（`documentation/Xcode/Markup Formatting Reference/*.md`），另有 `this,a`、`self.outputBuffer[bytesWritten...]`、
`iAd.START_EVENT,this,false`、`"menu-visible"` 等由代码文本意外构成 markdown 链接语法的串。
→ 这是 markdownify 把正文里的 `]( … )` 字面量当链接的通病，旧仓库照样有，**不修**。

#### (b) 无 pager 却以 `\n\n` 结尾：185 个 → **旧仓库同一行为，照抄不改**

产物这 185 个文件的最后一行**100% 是表格行**（`|` 开头）。
旧仓库「无 pager 且尾部 `\n\n`」共 **628 个**，其中表格结尾 **566（90%）**、普通段落 54、列表 8。
→ 转换器在表格结尾时多输出一个 `\n` 是旧仓库既有行为（规范 §3.2/§12 #4 也记录了这 566 个）。**不修**。
产物比例（185/807 = 23%）高于旧仓库（628/10,018 = 6%），原因是 legacy technote 几乎全是布局表结尾。

#### (c) 「产物内死链」7,629 条 → **全部是隔离校验的假阳性 + 移入后自然解决**

| 分类 | 条数 | 说明 |
|---|---|---|
| `../…/README.md` | 3,743 | 索引/根文件在暂存目录里不存在，移入仓库后成立 |
| `../…/_indexes/*.md` | 3,743 | 同上 |
| 其他（跨文档链接） | 139 | 大部分指向旧仓库已有页面（如 `../../Developer Tools/Testing with Xcode/About Testing with Xcode.md`），移入后成立；其中 6 条是 (a) 类伪链接 |

阶段 4 会给出移入后的真实死链数。

#### (d) 孤儿图片 753 / 1,145（65.8%）→ **旧仓库同一现象，照抄不改**

旧仓库 9,355 张图里 **4,270 张（45.6%）**同样没有任何 `![]( … )` 引用。
根因：markdownify 在表格单元格 / inline 上下文里把 `<img>` 降级为 alt 文本
（产物里表现为 `| images/tnmenutop.gif |` 这样的裸路径；旧仓库内同形态的裸图片路径共
`documentation` 2,038 处、`referencelibrary` 287、`samplecode` 89、`featuredarticles` 33、`releasenotes` 33、`recipes` 11、`qa` 11）。
legacy technote 几乎全是布局表，所以产物比例更高。**不修**——修了就与旧仓库不一致。

### 1.3 产物引入的结构性新东西（不是错，但要在索引层处理）

1. **新顶层目录 `technotes/`** —— 旧仓库 13 个顶层里没有它。798 份文档 / 799 页。
2. **第 5 个 `resource_type`：`Technical Note`（798 页）** —— 旧仓库只有 4 个
   （`Sample Code` 21,868 / `Guide` 9,842 / `Release Note` 2,540 / `QA` 1,502）。
   依据：`library.json` 的 `type_code_map` 里 `2 = "Technical Notes"`，与旧仓库把
   `"Guides"→Guide`、`"Release Notes"→Release Note` 的单数化方式一致。
   → 需要新建 `_indexes/by-type/technical-note.md`，README 的「按资源类型浏览」从 4 行变 5 行。
3. **4 个 `platform` 新组合**（旧仓库 43 种 → 47 种）：
   `Safari (Mobile)|Safari|iAd Producer|iOS|macOS`、`Safari (Mobile)|Safari|iOS`、
   `tvOS|Safari|iOS|macOS`、`tvOS|macOS`。token 集合和书写顺序都没变，主平台判定不受影响。
4. `topic` 取值 16 种，**全部落在旧仓库的 17 种之内**，没有新值。
5. `documentation/Quick Time/QuickTime 7.1 Update Reference` 的 `resource_type` 是 `Release Note`
   却放在 `documentation/` 下 —— 旧仓库同样有 218 页 `documentation/` + `Release Note` 的组合，**一致**。

### 1.4 分类层（category）规则的反推与验证

规范 §2.2 只说「分类 id 取自原 URL 第二段」，但没说**何时才建分类目录**。
用旧仓库 35,752 个 URL→路径对照反推出真正的规则：

> **URL 第二段只有在该段下的文档数 ≥ 2 时才落成分类目录；否则文档直接放在类型目录下。**

证据：旧仓库里 `documentation/CompilerTools`（1 份）、`documentation/Accessibility`（1 份）、
`documentation/2DDrawing`（1 份）、`qa/gxnew`、`qa/nw09`、`releasenotes/iPhone`（各 1 份）全部无分类层；
而 `_indexes/documentation.md`/`qa.md`/`releasenotes.md` 里**所有** 45+37+24 个分类的份数都 ≥ 2（最小值恰好是 2）。

**产物 358 个 `(顶层, URL第二段)` 组全部符合此规则**（5 个"1 份却建了分类目录"的组，其分类
`Quick Time` / `Xcode` / `qtmtb` / `Developer Tools` / `General` 都是旧仓库已存在的分类，合并后 ≥ 2，正确）。
特别地：产物把 `releasenotes/iphone/…` 放成无分类层，与旧仓库那唯一 1 份 `releasenotes/iPhone` 文档的处理**完全一致**。

`technotes/` 因此产生 **23 个分类目录**：
`cm dv fl hw ic im errata me nw os ov pr ps pt qd qt tb te tn tn2002 tn2004 tn2005 tn2006 tn2007`
（`im_errata` → `im errata` 与旧仓库 `qa/amt_pe` → `amt pe` 同规则；`tn2002…tn2007` 与旧仓库
`qa/qa2001`、`qa2005`、`qa2008` 同形）。

### 1.5 抓取覆盖率（供参考，不属于格式问题）

`archive_gap.json` 认定的缺口是 **1,098 份**，本次落盘 **950 份**（86.5%）。
差的 148 份里有 12 份 URL 本身不是 `/library/archive/`（`http:`/`https:` 前缀异常），其余为抓取失败/404。
**这是抓取阶段的缺口，不是本次回填能补的。**

---

## 阶段 2 · 移入文件

按产物里已经排好的相对路径整体复制进 worktree（`shutil.copy2`，保留 mtime）：

| 项 | 数 |
|---|---|
| 复制文件 | **4,888**（3,743 个 `.md` + 1,145 张图） |
| 与旧仓库路径冲突 | **0**（含大小写不敏感冲突 0 —— macOS 下已专门检查） |
| 复制后逐字节比对一致 | **4,888 / 4,888** |

新顶层目录 `technotes/`：799 个 `.md` + 1,143 张图，23 个分类子目录 + 105 个单页文档 + 78 个文档目录。
图片全部落在**文档目录下一层的 `attachments/`** 里（与规范 §2.7 一致），保留了原 HTML 的相对子目录
（`images/`、`Art/`、`art/` 等），共 227 个 `attachments/` 目录。

---

## 阶段 3 · 索引层

### 3.1 方法：先自证生成器，再写盘

旧仓库的索引生成器没提交，所以先按规范 §6 写了三个生成器，
**用「只喂旧文档」的方式重建仓库里现有的索引文件，与现有字节 diff**，全部一致后才带新文档写盘：

| 生成器 | 覆盖文件 | 仅旧数据重建的结果 |
|---|---|---|
| `buildidx.py`（by-type / by-platform） | 12 个 | **12 / 12 字节完全一致** |
| `buildtype.py`（`_indexes/<type>.md` 与 `<type>/<cat>.md`） | 116 个 | **116 / 116 字节完全一致** |
| `buildroot.py`（README.md） | 1 个 | **字节完全一致** |

自证过程中修正了规范里 3 处不准确/未写明的地方：

1. **§6.3 的平台分组条件**：规范把「`### <平台>（N 份）` 只在 ≥20 时出现」写在「无分类层的类型」名下，
   实测与有没有分类层无关，**只看该类型「无分类文档」的份数**：
   `qa`（539 份）和 `samplecode`（1,760 份）有 `###` 平台组，
   `documentation`（15 份）、`releasenotes`（12 份）、`featuredarticles`（7）、`recipes`（3）没有。
2. **两套标题排序键并存**：条目行按 `title.lower()` 排；
   而 `_indexes/by-platform/*.md` 里的 `## <顶层目录>` 分组标题按**原始 ASCII 序**排
   （`ApplePay_Guide` → `LucidDreams` → `documentation` …，与 README 的「按归档分类浏览」同序），
   `## <平台>` / `#### <Topic>` 标题按 `lower()` 排。用 `lower()` 排顶层会把 `LucidDreams` 排错位置。
3. **163 个已翻译中文标题的条目仍停在原英文标题的位置上**（索引先生成、后翻译）。
   复现排序必须对这些文档回退到「文档目录名 / 文件 stem」这个英文名。
   加上这条修正后 12/12 与 116/116 才字节一致 —— 这同时证明**翻译没有重排索引**。
4. **子页显示名的规则**（规范未写）：= 页面 H1 去掉 `<tag>` 与 `_` `*` 后**原样**（不折空白、不截断、`/` 保留），
   与文件名对不上时退回文件 stem。在旧仓库 30,955 条子页行上命中 30,308（97.9%）；
   未命中的 647 条全部是「H1 已翻译成中文而索引仍是英文名」加 1 处 `#` 的边角（`Dude #includes.c`）。
   本次 2,793 条新子页行**全部能用 `sanitize()` 反推回真实文件名（0 例外）**。

### 3.2 实际写出/改动的索引文件

| 文件 | 变化 |
|---|---|
| `_indexes/technotes.md` | **新建**。共 798 份文档；23 个 `## [<分类>]( technotes/<id>.md )（N 份）` + `## 文档`（183 份，按平台分 4 组：iOS 67 / Java 1 / macOS 112 / Xcode Developer Tools 3） |
| `_indexes/technotes/*.md` | **新建 23 个**：`cm(2) dv(32) fl(38) hw(44) ic(6) im_errata(5) me(14) nw(44) os(6) ov(22) pr(25) ps(3) pt(41) qd(22) qt(7) tb(44) te(31) tn(207) tn2002(13) tn2004(2) tn2005(3) tn2006(2) tn2007(2)`；≥20 份的按平台分 `##` 组 |
| `_indexes/by-type/technical-note.md` | **新建**。共 798 份（iOS 68 / Java 4 / macOS 686 / Xcode Developer Tools 40） |
| `_indexes/samplecode.md` | 1760 → **1905** 份；iOS 258→266、macOS 1479→1615、tvOS 2→3 |
| `_indexes/documentation.md` | 598 → **601**；`Quick Time` 32→33、`Xcode` 5→6、`## 文档` 15→16 |
| `_indexes/documentation/QuickTime.md`、`Xcode.md` | 各 +1 份 |
| `_indexes/releasenotes.md` | 212 → **215**；`General` 100→101、`Developer Tools` 12→13、`## 文档` 12→13 |
| `_indexes/releasenotes/General.md`、`DeveloperTools.md` | 各 +1 份 |
| `_indexes/qa.md` | 1502 → **1503**；`qtmtb` 38→39（字节数不变，只有数字变了） |
| `_indexes/qa/qtmtb.md` | +1 份 |
| `_indexes/by-type/{guide,qa,release-note,sample-code}.md` | Guide 641→646、QA 1502→1503、Release Note 217→218、Sample Code 1761→1906 |
| `_indexes/by-platform/{ios,java,macos,xcode-developer-tools}.md` | 各新增 `## technotes（N 份）` 段（macOS 687 / iOS 67 / Xcode DT 40 / Java 4，合计 798）+ 既有段内插入；`ios.md` 813 份、`macos.md` 4035、`java.md` 36、`xcode-developer-tools.md` 132 |
| `_indexes/by-platform/tvos.md` | 15 → 16 份（`## samplecode` +1） |
| `_indexes/by-platform/{cloudkit-js,safari,watchos}.md` | 不变（无新文档命中这些主平台） |
| `README.md` | 统计段与三个浏览清单重算；「按归档分类浏览」+1 行 `technotes`、「按资源类型浏览」+1 行 `Technical Note` |
| `_unindexed/index.md` | 35,052 → **38,795** 行条目（见 3.4） |

索引文件总数 **128 → 153**。

### 3.3 链接抽验

索引层（`README.md` + `_unindexed/index.md` + `_indexes/**`）共 **89,082 条相对链接**，
其中 **3,273 条指向新增的 technotes**。

- **随机抽 10 条实测目标文件存在：10/10 OK**（种子 20260727，覆盖 `_indexes/samplecode.md`、
  `_indexes/by-platform/macos.md`、`_indexes/by-type/technical-note.md`、
  `_indexes/documentation/LegacyTechnologies.md`、`_unindexed/index.md`）
- 又从「新增条目」里单独抽 10 条：**10/10 OK**（含 `technotes/im errata/…`、`technotes/tn2002/…`、
  `_indexes/technotes.md → _indexes/technotes/fl.md`）
- **索引层全量死链：8 条，全部是移入前就存在的旧行**
  （`_unindexed/index.md` 里 6 条 URL 含 `(` 被截断的、2 条 `qa/qa1429/_index.md`、`qa/qa1722/_index.md`）。
  本次新增的 3,743 条索引条目 **0 死链**。

### 3.4 `_unindexed/index.md` 的结构反推

规范 §6.6 只说它是「按标题排序的全库页面裸链接清单」，但直接按标题排会完全对不上。
实测它是**按 `resource_type` 切成 4 段**、段内按页面标题原始码位序：

```
行     5 –  9146   Guide         9,142 条（documentation 9,009 + referencelibrary 73 + featuredarticles 34 + recipes 20 + ApplePay_Guide 6）
行  9147 – 10648   QA            1,502 条
行 10649 – 13188   Release Note  2,540 条（releasenotes 2,322 + documentation 218）
行 13189 – 35056   Sample Code  21,868 条（samplecode 21,828 + LucidDreams 40）
                   合计 35,052 = 35,752 个文档页 − 700 个 _unindexed/ 自身页面
```

段内已被翻译打乱（32 个单调段，断点全部是中文标题），所以**没有重排旧行**，
而是「保留全部旧行原顺序、把新页面按英文标题插到非中文邻居之间」，并追加第 5 段 `Technical Note`。
校验：旧 35,052 行**逐行原顺序保持不变**（程序断言 True），新增 3,743 行，合计 38,795 行。

### 3.5 README 对账

| 段 | 行数 | 合计 |
|---|---|---|
| 按归档分类浏览 | 10（+`technotes`） | 5,071 |
| 按资源类型浏览 | 5（+`Technical Note`） | 5,071 |
| 按平台浏览 | 8 | 5,071 |

**23 个清单项的 `（N 份）` 与对应索引文件里的 `共 N 份文档。` 逐一核对：23/23 一致。**
`- 文档：5071 份`、`- 页面：39496 个 Markdown 文件`。
「页面」的口径按旧 README 反推确认为「全部 `.md` 减去 `_indexes/`、`README.md`、`doc/`」
（旧值 35,884−128−1−2 = 35,753，与旧 README 的 35753 完全吻合 —— 规范 §12 #17 标为「存疑，来源不明」的这个数字，
至此解释清楚了）；本次额外排除 `BACKFILL_REPORT.md`。

**153 个索引文件的内部一致性**：`共 N 份文档。` 与实际条目数（类型索引为「分类计数之和 + 无分类条目数」）
**153/153 全部相符**。

---

## 阶段 4 · 自检

### 4.1 全仓库死链对比

| | 移入前 | 移入后 | 差 |
|---|---|---|---|
| `.md` 文件 | 35,884 | **39,653** | +3,769 |
| 全部文件 | 45,244 | **50,158** | +4,914 |
| 相对链接总数 | 382,313 | **414,808** | +32,495 |
| **死链** | **5,964** | **5,988** | **+24** |

**消失的死链 0 条**（说明没有破坏任何既有链接），新增 24 条，逐条如下：

| 条数 | 文件 | 目标 |
|---|---|---|
| 14 | `technotes/tn2002/About the Keynote 1.x XML File Format (APXL Schema)/tn2067.md` | `\.0` |
| 6 | `documentation/Xcode/Xcode Release Notes — Archive/Xcode 7 Release Notes.md` | `@first` `@last` `@next` `@previous` `Overview` `Sorting` |
| 2 | `samplecode/Fox 2- SceneKit WWDC 2017 sample code/Swift-Shared-GameController.swift.md` | `repeatElement(SCNAudioSource(` 等 |
| 1 | `technotes/C++ Tips and Tricks for Mac OS X.md` | `void*` |
| 1 | `BACKFILL_REPORT.md`（本文件） | 报告里引用索引行格式时的示意串，非真实链接 |

**23 条真实新增死链（不含本报告自身那 1 条）全部是同一类**：markdownify 把正文里的 `]( … )` 字面量（代码片段、Xcode markup
文档里的 `@next` 之类）误当成 markdown 链接。**旧仓库同一类已有 33 条 16 种**
（`@next` 7、`@previous` 5、`this,a` 5、`self.outputBuffer[bytesWritten...]` 2 …），
其中 `@next` / `@previous` 与本次完全同源（都出自 Xcode markup 文档）。
→ 属于「旧仓库本身如此，照抄即可」，**没有修**。

**结论：3,743 个新页面 + 25 个新索引文件带来 32,495 条新的相对链接，其中 32,472 条可解析，
23 条不可解析且全部属于旧仓库已有的同一缺陷类别；结构性死链 0 条。**

### 4.2 最终计数

| 项 | 值 |
|---|---|
| `.md` 总数 | **39,653**（原 35,884，+3,743 页面 +25 索引 +1 本报告） |
| 全部文件 | **50,158** |
| 文档份数 | **5,071**（原 4,121，+950） |
| 页面数 | **39,496** |
| 索引文件 | **153**（原 128，+25） |
| 图片 | **10,500**（原 9,355，+1,145） |
| 归档顶层目录 | **11**（原 10，新增 `technotes/`；另有 `_indexes/`、`_unindexed/`、`doc/`） |

---

## 刻意不改的地方（连同理由）

| # | 项 | 数 | 理由 |
|---|---|---|---|
| 1 | 伪链接 `@next` / `\.0` / `void*` / `repeatElement(` | 21 处 / 23 条死链 | 旧仓库同类已有 33 条，改了才不一致（规范 §9.2 也把这类记为「漏编码」） |
| 2 | 无 pager 却以 `\n\n` 结尾 | 185 个（100% 表格结尾） | 旧仓库 628 个同样如此、其中 566 个也是表格结尾，是转换器既有行为（§3.2） |
| 3 | 孤儿图片（下载了但正文无 `![]( … )` 引用） | 753 / 1,145（65.8%） | 旧仓库 4,270 / 9,355（45.6%）同因同果：markdownify 在表格/inline 上下文把 `<img>` 降级成 alt 文本 |
| 4 | legacy 页面被压成一个巨大布局表 | technotes 的 legacy 页普遍如此 | 规范 §8.3 记录旧仓库同形（`qa/hw/A SCSI little secret/hw81.md` 是 25 列） |
| 5 | ADC 面包屑、"Legacy Document" 横幅、页尾反馈表单 | — | 旧仓库 3,528 个文件带着，抓取报告已声明保持一致 |
| 6 | README 第 3 行「文档间链接为 wiki 链接」这句错话 | 1 处 | 全库 0 个 `[[…]]`，但这是既有散文，不属于本次回填范围（规范 §12 #18） |
| 7 | `<aside>` Note 正文与 `h2.jump` 小标题被保留（比旧仓库多内容） | 抓取报告 §二 的 A、B 两条 | 规范 §12 #14 明确「已知内容丢失，不复现」；产出形态 `__Note:__ …` 旧仓库本来就有 260+ 处 |
| 8 | 旧索引里 163 个中文标题条目的位置 | 163 条 | 它们停在原英文标题的位次上；重排会产生 3 万行无意义 diff |

## 已知缺口 / 没做到的部分

1. **抓取覆盖率 950 / 1,098（86.5%）**。`archive_gap.json` 认定缺口 1,098 份，本次只有 950 份落盘；
   差的 148 份里 12 份 URL 本身不是 `/library/archive/`，其余是抓取失败/404。
   **这是抓取阶段的缺口，本次回填无法补。**
2. **子页显示名规则未 100% 逆向**：旧仓库 30,955 条子页行里有 647 条（2.1%）用我的规则推不出来，
   已确认全部是「H1 已译成中文而索引仍是英文」加 1 处 `#` 字符的处理差异
   （`Dude #includes.c` 说明 `sanitize()` 对 `#` 是**替换成 `-`** 而不是规范 §2.4 写的「删除」）。
   本次 2,793 条新子页行不受影响（全部能反推回文件名）。
3. **`resource_type: Technical Note` 是一个判断，不是从旧仓库抄来的**。
   依据是 `library.json` 的 `type_code_map` 里 `2 = "Technical Notes"`，
   与旧仓库 `"Guides"→Guide`、`"Release Notes"→Release Note` 的单数化一致；
   但旧仓库把 `"Technical Q&As"` 映射成了 `QA`（不是 `Technical Q&A`），说明这套映射并非纯机械单数化，
   所以 `Technical Note` 有可能不是原作者会选的名字。**若要改，需要同时改 798 个页面的 frontmatter
   + `_indexes/by-type/technical-note.md` 文件名 + README 一行。**
4. **未验证 Obsidian 内的实际渲染**（无 GUI 环境）。

---

## 附：两个容易看错的计数（已核对，不是 bug）

1. **`technotes/` 有 798 份文档，`Technical Note` 也有 798 份，但不是同一批。**
   - `technotes/Kiosk Mode Programming Topic/`（`TP40009080`）的 `resource_type` 是 **Guide**；
   - `releasenotes/NSFetchedResultsController- Moved objects sometimes reported as updated/`
     （`TP40009210`）的 `resource_type` 是 **Technical Note**，但按 URL 落在 `releasenotes/` 下。
   所以 `_indexes/by-type/technical-note.md` 的 iOS 组是 68 份，而 `_indexes/by-platform/ios.md`
   的 `## technotes` 段是 67 份 —— 差的那 1 份被记在 `ios.md` 的 `## releasenotes` 段里。
   旧仓库同样存在这种跨目录现象（`documentation/` 下有 218 页 `Release Note`）。

2. **`_indexes/by-type/sample-code.md`（1906）比 `_indexes/samplecode.md`（1905）多 1 份**：
   多的是 `LucidDreams/`（`resource_type: Sample Code`，独立顶层目录）。移入前也是 1761 vs 1760，同一个原因。

---

## 附：移入并生成索引后的就地复检

| 检查 | 结果 |
|---|---|
| 3,743 个新页面的导航行（前缀 + 顶层标签 + `../` 深度） | **0 不合规** |
| 新页面内的 23,003 条相对链接 | 死链 **23**（即上文那 23 条伪链接），其余全部可解析 |
| 25 个新索引文件（无 BOM / 无 CR / 以单个 `\n` 结尾 / `# 标题` 开头 / 有导航行 / 有 `共 N 份文档。`） | **25/25 合规** |
| 全部 153 个索引文件的编码与尾换行 | **153/153 合规** |
| `README.md`、`_unindexed/index.md` | 无 BOM、无 CR、单个尾换行 |
| worktree 里是否留下临时文件 | 无（校验/生成脚本都在 scratchpad，未进仓库；仓库只多了本报告） |

**未执行任何 git 命令；`/Users/tommywu/Desktop/翻译/vault` 全程未被读写。**

---

## 第二轮 · 独立复核（换一个人、换一套脚本，重新验一遍上面的结论）

> 背景：交接时被告知「阶段 2 只移进 1,514 个 md / 7 张图，阶段 3 一个字没改」。
> 实测**这个前提是错的**。上一轮并没有在写索引前被打断，它的写盘在 **07:57–07:58** 完成；
> 交接者读到的是写盘进行中的中间状态（本轮第一条 `find` 落在 07:57 前，`_indexes/` 只有 128 个文件；
> 第二条落在之后，153 个）。因此本轮的工作是**独立复核**，而不是补做。
> 复核脚本另写在 `scratchpad/work2/`（`catmap.py` / `repro.py` 等），与上一轮的 `work/` 互不复用逻辑。

### R1 阶段 2 复核：产物 100% 就位

逐文件 SHA-256 比对 `.staging/archive-gap/` 与 worktree 同相对路径：

| 类别 | 产物数 | 已在仓库且**字节相同** | 缺失 | 内容不同 |
|---|---|---|---|---|
| `.md` | 3,743 | **3,743** | 0 | 0 |
| 图片 | 1,145 | **1,145** | 0 | 0 |

- `technotes/` 顶层 **799 个 `.md`**，与 798 份 / 799 页一致，完整。
- 1,145 张图**全部**在 `attachments/` 下，且 `attachments` 在路径中的层号只有 2 或 3
  （`<顶层>/<文档>/attachments/…`、`<顶层>/<分类>/<文档>/attachments/…`）→ **恒为文档目录下一层**，符合 §2.7。
- 本轮**未写入任何产物文件**（无需补）。

### R2 阶段 3 复核：磁盘状态可从数据完整复现

不复用上一轮的 `old_docs.json`，改从**当前 5 个 `by-type` 索引**重新抽取全部文档记录
（`old` 与 `new` 靠产物路径集合区分），重建全部 153 个索引文件并与磁盘逐字节比对：

```
worktree by-type 抽出: 5071   old: 4121   new: 950
生成 153 个文件；与磁盘不一致 0 个
```

→ 磁盘上的索引层 **100% 等于生成器输出**，07:57 那次写盘完整、自洽，**没有半截文件**。
README 同样可复现（`count_pages()` 得 39,496，与文件内数字一致）。

### R3 生成器保真性：换一个基线再证一次（**这里踩到一个坑，记下来**）

上一轮的自证基线是「写盘前的 worktree」，这个基线**用过一次就没了**。
本轮改用另一处检出 `/Users/tommywu/Desktop/翻译/vault`（**只读**）当基线重证。

**坑**：该检出虽然计数/结构/顺序都是移入前状态（4,121 份 / 35,753 页），但它的**索引标签已被翻译**
（`### [数据管理]`、`## [3D 绘制]`、`- **[15 英寸 …]**`），而 worktree(main@85515b558) 是未翻译英文态。
上一轮的 `build_cat_ids()` 从 `## [<目录名>]` + `(<链接>)` 形态的行反查分类 id，在翻译态下**整体失效**
（`Data Management` 查不到 → 分类判定全部退化成 `None`），一上手就得到 6/12 不一致的假警报。
本轮改成**从路径反推**分类映射（`_indexes/<top>/<id>.md` 文件名与 `<top>/` 下真实目录名按 `[^0-9a-z]`
归一化匹配：`amt pe`↔`amt_pe`、`Data Management`↔`DataManagement` 都能对上，107/107 命中）。

修正后，把三级分类标题行里的标签归一化回英文再比：

| 索引组 | 逐字节一致 | 不一致 |
|---|---|---|
| `_indexes/<type>.md` + `_indexes/<type>/<cat>.md` | **115 / 116** | 1 |
| `by-type/*.md` + `by-platform/*.md` | **10 / 12** | 2 |
| `README.md`（旧数据 + 35,753 页） | **一致** | 0 |

3 个不一致文件（`by-type/guide.md`、`by-platform/macos.md`、`documentation/HardwareDrivers.md`）
**只差同一处**：`documentation/Hardware Drivers/` 下 5 份同名文档
（`15-inch MacBook Pro Developer Note` + `(2007)` / `(2007)-2` / `(2007)-3` / `(2008)` 后缀）的相对次序。
根因：这 5 份 frontmatter `title` 完全相同（`15-inch`/`15-Inch` 只差大小写，`lower()` 后全等）
→ 排序键相等 → 次序由稳定排序的**输入顺序**决定，不可从数据推导。
在**翻译态**基线里索引标签是中文，`eng()` 回退到目录名后键不再相等，才产生位移。
在 worktree（英文态）里键相等、稳定排序保留抽取顺序，实测这 3 个文件该处次序与基线**完全一致**
（`… -2, (2008), -3`）→ **worktree 上的输出是对的，这 3 处不是缺陷**，
但它暴露了一个隐患，见下面「隐患 2」。

### R4 索引层格式合规审计（153 个文件全量，独立重写的检查器）

| 检查项 | 结果 |
|---|---|
| 无 YAML frontmatter、首行 `# <标题>` | 153/153 |
| 第 2、4 行空行；第 3 行以 `> 导航：[总目录](` 开头 | 153/153 |
| 第 5 行严格匹配 `^共 \d+ 份文档。$` | 153/153 |
| 以单个 `\n` 结束（无尾随空行） | 153/153 |
| 文档条目行匹配 §6.2 语法（em dash / ` · ` / 全角 `，` / 可选 tech / 可选 `，N 页`） | **15,213 / 15,213** |
| 子页行匹配 `  - ` + `[<名>]` + `(<链接>)` | **33,748 / 33,748** |
| 分组标题匹配 `（N 份）` / `文档` / `其他` / `未编入索引的页面` | 全部通过 |
| 所有相对链接满足 `quote(unquote(h)) == h`（§9.2） | 全部通过 |
| 条目数 == 声明的「共 N 份文档」 | 全部通过 |
| **问题总数** | **0** |

`technotes/` 子索引的平台分组阈值独立复测：N ≥ 20 的 13 个文件**都有** `## <平台>（N 份）` 分组，
N < 20 的 10 个**都没有**，与 §6.3 的阈值 20 **无一反例**。

### R5 链接抽查（交接要求的规定动作）

- **随机 15 条**（README + 本次新建/修改的索引，seed 固定，候选 32,958 条）→ **15/15 目标文件存在**。
- 随机抽样被最大的 `samplecode.md` 主导，对新建文件覆盖不足，**另做分层 18 条**：
  README 4 / `_indexes/technotes.md` 4 / `by-type/technical-note.md` 4 / `technotes/*.md` 6
  → **18/18 存在**，且链接标签与目标 frontmatter `title` 逐条吻合
  （如 `[AEStream and Friends]` → `technotes/tn/AEStream and Friends/tn2046.md`，`title: AEStream and Friends`）。
- **合计 33/33 通过。**
- 交叉核对 README 的 23 个 `（N 份）` 与对应索引第 5 行的「共 N 份文档」：**23/23 一致**，三段各自合计 5,071。

### R6 死链复核

| | 移入前基线 | 现在 | 差 |
|---|---|---|---|
| `.md` 文件 | 35,884 | 39,653 | +3,769 |
| 相对链接 | 382,313 | 414,807 | +32,494 |
| **死链** | **5,964** | **5,987** | **+23** |

与基线死链清单做多重集差集：**新增 23 条，消失 0 条**，与上一轮结论一致
（上一轮报的 +24 里有 1 条是它自己写报告时引用索引行格式造成的示意串；
本轮把报告里所有 `]` + `(` 相邻的示意写法都改掉了，**本报告自身现在 0 死链**，所以净数回到 +23）。

23 条全部落在 4 个文件，全部是 §1.2(a) 判定的伪链接（`\.0`×14、`@first/@last/@next/@previous/Overview/Sorting`×6、
`repeatElement(`×2、`void*`×1）。**索引层（153 个 `_indexes/` 文件 + `README.md`）自身零死链**；
死链清单里唯一带 `_unindexed/index.md` 的 8 条是移入前就存在的旧行，不在本次差集内。

**「消失 0 条」的正面含义**：§1.2(c) 那 7,629 条「产物内死链」确实全是隔离校验的假阳性 ——
3,743 条 `../…/README.md` + 3,743 条 `../…/_indexes/*.md` 移入后全部成立，139 条跨文档链接也全部落地。

### R7 计数对账

| 项 | 基线 | 现在 | 增量 | 预期 | 对账 |
|---|---|---|---|---|---|
| `.md` | 35,884 | 39,653 | +3,769 | 3,743 产物 + 25 索引 + 1 报告 | ✅ |
| 图片 | 9,355 | 10,500 | +1,145 | 1,145 | ✅ |
| 全部文件 | 45,244 | 50,158 | +4,914 | 3,743+1,145+25+1 | ✅ |
| 文档页（带 frontmatter） | 35,752 | 39,495 | +3,743 | 3,743 | ✅ |
| 逻辑文档数 | 4,121 | 5,071 | +950 | 950 | ✅ |
| 索引文件 | 128 | 153 | +25 | 25 | ✅ |

> ⚠️ 数图片千万别用 `find -name '*.png'`：它**区分大小写**，会漏掉 22 个大写扩展名文件（`.PNG`/`.GIF`/`.JPG`），
> 得到 10,478 这个错数。按 `splitext().lower()` 统计才是 **10,500 = 9,355 + 1,145**。

### R8 索引改动集（独立算法重算，供 `git diff --stat` 核对）

做法：分别用「只喂旧文档」与「旧+新文档」生成两套索引，取差集。

- **新建 25 个**：`_indexes/technotes.md`、`_indexes/technotes/*.md`（23 个）、`_indexes/by-type/technical-note.md`
- **修改 18 个**：`by-platform/{ios,java,macos,tvos,xcode-developer-tools}.md`、
  `by-type/{guide,qa,release-note,sample-code}.md`、`documentation.md`、`documentation/{QuickTime,Xcode}.md`、
  `qa.md`、`qa/qtmtb.md`、`releasenotes.md`、`releasenotes/{DeveloperTools,General}.md`、`samplecode.md`
- **未受影响 110 个**
- 另加 `README.md`、`_unindexed/index.md` 两个非 `_indexes/` 文件

与上一轮 §3.2 的清单**完全吻合**。`by-platform/{cloudkit-js,safari,watchos}.md` 未变，
与 §1.3「新增 4 个 platform 组合但主平台判定不受影响」一致。

### R9 `_unindexed/` 核查（交接点名要查的项）

`_unindexed/` 下 1,498 个文件逐一 SHA-256 比对基线：**1,497 个完全未动**，无新增/删除。
只有 `_unindexed/index.md` 一个被改（35,052 → 38,795 条，+3,743）。
已验证：4 行文件头未变；**35,052 条旧行全部原样保留、相对顺序完全不变**（子序列比对 True）。

**⚠️ 需要你裁决**：交接指令要求「确认 `_unindexed/` 没有被你误动」。
本轮没动它，但**上一轮动了 `index.md`**。我**保留**了这个改动，理由：
规范 §6.6 说该文件是「按标题排序的**全库**页面裸链接清单」（基线 35,052 条 ≫ `_unindexed/` 自身 701 页，
可证它确实是全库清单），不补的话新增 3,743 页会在这里缺席。
但它超出你给阶段 3 的清单范围 —— **请确认要不要保留**。

---

## 第二轮新发现的隐患（不影响本次提交，但要知道）

1. **`build_cat_ids()` 依赖索引标签，翻译后会失效。** 见 R3。将来在已翻译的检出上重跑生成器，
   分类判定会整体退化成"无分类"，产出灾难性 diff。**建议改成 R3 里的路径反推法**（`scratchpad/work2/catmap.py`）。
2. **同名文档的排序缺显式 tie-break。** `Hardware Drivers` 下那 5 份同 title 文档现在靠
   「稳定排序 + 抽取顺序」维持次序。一旦这些索引标签被翻译成中文，重跑就会打乱它们
   （R3 已在翻译态检出上实测到）。生成器缺一个显式稳定键（如原索引行号）。

## 第二轮没做到 / 不确定的地方

1. **基线比对用的是另一处检出，不是 main@85515b558 的 git 内容。** 受「不执行任何 git 命令」约束，
   我没有读 git 对象，而是用 `/Users/tommywu/Desktop/翻译/vault` 当基线（**只读打开，全程未写入**
   —— 这一点修正上一轮报告末尾"全程未被读写"的说法：本轮**读**了它）。
   它的计数/结构/顺序是移入前状态，但索引标签已被翻译，所以 R3 的结论是
   「归一化标签后逐字节一致」，**不等于**「与 main@85515b558 原始字节一致」。
   要 100% 确证，请主会话跑一次 `git diff --stat` 复核 R8 的 25+18+2 改动集。
   （上一轮的自证基线是写盘前的 worktree，那个基线更准，但已不可重现。）
2. **新文档的子页顺序与显示名沿用上一轮的抓取清单**（`work/new_docs.json` ← `plans.json` 的 `rels`）。
   我验证了它们指向的文件都存在、显示名 `sanitize()` 后能回到文件名，
   但**没有回到原始 HTML 重新推导一遍顺序**。§6.2 明确子页顺序不是 pager 顺序，无法从产物反推。
3. **`resource_type: Technical Note` 这个命名判断本轮未复核**，沿用上一轮的推理（见「已知缺口」第 3 条）。
4. 未验证 Obsidian 内的实际渲染（无 GUI）。
5. **全程未执行任何 git 命令**；未写入 `/Users/tommywu/Desktop/翻译/vault`。

---

## 附：本 worktree 存在并发写入者（下一个接手的人务必先读这条）

复核期间实测到**至少一个其它进程在同时改这个 worktree**，本轮被它影响了三次：

1. **07:57–07:58** —— 上一轮的索引写盘。本轮第一条 `find` 读到 `_indexes/` 只有 128 个文件、
   第二条读到 153 个；`scan.py` 先报 `_indexes: 128` 后报 `153`。
   交接说明里「只移进 1,514 个 md / 7 张图、索引一个字没改」就是这个中间状态造成的误判。
2. **07:58** —— 报告正文（阶段 2/3/4）被追加进当时的 `BACKFILL_REPORT.md`。
   本轮最初读到的是只有阶段 0/1 的 153 行版本，因此一度重复写了一遍阶段 2/3/4（已删除去重）。
3. **08:18** —— `BACKFILL_REPORT.md` 被移动/改写为 `doc/ARCHIVE_GAP_BACKFILL.md`（正文同时润色过开头）。
   本轮 08:19 的追加因此在仓库根重建了一个只含「第二轮」章节的 `BACKFILL_REPORT.md`。
   **已把该章节并入本文件，并删除了那个残留文件**，仓库根现在没有 `BACKFILL_REPORT.md`。

**因此「页面数」的排除口径也跟着变了**：从「排除 `_indexes/` + `README.md` + `doc/` + `BACKFILL_REPORT.md`」
变成「排除 `_indexes/`（153）+ `doc/`（3）+ `README.md`（1）」。
两种口径的结果**都是 39,496**（39,653 − 153 − 3 − 1），与 README 里的数字一致 —— 已实测复核通过。

> **给下一个人的建议**：动这个 worktree 前先 `ls -la --time-style=full-iso` 看一遍 mtime，
> 或者干脆确认没有其它会话在跑。本轮所有结论都是在 **08:19 之后**重新测一遍才写下的
> （最终态：`.md` 39,653、死链 5,987、页面 39,496、索引 153），
> 08:19 之前的中间读数已全部作废。
