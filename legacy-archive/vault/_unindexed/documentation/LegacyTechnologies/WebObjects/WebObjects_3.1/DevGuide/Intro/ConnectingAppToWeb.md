---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/ConnectingAppToWeb.html
archived_at: '2026-07-15T07:47:09.440572Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](AppExecutables.md)

# Connecting to a WebObjects Application

To connect to a WebObjects application from a web browser, you open a URL with the following form:!Figure 2. URL to Start a WebObjects Application
Communicating with a WebObjects application involves the following processes:

- _An HTTP server._ Any HTTP server that uses the Common Gateway Interface (CGI), the Netscape Server API (NSAPI), or the Internet Server API (ISAPI).
- _[A WebObjects adaptor](Adaptors.md)_
. Acts as an intermediary between WebObjects applications and HTTP servers. Adaptors insulate applications from server interfaces by handling all server communication. Simply by switching adaptors, you use a different HTTP server and a different server interface without modifying application code.
- _A WebObjects application executable._ The application executable receives incoming requests and responds to them, usually by returning a dynamically generated HTML page.
!Figure 3. Chain of Communication between Browser and WebObjects

[!Table of Contents](Start.book.md) [!Next Section](Adaptors.md)
