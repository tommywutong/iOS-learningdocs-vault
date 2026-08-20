---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOApplet.html
archived_at: '2026-07-15T08:00:32.976338Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOApplet

---

# Synopsis

WOApplet { code=_javaClassName_; width=_aWidth_; height=_aHeight_; [associationClass=_className_;] [codeBase=_aPath_;] [archive=_jarFile1_[, _jarFile2_];] [archiveNames=_jarFile1_[, _jarFile2_];] [object=_serializedApplet_;] [hspace= _aSize_;] [vspace=_aSize_;] [align=_aString_]... };

---

# Description

WOApplet is a dynamic element that generates HTML to specify a Java applet. The applet's parameters are passed by one or more WOParam elements.

---

# Bindings

**---

### code

Name of the Java class.

**---

### width

Width, in pixels, of the area to allocate for the applet.

**---

### height

Height, in pixels, of the area to allocate for the applet.

**---

### associationClass

Name of Java subclass of next.wo.client.Association that aids in communication between client applet and the server.

**---

### codeBase

Directory that contains the applet code. If this attribute is omitted, the applet code is assumed to be in the same directory as the template HTML file.

**---

### archive

Comma-separated list of URLs for jar archive files containing classes and other resources that will be preloaded. (Note: Currently, most browser do not support a comma-separated list, so only a single archive file may be used.) Use this attribute for archive files that you have generated outside of a WebObjects application or framework. The value for this attribute is appended to the archiveNames attribute value.

**---

### archiveNames

Comma-separated list of archive files containing classes and other resources that will be preloaded. (Note: Currently, most browser do not support a comma-separated list, so only a single archive file may be used.) Use this attribute for archive files that are built as part of a WebObjects application or framework project.

**---

### object

File containing serialized representation of the applet.

**---

### hspace

Amount of whitespace (in pixels) to the left and right of the applet.

**---

### vspace

Amount of whitespace (in pixels) at the top and bottom of the applet.

**---

### align

Alignment of the applet. Possible values are top, bottom, left, right, and middle.**********************

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
