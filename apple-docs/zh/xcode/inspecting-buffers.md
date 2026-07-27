---
title: 检查缓冲区
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/inspecting-buffers
source_url: 'https://developer.apple.com/documentation/xcode/inspecting-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/inspecting-buffers.json'
content_hash: 'sha256:164a8d2489be7503'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal debugger](metal-debugger.md)

# 检查缓冲区

<sub>文章</sub>

通过检查缓冲区内容来确认缓冲区格式。

## 概述

在 Metal 调试器中，你可以使用缓冲区查看器检查缓冲区内容是否正确。缓冲区查看器会根据当前上下文自动设置缓冲区内容的格式，例如使用当前绑定的管线状态。在某些情况下（例如当前没有绑定管线状态时），你也可以手动配置格式。调整格式后，可以拷贝或导出日后可能需要的任何值。

### 浏览缓冲区

缓冲区查看器会在一个大型表格中显示缓冲区内容。如果你在特定绘制命令或计算分派的 Bound Resources 查看器中打开缓冲区，Xcode 会自动对内容进行布局，使其与着色器中绑定的任何参数匹配。有关更多信息，请参阅[检查命令的绑定资源](inspecting-the-bound-resources-for-a-command.md)。

例如，假设一个顶点着色器接受 `float3` 位置和 `float3` 法线作为输入，并输出 `float4` 位置和 `float3` 法线。如果在 Bound Resources 查看器中打开几何体，Xcode 会在表格中为每个参数显示一列。

![一张缓冲区查看器的屏幕截图，其中高亮显示输入 float3 和输出 float4 位置的列。](../../../attachments/800b0f04b28b1b74cfc4a757f4fd7046/gputools-metal-debugger-bv-hero@2x.png)

在上面的截图中，`in – float3` 位置列显示三个浮点值，而 `out – float4` 位置列显示四个浮点值。

### 更改布局和初始偏移量

你可以使用底部的控件更改缓冲区查看器对缓冲区内容的布局方式。若要更改列参数类型，请点按 Element Type 下拉菜单。若要更改每行的元素数量，请点按其右侧的 Number of Elements per Row 下拉菜单。

![](../../../attachments/21cdb24ea552353df212d3e38925b069/gputools-metal-debugger-bv-formatting-0@2x.png)

<sub>一张缓冲区查看器中布局控件的屏幕截图，其中包含 Element Type 下拉菜单和 Number of Elements per Row 下拉菜单。</sub>

例如，如果元素类型为 `ushort`，且每行有 `4` 个元素，缓冲区查看器就会以四个 `ushort` 类型的列显示内容。

![一张缓冲区查看器的屏幕截图，其中每行显示四个无符号短整数。](../../../attachments/b85ae14f373246ea5415613459d88e8b/gputools-metal-debugger-bv-formatting-1@2x.png)

你还可以更改底部的 Offset 字段，调整缓冲区中的初始偏移量。例如，在下面的截图中，将偏移量改为 `0x10` 后，Row 0 会从 `[2 0 1 0]` 变为 `[4 0 2 0]`。

![一张缓冲区查看器的屏幕截图，其中高亮显示 Offset 控件。](../../../attachments/5686838c1b6d0c6605fb9a9d0e548afc/gputools-metal-debugger-bv-formatting-2@2x.png)

### 创建自定义布局

你可以点按 Element Type 下拉菜单，然后选取 Custom Layout \> Show Custom Layout Editor，创建自己的自定义布局。

![一张 Element Type 下拉菜单的屏幕截图，其中选中了 Custom Layout 菜单项。](../../../attachments/a33e44f645d2849039690e4c79983f48/gputools-metal-debugger-bv-create-custom-layout@2x.png)

1. 在第一列的 Layout 字段中输入原始类型（例如 `float3`），然后按下 Return 键。
2. 输入第一列的名称，然后按下 Return 键。
3. 对自定义布局中的所有列重复此操作。
4. Xcode 会自动计算行步幅，你也可以手动配置。

![一张缓冲区查看器的屏幕截图，其中显示了多种自定义布局。](../../../attachments/7fbafd47a91b5a431f9d2ef4a63e7fcd/gputools-metal-debugger-bv-custom-layout@2x.png)

自定义布局编辑器还支持资源类型，帮助你直观查看参数缓冲区中的资源。

![一张缓冲区查看器的屏幕截图，其中在自定义布局中显示了参数缓冲区资源。](../../../attachments/e376dcbc0ffaf16bd04f1b7dc35b00e2/gputools-metal-debugger-bv-custom-layout-resources@2x.png)

使用自定义布局完成缓冲区内容编辑后，点按 Done。你可以从 Element Type 下拉菜单中访问自定义布局，它们位于 Custom Layout \> Recent Custom Layouts 下方。

### 配置列

你可以将缓冲区查看器配置为仅显示所需信息。将指针放在列标题上，然后按住 Control 键点按。上下文菜单提供以下选项：

- Visible：切换列的可见性。
- Pinned：将列固定到表格左侧，即使水平滚动时也保持可见。
- Hide Other Columns：隐藏所选列和所有固定列之外的全部列。
- View Value As：将值转换为大小相同的另一种格式，例如将浮点数转换为无符号整数。

此外，你可以通过上下文菜单配置任意列的选项，并使用筛选栏按名称筛选。

![一张缓冲区查看器表格标题上下文菜单的屏幕截图，其中勾号表示列可见。](../../../attachments/8dcd5b6d87c88c2f7a0c655e8908b154/gputools-metal-debugger-bv-header-context@2x.png)

如果隐藏了任何列，可以从上下文菜单中选择 Show All Columns 恢复配置。

### 搜索特定文本和值

你可以使用搜索功能查找值。按下 Command-F 打开搜索栏。搜索栏使用令牌系统设置搜索格式，并会针对不同输入类型显示不同选项。

![一张缓冲区查看器的屏幕截图，其中显示了搜索栏。](../../../attachments/c2090673002c753ba8bdb2ff94877af8/gputools-metal-debugger-bv-search@2x.png)

如果指定浮点数并使用 Equal 或 Not Equal 比较类型，系统会提供额外令牌，用于设置比较的 epsilon 值（默认为 0.001）。如果指定十进制数或十六进制数，结果中只会高亮显示完全匹配的数字。

![一张缓冲区查看器的屏幕截图，其中搜索栏显示了比较类型上下文菜单。](../../../attachments/8e788d94ddaffb145b03eb2a481cb2f6/gputools-metal-debugger-bv-search-comparison@2x.png)

此外，如果指定资源的 GPU 基地址，或参数缓冲区的 GPU 基地址值（带或不带偏移量），该值会在结果中高亮显示。

你还可以搜索文本，例如资源名称、错误和无效数值（nan、inf、-inf）。

![一张缓冲区查看器的屏幕截图，其中显示了文本搜索结果。](../../../attachments/d7503e3731afccc02f59e9b6b833e7db/gputools-metal-debugger-bv-search-text@2x.png)

### 导出缓冲区内容

你可以在表格中选择整行或单个单元格，然后选取 Edit \> Copy 来拷贝缓冲区内容。系统会使用当前布局格式拷贝值，包括可见性设置和任何类型转换覆盖设置。

你也可以选取 Editor \> Export Buffer，导出整个缓冲区的内容。然后，可以将其保存为原始数据或 CSV 文件。

![一张 App 主菜单的屏幕截图，其中选中了 Export Buffer 菜单选项。](../../../attachments/bc454faca98c26e879f901eb893601e2/gputools-metal-debugger-bv-export-buffer@2x.png)

此外，也可以在 Bound Resources 查看器中按住 Control 键点按缓冲区，然后选取 Export 来导出缓冲区。有关更多信息，请参阅[检查命令的绑定资源](inspecting-the-bound-resources-for-a-command.md)。

![](../../../attachments/50bf13b69c0e650b0367a8728c790ce7/gputools-metal-debugger-bv-export@2x.png)

<sub>一张 Bound Resources 查看器中缓冲区资源上下文菜单的屏幕截图，其中高亮显示 Export Buffer 菜单项。</sub>

## 另请参阅

### Metal 资源检查

- [检查加速结构](inspecting-acceleration-structures.md) — 通过检查加速结构，揭示光线相交的性能瓶颈。
- [检查管线状态](inspecting-pipeline-states.md) — 通过检查渲染和计算通道的属性，确定它们的行为方式。
- [检查采样器状态](inspecting-sampler-states.md) — 通过检查采样器状态的属性，验证其配置。
- [检查着色器](inspecting-shaders.md) — 通过检查和编辑着色器，提升 App 的着色器性能。
- [检查纹理](inspecting-textures.md) — 通过检查纹理内容，发现纹理中的问题。
