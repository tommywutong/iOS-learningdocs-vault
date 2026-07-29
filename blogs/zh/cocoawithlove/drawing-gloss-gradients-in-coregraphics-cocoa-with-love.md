---
title: '在 CoreGraphics 中绘制光泽渐变 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/09/drawing-gloss-gradients-in-coregraphics.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:dab095326a94b153'
translated: true
---

> 原文：[Drawing gloss gradients in CoreGraphics | Cocoa with Love](https://www.cocoawithlove.com/2008/09/drawing-gloss-gradients-in-coregraphics.html)　·　Cocoa with Love (Matt Gallagher)

本文提供了一个函数 &mdash; `DrawGlossGradient(CGContextRef context, NSColor *color, NSRect inRect)` &mdash; 它可以用一条语句绘制出「光泽」（gloss）渐变。渐变中的所有颜色都从单一的颜色参数计算得出。

## 概述

以下示例就是光泽渐变，它们全部由下面描述的 `DrawGlossGradient` 函数生成。

![](https://www.cocoawithlove.com/assets/objc-era/gradientSample.png)

这种类型的渐变常见于网页上的按钮或其他图形装饰。Mac OS X 的「aqua」美学也在许多地方使用了这种渐变。

实际上，这个渐变由多个部分组成，所有部分都旨在模拟一个从上方照亮的半透明玻璃或塑料透镜形状的物体。

所模拟物理结构的示意图如下：

![](https://www.cocoawithlove.com/assets/objc-era/glossDiagram.png)

浅灰色的「透镜」形状就是被模拟的玻璃或塑料半透明物体。

从观察者的视角来看，上半部分主要由标记为「B」的弧线主导，这是光源直接反射到观察者的光线。

下半部分则包含两条弧的效果：C 和 A。弧 C 是一种「焦散」（caustic）高光，光源发出的光被半透明材料的透镜形状聚焦到更高强度。弧 A 较暗，因为半透明材料的凹陷特性在该区域投射了阴影。

最后要注意的一点是，透镜形状的背部并非平坦，因此这些亮部和暗部成分以非线性方式衰减。

## 在代码中实现此效果

我们需要四种不同的颜色值：

- 光泽高光的顶部（因反射入射角而最白）
- 光泽高光的底部（偏白，但不如顶部白）
- 背景颜色——阴影中最暗的可见部分（将作为函数输入提供）
- 焦散颜色（比背景亮，并包含微妙的色调变化）

拥有这些值后，我们就可以直接用它们创建一个渐变。

> 我将使用 CoreGraphics 的 `CGShadingRef`。用 `NSGradient` 也可以产生相当类似的效果，但该类只支持恒定斜率的渐变，而我希望在渐变中加入微妙的指数变化。

## 光泽高光颜色

两种光泽高光颜色将只是白色和背景颜色的混合。选择这两种颜色的相对强度并不太难。我为顶部光泽颜色选择了 0.6 的白色比例，为底部光泽选择了 0.2（尽管这些比例会被下面的缩放减小）。

当使用一系列背景颜色时，我发现深色需要比浅色更小的白色比例才能看起来同样光泽，因此我必须根据背景亮度来缩放效果。

我选择了以下函数来根据背景颜色的亮度为光泽亮度生成一个缩放系数：

```objc
float perceptualGlossFractionForColor(float *inputComponents)
{
    const float REFLECTION_SCALE_NUMBER = 0.2;
    const float NTSC_RED_FRACTION = 0.299;
    const float NTSC_GREEN_FRACTION = 0.587;
    const float NTSC_BLUE_FRACTION = 0.114;

    float glossScale =
        NTSC_RED_FRACTION * inputComponents[0] +
        NTSC_GREEN_FRACTION * inputComponents[1] +
        NTSC_BLUE_FRACTION * inputComponents[2];
    glossScale = pow(glossScale, REFLECTION_SCALE_NUMBER);
    return glossScale;
}
```

输入分量是 3 个浮点数（RGB）。我用来乘它们的系数是 NTSC 颜色到亮度转换系数。对于颜色而言，这是一种可接受的「感知亮度」转换，并且比 RGB 到 LUV 转换简单得多。然后我将该值提升到一个小数次幂——该值是实验选择的，因为它在整个亮度范围内似乎能给出大致正确的最终值。

## 焦散高光颜色

焦散颜色是一个更难的问题。我们需要实现背景颜色向黄色的色调和亮度偏移，同时保持背景的饱和度。

同样，与光泽一样，存在一个非线性问题需要处理：色调上离黄色更远的颜色需要按比例减少色调偏移，以维持相同色调偏移效果的视觉表现。我选择用一个余弦来缩放色调偏移，使得色调偏移在视觉上显得合适。

此外，灰色（没有真正色调）需要特殊处理。红色需要特殊处理，因为色调在红色处会回绕。紫色向黄色偏移后视觉效果不佳，因此我决定让它们向品红色偏移。

```objc
void perceptualCausticColorForColor(float *inputComponents, float *outputComponents)
{
    const float CAUSTIC_FRACTION = 0.60;
    const float COSINE_ANGLE_SCALE = 1.4;
    const float MIN_RED_THRESHOLD = 0.95;
    const float MAX_BLUE_THRESHOLD = 0.7;
    const float GRAYSCALE_CAUSTIC_SATURATION = 0.2;
    
    NSColor *source =
        [NSColor
            colorWithCalibratedRed:inputComponents[0]
            green:inputComponents[1]
            blue:inputComponents[2]
            alpha:inputComponents[3]];

    float hue, saturation, brightness, alpha;
    [source getHue:&amp;hue saturation:&amp;saturation brightness:&amp;brightness alpha:&amp;alpha];

    float targetHue, targetSaturation, targetBrightness;
    [[NSColor yellowColor] getHue:&amp;targetHue saturation:&amp;targetSaturation brightness:&amp;targetBrightness alpha:&amp;alpha];
    
    if (saturation &lt; 1e-3)
    {
        hue = targetHue;
        saturation = GRAYSCALE_CAUSTIC_SATURATION;
    }

    if (hue &gt; MIN_RED_THRESHOLD)
    {
        hue -= 1.0;
    }
    else if (hue &gt; MAX_BLUE_THRESHOLD)
    {
        [[NSColor magentaColor] getHue:&amp;targetHue saturation:&amp;targetSaturation brightness:&amp;targetBrightness alpha:&amp;alpha];
    }

    float scaledCaustic = CAUSTIC_FRACTION * 0.5 * (1.0 + cos(COSINE_ANGLE_SCALE * M_PI * (hue - targetHue)));

    NSColor *targetColor =
        [NSColor
            colorWithCalibratedHue:hue * (1.0 - scaledCaustic) + targetHue * scaledCaustic
            saturation:saturation
            brightness:brightness * (1.0 - scaledCaustic) + targetBrightness * scaledCaustic
            alpha:inputComponents[3]];
    [targetColor getComponents:outputComponents];
}
```

所以这个函数实际上只是 `inputComponents` 和 `yellowColor` 的 HSV 转换，以及两者的混合。

## 组合成单一渐变

现在将颜色组合成一个渐变。我们需要实现一个插值函数，该函数将为渐变中的给定进度点返回正确的颜色。

将前述的「背景颜色」、「焦散颜色」、「顶部光泽白色比例」和「底部光泽白色比例」作为 `GlossParameters` 结构体的 `color`、`caustic`、`initialWhite` 和 `finalWhite` 参数传入此函数后，函数如下：

```objc
typedef struct
{
    float color[4];
    float caustic[4];
    float expCoefficient;
    float expScale;
    float expOffset;
    float initialWhite;
    float finalWhite;
} GlossParameters;

static void glossInterpolation(void *info, const float *input,
    float *output)
{
    GlossParameters *params = (GlossParameters *)info;

    float progress = *input;
    if (progress &lt; 0.5)
    {
        progress = progress * 2.0;

        progress =
            1.0 - params-&gt;expScale * (expf(progress * -params-&gt;expCoefficient) - params-&gt;expOffset);

        float currentWhite = progress * (params-&gt;finalWhite - params-&gt;initialWhite) + params-&gt;initialWhite;
        
        output[0] = params-&gt;color[0] * (1.0 - currentWhite) + currentWhite;
        output[1] = params-&gt;color[1] * (1.0 - currentWhite) + currentWhite;
        output[2] = params-&gt;color[2] * (1.0 - currentWhite) + currentWhite;
        output[3] = params-&gt;color[3] * (1.0 - currentWhite) + currentWhite;
    }
    else
    {
        progress = (progress - 0.5) * 2.0;

        progress = params-&gt;expScale *
            (expf((1.0 - progress) * -params-&gt;expCoefficient) - params-&gt;expOffset);

        output[0] = params-&gt;color[0] * (1.0 - progress) + params-&gt;caustic[0] * progress;
        output[1] = params-&gt;color[1] * (1.0 - progress) + params-&gt;caustic[1] * progress;
        output[2] = params-&gt;color[2] * (1.0 - progress) + params-&gt;caustic[2] * progress;
        output[3] = params-&gt;color[3] * (1.0 - progress) + params-&gt;caustic[3] * progress;
    }
}
```

如你所见，函数分为两半：前半部分处理光泽，后半部分处理焦散。使用指数来使渐变产生衰减效果。

## 绘制渐变

绘制函数非常直接。大部分工作是将 `GlossParameters` 结构体的指数系数和偏移量配置好，调用函数生成所需颜色，然后使用 `CGShadingCreateAxial` 和 `CGContextDrawShading` 执行绘制渐变的机制。

```objc
void DrawGlossGradient(CGContextRef context, NSColor *color, NSRect inRect)
{
    const float EXP_COEFFICIENT = 1.2;
    const float REFLECTION_MAX = 0.60;
    const float REFLECTION_MIN = 0.20;
    
    GlossParameters params;
    
    params.expCoefficient = EXP_COEFFICIENT;
    params.expOffset = expf(-params.expCoefficient);
    params.expScale = 1.0 / (1.0 - params.expOffset);

    NSColor *source =
        [color colorUsingColorSpaceName:NSCalibratedRGBColorSpace];
    [source getComponents:params.color];
    if ([source numberOfComponents] == 3)
    {
        params.color[3] = 1.0;
    }
    
    perceptualCausticColorForColor(params.color, params.caustic);
    
    float glossScale = perceptualGlossFractionForColor(params.color);

    params.initialWhite = glossScale * REFLECTION_MAX;
    params.finalWhite = glossScale * REFLECTION_MIN;

    static const float input_value_range[2] = {0, 1};
    static const float output_value_ranges[8] = {0, 1, 0, 1, 0, 1, 0, 1};
    CGFunctionCallbacks callbacks = {0, glossInterpolation, NULL};
    
    CGFunctionRef gradientFunction = CGFunctionCreate(
        (void *)&amp;params,
        1, // number of input values to the callback
        input_value_range,
        4, // number of components (r, g, b, a)
        output_value_ranges,
        &amp;callbacks);
    
    CGPoint startPoint = CGPointMake(NSMinX(inRect), NSMaxY(inRect));
    CGPoint endPoint = CGPointMake(NSMinX(inRect), NSMinY(inRect));

    CGColorSpaceRef colorspace = CGColorSpaceCreateDeviceRGB();
    CGShadingRef shading = CGShadingCreateAxial(colorspace, startPoint,
        endPoint, gradientFunction, FALSE, FALSE);
    
    CGContextSaveGState(context);
    CGContextClipToRect(context, NSRectToCGRect(inRect));
    CGContextDrawShading(context, shading);
    CGContextRestoreGState(context);
    
    CGShadingRelease(shading);
    CGColorSpaceRelease(colorspace);
    CGFunctionRelease(gradientFunction);
}
```

## 结论

这些函数中有很多参数可以根据个人喜好进行调整。你可以非常简单地增强色调变化、渐变斜率和光泽强度。

我对光泽及其亮度相当满意。我认为效果不错。

焦散的色调偏移效果良好，但焦散的亮度似乎有些不一致。这可以稍微调整一下。

位于蓝色或红色边界附近的紫色可能看起来有些奇怪。也许有办法平滑处理，我不知道。我没有仔细考虑过。

这种方法不适用于作为输入颜色的亮色，因为输入颜色被用作渐变中最暗的颜色。与其说这是一个问题，不如说是在选择输入颜色时需要考虑的一点。
