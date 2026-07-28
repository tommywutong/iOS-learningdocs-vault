---
title: 在 Xcode 中创建 SpriteKit 粒子发射器
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-a-spritekit-particle-emitter-in-xcode
source_url: 'https://developer.apple.com/documentation/xcode/creating-a-spritekit-particle-emitter-in-xcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-a-spritekit-particle-emitter-in-xcode.json'
content_hash: 'sha256:15bb717718eda7a0'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [资源管理](asset-management.md)

# 在 Xcode 中创建 SpriteKit 粒子发射器

<sub>文章</sub>

通过创建可重复的粒子，为你的 App 添加粒子效果。

## 概述

使用 SpriteKit 粒子发射器编辑器来试验 SpriteKit 粒子效果，并立即查看结果。可视化界面将设计粒子效果的任务与编程分开，使美术师可以独立于你的代码创建效果。

![](../../../attachments/913bd66038df2ae6ffda53c904455ae1/sk-pe-editor@2x.png)

<sub>Xcode 的屏幕截图，在项目导航器中选中了 SpriteKit 粒子发射器文件。编辑器区域显示粒子发射器的预览，属性检查器显示关于粒子的可编辑信息。</sub>

编辑器允许你修改粒子发射器的许多属性，包括：

- 发射器创建粒子的位置
- 发射器创建的粒子数量
- 粒子的旋转、大小和运动
- 每个粒子在其生命周期内如何变化

### 向你的项目添加粒子发射器资源文件

1. 选择“文件”>“新建”>“从模板新建文件”。
2. 选择“资源”>“SpriteKit 粒子文件”，然后点按“下一步”。
3. 选择一个预安装的粒子发射器纹理，然后点按“下一步”。
4. 在下一个表单（sheet）中，选择一个位置并输入文件名。
5. 选中与你的项目关联的复选框，然后点按“创建”。Xcode 会创建一个扩展名为 `.sks` 的粒子发射器文件。
6. 在项目导航器中选中新的粒子发射器文件。Xcode 会在粒子发射器编辑器中打开该文件。

### 向场景添加粒子发射器

SpriteKit 粒子发射器编辑器会显示发射器的预览，但不会将发射器添加到你的 SpriteKit 场景中。使用代码将你的粒子发射器添加到场景中，或者使用 SpriteKit 场景编辑器创建一个指向你的粒子发射器文件的引用节点。当场景加载时，你的粒子发射器会作为引用节点的子节点进行渲染。

要为你的粒子发射器向 SpriteKit 场景添加引用节点，请执行以下操作：

1. 在项目导航器中，选中场景文件。
2. 点按工具栏中的“库”按钮 (+)，然后将引用节点从库中拖放到你的场景中。
3. 选中引用节点并打开“属性检查器”。
4. 在“名称”字段中输入一个名称。
5. 在“引用”弹出菜单中，选择粒子发射器文件。

![](../../../attachments/78d6c5e85210b2dcfd2ee296efc6fdbe/sk-se-referencenode@2x.png)

<sub>SpriteKit 场景中选中了引用节点时的属性检查器屏幕截图。一个名为“引用”的部分包含“名称”、“父级”和“引用”字段。</sub>

### 选择粒子的形状

通过选择纹理来选择粒子的形状。发射器创建的每个粒子都基于一个纹理图像，该图像可以是实心形状或复杂图片。你可以使用与项目关联的任何图像作为粒子纹理。系统会将粒子发射器的所有修改应用于所选图像。

在“纹理”弹出菜单中，选择一个粒子纹理。请记住，粒子图像越大或越复杂，它消耗的资源就越多。为达到所需效果，请使用尽可能最小、最简单的图像。

![属性检查器的屏幕截图，显示一个名为“纹理”的字段，其值为 spark。](../../../attachments/1b53a6978a95e8fdd5f6c56f1fb71c88/sk-pe-texture@2x.png)

### 更改粒子的颜色

你可以更改粒子在其生命周期内的颜色，并确定粒子如何与其他图像进行混合。

使用“颜色混合”字段来控制粒子将其颜色与其纹理固有颜色混合的方式。

在“颜色混合”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入颜色混合值。

![属性检查器的屏幕截图，显示一个名为“颜色混合”的部分，包含“因子”、“范围”和“速度”字段。](../../../attachments/031f03d8442b9590a7539490626992a7/sk-pe-colorblend@2x.png)

- **`因子`** — 混合因子的平均起始值。该值对应于粒子发射器的 [particleColorBlendFactor](../spritekit/skemitternode/particlecolorblendfactor.md) 属性。值的有效区间是从 `0.0` 到 `1.0`（含）。高于或低于该区间的值会被钳制为最小值 (`0.0`)（如果低于）或最大值 (`1.0`)（如果高于）。默认值为 `0.0`，这意味着按原样使用纹理，忽略粒子的颜色。否则，纹理将与颜色混合。
- **`范围`** — 为每个粒子创建起始颜色混合的随机方差的范围值。该值对应于粒子发射器的 [particleColorBlendFactorRange](../spritekit/skemitternode/particlecolorblendfactorrange.md) 属性。
- **`速度`** — 修改每个粒子颜色混合的速率，以每秒变化量衡量。该值对应于粒子发射器的 [particleColorBlendFactorSpeed](../spritekit/skemitternode/particlecolorblendfactorspeed.md) 属性。

使用“颜色渐变”字段来更改粒子在其生命周期内的颜色。你可以让一个粒子在其生命周期内经历任意多次颜色变化。粒子根据颜色滑块之间的空间来改变颜色。

在“颜色渐变”字段中，点按字段内的任意位置以向颜色渐变添加新的颜色滑块。要创建即时颜色变化，请将两个颜色滑块叠放在一起，使它们在颜色渐变上没有间隔。

![属性检查器的屏幕截图，显示一个名为“颜色渐变”的字段，带有两个颜色滑块。](../../../attachments/972c4ec532f04306df403362235413aa/sk-pe-colorramp@2x.png)

使用“混合模式”字段来确定每个粒子如何与你 App 中的其他图像进行混合。该值对应于 [SKBlendMode](../spritekit/skblendmode.md) 枚举。默认值为 [SKBlendMode.alpha](../spritekit/skblendmode/alpha.md)。

在“混合模式”弹出菜单中，选择一个选项。

![属性检查器的屏幕截图，显示一个名为“混合模式”的字段，其值为 Add。](../../../attachments/3c35a199c1c8543ffb4618cb4095e063/sk-pe-blendmode@2x.png)

使用“Alpha”字段修改粒子的透明度。粒子的颜色是通过将粒子的 alpha 值与纹理和颜色混合状态相乘得到的结果。然后，在粒子显示之前，粒子颜色会与父级的帧缓冲区（framebuffer）进行混合。

在“Alpha”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入 alpha 值。

![属性检查器的屏幕截图，显示一个名为“Alpha”的部分，包含“起始”、“范围”和“速度”字段。](../../../attachments/855a61199641648543a6f04d3e6db4f9/sk-pe-alpha@2x.png)

- **`起始`** — 应用于每个粒子的平均起始透明度值。该值对应于粒子发射器的 [particleAlpha](../spritekit/skemitternode/particlealpha.md) 属性。默认值为 `1.0`。
- **`范围`** — 粒子起始 alpha 值允许的随机值范围。该值对应于粒子发射器的 [particleAlphaRange](../spritekit/skemitternode/particlealpharange.md) 属性。默认值为 `0.0`。
- **`速度`** — alpha 值变化的速率，以每秒变化量衡量。该值对应于粒子发射器的 [particleAlphaSpeed](../spritekit/skemitternode/particlealphaspeed.md) 属性。

使用“背景”字段更改 Xcode 预览中显示的背景颜色，以帮助你想象发射器在不同环境中的外观。

在“背景”弹出菜单中，选择一种颜色。如果所需的颜色未列出，请选择“其他”以调出颜色选择器。要创建没有背景颜色的发射器，请在颜色选择器中将不透明度设置为 `0`。

![属性检查器的屏幕截图，显示一个名为“背景”的字段，带有一个颜色值。](../../../attachments/90c9dde74f821503303dcfcde587a5c7/sk-pe-background@2x.png)

你选择的背景颜色会一直保留，直到你再次更改它。Xcode 在构建 App 时会保存背景颜色，但不会在运行时使用该颜色。

### 指定运动和物理反应

你可以控制粒子创建位置以及创建后粒子移动速度和角度的不同方面。

“位置范围”字段定义了发射器创建粒子的区域。粒子是在以场景中定义的位置为中心、由位置范围值界定的矩形内创建的。

在“位置范围”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入值。

![属性检查器的屏幕截图，显示一个名为“位置范围”的部分，包含“X”、“Y”和“Z 位置”字段。](../../../attachments/5786cbcdde4c897fc57516864deb9024/sk-pe-positionrange@2x.png)

- **`X 和 Y`** — 这些值构成对应于粒子发射器 [particlePositionRange](../spritekit/skemitternode/particlepositionrange.md) 属性的向量。默认值为 (`0.0`, `0.0`)。
- **`Z 位置`** — 对应于 [particleZPosition](../spritekit/skemitternode/particlezposition.md) 属性的值。默认值为 `0.0`。

“角度”字段控制粒子远离发射器移动的方向（以度为单位）。输入 `0` 度会使粒子直接向右移动。度数按逆时针旋转工作，因此在“起始”字段中输入 `90` 会使粒子移动到屏幕顶部。

在“角度”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入角度值。

![属性检查器的屏幕截图，显示一个名为“角度”的部分，包含“起始”和“范围”字段。](../../../attachments/dad71ea089a49407d65cb90064868db3/sk-pe-angle@2x.png)

- **`起始`** — 粒子的平均初始方向。该值对应于粒子发射器的 [emissionAngle](../spritekit/skemitternode/emissionangle.md) 属性。
- **`范围`** — 粒子诞生时方向允许的随机值范围。该值对应于粒子发射器的 [emissionAngleRange](../spritekit/skemitternode/emissionanglerange.md) 属性。

> [!tip] 提示
> 度与弧度 — 粒子发射器检查器在向用户显示角度时显示度数。但是，在构建 App 时，这些度数会转换为弧度以匹配 SpriteKit API。

“速度”字段定义了粒子在创建瞬间的移动速度，以每秒点数衡量。

在“速度”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入速度值。起始值和范围值对应于粒子发射器的 [particleSpeed](../spritekit/skemitternode/particlespeed.md) 和 [particleSpeedRange](../spritekit/skemitternode/particlespeedrange.md) 属性。

![属性检查器的屏幕截图，显示一个名为“速度”的部分，包含“起始”和“范围”字段。](../../../attachments/aba1ad35f189d02f4fbcd03498af710f/sk-pe-speed@2x.png)

“加速度”字段修改粒子创建后的速度。你可以使用它来模拟整体重力效果、风吹走火焰产生的烟雾或其他效果。

在“加速度”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入加速度值。

![属性检查器的屏幕截图，显示一个名为“加速度”的部分，包含“X”和“Y”字段。](../../../attachments/cd70bd550d18f8809230fdd4fa34441a/sk-pe-acceleration@2x.png)

- **`X`** — 指定沿水平轴的加速度。该值对应于粒子发射器的 [xAcceleration](../spritekit/skemitternode/xacceleration.md) 属性。
- **`Y`** — 指定沿垂直轴的加速度。该值对应于粒子发射器的 [yAcceleration](../spritekit/skemitternode/yacceleration.md) 属性。

使用“场掩码”字段来指定可以对你的粒子施加作用力的物理场类别。默认情况下，粒子不受物理场影响。你提供的值对应于粒子发射器的 [fieldBitMask](../spritekit/skemitternode/fieldbitmask.md) 属性。

在“场掩码”字段中，双击该字段并输入场掩码值，或者点按向上或向下箭头来更改值。

![属性检查器的屏幕截图，显示一个名为“场掩码”的字段，其值为 0。](../../../attachments/a9d4da85ad3bc9c4a9e2fc7e30e8620d/sk-pe-fieldmask@2x.png)

### 调整粒子的大小和旋转

你可以调整粒子在其生命周期内的大小，并控制发射器创建粒子时粒子旋转的速度和方向。

“缩放”字段操纵默认大小，以确定每个粒子诞生时的大小，以及粒子在其生命周期内是扩大还是缩小。粒子的默认大小等于粒子纹理的大小，以点为单位。

在“缩放”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入值。

![属性检查器的屏幕截图，显示一个名为“缩放”的部分，包含“起始”、“范围”和“速度”字段。](../../../attachments/d5f137c8b0cdfd4c710cc63f115513d9/sk-pe-scale@2x.png)

- **`起始`** — 每个粒子的平均起始缩放比例，对应于粒子发射器的 [particleScale](../spritekit/skemitternode/particlescale.md) 属性。默认值 `1.0` 保持粒子的初始大小。大于 `0.0` 且小于 `1.0` 的值会减小粒子的大小，而大于 `1.0` 的值会增加粒子的大小。
- **`范围`** — 允许的随机值范围，用于修改缩放值。该范围值对应于粒子发射器的 [particleScaleRange](../spritekit/skemitternode/particlescalerange.md) 属性。默认值 `0.0` 对缩放值没有影响。
- **`速度`** — 缩放因子每秒变化的速率，对应于粒子发射器的 [particleScaleSpeed](../spritekit/skemitternode/particlescalespeed.md) 属性。默认值 `0.0` 对缩放值没有影响。

“旋转”字段控制粒子在场景中渲染时的旋转速度和方向。你可以使用这些字段来模拟落叶、旋转的雪花以及任何需要旋转的物体。

在“旋转”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入旋转值。

![属性检查器的屏幕截图，显示一个名为“旋转”的部分，包含“起始”、“范围”和“速度”字段。](../../../attachments/3250976cc6a3ea63cc46b092456e8241/sk-pe-rotation@2x.png)

- **`起始`** — 粒子的平均初始旋转角度，以弧度表示。该值对应于粒子发射器的 [particleRotation](../spritekit/skemitternode/particlerotation.md) 属性。
- **`范围`** — 允许的随机值范围，以弧度表示。该值对应于粒子发射器的 [particleRotationRange](../spritekit/skemitternode/particlerotationrange.md) 属性。
- **`速度`** — 粒子的旋转速率，以弧度/秒表示。该值对应于 [particleRotationSpeed](../spritekit/skemitternode/particlerotationspeed.md) 属性。

### 指定粒子的生命周期

你可以管理创建多少个粒子、创建的最大粒子数以及每个粒子存在的时间长度。

> [!important] 重要
> 发射器创建的粒子数量及其在屏幕上显示的时间长短直接影响你 App 的性能。

“发射器”字段控制粒子创建的频率以及创建的最大粒子数。

在“发射器”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入值。

![属性检查器的屏幕截图，显示一个名为“发射器”的部分，包含“出生率”和“最大值”字段。](../../../attachments/201cc07ab8b5b2fb8ef4e552898f53f0/sk-pe-emitter@2x.png)

- **`出生率`** — 每秒创建的粒子数。该值对应于粒子发射器的 [particleBirthRate](../spritekit/skemitternode/particlebirthrate.md) 属性。默认值为 `0.0`。
- **`最大值`** — 创建的最大粒子数。默认值为 `0`，表示发射器创建无限的粒子流。该最大值对应于粒子发射器的 [numParticlesToEmit](../spritekit/skemitternode/numparticlestoemit.md) 属性。

“生命周期”字段控制每个单独粒子在屏幕上存在的时间长度，以秒为单位。

在“生命周期”字段中，点按减号 (—) 或加号 (+) 按钮，或者双击字段并输入值。

![属性检查器的屏幕截图，显示一个名为“生命周期”的部分，包含“起始”和“范围”字段。](../../../attachments/36a135695410ae1ecade19305720be24/sk-pe-lifetime@2x.png)

- **`起始`** — 平均起始值，对应于粒子发射器的 [particleLifetime](../spritekit/skemitternode/particlelifetime.md) 属性。
- **`范围`** — 粒子生命周期允许的随机值范围，对应于粒子发射器的 [particleLifetimeRange](../spritekit/skemitternode/particlelifetimerange.md) 属性。
