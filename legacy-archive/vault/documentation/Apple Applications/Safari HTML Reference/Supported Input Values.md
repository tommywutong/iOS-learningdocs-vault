---
title: Safari HTML Reference
apple_id: TP40002049
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariHTMLRef/Articles/InputTypes.html
archived_at: '2026-07-15T05:19:05.992542Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML Reference](Introduction.md)


[Next](Supported%20Meta%20Tags.md)[Previous](Supported%20Attributes.md)

# Supported Input Values

Supported values for the `input` element are described here.

Safari supports many different input types. They can be specified using the `type` attribute of the `input` element. These input types are listed below.

A button input type. More versatile than a submit button.

A standard checkbox.

An input control for specifying a RGB color value. The user can select a color from a color well.

An input control for specifying a date value. The user can select a month, day of the month, and year. Unlike `datetime`, `date` does not offer the time of day.

____Availability____: Available for iOS 5.0 and later.

An input control for specifying a date and time value. The user can select a month, day of the month, year, and time of day.

____Availability____: Available for iOS 5.0 and later.

An input control for specifying a date and time value where the format depends on the locale.

____Availability____: Available for iOS 5.0 and later.

A text field for specifying an email address. Brings up a keyboard optimized for email address entry for iOS.

____Availability____: Available for iOS.

A file upload interface.

A hidden input type (to store values without showing them on the page). Note that the input can still be seen in the page source.

An image that acts as an input.

An input control for selecting a month.

____Availability____: Available for iOS 5.0 and later.

A text field for specifying a number. Brings up a number pad keyboard for iOS. Specifying an input pattern of `\d*` or `[0-9]*` is equivalent to using this type.

____Availability____: Available for iOS.

A visually shielded password field.

A radio button.

A slider. Its minimum value should be set with the `min` attribute, its maximum value should be set with `max`, and its discrete step size should be set with `step`.

____Support Level____: Apple extension.

A reset button for a form.

A search field. Uses the `onsearch`, `incremental`, `placeholder`, `autosave`, and `results` attributes in addition to standard HTML attributes.

A submission button for a form.

A text field for specifying a phone number. Brings up a phone pad keyboard for iOS.

____Availability____: Available for iOS.

A standard text field.

An input control for specifying a time value. The user can select the hour, minute, and optionally AM or PM.

____Availability____: Available for iOS 5.0 and later.

A text field for specifying a URL. Brings up a keyboard optimized for URL entry for iOS.

____Availability____: Available for iOS.

[Next](Supported%20Meta%20Tags.md)[Previous](Supported%20Attributes.md)

