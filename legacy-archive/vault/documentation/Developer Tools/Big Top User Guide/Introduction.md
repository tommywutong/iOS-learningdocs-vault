---
title: Big Top User Guide
apple_id: TP40005234
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/BigTopUserGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:24:19.077396Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20BigTop.md)

# Introduction

BigTop is a tool for monitoring the overall resource utilization of Macintosh systems, either locally or remotely over the network. Effectively, BigTop puts a graphical front end onto the traditional UNIX `top` command. It allows you to visualize resource utilization trends with charts and to summarize the state of the various subsystems for each monitored machine. In addition, using the network support, BigTop can also show you a high-level overview of the functionality of large groups of machines.

The performance of complex computer systems can be difficult to comprehend. BigTop lets you easily monitor the health of your systems to look for problems and give you a starting point for in-depth analysis.

BigTop records the activity on a system by periodically collecting performance statistics from the underlying operating system. This statistics collection typically requires less than 5% of the CPU time, so its performance impact, while not zero, is fairly small. Metrics such as CPU utilization, amount of disk I/O, etc., provide a wealth of information about the current state of each subsystem. While each of these pieces of data are useful on their own, BigTop consolidates them together so that you can easily see which parts of a system are limiting performance.

[Next](Using%20BigTop.md)

