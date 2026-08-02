---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Debug11.html
archived_at: '2026-07-15T08:05:11.277776Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Debug10.md)

## Isolating Portions of a Page

If a component is producing unexpected HTML output, you can try to isolate the problem by displaying small portions of the page at a time. Use HTML comments (__<!--__) to comment out all but the suspect portion of the page and reload the component. Verify that this portion works as you intend it to. Reduce the size of the commented out portion of the page until more and more of the page is visible in the browser. Continue until you have found the offending area.

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](Programming%20Pitfalls%20to%20Avoid.md)
