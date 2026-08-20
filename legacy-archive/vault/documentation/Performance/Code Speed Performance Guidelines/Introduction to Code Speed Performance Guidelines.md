---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/CodeSpeed.html
archived_at: '2026-07-18T01:47:09.267710Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Diagnosing%20Slow%20Operations.md)

# Introduction to Code Speed Performance Guidelines

For most users, performance means speed. If an application performs its tasks quickly, the user is happy. If an application performs tasks slowly or is unresponsive to commands, the user is likely going to get frustrated and may possibly not want to use that application.

The focus of this programming topic is improving the speed of your code, both in the real and perceived sense. In the real sense, you should measure the time it takes to complete operations and modify your algorithms and loop code to be as efficient as possible. In the perceived sense, you should make your application appear fast to the user, even if an operation actually takes a long time to complete.

This programming topic contains the following articles:

- [Diagnosing Slow Operations](Diagnosing%20Slow%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dslkdjjbeursjirca) describes techniques for finding which parts of your code are slow.
- [Check Your Algorithms](Check%20Your%20Algorithms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dmlkdjjbegskgivba) provides some guidelines on how to approach speed improvements in your code.
- [Impedance Mismatches](Impedance%20Mismatches.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dolkcijbusq2kivaq) describes the performance impacts of translating between different data formats and tips on how to avoid such translations.
- [Perceived Responsiveness](Perceived%20Responsiveness.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dqlkcijbusq2djjdq) describes ways to make your application feel faster than it may actually be.
- [Detecting Polling Behavior](Detecting%20Polling%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3talkdjjbeursjirca) describes a simple way to tell if your application is polling the system for information.
- [Accelerating Critical Code](Accelerating%20Critical%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3tclkcineusqsjijfa) provides some practical tips on how to improve the performance of iterative code.
- [Tuning for Specific Hardware](Tuning%20for%20Specific%20Hardware.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinrxfvbegskjijeuesq) provides tips on how to tune your software for maximum performance on the G5 processor.

[Next](Diagnosing%20Slow%20Operations.md)

