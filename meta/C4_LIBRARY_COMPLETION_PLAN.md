# C4：全库补齐计划（Apple 文档三框架 + 博客全量 + WWDC 全量）

> 状态日期：2026-09-05
> 范围状态：**已批准，执行中**
> 与 C3 的关系：C3（OC 存量清零，62 篇）继续按
> [`C3_OC_CORE_PLAN.md`](C3_OC_CORE_PLAN.md) 执行；本计划范围**明确扣除 C3 承接篇目**，
> 不重复领取。

## 0. 用户裁决（2026-09-05 夜）

1. **引擎 B**：全部使用 ZCode 子代理（GLM 模型），**不调用 DeepSeek**，无 API 费用；
2. **节奏**：按优先级连夜推进，能做多少做多少；**每批完成即提交并推送**，防止中断丢失成果；
3. **objc.io 148 篇**：维持「已有 objccn 官方中文配对、不重译」裁决；
4. 优先级：先收尾 C3 在途批次，然后按 Xcode 清零 → UIKit → Foundation →（WWDC/博客后续）推进。

## 0.1 用户指令与范围

用户于 2026-09-05 指示补齐以下五块，并要求先出计划、审核后再定开工时间与方式：

1. UIKit 现行文档补齐（缺 96 篇）；
2. Foundation 现行文档补齐（缺 99 篇）；
3. Xcode 现行文档清零（缺 5 篇，现 99%）；
4. 英文技术博客 1,865 篇待译全部补齐；
5. WWDC 逐字稿 73 场全部翻译。

## 1. 精确体量（2026-09-05 实测）

| 板块 | 待译 | 字节/字符 | 说明 |
|---|---:|---:|---|
| Xcode 成篇文档 | 5 篇 | ~45,000 B | 清零即 100% |
| UIKit 成篇文档 | 96 篇 | ~627,765 B | 中位 5.8KB，最大 24.6KB |
| Foundation 成篇文档 | 99 篇 | ~167,454 B | 中位仅 1.1KB，多为集合实现短页 |
| **Apple 文档小计** | **200 篇** | **~840,000 B** | |
| WWDC 逐字稿 | 73 场 | 2,020,501 B | |
| 英文博客 | 1,865 篇 | 20,724,572 B | 含 objcio 148 篇（见 §2 排除）与 C3 承接 62 篇（见 §3） |
| **本计划净范围** | **≈1,928 项** | **≈19.8 MB** | 扣除 objcio 148 与 C3 承接 62 |

## 2. 排除与边界

- **objc.io 148 篇**：已有 objccn 正式中文配对，按 2026-07-28 裁决**不重译**，
  从 1,865 中扣除（默认维持原裁决；如你要求重译需明确推翻）。
- **C3 承接 62 篇**：mikeash/Cocoa with Love/NSHipster 中 OC 相关篇目由 C3 计划完成，
  本计划不再领取。
- 学习计划快照剩余 2 篇（W3C XML 规范、Open Data Structures）：维持明确排除。
- robots 禁止抓取的 22 个单页：维持现状，不绕过。
- 原生中文博客（onevcat、雷纯锋、ibireme 等）与 API 条目（symbol_kind 非成篇）：
  本就不在翻译范围。

## 3. 里程碑与批次

每批固定体量：**8–15 篇或 120–180K 英文字符**（沿用 NEXT_STEPS §5 控制规则），
每批一个 PR。批次划分执行时用 `tools/shard.py`/计划清单精确生成，这里定到里程碑。

| 里程碑 | 内容 | 篇数 | 体量 | 预计批数 |
|---|---|---:|---:|---:|
| M0 | Xcode 清零 | 5 | 45KB | 1 |
| M1 | UIKit 补齐（按主题分批：视图生命周期/动画/手势触摸/文本/导航与工具栏/其他） | 96 | 628KB | 6–7 |
| M2 | Foundation 补齐（多为短页） | 99 | 167KB | 3 |
| M3 | WWDC 73 场（按年份与主题分批） | 73 | 2.0MB | 6 |
| M4a | 博客小来源清零：Always Processing 3、Saagar Jha 18、Ciechanowski 20、EmergeTools 21、worthdoingbadly 31、Low Level Bits 34 | 127 | ~1.4MB | 4 |
| M4b | Meta Engineering 85 + Kreya 45 | 130 | ~1.6MB | 4 |
| M4c | NSHipster 169（扣 C3）+ Belkadan 141 | 310 | ~3.4MB | 9 |
| M4d | Cocoa with Love 133（扣 C3）+ mikeash 157（扣 C3） | 290 | ~4.6MB | 9 |
| M4e | Ole Begemann 274 + Jesse Squires 266 | 540 | ~5.6MB | 16 |
| M4f | MaskRay 256 | 256 | ~2.6MB | 8 |
| M4g | 其余长尾来源约 143 篇（执行时按来源清单核验） | ~143 | ~1.7MB | 5 |
| **合计** | | **≈1,928** | **≈19.8MB** | **≈71 批** |

里程碑顺序即推荐执行顺序：先易后难、先短后长、先清零后铺开。

## 4. 执行引擎（需你选定「怎么开工」）

| 引擎 | 说明 | 吞吐 | 费用估算 | 质量证据 |
|---|---|---|---|---|
| A. DeepSeek 流水线 | 仓库现成 `tools/deepseek_pipeline.py` + `tools/shard.py`，初译 + Pro 独立审校内置，冒烟 `--limit 3` | 历史实测 2 轮 218 篇 | 全部 ≈1,000 次调用、输入 ~12M token、输出 ~8M token，按历史价格 **≈$15–30** | `core-r03`/`core-r04` 218 篇已验收 |
| B. ZCode 子代理 | 本会话同款：并行子代理初译 + 跨上下文审校 | 8–15 篇/会话 | **0 美元** | C2 批次 8 篇已验收 |
| C. 混合（推荐） | Apple 文档短页（M0–M2，200 篇，多为公式化 DocC 页）走流水线；博客/WWDC 长文走子代理分批或流水线大分片 | — | ≈$5–10（仅 Apple 文档） | 两者皆有验收记录 |

**注意**：2026-08-02 的「不调用 DeepSeek」裁决只针对 C 类小批试点（防止恢复旧
`core-r04-all`）。本计划如选引擎 A/C，即构成对该裁决的有意扩大，需要你在批准本计划时
明确点头；旧 `core-r04-all` 分片依旧不得恢复，所有批次按新清单用全新 run-id 生成。

## 5. 每批质量门（与 C2/C3 完全一致，不因量大而降级）

1. 初译按 [`TRANSLATION_STYLE.md`](TRANSLATION_STYLE.md) 与 [`TERMS.md`](TERMS.md)；
2. 独立审校由未参与初译的上下文对照原文完成（流水线为 Pro 审校调用 + 人工抽检，
   子代理为跨上下文审校）；
3. 机械校验零问题：`validate.py --strict-identifiers`（Apple 文档另跑
   `audit_consistency.py`）、`test_validate.py`、`check_links.py`、
   `title_aliases.py check`、`indexes.py`、`studyplan.py`；
4. 每批先 `--limit 3` 冒烟（流水线）或 3 篇试点（子代理），确认后再放大；
5. 每批一个 PR，交仓库所有者审核，执行者不自行合并；
6. 只提交合格文件；Key、`.staging/`、分片、模型原始响应不进 Git。

**抽检规则（大批量新增）**：流水线批次每批人工/子代理抽查 ≥20% 译文
（标题、否定/比较/版本条件、关键术语、代码示例），抽查发现问题整批复查。

## 6. 节奏选项（需你选定「什么时候开工」）

| 节奏 | 内容 | 预计总时长 |
|---|---|---|
| 快速 | 引擎 A/C 为主，每天 2–4 批 | M0–M3 约 2–3 周；M4 约 6–10 周；**总计 2–3 个月** |
| 稳健 | 每晚一个会话推进 1–2 批（子代理为主） | **3–5 个月** |
| 混合 | Apple 文档走流水线一次跑完（约 2 周），博客按里程碑用晚间会话消化 | Apple 2–3 周；博客 2–4 个月 |

## 7. 里程碑验收

每个里程碑合并后运行全仓复验并把结果记入本文件完成记录：

```bash
python3 tools/validate.py apple-docs/zh
python3 tools/validate.py wwdc/zh
python3 tools/validate.py blogs/zh
python3 tools/audit_consistency.py apple-docs
python3 tools/audit_consistency.py blogs
python3 tools/check_links.py
python3 tools/translate_plan.py status
```

里程碑验收标准：对应板块 `translate_plan.py status` 待译清零（M0–M3）或来源清零
（M4 各子项），全仓机械校验零问题，术语一致性审计通过。

## 8. 完成记录

- **M0（Xcode 清零）**：2026-09-05 完成 4 篇（屏幕快照、宽度与设备变体、
  增强安全辅助扩展、分发签名代码），`translate_plan.py next` 确认 xcode 队列
  清零（100%）。主会话初译，独立审校待补（PR #30）。
- **M1 批 1（UIKit 前 16 篇，约 99KB）**：2026-09-05 完成。3 个并行子代理
  初译 9 篇 + 主会话初译 7 篇；两个独立子代理上下文交叉审校 16 篇，修订全部
  采纳：2 处 [高]（languages frontmatter 还原、sampleCode 页 sub 标签）、
  TERMS 违规清零（导航控制器→导览控制器、控件→控制、VoiceOver→旁白、
  document→文稿全族、picker→选择器、popover→弹出窗口）、trait 词族按
  TERMS 定为「特性」（初译提示词误写「特征」，已纠正）、页脚与导航行
  跨篇统一。`validate.py --strict-identifiers` 零问题（存量 7 个历史问题
  文件与本批无关）。
  **新增备案（建议 TERMS 定案）**：asset catalog=资源目录（与「素材目录」
  两说并存）、launch screen=启动屏幕、size class=尺寸类别、
  preservation=保留 / restoration=恢复、Guided Access=引导式访问、
  handler=处理程序、自定/自定义两形并存、轻点/点按两形并存。
- **M1 批 2（UIKit 字母序续 16 篇，约 132KB）**：2026-09-05 完成。子代理 5 篇
  + 主会话 11 篇（代理并发失败全部接管）；2 个独立子代理交叉审校，
  [中]×7 修复（动态类型统一、Auto Layout/Simulator 保留英文、picker 标注、
  视图层级结构、文稿选择器标注）、代码注释补译 40+ 条、低级润色若干。
  `validate.py --strict-identifiers` 零问题（存量 7 个历史问题文件除外）。
  **新增备案**：B1 SF Symbols 篇大模板内 XML 注释承载正文说明但校验器视其为
  代码行，补译需先调整校验器 COMMENT 规则；B2 自定/自定义；B3 sheet 保留
  英文 vs TERMS「表单」、transition=转场 vs TERMS「过渡」；B4 item=条目
  （焦点语境）/项目（集合视图语境）；点按=Mac click / 轻点=iOS tap。
