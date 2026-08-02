---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOJavaScript.html
archived_at: '2026-07-15T08:00:42.395524Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


![Developer Documentation](attachments/images/wothinban.gif)

__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOJavaScript

---

# Synopsis

WOJavaScript { scriptFile=_aPath_; | scriptString=_aString_; | scriptSource=_aURL_; [hideInComment=_aBOOL_;] ... };

---

# Description

WOJavaScript lets you embed a script written in JavaScript in a dynamically generated page.

---

# Bindings

**---

### scriptFile

Path to the file containing the script. The path can be statically specified in the declaration file or it can be an NSString, an object that responds to a description message by returning an NSString, or a method that returns an NSString.

**---

### scriptString

String containing the script. Typically, scriptString is an NSString object, an object that responds to a description message by returning an NSString, or a method that returns an NSString.

**---

### scriptSource

URL specifying the location of the script.

**---

### hideInComment

If hideInComment evaluates to YES, the script will be enclosed in an HTML comment (<!-- _script_ //-->). Since scripts can generate errors in some older browsers that weren't designed to execute them, you may want to enclose your script in an HTML comment. Browsers designed to run these scripts will still be able to execute them despite the surrounding comment tags.********

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
