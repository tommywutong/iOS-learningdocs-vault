---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOTextAssociation.html
archived_at: '2026-07-15T08:13:55.417660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOTextAssociation

> **__Inherits from:__**
> : [EOValueAssociation](EOValueAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvmylmovsuc43tn5rwsylunfxw4) : [EOWidgetAssociation](EOWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

In a Java Client application (using Swing), an EOTextAssociation object displays a plain text attribute in an EOTextField, EOTextArea, or EOFormCell by binding the text object to a string. Text is written back to the object as a String.

In a Cocoa application, an EOTextAssociation object displays a plain or rich text attribute in an NSText object by binding the text object to a string or NSData attribute. It determines the kind of text received from an object by examining the beginning for signature codes specific to RTF and RTFD. When writing text back to the object, the association examines the configuration of the NSText object to determine the type to use according to the following table:

|  |  |  |
| --- | --- | --- |
| __Multiple Fonts__ | __Allows Graphics__ | __Type Written to Object__ |
| NO | NO | NSString text |
| YES | NO | NSData containing RTF |
| YES | YES | NSData containing RTFD |

|  |
| --- |
| __Usable With__ |
| com.webobjects.eointerface.swing: EOTextField, EOTextArea, EOFormCell |
| com.webobjects.eointerface.cocoa: NSText, NSTextView |

|  |
| --- |
| __Aspects__ |
| `value` | A text attribute of the selected object. |
| `URL` | Description forthcoming. |
| `enabled` | Description forthcoming. |
| `textColor` | Description forthcoming. |
| `backgroundColor` | Description forthcoming. |
| `bold` | Description forthcoming. |
| `italic` | Description forthcoming. |

|  |
| --- |
| __Object Keys Taken__ |
| `delegate` | An EOTextAssociation accepts delegate messages related to the editing and validation of text; see the NSText and NSTextView class specifications for more information. |

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbonzw6y3jmf2gs33of5sgs43qn5zwk)
>
> :
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOTextAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbonzw6y3jmf2gs33of5cu6vdfpb2ec43tn5rwsylunfxw4): [defaultDisabledBackgroundColor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vdfpb2ec43tn5rwsylunfxw4l3emvtgc5lmorcgs43bmjwgkzccmfrwwz3sn52w4zcdn5wg64q): [defaultEnabledBackgroundColor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vdfpb2ec43tn5rwsylunfxw4l3emvtgc5lmorcw4ylcnrswiqtbmnvwo4tpovxgiq3pnrxxe): [setDefaultBackgroundColors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vdfpb2ec43tn5rwsylunfxw4l3tmv2eizlgmf2wy5ccmfrwwz3sn52w4zcdn5wg64tt): [displayValueFromURL](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbonzw6y3jmf2gs33of5sgs43qnrqxsvtbnr2wkrtsn5wvkusm): [setUsesDefaultBackgroundColors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbonzw6y3jmf2gs33of5zwk5cvonsxgrdfmzqxk3duijqwg23hojxxk3teinxwy33som): [usesDefaultBackgroundColors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cbonzw6y3jmf2gs33of52xgzltirswmylvnr2eeyldnntxe33vnzseg33mn5zhg)

## Constructors

---

### EOTextAssociation

`public EOTextAssociation(Object aDisplayObject)`

Creates a new EOTextAssociation to monitor and update the value in _aDisplayObject_, which is typically Cocoa NSActionCell or, in Swing applications, an EOFormCell.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Static Methods

---

### defaultDisabledBackgroundColor

`public static Object defaultDisabledBackgroundColor()`

Description forthcoming.

---

### defaultEnabledBackgroundColor

`public static Object defaultEnabledBackgroundColor()`

Description forthcoming.

---

### setDefaultBackgroundColors

`public static void setDefaultBackgroundColors( Object enabledColor, Object disabledColor)`

Description forthcoming.

---

## Instance Methods

---

### displayValueFromURL

`protected Object displayValueFromURL(String URLString)`

Description forthcoming.

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

---

### setUsesDefaultBackgroundColors

`public void setUsesDefaultBackgroundColors(boolean flag)`

Description forthcoming.

---

### usesDefaultBackgroundColors

`public boolean usesDefaultBackgroundColors()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
