---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.015.html
archived_at: '2026-07-15T07:58:28.396432Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Support%20for%20Multithreaded%20Applications.md)

## Deprecated API

The following tables list methods whose use is deprecated in WebObjects 4.0 and list new methods to use in their place. If you don't allow concurrent request handling, you can continue to use the deprecated methods. You'll receive a warning at run-time. If you want to allow concurrent request handling, you must change to the new methods. Use of deprecated methods raises an exception when concurrent request handling is enabled (that is, when you override WOApplication's method __allowsConcurrentRequestHandling__ to return __YES__ or __true__.)

|  WOApplication |  |
|  Old API |  New API |
|  session |  WOComponent __session__ |
|  context |  WOComponent __context__ |
|  pageWithName: |  WOComponent __pageWithName:__  WOApplication __pageWithName:inContext:__ or __pageWithName:forRequest:__ (Objective-C)  WOApplication __pageWithName__ (Java) |
|  handleSessionCreationError |  __handleSessionCreationErrorInContext__: |
|  handleSessionRestorationError |  __handleSessionRestorationErrorInContext:__ |
|  handlePageRestorationError |  __handlePageRestorationErrorInContext:__ |
|  handleException: |  __handleException:inContext:__ (Objective-C)  handleException (Java) |
|  pathForResourceNamed:ofType: |  WOResourceManager pathForResourceNamed:inFramework:languages: (Objective-C)  WOResourceManager __pathForResourceNamed__ (Java) |
|  urlForResourceNamed:ofType: |  WOResourceManager urlForResourceNamed:inFramework:languages:request: (Objective-C)  WOResourceManager __urlForResourceNamed__ (Java) |
|  stringForKey:inTableNamed:withDefaultValue: |  WOResourceManager stringForKey:inTableNamed:withDefaultValue:languages: (Objective-C)  WOResourceManager __stringForKey__ (Java) |
|  handleRequest: |  dispatchRequest: |
|  createSession |  createSessionForRequest: |
|  restoreSession |  restoreSessionWithID:inContext: (Objective-C)  __restoreSessionWithID__ (Java) |
|  restorePageForContextID: |  WOSession restorePageForContextID: |
|  savePage: |  WOSession savePage: |
|  saveSession: |  __saveSessionForContext__: |
|  dynamicElementWithName:associations: template: |  dynamicElementWithName:associations:template:languages: (Objective-C)  __dynamicElementWithName__ (Java) |
|  isBrowserLaunchingEnabled |  __autoOpenInBrowser__ |
|  setBrowserLaunchingEnabled: |  Use the __WOAutoOpenInBrowser__ command-line option (see [Command-Line Options](NewInWO4.09.md#apple-giytemzy)) |
|  runLoop |  __mainThreadRunLoop__ |

```
```

|  WOAssociation |  |
|  Old API |  New API |
|  value |  valueInComponent: |
|  setValue: |  setValue:inComponent: (Objective-C)  __setValue__ (Java) |

```
```

|  WOContext |  |
|  Old API |  New API |
|  setDistributionEnabled: |  WOSession setDistributionEnabled: |
|  isDistributionEnabled |  WOSession isDistributionEnabled |
|  application |  WOApplication application class or static method |
|  urlSessionPrefix |  None (deprecated functionality) |
|  url |  __componentActionURL__ |

```
```

|  WORequest |  |
|  Old API |  New API |
|  applicationHost |  See NSProcessInfo or NSHost (Objective-C)  __java.net.InetAddress__ (Java) |
|  contextID |  WOContext __contextID__ |
|  pageName |  WOComponent __name__ |
|  senderID |  WOContext __senderID__ |

```
```

|  WOResourceManager |  |
|  Old API |  New API |
|  pathForResourceNamed:inFramework: |  pathForResourceNamed:inFramework:languages: (Objective-C)  __pathForResourceNamed__ (Java) |
|  urlForResourceNamed:inFramework: |  urlForResourceNamed:inFramework:languages:request: (Objective-C)  __urlForResourceNamed__ (Java) |

```
```

|  WOSession |  |
|  Old API |  New API |
|  application |  WOApplication application class or static method |

```
```

|  WOSessionStore |  |
|  Old API |  New API |
|  restoreSession |  __restoreSessionWithID:request__: (Objective-C)  __restoreSessionWithID__ (Java) |
|  saveSession: |  __saveSessionForContext:__ |
|  cookieSessionStoreWithDistributionDomain:secure: |  None. See [Cookie API](Cookie%20API.md#apple-gmydamjr) for new API that allows you to store session IDs in cookies. |

```
```

|  WOStatisticsStore |  |
|  Old API |  New API |
|  validateLogin: |  __validateLogin:forSession__: (Objective-C)  __validateLogin__ (Java) |
|  setMovingAverageSampleSize: |  __setTransactionMovingAverageSampleSize:__  __setSessionMovingAverageSampleSize:__ |
|  movingAverageSampleSize |  __transactionMovingAverageSampleSize__  __sessionMovingAverageSampleSize__ |

```
```

|  WOComponent |  |
|  Old API |  New API |
|  pathForResourceNamed:ofType: |  WOResourceManager pathForResourceNamed:inFramework:languages: (Objective-C)  WOResourceManager __pathForResourceNamed__ (Java) |
|  urlForResourceNamed:ofType: |  WOResourceManager urlForResourceNamed:inFramework:languages:request: (Objective-C)  WOResourceManager __urlForResourceNamed__ (Java) |
|  stringForKey:inTableNamed:withDefaultValue: |  WOResourceManager stringForKey:inTableNamed:withDefaultValue:languages: (Objective-C)  WOResourceManager __stringForKey__ (Java) |
|  templateWithHTMLString:declarationString: |  __templateWithHTMLString:declarationString:languages:__ (Objective-C)  __templateWithHTMLString__ (Java) |

```
```

|  WODisplayGroup |  |
|  Old API |  New API |
|  setSortOrdering |  __setSortOrderings:__ |
|  sortOrdering |  __sortOrderings__ |
|  endEditing |  None (this method had no effect in WebObjects 3.5) |
|  executeQuery |  __queryMatch__, __queryMin__, __queryMax__ |
|  inputObjectForQualifier |  __queryMatch__, __queryMin__, __queryMax__ |
|  secondObjectForQualifier |  __queryMatch__, __queryMin__, __queryMax__ |
|  setBuildsQualifierFromInput: |  __queryMatch__, __queryMin__, __queryMax__ |
|  buildsQualifierFromInput |  __queryMatch__, __queryMin__, __queryMax__ |
|  qualifierFromInputValues |  __queryMatch__, __queryMin__, __queryMax__ |
|  lastQualifierFromInputValues |  __queryMatch__, __queryMin__, __queryMax__ |
|  localKeys |  None (this method was inadvertently carried over from EODisplayGroup) |
|  setLocalKeys: |  None (this method was inadvertently carried over from EODisplayGroup) |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.016.md)
