---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.18.html
archived_at: '2026-07-15T08:09:57.066109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Batching%20the%20Output%20of%20a%20WODisplayGroup.md) [!](Working%20with%20Unnormalized%20Tables.md)

#   Manipulating Selections in a WODisplayGroup

##  Synopsis

Outlines various methods to manipulate a WODisplayGroup selection.

##  Description

A WODisplayGroup keeps a selection in terms of indexes into the array of displayed objects. Components that display values for multiple objects are responsible for updating the selection in their WODisplayGroups according to user actions on their dynamic elements. This is typically done with the
setSelectionIndexes
method. Other methods available for indirect manipulation of the selection are the action methods
selectNext
and
selectPrevious
.

To get the selection, you can use the
selectionIndexes
method, which returns an array of indexes as Number objects (NSNumber in Objective-C), or
selectedObjects
, which returns an array containing the selected objects themselves. Another method,
selectedObject
, returns the first selected object if there is one.

!Note The selection is a programmatical selection only. WebObjects does not
automatically highlight the selected objects on the web page.!

##  See Also

- 

  [Creating a WODisplayGroup](Creating%20a%20WODisplayGroup.md#apple-gi3tanbu)
- 

  [Setting a WODisplayGroup's Fetch Specification Programmatically](Setting%20a%20WODisplayGroup%27s%20Fetch%20Specification%20Programmatically.md#apple-gi3tanbu)
- 

  WODisplayGroup class specification in the _WebObjects Framework Reference_

##  Questions

- 

  What can I do with WODisplayGroup selections?

##  Keywords

- 

  WODisplayGroup
- 

  Selection

##  Revision History

22 February 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Batching%20the%20Output%20of%20a%20WODisplayGroup.md) [!](Working%20with%20Unnormalized%20Tables.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
