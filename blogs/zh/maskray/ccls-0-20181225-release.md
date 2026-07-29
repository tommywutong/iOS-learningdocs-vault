---
title: ccls 0.20181225 发布
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2018-12-25-ccls-release'
original_language: en
published: 2018-12-25
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:294a7298358f6a91'
translated: true
---

> 原文：[ccls 0.20181225 release](https://maskray.me/blog/2018-12-25-ccls-release)　·　MaskRay (宋方睿)

[2018-12-25](https://maskray.me/blog/2018-12-25-ccls-release)

# ccls 0.20181225 发布

聖誕發佈新版[https://github.com/MaskRay/ccls/releases/tag/0.20181225](https://github.com/MaskRay/ccls/releases/tag/0.20181225)

- `workspace/didChangeWatchedFiles` 正常工作（已在 VSCode 和 coc.nvim 上测试），文件删除会移除索引符号
- `.ccls` 增强 [#171](https://github.com/MaskRay/ccls/pull/171) 新增指令 `%compile_commands.json`、`%h`、`%hpp`、`%objective-c`、`%objective-cpp`
- `-v=1` 转储用于解析的文件命令行选项
- fuzzy_match：当补全过滤器以字母开头时，不会返回以下划线为前缀的内建宏
- 支持 `textDocument/declaration` 和 `LocationLink[]` 返回类型
- 正确处理 `"exit"` [#159](https://github.com/MaskRay/ccls/pull/159)
- 支持 `signatureHelp.signatureInformationparameterInformation.labelOffsetSupport`，参见 [https://github.com/Microsoft/language-server-protocol/issues/640](https://github.com/Microsoft/language-server-protocol/issues/640)
- codeAction：修复了与 VSCode 的不兼容问题

## 补全

- 更精确的诊断/补全：已修改的包含文件无需保存即可生效
- 在某些情况下将 `Content-Length:` 从 32K 降低到 25K
- 在 clang \< 8 上，修复了 `-I dir` 的 `#include <` 补全
- 宏被归类为 `Text`，而非 `Interface`
- 重构和重命名（`clang_complete.cc` → `sema_manager.cc`）
- C++17 deduction guide #173

## 其他

- 支持多个 `-init=`：首先应用来自客户端的 `initializationOptions`，然后是 `-init=`。标量选项会被覆盖，数组则会被拼接

重点是

- 更加精确的诊断/补全（针对 `#include` 中的依赖 unsaved buffers），之前 cquery/ccls 的做法都不好
- 文件删除、重命名：之前这两个项目都不会清理删除的文件 [#170](https://github.com/MaskRay/ccls/pull/170)
- #159 是之前 LSP exit 触发 `exit(0)`（中断一个正在写缓存的 indexer 线程，下次可能读不出来，但非常罕见）
- 补全的其他大大小小改进
- 如果一个 textDocument 的索引未被加载，request（`textDocument/documentHighlight`、`textDocument/hover` 等）会报告 `not indexed`，显示在 echo area，比较恼人。我在 `pipeline.cc` 引入了一个 backlog 解决这一问题，详见 [https://github.com/MaskRay/ccls/pull/176](https://github.com/MaskRay/ccls/pull/176)。code lens 可以用 `(add-hook 'lsp-after-open-hook #'ccls-code-lens-mode)` 而不需要 `(run-at-time 0.5 nil #'ccls-code-lens-mode)` 了
- 增强 `.ccls` 和 `compile_commands.json` 的协作，详见 Paul Smith 的分析 [https://github.com/MaskRay/ccls/issues/115#issuecomment-449455357](https://github.com/MaskRay/ccls/issues/115#issuecomment-449455357)

## 其他

- ccls/wiki/Emacs 拆分为 [wiki/lsp-mode](https://github.com/MaskRay/ccls/wiki/lsp-mode) 和 [wiki/egot](https://github.com/MaskRay/ccls/wiki/eglot)，后者还比较简陋（欢迎贡献）
- eglot 支持 `workspace/didChangeWatchedFiles`，lsp-mode 尚未支持
- 我给 lsp-mode 加了 `LocationLink` 支持，`targetSelectRange` 可以指向名字，而 `targetRange` 指向轮廓。mouse hover 时可以有可视效果（对于 Emacs 用途不大）
- xref.el 的 `xref-file-location` 并非表示 `interface Range` 的良好选择，因为仅能表示点（line column），不能表示区间。lsp-ui-peek 里需要区间信息 highlight 文本，无法良好地用 xref 表达，在 lsp-ui-peek 里的实现有点恶心（希望有人能改好）

  ```plaintext
  ;; xref.el
  (defclass xref-file-location (xref-location)
    ((file :type string :initarg :file)
     (line :type fixnum :initarg :line :reader xref-location-line)
     (column :type fixnum :initarg :column :reader xref-file-location-column))
    :documentation "A file location is a file/line/column triple.
  Line numbers start from 1 and columns from 0.")

  ;; lsp-ui-peek.el
            (-if-let (uri (gethash "uri" x))
                (-let (((&hash "start" (&hash "line" "character")) (gethash "range" x)))
                  (lsp-ui-peek--goto-xref `(:file ,(lsp--uri-to-path uri) :line ,line :column ,character)))
              (-let (((&hash "start" (&hash "line" "character")) (or (gethash "targetSelectionRange" x) (gethash "targetRange" x))))
                (lsp-ui-peek--goto-xref `(:file ,(lsp--uri-to-path (gethash "targetUri" x)) :line ,line :column ,character))))
  ```
- 非常希望看到有人能把 lsp-mode 的 hash tables+string keys（`(gethash "range" xx)`）都改成 plists + keyword keys（`(plist-get xx :range)`），这样会让我感觉还是有希望的……
- code lens 我另外也在等待 eglot 的处理：[https://github.com/joaotavora/eglot/pull/71](https://github.com/joaotavora/eglot/pull/71)，lsp-mode 中的 issue 是 [https://github.com/emacs-lsp/lsp-mode/issues/361](https://github.com/emacs-lsp/lsp-mode/issues/361)
