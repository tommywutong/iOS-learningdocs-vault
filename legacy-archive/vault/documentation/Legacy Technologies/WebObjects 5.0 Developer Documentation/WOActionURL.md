---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOActionURL.html
archived_at: '2026-07-15T08:14:38.810932Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOActionURL

## Element Description

WOActionURL enables the creation of URLs to invoke methods
or specify pages to return. You can use this element for a variety
of purposes, but it is primarily intended to support JavaScript
within a WebObjects application.

## Synopsis

WOActionURL { action=_aMethod_ |
pageName=_aString_; | directActionName=_anActionName_; actionClass=_className_;
[fragmentIdentifier=_anchorFragment_;]
[queryDictionary=_aDict_; ?key=_value_;]...
};

## Bindings

**action**
: Action method to invoke when the URL is accessed. This
method must return a an object that conforms to the WOActionResults protocol
such as WOComponent or WOResponse.

**pageName**
: The name of a WebObjects page to display when the URL
is accessed.

**directActionName**
: The direct action method to invoke when the URL is accessed
(minus the "Action" suffix).

**actionClass**
: The name of the class in which the __directActionName__ can
be found. Defaults to "DirectAction".

**fragmentIdentifier**
: Named location to display in the destination page (that
is, an anchor in the destination page).

**queryDictionary**
: NSDictionary with keys/value pairs to be placed into
the URL's query string.

**?key**
: Adds a key/value pair to the specified __queryDictionary__ (or
replaces an existing key) by prefixing the key with a "?".
For example:

> ```
>    ?x = y;
> ```

puts the key "x" into the query dictionary with
the value of the keypath y.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
