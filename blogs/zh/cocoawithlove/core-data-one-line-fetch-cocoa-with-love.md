---
title: 'Core Data：一行代码获取数据 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/core-data-one-line-fetch.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:5b07a4e05f0f0348'
translated: true
---

> 原文：[Core Data: one line fetch | Cocoa with Love](https://www.cocoawithlove.com/2008/03/core-data-one-line-fetch.html)　·　Cocoa with Love (Matt Gallagher)

从 Core Data 中获取数据其实比文档告诉你的要简单得多。这个简单的单行代码获取，在大多数情况下和 Apple 建议的十行方法一样好用。

## Core Data 做了什么？

Core Data 文档没有简单说明它的功能。我来帮它们一把。

> Core Data 替你保管数据。

假设它保管数据保管得很好。合理的假设，它是一个很不错的 API。搞定之后，一个典型的程序员接下来想做什么？我认为以下想法很合理：

> 一个典型的程序员想把数据拿回来。

哇，多么了不起的启示！我觉得这能流行起来。程序员甚至可能 **一直**都想这么做。

## 按照 Core Data 的方式获取数据

这是一个非常常见的任务。好的 API 应该为此提供简洁的选项。让我们看看 Core Data 的建议。根据 [Core Data 编程指南](http://developer.apple.com/documentation/Cocoa/Conceptual/CoreData/Articles/cdFetching.html)：

```objc
NSManagedObjectContext *moc = [self managedObjectContext];
NSEntityDescription *entityDescription = [NSEntityDescription entityForName:@"Employee" inManagedObjectContext:moc];
NSFetchRequest *request = [[[NSFetchRequest alloc] init] autorelease];
[request setEntity:entityDescription];
 
// Set example predicate and sort orderings...
NSNumber *minimumSalary = ...;
NSPredicate *predicate = [NSPredicate predicateWithFormat:
    @"(lastName LIKE[c] 'Worsley') AND (salary > %@)", minimumSalary];
[request setPredicate:predicate];
 
NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc]
    initWithKey:@"firstName" ascending:YES];
[request setSortDescriptors:[NSArray arrayWithObject:sortDescriptor]];
[sortDescriptor release];
 
NSError *error = nil;
NSArray *array = [moc executeFetchRequest:request error:&error];
if (array == nil)
{
    // Deal with error...
}
```

真的吗，Core Data 的设计者们？真的吗？这是一个常见的任务，程序员需要一直做，是使用 Core Data 的基础——**却要用 13 行代码来完成这个最常见的单一任务？**

## 一行，多谢

我认为他们搞错了。上面所有的代码都应该简化为：

```objc
[[self managedObjectContext] fetchObjectsForEntityName:@"Employee" withPredicate:
    @"(lastName LIKE[c] 'Worsley') AND (salary > %@)", minimumSalary];
```

这一行就能完成之前那堆代码的所有工作，只是排序仍需单独步骤（如果需要的话）。从 10 行减少到 1 行，因为针对常见情况提供了更好的方法。

显然，每次都查找实体并构建 NSPredicate 并非最优的快速路径，其他的特殊 NSFetchRequest 选项也无法访问，但对于大多数其他情况，短 10 倍就等于好 10 倍。

你也会注意到，由于我们去掉了排序，返回的所有对象都是唯一的，且没有特定顺序。这是一个 NSSet，而不是 NSArray，返回类型也相应修改了。创建 NSSet 的开销比创建 NSArray 稍高一些，但再次说明，我们考虑的是快速简单的获取，而且这种方式可以轻松测试结果集中的成员关系（一个非常有用的逻辑情况）。

## 实现它

Objective-C 的一个好处是，默认 API 中的局限性不会成为真正的障碍。将以下代码放入 NSManagedObjectContext 的分类（category）中，所有这些神奇功能就都是你的了。

```objc
// Convenience method to fetch the array of objects for a given Entity
// name in the context, optionally limiting by a predicate or by a predicate
// made from a format NSString and variable arguments.
//
- (NSSet *)fetchObjectsForEntityName:(NSString *)newEntityName
    withPredicate:(id)stringOrPredicate, ...
{
    NSEntityDescription *entity = [NSEntityDescription
        entityForName:newEntityName inManagedObjectContext:self];

    NSFetchRequest *request = [[[NSFetchRequest alloc] init] autorelease];
    [request setEntity:entity];
    
    if (stringOrPredicate)
    {
        NSPredicate *predicate;
        if ([stringOrPredicate isKindOfClass:[NSString class]])
        {
            va_list variadicArguments;
            va_start(variadicArguments, stringOrPredicate);
            predicate = [NSPredicate predicateWithFormat:stringOrPredicate
                arguments:variadicArguments];
            va_end(variadicArguments);
        }
        else
        {
            NSAssert2([stringOrPredicate isKindOfClass:[NSPredicate class]],
                @"Second parameter passed to %s is of unexpected class %@",
                sel_getName(_cmd), [stringOrPredicate className]);
            predicate = (NSPredicate *)stringOrPredicate;
        }
        [request setPredicate:predicate];
    }
     
    NSError *error = nil;
    NSArray *results = [self executeFetchRequest:request error:&error];
    if (error != nil)
    {
        [NSException raise:NSGenericException format:[error description]];
    }
    
    return [NSSet setWithArray:results];
}
```

敏锐的编码者会注意到，第二个参数可以是 NSPredicate 或 NSString，如果需要，允许一点额外的偷懒自由度。这是一时冲动选择的便利方法，稍后我会再决定它是否构成糟糕的设计。
