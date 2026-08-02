---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOInterfaceController.html
archived_at: '2026-07-15T08:13:42.893297Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOInterfaceController

> **__Inherits from:__**
> : [EODocumentController](EODocumentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhui33dovwwk3tuinxw45dsn5wgyzls): [EOEntityController](EOEntityController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuk3tunf2hsq3pnz2he33mnrsxe): [EOComponentController](EOComponentController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33nobxw4zloorbw63tuojxwy3dfoi): [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

EOInterfaceController serves as a convenient base class for logic related to the interface of client-side applications. When the WebObjectsApplication wizard in Project Builder creates a new client-side interface, it adds (to the client-side subproject) an Interface Builder nib file representing this interface and a skeletal EOInterfaceController subclass defined as the nib file's root object or "owner."

In an application constructed in conformance to the Model-View-Controller paradigm, EOInterfaceController plays the role of controller. It has four special outlets (defined in the EOEntityController superclass): its `editingContext`, its `component`, its `displayGroup`, and its `controllerDisplayGroup`, all of which you can configure using Interface Builder. The object identified by component is an AWT JComponent that functions as the view, since it is the main entry point into the user interface. Because an enterprise object must always inhabit an editing context, `editingContext` and its contents serve as the "model." The `displayGroup` is an EODisplayGroup containing the enterprise objects manipulated by the controller's user interface (which may will involve other display groups). The `controllerDisplayGroup` is a convenience instance containing nothing but the interface controller itself.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| `INTERFACECONTROLLER` | `entityController` |

## Method Types

---

> **All methods**
> : [EOInterfaceController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhizlsmzqwgzkdn5xhi4tpnrwgk4rpivhus3tumvzgmyldmvbw63tuojxwy3dfoi): [archiveName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhizlsmzqwgzkdn5xhi4tpnrwgk4rpmfzgg2djozsu4ylnmu): [collectChangesFromServer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhizlsmzqwgzkdn5xhi4tpnrwgk4rpmnxwy3dfmn2eg2dbnztwk42gojxw2u3foj3gk4q): [generateComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpjfxhizlsmzqwgzkdn5xhi4tpnrwgk4rpm5sw4zlsmf2gkq3pnvyg63tfnz2a)

## Constructors

---

### EOInterfaceController

`public EOInterfaceController()`

`public EOInterfaceController(com.webobjects.eocontrol.EOEditingContext editingContext)`

Initializes a new instance then attempts to load the nib file matching the class name. The one-argument and two-argument constructors allow you to specify the editing context used as the nib file's substitution editing context during the load.

`public EOInterfaceController( com.webobjects.eocontrol.EOEditingContext editingContext, String archiveName)`

Initializes a new instance then attempts to load the associated nib file identified by _archiveName_. The _editingContext_ argument is used as the nib file's substitution editing context during the load.

`public EOInterfaceController(EOXMLUnarchiver unarchiver)`

Initializes a new instance with the contents of the _unarchiver_ EOXMLUnarchiver.

---

## Instance Methods

---

### archiveName

`public String archiveName()`

Returns the name of the nib file that specifies the receiver's user interface. Defaults to the receiver's class name.

---

### collectChangesFromServer

`public void collectChangesFromServer()`

Updates the receiver's editing context to reflect any changes to enterprise objects pending on the server.

---

### generateComponent

`protected void generateComponent()`

Since an EOInterfaceController requires a nib file, this method is overridden to raise a NSInternalInconsistencyException.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
