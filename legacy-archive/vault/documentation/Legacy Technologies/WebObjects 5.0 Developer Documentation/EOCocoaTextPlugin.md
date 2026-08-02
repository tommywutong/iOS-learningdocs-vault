---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.cocoa/Classes/EOCocoaTextPlugin.html
archived_at: '2026-07-15T08:13:54.113522Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.cocoa/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOCocoaTextPlugin

> **__Inherits from:__**
> : [EOCocoaSimpleTextPlugin](EOCocoaSimpleTextPlugin.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33dn5qvg2lnobwgkvdfpb2fa3dvm5uw4) : [EOTextAssociation.TextPlugin (EOInterface)](EOTextAssociation.TextPlugin.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvizlyoraxg43pmnuwc5djn5xc4vdfpb2fa3dvm5uw4) : [EOValueAssociation.ValuePlugin (EOInterface)](EOValueAssociation.ValuePlugin.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvmylmovsuc43tn5rwsylunfxw4lswmfwhkzkqnr2wo2lo) : EOWidgetAssociation.WidgetPlugin (EOInterface) : Object

> **__Implements:__**
> : NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.cocoa

---

## Class Description

---

In a Cocoa application, an EOCocoaTextPlugin object displays a plain or rich text attribute in an NSText object (com.apple.cocoa.application.NSText) by binding the text object to a string or NSData attribute. It determines the kind of text received from an object by examining the beginning for signature codes specific to RTF and RTFD. When writing text back to the object, the association examines the configuration of the NSText object to determine the type to use according to the following table:

|  |  |  |
| --- | --- | --- |
| __Multiple Fonts__ | __Allows Graphics__ | __Type Written to Object__ |
| NO | NO | NSString text |
| YES | NO | NSData containing RTF |
| YES | YES | NSData containing RTFD |

|  |
| --- |
| __Usable With__ |
| NSText, NSTextView. |

|  |
| --- |
| __Aspects__ |
| `value` | A text attribute of the selected object. |
| `editable` | A boolean attribute of the selected object, which determines whether the text object is editable. |
| `enabled` | A boolean attribute of the selected object, which determines whether the text object is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| `delegate` | An EOTextAssociation accepts delegate messages related to the editing and validation of text; see the NSText and NSTextView class specifications for more information. |

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof5sgs43qn5zwk)
>
> :

## Method Types

---

> **All methods**
>
> : [EOCocoaTextPlugin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof5cu6q3pmnxwcvdfpb2fa3dvm5uw4): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof5rhezlbnnbw63tomvrxi2lpny): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof5sxg5dbmjwgs43iinxw43tfmn2gs33o): [setColors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof5zwk5cdn5wg64tt): [setFontProperties](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof5zwk5cgn5xhiudsn5ygk4tunfsxg): [setValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof5zwk5cwmfwhkzi): [value](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrsxq5cqnr2wo2lof53gc3dvmu)

## Constructors

---

### EOCocoaTextPlugin

`public EOCocoaTextPlugin( com.webobjects.eointerface.EOWidgetAssociation anEOWidgetAssociation, Object widget)`

Creates a new EOCocoaTextPlugin to monitor and update the value in _aDisplayObject_, which is typically aCocoa NSActionCell.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### breakConnection

`public void breakConnection()`

See the breakConnection method description in the superclass EOAssociation.

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.Description forthcoming.

---

### establishConnection

`public void establishConnection()`

See the establishConnection method description in the superclass (EOAssociation).

---

### setColors

`public void setColors( Object textColor, Object backgroundColor)`

Description forthcoming.

---

### setFontProperties

`public void setFontProperties( int boldState, int italicState)`

Description forthcoming.

---

### setValue

`public void setValue( Object value, boolean editable)`

Description forthcoming.

---

### value

`public Object value()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.cocoa/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
