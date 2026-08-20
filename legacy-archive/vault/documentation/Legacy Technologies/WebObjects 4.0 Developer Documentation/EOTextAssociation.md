---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOTextAssociation.html
archived_at: '2026-07-18T01:28:44.371152Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOTableViewAssociation.md)
[!](EOViewLayout.md)

---

# EOTextAssociation

__Inherits From:__
EOAssociation : .EODelayedObserver (EOControl) : Object (Java Client)
EOAssociation : .EODelayedObserver (EOControl) : NSObject (Yellow Box)

EOObserving (EODelayedObserver)
java.awt.event.FocusListener (Java Client)

__Inherits From:__
com.apple.client.eointerface (Java Client)
com.apple.yellow.eointerface (Yellow Box)

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
| NSText, NSTextView (Application Kit) |
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
| delegate (Yellow Box only) | An EOTextAssociation accepts delegate messages related to the editing and validation of text; see the NSText and NSTextView class specifications for more information. |

```
```


---

## Constructors

public `EOTextAssociation`(java.lang.Object _aDisplayObject_)

Creates a new EOTextAssociation to monitor and update the value in _aDisplayObject_, which is typically an Application Kit NSActionCell or, in Java Client applications, an EOFormCell.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See also:__
[`bindAspect`](EOAssociation.md#apple-gu2tq) (EOAssociation), [`establishConnection`](EOAssociation.md#apple-gu4dq) (EOAssociation)

---

## Instance Methods

---

### focusGained

public void `focusGained`(java.awt.event.FocusEvent _aFocusEvent_)

EOTextAssociation listens to its display object's focus state changes in order to notify the display group when the user starts editing in the display object. `focusGained` is invoked when the user selected the display object in order to edit its value.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

### focusLost

public void `focusLost`(java.awt.event.FocusEvent _aFocusEvent_)

`focusLost` is invoked when the users leaves the display object, having finished editing its value.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

### format

public java.text.Format `format`()

Returns the java.lang.text.Format used to format values bound to the receiver's ValueAspect for display and editing.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

### primaryAspect

public java.lang.String `primaryAspect`()

Returns ValueAspect.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

### setFormat

public void `setFormat`(java.text.Format _aFormat_)

Sets the java.lang.text.Format object to use in formatting values bound to the receiver's ValueAspect for display and editing.

This method is available for Java Client applications only; there is no Yellow Box equivalent.

---

### 

---

[!](EOTableViewAssociation.md)
[!](EOViewLayout.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
