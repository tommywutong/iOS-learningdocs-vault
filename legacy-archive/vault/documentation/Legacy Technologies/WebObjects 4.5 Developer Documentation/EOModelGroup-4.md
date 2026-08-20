---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/More/EOModelGroup.html
archived_at: '2026-07-15T08:11:35.843099Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)

# EOModelGroup

## Setting Up A Model Group Programmatically

In the majority of applications, the automatic creation of
the default model group is sufficient. However, if your particular
application requires different model grouping semantics, you can
create your own EOModelGroup instance, add the appropriate models,
and then use that instance to replace the default EOModelGroup.
The following code demonstrates the process:

> ```
> NSString *modelPath;  // Assume this exists
> EOModelGroup *group = [EOModelGroup new];
>
> [group addModelWithFile:modelPath];
> [EOModelGroup setDefaultGroup:group];
> [group release];
> ```

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
