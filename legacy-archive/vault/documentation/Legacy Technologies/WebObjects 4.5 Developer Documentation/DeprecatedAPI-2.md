---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Deprecated.html
archived_at: '2026-07-15T08:11:45.206375Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](EOInterfaceTOC.md)

# DeprecatedAPI

This file enumerates those EOInterface classes and methods
that have been deprecated and should no longer be used. Wherever
possible, notes have been included to indicate what API should be
used in place of the deprecated class or method.

## EOTableAssociation

### isEditableAtRow

`public boolean isEditableAtRow(int  row)`

Returns whether or not the display object bound
to the receiver is editable at  _row_ as
determined by the `EnabledAspect`.
If this aspect is bound, a non-zero value at  _row_ indicates
that the property can be edited. If the `EnabledAspect` is
unbound all rows are considered editable.

---

[![Table of Contents](attachments/images/up.gif)](EOInterfaceTOC.md)
