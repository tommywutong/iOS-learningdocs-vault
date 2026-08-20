---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOGenericContainer.html
archived_at: '2026-07-15T08:00:39.266443Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOGenericContainer

---

# Synopsis

WOGenericContainer { elementName = _aConstantString_; [omitTags=YES|NO;] [elementID=_identifier_;] [otherTagString=_aString_;] [formValue=_singleValue_;] [formValues=_arrayOfValues_;] [invokeAction=_aMethod_;]... };

---

# Description

WOGenericContainer supports development of reusable components that closely model the behavior of common HTML elements. For example, along with WOComponentContent, you can use WOGenericContainer to implement your own hyperlink element as a reusable component. WOGenericContainer has attributes that support the takeValues... and invokeAction... phases of the component-action request/response loop.

---

# Bindings

**---

### elementName

Name of the HTML tag. This name (for example "TEXTAREA") will be used to generate the container's opening and closing tags (<TEXTAREA>...</TEXTAREA>). elementName can either be a constant or a variable, such as a key path. You can also set the value of this attribute to nil or null, which effectively shuts off this element (that is, WebObjects doesn't generate HTML tags for this element). Alternatively, you can use the omitTags attribute to achieve the same effect.

**---

### omitTags

A boolean specifying whether the element's tags should be displayed. This attribute is useful for defining an element that conditionally wraps HTML in a container tag. The default value is NO. If the flag is YES, the contents of the tag are rendered but not the tags themselves. Using omitTags for a container makes the container itself optional.

**---

### elementID

Allows programmatic access to the element's element ID. This is a read-only attribute.

**---

### otherTagString

Enables any string to be part of the opening tag. This permits standalone attributes such as "checked" or "selected" to be part of a tag.

**---

### formValue formValues

Enables implementation of input-type elements (for example, WOTextField). Bind these attributes to a variable that can contain the component's input value. During the takeValues... phase, if the element ID of the current generic container matches an element ID of a form value in the request, the form value is pushed into the component using this attribute. The formValue attribute corresponds to WORequest's formValueForKey: while the formValues atribute corresponds to WORequest's formValuesForKey: method; in other words, formValue pushes a single attribute while formValues pushes an array of attributes.

**---

### invokeAction

Enables implementation of action elements (for example, WOHyperlink). During the invokeAction... phase, if the element ID of the current generic container matches the sender ID of the URL, the method bound to this attribute is evaluated. Just as with any action method, it must return an object that conforms to the WOActionResults protocol, such as WOComponent or WOResponse.************

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
