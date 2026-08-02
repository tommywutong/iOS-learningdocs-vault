---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WConfirmPage.html
archived_at: '2026-07-15T08:12:43.150787Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WConfirmPage__

__Package__:
com.webobjects.directtoweb

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- com.webobjects.generation.directtoweb.DTWGeneration
- [ConfirmPageInterface](ConfirmPageInterface.md)

__Subclasses__:

- [BASConfirmPage](BASConfirmPage.md)
- [NEUConfirmPage](NEUConfirmPage.md)
- [WOLConfirmPage](WOLConfirmPage.md)

---

__Class Description__

---

This class provides the behavior for the confirm page Direct to Web templates, specifically BASConfirmPage, NEUConfirmPage, and WOLConfirmPage. The classes for these pages inherit directly from D2WConfirmPage and define no additional methods or variables.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from a confirm page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WConfirmPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss6rbsk5bw63tgnfzg2udbm5ss6rbsk5bw63tgnfzg2udbm5ss6kbj)

---

Actions

- [cancelAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss6y3bnzrwk3cbmn2gs33of5lu6q3pnvyg63tfnz2c6kbj)
- [confirmAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss6y3pnztgs4tnifrxi2lpnyxvot2dn5wxa33omvxhilzife)

Managing the Message

- [message](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss63lfonzwcz3ff5jxi4tjnzts6kbj)
- [setMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss643forgwk43tmftwkl3wn5uwilzikn2he2lom4uq)

Managing the Next Page Parameters

- [setCancelDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss643forbwc3tdmvweizlmmvtwc5dff53g62lef4ue4zlyorigcz3firswyzlhmf2gkki)
- [setConfirmDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss643forbw63tgnfzg2rdfnrswoylumuxxm33jmqxsqttfpb2faylhmvcgk3dfm5qxizjj)

Private Methods

- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss64tfobwgcy3fnvsw45cbonzw6y3jmf2gs33oizxxeqltonxwg2lboruw63rpk5huc43tn5rwsylunfxw4lzik5huc43tn5rwsylunfxw4lctorzgs3thfrcfiv2umvwxa3dborssyv2pinxw45dfpb2cs)

---

__Constructors__

---

__D2WConfirmPage__

public D2WConfirmPage()

Standard Java no-argument constructor.

---

__Methods__

__cancelAction__

public WOComponent cancelAction()

This action method is invoked when the user clicks Cancel. If you need this method to execute custom code, use the cancel delegate.

__See Also:__[setCancelDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss643forbwc3tdmvweizlmmvtwc5dff53g62lef4ue4zlyorigcz3firswyzlhmf2gkki)

---

__confirmAction__

public WOComponent confirmAction()

This action method executes when the user clicks Confirm. To specify the confirm behavior, use the confirm delegate.

__See Also:__[setConfirmDelegate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5bw63tgnfzg2udbm5ss643forbw63tgnfzg2rdfnrswoylumuxxm33jmqxsqttfpb2faylhmvcgk3dfm5qxizjj)

---

__message__

public String message()

Returns the message displayed by the confirm page.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setCancelDelegate__

public void setCancelDelegate(NextPageDelegate cancelDelegate)

Sets the receiver's cancel delegate to `cancelDelegate`. When the user clicks No in the confirm page, Direct to Web invokes the `nextPage` method on the cancel delegate.

---

__setConfirmDelegate__

public void setConfirmDelegate(NextPageDelegate confirmDelegate)

Sets the receiver's cancel delegate to `cancelDelegate`. When the user clicks Yes in the confirm page, Direct to Web invokes the `nextPage` method on the confirm delegate.

---

__setMessage__

public void setMessage(String message)

Sets the message displayed by the confirm page.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
