---
title: PreLoginAgents
apple_id: DTS10004414
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: null
published: '2014-04-07'
source_url: https://developer.apple.com/library/archive/samplecode/PreLoginAgents/Introduction/Intro.html
archived_at: '2026-07-18T03:19:30.607091Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](PreLoginAgentCarbon%20%28legacy%29-main.c.md)

# PreLoginAgents

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2014-04-07 Updated to use the latest coding tools and techniques. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydinbrgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 5.1 |
| __Runtime Requirements:__ | OS X 10.9 |

Pre-login launchd agents are the best solution to a small but important class of problems. For example, if you're developing assistive technology for OS X and you want to provide assistance at login time, you will probably need a pre-login launchd agent.

To a large extent a pre-login launchd agent can operate like a normal Cocoa application. However, the pre-login environment results in some unique challenges; this sample shows how to meet those challenges.

[Next](PreLoginAgentCarbon%20%28legacy%29-main.c.md)

