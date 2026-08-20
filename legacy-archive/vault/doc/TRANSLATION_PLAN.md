# iOS / Cocoa 文档翻译计划

> 关联计划：Windows Views 分类（8 份文档、51 页）的翻译计划单独维护在 `doc/TRANSLATION_PLAN_WINDOWS_VIEWS.md`。

## Context

`Apple Developer Archive Vault`（已发布在 `XiyouMobile3G-iOS/apple-developer-archive-vault` 公开仓库，`main` 分支为标准 Markdown 可读版）目前只有导航层（`README.md`、`_indexes/` 下的索引文件）是中文结构文字，正文全部是英文原文，一字未译。

用户计划先把"目录层"（索引/导航文件）整体中文化，再重点翻译 iOS 平台下 Cocoa 分类的 40 份文档（共 344 个页面，含各文档内部的嵌套子页面），边译边顺手修正翻译中发现的代码块缺失语言标注、表格错位等历史遗留格式问题。翻译采用原地替换（不保留双语、不建镜像目录），但由于 vault 是 git 仓库、且 `obsidian` 分支和历史提交仍完整保留英文原文，原地替换不会真的丢失原文，可随时通过 git 找回。

已知风险并经用户确认：该仓库是公开仓库，翻译并发布 Apple 官方文档的完整中文版本存在版权风险，用户已知悉并选择自行承担，继续公开发布。

## 协作与合并规则（强制）

- 所有翻译都从最新 `main` 创建独立功能分支；**禁止直接向 `main` 提交或推送**。
- 保持本仓库既有术语、标题、frontmatter、导航、分页链接和 Markdown 风格一致；不要顺手改名、搬目录或重排无关索引。
- 固定流程：**翻译 → 独立审校 → 机械校验 → 提 PR → 由仓库所有者审核合并**。
- 执行者只能提交 PR，无权自行合并；PR 未经用户审核不得 squash、rebase 后强推或关闭重开。
- 一个 PR 只处理计划中明确领取的一批文档，避免把抓取回填、索引重建和正文翻译混在同一 PR。

## 范围口径（重要，避免走错目录）

- **"40 份文档"** = `_indexes/by-platform/ios.md` 里 `### [Cocoa](../documentation/Cocoa.md)（40 份）` 小节列出的那 40 条，对应 344 个页面文件。
- **不是** `documentation/Cocoa/` 整个目录（那里有 120 份文档、1088 个页面，含大量 macOS 专属内容，超出本次范围）。
- 实际要动的文档物理文件都在 `documentation/Cocoa/<文档目录>/*.md` 下，但**只翻译**在 iOS 40 份名单里出现的那些子目录，其余 80 份 Cocoa 文档本轮不碰。
- 40 份名单以 `_indexes/by-platform/ios.md` 中 Cocoa 小节当前的实际列出顺序为准（该顺序是按标题字母排序生成的，直接照此顺序推进，不再另行排序）。

## 阶段一：翻译目录/索引层

**范围**：`README.md` + `_indexes/` 下全部索引文件（约 100 个，包括顶层分类索引、`by-platform/*.md`、`by-type/*.md`、以及各分类下的二级索引如 `_indexes/documentation/Cocoa.md`）。

**翻译内容**：
- 每个索引文件里的文档标题链接文字（如 `[Core Data Programming Guide](...)` → 译成中文标题，保留链接目标路径不变）
- 分类/平台名称等标签视情况处理（如 "Cocoa"、"iOS" 等专有名词/框架名保留英文，不生造中文译名）
- 已经是中文的结构性文字（导航面包屑、"共 XX 份文档"、标题行等）不用动

**产出物**：除了实际改动索引文件之外，同步整理一份 iOS Cocoa 40 份文档的**中英文标题对照表**（英文标题 ↔ 拟定中文译名 ↔ 对应物理路径），作为阶段二翻译正文时统一标题译法的依据，避免同一文档在不同索引里译名不一致。这份对照表可以直接作为一次性变更说明放在提交信息里，或者作为附带的 Markdown 表格产出，不需要额外建独立文件。

**执行方式**：批量处理，可用脚本辅助定位所有需要替换的标题文字位置（正则找 `[英文标题](路径)` 模式），但标题翻译本身需要人工/逐条给出准确译文，不能机械替换。

## 阶段二：翻译 iOS Cocoa 40 份文档正文（344 页）

**顺序**：严格按 `_indexes/by-platform/ios.md` 里 Cocoa 小节当前列出的顺序（字母序），逐份文档、逐页翻译。

**每份文档的处理流程**（以文档为单位，不是以页面为单位提交）：
1. 定位该文档在 `documentation/Cocoa/<文档目录>/` 下的全部页面文件（入口页 + 子章节页 + Document Revision History，参考已确认的三段式结构）。
2. 逐页把正文英文替换成中文翻译，原地写回同一文件（不新建双语版本、不新建镜像目录）。
3. **翻译时顺手检查并修复**：
   - 代码块缺失语言标注（裸 ` ``` ` 块，补 `objc`/`swift`/`c` 等，参考 `tools/build_obsidian_vault.py` 里已有的 `guess_code_language` 启发式规则，人工确认后手动补标）
   - 表格错位、残留 HTML 等格式问题（历史清理已覆盖大部分，个别文档仍可能有遗漏，发现即修）
   - 不在这个阶段引入新的结构性改动（比如不改文件名、不改目录结构），只改正文内容和代码块语言标注
4. 该文档全部页面译完后，在功能分支中作为一个 git 提交（提交信息里注明文档标题），推送后提交 PR；只由仓库所有者审核并合并到 `main`。

**已确认的文档层级样例**（供翻译时参考页面结构，无需重新调研）：
- `Advanced Memory Management Programming Guide`（5页）：入口页 → 3个子章节页 → Document Revision History
- `Key-Value Coding Programming Guide`（15页）：`index.md`入口 → 13个子主题页 → `RevisionHistory.md`
- `Core Data Programming Guide`（20页）：`index.md`入口 → 18个子主题页 → `RevisionHistory.md`

## 验证方式

- 每份文档翻译提交后，跑一次 `tools/` 里已有的链接校验逻辑（复用 `build_obsidian_vault.py` 里 `verify()` 的检查思路，或者简单用 grep 确认该文档内部相对链接、图片引用没有因为翻译误改路径而失效）。
- 代码块语言标注修复后，用 grep 确认裸 ` ``` ` 块数量在该文档范围内降到 0（或有意保留的除外，比如纯数据/无法判断语言的块）。
- 阶段一索引翻译完成后，抽查 `README.md` 和 `_indexes/by-platform/ios.md` 在 GitHub 网页上直接预览，确认中文标题渲染正常、链接可跳转。
- 阶段二全部 40 份文档译完后，回到 `_indexes/by-platform/ios.md` 的 Cocoa 小节和 `_indexes/documentation/Cocoa.md`，确认索引里的标题文字与阶段一确定的中文标题对照表一致（避免阶段一、阶段二译名不统一）。

## 关于范围的现实提醒

40 份文档共 344 页，且要求"边译边查格式问题"，是一个内容量很大的人工翻译工作，不是一次性能自动跑完的脚本任务。实际执行会是多轮、逐文档进行——每次会话/每次调用大概率只能完成其中若干份文档，需要按文档为单位持续推进，直到 40 份全部完成。

## 子 agent 领取任务的方式

用户会在这份计划确认后自行启动其他 agent 来做实际翻译。每个子 agent 应该：
1. 认领附录清单里**尚未开始**的某一份完整文档（不要跨文档拆页面认领，保持"一份文档一次提交"的粒度）。
2. 翻译该文档目录下列出的全部页面文件，原地替换正文为中文，同时按阶段二的要求顺手修代码块语言标注、格式问题。
3. 完成后把该文档在附录里对应的所有页面状态从「未开始」改成「已译」，提交一次 git commit。
4. 领取下一份「未开始」的文档，重复上述流程，直到 40 份全部变成「已译」。

下面附录里的路径都是相对 vault 根目录（即 `Apple Developer Archive Vault/` 目录）的相对路径。

## 附：40 份文档 × 344 页 分阶段任务清单

状态统一初始为「未开始」；子 agent 领取任务后应把对应行改成「进行中」，完成后改成「已译」。每份文档一张小表，按 `_indexes/by-platform/ios.md` 里 Cocoa 小节的原始顺序排列（与阶段二执行顺序一致）。

### 1. Archives and Serializations Programming Guide

目录：`documentation/Cocoa/Archives and Serializations Programming Guide/`　共 10 页

| 页面文件 | 状态 |
|---|---|
| `Archives.md` | 已译 |
| `Creating and Extracting Archives.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Encoding and Decoding C Data Types.md` | 已译 |
| `Encoding and Decoding Objects.md` | 已译 |
| `Forward and Backward Compatibility for Keyed Archives.md` | 已译 |
| `Introduction.md` | 已译 |
| `Object Graphs.md` | 已译 |
| `Serializing Property Lists.md` | 已译 |
| `Subclassing NSCoder.md` | 已译 |

### 2. Assertions and Logging Programming Guide

目录：`documentation/Cocoa/Assertions and Logging Programming Guide/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `Document Revision History.md` | 已译 |
| `How Assertions Work.md` | 已译 |
| `Introduction to Assertions and Logging.md` | 已译 |
| `Logging Messages.md` | 已译 |
| `Using a Custom Assertion Handler.md` | 已译 |
| `Using the Assertion Macros.md` | 已译 |

### 3. Atomic Store Programming Topics

目录：`documentation/Cocoa/Atomic Store Programming Topics/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `Atomic Store Fundamentals.md` | 已译 |
| `Atomic Store Life-cycle.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Initializing a Store and Loading Data.md` | 已译 |
| `Introduction to Atomic Store Programming Topics.md` | 已译 |
| `Registering a Custom Store Type.md` | 已译 |

### 4. Attributed String Programming Guide

目录：`documentation/Cocoa/Attributed String Programming Guide/`　共 12 页

| 页面文件 | 状态 |
|---|---|
| `Accessing Attributes.md` | 已译 |
| `Attributed Strings.md` | 已译 |
| `Changing an Attributed String.md` | 已译 |
| `Creating Attributed Strings in Cocoa.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Drawing Attributed Strings.md` | 已译 |
| `Formatted Documents and Attributed Strings.md` | 已译 |
| `Index.md` | 已译 |
| `Introduction to Attributed String Programming Guide.md` | 已译 |
| `RTF Files and Attributed Strings.md` | 已译 |
| `Standard Attributes.md` | 已译 |
| `Word and Line Calculations in Attributed Strings.md` | 已译 |

### 5. Binary Data Programming Guide

目录：`documentation/Cocoa/Binary Data Programming Guide/`　共 5 页

| 页面文件 | 状态 |
|---|---|
| `Data Objects.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction to Binary Data Programming Guide for Cocoa.md` | 已译 |
| `Working With Binary Data.md` | 已译 |
| `Working With Mutable Binary Data.md` | 已译 |

### 6. Collections Programming Topics

目录：`documentation/Cocoa/Collections Programming Topics/`　共 10 页

| 页面文件 | 状态 |
|---|---|
| `About Collections.md` | 已译 |
| `Arrays- Ordered Collections.md` | 已译 |
| `Copying Collections.md` | 已译 |
| `Dictionaries- Collections of Keys and Values.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Enumeration- Traversing a Collection’s Elements.md` | 已译 |
| `Index Paths- Storing a Path Through Nested Arrays.md` | 已译 |
| `Index Sets- Storing Indexes into an Array.md` | 已译 |
| `Pointer Function Options.md` | 已译 |
| `Sets- Unordered Collections of Objects.md` | 已译 |

### 7. Core Data Model Versioning and Data Migration Programming Guide

目录：`documentation/Cocoa/Core Data Model Versioning and Data Migration Programming Guide/`　共 10 页

| 页面文件 | 状态 |
|---|---|
| `Core Data Model Versioning and Data Migration.md` | 已译 |
| `Customizing the Migration Process.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Initiating the Migration Process.md` | 已译 |
| `Lightweight Migration.md` | 已译 |
| `Mapping Overview.md` | 已译 |
| `Migration and iCloud.md` | 已译 |
| `Model File Format and Versions.md` | 已译 |
| `The Migration Process.md` | 已译 |
| `Understanding Versions.md` | 已译 |

### 8. Core Data Programming Guide

目录：`documentation/Cocoa/Core Data Programming Guide/`　共 20 页

| 页面文件 | 状态 |
|---|---|
| `ChangeManagement.md` | 已译 |
| `CocoaBindings.md` | 已译 |
| `Concurrency.md` | 已译 |
| `CoreDataandStoryboards.md` | 已译 |
| `CreatingObjects.md` | 已译 |
| `FaultingandUniquing.md` | 已译 |
| `FetchingObjects.md` | 已译 |
| `FrequentlyAskedQuestions.md` | 已译 |
| `HowManagedObjectsarerelated.md` | 已译 |
| `IntegratingCoreData.md` | 已译 |
| `KeyConcepts.md` | 已译 |
| `LifeofaManagedObject.md` | 已译 |
| `MO_Lifecycle.md` | 已译 |
| `ObjectValidation.md` | 已译 |
| `Performance.md` | 已译 |
| `PersistentStoreFeatures.md` | 已译 |
| `RevisionHistory.md` | 已译 |
| `TroubleshootingCoreData.md` | 已译 |
| `index.md` | 已译 |
| `nsfetchedresultscontroller.md` | 已译 |

### 9. Core Data Utility Tutorial

目录：`documentation/Cocoa/Core Data Utility Tutorial/`　共 9 页

| 页面文件 | 状态 |
|---|---|
| `Complete Source Listings.md` | 已译 |
| `Creating the Core Data Stack.md` | 已译 |
| `Creating the Managed Object Model.md` | 已译 |
| `Creating the Project.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction to Core Data Utility Tutorial.md` | 已译 |
| `Listing Previous Runs.md` | 已译 |
| `The Application Log Directory.md` | 已译 |
| `The Custom Managed Object Class.md` | 已译 |

### 10. Data Formatting Guide

目录：`documentation/Cocoa/Data Formatting Guide/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `Creating a Custom Formatter.md` | 已译 |
| `Date Formatters.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Formatters and User Interface Elements.md` | 已译 |
| `Introduction to Data Formatting Programming Guide For Cocoa.md` | 已译 |
| `Number Formatters.md` | 已译 |

### 11. Date and Time Programming Guide

目录：`documentation/Cocoa/Date and Time Programming Guide/`　共 7 页

| 页面文件 | 状态 |
|---|---|
| `About Dates and Times.md` | 已译 |
| `Calendars, Date Components, and Calendar Units.md` | 已译 |
| `Dates.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Historical Dates.md` | 已译 |
| `Performing Calendar Calculations.md` | 已译 |
| `Using Time Zones.md` | 已译 |

### 12. Error Handling Programming Guide

目录：`documentation/Cocoa/Error Handling Programming Guide/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `Document Revision History.md` | 已译 |
| `Error Objects, Domains, and Codes.md` | 已译 |
| `Error Responders and Error Recovery.md` | 已译 |
| `Handling Received Errors.md` | 已译 |
| `Index.md` | 已译 |
| `Introduction to Error Handling Programming Guide For Cocoa.md` | 已译 |
| `Recovering From Errors.md` | 已译 |
| `Using and Creating Error Objects.md` | 已译 |

### 13. Event-Driven XML Programming Guide

目录：`documentation/Cocoa/Event-Driven XML Programming Guide/`　共 10 页

| 页面文件 | 状态 |
|---|---|
| `Constructing XML Tree Structures.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Handling Parsing Errors.md` | 已译 |
| `Handling XML Elements and Attributes.md` | 已译 |
| `Introduction to Event-Driven XML Programming Guide for Cocoa.md` | 已译 |
| `Parser Capabilities and Architecture.md` | 已译 |
| `Using Multiple Delegates.md` | 已译 |
| `Validation Tips and Techniques.md` | 已译 |
| `XML Glossary.md` | 已译 |
| `XML Parsing Basics.md` | 已译 |

### 14. Exception Programming Topics

目录：`documentation/Cocoa/Exception Programming Topics/`　共 10 页

| 页面文件 | 状态 |
|---|---|
| `Controlling a Program’s Response to Exceptions.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Exceptions and the Cocoa Frameworks.md` | 已译 |
| `Exceptions in 64-Bit Executables.md` | 已译 |
| `Handling Exceptions.md` | 已译 |
| `Introduction to Exception Programming Topics for Cocoa.md` | 已译 |
| `Nesting Exception Handlers.md` | 已译 |
| `Predefined Exceptions.md` | 已译 |
| `Throwing Exceptions.md` | 已译 |
| `Uncaught Exceptions.md` | 已译 |

### 15. Key-Value Coding Programming Guide

目录：`documentation/Cocoa/Key-Value Coding Programming Guide/`　共 15 页

| 页面文件 | 状态 |
|---|---|
| `AccessingCollectionProperties.md` | 已译 |
| `AccessorConventions.md` | 已译 |
| `BasicPrinciples.md` | 已译 |
| `CollectionOperators.md` | 已译 |
| `Compliant.md` | 已译 |
| `DataTypes.md` | 已译 |
| `DefiningCollectionMethods.md` | 已译 |
| `HandlingNon-ObjectValues.md` | 已译 |
| `Performance.md` | 已译 |
| `Relationships.md` | 已译 |
| `RevisionHistory.md` | 已译 |
| `SearchImplementation.md` | 已译 |
| `ValidatingProperties.md` | 已译 |
| `Validation.md` | 已译 |
| `index.md` | 已译 |

### 16. Key-Value Observing Programming Guide

目录：`documentation/Cocoa/Key-Value Observing Programming Guide/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `Document Revision History.md` | 已译 |
| `Introduction to Key-Value Observing Programming Guide.md` | 已译 |
| `KVO Compliance.md` | 已译 |
| `Key-Value Observing Implementation Details.md` | 已译 |
| `Registering Dependent Keys.md` | 已译 |
| `Registering for Key-Value Observing.md` | 已译 |

### 17. Low-Level File Management Programming Topics

目录：`documentation/Cocoa/Low-Level File Management Programming Topics/`　共 11 页

| 页面文件 | 状态 |
|---|---|
| `Creating Paths and Locating Directories.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `File Handle.md` | 已译 |
| `File Management Classes.md` | 已译 |
| `File Management.md` | 已译 |
| `HFS File Types.md` | 已译 |
| `Information about Files and Volumes.md` | 已译 |
| `Introduction to Low-Level File Management Programming Topics.md` | 已译 |
| `Resolving Aliases.md` | 已译 |
| `Using URLs.md` | 已译 |
| `Working with the Contents of a Directory.md` | 已译 |

### 18. Notification Programming Topics

目录：`documentation/Cocoa/Notification Programming Topics/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `Delivering Notifications To Particular Threads.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction.md` | 已译 |
| `Notification Centers.md` | 已译 |
| `Notification Queues.md` | 已译 |
| `Notifications.md` | 已译 |
| `Posting a Notification.md` | 已译 |
| `Registering for a Notification.md` | 已译 |

### 19. Number and Value Programming Topics

目录：`documentation/Cocoa/Number and Value Programming Topics/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `Document Revision History.md` | 已译 |
| `Introduction to Numbers and Other Values.md` | 已译 |
| `Using Decimal Numbers.md` | 已译 |
| `Using NSNull.md` | 已译 |
| `Using Numbers.md` | 已译 |
| `Using Values.md` | 已译 |

### 20. Predicate Programming Guide

目录：`documentation/Cocoa/Predicate Programming Guide/`　共 7 页

| 页面文件 | 状态 |
|---|---|
| `BNF Definition of Cocoa Predicates.md` | 已译 |
| `Comparison of NSPredicate and Spotlight Query Strings.md` | 已译 |
| `Creating Predicates.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction.md` | 已译 |
| `Predicate Format String Syntax.md` | 已译 |
| `Using Predicates.md` | 已译 |

### 21. Preferences and Settings Programming Guide

目录：`documentation/Cocoa/Preferences and Settings Programming Guide/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `About Preferences and Settings.md` | 已译 |
| `About the User Defaults System.md` | 已译 |
| `Accessing Preference Values.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Implementing an iOS Settings Bundle.md` | 已译 |
| `Storing Preferences in iCloud.md` | 已译 |

### 22. Property List Programming Guide

目录：`documentation/Cocoa/Property List Programming Guide/`　共 9 页

| 页面文件 | 状态 |
|---|---|
| `About Property Lists.md` | 已译 |
| `Creating Property Lists Programmatically.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction to Property Lists.md` | 已译 |
| `Old-Style ASCII Property Lists.md` | 已译 |
| `Quick Start for Property Lists.md` | 已译 |
| `Reading and Writing Property-List Data.md` | 已译 |
| `Serializing a Property List.md` | 已译 |
| `Understanding XML Property Lists.md` | 已译 |

### 23. Resource Programming Guide

目录：`documentation/Cocoa/Resource Programming Guide/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `About Resources.md` | 已译 |
| `Data Resource Files.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Image, Sound, and Video Resources.md` | 已译 |
| `Nib Files.md` | 已译 |
| `String Resources.md` | 已译 |

### 24. Sort Descriptor Programming Topics

目录：`documentation/Cocoa/Sort Descriptor Programming Topics/`　共 3 页

| 页面文件 | 状态 |
|---|---|
| `Creating and Using Sort Descriptors.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction to Sort Descriptors.md` | 已译 |

### 25. String Programming Guide

目录：`documentation/Cocoa/String Programming Guide/`　共 15 页

| 页面文件 | 状态 |
|---|---|
| `Character Sets.md` | 已译 |
| `Characters and Grapheme Clusters.md` | 已译 |
| `Creating and Converting String Objects.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Drawing Strings.md` | 已译 |
| `Formatting String Objects.md` | 已译 |
| `Index.md` | 已译 |
| `Introduction to String Programming Guide.md` | 已译 |
| `Reading Strings From and Writing Strings To Files and URLs.md` | 已译 |
| `Scanners.md` | 已译 |
| `Searching, Comparing, and Sorting Strings.md` | 已译 |
| `String Format Specifiers.md` | 已译 |
| `String Representations of File Paths.md` | 已译 |
| `Strings.md` | 已译 |
| `Words, Paragraphs, and Line Breaks.md` | 已译 |

### 26. Timer Programming Topics

目录：`documentation/Cocoa/Timer Programming Topics/`　共 4 页

| 页面文件 | 状态 |
|---|---|
| `Document Revision History.md` | 已译 |
| `Introduction to Timers.md` | 已译 |
| `Timers.md` | 已译 |
| `Using Timers.md` | 已译 |

### 27. Undo Architecture

目录：`documentation/Cocoa/Undo Architecture/`　共 10 页

| 页面文件 | 状态 |
|---|---|
| `Clearing the Undo Stack.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction to Undo Architecture.md` | 已译 |
| `Performing Undo and Redo.md` | 已译 |
| `Registering Undo Operations.md` | 已译 |
| `Setting Action Names.md` | 已译 |
| `Undo Manager.md` | 已译 |
| `Using Undo Notifications.md` | 已译 |
| `Using Undo in AppKit-Based Applications.md` | 已译 |
| `Using Undo on iPhone.md` | 已译 |

### 28. Cocoa Fundamentals Guide

目录：`documentation/Cocoa/Cocoa Fundamentals Guide/`　共 7 页

| 页面文件 | 状态 |
|---|---|
| `Adding Behavior to a Cocoa Program.md` | 已译 |
| `Cocoa Design Patterns.md` | 已译 |
| `Cocoa Objects.md` | 已译 |
| `Communicating with Objects.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction.md` | 已译 |
| `What Is Cocoa.md` | 已译 |

### 29. Coding Guidelines for Cocoa

目录：`documentation/Cocoa/Coding Guidelines for Cocoa/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `Acceptable Abbreviations and Acronyms.md` | 已译 |
| `Code Naming Basics.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction to Coding Guidelines for Cocoa.md` | 已译 |
| `Naming Functions.md` | 已译 |
| `Naming Methods.md` | 已译 |
| `Naming Properties and Data Types.md` | 已译 |
| `Tips and Techniques for Framework Developers.md` | 已译 |

### 30. Animation Types and Timing Programming Guide

目录：`documentation/Cocoa/Animation Types and Timing Programming Guide/`　共 6 页

| 页面文件 | 状态 |
|---|---|
| `Animation Class Roadmap.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Introduction to Animation Types and Timing Programming Guide.md` | 已译 |
| `Property-Based Animations.md` | 已译 |
| `Timing, Timespaces, and CAAnimation.md` | 已译 |
| `Transition Animation.md` | 已译 |

### 31. Core Animation Programming Guide

目录：`documentation/Cocoa/Core Animation Programming Guide/`　共 12 页

| 页面文件 | 状态 |
|---|---|
| `About Core Animation.md` | 已译 |
| `Advanced Animation Tricks.md` | 已译 |
| `Animatable Properties.md` | 已译 |
| `Animating Layer Content.md` | 已译 |
| `Building a Layer Hierarchy.md` | 已译 |
| `Changing a Layer’s Default Behavior.md` | 已译 |
| `Core Animation Basics.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Improving Animation Performance.md` | 已译 |
| `Key-Value Coding Extensions.md` | 已译 |
| `Layer Style Property Animations.md` | 已译 |
| `Setting Up Layer Objects.md` | 已译 |

### 32. Blocks Programming Topics

目录：`documentation/Cocoa/Blocks Programming Topics/`　共 7 页

| 页面文件 | 状态 |
|---|---|
| `Blocks and Variables.md` | 已译 |
| `Conceptual Overview.md` | 已译 |
| `Declaring and Creating Blocks.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Getting Started with Blocks.md` | 已译 |
| `Introduction.md` | 已译 |
| `Using Blocks.md` | 已译 |

### 33. Object-Oriented Programming with Objective-C

目录：`documentation/Cocoa/Object-Oriented Programming with Objective-C/`　共 7 页

| 页面文件 | 状态 |
|---|---|
| `Document Revision History.md` | 已译 |
| `Introduction.md` | 已译 |
| `Object-Oriented Programming.md` | 已译 |
| `Structuring Programs.md` | 已译 |
| `Structuring the Programming Task.md` | 已译 |
| `The Object Model.md` | 已译 |
| `Why Objective-C.md` | 已译 |

### 34. Objective-C Runtime Programming Guide

目录：`documentation/Cocoa/Objective-C Runtime Programming Guide/`　共 9 页

| 页面文件 | 状态 |
|---|---|
| `Declared Properties.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Dynamic Method Resolution.md` | 已译 |
| `Interacting with the Runtime.md` | 已译 |
| `Introduction.md` | 已译 |
| `Message Forwarding.md` | 已译 |
| `Messaging.md` | 已译 |
| `Runtime Versions and Platforms.md` | 已译 |
| `Type Encodings.md` | 已译 |

### 35. Programming with Objective-C

目录：`documentation/Cocoa/Programming with Objective-C/`　共 11 页

| 页面文件 | 状态 |
|---|---|
| `About Objective-C.md` | 已译 |
| `Conventions.md` | 已译 |
| `Customizing Existing Classes.md` | 已译 |
| `Dealing with Errors.md` | 已译 |
| `Defining Classes.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Encapsulating Data.md` | 已译 |
| `Values and Collections.md` | 已译 |
| `Working with Blocks.md` | 已译 |
| `Working with Objects.md` | 已译 |
| `Working with Protocols.md` | 已译 |

### 36. The Objective-C Programming Language

目录：`documentation/Cocoa/The Objective-C Programming Language/`　共 14 页

| 页面文件 | 状态 |
|---|---|
| `Associative References.md` | 已译 |
| `Categories and Extensions.md` | 已译 |
| `Declared Properties.md` | 已译 |
| `Defining a Class.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Enabling Static Behavior.md` | 已译 |
| `Exception Handling.md` | 已译 |
| `Fast Enumeration.md` | 已译 |
| `Glossary.md` | 已译 |
| `Introduction.md` | 已译 |
| `Objects, Classes, and Messaging.md` | 已译 |
| `Protocols.md` | 已译 |
| `Selectors.md` | 已译 |
| `Threading.md` | 已译 |

### 37. Bonjour Overview

目录：`documentation/Cocoa/Bonjour Overview/`　共 7 页

| 页面文件 | 状态 |
|---|---|
| `About Bonjour.md` | 已译 |
| `Bonjour - Frequently Asked Questions.md` | 已译 |
| `Bonjour API Architecture.md` | 已译 |
| `Bonjour Concepts.md` | 已译 |
| `Bonjour Operations.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Domain Naming Conventions.md` | 已译 |

### 38. Stream Programming Guide

目录：`documentation/Cocoa/Stream Programming Guide/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `Cocoa Streams.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Handling Stream Errors.md` | 已译 |
| `Introduction to Stream Programming Guide for Cocoa.md` | 已译 |
| `Polling Versus Run-Loop Scheduling.md` | 已译 |
| `Reading From Input Streams.md` | 已译 |
| `Setting Up Socket Streams.md` | 已译 |
| `Writing To Output Streams.md` | 已译 |

### 39. Advanced Memory Management Programming Guide

目录：`documentation/Cocoa/Advanced Memory Management Programming Guide/`　共 5 页

| 页面文件 | 状态 |
|---|---|
| `About Memory Management.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Memory Management Policy.md` | 已译 |
| `Practical Memory Management.md` | 已译 |
| `Using Autorelease Pool Blocks.md` | 已译 |

### 40. Threading Programming Guide

目录：`documentation/Cocoa/Threading Programming Guide/`　共 8 页

| 页面文件 | 状态 |
|---|---|
| `About Threaded Programming.md` | 已译 |
| `Document Revision History.md` | 已译 |
| `Glossary.md` | 已译 |
| `Introduction.md` | 已译 |
| `Run Loops.md` | 已译 |
| `Synchronization.md` | 已译 |
| `Thread Management.md` | 已译 |
| `Thread Safety Summary.md` | 已译 |

（共计 40 份文档，344 个页面文件，与阶段二统计口径一致。所有路径均需加上 `documentation/Cocoa/<对应目录>/` 前缀，与上方"目录"字段拼接后才是相对 vault 根目录的完整路径。）
