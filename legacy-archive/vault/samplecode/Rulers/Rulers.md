---
title: Rulers
apple_id: DTS40008871
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-06-07'
source_url: https://developer.apple.com/library/archive/samplecode/Rulers/Introduction/Intro.html
archived_at: '2026-07-18T03:22:24.664836Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ColorRect.h.md)

# Rulers

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2012-06-07 Updated for Mac OS X 10.7 [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobxgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4.0 or later, Mac OS X v10.7 or later |
| __Runtime Requirements:__ | Mac OS X v10.7 or later |

This project demonstrates many of the interactions between an NSRulerView and its client view. It should give you an idea how to go about this when creating a view subclass that really does something.

The principal class, RectsView, displays colored rectangles that the user can select and drag around. The RectsView puts markers in the horizontal and vertical rulers showing the placement of the rectangle; manipulating these markers changes the size of the selected rectangle. Removing a marker deletes the selected rectangle, and clicking in the ruler area creates a new rectangle. The user can also lock a rectangle down, so that the markers can't be moved.

[Next](ColorRect.h.md)

