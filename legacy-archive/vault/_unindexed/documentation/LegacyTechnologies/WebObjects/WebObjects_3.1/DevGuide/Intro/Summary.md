---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/Intro/Summary.html
archived_at: '2026-07-15T07:47:12.403263Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Start.book.md) [!Previous Section](WhereThingsGo.md)

# Summary

## What's in a WebObjects Application?

A typical WebObjects application contains the following ingredients:

- Components that specify the content, presentation, and behavior of the application's pages
- An optional application script that creates and manages application-wide resources
- An optional session script that creates and manages session-wide resources
- Optional compiled code that implements custom data and logic
- WebObjects classes that provide an infrastructure for the web application

## What Parts Do I Write?

You write the following parts of a WebObjects application:

- Components consisting of HTML templates, script files, and declarations files
- An optional application script
- An optional session script
- Optional compiled code

## How Do I Run a WebObjects Application?

To run a WebObjects application, you open an URL with the following form:!Figure 9. URL to Start a WebObjects Application

## How Do I Connect a WebObjects Application to the Web?

To connect a WebObjects application to the Web, you need the following:

- _An HTTP server._ You can use any HTTP server that uses the Common Gateway Interface (CGI), the Netscape Server API (NSAPI), or the Internet Server API (ISAPI).
- _A WebObjects adaptor_. A WebObjects adaptor connects WebObjects applications to the Web by acting as an intermediary between web applications and HTTP servers.
- _A WebObjects application executable._ An application executable receives incoming requests and responds to them, usually by returning a dynamically generated HTML page.

## What Happens Behind the Scenes?

Behind the scenes of a running WebObjects application, the application enters a request-response loop each time it receives a request. In the request-response loop, a WebObjects application uses the page-to-script file mappings defined in declarations files to:

- Take values from the request.
- Invoke an action.
- Generate a response page.
