---
title: Developing SMIL Presentations
apple_id: TP40000999
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-03-29'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Developing_SMIL_Presentation/Reference/WOSMILActiveLink.html
archived_at: '2026-07-18T02:20:17.970454Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing SMIL Presentations](toc.md)


[!](WOSMILPar.md) [!](WOSMILAnchor.md)

## WOSMILActiveLink

This element provides a way to link an element to a presentation;
it corresponds to the `<a>` tag.
Its bindings are described in [Table 4-16](#apple-ijbegskeirdes).

__Table
4-16 Basic bindings of the WOSMILActiveLink
element__

| Binding | Description |
| `filename` | Filename of the presentation to show. Use with `framework`. `filename` and `href` are mutually exclusive. |
| `framework` | Logical location of the presentation indicated by `filename`. Values: `"app"`, `"JavaJDBCAdaptor"`, `"JavaWOExtensions"` or `"JavaWebObjects"`. |
| `href` | URL of the media object to render. `href` and `filename` are mutually exclusive. |
| `pageName` | Name of the component to render. `filename`, `href`, and `pageName` are mutually exclusive. |
| `show` | Value: `"replace"`, `"new"`, or `"pause"`. |
| `title` | Meaningful description for this element. |

[!](WOSMILPar.md) [!](WOSMILAnchor.md)

---

© 2002 Apple Computer, Inc. (Last Updated March 29, 2002)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
