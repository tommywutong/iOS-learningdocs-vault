---
title: Final Cut Pro 7 XML Interchange Format
apple_id: TP30001149
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/AboutThisDoc/AboutThisDoc.html
archived_at: '2026-07-15T05:19:00.712447Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Documents/Documents.html)

# About This Document

The Final Cut Pro XML Interchange Format provides extensive access to the contents of Final Cut Pro projects, including edits and transitions, effects, layer-compositing information, and organizational structures. Using the interchange format, you can process project content in ways that supplement the capabilities of the Final Cut Pro application itself. You can also share Final Cut Pro information with other applications or systems that support XML—including nonlinear editors, asset management systems, database systems, and broadcast servers.

The main body of this document describes version 5 of the Final Cut Pro XML Interchange Format. The appendix [Versions of XMEML and Final Cut](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/VersionsoftheInterchangeFormat/VersionsoftheInterchangeFormat.html#//apple_ref/doc/uid/TP30001149-CH293-SW1) compares versions 1, 2, 3, 4, and 5 of the interchange format.

This document assumes that you are familiar with XML conventions and with the Final Cut Pro 7 application.

This document contains the following chapters and appendixes:

- [Document Export and Import](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Documents/Documents.html#//apple_ref/doc/uid/TP30001153-TPXREF101) discusses exporting, importing, and validating interchange format documents.
- [Basics of Encoding](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Basics/Basics.html#//apple_ref/doc/uid/TP30001154-TPXREF101) reviews the key elements of the interchange format.
- [XMEML Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Topics/Topics.html#//apple_ref/doc/uid/TP30001149-CH294-SW1) provides information about selected Final Cut Pro XML topics.
- [Applications of the Interchange Format](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Applications/Applications.html#//apple_ref/doc/uid/TP30001155-BABCDEGE) illustrates some applications of the interchange format to various tasks.
- [Elements Catalog](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Elements/Elements.html#//apple_ref/doc/uid/TP30001156-TPXREF101) provides reference information about the elements of the interchange format.
- [DTD for the Interchange Format](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/DTD/DTD.html#//apple_ref/doc/uid/TP30001157-BCIHDFGD) lists the DTDs for versions 1, 2, 3, 4, and 5 of the interchange format.
- [Frame Rates](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/FrameRate/FrameRate.html#//apple_ref/doc/uid/TP30001158-BCIHDFGD) indicates the values required to specify various types of video and associated frame rates.
- [Keyframe Interpolation](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Interpolation/Interpolation.html#//apple_ref/doc/uid/TP30001159-BAJGAAJG) explains the interpolation method Final Cut Pro uses to construct Bezier curves in keyframes.
- [Apple Events and Final Cut Pro](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/AppleEvents/AppleEvents.html#//apple_ref/doc/uid/TP30001149-CH292-SW1) discusses using Apple Events to export or import interchange format documents.
- [Versions of XMEML and Final Cut](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/VersionsoftheInterchangeFormat/VersionsoftheInterchangeFormat.html#//apple_ref/doc/uid/TP30001149-CH293-SW1) provides information about various versions of XMEML and Final Cut Pro.
- [Document Revision History](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/RevisionHistory/RevisionHistory.html#//apple_ref/doc/uid/TP30000185-SW1) provides a history of changes to this document.

This document also has an index.

Here are some recommended XML resources:

- For a general introduction XML and the Final Cut Pro XML Interchange Format, see the section “Using Final Cut Pro XML and QuickTime Metadata” in the _Final Cut Pro 7 User Manual_.
- For a comprehensive reference guide to XML-related topics, see _XML In a Nutshell, Third Edition_, published by O'Reilly. ISBN 0-596-00764-7.
- For a useful resource of XML-related information, see _XML From the Inside Out_ ([http://xml.com](http://xml.com/)).
- On the Apple developer website, the document [Core Foundation XML](https://developer.apple.com/documentation/CoreFoundation/Conceptual/CFXML/index.html) describes the Core Foundation objects you can use to parse XML. (Cocoa developers please visit this [link.](https://developer.apple.com/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html))

[Next](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/FinalCutPro_XML/Documents/Documents.html)

