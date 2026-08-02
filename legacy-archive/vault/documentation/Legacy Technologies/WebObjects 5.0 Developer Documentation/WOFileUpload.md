---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOFileUpload.html
archived_at: '2026-07-15T08:14:38.958436Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOFileUpload

## Element Description

A WOFileUpload element displays a form element in which a
client browser can specify a file to be uploaded to the server.
It corresponds to the HTML: `<INPUT type=file>`.

WOFileUpload elements inside of a WOForm require that the
WOForm have the attribute's encoding type set as follows:

> ```
> enctype = "multipart/form-data"
> ```

For further information on the file upload specification,
see RFC1867: `http://www.w3.org/RT/REC-html32.html#rfc1867`.

If you want to process a file upload in a direct action, use WORequest's __formValueForKey:__ method
to get the contents of the file that has been uploaded. This method
is declared as follows:

- (id)formValueForKey:(NSString \*)_aKey_

or, in Java,

public java.lang.Object formValueForKey(java.lang.String _aKey_)

## Synopsis

WOFileUpload { filePath=_aPath_;
data=_fileData_ };

## Bindings

**filePath**
: The full file path and name of the file uploaded is
sent by the browser and returned as a string to the variable or
method bound to this attribute.

**data**
: The file that is uploaded will be returned as an NSData object
to the variable or method bound to this attribute.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
