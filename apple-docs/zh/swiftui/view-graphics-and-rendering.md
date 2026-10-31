---
title: 图形与渲染修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-graphics-and-rendering
source_url: 'https://developer.apple.com/documentation/swiftui/view-graphics-and-rendering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-graphics-and-rendering.json'
content_hash: 'sha256:e679f6be14037b0f'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 图形与渲染修饰符

<sub>API 集合</sub>

影响系统绘制视图的方式，例如缩放或遮罩视图，或者应用图形效果。

## 概述

使用这些视图修饰符来应用许多通常与图形上下文相关的渲染效果，例如添加遮罩和创建合成图像。你可以把这些效果应用到图形视图（例如 [Shapes](shapes.md)）以及任何其他 SwiftUI 视图上。

当你确实需要图形上下文中即时模式绘制的灵活性时，请改用 [Canvas](canvas.md) 视图。当你想要绘制数量极其庞大的动态形状时——例如创建粒子效果——这会特别有帮助。

有关在你的 App 中使用这些效果的更多信息，请参阅[绘图与图形](drawing-and-graphics.md)。

## 主题

### 遮罩与裁剪

- [mask(alignment:_:)](<view/mask(alignment___).md>) — 使用给定视图的 alpha 通道遮罩此视图。
- [clipped(antialiased:)](<view/clipped(antialiased_).md>) — 将此视图裁剪到其边界矩形 frame。
- [clipShape(_:style:)](<view/clipshape(__style_).md>) — 为此视图设置裁剪形状。
- [containerShape(_:)](<view/containershape(__).md>) — 设置此视图内任何容器相对形状或同心矩形所使用的容器形状。

### 缩放

- [scaledToFill()](<view/scaledtofill().md>) — 缩放此视图以填满其父视图。
- [scaledToFill3D()](<view/scaledtofill3d().md>) — 缩放此视图以填满其父视图。
- [scaledToFit()](<view/scaledtofit().md>) — 缩放此视图以适应其父视图。
- [scaledToFit3D()](<view/scaledtofit3d().md>) — 缩放此视图以适应其父视图。
- [scaleEffect(_:anchor:)](<view/scaleeffect(__anchor_).md>) — 相对于一个锚点，按指定因子均匀缩放此视图。
- [scaleEffect(x:y:anchor:)](<view/scaleeffect(x_y_anchor_).md>) — 相对于一个锚点，按给定的水平和垂直量缩放此视图的渲染输出。
- [scaleEffect(x:y:z:anchor:)](<view/scaleeffect(x_y_z_anchor_).md>) — 相对于一个锚点，按指定的水平、垂直和深度因子缩放此视图。
- [imageScale(_:)](<view/imagescale(__).md>) — 根据可用的相对尺寸（例如小、中、大图像尺寸）缩放视图内的图像。
- [aspectRatio(_:contentMode:)](<view/aspectratio(__contentmode_).md>) — 将此视图的尺寸约束为指定的宽高比。
- [aspectRatio3D(_:contentMode:)](<view/aspectratio3d(__contentmode_).md>) — 将此视图的尺寸约束为指定的 3D 宽高比。

### 旋转与变换

- [rotationEffect(_:anchor:)](<view/rotationeffect(__anchor_).md>) — 围绕指定点在二维空间中旋转视图的渲染输出。
- [rotation3DEffect(_:anchor:)](<view/rotation3deffect(__anchor_).md>) — 按指定的 3D 旋转值旋转视图的内容。
- [rotation3DEffect(_:axis:anchor:anchorZ:perspective:)](<view/rotation3deffect(__axis_anchor_anchorz_perspective_).md>) — 渲染视图的内容，如同它围绕指定的轴在三维空间中旋转。
- [rotation3DEffect(_:axis:anchor:)](<view/rotation3deffect(__axis_anchor_).md>) — 围绕一个以元素元组形式指定的轴，按某个角度旋转视图的内容。
- [rotation3DLayout(_:)](<view/rotation3dlayout(__).md>) — 旋转视图，同时影响其在包含布局中的 frame
- [rotation3DLayout(_:axis:)](<view/rotation3dlayout(__axis_).md>) — 旋转视图，同时影响其在包含布局中的 frame
- [perspectiveRotationEffect(_:axis:anchor:anchorZ:perspective:)](<view/perspectiverotationeffect(__axis_anchor_anchorz_perspective_).md>) — 渲染视图的内容，如同它围绕指定的轴在三维空间中旋转。
- [projectionEffect(_:)](<view/projectioneffect(__).md>) — 对此视图的渲染输出应用投影变换。
- [transformEffect(_:)](<view/transformeffect(__).md>) — 对此视图的渲染输出应用仿射变换。
- [transform3DEffect(_:)](<view/transform3deffect(__).md>) — 对此视图的渲染输出应用 3D 变换。

### 图形效果

- [blur(radius:opaque:)](<view/blur(radius_opaque_).md>) — 对此视图应用高斯模糊。
- [opacity(_:)](<view/opacity(__).md>) — 设置此视图的不透明度。
- [brightness(_:)](<view/brightness(__).md>) — 按指定量提亮此视图。
- [contrast(_:)](<view/contrast(__).md>) — 设置此视图中相似颜色之间的对比度和分离度。
- [colorInvert()](<view/colorinvert().md>) — 反转此视图中的颜色。
- [colorMultiply(_:)](<view/colormultiply(__).md>) — 为此视图添加颜色相乘效果。
- [saturation(_:)](<view/saturation(__).md>) — 调整此视图的颜色饱和度。
- [grayscale(_:)](<view/grayscale(__).md>) — 为此视图添加灰度效果。
- [hueRotation(_:)](<view/huerotation(__).md>) — 对此视图应用色相旋转效果。
- [luminanceToAlpha()](<view/luminancetoalpha().md>) — 为此视图添加亮度转 alpha 效果。
- [shadow(color:radius:x:y:)](<view/shadow(color_radius_x_y_).md>) — 为此视图添加阴影。
- [visualEffect(_:)](<view/visualeffect(__).md>) — 对此视图应用效果，同时通过几何代理提供对布局信息的访问。
- [visualEffect3D(_:)](<view/visualeffect3d(__).md>) — 对此视图应用效果，同时通过 3D 几何代理提供对布局信息的访问。
- [materialActiveAppearance(_:)](<view/materialactiveappearance(__).md>) — 为此视图中的材质设置显式的活跃外观。

### 着色器

- [colorEffect(_:isEnabled:)](<view/coloreffect(__isenabled_).md>) — 返回一个新视图，它将 `shader` 应用到 `self`，作为对每个像素颜色的滤镜效果。
- [distortionEffect(_:maxSampleOffset:isEnabled:)](<view/distortioneffect(__maxsampleoffset_isenabled_).md>) — 返回一个新视图，它将 `shader` 应用到 `self`，作为对每个像素位置的几何扭曲效果。
- [layerEffect(_:maxSampleOffset:isEnabled:)](<view/layereffect(__maxsampleoffset_isenabled_).md>) — 返回一个新视图，它将 `shader` 应用到由 `self` 创建的光栅图层，作为其上的滤镜。

### 合成

- [blendMode(_:)](<view/blendmode(__).md>) — 设置此视图与重叠视图合成时所使用的混合模式。
- [compositingGroup()](<view/compositinggroup().md>) — 将此视图包裹在一个合成组中。
- [drawingGroup(opaque:colorMode:)](<view/drawinggroup(opaque_colormode_).md>) — 在最终显示之前将此视图的内容合成为一张离屏图像。

### 动画

- [animation(_:)](<view/animation(__).md>) — 在此视图发生变化时将给定的动画应用到该视图。
- [animation(_:value:)](<view/animation(__value_).md>) — 在指定值发生变化时将给定的动画应用到该视图。
- [animation(_:body:)](<view/animation(__body_).md>) — 将给定的动画应用到 `body` 闭包内的所有可动画值。
- [contentTransition(_:)](<view/contenttransition(__).md>) — 修改视图，使用给定的过渡作为对其视图内容变化添加动画的方法。
- [geometryGroup()](<view/geometrygroup().md>) — 将视图的几何属性（例如位置和大小）与其父视图隔离开。
- [keyframeAnimator(initialValue:repeating:content:keyframes:)](<view/keyframeanimator(initialvalue_repeating_content_keyframes_).md>) — 连续循环给定的关键帧，使用你在 `body` 中应用的修饰符更新视图。
- [keyframeAnimator(initialValue:trigger:content:keyframes:)](<view/keyframeanimator(initialvalue_trigger_content_keyframes_).md>) — 当给定的触发值发生变化时播放给定的关键帧，使用你在 `body` 中应用的修饰符更新视图。
- [matchedGeometryEffect(id:in:properties:anchor:isSource:)](<view/matchedgeometryeffect(id_in_properties_anchor_issource_).md>) — 使用你提供的标识符和命名空间定义一组具有同步几何属性的视图。
- [matchedTransitionSource(id:in:)](<view/matchedtransitionsource(id_in_).md>) — 将此视图标识为导览过渡（例如缩放过渡）的来源。
- [matchedTransitionSource(id:in:configuration:)](<view/matchedtransitionsource(id_in_configuration_).md>) — 将此视图标识为导览过渡（例如缩放过渡）的来源。
- [phaseAnimator(_:content:animation:)](<view/phaseanimator(__content_animation_).md>) — 让你应用于视图的效果在一系列持续变化的阶段上生成动画。
- [phaseAnimator(_:trigger:content:animation:)](<view/phaseanimator(__trigger_content_animation_).md>) — 让你应用于视图的效果在一系列基于触发器变化的阶段上生成动画。
- [transition(_:)](<view/transition(__).md>) — 将一个过渡与该视图关联。
- [transaction(_:)](<view/transaction(__).md>) — 将给定的事务变更函数应用到视图内使用的所有动画。
- [transaction(value:_:)](<view/transaction(value___).md>) — 将给定的事务变更函数应用到视图内使用的所有动画。
- [transaction(_:body:)](<view/transaction(__body_).md>) — 将给定的事务变更函数应用到 `body` 闭包内使用的所有动画。

## 另请参阅

### 绘图视图

- [样式修饰符](view-style-modifiers.md) — 为不同类型的视图应用内置样式。
- [布局修饰符](view-layout.md) — 通过调整视图的大小、位置、对齐方式、内边距等，告知视图如何在视图层级结构中安排自身。
