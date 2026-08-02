---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOJavaScript.html
archived_at: '2026-07-15T07:49:42.271156Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOImage.md)

---

# __WOJavaScript__

### Synopsis

__WOJavaScript__ __{__ __scriptFile__=_`aPath`_ | __scriptString__=_`aString`_ | __scriptSource__=_`aURL`___;__ [__hideInComment__=_`aBOOL`_;] ... __};

### Description__

WOJavaScript lets you embed a script written in JavaScript in a dynamically generated page.

**__scriptFile__**
: Path to the file containing the script. The path can be statically specified in the declaration file or it can be an NSString, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.

**__scriptString__**
: String containing the script. Typically, __scriptString__ is an NSString object, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.

**__scriptSource__**
: URL specifying the location of the script.

**__hideInComment__**
: If __hideInComment__ evaluates to YES, the script will be enclosed in an HTML comment (<!-- _`script`_ //-->). Since scripts can generate errors in some older browsers that weren't designed to execute them, you may want to enclose your script in an HTML comment. Browsers designed to run these scripts will still be able to execute them despite the surrounding comment tags.

### Examples

[Simple math](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=JavaScriptEx1)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOPasswordField.md)
