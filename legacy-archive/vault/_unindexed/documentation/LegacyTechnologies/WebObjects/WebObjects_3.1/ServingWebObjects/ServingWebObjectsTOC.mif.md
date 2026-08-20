---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/ServingWebObjectsTOC.mif.html
archived_at: '2026-07-15T07:50:01.232146Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[! WebObjects Library](../WebObjectsTOC.md)

# Serving WebObjects

_WebObjects System Administration_

To a large extent, WebObjects needs little attention once it is installed. For its essential purpose---the handling of HTTP requests---WebObjects should "just work." However, there are a few things a system administrator might have to do, especially when it comes to deploying WebObjects applications or porting deployment functionality to new platforms. This document describes the procedures for accomplishing these and related tasks. It also offers some background information on HTTP adaptors that system administrators might find useful.

## Table of Contents

__[HTTP Adaptors](HTTPAdaptors.md#apple-kjcummjtgyytm)__- [Introduction](HTTPAdaptors.md#apple-kjcummjtgyytm)
- [Configuration Files](ConfigFiles.md#apple-kjcummrwgq4dc)
- [Adaptor Modes](AdaptorModes.md#apple-kjcumnrxhe2ta)
- [Installed HTTP Adaptors](InstalledAdaptors.md#apple-kjcumnrsgy4da)

  __[Administrative Tasks](AdminTasks.md#apple-kjcumobrheztm)__- [Manually Starting WebObjects Applications](ManualStarting.md#apple-kjcummjygi3ts)
  - [Managing Application Processes](ManagingProcesses.md#apple-kjcummztg43ds)
  - [Logging and Analyzing Adaptor Activity](Logging.md#apple-kjcumnrxgi4dc)
  - [Load Balancing](LoadBalancing.md#apple-kjcumnjygyzda)
  - [Installing and Configuring NSAPI Adaptors](NSAPIConfig.md#apple-kjcumobvgi3tm)
  - [Installing and Configuring the ISAPI Adaptor](ISAPIConfig.md#apple-kjcummzxgi4da)
  - [Autostarting Applications](Autostarting.md#apple-kjcumojugu3dq)
  - [Securing Application Source Code](SecuringSource.md#apple-kjcumnjygazta)

    ## Related Topics

    Other WebObjects documents might be of interest to system administrators:

    - _Installation Guide_: Includes system requirements, compatibility information, and location of the WebObjects Home Page. You can download the installation guide, which is printed only, from [NeXTanswers](http://enterprise.apple.com/NeXTanswers/HTMLFiles/2455.htmld/2455.html).
      You can also view [post-installation instructions](../PostInstall.md) on-line.
    - _[WebObjects Developer's Guide](../DevGuide/DevGuide.md)_:

      - "[Introduction](../DevGuide/Intro/Start.book.md)": Among other things, describes application executables, how to connect to a WebObjects application, WebObjects adaptors, the files that comprise WebObjects, and the directories where these files reside.
      - "[How WebObjects Works](../DevGuide/HowWOWorks/HowWOWorks.mif.book.md)": Among other things, describes in some detail the relationship between WebObjects adaptors and applications and what happens when an application starts up.[!First Section](HTTPAdaptors.md#apple-kjcummjtgyytm)
