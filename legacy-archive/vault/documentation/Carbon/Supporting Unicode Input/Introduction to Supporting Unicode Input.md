---
title: Supporting Unicode Input
apple_id: TP40000951
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-10-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Supporting_Unicode_Input/sui_intro/sui_intro.html
archived_at: '2026-07-15T05:24:41.754887Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](International%20Text%20in%20Mac%20OS%20X.md)

# Introduction to Supporting Unicode Input

This document describes how applications and input methods can use the Text Services Manager and Unicode Utilities programming interfaces to support Unicode input in Mac OS X.

The Text Services Manager is the part of the Mac OS that provides an environment for applications to use text services such as input methods. The Text Services Manager handles communication between client applications that request text services and the software modules, known as text service components, that provide them. The Text Services Manager presents two separate programming interfaces to the features it provides: one for applications and another for text service components.

Unicode Utilities allow applications and text service components (such as input methods) to perform various operations on Unicode text. You can use Unicode Utilities to control Unicode-related text behavior, such as the specification of Unicode keyboard layout.

In addition to Unicode input, most complete Unicode applications need various other services which are not be covered in this document, such as imaging Unicode and processing text. You can use Apple Type Services for Unicode Imaging (ATSUI) and Multilingual Text Engine (MLTE) for these services. In addition, Unicode input using the methods described in this document is compatible with any other service for imaging and processing Unicode text.

For information on ATSUI see _[ATSUI Programming Guide](../ATSUI%20Programming%20Guide/Introduction%20to%20ATSUI%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobu)_.

For information on MLTE see _[Handling Unicode Text Editing With MLTE](../Handling%20Unicode%20Text%20Editing%20With%20MLTE/MLTE%20Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobt)_.

[Next](International%20Text%20in%20Mac%20OS%20X.md)

