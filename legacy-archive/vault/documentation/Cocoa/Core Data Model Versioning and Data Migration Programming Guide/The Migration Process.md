---
title: Core Data 模型版本管理与数据迁移编程指南
apple_id: TP40004399
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/vmMigrationProcess.html
archived_at: '2026-07-15T07:14:29.249715Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 模型版本管理与数据迁移编程指南](Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md)


[下一页](Initiating%20the%20Migration%20Process.md)[上一页](Mapping%20Overview.md)

# 迁移过程

在迁移过程中，Core Data 会创建两个技术栈，一个用于源存储，一个用于目标存储。然后 Core Data 从源技术栈中获取对象，并将相应的对应对象插入目标技术栈中。请注意，Core Data 必须在新的技术栈中_重新创建_对象。

回忆一下，存储是与其模型绑定的。当模型与存储不匹配时，就需要进行迁移。有两个环节你可以获得默认功能，也可以定制默认行为：

- 检测版本偏差并初始化迁移过程时。
- 执行迁移过程时。

要执行迁移过程，需要两个 Core Data 技术栈——这两个栈会自动为你创建——一个用于源存储，一个用于目标存储。迁移过程分三个阶段执行，将对象从一个技术栈拷贝到另一个技术栈。

持久化存储的迁移由 [NSMigrationManager](https://developer.apple.com/documentation/coredata/nsmigrationmanager) 的实例执行。要迁移一个存储，迁移管理器需要以下几样东西：

- 目标存储的托管对象模型。

  这就是持久化存储协调器所使用的模型。
- 一个可用于打开现有存储的托管对象模型。
- 通常还需要一个映射模型，用于定义从源模型（该存储的模型）到目标模型的转换。

  如果你能够使用轻量级迁移，就不需要映射模型——参见 [Lightweight Migration](Lightweight%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnbnknltc)。

你可以指定自定义的实体迁移策略类，来定制单个实体的迁移方式。自定义迁移策略类是在映射模型中指定的（参见 [图 4-1](Mapping%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqnjnknlti) 中的"Custom Entity Policy Name"文本框）。

如果你的新模型只是在原有模型的基础上添加了属性或实体，可能根本不需要编写任何自定义代码。但如果转换更为复杂，你可能需要创建 [NSEntityMigrationPolicy](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy) 的子类来执行该转换，例如：

- 如果你有一个 Person 实体，其中还包含地址信息，而你想把地址信息拆分到一个单独的 Address 实体中，同时确保每个 Address 的唯一性。
- 如果你有一个以字符串格式编码数据的属性，而你想把它改为二进制表示形式。

在自定义迁移策略中要重写的方法，对应迁移过程的不同阶段——这些方法会在下面对"三阶段迁移"过程的说明中一一指出。

迁移过程本身分为三个阶段。它使用源模型和目标模型的一个拷贝，其中校验规则被禁用，且所有实体的类都被改为 `NSManagedObject`。

为执行迁移，Core Data 会建立两个技术栈，一个用于源存储，一个用于目标存储。然后 Core Data 依次处理映射模型中的每一个实体映射。它会将当前实体的对象获取到源技术栈中，在目标技术栈中创建对应的对象，然后在第二阶段重新创建目标对象之间的关系，最后在最后一个阶段应用校验约束。

在一个周期开始之前，负责当前实体的实体迁移策略会收到一条 [beginEntityMapping:manager:error:](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423785-beginentitymapping) 消息。你可以重写这个方法，执行该策略所需的任何初始化操作。此后该过程按如下方式进行：

1. 根据源实例创建目标实例。

   在此阶段开始时，实体迁移策略会收到一条 [createDestinationInstancesForSourceInstance:entityMapping:manager:error:](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423801-createdestinationinstancesforsou) 消息；结束时会收到一条 [endInstanceCreationForEntityMapping:manager:error:](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423805-endinstancecreationforentitymapp) 消息。

   在这一阶段，只有属性（不包括关系）会被设置到目标对象中。

   源实体的实例会被获取出来。对每个实例，都会创建相应的目标实体实例（通常只有一个），并填充其属性（对于简单情形，即 `name = $source.name`）。系统会为每个实体映射保留一份实例记录，因为这在第二阶段可能会用到。
2. 重新创建关系。

   在此阶段开始时，实体迁移策略会收到一条 [createRelationshipsForDestinationInstance:entityMapping:manager:error:](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423783-createrelationships) 消息；结束时会收到一条 [endRelationshipCreationForEntityMapping:manager:error:](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423793-endrelationshipcreation) 消息。

   对于每个实体映射（按顺序），针对第一阶段中创建的每个目标实例，重新创建其所有关系。
3. 校验并保存。

   在这一阶段，实体迁移策略会收到一条 [performCustomValidationForEntityMapping:manager:error:](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423791-performcustomvalidationforentity) 消息。

   系统会应用目标模型中的校验规则，以确保数据的完整性和一致性，然后保存该存储。

在该周期结束时，实体迁移策略会收到一条 [endEntityMapping:manager:error:](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/1423787-endentitymapping) 消息。你可以重写这个方法，执行该策略所需的任何清理工作。

请注意，Core Data 不能只是简单地把对象获取到源技术栈中，再插入目标技术栈中；这些对象必须在新的技术栈中被重新创建。Core Data 维护着"关联表"，用于记录目标存储中的哪个对象是源存储中哪个对象迁移而来的版本，反之亦然。此外，由于它没有办法刷新（flush）自己正在使用的上下文，随着迁移的推进，迁移管理器中可能会积累大量对象。如果这带来了显著的内存开销，进而引发性能问题，你可以按照 [Multiple Passes—Dealing With Large Datasets](Customizing%20the%20Migration%20Process.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojzfvbuqobnknlts) 中所述的方式定制该过程。

[下一页](Initiating%20the%20Migration%20Process.md)[上一页](Mapping%20Overview.md)
