---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Rendering_a__An_Example.html
archived_at: '2026-07-15T08:12:23.057445Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](The_Direct_to_Web_Factory.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Rendering_t_eb_Template.md)

## Rendering a Direct to Web Page: An Example

This section describes how the components, the Direct to Web
context, and the Direct to Web factory interact while creating and
rendering a query page for the Movie entity. This example begins
with the user viewing a query all page in the Basic look and clicking
a hyperlink labeled "more.." in the Movie row, which links to
the query page. The query all page is rendered using a `BASQueryAllEntitiesPage.wo` template.

### Creating the Query Page

When the user clicks the hyperlink, the hyperlink invokes
the `showRegularQueryAction` method
defined in the D2WQueryAllEntitiesPage class, the superclass of
the BASQueryAllEntitiesPage class. [Listing 3-2](#apple-ijauurchijcui) shows the implementation
of the `showRegularQueryAction` method.

__Listing
3-2 D2WQueryAllEntitiesPage.showReqularQueryAction__

```
public WOComponent showRegularQueryAction()
{
    QueryPageInterface newQueryPage = D2W.factory().queryPageForEntityNamed
        (entity().name(),session());
    return (WOComponent)newQueryPage;
}
```

The Direct to Web factory object creates a Direct to Web context
and initializes its NSDictionary by setting the value for the `task` key
to "query" and the value for the `entity` key
to the Movie EOEntity.

__Table 3-6 Initial
Direct to Web context dictionary__

__|  |  |
| --- | --- |
| Key | Value |__| `task` | "query" |
| `entity` | <EOEntity Movie> |

To determine which Direct to Web template to create, the Direct
to Web factory asks the Direct to Web context for the value of the `pageName` key.
Since this key is neither in the dictionary nor a derived value
from the dictionary, the Direct to Web context enlists the aid of
the rule engine. [Listing 3-3](#apple-ijauuqsgjfdum) shows the rules that resolve the key.

__Listing
3-3 Rules used to resolve the pageName key__

```
((look = "BasicLook") and (task = "query")) => pageName = "BASQueryPage"

*true* => look = "BasicLook"
```

A rule has a left-hand side and a right-hand side separated
by "=>". The left-hand side specifies a condition that must
be met for the rule to be a candidate to "fire," or resolve
a key. The right-hand side specifies the key-value assignment that
takes place when the rule fires. Since the left-hand side for the
second rule is true, the rule always fires when the Direct to Web
context wants the value for the `look` key.

There are three sources for the rules that the rule engine
uses:

- __The
  Direct to Web framework__ defines rules that determine
  the default application behavior.
- __You__ can write your own rules that override
  the framework's defaults rules.
- __The Web Assistant__ generates rules involving
  the specific application information. These rules are generated
  automatically as you configure the application with the Web Assistant;
  you don't have to write them.

See ["The Rule System"](The_Rule_System.md#apple-ijauurcbifbeu) for more information about rules.

The two rules that resolve the `pageName` key
(defined in the Direct to Web Framework) fire and the Direct to
Web context returns "BASQueryPage" as the value for the `pageName` key.

Knowing the template name, the Direct to Web factory object
creates a page using the `WOComponent.pageWithName` method.
Then it attaches the Direct to Web context to the newly generated
page.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](The_Direct_to_Web_Factory.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Rendering_t_eb_Template.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
