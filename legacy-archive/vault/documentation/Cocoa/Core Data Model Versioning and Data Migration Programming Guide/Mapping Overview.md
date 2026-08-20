---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/vmMappingOverview.html
archived_at: '2026-07-15T07:14:29.031525Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 模型版本管理与数据迁移编程指南](Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md)


[下一页](The%20Migration%20Process.md)[上一页](Lightweight%20Migration.md)

# 映射概述

在很多情况下，Core Data 能够自行推断出如何将数据从一种模式转换为另一种模式（参见 [Lightweight Migration](Lightweight%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnbnknltc)）。如果 Core Data 无法推断出从一个模型到另一个模型的映射，你就需要自己定义如何执行这种转换。这些信息记录在一个映射模型（mapping model）中。

_映射模型_ 是一组对象的集合，用于指定将存储的一部分从模型的一个版本迁移到另一个版本所需的转换（例如，某个实体被重命名，某个属性被添加到另一个实体，或者某个实体被拆分为两个）。你通常在 Xcode 中创建映射模型。正如托管对象模型编辑器让你能够以图形方式创建模型一样，映射模型编辑器也让你能够定制源实体/属性与目标实体/属性之间的映射关系。

与托管对象模型一样，映射模型也是一组对象的集合。映射模型的类与托管对象模型的类一一对应——分别有针对模型、实体和属性的映射类（[NSMappingModel](https://developer.apple.com/documentation/coredata/nsmappingmodel)、[NSEntityMapping](https://developer.apple.com/documentation/coredata/nsentitymapping) 和 [NSPropertyMapping](https://developer.apple.com/documentation/coredata/nspropertymapping)）。

- `NSEntityMapping` 的实例指定一个源实体、一个目标实体（对应源对象要创建的对象类型），以及映射类型（添加、移除、原样拷贝，或转换）。
- `NSPropertyMapping` 的实例指定源实体和目标实体中属性的名称，以及一个用于生成目标属性值的值表达式。

该模型不包含 [NSEntityMigrationPolicy](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy) 或其任何子类的实例，不过在其他属性之外，`NSEntityMapping` 的实例可以指定要用于定制迁移过程的实体迁移策略类（[NSEntityMigrationPolicy](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy) 的子类）的_名称_。关于实体迁移策略类的更多内容，请参阅 [Custom Entity Migration Policies](The%20Migration%20Process.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnrnknlti)。

你可以直接在 Xcode 的映射模型编辑器中，通过在属性映射上配置自定义值表达式，来处理简单的属性迁移变化。例如，你可以：

- 将数据从一个属性迁移到另一个属性。

  要把 `amount` 重命名为 `totalCost`，可以将 `totalCost` 属性映射的自定义值表达式设为 `$source.amount`。
- 对某个属性应用一次值转换。

  要把 `temperature` 从华氏度转换为摄氏度，可以使用自定义值表达式 `($source.temperature - 32.0) / 1.8`。
- 将对象从一个关系迁移到另一个关系。

  要把 `trades` 重命名为 `transactions`，可以将 transactions 属性映射的自定义值表达式设为 `FUNCTION($manager, "destinationInstancesForEntityMappingNamed:sourceInstances:", "TradeToTrade", $source.trades)`。（这里假设迁移 Trade 实例的实体映射名为 TradeToTrade。）

在自定义值表达式中，有六个预定义的键可供引用。要在源代码中访问这些键，可使用所声明的常量；要在 Xcode 映射模型编辑器的自定义值表达式字符串中访问它们，需遵循谓词格式字符串语法指南中列出的语法规则，并按以下方式引用：

[NSMigrationManagerKey](https://developer.apple.com/documentation/coredata/nsmigrationmanagerkey)：`$manager`

[NSMigrationSourceObjectKey](https://developer.apple.com/documentation/coredata/nsmigrationsourceobjectkey)：`$source`

[NSMigrationDestinationObjectKey](https://developer.apple.com/documentation/coredata/nsmigrationdestinationobjectkey)：`$destination`

[NSMigrationEntityMappingKey](https://developer.apple.com/documentation/coredata/nsmigrationentitymappingkey)：`$entityMapping`

[NSMigrationPropertyMappingKey](https://developer.apple.com/documentation/coredata/nsmigrationpropertymappingkey)：`$propertyMapping`

[NSMigrationEntityPolicyKey](https://developer.apple.com/documentation/coredata/nsmigrationentitypolicykey)：`$entityPolicy`

从 File 菜单中选择 New File，在 New File 面板中选择 Design > Mapping Model。在随后出现的面板中，选择源模型和目标模型。点击 Finish 后，Xcode 会创建一个新的映射模型，其中包含它能从源模型和目标模型推断出的尽可能多的默认映射。例如，给定 [图 1-1](Understanding%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqmrnknlte) 和 [图 1-2](Understanding%20Versions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqmrnknltg) 所示的模型文件，Xcode 会创建出如图 4-1 所示的映射模型。

__图 4-1__  Core Recipes 模型 1-2 版之间的映射模型

!!

[下一页](The%20Migration%20Process.md)[上一页](Lightweight%20Migration.md)
