---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Direct_to_Web_Templates.html
archived_at: '2026-07-15T08:12:23.016446Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_Web_Components.md)[!](Direct_to_W__Components.md)

## Direct to Web Templates

Direct to Web generates the task Web pages using instances
of the D2WPage class (itself a descendent of the WOComponent class) called Direct
to Web templates. A Direct to Web template defines the basic layout for the
task's user interface. Direct to Web includes 29 templates: 9 for the Basic look,
10 for the Neutral look, and 10 for the WebObjects look. For more information
about looks, see ["The
Different Looks for WebObjects Applications"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/index.html). The Direct to Web templates are
listed in [Table 3-2](#apple-ijauuskbirdug).

__Table 3-2 Direct to Web
Templates__

 __|  |  |  |  |
| --- | --- | --- | --- |
| Task | Basic Look | Neutral Look | WebObjects Look |__| Confirm | BASConfirmPage | NEUConfirmPage | WOLConfirmPage |
| Edit relationship | BASEditRelationshipPage | NEUEditRelationshipPage | WOLEditRelationship- Page |
| Error | BASErrorPage | NEUErrorPage | WOLErrorPage |
| Edit, Inspect | BASInspectPage | NEUInspectPage | WOLInspectPage |
| List, Select | BASListPage | NEUListPage | WOLListPage |
| List | BASMasterDetailPage | NEUMasterDetailPage | WOLMasterDetailPage |
| List, Select | BASPlainListPage | NEUPlainListPage | WOLPlainListPage |
| Query all | BASQueryAllEntitiesPage | NEUQueryAllEntitiesPage | WOLQueryAllEntities- Page |
| Query | BASQueryPage | NEUQueryPage | WOLQueryPage |
| Edit, Inspect |  | NEUTabInspectPage | WOLTabInspectPage |

Some Direct to Web templates perform multiple
tasks. For example, an InspectPage template also edits. For some tasks, there are
multiple Direct to Web templates in a given look that you can use. For example,
you can use a ListPage, a PlainListPage, or a MasterDetailPage template to
perform the list task.

Like any other
WOComponent, a Direct to Web template has an HTML template (`.html` )
file and a bindings (`.wod` ) file. What differentiates a Direct to
Web template from other components is that it resolves its bindings with the help
of the Direct to Web framework at runtime.

Note
that a Direct to Web template is different from a component's HTML template
(`.html` ) file: a Direct to Web template is a special type of
component while an HTML template is a file containing the HTML code that defines
a component's appearance.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_Web_Components.md)[!](Direct_to_W__Components.md)

© 2001 Apple Computer, Inc.

Shop the [Apple Online Store](http://www.apple.com/store/) (1-800-MY-APPLE), visit an [Apple Retail Store](http://www.apple.com/retail/), or find a [reseller](http://www.apple.com/buy/locator/).

- [Mailing Lists](http://lists.apple.com/)
- [RSS Feeds](https://developer.apple.com/rss/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
