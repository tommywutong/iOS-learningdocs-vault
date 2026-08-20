---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/JSValidatedField.html
archived_at: '2026-07-15T08:14:39.700566Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# JSValidatedField

## Component Description

This component is similar to a WOTextField and needs to be
placed within a WOForm. When the user clicks on one of the form's
submit buttons, the text in the field is tested according to the
following rules:

- If `inputIsRequired` is
  set to YES, the text must not be the empty string.
- If `requiredText` is
  not the empty string, the text must contain it.

If the text conforms to these rules, JSValidatedField submits
the form. Otherwise it displays a message and does not submit the
form.

## Synopsis

JSValidatedField { inputText=_aVariable_;
errorMessage=_aString_; formName=_aString_;
[fieldSize=_fieldSize_;]
[inputIsRequired="YES"|"NO";] [requiredText=_requiredText_;]
};

## Bindings

**inputText**
: The variable into which the entered data is stored.

**errorMessage**
: The message to display if the validation fails.

**formName**
: The name of the form that contains the JSValidatedField.

**fieldSize**
: Specifies the width of the text field.

**inputIsRequired**
: If YES, this field must be nonempty before JSValidate
Field allows the user to submit the form.

**requiredText**
: A string that the entered text must contain before JSValidateField
allows the user to submit the form.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
