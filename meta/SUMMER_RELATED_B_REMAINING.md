# 暑期强相关 B 类剩余清单

> 状态日期：2026-07-29  
> 权威运行：`summer-related-b-full-r01`  
> 当前成品：388 / 407（完整批次 385 篇，加烟雾样本 3 篇）  
> 当前决定：用户已停止继续消耗，不自动恢复

本页只记录尚未形成最终成品的 19 篇。不得把它们计入“已完成”，也不得再次对完整
407 篇盲目重跑。

它们均为复杂技术博客。分段流程降低了模型破坏 Markdown 骨架、代码、链接目标和行内
代码的概率，但仍会出现 JSON 不完整、标题漏译、技术输出误判和链接显示文字损坏。
当前不再修复；未来只有用户明确重启时，才从本页逐篇处理。

| 英文原文 | 状态 | 最后失败原因 |
|---|---|---|
| `blogs/en/maskray/all-about-leaksanitizer.md` | 审校中断 | 仍有 1 个片段缺失或不合格 |
| `blogs/en/maskray/stack-unwinding.md` | 失败 | 链接显示文字中的 API selector 被改动 |
| `blogs/en/maskray/weak-symbol.md` | 失败 | 标题未翻译 |
| `blogs/en/maskray/all-about-thread-local-storage.md` | 失败 | 标题未翻译 |
| `blogs/en/nshipster/optional-throws-result-async-await.md` | 审校中断 | 一批片段返回不完整 |
| `blogs/en/maskray/dependency-related-linker-options.md` | 审校中断 | 技术命令输出触发残留英文检查 |
| `blogs/en/maskray/explain-gnu-style-linker-options.md` | 审校中断 | 模型未返回可解析 JSON |
| `blogs/en/maskray/exploring-the-section-layout-in-linker-output.md` | 审校中断 | 模型未返回可解析 JSON |
| `blogs/en/maskray/linker-compatibility-and-the-user-agent-problem.md` | 审校中断 | 版本输出触发残留英文检查 |
| `blogs/en/maskray/lld-and-gnu-linker-incompatibilities.md` | 失败 | 符号表输出触发残留英文检查 |
| `blogs/en/maskray/relocatable-linking.md` | 审校中断 | 命令输出触发残留英文检查 |
| `blogs/en/maskray/the-dark-side-of-risc-v-linker-relaxation.md` | 审校中断 | 模型未返回可解析 JSON |
| `blogs/en/maskray/addresssanitizer-global-variable-instrumentation.md` | 失败 | LLVM IR 输出触发残留英文检查 |
| `blogs/en/maskray/all-about-sanitizer-interceptors.md` | 审校中断 | 模型未返回可解析 JSON |
| `blogs/en/maskray/all-about-undefinedbehaviorsanitizer.md` | 审校中断 | 模型未返回可解析 JSON |
| `blogs/en/maskray/compressed-debug-sections.md` | 失败 | 模型未返回可解析 JSON |
| `blogs/en/maskray/distribution-of-debug-information.md` | 失败 | `objcopy` 命令输出触发残留英文检查 |
| `blogs/en/maskray/skipping-boring-functions-in-debuggers.md` | 失败 | 调试器命令触发残留英文检查 |
| `blogs/en/maskray/zstd-compressed-debug-sections.md` | 失败 | 模型生成了错误的链接目标 |

## 下一步质量门

1. 默认停止，不调用模型；
2. 若用户明确重启，只处理这 19 篇，不重跑已完成的 388 篇；
3. 仍由英文原文骨架重建 Markdown，再运行严格标识符校验；
4. 机械校验通过后仍需独立语言与术语复审；
5. 19 篇全部通过前，B 类状态只能写作 388 / 407。
