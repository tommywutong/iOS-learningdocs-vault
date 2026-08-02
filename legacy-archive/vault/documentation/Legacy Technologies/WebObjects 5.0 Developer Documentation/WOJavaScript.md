---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOJavaScript.html
archived_at: '2026-07-15T08:14:39.094961Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOJavaScript

## Element Description

WOJavaScript lets you embed a script written in JavaScript
in a dynamically generated page.

## Synopsis

WOJavaScript { scriptFile=_aPath_;
| scriptString=_aString_; | scriptSource=_aURL_; [hideInComment=_aBoolean_;]
... };

## Bindings

**scriptFile**
: Path to the file containing the script. The path can
be statically specified in the declaration file or it can be an NSString,
an object that responds to a description message by returning an NSString,
or a method that returns an NSString.

**scriptString**
: String containing the script. Typically, __scriptString__ is
an NSString object, an object that responds
to a description message by returning an NSString,
or a method that returns an NSString.

**scriptSource**
: URL specifying the location of the script.

**hideInComment**
: If __hideInComment__ evaluates
to `true` (or `YES`),
the script will be enclosed in an HTML comment (`<!--
script //-->`). Since scripts can generate
errors in some older browsers that weren't designed to execute
them, you may want to enclose your script in an HTML comment. Browsers
designed to run these scripts will still be able to execute them
despite the surrounding comment tags.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
