---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/Concepts/EOModelGroup.html
archived_at: '2026-07-15T08:13:40.734637Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

# EOModelGroup.Concepts

## Setting Up A Model Group Programmatically

In the majority of applications, the automatic creation of the default model group is sufficient. However, if your particular application requires different model grouping semantics, you can create your own EOModelGroup instance, add the appropriate models, and then use that instance to replace the default EOModelGroup. The following code demonstrates the process:

> ```
> String modelPath;  // Assume this exists
> EOModelGroup group = new EOModelGroup();
>
> group.addModelWithPath(modelPath);
> EOModelGroup.setDefaultGroup(group);
> ```

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
