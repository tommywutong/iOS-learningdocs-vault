---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOString.html
archived_at: '2026-07-15T08:09:53.531980Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOString

## Element Description

A WOString represents itself in the HTML page as a dynamically
generated string.

## Synopsis

WOString { value=_aString_;
[formatter=_formatterObj_;] [escapeHTML=_aBoolean_;
] [dateformat=_dateFormatString_;]
[numberformat=_numberFormatString_;] [valueWhenEmpty=_emptyString_...
};

## Bindings

**value**
: Text to display in the HTML page. __value__ is
typically assigned an NSString object, an
object that responds to a description message by returning an NSString,
or a method that returns an NSString. The NSString's
contents are substituted into the HTML in the place occupied by
this dynamic element.

**escapeHTML**
: If __escapeHTML__ evaluates to `true` (or `YES` ),
the string rendered by __value__ is converted
so that characters which would be interpreted as HTML control characters
become their escaped equivalent (this is the default). Thus, if
a your value is "`a <b>bold</b>
idea`", the string passed to the client browser
would be "`a <B>bold</B>
idea`", but it would display in the browser
as "`a <b>bold</b> idea`".
If __escapeHTML__ evaluates to `false` (or `NO`), WebObjects
simply passes your data to the client browser "as is." In this
case, the above example would display in the client browser as "`a
bold idea`". If you are certain that your strings
have no characters in them which might be interpreted as HTML control
characters, you get better performance if you set __escapeHTML__ to `false` (or `NO`).

**formatter**
: An instance of an NSFormatter subclass
to be used to format object values for display as strings. This
attribute should specify a variable containing (or method returning)
a preconfigured formatter object. For instance, a WOString might
have the binding:

> ```
> formatter = application.dateFormatter
> ```

With the following code:

> ```
> // Application.wos
> NSFormatter *_dateFormatter;
>
> - (NSFormatter *)dateFormatter {
>     if (!_dateFormatter) {
>         _dateFormatter = [[NSDateFormatter alloc]               initWithDateFormat:@"%m/%d/%Y"             allowNaturalLanguage:NO];
>     }
>     return _dateFormatter;
> }
> ```

If a user enters an "unformattable" value, WOString passes
the invalid value through, allowing you to send back an error page
that shows the invalid value.

**dateformat**
: A format string that specifies how __value__ should
be formatted as a date. If a date format is used, __value__ can
be assigned an NSCalendarDate object (if it is assigned an NSString
object, it is stored as the string representation of an NSCalendarDate
object). If the element's value can't be interpreted according
to the format you specify, __value__ is set
to `nil`. See the NSCalendarDate class
specification for a description of the date format syntax.

**numberformat**
: A format string that specifies how __value__ should
be formatted as a number. If a number format is used, __value__ must
be assigned an NSNumber object. If the element's value can't
be interpreted according to the format you specify, __value__ is
set to `nil`. See the NSNumberFormatter
class specification for a description of the number format syntax.

**valueWhenEmpty**
: A string that will be substituted for _value_ when _value_ is
the empty string.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
