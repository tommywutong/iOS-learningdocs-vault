---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOString.html
archived_at: '2026-07-15T07:55:35.429779Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOStateStorage.md)

## WOString

### Synopsis

__WOString__ __{__ __value__=_aString___;__ [__escapeHTML__=YES|NO; ][__dateformat__=_dateFormatString___;__] [__numberformat__=_numberFormatString_;] ... __};__

### Description

A WOString represents itself in the HTML page as a dynamically generated string.

**__value__**
: Text to display in the HTML page. __value__ is typically assigned an NSString object, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.
: The NSString's contents are substituted into the HTML in the place occupied by this dynamic element.

**__escapeHTML__**
: If __escapeHTML__ is YES, HTML tags in WOString's contents are protected from being interpreted by the browser; otherwise, they are not.
: By default, WebObjects tries to ensure that the contents of a WOString appears in the client browser just as it appears in the WebObjects application source code. Thus, if a WOString's value is "<B>a bold idea</B>" (and __escapeHTML__ is YES or not specified), the string will be passed to the browser as "<B>a bold idea</B>" and it will appear in the browser as "<B>a bold idea</B>". If __escapeHTML__ is NO, WebObjects simply passes the string to the browser without protecting HTML tags from being interpreted as commands. In this case, the string will appear in the browser as "__a bold idea__".

**__dateformat__**
: A format string that specifies how __value__ should be formatted as a date. If a date format is used, __value__ must be assigned an NSCalendarDate object. If __value__ can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSCalendarDate class specification for a description of the date format syntax.

**__numberformat__**
: A format string that specifies how __value__ should be formatted as a number. If a number format is used, __value__ must be assigned an NSNumber object. If the element's value can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSNumberFormatter class specification for a description of the number format syntax.

### Examples

[How long is a fortnight?](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=StringEx1)

[Using escapeHTML](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=StringEx2)

[Using date and number formats](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=StringEx3)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOSubmitButton.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
