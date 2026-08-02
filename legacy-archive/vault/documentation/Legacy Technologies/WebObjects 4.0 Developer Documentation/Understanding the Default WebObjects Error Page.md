---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/UnderstandDefaultErrPg.html
archived_at: '2026-07-15T08:01:32.534547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Understanding the Default WebObjects Error Page

##  Synopsis

Describes the structure and layout of the default WebObjects error page.

##  Description

By default, when an error occurs in your application, WebObjects returns a page containing debugging information. This page is displayed in the Web browser and contains information that may be useful in the debugging of your application.

!

The default error page consists of the Exception Description and a hyperlink that restarts the application. The Exception Description contains information that may be useful in debugging the error. It is broken into the following areas:

######  TABLE 1.

|   Application |   The name of the application with the error. |
|   Error |   This defines the name of the exception that occurred. The exception names are defined in NSException.h. Common exceptions include NSGenericException, NSRangeException, and NSInvalidArgumentException. |
|   Description |   The description provides detailed information concerning the error. This information contains the name of the method that was executing when the error occurred, the contents of the Application Object, a human-readable short description of the cause of the error, and a stack trace at the point at which the error occurred. |
|   User Info Dictionary |   This dictionary is used to supply data to the exception handler.. For example, an application may raise an exception if the return value of a method is out of range, and store the return value in the User Info Dictionary for the exception handler to display. Not all code that raises exceptions provides a User Info Dictionary. |

The default error page is defined at $NEXT_ROOT\Library\Frameworks\ WOExtensions.framework\ Resources\WOExceptionPage.wo.

##  See Also

· Replacing the Default Error Page

##  Questions

· How do I use information from the error page to debug my application?

##  Keywords

· Error Page

· Error Handling

· Exception Handling

##  Revision History

22 July, 1998. John Malach. First Draft.
26 October, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
