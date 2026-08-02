---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOTextAssociation.html
archived_at: '2026-07-18T01:28:46.952941Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOTableViewAssociation-2.md)
[!](EOViewLayout-2.md)

---

# EOTextAssociation

__Inherits From:__
EOAssociation : EODelayedObserver (EOControl) : NSObject

__Conforms To:__
NSCoding (EOAssociation)
EOObserving (EODelayedObserver)
NSObject (NSObject)

__Declared in:__
EOInterface/EOTextAssociation.h

---

## Class Description

In a Yellow Box application, an EOTextAssociation object displays a plain or rich text attribute in an NSText object (Application Kit) by binding the text object to a string or NSData attribute. It determines the kind of text received from an object by examining the beginning for signature codes specific to RTF and RTFD. When writing text back to the object, the association examines the configuration of the NSText object to determine the type to use according to the following table:

| __Multiple Fonts__ | __Allows Graphics__ | __Type Written to Object__ |
| NO | NO | NSString text |
| YES | NO | NSData containing RTF |
| YES | YES | NSData containing RTFD |

```
```

In a Java Client application, an EOTextAssociation object displays a plain text attribute in an EOTextField, EOTextArea, or EOFormCell by binding the text object to a string. Text is written back to the object as an NSString.

The following tables describe the display objects an EOTextAssociation can be used with, the aspects of an EOTextAssociation, and the object keys it takes.

| __Usable With__ |
| NSText, NSTextView, NSCStringText (Application Kit) |
| EOTextField, EOTextArea, EOFormCell (Java Client) |

```
```

| __Aspects__ | __Aspects__ |
| value | A text attribute of the selected object. |
| editable (Yellow Box only) | A boolean attribute of the selected object, which determines whether the text object is editable. |
| enabled (Java Client only) | A boolean attribute of the selected object, which determines whether the text object is enabled. |

```
```

| __Object Keys Taken__ | __Object Keys Taken__ |
| delegate (Yellow Box only) | An EOTextAssociation accepts delegate messages related to the editing and validation of text; see the NSText, NSTextView, and NSCStringText class specifications for more information. |

```
```


---

###

---

[!](EOTableViewAssociation-2.md)
[!](EOViewLayout-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
