---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb28.html
archived_at: '2026-07-18T01:24:57.562459Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb27.md)

# Deploying a Direct To Web Application

To deploy a Direct to Web application, you need to take a couple of steps in addition to the standard derployment procedure (as described in _Serving WebObjects_).

- Make sure that the D2WLiveAssistantEnabled command-line option is set to NO. The WebAssistant should not be accesible in deployment mode; it is strictly a development tool for configuring your application.
- Because the Direct to Web pages are built dynamically, they take more time to render than regular WebObjects pages. To improve performance, you should consider "freezing" some of the more sophisticated pages, especially the list pages. (See ["Generating Components"](Generating%20Components.md#apple-gezdanjw) for instructions on freezing pages.) Remember, though, that after you freeze a page you cannot customize your page with WebAssistant.
