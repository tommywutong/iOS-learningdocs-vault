---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/Restricting_to_Entities.html
archived_at: '2026-07-15T08:12:30.547644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](WebAssistant_Overview.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Customizing_Pages.md)

## Restricting Access to Entities

The Entities display of the WebAssistant enables you to specify
which entities of the database model appear in the application.
Of those entities, it further allows you to specify which are read-only
and which the user can write data to. Records from read-only entities are
restricted from appearing in edit pages.

The user interface for accomplishing these tasks is simple,
as the following example illustrates:

![[image: ../Art/waentities.gif]](../Art/waentities.gif)

To specify an entity that shouldn't appear in the application,
select it and use the arrow keys to move it to the Hidden Entities
column. To specify an entity that should be read-only, select it
and use the arrow keys to move it to the Read-only Entities column.
By default, all entities initially appear in the Read/Write Entities
column.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](WebAssistant_Overview.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Customizing_Pages.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
