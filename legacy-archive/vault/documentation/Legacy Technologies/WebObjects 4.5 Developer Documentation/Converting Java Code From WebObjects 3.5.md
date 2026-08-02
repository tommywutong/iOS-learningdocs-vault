---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.3f.html
archived_at: '2026-07-15T08:09:41.061571Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Converting%20Projects%20from%20WebObjects%203.5%20to%204.0.md) [!](Troubleshooting%20WebObjects%204%20Template%20Parsing.md)

---

#   Converting Java Code From WebObjects 3.5

This section covers the details of converting any Java code you may have in an existing WebObjects application (see step [3](Converting%20Projects%20from%20WebObjects%203.5%20to%204.0.md#apple-gm4tsnrv)
above). In WebObjects 4, the Java APIs changed considerably. These changes are summarized here:

- 

  A two-letter prefix was added to each Java class name so that class names are unique without the package names. The Java class name is now identical to its Objective-C counterpart in almost all cases. For example, Component is now WOComponent, and WebApplication is now WOApplication.
- 

  The Java package names changed to the following:

  com.apple.yellow.eoaccess

  com.apple.yellow.eocontrol

  com.apple.yellow.foundation

  com.apple.yellow.webobjects

  Notice that the
  next.eo
  package was split into two packages:
  eoaccess
  and
  eocontrol
  .
- 

  The basic classes (for arrays, dictionaries, and data) became more like their Foundation counterparts than their Java counterparts. For example, ImmutableVector is now named NSArray and responds to
  count
  instead of
  size
  . MutableHashtable is now named NSMutableDictionary and responds to
  setObjectForKey
  instead of
  put
  .

  Note that for numbers and strings, you still use the classes
  java.lang.Number
  and
  java.lang.String
  .

  __Warning:__
  Changing to Foundation-style methods for the dictionary class introduces a subtle change. The Java Hashtable classes take the arguments in the key-value order. For example, the
  put
  method takes the key and then the value. NSDictionary takes the value and then the key. The conversion scripts change the order of the arguments for you. Unfortunately, these scripts incorrectly convert uses of
  get()
  and
  put()
  on java.util.Hashtable objects as well as on objects of other Foundation classes.
- 

  DecimalNumber is no longer available. Use
  java.math.BigDecimal
  instead.
- 

  CalendarDate is now named NSGregorianDate.
- 

  The root object is now
  com.apple.yellow.foundation.NSObject
  .
- 

  Delegate interfaces are now declared as inner interfaces of the appropriate class. For example, the DisplayGroupDelegates interface is now
  WODisplayGroup.Delegates
  .

Scripts are provided with the release to help you convert Java code to the new APIs. They are located in /System/Developer/Java/Conversion/WebObjects or, on NT, in _$NEXT_ROOT_/Developer/Java/Conversion/WebObjects
. Descriptions of these scripts and instructions for their use can be found in the ReadMe.html file, which is located in the same directory as the script files.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Converting%20Projects%20from%20WebObjects%203.5%20to%204.0.md) [!](Troubleshooting%20WebObjects%204%20Template%20Parsing.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
