---
title: TemperatureConverter
apple_id: DTS40008839
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: Foundation
published: '2012-06-05'
source_url: https://developer.apple.com/library/archive/samplecode/TemperatureConverter/Introduction/Intro.html
archived_at: '2026-07-18T03:26:23.423089Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# TemperatureConverter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-06-05 Updated for Mac OS X 10.7 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobthewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.7 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

A simple example using NSValueTransformer to automatically convert data between different representations. The purpose of this example is to show how to create and use custom NSValueTransformer subclasses. Otherwise it is possible to create a temperature converter using "regular glue code" with less lines of code.

Temperature Converter presents a simple user interface through which the user can enter temperature values in any of four different units and the application will automatically convert and display the temperature in the other three units. The four units are Kelvin, Centigrade, Fahrenheit, and-- the infrequently used-- Rankine temperature scale.

Internally, the application stores temperature values in Kelvin and uses value transformers to transform the entered temperature value to Kelvin and then from Kelvin to the other scales needed.

[Next](main.m.md)

