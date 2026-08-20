---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Objective-C/XCTest.html
archived_at: '2026-07-18T02:51:43.874081Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# XCTest Changes for Objective-C

### XCTest

#### XCUICoordinate.h

Added [-[XCUICoordinate doubleTap]](https://developer.apple.com/documentation/xctest/xcuicoordinate/1615005-doubletap)Added [-[XCUICoordinate pressForDuration:]](https://developer.apple.com/documentation/xctest/xcuicoordinate/1615002-press)Added [-[XCUICoordinate pressForDuration:thenDragToCoordinate:]](https://developer.apple.com/documentation/xctest/xcuicoordinate/1615003-pressforduration)Added [-[XCUICoordinate tap]](https://developer.apple.com/documentation/xctest/xcuicoordinate/1615004-tap)Added XCUICoordinate(XCUICoordinateMouseEvents)Added XCUICoordinate(XCUICoordinateTouchBarEvents)

#### XCUIElement.h

Removed XCUIElement(XCUIElementEventSynthesis)Added [-[XCUIElement doubleTap]](https://developer.apple.com/documentation/xctest/xcuielement/1618673-doubletap)Added [-[XCUIElement pressForDuration:]](https://developer.apple.com/documentation/xctest/xcuielement/1618663-press)Added [-[XCUIElement pressForDuration:thenDragToElement:]](https://developer.apple.com/documentation/xctest/xcuielement/1618670-press)Added [-[XCUIElement tap]](https://developer.apple.com/documentation/xctest/xcuielement/1618666-tap)Added XCUIElement(XCUIElementKeyboardEvents)Added XCUIElement(XCUIElementMouseEvents)Added XCUIElement(XCUIElementTouchBarEvents)

#### XCUIElementTypeQueryProvider.h

Added [XCUIElementTypeQueryProvider.touchBars](https://developer.apple.com/documentation/xctest/xcuielementtypequeryprovider/2673960-touchbars)

#### XCUIElementTypes.h

Added [XCUIElementTypeTouchBar](https://developer.apple.com/documentation/xctest/xcuielement/elementtype/touchbar)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
