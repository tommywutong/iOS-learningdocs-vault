---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtVersionsPlatforms.html
archived_at: '2026-07-15T07:17:29.408042Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 运行时编程指南](Introduction.md)


[下一页](Interacting%20with%20the%20Runtime.md)[上一页](Introduction.md)

# 运行时版本与平台

不同平台上的 Objective-C 运行时（runtime）版本各不相同。

Objective-C 运行时有两个版本——“现代版”和“旧版”。现代版随 Objective-C 2.0 一同引入，包含若干新特性。旧版运行时的编程接口在 _Objective-C 1 Runtime Reference_ 中有说明；现代版运行时的编程接口在 _[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ 中有说明。

最值得注意的新特性是现代版运行时中的实例变量是“非脆弱的”（non-fragile）：

- 在旧版运行时中，如果你改变了某个类中实例变量的布局，就必须重新编译继承自它的类。
- 在现代版运行时中，如果你改变了某个类中实例变量的布局，无需重新编译继承自它的类。

此外，现代版运行时支持为声明属性合成实例变量（参见 _[Objective-C 编程语言](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 中的 [声明属性](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html#//apple_ref/doc/uid/TP30001163-CH17)）。

iPhone 应用程序以及 OS X v10.5 及更高版本上的 64 位程序使用现代版运行时。

其他程序（OS X 桌面上的 32 位程序）使用旧版运行时。

[下一页](Interacting%20with%20the%20Runtime.md)[上一页](Introduction.md)

