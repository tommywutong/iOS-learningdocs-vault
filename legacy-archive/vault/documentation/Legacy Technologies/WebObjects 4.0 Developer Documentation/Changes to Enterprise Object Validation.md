---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.013.html
archived_at: '2026-07-15T07:57:57.134017Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Changes%20to%20Key-Value%20Coding.md)

# Changes to Enterprise Object Validation

Enterprise Objects Framework 3.0 makes slight changes to validation. First, it adds new validation API, summarized in the following tables.

|  EOEnterpriseObject Informal Protocol (Objective-C) or Interface (Java) |  EOEnterpriseObject Informal Protocol (Objective-C) or Interface (Java) |
|  validateTakeValue:forKeyPath: (Objective-C)  validateTakeValue (Java) |  Validates (and coerces) the provided value and assigns it to destination of the provided key path if the value is different from the current value. |

```
```

|  New Exception |  New Exception |
|  EOUnknownKeyException |  The default implementation of valueForKey: and takeValue:forKey: (takeValueForKey in Java) raise or throw this exception when they are invoked with a key that doesn't correlate with a method or instance variable in the receiver. The userInfo dictionary is augmented with the target object (EOTargetObjectUserInfoKey) and the unknown key (EOUnknownUserInfoKey). |

```
```


Second, the Java validation methods have changed. Where their Objective-C counterparts (and their release 2.2 equivalents) return an exception, the 3.0 methods throw the (previously returned) exception. For more information, see the interface specification for EOValidation.

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Changes%20to%20the%20Interface%20Layer.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
