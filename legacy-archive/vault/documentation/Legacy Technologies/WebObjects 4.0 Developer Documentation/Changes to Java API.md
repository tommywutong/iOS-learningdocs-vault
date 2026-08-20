---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.03.html
archived_at: '2026-07-15T07:57:58.925596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](File%20Location%20Changes-2.md)

# Changes to Java API

In Enterprise Objects Framework 3.0, the Java APIs have changed considerably. The changes to the Java APIs are summarized here:

- A two-letter prefix (EO) has been added to each Java class name. In almost all cases, the Java class name is now identical to its Objective-C counterpart.
- The Java package names have changed to the following:

com.apple.yellow.eoaccess
com.apple.yellow.eocontrol
com.apple.yellow.eointerface
com.apple.yellow.informixeoadaptor
com.apple.yellow.odbceoadaptor
com.apple.yellow.oracleeoadaptor
com.apple.yellow.sybaseeoadaptor

Note that the next.eo package has been split into two packages: eoaccess and eocontrol. Also note that Java APIs are now available for the EOInterface framework and the database-specific adaptor frameworks.

- The basic classes (for arrays, dictionaries, and data) have become more like their Foundation counterparts than their Java counterparts. For example, ImmutableVector is now named NSArray and responds to __count__ instead of __size__. MutableHashtable is now named NSMutableDictionary and responds to __setObjectForKey__ instead of __put__.

Note that for numbers and strings, you still use the classes java.lang.Number and java.lang.String.

Also note that changing to Foundation-style methods for the dictionary class introduces a subtle change. The Java Hashtable classes take the arguments in the key-value order. For example, the __put__ method takes the key and then the value. NSDictionary takes the value and then the key. The conversion scripts change the order of the arguments for you.

- DecimalNumber is no longer available. Use java.math.BigDecimal instead.
- CalendarDate is now named NSGregorianDate.
- The root object is now com.apple.yellow.foundation.NSObject.
- Delegate interfaces are now declared as inner classes (within the appropriate class). For example, EditingContextDelegates is now EOEditingContext.Delegate.

If you have existing Java code that you want to convert, see the document "[What's New in WebObjects 4.0](What%27s%20New%20in%20WebObjects%204.0.md)."

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Deprecated%20API.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
