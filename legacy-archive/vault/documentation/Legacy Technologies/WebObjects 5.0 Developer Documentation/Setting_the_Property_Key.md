---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Setting_the_Property_Key.html
archived_at: '2026-07-15T08:12:23.108812Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Rendering_t_eb_Template.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Resolving_K_he_Property.md)

## Setting the Property Key

When the template begins to render the query fields for the
entity's attributes and relationships (like the category and the
release date) it encounters the WORepetition labeled `ResourceRepetition`.
See [Listing 3-4](Rendering_t_eb_Template.md#apple-ijdemrckijduq) and [Listing 3-5](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Setting_the_Property_Key.html#BAJCFBFA). The WORepetition's `list` attribute
is bound to `d2wContext.displayPropertyKeys`.
Since `displayPropertyKeys` is
not in its dictionary, the Direct to Web context resolves the key
using the rule engine, which causes the following rule to fire:

```
*true* => displayPropertyKeys = "defaultPropertyKeysFromEntity"
```

The `defaultPropertyKeysFromEntity` key
refers to a method that derives a value based on the Direct to Web
context's dictionary. See ["The Rule System"](The_Rule_System.md#apple-ijauurcbifbeu) for more information
about the how derived values are handled. The `defaultPropertyKeysFromEntity` method
returns an NSArray containing the Movie entity's property keys,
which resolves the WORepetition's `list` binding.

As the repetition iterates, it sets the `item` attribute
for each of the objects in the list. The first object is the string
"category". Since `item` is
bound to `d2wContext.propertyKey`,
the Direct to Web context sets the value for `propertyKey` in
its dictionary to "category". At the same time, it sets the
value for the `attribute` key
to the `category` EOAttribute
and the value for the `relationship` key
to `null`, since a Movie's `category` property
is an attribute and not a relationship. Now the Direct to Web Context
dictionary contains the information listed in [Table 3-7](#apple-ijauuscbjbeeu).

__Table
3-7 Direct to Web context dictionary after
setting propertyKey__

__|  |  |
| --- | --- |
| Key | Value |__| `task` | "query" |
| `entity` | <EOEntity Movie> |
| `propertyKey` | "category" |
| `attribute` | <EOAttribute category> |
| `relationship` | `null` |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Rendering_t_eb_Template.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Resolving_K_he_Property.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
