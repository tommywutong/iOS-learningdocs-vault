---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOVBScript.html
archived_at: '2026-07-15T08:09:53.592548Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOVBScript

## Element Description

WOVBScript lets you embed a script written in Visual Basic
in a dynamically generated page.

## Synopsis

WOVBScript { scriptFile=_aPath_ |
scriptString=_aString_ | scriptSource=_aURL_; [hideInComment=_aBoolean_;]
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
script -->`). Since scripts can generate
errors in some older browsers that weren't designed to execute
them, you may want to enclose your script in an HTML comment. Browsers
designed to run these scripts will still be able to execute them
despite the surrounding comment tags.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
