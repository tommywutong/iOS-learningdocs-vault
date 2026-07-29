---
title: 在 Core Data 中立即传播删除 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/04/propagate-deletes-immediately-in-core.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:a373cc4a79a498fe'
translated: true
---

> 原文：[Propagate deletes immediately in Core Data | Cocoa with Love](https://www.cocoawithlove.com/2008/04/propagate-deletes-immediately-in-core.html)　·　Cocoa with Love (Matt Gallagher)

了解 Core Data 中层叠删除的一些限制，并学习如何在 Core Data 中立即传播删除，从而克服这些潜在问题。

> **更正**：本文此前指出，NSManagedObject 的删除会在 `processPendingChanges` 内部失败。该问题已在 Mac OS X 10.5 中修复。本文已进行编辑，以反映在 Mac OS X 10.5 中，只有 `processPendingChanges` 无法在其自身内部被调用。

## 默认 "deleteObject" 在变更传播中的局限性

Core Data 能够通过对象模型中每个实体可用的 "cascade" 删除规则，执行完整的对象图删除。

如果你已经为模型实体上的关系覆写了键值编码（Key Value Coding）方法，可能会遇到以下问题。

### 始终延迟

Core Data 中的删除始终是延迟的，要么延迟到事件结束时（当 `-[NSManagedObjectContext processPendingChanges]` 下次被调用时），要么延迟到上下文被保存时。

这意味着，如果你想读取因删除而改变的值，必须：

- 不在 `-[NSManagedObjectContext processPendingChanges]` 调用内部（即在删除传播期间）
- 在删除后调用 `-[NSManagedObjectContext processPendingChanges]`，以刷新整个操作

如果你位于 `processPendingChanges` 内部（或者你出于其他原因不想调用它），但又需要立即看到变更，那么你需要实现自己的变更传播，而不是依赖默认的 `deleteObject:` 来应用变更。

### 关系删除顺序不确定

"cascade" 删除规则不会按特定顺序遍历关系进行删除。如果你需要以特定顺序删除关系（例如，在删除期间你可能从对象中读取数据），你将需要实现自己的变更传播。

### 10.4 中不支持递归删除

在 Mac OS X 10.4 中，Core Data 的删除传播与递归调用的删除不兼容。如果一个删除传播在其执行过程中触发了另一个删除传播，则第二个传播将不会生效（它不会产生任何效果）。

## 这些问题如何发生的一个示例

考虑以下 .xcdatamodel：

![](https://www.cocoawithlove.com/assets/objc-era/propagatedelete.png)

在这个示例中，"A" 为其属性使用了 "cascade" 删除规则，而 "B" 和 "C" 使用了 "nullify"。

我们的程序必须遵守以下规则：

我们的程序通过覆写 "A" 类的键值编码方法来维护此规则。

`addBObject:` 方法被覆写为在 "b" 属性改变之前创建一个 C 对象并将其添加到 "A" 对象的 "c" 属性中。类似地，`removeBObject:` 方法被覆写为在 "b" 属性改变之后删除 "A" 对象的 "c" 属性中匹配的 C 对象。

通过在 "b" 属性改变**之前**添加 C 对象，并在 "b" 属性改变**之后**删除 C 对象，我们确保了当一个 "B" 对象附加到 "A" 对象上时，总是有一个匹配的 "C" 对象附加在上面。

一旦我们删除了 "C" 对象，我们就使用 `NSAssert` 来检查附加到 "A" 上的 "B" 对象和 "C" 对象的数量是否相同。为了确保在读取之前 "C" 对象已经被删除，我们必须调用 `processPendingChanges` 来刷新删除操作。

### 嵌套的 processPendingChanges 的问题

上述示例可以正常工作，除非它是从删除传播内部被调用的。

如果我们删除一个 "B" 对象，而不是简单地从 "A" 中移除它，那么移除动作发生在针对 "B" 对象删除的 `processPendingChanges` 内部。

在 Mac OS X 10.4 中，`removeBObject:` 里的 `deleteObject:` 调用在 `processPendingChanges` 内部无法正常工作。这是一个文档化的限制。在 Mac OS X 10.4 中，任何在覆写的访问方法中使用 `deleteObject:` 的地方，都应自行传播删除。

在 Mac OS X 10.5 中，`removeBObject:` 中对 `processPendingChanges` 的调用将不起作用。这意味着 `NSAssert` 会失败。

在这个简单的示例中，`NSAssert` 并不重要，但这表明，如果你需要在删除期间刷新删除操作以立即读回数据，并且你可能在删除传播中需要此功能，那么你需要自行传播此删除。

### 删除顺序的问题

如果你删除一个 "A" 对象，那么你无法控制 "b" 属性还是 "c" 属性先被删除。

"C" 属性可能先被删除。如果发生这种情况，那么规则 *"在任何时候，必须有一个匹配的 C 对象附加到同一个 A 对象上"* 就被违反了。

如果你需要控制关系的删除顺序，那么你必须自行传播删除。

## 解决方案：主动自行执行删除传播

解决上述问题的方法是主动自行执行删除传播。这意味着遍历对象上的所有关系，并使用关系中的 `deleteRule` 信息来决定如何处理另一端的对象。

这比默认的删除传播要慢，但我们是有意复制其行为，以便能够对传播过程中的操作拥有更大的控制权。

对象仍然会使用 `-[NSMangedObjectContext deleteObject:]` 进行删除，但在此之前，它们会被正确地从对象图中断开连接。为了确保不会发生无限循环，受影响的（affected）对象中的所有关系会在传播经过时被设置为 `nil`。

简短提醒：以下方法不处理 "Deny" 删除规则。你需要自行添加对此的支持。

以下是主要的代码块。这是作为 `NSManagedObject` 的一个分类（Category）方法编写的（否则它无法像这样工作）。`priorityDeletionRelationships` 方法应由需要优先删除某些关系的类覆写——返回的数组应是需要优先删除的关系键的有序列表。

```objc
- (NSArray *)priorityDeletionRelationships
{
   return nil;
}

- (void)propagateDelete
{
   NSEntityDescription *entityDescription = [self entity];
  
   // Get the set of relationships
   NSDictionary *relationships = [entityDescription relationshipsByName];
   NSArray *unsortedKeys = [relationships allKeys];
   NSArray *priorityKeys = [self priorityDeletionRelationships];
   NSArray *keys;
   if ([priorityKeys count] > 0)
   {
       keys = [[unsortedKeys mutableCopy] autorelease];
       [(NSMutableArray *)keys
           removeObjectsInArray:priorityKeys];
       [(NSMutableArray *)keys
           replaceObjectsInRange:NSMakeRange(0, 0)
           withObjectsFromArray:priorityKeys];
   }
   else
   {
       keys = unsortedKeys;
   }
  
   // Iterate over the set of relationships
   NSEnumerator *relationshipEnumerator = [keys keyEnumerator];
   NSString *relationshipName;
   while ((relationshipName = [relationshipEnumerator nextObject]) != nil)
   {
       NSRelationshipDescription *relationshipDescription =
           [relationships objectForKey:relationshipName];
      
       // If the relationship is not "cascade", then just nullify it.
       if ([relationshipDescription deleteRule] != NSCascadeDeleteRule)
       {
           if (![relationshipDescription isToMany])
           {
               [self setValue:nil forKey:relationshipName];
           }
           else
           {
               NSMutableSet *relationshipSet =
                   [self mutableSetValueForKey:relationshipName];
               [relationshipSet removeAllObjects];
           }
           continue;
       }
      
       // Propagate the delete to the object at the other end of the
       // relationship
       if (![relationshipDescription isToMany])
       {
           NSManagedObject *destination = [self valueForKey:relationshipName];
           [self setValue:nil forKey:relationshipName];
           [destination propagateDelete];
           continue;
       }
      
       // Propagate the delete to every object in the to-many relationship.
       // We copy the set because we plan to change it during iteration.
       NSMutableSet *mutableRelationship =
           [self mutableSetValueForKey:relationshipName];
       NSSet *iterateSet = [[mutableRelationship copy] autorelease];
       NSEnumerator *enumerator = [iterateSet objectEnumerator];
       NSManagedObject *setObject;
       while ((setObject = [enumerator nextObject]) != nil)
       {
           [mutableRelationship removeObject:setObject];
           [setObject propagateDelete];
       }
   }
  
   // Delete this object
   [[self managedObjectContext] deleteObject:self];

}
```
