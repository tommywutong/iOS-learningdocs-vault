---
title: 'enumerateMatches(in:options:range:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/enumeratematches(in:options:range:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/enumeratematches(in:options:range:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/enumeratematches%28in%3Aoptions%3Arange%3Ausing%3A%29.json'
content_hash: 'sha256:b8de73fc6ac2050e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# enumerateMatches(in:options:range:using:)

<sub>Instance Method</sub>

Enumerates the string allowing the Block to handle each regular expression match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateMatches(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange, using block: (NSTextCheckingResult?, NSRegularExpression.MatchingFlags, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `string` — The string.

- `options` — The matching options to report. See [MatchingOptions](matchingoptions.md) for the supported values.

- `range` — The range of the string to test.

- `block` — The Block enumerates the matches of the regular expression in the string. The block takes three arguments: - **result** — An [NSTextCheckingResult](../nstextcheckingresult.md) specifying the match. This result gives the overall matched range via its [range](../nstextcheckingresult/range.md) property, and the range of each individual capture group via its [- rangeAtIndex:](<../nstextcheckingresult/range(at_).md>) method. The range {`NSNotFound`, 0} is returned if one of the capture groups did not participate in this particular match. - **flags** — The current state of the matching progress. See [MatchingFlags](matchingflags.md) for the possible values. - **stop** — A reference to a Boolean value. The Block can set the value to [true](../../swift/true.md) to stop further processing of the array. The stop argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the Block. The Block returns void.

## Discussion

This method is the fundamental matching method for regular expressions and is suitable for overriding by subclassers. There are additional convenience methods for returning all the matches as an array, the total number of matches, the first match, and the range of the first match.

By default, the Block iterator method calls the Block precisely once for each match, with a non-`nil` `result` and the appropriate `flags`.  The client may then stop the operation by setting the contents of `stop` to [true](../../swift/true.md). The `stop` argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the Block.

If the [NSMatchingReportProgress](matchingoptions/reportprogress.md) matching option is specified, the Block will also be called periodically during long-running match operations, with `nil` result and [NSMatchingProgress](matchingflags/progress.md) matching flag set in the Block’s `flags` parameter, at which point the client may again stop the operation by setting the contents of stop to [true](../../swift/true.md).

If the [NSMatchingReportCompletion](matchingoptions/reportcompletion.md) matching option is specified, the Block object will be called once after matching is complete, with `nil` result and the [NSMatchingCompleted](matchingflags/completed.md) matching flag is set in the `flags` passed to the Block, plus any additional relevant [MatchingFlags](matchingflags.md) from among [NSMatchingHitEnd](matchingflags/hitend.md), [NSMatchingRequiredEnd](matchingflags/requiredend.md), or [NSMatchingInternalError](matchingflags/internalerror.md).

[NSMatchingProgress](matchingflags/progress.md) and [NSMatchingCompleted](matchingflags/completed.md) matching flags have no effect for methods other than this method.

The [NSMatchingHitEnd](matchingflags/hitend.md) matching flag is set in the `flags` passed to the Block if the current match operation reached the end of the search range.  The [NSMatchingRequiredEnd](matchingflags/requiredend.md) matching flag is set in the `flags` passed to the Block if the current match depended on the location of the end of the search range.

The [MatchingFlags](matchingflags.md) matching flag is set in the `flags` passed to the block if matching failed due to an internal error (such as an expression requiring exponential memory allocations) without examining the entire search range.

The [NSMatchingAnchored](matchingoptions/anchored.md), [NSMatchingWithTransparentBounds](matchingoptions/withtransparentbounds.md), and [NSMatchingWithoutAnchoringBounds](matchingoptions/withoutanchoringbounds.md) regular expression options, specified in the [options](options-swift.property.md) property specified when the regular expression instance is created, can apply to any match or replace method.

If [NSMatchingAnchored](matchingoptions/anchored.md) matching option is specified, matches are limited to those at the start of the search range.

If [NSMatchingWithTransparentBounds](matchingoptions/withtransparentbounds.md) matching option is specified, matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc.

If [NSMatchingWithoutAnchoringBounds](matchingoptions/withoutanchoringbounds.md) matching option is specified, `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string.

[NSMatchingWithTransparentBounds](matchingoptions/withtransparentbounds.md) and [NSMatchingWithoutAnchoringBounds](matchingoptions/withoutanchoringbounds.md) matching options have no effect if the search range covers the entire string.

## See Also

### Searching Strings Using Regular Expressions

- [- numberOfMatchesInString:options:range:](<numberofmatches(in_options_range_).md>) — Returns the number of matches of the regular expression within the specified range of the string.
- [- matchesInString:options:range:](<matches(in_options_range_).md>) — Returns an array containing all the matches of the regular expression in the string.
- [- firstMatchInString:options:range:](<firstmatch(in_options_range_).md>) — Returns the first match of the regular expression within the specified range of the string.
- [- rangeOfFirstMatchInString:options:range:](<rangeoffirstmatch(in_options_range_).md>) — Returns the range of the first match of the regular expression within the specified range of the string.
