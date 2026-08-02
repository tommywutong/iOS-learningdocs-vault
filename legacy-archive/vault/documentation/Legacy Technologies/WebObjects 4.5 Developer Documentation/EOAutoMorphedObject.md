---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOAutoMorphedObject.html
archived_at: '2026-07-15T08:11:31.637003Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOAutoMorphedObject

> __Inherits
> from:__  NSObject

> __Implements:__ com.apple.yellow.eocontrol.EOEnterpriseObject

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

The EOAutoMorphedObject class is available
in Yellow Box applications only; these is not an equivalent in Java
Client.

EOAutoMorphedObject allows you to use Objective-C enterprise
object classes in Java code without wrapping them. When you use
an unwrapped Objective-C enterprise object in Java code, the Java bridge
creates EOAutoMorphedObjects to represent them. The drawback to
using this feature is that you must use key-value coding rather
than invoke methods directly.

You never instantiate or subclass EOAutoMorphedObject. Rather,
it's something that the Java bridge creates automatically.

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
