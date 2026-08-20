---
title: Crossing To-Many Relationships with Cocoa Bindings
apple_id: DTS10004234
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-04'
source_url: https://developer.apple.com/library/archive/samplecode/TwoManyControllers/Introduction/Intro.html
archived_at: '2026-07-18T03:27:24.441583Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Crossing To-Many Relationships with Cocoa Bindings

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2013-04-04 Updated project format. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrtgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.6 or later, OS X 10.7 or later. |
| __Runtime Requirements:__ | OS X 10.7 or later. |

This sample shows how you can use array controllers (instances of NSArrayController) to create a user interface that traverses multiple (in this case two) to-many relationships. In particular, it illustrates the use of the @distinctUnionOfSets collection operator to display the aggregation of the objects in a to-many relationship derived from another to-many relationship; that is, given A ->> B ->> C, it shows all the Cs associated with a given A. The sample also demonstrates use of conditional bindings, and integration with Core Data. No custom code is required to support the application user interface.

[Next](ReadMe.txt.md)

