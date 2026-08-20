---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOArchive.html
archived_at: '2026-07-18T01:28:45.301932Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOApplication-2.md)
[!](EOAssociation-3.md)

---

# EOArchive

__Inherits From:__
java.lang.Object

__Inherits From:__
com.apple.client.eointerface

---

## Class Description

An EOArchive is a client-side rendering of an Interface Builder archive document. By default, the EOInterfaceController for a WOJavaClientApplet manages its associated archive transparently and the developer never needs to interact directly with this class. The [`loadArchiveNamed`](#apple-gm2tcnq) method is exposed for developers who do not wish to use EOInterfaceControllers. Please note that EOArchive's implementation is intentionally opaque because it is guaranteed to change in the next release.

---

## Constructors

public `EOArchive`(Object _owner_)

Creates an EOArchive instance initialized with _owner_, the "File's Owner" for the Interface Builder archive document.

---

### loadArchiveNamed

public static boolean `loadArchiveNamed`(String _archiveName_, Object _owner,_ String _packageName_)

Loads a new instance of the EOArchive _name_, where _name_ identifies an InterfaceBuilder document (localization is driven by WOJavaClientApplet's EOLanguageKey) and _owner_ indicates the "File's Owner.""The _packageName_ argument identifies a package and is used in constructing the complete path to the archive. If _packageName_ is `null`, the package of _owner_ is used.

---

[!](EOApplication-2.md)
[!](EOAssociation-3.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
