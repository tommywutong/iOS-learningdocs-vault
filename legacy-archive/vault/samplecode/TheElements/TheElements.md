---
title: TheElements
apple_id: DTS40007419
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2015-08-25'
source_url: https://developer.apple.com/library/archive/samplecode/TheElements/Introduction/Intro.html
archived_at: '2026-07-18T03:26:45.148798Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# TheElements

|  |  |
| --- | --- |
| __Last Revision:__ | Version 6.0, 2015-08-25 Updated to Modern Objective-C syntax, fixed deprecations, using Objective-C modules, all images now in image assets. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonbrhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS 8.0 SDK or later |
| __Runtime Requirements:__ | iOS 8.0 or later |

TheElements is a sample application that provides access to the data contained in the Periodic Table of the Elements. The Periodic Table of the Elements catalogs all the known atomic elements in the universe.

TheElements provides this data in multiple formats, allowing you to sort the data by name, atomic number, symbol name, and an element's physical state at room temperature.

TheElements is structured as a Model-View-Controller application. There is distinct separation of the model data, the views used to present that data, and the controllers which act as a liaison between the model and controller.

The application illustrates the following techniques: configuring and responding to selections in a tab bar, displaying information in a tableview using both plain and grouped style table views, using navigation controllers to navigate deeper into a data structure, subclassing UIView, providing a custom UITableViewCell consisting of multiple subviews, implementing the UITableViewDelegate protocol, implementing the UITableViewDataSource protocol, reacting to taps in views, open a URL to an external web site using Safari, flipping view content from front to back, and creating a reflection of a view in the interface.

[Next](main.m.md)

