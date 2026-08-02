---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/D2WErrorPage.html
archived_at: '2026-07-15T08:12:44.006066Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__D2WErrorPage__

__Package__:
com.webobjects.directtoweb

__Inherits from__:[D2WPage](D2WPage.md)__Implements__:

- com.webobjects.directtoweb.generation.DTWGeneration
- [ErrorPageInterface](ErrorPageInterface.md)

__Subclasses__:

- [BASErrorPage](BASErrorPage.md)
- [WOLErrorPage](WOLErrorPage.md)
- [NEUErrorPage](NEUErrorPage.md)

---

__Class Description__

---

This class provides the behavior for the error page Direct to Web templates, specifically BASErrorPage, NEUErrorPage, and WOLErrorPage. The classes for these pages inherit directly from D2WErrorPage and define no additional methods or variables.

Most of the methods in this class are accessed (via the EOKeyValueCoding interface defined in the EOControl framework) from the Direct to Web template's bindings (`.wod`) file. If you create a Direct to Web template from an error page, you can invoke the methods in this class in the same way. See the "Direct to Web" chapter of _WebObjects Tools and Techniques_ for more information about creating a Direct to Web template.

__Method Types__

---

Constructors

- [public D2WErrorPage()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5cdev2fojzg64sqmftwkl2egjluk4tsn5zfaylhmuxsqki)

---

Actions

- [cancelAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5rwc3tdmvwecy3unfxw4l2xj5bw63lqn5xgk3tuf4ucs)

Managing the Message

- [firstLineOfMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5tgs4ttorggs3tfj5te2zltonqwozjpkn2he2lom4xsqki)
- [formattedMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5tg64tnmf2hizlejvsxg43bm5ss6u3uojuw4zzpfauq)
- [message](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5wwk43tmftwkl2torzgs3thf4ucs)
- [setMessage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5zwk5cnmvzxgylhmuxxm33jmqxsqu3uojuw4zzj)

Managing the Next Page Parameters

- [hasNextPage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5ugc42omv4hiudbm5ss6ytpn5wgkylof4ucs)

Private Methods

- [replacementAssociationForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5cxe4tpojigcz3ff5zgk4dmmfrwk3lfnz2ec43tn5rwsylunfxw4rtpojaxg43pmnuwc5djn5xc6v2pifzxg33dnfqxi2lpnyxsqv2pifzxg33dnfqxi2lpnywfg5dsnfxgolcekrlvizlnobwgc5dffrlu6q3pnz2gk6dufe)

---

__Constructors__

---

__D2WErrorPage__

public D2WErrorPage()

Standard Java no-argument constructor.

---

__Methods__

__cancelAction__

public WOComponent cancelAction()

This method is invoked when the user clicks Return. You can specify the component this action displays by overriding `nextPage`. Alternatively, you can override `nextPageDelegate`; in this case, `nextPage` is ignored.

__See Also:__[nextPage](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozjpk5hug33nobxw4zlooqxsqki) ([D2WPage](D2WPage.md))
[nextPageDelegate](D2WPage.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rbsk5igcz3ff5xgk6dukbqwozkemvwgkz3borss6ttfpb2faylhmvcgk3dfm5qxizjpfauq) ([D2WPage](D2WPage.md))

---

__firstLineOfMessage__

public String firstLineOfMessage()

Returns a String containing a truncated version of the receiver's error message that fits on a single line.

---

__formattedMessage__

public String formattedMessage()

Returns a String containing a version of the error message with line breaks added so it fits on the page.

---

__hasNextPage__

public boolean hasNextPage()

Returns whether `nextPage` or `nextPageDelegate` have been set in the receiver. If either is set, the error page can navigate to another page when the user clicks Return. Otherwise, the error page displays a hyperlink that starts a new session.

---

__message__

public String message()

Returns the error message displayed by the error page.

---

__replacementAssociationForAssociation__

public WOAssociation replacementAssociationForAssociation(WOAssociation oldAssociation, String oldBinding, DTWTemplate aTemplate, WOContext aContext)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__setMessage__

public void setMessage(String message)

Sets the error message displayed by the error page.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
