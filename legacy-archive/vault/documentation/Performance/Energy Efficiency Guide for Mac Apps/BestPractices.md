---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/BestPractices.html
archived_at: '2026-07-18T01:49:42.777517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Best Practices

As you develop your app, try to recognize potential energy problem areas and address them early.

- Ensure your app is absolutely idle when not in use—even at the microsecond scale, such as between keystrokes. Stay idle as long as possible. Exit idle only when there is work to do, primarily in response to user input. After your app completes the user’s request, make sure it races back to a zero-power idle state.
- Think about the dynamic and fixed costs your app produces, and implement coding and design techniques to reduce them whenever possible. Use CPU cores efficiently. When the user requests action, your app should employ efficient, multithreaded algorithms. Concurrency generally helps conserve power—two cores running for half the time consume less energy because the system is kept awake for half the time.
- Eliminate unnecessary, non-user-driven work and wait for user input. Don’t poll for state changes, don’t update content on the screen when the user can’t see your app, and don’t perform power-intensive, discretionary operations when the system is running on battery power.
- Limit the type of work being done on the main thread. This is where your app should handle user input, not processor-intensive, long-running, or potentially unbounded operations, such as tasks that access the network.
- Minimize timer usage. If you must use timers, allow flexibility in their timing so they can execute when the system is already awake.
- Prioritize work and batch tasks together whenever possible.
- Schedule tasks for energy efficient times. This applies to all components on all platforms, particularly the CPU on Macs and the radio on iOS devices.
- Allow the system to make smart decisions about when to run discretionary tasks.

[Test Performance](TestPerformance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrzfvjvomi)

[Related Documents](RelatedDocuments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrqfvjvomi)
