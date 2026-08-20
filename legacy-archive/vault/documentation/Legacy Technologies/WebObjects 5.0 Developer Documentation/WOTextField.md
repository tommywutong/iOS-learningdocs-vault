---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOTextField.html
archived_at: '2026-07-15T08:14:39.332993Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOTextField

## Element Description

A WOTextField represents itself as a text input field. It
corresponds to the HTML element `<INPUT TYPE="TEXT"...>`.

## Synopsis

WOTextField { value=_aValue_;
[formatter=_formatterObj_;] [dateformat=_dateFormatString_;] [numberformat=_numberFormatString_;]
[name=_fieldName_;] [disabled=_aBoolean_;]
... };

## Bindings

**value**
: During page generation, value sets the default value
displayed in the single-line text field. During request handling,
it holds the value the user entered into the field, or the default value
if the user left the field untouched.

**formatter**
: An instance of an NSFormatter subclass to be used
to format object values for display as strings, and format user-entered
strings back into object values. This attribute should specify
a variable containing (or method returning) a preconfigured formatter
object. For instance, a WOTextField might have the binding:

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

If a user enters an "unformattable" value, WOTextField
passes the invalid value through, allowing you to send back an error
page that shows the invalid value.

**dateformat**
: A format string that specifies how __value__ should
be formatted as a date. If a date format is used, __value__ can
be assigned an NSCalendarDate object (if it is assigned an NSString
object, it will be stored as the string representation of an NSCalendarDate
object). If the element's value can't be interpreted according
to the format you specify, it is set to `nil`.
See the NSCalendarDate class specification for a description of
the date format syntax.

**numberformat**
: A format string that specifies how __value__ should
be formatted as a number. If a number format is used, __value__ must
be assigned an NSNumber object. If the element's value can't
be interpreted according to the format you specify, __value__ is
set to `nil`. See the NSNumberFormatter
class specification for a description of the number format syntax.

**name**
: Name that uniquely identifies this element within the
form. You may specify a name or let WebObjects automatically assign
one at runtime.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
the element appears in the page but is not active. That is, __value__ does
not contain the user's input when the page is submitted.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
