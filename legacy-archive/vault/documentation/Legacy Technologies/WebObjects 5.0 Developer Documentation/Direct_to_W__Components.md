---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Direct_to_W__Components.html
archived_at: '2026-07-15T08:12:21.996733Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_Web_Templates.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Property_Level_Components.md)

## Direct to Web Reusable Components

Some Direct to Web templates can be viewed as implementing
more than one task:

- A MasterDetailPage
  template consists of a select component at the top and an edit component
  at the bottom.
- An EditRelationshipPage template consists of a select component
  at the top and query, select, and edit components at the bottom.

Direct to Web displays these subcomponents with Direct to
Web templates. For example, a NEUMasterDetailPage displays its select
component using a NEUListPage and its edit component with a NEUInspectPage.
However, the Direct to Web templates are not designed to be nested
directly within other Direct to Web templates. To permit nesting, Direct
to Web uses another type of component called a _Direct
to Web reusable component_, which acts as an interface
between the outer template and the inner template. There are five
types of Direct to Web reusable components; they are listed in [Table 3-3](#apple-ijauur2cjbbuq).

__Table
3-3 Reusable components__

__|  |  |
| --- | --- |
| Name | Task |__| D2WEdit | Edit |
| D2WInspect | Inspect |
| D2WList | List |
| D2WQuery | Query |
| D2WSelect | Select |

[Table 3-4](#apple-ijauuskbjfbuq) shows how the reusable components are used in the
Direct to Web templates containing multiple tasks. The remaining
templates do not contain Direct to Web reusable components.

__Table
3-4 Direct to Web templates and reusable
components__

__|  |  |
| --- | --- |
| Direct to Web Template | Direct to Web Reusable Components Used |__| BASMasterDetailPageNEUMasterDetailPageWOLMasterDetailPage | D2WSelect, D2WEdit |
| BASEditRelationshipPageNEUEditRelationshipPageWOLEditRelationshipPage | D2WSelect, D2WQuery, D2WEdit |

In addition to allowing the nesting of Direct to Web templates,
Direct to Web reusable components can also be embedded in your own
components; they are available on a palette in WebObjects Builder.
See the _Direct to Web Reference_ for more information
about the individual Direct to Web reusable components.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_Web_Templates.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Property_Level_Components.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
