---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOFileUpload.html
archived_at: '2026-07-15T08:00:36.482160Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


![Developer Documentation](attachments/images/wothinban.gif)

__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOFileUpload

---

# Synopsis

WOFileUpload { filePath=_aPath_; data=_uploadData_ };

---

# Description

A WOFileUpload element displays a form element in which a client browser can specify a file to be uploaded to the server. It corresponds to the HTML: __<INPUT type=file>__.

__Note:__  WOFileUpload elements inside of a WOForm require that the WOForm have the attribute's encoding type set as follows:

```
enctype = "multipart/form-data"
```

For further information on the file upload specification, see RFC1867: __http://www.w3.org/RT/REC-html32.html#rfc1867__.

If you want to process a file upload in a direct action, use WORequest's __formValueForKey:__ method to get the contents of the file that has been uploaded. This method previously returned an NSString. It is now declared as follows:

```objc
- (id)formValueForKey:(NSString *)aKey
```

or, in Java,

```
public java.lang.Object formValueForKey(java.lang.String aKey)
```

---

# Bindings

**---

### filePath

The full file path and name of the file uploaded is sent by the browser and returned as a string to the variable or method bound to this attribute.

**---

### data

The file that is uploaded will be returned as an NSData object to the variable or method bound to this attribute.

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._****
