---
title: Fiendishthngs
apple_id: DTS10003446
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2007-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/Fiendishthngs/Introduction/Intro.html
archived_at: '2026-07-18T03:08:27.665454Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# Fiendishthngs

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.02, 2007-09-13 Now displays 'cpix' resources for codec components. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbugywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.4.1 |
| __Runtime Requirements:__ | MacOS 10.4+, QuickTime 6.5.2+ |

Many services on Mac OS X, such as image compression/decompression, audio format conversion, file import/export and so on are provided by components. Components are a type of shared library that you can manipulate using the Component Manager. The Component Manager registers these shared libraries by looking for a component resource (a resource of type 'thng') in a specific component file.

Given a particular component type, the Component Manager can locate and query all components of that type. You can find out how many components of a specific type are available and you can get further details about a component's capabilities.

Fiendishthngs lists all the Components it finds on the system and lets you query them for information.

It will also list more detailed information for the following QuickTime Component Types:

Movie Importers 'eat '

Movie Exporters 'spit'

Graphics Importers 'grip'

Graphics Exporters 'grex'

Image Codecs 'imco' / 'imdc'

QuickTime Effects 'imdc'

Data Handlers 'dhlr'

Video Digitizers 'vdig'

Clock Components 'clok'

Video Output Components 'vout'

[Next](main.m.md)

