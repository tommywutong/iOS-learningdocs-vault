---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/ReusableComponents/D2WQuery.html
archived_at: '2026-07-15T08:12:46.328364Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

# D2WQuery

## Component Description

This Direct to Web reusable component displays a query component.
See the "Direct to Web" chapter of _WebObjects Tools
and Techniques_ for information about the behavior and
appearance of this component.

## Synopsis

D2WQuery { [action=_anAction_;]
[displayKeys=_keyArray_;] entityName=_nameString_; queryDataSource=_aDataSource_;
[pageConfiguration=_configurationName_;]
};

## Bindings

**action**
: The action method to invoke when the user clicks Search
DB. This method is invoked after the D2WQuery component fetches
the objects matching the query.

**displayKeys**
: The properties of the entity to query (NSArray). You
can also represent the array as a string: "(_prop1_, _prop2_,
...)".

**entityName**
: The name of the entity to query for (String).

**queryDataSource**
: An EODataSource containing the objects that match the
query.

**pageConfiguration**
: The named configuration containing the Web Assistant
settings for this component (String). If this binding is not specified,
the "\*all\*" configuration for the query task and the _entityName_ entity
is used. See the "Direct to Web" chapter of _WebObjects
Tools and Techniques_ for more information about named
configurations.

## Example

> ```
> myQuery : D2WQuery {
>     entityName = "Movie";
>     displayKeys = "(title, roles)";
>     queryDataSource = displayGroup.dataSource;
>     action = displayGroup.fetch;
> }
> ```

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
