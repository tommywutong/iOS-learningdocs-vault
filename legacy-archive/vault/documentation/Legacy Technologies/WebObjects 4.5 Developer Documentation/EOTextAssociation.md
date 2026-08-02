---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTextAssociation.html
archived_at: '2026-07-15T08:11:45.096640Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTextAssociation

> **__Inherits
> from:__**
> : [(com.apple.client.eointerface)
> EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) :
> EODelayedObserver (EOControl) :
> Object
> (com.apple.yellow.eointerface)
> EOAssociation :
> EODelayedObserver (EOControl) :
> NSObject

> **__Implements:__**
> : EOObserving (EODelayedObserver)
> : (com.apple.client.eointerface only) java.awt.event.FocusListener
> : (com.apple.client.eointerface only) NSDisposable (EOAssociation)

> **__Package:__**
> : com.apple.client.eointerface
> : com.apple.yellow.eointerface

---

## Class Description

---

In a Java Client application (using com.apple.client.eointerface),
an EOTextAssociation object displays a plain text attribute in an
EOTextField, EOTextArea, or EOFormCell by binding the text object
to a string. Text is written back to the object as a String.

In a com.apple.yellow.eointerface application, an EOTextAssociation
object displays a plain or rich text attribute in an NSText object
(Application Kit) by binding the text object to a string or NSData
attribute. It determines the kind of text received from an object
by examining the beginning for signature codes specific to RTF and
RTFD. When writing text back to the object, the association examines
the configuration of the NSText object to determine the type to
use according to the following table:

|  |  |  |
| --- | --- | --- |
| __Multiple Fonts__ | __Allows Graphics__ | __Type Written to Object__ |
| NO | NO | NSString text |
| YES | NO | NSData containing RTF |
| YES | YES | NSData containing RTFD |

The following tables describe the display objects an EOTextAssociation
can be used with, the aspects of an EOTextAssociation, and the object
keys it takes.

|  |
| --- |
| __Usable With__ |
| (com.apple.client.eointerface) EOTextField, EOTextArea, EOFormCell |
| (com.apple.yellow.eointerface) NSText, NSTextView |

|  |
| --- |
| __Aspects__ |
| value | A text attribute of the selected object. |
| (com.apple.yellow.eointerface only) editable | A boolean attribute of the selected object, which determines whether the text object is editable. |
| (com.apple.client.eointerface only) enabled | A boolean attribute of the selected object, which determines whether the text object is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| (com.apple.yellow.eointerface only) delegate | An EOTextAssociation accepts delegate messages related to the editing and validation of text; see the NSText and NSTextView class specifications for more information. |

## Constructors

---

### EOTextAssociation

`public EOTextAssociation(Object  aDisplayObject)`

Creates a new EOTextAssociation to monitor and
update the value in  _aDisplayObject,_
which is typically an Application Kit NSActionCell or, in com.apple.client.eointerface applications,
an EOFormCell.

You normally set up associations with the Interface
Builder application, in which case you don't need to create them
programmatically. However, if you do create them up programmatically,
setting them up is a multi-step process. After creating an association,
you must bind its aspects and establish its connections.

__See
Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) (EOAssociation)

---

## Instance Methods

---

### breakConnection

`public void breakConnection()`

See the [breakConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe4tfmfvug33onzswg5djn5xa) method description
in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

### endEditing

`public void endEditing()`

See the [endEditing](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk3teivsgs5djnztq) method description in
the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

### establishConnection

`public void establishConnection()`

See the [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) method
description in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

### focusGained

`public void focusGained(java.awt.event.FocusEvent  aFocusEvent)`

(com.apple.client.eointerface only) EOTextAssociation
listens to its display object's focus state changes in order to
notify the display group when the user starts editing in the display
object. `focusGained` is invoked when the
user selected the display object in order to edit its value.

---

### focusLost

`public void focusLost(java.awt.event.FocusEvent  aFocusEvent)`

(com.apple.client.eointerface only) Invoked
when a user leaves the display object, having finished editing its
value.

---

### format

`public java.text.Format format()`

(com.apple.client.eointerface only) Returns
the java.lang.text.Format used to format values bound to the receiver's `ValueAspect` for
display and editing.

---

### isUsableWithObject

`public boolean isUsableWithObject(Object  aDisplayObject)`

(com.apple.client.eointerface only) Returns `true` if  _aDisplayObject_ implements
the [EOTextAssociation.JTextComponentAccess](EOTextAssociation.JTextComponentAccess.md#apple-incugrskjjceg) interface
and if its [jTextComponent](EOTextAssociation.JTextComponentAccess.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkrsxq5cbonzw6y3jmf2gs33ofzffizlyorbw63lqn5xgk3tuifrwgzltomxwuvdfpb2eg33nobxw4zlooq) is non `null`, `false` otherwise.

__See
Also:__  [isUsableWithObject](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

### primaryAspect

`public String primaryAspect()`

(com.apple.client.eointerface only) Returns [ValueAspect](EOAssociation.md#apple-ijeugsskjfbeo).

---

### setFormat

`public void setFormat(java.text.Format  aFormat)`

(com.apple.client.eointerface only) Sets the
java.lang.text.Format object to use in formatting values bound to
the receiver's ValueAspect for display and editing.

---

### subjectChanged

`public void subjectChanged()`

See the [subjectChanged](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq) method description
in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
