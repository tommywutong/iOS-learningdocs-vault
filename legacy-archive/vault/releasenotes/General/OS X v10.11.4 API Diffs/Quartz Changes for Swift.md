---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/Quartz.html
archived_at: '2026-07-18T02:53:53.697671Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# Quartz Changes for Swift

### Quartz

Modified [QCCompositionPickerView](https://developer.apple.com/documentation/quartz/qccompositionpickerview)

|  | Declaration |
| --- | --- |
| From | ``` class QCCompositionPickerView : NSView {     func setCompositionsFromRepositoryWithProtocol(_ `protocol`: String!, andAttributes attributes: [NSObject : AnyObject]!)     func compositions() -> [AnyObject]!     func setDelegate(_ delegate: AnyObject!)     func delegate() -> AnyObject!     func setShowsCompositionNames(_ flag: Bool)     func showsCompositionNames() -> Bool     func setAllowsEmptySelection(_ flag: Bool)     func allowsEmptySelection() -> Bool     func setCompositionAspectRatio(_ ratio: NSSize)     func compositionAspectRatio() -> NSSize     func setDefaultValue(_ value: AnyObject!, forInputKey key: String!)     func resetDefaultInputValues()     func setSelectedComposition(_ composition: QCComposition!)     func selectedComposition() -> QCComposition!     func startAnimation(_ sender: AnyObject!)     func stopAnimation(_ sender: AnyObject!)     func isAnimating() -> Bool     func setMaxAnimationFrameRate(_ maxFPS: Float)     func maxAnimationFrameRate() -> Float     func setBackgroundColor(_ color: NSColor!)     func backgroundColor() -> NSColor!     func setDrawsBackground(_ flag: Bool)     func drawsBackground() -> Bool     func numberOfColumns() -> Int     func setNumberOfColumns(_ columns: Int)     func numberOfRows() -> Int     func setNumberOfRows(_ rows: Int) } ``` |
| To | ``` class QCCompositionPickerView : NSView {     func setCompositionsFromRepositoryWithProtocol(_ protocol: String!, andAttributes attributes: [NSObject : AnyObject]!)     func compositions() -> [AnyObject]!     func setDelegate(_ delegate: AnyObject!)     func delegate() -> AnyObject!     func setShowsCompositionNames(_ flag: Bool)     func showsCompositionNames() -> Bool     func setAllowsEmptySelection(_ flag: Bool)     func allowsEmptySelection() -> Bool     func setCompositionAspectRatio(_ ratio: NSSize)     func compositionAspectRatio() -> NSSize     func setDefaultValue(_ value: AnyObject!, forInputKey key: String!)     func resetDefaultInputValues()     func setSelectedComposition(_ composition: QCComposition!)     func selectedComposition() -> QCComposition!     func startAnimation(_ sender: AnyObject!)     func stopAnimation(_ sender: AnyObject!)     func isAnimating() -> Bool     func setMaxAnimationFrameRate(_ maxFPS: Float)     func maxAnimationFrameRate() -> Float     func setBackgroundColor(_ color: NSColor!)     func backgroundColor() -> NSColor!     func setDrawsBackground(_ flag: Bool)     func drawsBackground() -> Bool     func numberOfColumns() -> Int     func setNumberOfColumns(_ columns: Int)     func numberOfRows() -> Int     func setNumberOfRows(_ rows: Int) } ``` |

Modified [QCCompositionPickerView.setCompositionsFromRepositoryWithProtocol(_: String!, andAttributes: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/quartz/qccompositionpickerview/1447335-setcompositionsfromrepositorywit)

|  | Declaration |
| --- | --- |
| From | ``` func setCompositionsFromRepositoryWithProtocol(_ `protocol`: String!, andAttributes attributes: [NSObject : AnyObject]!) ``` |
| To | ``` func setCompositionsFromRepositoryWithProtocol(_ protocol: String!, andAttributes attributes: [NSObject : AnyObject]!) ``` |

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
