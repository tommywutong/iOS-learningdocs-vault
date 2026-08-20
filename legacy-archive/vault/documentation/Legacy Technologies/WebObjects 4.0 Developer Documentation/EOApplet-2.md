---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOApplet.html
archived_at: '2026-07-18T01:28:45.123423Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOActionInsertionAssociation-2.md)
[!](EOApplication-2.md)

---

# EOApplet

__Inherits From:__
com.sun.java.swing.JApplet

__Inherits From:__
com.apple.client.eointerface

---

## Class Description

EOApplet is the default Applet class embedded in WebObjects pages containing a WOJavaClientApplet WOElement. EOApplet is actually something of a shell, as all application initialization logic actually resides in EOApplication. For maximum flexibility, any application specifics should be implemented in EOApplication's [`finishInitialization`](EOApplication.md#apple-gq2temy) rather than EOApplet's [`init`](#apple-gm2teoa).

EOApplet is for use in Java Client applications only; there isn't an equivalent class for Yellow Box.

---

## Instance Methods

---

### init

public void `init`()

Instantiates an EODistributionChannel before passing it to EOApplication's [`application`](EOApplication.md#apple-gq2dmma) method, using the receiver's `contentPane` as _container_ and _className_,_languages_ and _controllerClassName_ retrieved via Applet's `getParameter`.

---

[!](EOActionInsertionAssociation-2.md)
[!](EOApplication-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
