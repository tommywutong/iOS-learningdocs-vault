---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Property_Level_Components.html
archived_at: '2026-07-15T08:12:23.037108Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_W__Components.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Direct_to_W_rganization.md)

## Property-Level Components

Direct to Web uses _property-level components_ to
display, query, and edit individual properties of an entity. A property
is an attribute or relationship of an entity. Direct to Web defines
components for manipulating strings, dates, numbers, to-one relationships, to-many
relationships, and other objects. For example, [Table 3-5](#apple-ijauur2bi5cuk) lists some property-level components;
these components work with numbers.

__Table
3-5 Number property-level components (java.lang.Number, java.math.BigDecimal)__

__|  |  |  |
| --- | --- | --- |
| Display | Edit | Query |__| D2WDisplayNumber | D2WEditNumber | D2WQueryNumberOperator |
| D2WDisplayStyledNumber |  | D2WQueryNumberRange |
| D2WDisplayBoolean | D2WEditBoolean | D2WQueryBoolean |

At runtime when a template displays a property, Direct to
Web chooses which property-level component should display the property.
The choice depends on the property's data type and how you configure
the application with the Web Assistant.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Direct_to_W__Components.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Direct_to_W_rganization.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
