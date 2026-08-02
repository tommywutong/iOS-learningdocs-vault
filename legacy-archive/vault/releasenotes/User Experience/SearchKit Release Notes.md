---
title: SearchKit Release Notes
apple_id: TP40001359
resource_type: Release Note
platform: macOS
topic: User Experience
technology: CoreServices
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/releasenotes/UserExperience/RN-SearchKit/index.html
archived_at: '2026-07-18T02:59:02.523760Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# SearchKit Framework Release Notes for OS X v10.4

Search Kit is an OS X framework that provides C APIs for indexing and searching text in most human languages.

There are several new Search Kit APIs for OS X v10.4:

1. SKAnalysis.h - five more text analysis properties
2. SKSearch.h - six new api for asynchronous search
3. SKSummary.h  - a new header file for summarization that replaces the functionality in the Find by Content framework

#### Contents:

- [SKAnalysis.h](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjzfvjvomi)
- [SKSearch.h](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjzfvjvomq)
- [SKSummary.h](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjzfvjvomy)

### SKAnalysis.h

|  |  |
| --- | --- |
| **kSKProximityIndexing -The proximity indexing option.** | : The kSKProximityIndexing constant is an optional key in the text analysis properties dictionary whose corresponding value is a CFBoolean object containing the proximity indexing option. If this key is not present, SearchKit indexing defaults to not doing proximity indexing. |
| **kSKMaximumTerms - The maximum unique terms per document to index.** | : The kSKMaximumTerms constant is an optional key in the text analysis properties dictionary whose corresponding value is a CFNumber object containing the maximum unique terms per document to index. If this key is not present, SearchKit indexing defaults to 2000. If the value of this key is zero, there is no limit of the maximum unique terms per document to index. |
| **kSKTermChars - The additional valid "word" characters for indexing.** | : The kSKTermCharSet constant is an optional key in the text analysis properties dictionary whose corresponding value is a CFString object containing the additional characters that you want to count as "word" characters for terms, as oppoosed to "non-word" characters such as spaces. Used for indexing and query processing. |
| **kSKStartTermChars -The additional valid first "word" characters for indexing.** | : The kSKStartTermChars constant is an optional key in the text analysis properties dictionary whose corresponding value is a CFString object containing the additional characters that you want to count as valid first characters of a term.Overrides the kSKTermChars for the first character of a term. |
| **kSKEndTermChars - The additional valid ending "word" characters for indexing.** | : The kSKEndTermChars constant is an optional key in the text analysis properties dictionary whose corresponding value is a CFString object containing the additional characters that you want to count as valid last characters of a term.Overrides the kSKTermChars for the last character of a term. |

### SKSearch.h

```
/*
 * Asynchronous search
 */

/*
 *  SKSearchRef
 *
 *  Summary:
 *    An opaque data type representing an asynchronous search.
 */
typedef struct __SKSearch*              SKSearchRef;

/*
 *  SKSearchOptions
 *
 *  Summary:
 *    The various search options you can use with SKSearchCreate().
 */
typedef UInt32                          SKSearchOptions;
enum {
  kSKSearchOptionDefault        = 0,
  kSearchOptionNoRelevanceScores = 1L << 0, /* Save time by not computing relevance scores. */
  kSKSearchOptionSpaceMeansOR   = 1L << 1 /* Space in a query means OR instead of AND. */
};

/*
 *  SKSearchCreate()
 *
 *  Summary:
 *    Create an asynchronous search request.
 */
extern SKSearchRef
SKSearchCreate(
  SKIndexRef        inIndex,
  CFStringRef       inQuery,
  SKSearchOptions   inSearchOptions);

/*
 *  SKSearchCancel()
 *
 *  Summary:
 *    Cancel the search request.
 */
extern void
SKSearchCancel(SKSearchRef inSearch);

/*
 *  SKSearchFindMatches()
 *
 *  Summary:
 *    Search for up to maximumTime seconds or until  inMaximumCount (or all) items are found.
 *
 *  Discussion:
 *    Returns TRUE if more to search, FALSE when the search is
 *    exhausted. Returns number of entries actually found in
 *    *outFoundCount. The maximumTime of 0 means return quickly, so may
 *    return TRUE, and 0 outFoundCount. The relevance score is not
 *    normalized, so it can be very large.
 */
extern Boolean
SKSearchFindMatches(
  SKSearchRef      inSearch,
  CFIndex          inMaximumCount,
  SKDocumentID *   outDocumentIDsArray,
  float *          outScoresArray,
  CFTimeInterval   maximumTime,
  CFIndex *        outFoundCount);

/*
 *  SKIndexCopyInfoForDocumentIDs()
 *
 *  Summary:
 *    Copies document names and parent ids by way of document IDs in an index.
 */
extern void
SKIndexCopyInfoForDocumentIDs(
  SKIndexRef      inIndex,
  CFIndex         inCount,
  SKDocumentID *  inDocumentIDsArray,
  CFStringRef *   outNamesArray,
  SKDocumentID *  outParentIDsArray);

/*
 *  SKIndexCopyDocumentRefsForDocumentIDs()
 *
 *  Summary:
 *    Copies document references by way of document IDs in an index.
 */
extern void
SKIndexCopyDocumentRefsForDocumentIDs(
  SKIndexRef       inIndex,
  CFIndex          inCount,
  SKDocumentID *   inDocumentIDsArray,
  SKDocumentRef *  outDocumentRefsArray);

/*
 *  SKIndexCopyDocumentURLsForDocumentIDs()
 *
 *  Summary:
 *    Copies document URLs by way of document IDs in an index.
 */
extern void
SKIndexCopyDocumentURLsForDocumentIDs(
  SKIndexRef      inIndex,
  CFIndex         inCount,
  SKDocumentID *  inDocumentIDsArray,
  CFURLRef *      outDocumentURLsArray);
```


### SKSummary.h

```
/*
 * Summarization API
 */

/*
 *  SKSummaryRef
 *
 *  Summary:
 *    An opaque data type representing summary information.
 *
 *  Discussion:
 *    A summary reference contains summary information, from which
 *    summary text can be obtained.
 */
typedef struct __SKSummary*             SKSummaryRef;

/*
 *  SKSummaryCreateWithString()
 *
 *  Summary:
 *    Creates a summary reference with text string.
 *
 *  Discussion:
 *    Creates a summary reference that pre-computes what is needed for
 *    fast summarization. This function must be balanced with a call at
 *    a later time to CFRelease.
 */
extern SKSummaryRef
SKSummaryCreateWithString(CFStringRef inString);

/*
 *  SKSummaryCopySentenceSummaryString()
 *
 *  Summary:
 *    Gets a summary string that includes at most the requested number
 *    of sentences.
 */
extern CFStringRef
SKSummaryCopySentenceSummaryString(
  SKSummaryRef   summary,
  CFIndex        numSentences);
```
