---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/GuestBook/GuestBook2.html
archived_at: '2026-07-15T07:53:21.876587Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](GuestBookTOC.md) [!Previous Section](GuestBook1.md)

# Choosing the Programming Language

WebObjects supports three languages:

- Java
- Objective-C
- WebScript

Java and Objective-C are _compiled_ languages. They require you to build your application before running it. WebScript, which is based on Objective-C, is a _scripted_ language. It allows you to make changes to your application while it is running.
When you create a new project, Project Builder provides you with a _component_ called Main. In WebObjects terminology, a component represents a page in your application (or possibly part of a page).
In the Wizard, you specify the language you'll use to program your Main component, as well as the _application_ and _session_ code files (which will be described later).

- For the primary language, select Java.

Later, you'll create an additional component for your application and write its code in WebScript.

- Click Finish.

Project Builder creates a new application directory called __GuestBook__. This directory contains the files you work with in both Project Builder and WebObjects Builder.

[!Table of Contents](GuestBookTOC.md) [!Next Section](GuestBook3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
