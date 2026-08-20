---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.1b.html
archived_at: '2026-07-15T08:09:57.583001Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Fetching%20with%20an%20Editing%20Context.md) [!](Creating%20Fetch%20Specifications%20Programmatically.md)

#   Setting a WODisplayGroup's Fetch Specification Programmatically

##  Synopsis

Describes how you use a programmatically-generated EOFetchSpecification with a WODisplayGroup.

##  Description

A WODisplayGroup does not actually maintain a fetch specification; this is the job of the display group's EODatabaseDataSource. The [Creating a WODisplayGroup](Creating%20a%20WODisplayGroup.md#apple-gi3tanbu)
programming topic contains more information about the EODatabaseDataSource. WebObjects provides two nonprogrammatic ways to set this fetch specification.

If you use Project Builder's wizard to create a component with a display group, the fetch specification is created based on the display group's
queryMatch
dictionary using the
qualifyDataSource
method. See the WODisplayGroup class specification in the _WebObjects Framework Reference_
for more information about the
queryMatch
dictionary.

You can also create a fetch specification using EOModeler's fetch specification builder. You associate this fetch specification with the display group using WebObjects Builder's display group configuration panel. See "Working With Fetch Specifications" in _Enterprise Objects Framework Tools and Techniques_
and "Configuring the Display Group" in _WebObjects Framework Tools and Techniques_
for more information.

However, sometimes you need to create the fetch specification programmatically. For example, to perform a keyword search with an unlimited number of keywords, you must build the qualifier dynamically. To get the WODisplayGroup to fetch using such a fetch specification you need to send the EODatabaseDataSource the fetch specification as shown in the following Java code.

```

WODisplayGroup dg;       // assume this existsEOFetchSpecification fs; // assume this exists// Get the EODatabaseDataSourceEODatabaseDataSource ds = (EODatabaseDataSource)dg.dataSource();// Set the fetch specificationds.setFetchSpecification(fs);// Fetch the objectsdg.fetch();
```

##  See Also

- 

  [Creating a WODisplayGroup](Creating%20a%20WODisplayGroup.md#apple-gi3tanbu)
- 

  [Batching the Output of a WODisplayGroup](Batching%20the%20Output%20of%20a%20WODisplayGroup.md#apple-gi3tanbu)
- 

  [Manipulating Selections in a WODisplayGroup](Manipulating%20Selections%20in%20a%20WODisplayGroup.md#apple-gi3tanbu)

##  Questions

- 

  How do I use a programmatically-generated fetch specification with a WODisplayGroup?

##  Keywords

- 

  WODisplayGroup
- 

  Fetch
- 

  Data Source

##  Revision History

19 February 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Fetching%20with%20an%20Editing%20Context.md) [!](Creating%20Fetch%20Specifications%20Programmatically.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
