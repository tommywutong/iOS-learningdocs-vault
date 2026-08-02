---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.03.html
archived_at: '2026-07-15T07:58:39.637759Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Converting%20an%20Existing%20WebObjects%20Application.md)

## Converting Java Code

This section covers the details of converting any Java code you may have in an existing WebObjects application (see step [2](Converting%20an%20Existing%20WebObjects%20Application.md#apple-giydsnzx) of "[Converting an Existing WebObjects Application](Converting%20an%20Existing%20WebObjects%20Application.md#apple-giydsnzt)," above). In WebObjects 4.0, the Java APIs changed considerably. These changes are summarized here:

- A two-letter prefix has been added to each Java class name so that class names are unique without the package names. The Java class name is now identical to its Objective-C counterpart in almost all cases. For example, Component is now WOComponent, and WebApplication is now WOApplication.
- The Java package names have changed to the following:

```
com.apple.yellow.eoaccess
com.apple.yellow.eocontrol
com.apple.yellow.foundation
com.apple.yellow.webobjects
```


Notice that the next.eo package has been split into two packages: eoaccess and eocontrol.

- The basic classes (for arrays, dictionaries, and data) have become more like their Foundation counterparts than their Java counterparts. For example, ImmutableVector is now named NSArray and responds to __count__ instead of __size__. MutableHashtable is now named NSMutableDictionary and responds to __setObjectForKey__ instead of __put__.

Note that for numbers and strings, you still use the classes __java.lang.Number__ and __java.lang.String__.

__Warning:__  Changing to Foundation-style methods for the dictionary class introduces a subtle change. The Java Hashtable classes take the arguments in the key-value order. For example, the __put__ method takes the key and then the value. NSDictionary takes the value and then the key. The conversion scripts change the order of the arguments for you. Unfortunately, these scripts incorrectly convert uses of __get()__ and __put()__ on java.util.Hashtable objects as well as on objects of other Foundation classes.

- DecimalNumber is no longer available. Use __java.math.BigDecimal__ instead.
- CalendarDate is now named NSGregorianDate.
- The root object is now __com.apple.yellow.foundation.NSObject__.
- Delegate interfaces are now declared as inner interfaces of the appropriate class. For example, the DisplayGroupDelegates interface is now __WODisplayGroup.Delegates__.

Scripts are provided with the release to help you convert Java code to the new APIs. They are located in __/System/Developer/Java/Conversion/WebObjects__ or, on NT, in __$(NEXT_ROOT)/Developer/Java/Conversion/WebObjects__. Descriptions of these scripts and instructions for their use can be found in the ReadMe file, which is located in the same directory as the script files.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.04.md)
