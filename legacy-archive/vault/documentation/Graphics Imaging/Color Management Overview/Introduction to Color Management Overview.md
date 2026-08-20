---
title: Color Management Overview
apple_id: TP30001148
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/csintro/csintro_intro/csintro_intro.html
archived_at: '2026-07-15T07:38:07.603014Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Color-%20A%20Brief%20Overview.md)

# Introduction to Color Management Overview

This document provides a general introduction to the basics of color and color management. Read this document to learn about:

- Color perception
- Color spaces
- The values used to describe color
- Color conversion and color matching
- The role of color management systems

Color management is the process of maintaining consistent color among devices. Different imaging devices such as scanners, displays, and printers work in different color spaces, and each can have a different gamut (the range of colors a device can display). Color displays from different manufacturers all use RGB colors but may have different RGB gamuts as a result of the device type and its age. Printers and presses work in CMYK space and can vary drastically in their gamuts, especially if they use different printing technologies. Even a single printer’s gamut can vary significantly depending on the ink or type of paper in use. It’s easy to see that conversion from RGB colors on an individual display to CMYK colors on an individual printer using a specific ink and paper type can lead to unpredictable results.

This document provides the conceptual foundation developers need to understand ColorSync developer documentation. You should be familiar with the concepts in this document before you read _[ColorSync Manager Reference](https://developer.apple.com/documentation/applicationservices/colorsync_manager)_.

The information in this document is also useful for anyone who works with color and wants to understand the challenges of maintaining consistent color from input device (scanner, digital camera) to output device (monitor, printer, printing press).

This document is divided into these chapters:

- [Color: A Brief Overview](Color-%20A%20Brief%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbyfvbuqmrqguwueqsdijceorce) discusses color perception and additive and subtractive color systems.
- [Color Spaces](Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbyfvbuqmrsgiwueqsdijceorce) describes how different peripheral devices represent color and the values used to represent color.
- [Color Management Systems](Color%20Management%20Systems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbyfvbuqmrsgmwueqsdijceorce) discusses the color matching problem and how color management systems maintain consistent color among devices.

For information on ColorSync, Apple’s standards-based solution for color management, see:

- _[ColorSync Manager Reference](https://developer.apple.com/documentation/applicationservices/colorsync_manager)_, provides a complete reference for the ColorSync Manager application programming interface.

For more information on color theory and color spaces, see:

- Bruce Fraser, Fred Bunting, and Chris Murphy. _Real World Color Management_, first edition. Peachpit Press, 2003.
- Roy S. Berns. _Billmeyer and Saltzman’s Principles of Color Technology_, third edition. Wiley-Interscience, 2000.
- James D. Foley, Andries van Dam, Steven K. Feiner, and John F. Hughes. _Computer Graphics: Principles and Practice in C_, second edition. Addison-Wesley, 1995.
- Roy Hall. _Illumination and Color in Computer Generated Imagery_. New York: Springer-Verlag, 1988.
- R.W.G. Hunt. _Measuring Colour_, third edition. Fountain Pr LTD, 2001.
- Günther Wyszecki and W.S. Stiles. _Color Science: Concepts and Methods, Quantitative Data and Formulae_, second edition. John Wiley & Sons, 2000.
[Next](Color-%20A%20Brief%20Overview.md)

