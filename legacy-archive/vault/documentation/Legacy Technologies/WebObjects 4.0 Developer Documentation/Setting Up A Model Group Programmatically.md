---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/CreatingModelGroups.html
archived_at: '2026-07-18T01:28:11.103961Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOModelGroup.md)
[!](EORelationship.md)

---

# Setting Up A Model Group Programmatically

In the majority of applications, the automatic creation of the default model group is sufficient. However, if your particular application requires different model grouping semantics, you can create your own EOModelGroup instance, add the appropriate models, and then use that instance to replace the default EOModelGroup. The following code demonstrates the process:
> ```
> String modelPath;                      // Assume this existsModelGroup group = new ModelGroup();    group.addModelWithPath(modelPath);ModelGroup.setDefaultGroup(group);
> ```

****

---

[!](EOModelGroup.md)
[!](EORelationship.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
