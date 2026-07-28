---
title: 使用 Icon Composer 创建你的 App 图标
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-your-app-icon-using-icon-composer
source_url: 'https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-your-app-icon-using-icon-composer.json'
content_hash: 'sha256:956eff167b8ebd83'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [资源管理](asset-management.md)

# 使用 Icon Composer 创建你的 App 图标

<sub>文章</sub>

使用 Icon Composer 来为不同的平台和外观样式设计你的 App 图标。

## 概述

使用 Icon Composer 来创建一个多层文件，你可以将它添加到 Xcode 项目中，让你的 Liquid Glass App 图标在你 App 图标出现的所有地方（包括 iOS、iPadOS、macOS、watchOS 以及 App Store）进行展示。使用你喜欢的图形设计工具来创作你的 App 图标素材，但把部分设计决策留给 Icon Composer，你可以在其中优化 [Liquid Glass](../technologyoverviews/liquid-glass.md) 的动态属性，并为不同的平台和外观定制 App 图标的变体。

![](../../../attachments/4d66768899a2f11c38516ebb5146bdaa/icon-composer-hero-overview@2x.png)

<sub>Icon Composer 的截图，显示侧边栏中选择了一个组，画布中选择了 iOS、macOS 平台和 mono 外观，以及外观检查器中的 Liquid Glass 设置。画布中的图标显示在自定义背景图片上，并应用了 50% 模糊和半透明度的 Liquid Glass 设置。</sub>

在构建你的 App 之前，将 Icon Composer 文件添加到你的 Xcode 项目中，以将其包含在你的 App 包（bundle）中。系统会根据你的单个 Icon Composer 文件，自动为不同的平台、外观和尺寸渲染你的 App 图标。如果你的 App 支持那些不具备相同图标和小组件风格外观以及 Liquid Glass 材质的早期版本（在目标的“通用”（General）面板中的“最低部署”（Minimum Deployments）设置中），Xcode 会在构建时从 Icon Composer 文件为这些版本自动生成 App 图标图像。

> [!important] 重要
> 如果你将 Icon Composer 文件添加到 Xcode 项目中，它将替换你之前用于表示 App 图标的任何现有图标资源目录（asset catalog）。Xcode 会自动为早期版本生成一个外观相似的 Liquid Glass 图标版本。如果你希望现有图标出现在早期版本中，请继续使用资源目录来表示你的 App 图标。

要了解更多信息，请参阅以下资源：

- 有关设计 App 图标的指导，请参阅[人机界面指南 \> 基础 \> App 图标](../design/human-interface-guidelines/app-icons.md)。
- 有关将旧版 App 图标转换为使用 Liquid Glass 材质，请参阅[采用 Liquid Glass \> App 图标](../technologyoverviews/adopting-liquid-glass.md#App-icons)。
- 有关 Liquid Glass 和 Icon Composer 的更多信息，请观看[Say hello to the new look of app icons](https://developer.apple.com/videos/play/wwdc2025/220/)和[Create icons with Icon Composer](https://developer.apple.com/videos/play/wwdc2025/361/)。
- 对于仍然使用 `AppIcon` 资源目录的 tvOS 和 visionOS 目标，请参阅[使用资源目录配置你的 App 图标](configuring-your-app-icon.md)。

### 准备要导出的素材

要设计你的 Liquid Glass App 图标，请使用你选择的第三方矢量图形编辑器，将图层导出为 SVG 或 PNG 格式的图形文件。为了获得最大的可扩展性，可以使用矢量图形绘制形状并导出 SVG 文件。

在你设计 App 图标并导出图层之前，请遵循以下指南以获得最佳效果：

- 从[Apple 设计资源](https://developer.apple.com/design/resources/)下载带有最新网格、形状和画布尺寸的 App 图标模板开始。
- 否则，将画布尺寸更改为与你在 Icon Composer 中使用的尺寸相匹配，例如 iPhone、iPad 和 Mac 使用 1024 x 1024 像素，Apple Watch 使用 1088 x 1088 像素。
- 按图层设计你的 App 图标，系统会在 z 轴上从后到前渲染这些图层。
- 将颜色、文本以及任何其他图形分离到要在 Icon Composer 中为平台和外观修改的图层中。
- 由于 SVG 格式不保留字体，请将文本转换为轮廓。
- 为图层赋予有意义的名称，包含数字（从后到前递增），以帮助你在 Icon Composer 中组织它们。

此外，建议将一些效果留到 Icon Composer 中应用，在那里你可以预览并为 Liquid Glass 进行调整：

- 移除模糊和阴影，以及高光、不透明度和半透明度设置。
- 移除背景颜色和渐变。

当你准备好从第三方工具导出图层时，尽可能选择 SVG 格式。对于包含不支持 SVG 功能的图层，请选择 PNG 或 Icon Composer 支持的其他光栅图像格式。不要导出画布蒙版（canvas mask），因为系统会自动应用该蒙版以确保完美裁剪。

### 创建你的 Icon Composer 文件

要启动最新版本 Xcode 中的 Icon Composer，请选择 Xcode \> Open Developer Tool \> Icon Composer。如果你没有安装 Xcode，请转到 [Icon Composer](https://developer.apple.com/icon-composer) 下载它。

Icon Composer 会显示一个带有纯背景颜色的默认 App 图标。给文件起一个稍后要在 Xcode 项目中使用的名称，例如 `AppIcon`。选择文件 \> 保存，在弹出的对话框中输入文件名并点击存储。或者，点击工具栏中的“未命名”（Untitled），并在弹出的对话框中更改名称和位置。

![](../../../attachments/e4aea2562f33b63cb9b0d3bd84404fc8/icon-composer-app-anatomy@2x.png)

<sub>Icon Composer 的截图，带有标注，显示侧边栏中 Landmarks 示例 App 的组和图层，画布中选择了 iOS、macOS 平台和默认外观，以及外观检查器（Appearance inspector）中某个组的设置。</sub>

你使用左侧的侧边栏将图层组织成组，使用中间的画布预览变体，并使用右侧的检查器修改外观。在画布区域，你使用底部的控件选择平台和外观的组合，并使用顶部的控件应用网格或模拟设备条件。

你可以继续使用 Icon Composer 来微调你的 App 图标，并在稍后将其添加到你的 Xcode 项目中。要将 App 图标添加到 Xcode 项目并将其与 App 目标关联，请参阅[将你的 Icon Composer 文件添加到 Xcode 项目](creating-your-app-icon-using-icon-composer.md#Add-your-Icon-Composer-file-to-an-Xcode-project)。

如果你的 Icon Composer 文件在 Xcode 项目中，你可以在项目导航器（Project navigator）中选择它，并在画布区域中看到预览。要打开已存在于 Xcode 项目中的 Icon Composer 文件，请点击预览下方的“使用 Icon Composer 打开”（Open with Icon Composer），或按住 Control 键点击项目导航器中的文件并选择“使用外部编辑器打开”（Open with External Editor）。

### 导入你的图形文件

从你的设计工具导出素材后，将图形文件（SVG 或 PNG 格式）导入到你的 Icon Composer 文件中。

将一个或多个图形文件从访达（Finder）拖到侧边栏，每个文件将成为 Icon Composer 创建的默认组中的一个图层。或者，将包含图形文件的文件夹拖到侧边栏。然后，文件夹会成为组，文件夹中的文件会成为这些组中的图层。Icon Composer 使用与文件夹和文件相同的名称，按字母顺序组织组和图层。

或者，点击侧边栏下方的添加按钮（+），并从弹出菜单中选择“新建图像”（New Image）。在弹出的对话框中，选择一个或多个文件（使用 Command-点击选择多个文件），然后点按“打开”。

![侧边栏底部添加按钮弹出菜单的截图，其中选中了“新建图像”菜单项。](../../../attachments/fdd248093a92ca4908aaf0ab1509bb16/icon-composer-add-new-layer@2x.png)

稍后，如果你想更改与某个图层关联的图形文件，请在侧边栏中选择该图层，然后在“外观检查器”的“构图”（Composition）下，从“图像”（Image）弹出菜单中选择“替换”（Replace）。然后，从出现的对话框中，选择新的图形文件。

### 将图层组织成组

导入图形文件后，将出现在默认组中的图层组织成最多四个组，以降低复杂性。这些组成为平台渲染的 App 图标图像中的图层，为图标赋予深度。系统按照侧边栏中的顺序，在 z 轴上从下到上渲染这些图层。组也允许你对多个图层应用通用设置。

![侧边栏的截图，带有标注，显示 Landmarks 示例 App 图标中的组和图层。](../../../attachments/6380db00b4ba44152d808487c20eaeca/icon-composer-layer-groups@2x.png)

你可以使用侧边栏进行以下编辑：

- 要创建一个组，点击侧边栏底部的添加按钮，并从弹出菜单中选择“新建组”（New Group）。
- 要更改组或图层的名称，请双击它并输入名称。
- 要将图层移入组，请将它们拖到你希望它们所在的组中。
- 要更改组或图层的顺序，请上下拖动它们。或者，选择图层或组，然后选择“排列”（Arrange）\>“前移 [组 | 图层]”（Bring [Group | Layer] Forward）或“排列”\>“后移 [组 | 图层]”（Send [Group | Layer] Backward）（或类似）菜单项。
- 要添加另一个图层，点击添加按钮并选择“图像”（Image）。

要进行更多编辑，请按住 Control 键点击图层或组，然后从上下文菜单中选择一个操作。

要在大纲中折叠组，请点击组左侧的展开箭头。要在画布中隐藏或显示图层和组，请在侧边栏中将指针悬停在组或图层上时，点击其右侧的眼睛图标。或者，在“外观检查器”的“构图”下，使用“可见”（Visible）切换开关来隐藏或显示图层和组。

要删除组、图层或图层中的图形，请在侧边栏或画布中选择它们，然后按 Delete 键。要还原更改，请选择“编辑”\>“撤销删除”。

### 自定义 Icon Composer 界面

在开始预览变体并为你的 App 图标添加效果之前，请考虑自定义 Icon Composer 界面，以仅显示你的 App 支持的平台。点击右上角的“文稿”（Document）按钮，并从“文稿检查器”（Document inspector）中选择平台。

![](../../../attachments/471bb47eb7fb0310fe330f9811f743e5/icon-composer-document-target-platforms@2x.png)

<sub>“文稿检查器”的截图，显示平台控制，你可以在其中选择支持的平台以减少界面的复杂性。</sub>

例如，如果你的 App 仅在 iOS 上运行，请从“iOS, macOS”弹出菜单中选择“仅 iOS”（iOS Only），并将 watchOS 切换为关闭。Icon Composer 会隐藏 macOS 和 watchOS 的控制项，以便你可以专注于 iOS App 图标的设计。

### 预览你的 App 图标的变体

Icon Composer 会向你显示你的 App 图标在不同平台（iOS、macOS 和 watchOS）以及针对 iOS 和 macOS 的不同外观（默认、深色和单色（mono））下的预览。对于单色，你还可以预览清晰（clear）和着色（tinted）变体。对于 watchOS，没有外观可供预览。

在画布区域图标图像的下方，点击左侧的平台和右侧的外观，以预览或编辑该变体。例如，要预览 iOS 中的深色外观，请在左侧选择 iOS，在右侧选择深色（Dark）。

![选择默认外观时显示 Landmarks 图标预览的截图。](../../../attachments/3713f5945eb1cfaf6d7f6037805f96a2/icon-composer-mode-preview-default@2x.png)

![选择深色外观时显示 Landmarks 图标预览的截图。](../../../attachments/c843fbdfa033256ccf7e34382fc20bd1/icon-composer-mode-preview-dark@2x.png)

![选择单色外观时显示 Landmarks 图标预览的截图。](../../../attachments/08d0be0e1101db6764f6ad341ff2098c/icon-composer-mode-preview-mono@2x.png)

要预览清晰和着色变体，请点击“单色”（Mono），然后点击“选项”（Options）。在对话框中，选择浅色或深色，打开或关闭着色，并使用滑块选择色调颜色。

![](../../../attachments/3dbcdca65e95dbc24d9949ce9c9a358f/icon-composer-mono-preview-settings@2x.png)

<sub>显示单色选项设置的截图，包含浅色和深色外观之间的切换开关、着色切换开关以及颜色滑块。</sub>

### 模拟设备背景和光照

要在不同的上下文中预览你的 App 图标，请使用画布区域上方工具栏中的控件。这些控件仅更改模拟显示你的 App 图标的设备；它们不会编辑你的 App 图标。

![带有标注的截图，显示背景、网格、光照角度和图标尺寸控制。](../../../attachments/b2fbc19d3476b14c82cb9da262a38c09/icon-composer-canvas-preview-settings@2x.png)

你可以使用工具栏控件设置以下内容：

- 要更改背景颜色，请从左侧的颜色井中选择一种颜色。
- 要更改背景图片，请从“背景图片”（Background Image）弹出菜单中选择一张背景图片。要使用你自己的图片，请在弹出菜单中点击“添加背景”（Add Background）。
- 要在背景颜色和图片之间切换，请点击背景切换开关。
- 要添加网格线，请从“网格”（Grid）弹出菜单中选择浅色或深色。
- 要打开或关闭网格线，请点击“网格”按钮。
- 要在不同光照方向下查看 App 图标，请旋转光照角度旋钮。
- 要查看 App 图标的特定尺寸，请从“选择预览尺寸”（Select preview size）弹出菜单中选择尺寸。
- 要放大或缩小，请从“更改缩放级别”（Change zoom level）弹出菜单中选择一个百分比。

你可以使用这些控件在你自己的背景上查看清晰和着色模式中的透明度。例如，要预览样本图像上的清晰深色变体，请选择 iOS 或 macOS 作为平台，单色作为外观。从单色选项对话框中，关闭着色。然后，在画布顶部的“背景图片”弹出菜单中选择“添加背景”，并在出现的对话框中选择屏幕截图。

![画布的截图，显示单色外观叠加在蓝色背景图片上。](../../../attachments/85acb4ca264331cb594ef7863a4d34e4/icon-composer-background-preview-mode-clear-dark@2x.png)

### 将效果应用到背景、组和图层

在你预览 App 图标在不同平台和设备设置下的变体时，使用外观检查器应用效果并修复你看到的任何问题。探索针对组以及组内图层的不同设置。

通常，“颜色”（Color）下的设置对于创建深色和单色外观的变体很有用。对于组和图层，你可以在 Liquid Glass 下自定义动态材质。然后，使用“构图”下的控件来改变你在不同平台上的设计。

![](../../../attachments/d5f6984e6f682fb1fa8385dae1e37ff3/icon-composer-applying-effects-inspector@2x.png)

<sub>外观检查器的截图，带有标注，显示设置中的“颜色”、“Liquid Glass”和“构图”区域。</sub>

要快速复制设置，你可以按住 Control 键点击单个设置或一个区域，然后从上下文菜单中选择“复制 [设置 | 区域]”（Copy [Setting | Section]）或“粘贴 [设置 | 区域]”（Paste [Setting | Section]）。或者，按住 Control 键点击侧边栏中的图层或组，然后从上下文菜单中选择“复制样式”（Copy Style）或“粘贴样式”（Paste Style）（编辑 \> 复制样式 和 编辑 \> 粘贴样式）。

对于任何你输入数字的文本字段，你可以输入一个算式，Xcode 会自动为你计算数值。例如，输入 `35*3`，或者要加倍现有值，输入 `*2`。

要移除你在外观检查器中做出的任何更改，请选择“编辑”\>“撤销”。

### 应用渐变填充和不透明度

在外观检查器的“颜色”下，你可以更改图层的填充，不再是 Icon Composer 从图形文件获取的默认值（自动（Automatic））。在侧边栏中选择图层，然后在外观检查器的“填充”（Fill）弹出菜单中，选择“无”（None）、“纯色”（Solid）或“渐变”（Gradient）。

![](../../../attachments/4e791cf1b42918c64c7c27b53a336cb4/icon-composer-color-app-icon-layer@2x.png)

<sub>某个图层的“颜色”设置截图，显示“填充”设置为“渐变”，其中“从”（From）颜色为黄色，“到”（To）颜色为橙色。</sub>

> [!tip] 提示
> 要为颜色设置 RGB 值或十六进制颜色编号，请使用“颜色选择器”（Color picker）中“颜色滑块检查器”（Color Sliders inspector）的 RGB 滑块。

例如，按照以下步骤为你的 App 图标背景应用渐变：

1. 在侧边栏中，点击图标文件名。
2. 在画布中，选择一个平台以及可选的外观。
3. 要显示设置，请点击窗口右上角的“外观检查器”（Appearance inspector）。
4. 从“颜色”弹出菜单中，选择“全部”（All）以更改所有变体。
5. 从“填充”弹出菜单中，选择“渐变”（Gradient）。
6. 从下方出现的两个颜色井中，选择“从”和“到”颜色。

![](../../../attachments/5d623b8b5ece365b45f3375578ddd013/icon-composer-color-app-icon-base@2x.png)

<sub>App 图标的“颜色”设置截图，显示“填充”设置为“渐变”，其中“从”颜色为“自动”（Auto），“到”颜色为蓝色。</sub>

要切换颜色，请在将指针悬停在渐变颜色井左侧的箭头上时点击它们。对于图层，你可以使用画布中出现在图层上的点来更改渐变的“从”和“到”位置。

![](../../../attachments/5495337f65a37b1565eb6255688626ff/icon-composer-gradient-dots@2x.png)

<sub>截图，左侧是侧边栏中选中的图层，中间是画布中形状上的渐变点，右侧是“渐变”下设置的“从”和“到”颜色。</sub>

你还可以使用“颜色”下的“不透明度”（Opacity）设置，让一个组或图层变得透明，以显示其背后的细节。

### 对组和图层应用 Liquid Glass 效果

当你导入图形文件时，Icon Composer 会自动将 Liquid Glass 材质添加到图层，并在你创建组时应用其他默认的 Liquid Glass 设置。

对于一个组，你有所有选项来自定义 Liquid Glass 材质。在侧边栏中选中一个组，然后在检查器的“模式”（Mode）弹出菜单中选择“单独”（Individual）或“合并”（Combined）。“单独”将效果分别应用于组中的每个图层。“合并”将效果作为一个对象应用于组中的图层。

**单独**

![显示 Liquid Glass 单独应用于组中各图层的预览截图。](../../../attachments/b720f1c3f4bd601f50a09ee79098b324/icon-composer-liquid-glass-on-individual@2x.png)

![显示“模式”设置为“单独”的截图。](../../../attachments/5d909fb323c9c7c1aaf5c62b2bffbb8b/icon-composer-liquid-glass-on-individual-settings@2x.png)

**合并**

![显示 Liquid Glass 共同应用于组中各图层的预览截图。](../../../attachments/daa44c88949c0eb4c1bcfdd4c21989b2/icon-composer-liquid-glass-on-combined@2x.png)

![显示“模式”设置为“合并”的截图。](../../../attachments/6830dbf29bbeddcfdf447d5cbe0299e8/icon-composer-liquid-glass-on-combined-settings@2x.png)

高光材质默认开启。如果你关闭高光（Specular），背景的轻微模糊和边缘周围的浅色高光就会消失。以下截图显示了一个包含太阳和山脉且关闭了高光的组。

**高光开启**

![显示 Liquid Glass 单独应用于组中各图层的预览截图。](../../../attachments/b720f1c3f4bd601f50a09ee79098b324/icon-composer-liquid-glass-on-individual@2x.png)

![显示“模式”设置为“单独”的截图。](../../../attachments/5d909fb323c9c7c1aaf5c62b2bffbb8b/icon-composer-liquid-glass-on-individual-settings@2x.png)

**高光关闭**

![包含太阳和山脉且高光已关闭的组的预览截图。](../../../attachments/c2eb38fec7bc3a5e8060d3ac7e42be56/icon-composer-specular-off@2x.png)

![高光已关闭的组的 Liquid Glass 设置截图。](../../../attachments/fc6f7c40b449614bce94785e9a976351/icon-composer-specular-off-settings@2x.png)

在高光下方，你可以将其余的 Liquid Glass 设置（模糊（Blur）、半透明度（Translucency）和阴影（Shadow））应用于该组。

要为单个图层关闭 Liquid Glass，请在侧边栏中选择该图层，然后在检查器中，关闭 Liquid Glass 下的“效果”（Effects）开关。

**效果开启**

![所有图层 Liquid Glass 效果均已开启的预览截图。](../../../attachments/b720f1c3f4bd601f50a09ee79098b324/icon-composer-liquid-glass-layer-on@2x.png)

![效果已开启的图层的 Liquid Glass 设置截图。](../../../attachments/7e68acd0e7e3c7be26bf0c9d9643e1e3/icon-composer-liquid-glass-layer-on-setting@2x.png)

**效果关闭**

![包含太阳的图层 Liquid Glass 效果已关闭的预览截图。](../../../attachments/992befb950ec194a5c151f9aa4f1d253/icon-composer-liquid-glass-layer-off@2x.png)

![效果已关闭的图层的 Liquid Glass 设置截图。](../../../attachments/ccb6fa4ce75ad5b85a0cb948c21bafa2/icon-composer-liquid-glass-layer-off-setting@2x.png)

### 更改图形的位置和缩放

你可以使用 Icon Composer 重新定位和缩放图层中的图形。只需在画布区域内拖动你想要移动的图形。

**图层**

[视频演示如何选择图层并在画布中拖动以更改其位置。](https://docs-assets.developer.apple.com/published/840d3c68973f585d0c2433140d6b74df/icon-composer-individual-layer-move.mp4)

**组**

[视频演示如何选择一个组并在画布中拖动以更改其位置。](https://docs-assets.developer.apple.com/published/c0f20a9da6e28f04c9d8600f2ab758fa/icon-composer-layer-group-move.mp4)

要移动多个组、图层或单个图形，请首先在侧边栏或画布中使用 Command-点击选中它们，或者在画布中拖拽出一个边界框来选中它们。Icon Composer 会在侧边栏和画布中高亮显示选中的图形。要取消选择所有图形，请按 Escape 键。

在拖动时使用出现的参考线来对齐选中的内容与其他图形。要进行更精确的编辑，你可以在外观检查器中“构图”下的“布局”（Layout）部分输入 x、y 和缩放。要逐点移动，请使用向上箭头和向下箭头键。

![截图显示“构图”下的“布局”部分，包含 x、y 和缩放设置。](../../../attachments/dbb0f178dec0543ae41a3f4ba818e482/icon-composer-composition-edit-selection@2x.png)

或者，打开网格，这样你就可以看到将图形放置在哪里。在工具栏中，点击“网格”按钮或从“网格”弹出菜单中选择浅色或深色。Icon Composer 会以你选择的颜色在你的 App 图标预览上叠加网格线。要移除网格线，请关闭网格。

![从画布顶部的“网格”弹出菜单中选择“深色”的截图。](../../../attachments/a500841c2535d1a45f27d21cd857d83d/icon-composer-grid-toggle@2x.png)

要使用其他方式重新定位所选内容，请使用“排列”\>“对齐”（Align）和“排列”\>“分布”（Distribute）菜单项。

### 自定义 App 图标的变体

你可以使用外观检查器自定义 App 图标特定的平台和外观变体。

要查看你自定义的设置，请在侧边栏中选择图标、组或图层，然后在外观检查器中的“颜色”、“Liquid Glass”或“构图”弹出菜单中选择“全部”。自定义设置会出现在主要设置下方。例如，如果你更改了 iOS 中深色和单色外观的“混合模式”（Blend Mode）设置，则“深色”和“单色”设置会出现在“混合模式”设置下方。主要设置适用于你未自定义的变体。

![从“颜色”弹出菜单中选择“全部”时显示深色和单色外观自定义设置的截图。](../../../attachments/0ce8fcfce0850effb570c9ff9815e07f/icon-composer-inspector-color-varied-by-mode@2x.png)

外观检查器会启用你在画布中选择的平台或外观的控件。例如，要启用出现在“混合模式”下方的“深色”设置，请在画布中选择深色外观。

要添加另一个自定义设置，请在画布中选择你想要变化的平台或外观，然后在外观检查器中，点击设置旁边的图标。从添加按钮弹出菜单中选择“让 [外观 | 平台] 变化”（Vary for [appearance | platform]）。例如，在画布中选择 iOS / macOS 和“默认”，然后从 Liquid Glass 下的“模糊”弹出菜单中选择“让 iOS / macOS 变化”（Vary for iOS / macOS）。

![](../../../attachments/a0078f96de7a8678eb838dbfe62b6bfe/icon-composer-edit-all-exception@2x.png)

<sub>从 Liquid Glass 弹出菜单中选择“全部”时，“模糊”设置下的“让...变化”弹出菜单的截图。</sub>

要移除自定义设置，请点击平台或外观旁边的 X。例如，要移除“混合模式”设置下的“深色”设置，请点击“深色”旁边的 X。

或者，从“颜色”或“Liquid Glass”弹出菜单中选择你在画布中选择的外观。然后，该区域中的控件仅适用于该外观。类似地，从“构图”弹出菜单中选择你在画布中选择的平台，该区域中的控件仅适用于该平台。控件以这种方式运行，是为了保持你的 App 图标外观的一致性，并且只有几何形状会跨平台变化。

![在画布中选择深色外观时，从“颜色”弹出菜单中选择“深色”的截图。](../../../attachments/900cee3fbd372908feb9f2ead14b5a5a/icon-composer-color-edit-selection@2x.png)

然后，你可以通过从“颜色”、“Liquid Glass”和“构图”弹出菜单中选择“全部”，切换回在一个地方查看你为平台和外观所做的所有自定义设置。

### 将你的 Icon Composer 文件添加到 Xcode 项目

如果你在 Xcode 外部创建了你的 Icon Composer 文件，你可以随时将其添加到 Xcode 项目中，以便在模拟器和真实设备上查看你的图标。

只需将 Icon Composer 文件从访达（Finder）拖到项目导航器中，Xcode 会提供反馈，指示将其放置在目标文件夹中的哪个位置。或者，从项目导航器底部的添加按钮中选择“添加文件”（Add Files），并在出现的对话框中选择你的 Icon Composer 文件。

在项目编辑器中，选择目标和“通用”标签页。在“App 图标和启动屏幕”（App Icons and Launch Screen）下，确保“App 图标”（App Icon）文本字段中的名称与 Icon Composer 文件的名称匹配（不带扩展名）。你可以在项目中拥有多个 Icon Composer 文件，但只有一个文件的名称与“App 图标”文本字段中的名称匹配。

> [!note] 注意
> 最新版本的 Xcode 会使用 Icon Composer 文件，而不是项目中现有的 `AppIcon` 资源目录。

### 在模拟和真实设备上测试你的 App 图标

在 Xcode 中，从运行目标菜单中选择一个模拟或真实设备，然后点按运行按钮。验证你的 App 图标在不同平台和外观下是否正确显示。使用模拟器或真实设备中的“外观”（Appearance）系统设置来测试外观。

有关在 Xcode 中运行 App 的更多信息，请参阅[在模拟或物理设备上运行你的 App](running-your-app-on-simulated-or-physical-devices.md)。

## 另请参阅

### App 图标和启动屏幕

- [配置你的 App 以使用备用 App 图标](configuring-your-app-to-use-alternate-app-icons.md) — 向你的 App 添加备用 App 图标，并让人们选择显示哪个图标。
- [使用资源目录配置你的 App 图标](configuring-your-app-icon.md) — 向资源目录添加 App 图标变体，在 App Store、主屏幕、设置和搜索结果等地方代表你的 App。
- [指定你的 App 的启动屏幕](specifying-your-apps-launch-screen.md) — 通过自定义启动屏幕，让你的 iOS App 启动体验更快、响应更迅速。
