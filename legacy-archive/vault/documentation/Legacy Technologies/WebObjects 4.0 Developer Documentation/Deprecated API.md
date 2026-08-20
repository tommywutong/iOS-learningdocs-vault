---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.04.html
archived_at: '2026-07-15T07:58:00.614484Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Changes%20to%20Java%20API.md)

# Deprecated API

Enterprise Objects Framework 3.0 introduces API improvements that require deprecating existing API. You'll still be able to use deprecated API, but you'll receive a warning at runtime. The following tables summarize the deprecated API.

|  Fetch Specification Hint Keys |  Fetch Specification Hint Keys |
|  Old API |  New API |
|  EOPrefetchingRelationshipHintKey (Objective-C)  FetchSpecification.PrefetchingRelationshipHintKey and DatabaseContext.PrefetchingRelationshipHintKey (Java) |  EOFetchSpecification's accessor methods, prefetchingRelationshipKeyPaths and setPrefetchingRelationshipKeyPaths: |
|  EOFetchLimitHintKey (Objective-C)  DatabaseContext.FetchLimitHintKey (Java) |  EOFetchSpecification's accessor methods, fetchLimit and setFetchLimit: |
|  EOPromptAfterFetchLimitHintKey (Objective-C)  DatabaseContext.PromptAfterFetchLimitHintKey (Java) |  EOFetchSpecification's accessor methods, promptsAfterFetchLimit and setPromptsAfterFetchLimit: |

```
```

|  EOClassDescription |  EOClassDescription |
|  Old API |  New API |
|  delegate and setDelegate: class (Objective-C) or static (Java) methods |  classDelegate and setClassDelegate: class (Objective-C) or static (Java) methods. |

```
```

|  EOModelGroup |  EOModelGroup |
|  Old API |  New API |
|  delegate and setDelegate: class methods (Objective-C only) |  classDelegate and setClassDelegate: class methods. Note that the corresponding Java static methods have always been named classDelegate and setClassDelegate. |

```
```

|  NSObject Additions (Objective-C) EOCustomObject (Java) |  NSObject Additions (Objective-C) EOCustomObject (Java) |
|  Old API |  New API |
|  useStoredAccessor class (Objective-C) or static (Java) method |  This method still exists, but the default is now YES or true. |
|  flushClassKeyBindings |  None. Use flushAllKeyBindings instead. |

```
```

|  EOUndoManager |  EOUndoManager |
|  Old API |  New API |
|  EOUndoManager class |  NSUndoManager in Foundation.  The EOUndoManager header file is no longer included in EOControl. If you want to continue using EOUndoManager, you'll have to include EOControl/EODeprecated.h, where it's now defined.  EOUndoManager is no longer available in Java at all. |

```
```

|  EOLoginPanel |  EOLoginPanel |
|  Old API |  New API |
|  __runPanelForAdaptor:validate:__ (Objective-C only)  There wasn't an equivalent Java class in WebObjects 3.5. |  __runPanelForAdaptor: validate: allowsCreation:__ (Objective-C)  __runPanelForAdaptor__ (Java) |

```
```

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Support%20for%20the%20OpenBase%20Lite%20Database.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
