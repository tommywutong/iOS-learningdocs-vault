---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOString.html
archived_at: '2026-07-15T07:49:45.714484Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOStateStorage.md)

---

# __WOString__

### Synopsis

__WOString__ __{__ __value__=_`aString`___;__ [__escapeHTML__=YES|NO; ][__dateformat__=_`dateFormatString`___;__] [__numberformat__=_`numberFormatString`_;] ... __};

### Description__

A WOString represents itself in the HTML page as a dynamically generated string.

**__value__**
: Text to display in the HTML page. __value__ is typically assigned an NSString object, an object that responds to a __description__ message by returning an NSString, or a method that returns an NSString.

: The NSString's contents are substituted into the HTML in the place occupied by this dynamic element.

**__dateformat__**
: A format string that specifies how __value__ should be formatted as a date. If a date format is used, __value__ must be assigned an NSCalendarDate object. If __value__ can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSCalendarDate class specification for a description of the date format syntax.

**__numberformat__**
: A format string that specifies how __value__ should be formatted as a number. If a number format is used, __value__ must be assigned an NSDecimalNumber object. If the element's value can't be interpreted according to the format you specify, __value__ is set to __nil__. See the NSNumberFormatter class specification for a description of the number format syntax.

**__escapeHTML__**
: If __escapeHTML__ is YES, HTML tags in WOString's contents are protected from being interpreted by the browser; otherwise, they are not.

: By default, WebObjects tries to ensure that the contents of a WOString appears in the client browser just as it appears in the WebObjects application source code. Thus, if a WOString's value is "<B>a bold idea</B>" (and __escapeHTML__ is YES or not specified), the string will be passed to the browser as "<B>a bold idea</B>" and it will appear in the browser as "<B>a bold idea</B>". If __escapeHTML__ is NO, WebObjects simply passes the string to the browser without protecting HTML tags from being interpreted as commands. In this case, the string will appear in the browser as "__a bold idea__".

### Examples

[How long is a fortnight?](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=StringEx1)

[Using escapeHTML](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=StringEx2)


```

```

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOSubmitButton.md)
