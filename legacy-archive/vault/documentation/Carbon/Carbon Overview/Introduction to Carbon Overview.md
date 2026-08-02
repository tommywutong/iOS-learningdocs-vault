---
title: Carbon Overview
apple_id: TP30000990
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/newtocarbon/Introduction.html
archived_at: '2026-07-15T05:25:14.862704Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Carbon%20Basics.md)

# Introduction to Carbon Overview

Originally designed to provide a gentle migration path for developers transitioning from Mac OS 9, Carbon is a collection of C programming interfaces that let you implement basic application functionality such as the user interface, event handling, file management, and so on.

This document describes Carbon's place in Mac OS X and gives overviews of the Carbon interfaces. It also describes a wide variety of other programming interfaces that Carbon applications can use, supporting everything from video playback to alternate text input.

As Carbon is a C interface, you can also use all the standard C library APis; however, Mac OS X often has superior replacements (for example, Unicode string manipulation APIs versus the ASCII-related APIs, such as `strcmp` in the standard C library).

You should read this document if you are new to Mac OS X and would like to write Mac OS X applications using procedural C or C++.

This document contains two chapters:

- [Carbon Basics](Carbon%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnjtfvjvomi) briefly describes how Carbon fits into Mac OS X and the tools available to build Carbon applications.
- [The Carbon Factory Tour](The%20Carbon%20Factory%20Tour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnjufvjvomi) gives an overview of Carbon managers and services, including nonCarbon specialty services.
- [Legacy Interfaces](Legacy%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnjwfvjvomi) describes managers and services that have been superseded by newer technologies. If you are a new developer, this chapter is of historical interest only.

When you are ready to explore Carbon programming, see _[Getting Started with Carbon](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Carbon/_index.html#//apple_ref/doc/uid/TP30001086)_ to determine which documents to start reading.

[Next](Carbon%20Basics.md)

