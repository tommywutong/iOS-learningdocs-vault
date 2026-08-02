---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOStateStorage.html
archived_at: '2026-07-15T07:55:34.392837Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOResetButton.md)

## WOStateStorage

### Synopsis

__WOStateStorage__ __{__ [__size__=_numBytes___;__] ... __};__

### Description

A WOStateStorage element provides a simple mechanism for storing application state in an HTML page. If you include a WOStateStorage element in a form, any session and persistent data will be stored in the page rather than on the server. (For a detailed discussion of state management in WebObjects applications, see the chapter "[Managing State](../../DevGuide/State/StateTOC.md)" in the _WebObjects Developer's Guide_).

WOStateStorage uses HTML hidden fields ( <INPUT TYPE="HIDDEN"...>) to store state data. It will use as many hidden fields as needed to store the data, but no field will be larger than the size specified by the __size__ attribute. The default size setting is designed to work with most browsers.

**__size__**
: Maximum size for each of the hidden fields used to store the state data. This attribute is optional; if __size__ is not specified, the maximum size for hidden fields will be 1000 bytes.

Since WOStateStorage elements are implemented using hidden fields-which in HTML must be located within a form-they too must be located within a form. If a page has more than one form, you must declare a WOStateStorage element within each form.

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOString.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
