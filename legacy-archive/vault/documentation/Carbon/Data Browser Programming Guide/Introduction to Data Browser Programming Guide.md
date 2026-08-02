---
title: Data Browser Programming Guide
apple_id: TP30000968
resource_type: Guide
platform: macOS
topic: User Experience
technology: Carbon
published: '2007-08-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/display_databrowser/databrowser_intro/databrowser_intro.html
archived_at: '2026-07-15T05:25:07.461634Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Data%20Browser%20Concepts.md)

# Introduction to Data Browser Programming Guide

A data browser provides a user interface for displaying and selecting items from a list of data or from hierarchically organized lists of data such as directory paths. The list and column views in the Finder are representative of the kind of behavior your application can provide using the data browser API.

The data browser API supports the following:

- The ability to display an unlimited number of cells
- Built-in drag-and-drop handling
- Display of a variety of data—text, icons, checkboxes, pop-up menus, progress bars, relevance indicators, and sliders
- Contextual menus and help tags
- Built-in support for editing text displayed in the data browser
- Display of hierarchically organized data in a list
- Keyboard navigation and accessibility

This document is targeted at Mac OS X Carbon developers who want to display data that can be browsed in a way similar to data browsing in the Mac OS X Finder. The document assumes you are familiar with Mac OS X programming and with Carbon in particular.

Some of the features available in a data browser assume you are familiar with the technologies underlying the features. For example, if you want to provide help tags for data browser items, knowledge of the Carbon Help Manager is useful. Cross-references are provided for situations in which information from another technology is helpful.

This document contains the following chapters:

[Data Browser Concepts](Data%20Browser%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkrbeilkukbmferkggeydc) shows typical data browser user interfaces, introduces data browser terminology, describes how the data browser works, provides in-depth information on what can be displayed, and defines the terms needed to refer to the displayed data.

[Data Browser Tasks](Data%20Browser%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnryfvbuqmrqgywviucykjcummjqge) describes how to use the data browser API to display data in list view and column view, to switch between views, to support text editing in a cell. It also provides information on the callbacks you need to supply to support drag and drop, provide help tags and contextual menus, and to customize drawing, tracking, and dragging behavior.

_Data Browser Reference_. This document is a complete reference for the functions, callbacks, data types, and constants provided by the data browser API.

[Next](Data%20Browser%20Concepts.md)

