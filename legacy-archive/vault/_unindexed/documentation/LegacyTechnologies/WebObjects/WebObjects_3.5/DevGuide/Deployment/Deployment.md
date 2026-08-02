---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Deployment/Deployment.html
archived_at: '2026-07-15T07:51:22.330147Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../DevGuideTOC.md)

# Deployment and Performance Issues

---

After you've written your application, tested it, and verified that it works properly, it's ready to be deployed for use by your customers. Before you deploy, you'll want to perform some finishing touches. For example, if you included any __logWithFormat:__ (or __logString__) statements in your code for debugging purposes, you'll probably want to remove them before you deploy.
This chapter describes finishing touches that you might want to add after you're through debugging the bulk of your application's code. It covers such topics as how to record application usage statistics, how to shut down an application gracefully, how to substitute your own code when an error occurs, and how to improve the application's performance.
You'll also want to read the online document [_Serving WebObjects_](../../ServingWebObjects/ServingWebObjectsTOC.md). This document is intended for the person who sets up the website and maintains the application after it is deployed. It covers such topics as how to perform load balancing, how to maintain a log file, and how to test and improve performance of the applications running on a site.

[****
: __Recording Application Statistics__](Stats.md#apple-gq2tami)

[****
: Maintaining a Log File](Stats.md#apple-gu4tooa)[****
: Accessing Statistics](Stats.md#apple-gu4tqoa)[****
: Recording Extra Information](Stats.md#apple-guydcmy)

[****
: __Error Handling__](ErrorHandling.md#apple-gq4tqmi)

[****
: __Automatically Terminating an Application__](TerminateApp.md#apple-gq3temy)

[****
: __Performance Tips__](Performance.md#apple-gq2taoi)

[****
: Cache Component Definitions](Performance.md#apple-gq4dgma)[****
: Compile the Application](Performance.md#apple-gq3tgny)[****
: Control Memory Leaks](Performance.md#apple-gyzteoa)[****
: Limit State Storage](Performance.md#apple-gyztini)[****
: Limit Database Fetches](Performance.md#apple-gy4tena)[****
: Limit Page Sizes](Performance.md#apple-gq3tgoa)

[****
: __Installing Applications__](Install.md#apple-gy3tgni)

[!First Section](Stats.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
