---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/StdlibUnittest.html
archived_at: '2026-07-18T02:52:41.215080Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# StdlibUnittest Changes

## StdlibUnittest (Removed)

Removed AssertionResult [struct]Removed AssertionResult.descriptionRemoved AssertionResult.getLogicValue() -> BoolRemoved AssertionResult.init(isPass: Bool)Removed AssertionResult.withDescription(String) -> StdlibUnittest.AssertionResultRemoved SourceLoc [struct]Removed SourceLoc.init(_: String, _: UWord, comment: String?)Removed SourceLoc.commentRemoved SourceLoc.fileRemoved SourceLoc.lineRemoved SourceLoc.withCurrentLoc(String, line: UWord) -> StdlibUnittest.SourceLocStackRemoved SourceLocStack [struct]Removed SourceLocStack.init()Removed SourceLocStack.init(_: StdlibUnittest.SourceLoc)Removed SourceLocStack.init(_locs: [StdlibUnittest.SourceLoc])Removed SourceLocStack.isEmptyRemoved SourceLocStack.locsRemoved SourceLocStack.with(StdlibUnittest.SourceLoc) -> StdlibUnittest.SourceLocStackRemoved SourceLocStack.withCurrentLoc(String, line: UWord) -> StdlibUnittest.SourceLocStackRemoved TestCase [struct]Removed TestCase.init(_: String)Removed TestCase.nameRemoved TestCase.run()Removed TestCase.test(String, testFunction:() -> ())Removed asHex([UInt32]) -> StringRemoved asHex([UInt8]) -> StringRemoved assertionFailure() -> StdlibUnittest.AssertionResultRemoved assertionSuccess() -> StdlibUnittest.AssertionResultRemoved checkCollection([Element], C, StdlibUnittest.SourceLocStack)Removed checkGenerator([Element], G, StdlibUnittest.SourceLocStack)Removed checkSequence([Element], S, StdlibUnittest.SourceLocStack)Removed checkSliceableWithBidirectionalIndex([Element], S, StdlibUnittest.SourceLocStack)Removed expectEmpty(T?, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectEqual(ContiguousArray<T>, ContiguousArray<T>, StdlibUnittest.SourceLocStack?,() -> String, String, UWord)Removed expectEqual(ContiguousArray<T>, ContiguousArray<T>, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectEqual(Slice<T>, Slice<T>, StdlibUnittest.SourceLocStack?,() -> String, String, UWord)Removed expectEqual(Slice<T>, Slice<T>, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectEqual(T, T, StdlibUnittest.SourceLocStack?,() -> String, String, UWord)Removed expectEqual(T, T, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectEqual([T: U],[T: U], StdlibUnittest.SourceLocStack?,() -> String, String, UWord)Removed expectEqual([T: U],[T: U], StdlibUnittest.SourceLocStack?, String, UWord)Removed expectEqual([T],[T], StdlibUnittest.SourceLocStack?,() -> String, String, UWord)Removed expectEqual([T],[T], StdlibUnittest.SourceLocStack?, String, UWord)Removed expectFalse(Bool, String, UWord)Removed expectFalse(StdlibUnittest.AssertionResult, String, UWord)Removed expectGE(Int, Int, String, UWord)Removed expectLE(Int, Int, String, UWord)Removed expectNotEmpty(T?, String, UWord)Removed expectNotEqual(T, T, String, UWord)Removed expectOptionalEqual(T, T?, String, UWord)Removed expectTrue(Bool, StdlibUnittest.SourceLocStack?, String, UWord)Removed expectTrue(StdlibUnittest.AssertionResult, StdlibUnittest.SourceLocStack?, String, UWord)

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
