---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects4.html
archived_at: '2026-07-15T08:06:54.147031Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](How%20WebObjects%20Applications%20Work.md)

## Java Client-Based WebObjects Applications

[Figure 5](#apple-geytkojw) shows a client browser communicating with a WebObjects server while running a Java Client application. The portion of your application that runs in the browser is linked to an EOJavaClient object. The portion that runs on the server is similarly linked to an EODistribution object. These two objects handle communications between the client and the server, allowing both portions of your application to focus on implementing your application's business logic.

!

Figure 5. Chain of Communication Between the Browser and a Java Client-based WebObjects Application

__Note:__  The techniques used in creating the Java Client portions of your WebObjects applications are documented in greater detail in the _Enterprise Objects Framework Developer's Guide_. The remainder of this book deals with those aspects of WebObjects that are common to all WebObjects applications.

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](WhatIsWebObjects5.md)
