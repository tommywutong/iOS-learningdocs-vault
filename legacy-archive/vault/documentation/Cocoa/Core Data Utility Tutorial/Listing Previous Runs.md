---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/07_fetch.html
archived_at: '2026-07-15T07:14:28.966254Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 实用工具教程](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)


[下一页](Complete%20Source%20Listings.md)[上一页](The%20Custom%20Managed%20Object%20Class.md)

# 列出历次运行记录

本节将向你展示如何从持久化存储中获取全部 Run 实例。

第一步是创建获取请求。你想获取 Run 实体的实例，并按最近程度对结果排序。你需要把获取请求的实体设为 Run 实体，并创建、设置一个合适的排序数组。最后，通过向托管对象上下文发送 `executeFetchRequest:request error:` 消息来执行获取。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)创建并执行一个获取请求

1. 在 `main` 函数中，紧接在上一章添加的代码之后，为名为"Run"的实体创建一个新的获取请求。

```objc
NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Run"];
```
2. 创建一个新的排序描述符，按最近程度排列获取结果。

   设置该获取请求的排序描述符——注意你必须提供一个排序描述符数组。

```objc
NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc]
        initWithKey:@"date" ascending:YES];
[request setSortDescriptors:@[sortDescriptor]];
```
3. 将获取请求发送给托管对象上下文来执行它。

   回忆一下，你在上一章中已经声明了一个 error 变量。如果出现错误（即 `executeFetchRequest:error:` 返回的值为 `nil`），报告该错误并退出。

```objc
error = nil;
NSArray *fetchedArray = [moc executeFetchRequest:request error:&error];
if (fetchedArray == nil)
{
    NSLog(@"Error while fetching\n%@",
            ([error localizedDescription] != nil) ? [error localizedDescription] : @"Unknown Error");
    exit(1);
}
```


要显示获取请求的结果，只需遍历获取到的 run 对象数组，并记录 run 的信息。使用日期格式化器对日期进行适当的格式化。

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)显示获取结果

1. 创建一个日期格式化器对象，用于显示时间信息。

```objc
NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
[formatter setDateStyle:NSDateFormatterMediumStyle];
[formatter setTimeStyle:NSDateFormatterMediumStyle];
```
2. 打印出该进程的运行历史。

```objc
NSLog(@"%@ run history:", [processInfo processName]);

for (Run *aRun in fetchedArray)
{
    NSLog(@"On %@ as process ID %ld",
            [formatter stringForObjectValue:aRun.date],
            aRun.processID);
}
```


构建并运行该工具。它应该能够无警告地编译通过。运行该工具时，不应记录任何错误，并应正确显示运行历史。

[下一页](Complete%20Source%20Listings.md)[上一页](The%20Custom%20Managed%20Object%20Class.md)
