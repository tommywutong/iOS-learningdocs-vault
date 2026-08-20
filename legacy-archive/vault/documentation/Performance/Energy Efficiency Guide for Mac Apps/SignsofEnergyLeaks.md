---
title: Energy Efficiency Guide for Mac Apps
apple_id: TP40013929
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/SignsofEnergyLeaks.html
archived_at: '2026-07-18T01:50:25.740693Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for Mac Apps](index.md)



## Observe Signs of Energy Leaks

When testing and debugging your app, watch for these signs of excessive energy use:

- Battery drain
- Activity when you expect your app to be idle
- An unresponsive or slow user interface
- Large amounts of work on the main thread
- High use of animations
- High use of view opacity
- Swapping
- Memory stalls and cache misses
- Memory warnings
- Lock contention
- Excessive context switches
- Excessive use of timers
- Excessive drawing to screen
- Excessive or repeated small disk I/O
- High-overhead communication, such as network activity with small packets and buffers
- Preventing device sleep

[Defer Tasks with XPC Activity](CentralizedTaskScheduling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmznknltc)

[Monitor Usage Regularly](MonitoringEnergyUsage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmrzfvbuqmrufvjvomi)
