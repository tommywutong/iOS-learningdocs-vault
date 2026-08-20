---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/Concepts/EOAdaptor.html
archived_at: '2026-07-15T08:13:38.224301Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md) 

# EOAdaptor.Concepts

## Creating an EOAdaptor Subclass

Enterprise Objects Framework provides concrete adaptors for three standard relational database management systems-Informix, Oracle, and Sybase-as well as a concrete adaptor for ODBC-compliant databases. You may want to create a subclass of one of these adaptors to extend its behavior, or you may want to create a concrete EOAdaptor subclass for a different database or persistent storage system. EOAdaptor provides many default method implementations that are sufficient for concrete subclasses:

- assignExternalInfoForEntireModel
- connectionDictionary
- contexts
- delegate
- hasOpenChannels
- name

The following methods establish structure and conventions that other Enterprise Objects Framework classes depend on and should be overridden with caution:

- adaptorWithModel
- adaptorWithName
- setExpressionClassName
- setConnectionDictionary
- setDelegate

If you override __setConnectionDictionary__ or __setDelegate__, your implementations should incorporate the superclass's implementation through a message to __super__.

The remaining EOAdaptor methods must be overridden by concrete adaptor subclasses in terms of the persistent storage system with which it interacts:

- assignExternalInfoForAttribute
- assignExternalInfoForEntity
- externalTypesWithModel
- internalTypeForExternalType
- assertConnectionDictionaryIsValid
- createAdaptorContext
- fetchedValueForDataValue
- fetchedValueForDateValue
- fetchedValueForNumberValue
- fetchedValueForStringValue
- fetchedValueForValue
- isValidQualifierType

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
