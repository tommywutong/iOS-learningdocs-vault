---
title: Core Animation 编程指南
apple_id: TP40004514
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Key-ValueCodingExtensions/Key-ValueCodingExtensions.html
archived_at: '2026-07-15T07:14:03.334329Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Core Animation 编程指南](About%20Core%20Animation.md)


[下一页](Document%20Revision%20History.md)[上一页](Animatable%20Properties.md)

# 键值编码扩展

Core Animation 针对 [CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation) 和 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类扩展了 `NSKeyValueCoding` 协议。这项扩展为部分键（key）添加了默认值，扩充了包装（wrapping）约定，并为 [CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint)、[CGRect](https://developer.apple.com/documentation/coregraphics/cgrect)、[CGSize](https://developer.apple.com/documentation/coregraphics/cgsize) 和 [CATransform3D](https://developer.apple.com/documentation/quartzcore/catransform3d) 类型添加了键路径支持。

[CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation) 和 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类都是符合键值编码规范的容器类（container class），这意味着你可以为任意键设置值。即使 `someKey` 这个键并不是 `CALayer` 类中声明的属性，你依然可以像下面这样为它设置一个值：

```objc
[theLayer setValue:[NSNumber numberWithInteger:50] forKey:@"someKey"];
```

你也可以像获取其他键路径的值一样，获取任意键的值。例如，要获取前面设置的 `someKey` 路径的值，可以使用以下代码：

```objc
someKeyValue=[theLayer valueForKey:@"someKey"];
```


Core Animation 为键值编码添加了一项约定：类可以为尚未设置值的键提供一个默认值。[CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation) 和 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类通过 `defaultValueForKey:` 类方法支持这项约定。

要为某个键提供默认值，请为目标类派生一个子类，并重写其 `defaultValueForKey:` 方法。这个方法的实现应当检查传入的 key 参数，并返回相应的默认值。清单 C-1 展示了一个图层对象的 `defaultValueForKey:` 方法示例实现，它为 `masksToBounds` 属性提供了一个默认值。

__清单 C-1__  defaultValueForKey: 的示例实现

```objc

+ (id)defaultValueForKey:(NSString *)key
{
    if ([key isEqualToString:@"masksToBounds"])
         return [NSNumber numberWithBool:YES];

    return [super defaultValueForKey:key];
}
```


当某个键对应的数据是标量值或 C 数据结构时，你必须先将该类型包装成一个对象，然后才能赋值给图层。同样地，在访问该类型时，你必须先获取一个对象，然后使用相应类提供的扩展来解包出所需的值。表 C-1 列出了常用的 C 类型，以及用于包装它们的 Objective-C 类。

__表 C-1__  C 类型的包装类

| C type | Wrapping class |
| --- | --- |
| [CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint) | [NSValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/cl/NSValue) |
| [CGSize](https://developer.apple.com/documentation/coregraphics/cgsize) | `NSValue` |
| [CGRect](https://developer.apple.com/documentation/coregraphics/cgrect) | `NSValue` |
| [CATransform3D](https://developer.apple.com/documentation/quartzcore/catransform3d) | `NSValue` |
| [CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform) | [NSAffineTransform](https://developer.apple.com/documentation/foundation/nsaffinetransform)（仅限 OS X） |

[CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation) 和 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 类允许你使用键路径来访问选定数据结构中的字段。这个特性提供了一种便捷的方式，用来指定你想要进行动画处理的数据结构字段。你还可以结合 [setValue:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1418139-setvalue) 和 [valueForKeyPath:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKeyPath:) 方法，使用这些约定来设置和获取这些字段。

你可以利用增强的键路径支持，获取包含 [CATransform3D](https://developer.apple.com/documentation/quartzcore/catransform3d) 数据类型的属性中特定的变换值。要指定图层变换的完整键路径，你需要使用字符串值 `transform` 或 `sublayerTransform`，后面再跟上表 C-2 中的某个字段键路径。例如，要指定绕图层 z 轴的旋转因子，你可以指定键路径 `transform.rotation.z`。

__表 C-2__  变换字段值键路径

| Field Key Path | Description |
| --- | --- |
| `rotation.x` | 设置为一个 `NSNumber` 对象，其值是绕 x 轴的旋转量（以弧度为单位）。 |
| `rotation.y` | 设置为一个 `NSNumber` 对象，其值是绕 y 轴的旋转量（以弧度为单位）。 |
| `rotation.z` | 设置为一个 `NSNumber` 对象，其值是绕 z 轴的旋转量（以弧度为单位）。 |
| `rotation` | 设置为一个 `NSNumber` 对象，其值是绕 z 轴的旋转量（以弧度为单位）。该字段与设置 `rotation.z` 字段的效果相同。 |
| `scale.x` | 设置为一个 `NSNumber` 对象，其值是 x 轴的缩放因子。 |
| `scale.y` | 设置为一个 `NSNumber` 对象，其值是 y 轴的缩放因子。 |
| `scale.z` | 设置为一个 `NSNumber` 对象，其值是 z 轴的缩放因子。 |
| `scale` | 设置为一个 `NSNumber` 对象，其值是三个轴的缩放因子的平均值。 |
| `translation.x` | 设置为一个 `NSNumber` 对象，其值是沿 x 轴的平移量。 |
| `translation.y` | 设置为一个 `NSNumber` 对象，其值是沿 y 轴的平移量。 |
| `translation.z` | 设置为一个 `NSNumber` 对象，其值是沿 z 轴的平移量。 |
| translation | 设置为一个包含 `NSSize` 或 `CGSize` 数据类型的 `NSValue` 对象。该数据类型表示沿 x 轴和 y 轴的平移量。 |

以下示例展示了如何使用 [setValue:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1418139-setvalue) 方法修改图层。该示例将 x 轴的平移因子设置为 10 点，从而使图层沿指定轴移动相应的距离。

```objc
[myLayer setValue:[NSNumber numberWithFloat:10.0] forKeyPath:@"transform.translation.x"];
```


如果某个属性的值是 [CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint) 数据类型，你可以在该属性后面附加表 C-3 中的某个字段名来获取或设置该值。例如，要更改图层 [position](https://developer.apple.com/documentation/quartzcore/calayer/1410791-position) 属性的 x 分量，你可以写入键路径 `position.x`。

__表 C-3__  CGPoint 数据结构字段

| Structure Field | Description |
| --- | --- |
| `x` | 该点的 x 分量。 |
| `y` | 该点的 y 分量。 |

如果某个属性的值是 [CGSize](https://developer.apple.com/documentation/coregraphics/cgsize) 数据类型，你可以在该属性后面附加表 C-4 中的某个字段名来获取或设置该值。

__表 C-4__  CGSize 数据结构字段

| Structure Field | Description |
| --- | --- |
| `width` | 该尺寸的宽度分量。 |
| `height` | 该尺寸的高度分量。 |

如果某个属性的值是 [CGRect](https://developer.apple.com/documentation/coregraphics/cgrect) 数据类型，你可以在该属性后面附加表 C-3 中列出的字段名来获取或设置该值。例如，要更改图层 [bounds](https://developer.apple.com/documentation/quartzcore/calayer/1410915-bounds) 属性的 width 分量，你可以写入键路径 `bounds.size.width`。

__表 C-5__  CGRect 数据结构字段

| Structure Field | Description |
| --- | --- |
| `origin` | 以 `CGPoint` 表示的矩形原点。 |
| `origin.x` | 矩形原点的 x 分量。 |
| `origin.y` | 矩形原点的 y 分量。 |
| `size` | 以 `CGSize` 表示的矩形尺寸。 |
| `size.width` | 矩形尺寸的宽度分量。 |
| `size.height` | 矩形尺寸的高度分量。 |

[下一页](Document%20Revision%20History.md)[上一页](Animatable%20Properties.md)

