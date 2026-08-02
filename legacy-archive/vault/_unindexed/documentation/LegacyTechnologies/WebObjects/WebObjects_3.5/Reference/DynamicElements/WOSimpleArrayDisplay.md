---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOSimpleArrayDisplay.html
archived_at: '2026-07-15T07:55:33.407878Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WOExtensionsTOC.md) [!Previous Section](WORedirect.md)

## WOSimpleArrayDisplay

### Synopsis

**__WOSimpleArrayDisplay__ __{__ __list =__ _anObjectArray___;__ [__numberToDisplay =__ _anInt___;__] [__itemDisplayKey =__ _aKey___;__] [__listAction =__ _methodName___;__] [__listActionString =__ _actionString___;__]__};__**

### Description

The WOSimpleArrayDisplay component is intended to display a to-many relationship of an Enterprise Object. It could also be used to display an array of objects.
The WOSimpleArrayDisplay is designed to only provide an idea of what is in the relationship (or list). It only displays the first _n_ items in the list, where _n_ is specified by the __numberToDisplay__ attribute. (The default is 5.) If you want, you can have a hyperlink displayed at the bottom of the list by specifying the __listAction__ and __listString__ attributes. You could use this hyperlink to provide more information about the relationship or, for example, to list all of the elements in the relationship.
If you use Direct to Web to create your application, you may have a page that uses WOSimpleArrayDisplay.

**__list__**
: Array of items to display.

**__numberToDisplay__**
: The number of items to display at one time. The default is 5 items.

**__itemDisplayKey__**
: Key to the value that should be displayed for each item. For example, if you were displaying a movies entity object, you'd want to display the value of the movieName key.

**__listAction__**
: Method to perform when the hyperlink is clicked.

**__listActionString__**
: The string that should appear on the hyperlink. The default is "Inspect."

[!Table of Contents](WOExtensionsTOC.md) [!Next Section](WOSortOrder.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
