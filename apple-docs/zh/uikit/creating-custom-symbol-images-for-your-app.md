---
title: 为你的 App 创建自定符号图像
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/creating-custom-symbol-images-for-your-app
source_url: 'https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/creating-custom-symbol-images-for-your-app.json'
content_hash: 'sha256:2476d9bee12f7531'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [图像与 PDF](images-and-pdf.md) · [UIImage](uiimage.md)

# 为你的 App 创建自定符号图像

<sub>文章</sub>

使用 SF Symbols 创建、整理符号图像（symbol image）并为其添加注解。

## 概述

SF Symbols 提供一整套一致且高度可配置的符号图像，供你在 App 中使用。你可以应用通常与文本相关联的风格特性（trait），例如应用颜色、文本样式、字重和缩放比例。符号还包含一些额外的特性，使它们能与周围文本无缝整合，并适应动态字体（Dynamic Text）和深色模式（Dark Mode）等平台特性。

你可以创建自己的自定符号图像，使其具备与 SF Symbols 所提供的相同能力。创建你的自定符号的步骤如下：

1. 从 [SF Symbols](https://developer.apple.com/sf-symbols/) App 导出 SVG 文件。
2. 在矢量绘图 App 中编辑 SVG 文件。
3. 从你的绘图 App 将该文件导出为 SVG 文件。
4. 使用 SF Symbols App 校验 SVG 文件。
5. 将自定符号导入 SF Symbols App，并将它整理到一个组中。
6. 如有需要，添加注解以支持渲染模式或动画。
7. 导出用于分发的模板文件。

开始创建你自己的符号的一种方式，是以 SF Symbols App 中找到的现有符号为基础。例如，circle 符号就可以作为你着手起步的绝佳参照。

> [!tip] 提示
> 你可以将现有符号——来自先前模板版本的——拖放到这个 App 上，它会自动把该符号转换为模板版本 4，并将它添加到当前集合中。

设计指引参见[人机界面指南 \> SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/)。

### 导出自定符号模板文件

从模板版本 3 开始，左外边距和右外边距参考线有了更明确的名称，标明它们对应的设计变体。为了对视觉对齐进行更多控制，你可以为模板中的任意变体添加外边距。模板能够嵌入关于符号在不同渲染模式下应如何显示的信息。

找到要用作设计基础的符号图像后，选取“File \> Duplicate as Custom Symbol”。App 会在分类边栏底部创建一个新分类，你的自定符号就位于那里。要为你的自定符号创建 SVG 文件，请选中该符号并选取“File \> Export Template”，导出一个用于设计自定的符号模板文件。

导出模板时，你可以在静态和可变之间选择。如果你针对的是特定字重和缩放比例，或者只打算设计符号的一两个变体，请使用静态设置。该设置包含 27 组路径和一组显式外边距。可变模板设置包含三组路径和三组外边距。如果你打算支持全部设计变体，这就提供了系统生成其余 24 个变体所需的最少变体数量。

> [!note] 注意
> 从模板版本 3 开始，SF Symbols 为符号变体引入了矢量插值。通过使用三个来源——`Ultralight-S`、`Regular-S` 和 `Black-S`——SF Symbols 可以动态生成你没有指定的全部字重和缩放比例。

导出模板文件后，使用矢量绘图 App（例如 Adobe Illustrator 或 Sketch）开始修改它。

### 管理符号图像变体

Symbols 图层最多包含 27 个子图层，每个子图层代表一个符号图像变体。符号变体的标识符采用 `<weight>-<{S, M, L}>` 的形式，其中 _weight_ 对应 San Francisco 系统字体的一种字重，_S_、_M_ 或 _L_ 则匹配小、中或大符号缩放比例。

```xml
<g id="Symbols">
    <g id="Regular-M" transform="matrix(1 0 0 1 2855.62 1556)">
        <!-- Path and style details for the Regular-M image variant. -->
    </g>
</g>
```

如果符号内的所有形状都具有纯色填充，且没有描边或其他图形特征，SF Symbols 会将该符号视为基于路径而非基于描边。插值让系统能够在兼容的路径之间生成变体。模板在以下情况下可插值：

- 它包含插值来源 `Ultralight-S`、`Regular-S` 和 `Black-S`。
- 这三个插值来源都是基于路径的。
- 这三个插值来源包含相同数量的路径和相同数量的控制点。

模板不必包含全部 27 个变体。你可以向模板添加任意数量的变体，如果这些变体存在，系统就会使用它们而不是插值。与处理版本 3 之前的模板类似，你可以删除不需要的变体，从而生成你的 App 所需的任意数量的字重和缩放比例。

### 整理 Guides 图层

系统使用参考线来将你的自定符号图像与周围文本对齐。例如，系统使用为三种字体缩放比例各自提供的基线和大写字母高度（cap height）信息，来计算符号图像的基线偏移量和大写字母高度。

Guides 图层针对 San Francisco 系统字体的每种缩放比例，各包含一个轮廓形式的大写字母 _A_ 作为参考字形。请把模板中的参考字形当作参考线，用来衡量符号图像在文本旁边的外观。

从模板版本 3 开始，符号的每个图像变体都可以拥有自己的外边距参考线。这样外边距可以随字重和缩放比例略有变化，而不是为所有变体使用固定外边距。显式外边距参考线采用 `left-margin-<variant-specifier>` 或 `right-margin-<variant-specifier>` 的形式。下面的示例表示 `Regular-S` 符号变体的左右参考线：

```xml
<g id="Guides">
    <line id="left-margin-Regular-S" style="fill:none;stroke:#00AEEF;stroke-width:0.5;opacity:1.0;" x1="1403.33" x2="1403.33" y1="600.784" y2="720.121"/>
    <line id="right-margin-Regular-S" style="fill:none;stroke:#00AEEF;stroke-width:0.5;opacity:1.0;" x1="1496.36" x2="1496.36" y1="600.784" y2="720.121"/>
</g>
```

符号可以包含负外边距，以辅助水平对齐。如果你没有指定显式外边距参考线，系统会使用它找到的下一组可用外边距——插值得到的外边距（如果模板可插值）、`Regular-M`、`Regular-S`，最后是系统可以使用的任何可用外边距。

### 创建你的自定符号图像

创建你的自定符号图像，从修改你导出的模板文件中的符号开始。如果你导出的是可变模板，则需要修改所有三个符号配置，系统才能生成其他变体。

完成基础变体后，将现有绘图拷贝到所需的图层，并在此基础上调整。这有助于你在各个设计变体之间保持相同的路径数量；如果你想生成带有多色或分层数据的符号，这是一项必要条件。

设计变体时，请使用以下缩放因子：

|  | \<weight\>-S | \<weight\>-M | \<weight\>-L |
|---|---|---|---|
| 缩放因子 | 0.783 | 1.0 | 1.29 |

在所有不同的缩放比例和字重下，系统都会自动让符号相对 San Francisco 的大写字母高度垂直居中。请务必使用指定的参考线来放置你的自定符号，以确保它在文本中正确显示。当符号图像出现在文本中时，系统会垂直放置它，使符号图像的底边到文本的距离（按点大小缩放）等于符号图像在模板文件中到基线参考线的距离。

> [!important] 重要
> SF Symbols 会把变体图层中的所有路径——包括不可见的路径——都视为符号轮廓的一部分。在 SF Symbols App 中处理图层时，这可能导致意外结果，所以请不要使用隐藏路径。

创建符号时，你处理的是单色表示。为确保你的符号支持单色以外的渲染模式：

- 将所有描边转换为路径，让得到的形状能够呈现颜色或层级组。当描边不够精确时，路径更容易进行细微的视觉调整。
- 使用标准的纯色填充，不要添加投影之类的额外效果。如果存在这些效果，它们会覆盖你为符号创建的任何多色或分层数据。
- 检查设计中的所有形状是否都定义了填充区域，且起点和终点相互连接。

> [!important] 重要
> 注解数据要求各设计之间的路径数量一致。要在修改已注解符号的路径时保留注解数据，你可以添加、移除和调整点，但移除或重新排列整条路径会让你的设计失去同步。在这些情况下，你需要为符号重新添加注解，以适应它的新路径结构。

图像变体会根据用户的设备语言自动调整，包括从右到左的书写系统。如果你要同时为从左到右和从右到左的书写系统设计，请考虑两个本地化变体的方向性和整体外观。某些情况下，一些符号在镜像后无法呈现预期的外观。设计指引参见[人机界面指南 \> 从右到左](https://developer.apple.com/design/human-interface-guidelines/right-to-left/overview/introduction/)。

### 在 Notes 图层中保留注解和元信息

Notes 图层包含关于模板文件的可选注解和元信息。`template-version` 图层包含一个必需的版本字符串，用于标明模板格式版本，因此你不能移除它，否则 SF Symbols 无法读取该文件。`artboard` 图层确保设计工具以合适的画布大小和清晰易读的符号来显示模板。

Notes 图层包含关于自定符号模板文件的注解，可以帮助你理解其内容。这些注解是可选的，但最好保持原样，以供你参考。

> [!note] 注意
> 你不需要修改 Notes 图层的内容。在对文件做任何修改之前，请先在矢量绘图 App 中锁定 artboard 图层，以免不小心触碰并移动它。

### 导出你的自定符号并保留所有名称

完成符号设计后，以最高精度将它从矢量绘图 App 导出为 SVG 文件。Illustrator 默认生成低精度 SVG，因此请把默认小数位数改为 7 或更大再导出 SVG。请确认 SVG 文件保留了符号变体和参考线的所有标识符。

使用以下任意一种方法来校验你的 SVG 文件是否符合 SF Symbols 的要求：

- 使用 SF Symbols App，并选取“File \> Validate Templates”。
- 把它添加到 Xcode 项目的资源目录（asset catalog）中。Xcode 会校验 SVG 文件，如果文件不符合要求，会显示错误信息。
- 检查 SVG 文件，手动审阅 XML 源代码。理解模板布局有助于你调试校验问题，因此请保留你导入矢量绘图 App 的原始模板，作为比照的参考。

拿到有效的模板文件后，就可以开始为它添加注解。将你的符号拖放回 SF Symbols App 中你的自定符号上，即可把它重新导入。

### 为你的自定符号添加注解

如果你想控制符号在单色以外渲染模式下的外观，可以为符号添加注解。SF Symbols 以 CSS 样式的形式将注解应用于各个形状对象，使用的类名采用 `multicolor-<layer index>:<color name>` 或 `hierarchical-<layer index>:<hierarchy level>` 的形式，并且图层索引从零开始。你可以把颜色名称设为系统颜色、来自 App 资源目录的具名颜色（named color），或任何不会动态解析的常量。一个形状可以同时具有多色和分层注解，而且它们不必位于同一图层。

```xml
<style>
    .multicolor-0:systemBlueColor { fill:#007AFF; opacity:1.0 }
    .multicolor-1:white { fill:#FFFFFF; opacity:1.0 }
    .multicolor-2:tintColor { fill:#007AFF; opacity:1.0 }
    .hierarchical-0:tertiary { fill:#8E8E8E }
    .hierarchical-1:primary { fill:#212121 }
</style>

<g id="Symbols">
    <!-- A variant containing three shapes with multicolor and hierarchical annotations. -->
    <g id="Regular-M" transform="matrix(1 0 0 1 2853.78 1556)">
        <!-- The shape is in the first multicolor layer, whose fill color is systemBlueColor. It’s also in the first layer for hierarchical rendering, and the level is primary. -->
        <path class="multicolor-0:systemBlueColor hierarchical-1:primary" d="...">

        <!-- Two additional shapes. --><path class="multicolor-1:white hierarchical-1:primary" d="...">
        <path class="multicolor-2:tintColor hierarchical-0:tertiary" d="...">
     </g>
</g>
```

添加注解时，你把构成符号的各个路径作为基本构建单元。在此基础上，你为每种渲染模式创建一组图层。SF Symbols 在多色模式下为图层分配颜色，在分层模式下为图层分配层级组。图层具有明确的 Z 顺序：上层的图层会挡住其下层的图层。

在 SF Symbols 中，选中你的符号，选取“View \> As Gallery”进入画廊视图。选取“View \> Inspectors \> Show Color Sidebar”打开颜色检查器，然后选择渲染模式，开始添加注解。中央预览让你可以与所有路径交互，并将它们分配到图层。同一条路径可以用在任意数量的图层中。在分层模式下，你需要指定从 primary 到 tertiary 的分组，系统会在分层和调色板渲染模式中使用同一份数据。

> [!tip] 提示
> 尽可能使用系统提供的颜色，因为它们能适应系统外观的变化——浅色、深色和高对比度模式——以及不同的虚化（vibrancy）环境。

重叠形状有一个常见问题：路径重叠的地方会被看穿。在颜色检查器中，每个图层右侧都有一个切换开关。如果它处于停用状态，透明图层会与下面的图层融合；如果它处于启用状态，透明图层会清除背后的内容，渲染时就好像其他图层不存在一样。

完成符号的注解后，导出该符号用于分发。

### 为可变符号添加注解

系统和自定符号可以使用百分比值来动态应用颜色，以传达强度或随时间推移的进度。例如，无线信号强度符号可以在 100% 时反映满格信号，在 0% 时反映无信号。在 SF Symbols 中，选中你的符号并打开颜色检查器。每个图层都支持为它启用可变颜色（variable color）。矢量文件包含你的符号的阈值。

```xml
<style>
    <!-- A symbol that contains three variable color layers -->
    .monochrome-0 {fill:#000000}
    .monochrome-1 {fill:#000000}
    .monochrome-2 {fill:#000000;-sfsymbols-variable-threshold:0.0}
    .monochrome-3 {fill:#000000;-sfsymbols-variable-threshold:0.34}
    .monochrome-4 {fill:#000000;-sfsymbols-variable-threshold:0.68}
</style>
```

### 分发你的自定符号

分发符号时有两个选项需要考虑。先选取“File \> Export Symbol”。屏幕左下角默认显示的是版本 4。

模板版本 2 及更高版本会移除注解数据和显式外边距。如果你计划部署到较旧的操作系统（例如 iOS 14），请使用这个版本。它只包含单色，因此请确保你的符号在该模式下依然合理。

模板版本 3 及更高版本会嵌入你的所有多色和分层数据注解，以及任何自定外边距。它不向后兼容，因此当你支持 iOS 15 或更高版本时，请使用这个版本。

模板版本 4 会嵌入你的可变颜色注解，因此当你支持 iOS 16 或更高版本时，请使用这个版本。

> [!important] 重要
> 这些版本都不是用于编辑的源工件（source artifact）。当前的设计工具可能不兼容内嵌的注解数据。如果你需要编辑或与同事共享，请将它重新导入 SF Symbols App。

如果你的最低部署目标是 iOS 15 或更高版本，你只需要版本 3 模板。如果你的最低部署目标是 iOS 14，你需要导出版本 2、3 和 4 的模板，并根据版本检查使用相应的资源。与同事共享时请使用最新模板，因为对方可以把它导入自己的 SF Symbols App，继续编辑和添加注解。

下面的代码示例展示了最新模板版本文件——保留了标识符，但省略了路径细节——并包含针对每个部分的附加说明：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--Generator: Apple Native CoreSVG 168-->
<!DOCTYPE svg
  PUBLIC "-//W3C//DTD SVG 1.1//EN"
         "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="3300" height="2200">

<style>
<!--
Class names have the form <rendering mode style>-<layer index>:<color name>. Rendering mode is either hierarchical or multicolor, layer index is an integer between [0...N], and color name is either a system color, a named color from your app's asset catalog, or a constant (in which case it doesn't dynamically resolve).

If the color name isn't a system color and isn't in the asset catalog, a style can have a fill attribute. You can use an opacity attribute, and a custom attribute `-sfsymbols-clear-behind:true`, which, when present, occludes other shapes in the symbol that you annotate with that style, and blends with anything behind the symbol. The system may ignore other attributes you add.

Version 4 of the symbol template supports variable color thresholds by using `-sfsymbols-variable-threshold`.
-->
  .multicolor-0:systemBlueColor {fill:#007AFF;-sfsymbols-variable-threshold:0.0}
  .multicolor-1:tertiaryLabelColor {fill:#BDBDBD;-sfsymbols-clear-behind:true}
  .multicolor-2:white {fill:#FFFFFF;opacity:0.4}
  .hierarchical-0:tertiary {fill:#8E8E8E}
  .hierarchical-1:primary {fill:#212121;-sfsymbols-clear-behind:true}
</style>

<g id="Notes">
<!--
The symbol template supports rendering mode annotations and path interpolation.
-->
  <text id="template-version">Template v.3.0</text>
</g>

<g id="Guides">
  <line id="Baseline-S" x1="..." x2="..." y1="..." y2="..."/>
  <line id="Capline-S" x1="..." x2="..." y1="..." y2="..."/>
  <line id="Baseline-M" x1="..." x2="..." y1="1126" y2="..."/>
  <line id="Capline-M" x1="..." x2="..." y1="1055.54" y2="..."/>
  <line id="Baseline-L" x1="..." x2="..." y1="1556" y2="..."/>
  <line id="Capline-L" x1="..." x2="..." y1="1485.54" y2="..."/>

  <!--
  The symbol template supports explicit margins for each variant.
  -->
  <line id="left-margin-Ultralight-S" x1="..." x2="..." y1="..." y2="..."/>
  <line id="right-margin-Ultralight-S" x1="..." x2="..." y1="..." y2="..."/>
  <line id="left-margin-Regular-S" x1="..." x2="..." y1="..." y2="..."/>
  <line id="right-margin-Regular-S" x1="..." x2="..." y1="..." y2="..."/>
  <line id="left-margin-Black-S" x1="..." x2="..." y1="..." y2="..."/>
  <line id="right-margin-Black-S" x1="..." x2="..." y1="..." y2="..."/>
</g>

<g id="Symbols">
<!--
The symbol template generates variants from the following source variants: Black-S, Regular-S, and Ultralight-S. When you create other variants, the system uses them instead of interpolation for that configuration.
-->
  <g id="Black-S">
  <!--
  The system concatenates together all shapes for each rendering mode layer. A shape may be present in many layers. Shapes you nest within other shapes, and have opposite path windings, knock holes through their containing shapes.
  -->
    <path class="multicolor-0:systemBlueColor hierarchical-0:tertiary" d="..."/>
    <path class="multicolor-1:tertiaryLabelColor hierarchical-1:primary" d="..."/>
    <path class="multicolor-0:systemBlueColor multicolor-1:tertiaryLabelColor hierarchical-1:primary" d="..."/>
    <path class="multicolor-2:white hierarchical-1:primary" d="..."/>
  </g>

  <g id="Regular-S">
    <path class="multicolor-0:systemBlueColor hierarchical-0:tertiary" d="..."/>
    <path class="multicolor-1:tertiaryLabelColor hierarchical-1:primary" d="..."/>
    <path class="multicolor-0:systemBlueColor multicolor-1:tertiaryLabelColor hierarchical-1:primary" d="..."/>
    <path class="multicolor-2:white hierarchical-1:primary" d="..."/>
  </g>

  <g id="Ultralight-S">
    <path class="multicolor-0:systemBlueColor hierarchical-0:tertiary" d="..."/>
    <path class="multicolor-1:tertiaryLabelColor hierarchical-1:primary" d="..."/>
    <path class="multicolor-0:systemBlueColor multicolor-1:tertiaryLabelColor hierarchical-1:primary" d="..."/>
    <path class="multicolor-2:white hierarchical-1:primary" d="..."/>
  </g>
</g>
</svg>
```

### 使用你的自定符号图像

打开你 App 的 Xcode 项目并选中它的资源目录。在 Xcode 的菜单栏中，选取“Editor \> Add New Asset \> Symbol Image Set”，然后把导出的 SVG 文件拖到 Symbol 面板的 Symbol SVG 区域中。Xcode 会校验 SVG 文件，如果文件不满足要求，会显示错误信息。要在 App 中使用该符号图像，请遵循[在 UI 中配置和显示符号图像](configuring-and-displaying-symbol-images-in-your-ui.md)。

## 另请参阅

### 加载和缓存图像

- [为不同外观提供图像](providing-images-for-different-appearances.md) — 提供适合浅色和深色外观以及高对比度环境的图像资源。
- [在 UI 中配置和显示符号图像](configuring-and-displaying-symbol-images-in-your-ui.md) — 创建可与你的 App 文本整合的可缩放图像，并动态调整这些图像的外观。
- [+ imageNamed:inBundle:compatibleWithTraitCollection:](<uiimage/init(named_in_compatiblewith_).md>) — 使用与指定特性集合（trait collection）兼容的具名图像资源创建图像对象。
- [+ imageNamed:inBundle:withConfiguration:](<uiimage/init(named_in_with_).md>) — 使用与你指定的配置兼容的具名图像资源创建图像。
- [init(named:in:variableValue:configuration:)](<uiimage/init(named_in_variablevalue_configuration_).md>) — 使用你指定的名称、配置和可变值创建图像。
- [+ imageNamed:](<uiimage/init(named_).md>) — 根据指定的具名资源创建图像对象。
- [init(imageLiteralResourceName:)](<uiimage/init(imageliteralresourcename_).md>) — 返回指定资源的图像对象。
- [+ systemImageNamed:withConfiguration:](<uiimage/init(systemname_withconfiguration_).md>) — 创建包含带指定配置的系统符号图像的图像对象。
- [init(systemName:variableValue:configuration:)](<uiimage/init(systemname_variablevalue_configuration_).md>) — 创建包含系统符号图像的图像对象，使用你指定的配置和可变值。
- [+ systemImageNamed:compatibleWithTraitCollection:](<uiimage/init(systemname_compatiblewith_).md>) — 创建包含适合指定特性的系统符号图像的图像对象。
- [+ systemImageNamed:](<uiimage/init(systemname_).md>) — 创建包含系统符号图像的图像对象。
- [init(resource:)](<uiimage/init(resource_).md>)
- [构建高性能列表和集合视图](building-high-performance-lists-and-collection-views.md) — 使用预取和图像准备来提升你 App 中列表和集合的性能。
