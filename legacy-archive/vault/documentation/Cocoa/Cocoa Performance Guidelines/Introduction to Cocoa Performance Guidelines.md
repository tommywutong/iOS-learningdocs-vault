---
title: Cocoa Performance Guidelines
apple_id: TP40001448
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2009-08-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaPerformance/CocoaPerformance.html
archived_at: '2026-07-15T07:13:19.706001Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](General%20Recommendations.md)

# Introduction to Cocoa Performance Guidelines

This document provides practical advice and tips on how to improve the performance of your Cocoa applications. If you create any type of Cocoa program, including command-line tools, you will find information to help you improve its performance.

This document contains the following articles:

- [General Recommendations](General%20Recommendations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbrfvbuuqsiivdecri) provides some general tips for achieving good performance with Cocoa.
- [Unblocking Your User Interface](Unblocking%20Your%20User%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbsfvbegskhjjcuosi) explains ways to perform lengthy tasks in a way that keeps your user interface responsive to user commands.
- [Using Views Effectively](Using%20Views%20Effectively.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbtfvbuuqskjfdeoqy) explains how to get the best performance out of your custom NSView subclasses.
- [Cocoa Live Window Resizing](Cocoa%20Live%20Window%20Resizing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbufvbecsshireueri) provides tips for speeding up your drawing code during a live window resize.
- [Cocoa Bindings Tips](Cocoa%20Bindings%20Tips.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmrwfvbegskeivdessi) provides basic tips for improving performance when using Cocoa bindings.
- [Improving NSBezierPath Rendering Times](Improving%20NSBezierPath%20Rendering%20Times.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3tolkdjjbeursjirca) describes ways to speed up drawing operations involving the NSBezierPath object.
- [String Management](String%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbvfvbegskdi5eeeqy) provides tips for using strings effectively in your application.
- [Notifications](Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbwfvbegskeivdessi) provides tips for using notifications efficiently and offers alternatives for communicating among the objects in your application.

[Next](General%20Recommendations.md)

