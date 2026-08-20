# Archive Gap Phase 2：旧归档补回与 AI 接手说明

本轮针对 `main@ec0477976` 留下的 **148 个 Apple ID 精确缺口**继续恢复。
结论不是“148 个都已补齐”，而是：

- **114/148 已有可验证正文**，覆盖率 77.0%；
- 其中 **112 份是净新增文档、592 个 Markdown 页面**，另有 2 份是仓库内已有正文的
  `apple_id` / 标题元数据错配修复；
- **34/148 仍未恢复**，没有用现代 DocC 跳转页、404 页面或空壳内容凑数；
- 仓库总量由 **5,071 份 / 39,496 页**更新为 **5,183 份 / 40,090 页**。

机器可读的完整输入和逐条来源分别在：

- [`ARCHIVE_GAP_PHASE2_INPUT.json`](ARCHIVE_GAP_PHASE2_INPUT.json)
- [`ARCHIVE_GAP_PHASE2_SOURCES.json`](ARCHIVE_GAP_PHASE2_SOURCES.json)
- [`ARCHIVE_GAP_PHASE2_ASSETS.json`](ARCHIVE_GAP_PHASE2_ASSETS.json)

## 已恢复来源构成

| 状态 | 文档数 | 说明 |
|---|---:|---|
| `staged-html` | 83 | Apple Archive 原页或同 URL 的 Wayback 历史快照 |
| `restored-html` | 7 | Apple 旧帮助站、知识库或非标准 Archive HTML |
| `restored-pdf` | 7 | Apple 原始 PDF 或其 Wayback 快照 |
| `restored-mirror-html` | 10 | 固定提交的 ADC 2009 镜像 HTML / Sample Code |
| `restored-mirror-pdf` | 5 | 固定提交的 ADC 2009 镜像 PDF |
| `restored-alias-metadata` | 2 | 正文原已存在，仅修复相邻记录的错误元数据 |
| **合计** | **114** | 112 份净新增，2 份元数据修复 |

来源优先级固定为：

1. Apple 当前仍能返回的原 Archive HTML/PDF；
2. Internet Archive 对同一个历史 URL 的快照；
3. 固定到提交 `40bbfb75fbca44be17a305321eaee3ab8382572b` 的
   [`cellularmitosis/ADC-reference-library-2009-july`](https://github.com/cellularmitosis/ADC-reference-library-2009-july)
   镜像；
4. 无法验证时保持 `unresolved`。

镜像恢复条目仍把 frontmatter 的 `source_url` 写为原 Apple URL；镜像仓库、提交、
相对路径、SHA-256（适用时）单独记在来源 JSON 中，不能把镜像误写成 Apple 在线来源。

### 非正文资源审计

本轮对正文中的 969 个唯一配图文件额外做了文件头校验，避免把 Apple 404 HTML 当成
`.png` / `.jpg` / `.gif` 提交。当前结果为：

- `valid-existing` 208 个：抓取产物原本就是有效图片；
- `recovered` 116 个：通过页面对应的 Wayback 时间点重新恢复；
- `unavailable` 20 个：13 个 Watch 配图已确认无图片快照，另 7 个回放返回非图片内容；
- `network-error` 625 个：Wayback 传输层错误，**只能记为待重试，不能算确认缺失**。

无效伪图片已删除。Markdown 分别用“原归档配图未能恢复”和“原归档配图获取待重试”
替代坏图链接；不能把现代 DocC 截图、重绘图或无来源图片冒充原件。逐文件状态和最后一次
请求错误见资产审计 JSON。

## 仍缺的 34 份

### Wayback 只剩现代 DocC 跳转或没有旧快照（29）

- `DTS10004300` — vDSP Examples
- `DTS10004441` — SourceView: Using NSOutlineView with NSTreeController
- `DTS40007710` — UIKit Catalog (iOS)
- `DTS40009745` — Best Practices for Creating and Deploying HTTP Live Streaming Media
- `DTS40010112` — AVCam-iOS
- `DTS40011365` — PrefsInCloud
- `DTS40012713` — Understanding the EXT-X-VERSION tag
- `DTS40013332` — MapSearch
- `DTS40015177` — CFNetwork Diagnostic Logging
- `TP40014630` — MetalDeferredLighting
- `TP40014683` — Table Search with UISearchController
- `TP40015048` — HomeKit Catalog
- `TP40015064` — Apple TV Markup Language Reference
- `TP40015408` — Apple News Format Reference
- `TP40015409` — Apple News API Reference
- `TP40016265` — Safari Content-Blocking Rules Reference
- `TP40016596` — HLS Authoring Specification for Apple Devices
- `TP40016664` — Advertising Guide for News Publishers
- `TP40016784` — Apple News Format: Design Tutorial
- `TP40017290` — Speakerbox
- `TP40017313` — Metal Heaps And Fences
- `TP40017319` — Safari App Extension Programming Guide
- `TP40017320` — HLS Catalog
- `TP40017329` — Ice Cream Builder
- `TP40017333` — SpeedSketch
- `TP40017387` — Mobile Device Management Protocol Reference
- `TP40017495` — Search Ads API Reference
- `TP40017556` — AVCamPhotoFilter
- `TP40017580` — CloudKit Share

### Apple/Wayback 均为 404（4）

- `DTS40013190` — State Restoration
- `DTS40013589` — InfoBarStackView
- `TP40013500` — App Distribution Guide for Xcode 4
- `TP40016785` — Apple News Format: Advanced Design Tutorial

### 原 PDF URL 已跳到普通 HTML，未找到 PDF 快照（1）

- `TP40002029` — OS X Server Glossary

以上口径以来源 JSON 为准。今后找到新来源时，只能在核对 Apple ID、标题、历史 URL、
内容身份和文件类型后改变状态。

## 可复现流程

使用 Python 3.11 或更高版本。主要依赖为 `requests`、`beautifulsoup4`、
`markdownify==1.1.0`、`PyYAML`、`pypdf`；可在虚拟环境中安装，不能把本机绝对路径、
缓存或凭据写入仓库。

```bash
# 第一来源与 Wayback 恢复
python3 tools/archive_gap_phase2.py recover
python3 tools/archive_gap_phase2.py render
python3 tools/archive_gap_phase2.py repair-assets --workers 3
python3 tools/archive_gap_phase2.py install
python3 tools/archive_gap_phase2.py report

# 只重试 unresolved
python3 tools/archive_gap_phase2.py recover --retry-unresolved

# ADC 2009 镜像补救（镜像必须处于上文固定提交）
python3 tools/archive_gap_mirror_import.py --mirror-root /path/to/ADC-reference-library-2009-july
```

索引生成器位于 `tools/indexes/`。它先用 5,071 份基线文档重建现有索引并要求字节一致，
再插入 112 份新文档；既有中文标题和既有条目顺序不重排。

```bash
python3 tools/indexes/inv.py . /tmp/phase2-old.json
python3 tools/indexes/build_new.py \
  . \
  .staging/archive-gap-cache/_state/plans.json \
  doc/ARCHIVE_GAP_PHASE2_SOURCES.json \
  /tmp/phase2-old.json \
  /tmp/phase2-new.json

# 先不加 --write，确认基线重建差异数均为 0
python3 tools/indexes/buildtype.py \
  . /tmp/phase2-old.json doc/ARCHIVE_GAP_PHASE2_EMPTY.json
python3 tools/indexes/buildidx.py . /tmp/phase2-old.json

# 然后才允许写入 phase2 索引
python3 tools/indexes/buildtype.py . /tmp/phase2-old.json /tmp/phase2-new.json --write
python3 tools/indexes/buildidx.py . /tmp/phase2-old.json \
  --with-new /tmp/phase2-new.json --write
python3 tools/indexes/buildroot.py . /tmp/phase2-old.json /tmp/phase2-new.json --write
```

索引脚本面向 `ec0477976` 的 phase2 基线，不能在已经写过索引的工作树里重复把同一批
新文档再加一次。

## 后续接手计划

| 工作流 | 当前状态 | 下一步 | 完成标准 |
|---|---|---|---|
| 148 个旧归档缺口 | 114 已恢复，34 未恢复 | 继续寻找 34 份精确历史来源 | Apple ID、标题、历史 URL 和内容身份均可验证 |
| 已恢复文档附件 | 324 有效，20 确认不可用，625 待重试 | 先重试传输错误，再找确认缺失的原文件 | 文件头有效，来源与页面版本一致 |
| 本轮新增原文 | 112 份、592 个 Markdown 页面 | 进入独立翻译批次 | 原文不被覆盖，译文风格与仓库一致 |
| 翻译与审校 | 本轮新增尚未翻译 | 翻译后由另一人独立审校 | 术语、代码、链接、frontmatter 和分页均通过 |
| 机械校验 | `validate_archive_gap_phase2.py` 已建立 | 每次改动后重复运行 | 输出 `PASS`，并通过 `git diff --check` |
| Git 交付 | 仅允许功能分支和 PR | 提交给仓库所有者审核 | 执行者不推 `main`、不自行合并 |
| 338 个学习链接 | 不在本仓库范围 | 不纳入完成率 | 不作为抓取或翻译欠账 |

### A. 继续寻找 34 个英文原文

1. 优先搜索 Apple 官方旧下载包、旧 Xcode Sample Code 包和 Apple 自有 PDF 域名；
2. 再查 Internet Archive 的精确 URL、HTTP/HTTPS/旧主机名变体；
3. 镜像只能使用固定提交，并在来源 JSON 中记录仓库、提交、路径和哈希；
4. 现代 DocC 可以作为“新版本参考”，但不能登记为已恢复的 Archive 旧版本；
5. 每找到一份，先更新来源审计，再转换、校验、重建索引。

### B. 翻译协作

旧归档回填和中文翻译是两条独立任务。回填完成并不代表已翻译；新增的 112 份目前仍是英文原文。
翻译继续以 `TRANSLATION_PLAN*.md` 为任务清单，并严格执行：

> 翻译 → 独立审校 → 机械校验 → 提 PR → 由仓库所有者审核合并

- 从最新 `main` 建功能分支；
- 保持既有术语、标题、frontmatter、导航、分页和 Markdown 风格一致；
- 一个 PR 只处理明确领取的一批文档；
- 执行者只能提 PR，禁止直接推送 `main`，禁止自行合并。

### C. 与“338 个学习链接”的关系

338 个链接属于外部学习计划的导航/阅读清单，不是本仓库的抓取种子、完整性分母或翻译欠账。
判断本仓库英文原文是否齐全，只看 Apple Archive 清单、Apple ID 和本报告的来源审计。

## PR 审核清单

- [ ] `ARCHIVE_GAP_PHASE2_SOURCES.json` 中每个新增条目都有来源和状态
- [ ] 不包含现代 DocC 冒充旧 Archive 的页面
- [ ] PDF 以 `%PDF` 开头，原件位于 `attachments/original.pdf`
- [ ] frontmatter 恰好 9 个键且顺序一致
- [ ] 每个新增 Apple ID 唯一，未制造相邻 ID 丢失
- [ ] 导航深度、分页链接、图片相对路径通过机械校验
- [ ] 资产审计区分有效、确认不可用和网络待重试，没有把传输错误写成确认缺失
- [ ] 没有把无来源图片、现代 DocC 截图或 HTML 错误页冒充原归档配图
- [ ] 索引中的 112 个新文档和 592 个页面均可打开
- [ ] README 统计为 5,183 份 / 40,090 页
- [ ] 只提交本任务文件，没有 `.staging/`、缓存、token 或临时文件
- [ ] 只创建 PR，不直接合并
