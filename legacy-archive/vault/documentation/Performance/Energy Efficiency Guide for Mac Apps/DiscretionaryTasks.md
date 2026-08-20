---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/DiscretionaryTasks.html
archived_at: '2026-07-18T01:49:43.780740Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Manage Tasks with CTS and GCD

The main thread of your app is where your app should handle user input, rather than long-running, processor-intensive, and discretionary operations. Always move those tasks onto background threads. Moving tasks into the background leaves your main thread free to continue processing user input. This is especially important when your app is starting up or quitting, because it is expected to respond to events in a timely manner. Centralized Task Scheduling (CTS) and Grand Central Dispatch (GCD) APIs help you schedule and manage background activity.

### Centralized Task Scheduling (CTS)

Centralized Task Scheduling APIs allow you to designate criteria for when a task should be performed, such as when a user plugs the computer into power or when the system is not performing higher-priority tasks. The system can intelligently decide when to perform the task based on the specified criteria.

The following sections discuss how to defer execution of discretionary tasks by using CTS:

- [Schedule Background Activity](SchedulingBackgroundActivity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmzsfvjvomi)
- [Schedule Background Networking](SchedulingNetworkActivity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmztfvjvomi)
- [Defer Tasks with XPC Activity](CentralizedTaskScheduling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmznknltc)

> [!IMPORTANT]
> 

### Grand Central Dispatch (GCD)

Grand Central Dispatch is a low-level framework in OS X that manages concurrent and asynchronous execution of tasks across the operating system. Essentially, tasks are queued and scheduled for execution as processor cores become available. By allowing the system to control the allocation of threads to tasks, GCD uses resources more effectively, which help the system and apps run faster, efficiently, and responsively.

GCD supports the implementation of dispatch queues, which execute arbitrary blocks of code asynchronously or synchronously. Use dispatch queues to perform nearly all of the tasks that could be performed on separate threads. Dispatch queues are easier and more efficient to use than the corresponding threaded code. Serial dispatch queues are a good alternative to using timers for synchronization.

For detailed information about implementing GCD features in your app, refer to _[Concurrency Programming Guide](../../General/Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_ and _Grand Central Dispatch (GCD) Reference_.

> [!IMPORTANT]
> 

[Prioritize Work at the Task Level](PrioritizeWorkAtTheTaskLevel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmzvfvjvomi)

[Schedule Background Activity](SchedulingBackgroundActivity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmzsfvjvomi)
