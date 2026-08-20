---
title: 数据格式化指南
apple_id: 10000029i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html
archived_at: '2026-07-15T07:14:35.440439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[下一页](Date%20Formatters.md)

# 数据格式化指南简介

你可以使用格式化器来解释和创建表示其他数据类型的字符串，并验证文本字段和其他单元格中的文本。格式化器是抽象类 `NSFormatter` 的子类的实例。Foundation [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)提供了 `NSFormatter` 的两个具体子类：`NSNumberFormatter` 和 `NSDateFormatter`。（Core Foundation 提供了两个等价的不透明类型：CFNumberFormatter 和 CFDateFormatter。它们功能类似，但不是免费桥接的。）你也可以创建 `NSFormatter` 的子类来实现自定义格式化。

你应该阅读本文档，以基本了解如何创建和使用日期与数字格式化器，以及如何创建自定义格式化器对象。

[日期格式化器](Date%20Formatters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnrzfvjvomi)介绍了如何使用日期格式化器。

[数字格式化器](Number%20Formatters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnryfvjvomi)介绍了如何使用数字格式化器。

[格式化器与用户界面元素](Formatters%20and%20User%20Interface%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgmzxfvjvomi)介绍了如何为用户界面元素设置格式化器，以及在 OS X 中元素与其格式化器之间的交互方式。

[创建自定义格式化器](Creating%20a%20Custom%20Formatter.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge4tmlkdjjbemqkcjbba)概述了如何创建自定义格式化器类。

[下一页](Date%20Formatters.md)

