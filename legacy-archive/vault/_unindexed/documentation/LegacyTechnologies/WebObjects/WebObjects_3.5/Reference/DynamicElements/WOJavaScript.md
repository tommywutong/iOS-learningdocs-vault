---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOJavaScript.html
archived_at: '2026-07-15T07:55:28.883400Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOImageButton.md)

## WOJavaScript

### Synopsis

__WOJavaScript__ __{__ __scriptFile__=_aPath_ | __scriptString__=_aString_ | __scriptSource__=_aURL___;__ [__hideInComment__=_aBOOL_;] ... __};__

### Description

WOJavaScript lets you embed a script written in JavaScript in a dynamically generated page.

**__scriptFile__**
: Path to the file containing the script. The path can be statically specified in the declaration file or it can be an NSString, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.

**__scriptString__**
: String containing the script. Typically, __scriptString__ is an NSString object, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.

**__scriptSource__**
: URL specifying the location of the script.

**__hideInComment__**
: If __hideInComment__ evaluates to YES, the script will be enclosed in an HTML comment (<!-- _script_ //-->). Since scripts can generate errors in some older browsers that weren't designed to execute them, you may want to enclose your script in an HTML comment. Browsers designed to run these scripts will still be able to execute them despite the surrounding comment tags.

### Examples

[Simple math](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=JavaScriptEx1)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOPasswordField.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
