---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOGenericElement.html
archived_at: '2026-07-15T08:14:39.017543Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOGenericElement

## Element Description

WOGenericElement supports development of reusable components
that closely model the behavior of common HTML elements. For example,
you can use WOGenericElement to implement your own image (IMG) element
as a reusable component. WOGenericElement has attributes that support
the `takeValues...` and `invokeAction...` phases
of the component-action request/response loop.

## Synopsis

WOGenericElement { elementName = _aConstantString_;
[omitTags=_aBoolean_;] [elementID=_identifier_;] [otherTagString=_aString_;]
[formValue=_singleValue_;] [formValues=_arrayOfValues_;] [invokeAction=_aMethod_;]...
};

## Bindings

**elementName**
: Name of the HTML tag. This name (for example "`HR`")
will be used to generate the element's tag (`<HR>`). __elementName__ can
either be a constant ora variable, such as a key path. You can also set
the value of this attribute to `nil` or `null`,
which effectively shuts off this element (that is, WebObjects doesn't
generate HTML tags for this element). Alternatively, you can use
the __omitTags__ attribute to achieve the same
effect.

**omitTags**
: Specifies whether the element's tag should be displayed.
The default value is `false` (or `NO`). If __omitTags__ is `true` (or `YES`),
the entire element is not rendered.

**elementID**
: Allows access to the element's element ID. This is
a read-only attribute.

**otherTagString**
: Enables any string to be part of the opening tag. This
permits standalone attributes such as "`checked`"
or "`selected`"
to be part of a tag.

**formValue
formValues**
: Enables implementation of input-type elements (for example, [WOTextField](WOTextField.md#apple-infecqsgjjcem)). Bind these attributes
to a variable that can contain the component's input value. During
the __takeValues...__ phase, if the element
ID of the current generic element matches an element ID of a form
value in the request, the form value is pushed into the component
using this attribute. The __formValue__ attribute
corresponds to WORequest's __formValueForKey:__ while
the __formValues__ attribute corresponds to WORequest's `formValuesForKey:` method;
in other words, `formValue` pushes
a single attribute while `formValues` pushes
an array of attributes.

**invokeAction**
: Enables implementation of action elements (for example, [WOHyperlink](WOHyperlink.md#apple-ineeor2jivfei)). During the __invokeAction...__ phase,
if the element ID of the current generic element matches the sender ID
of the URL, the method bound to this attribute is evaluated. Just
as with any action method, it must return an object that conforms
to the WOActionResults protocol, such as WOComponent or WOResponse.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
