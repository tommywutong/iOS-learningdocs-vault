---
title: SearchKit Programming Guide
apple_id: TP40001071
resource_type: Guide
platform: macOS
topic: User Experience
technology: CoreServices
published: '2005-12-06'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SearchKitConcepts/searchKit_tasks/searchKit_tasks.html
archived_at: '2026-07-18T02:12:49.456294Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SearchKit Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Search%20Kit%20Concepts.md)

# Search Kit Tasks

This chapter provides instructions and code samples for common Search Kit tasks including creating and using indexes of various types, performing searches, and displaying results.

The code samples assume you are using Xcode and they illustrate how to use Search Kit's ANSI-C API within Objective-C methods.

To index a document your application first creates an empty index and then adds document content to it. Search Kit indexes have a variety of characteristics you can set at the time of index creation. These characteristics determine such things as which types of searches users can perform.

Your application can create file-based or memory-based indexes. Use file-based indexes for information you want to retain between invocations of your program. Use memory-based indexes for temporary processes such as searching on a subset of a file-based index. Because memory-based indexes can be opened as read-only as well as read/write, you can use a memory-based index when your application needs an index that is open only for searching.

When you create an index, either file-based or memory-based, the index is automatically open. The Search Kit functions for opening indexes let your application re-open an index that you've closed, or open a previously-created file-based index.

To create a persistent, file-based index your application need only supply a file-system location, in the form of a CFURL object, and an appropriate constant specifying the type of index you want. If you’re developing in Cocoa, you can use an NSURL object for the index location and cast it to a CFURLRef object as shown in Listing 3-1.

To create an index in memory, see [Creating an Index in Memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzt). To specify text analysis properties for an index, see [Specifying Text Analysis Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzu).

__Listing 3-1__  Creating a file-based index

```objc
- (void) newIndexInFile {
    NSString *path = [pathTextField stringValue];     // 1
    NSURL *url = [NSURL fileURLWithPath: path];       // 2

    NSString *name = [nameTextField stringValue];     // 3
    if ([name length] == 0) name = nil;

    SKIndexType type = kSKIndexInverted;              // 4

    mySKIndex = SKIndexCreateWithURL (                // 5
        (CFURLRef) url,
        (CFStringRef) name,
        (SKIndexType) type,
        (CFDictionaryRef) NULL
    );
}
```

Here is how this code works:

1. Gets the file-system path for a new file-based index and converts it to an NSString object.
2. Converts the NSString object to an NSURL object.
3. Gets the optional index name, if provided, and saves it in an NSString object. If there's no index name, uses `nil`.
4. Defines the index type, in this case specifying an inverted index.
5. Creates the new, empty, file-based index using the specified URL, name, and type. Returns a Search Kit index object. In this simple example, the code creates an index without specifying a text analysis properties dictionary. See [Specifying Text Analysis Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzu) for more information on using a text analysis properties dictionary.

To create an index in memory, your application supplies an [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) object (or, equivalently, a [CFMutableDataRef](https://developer.apple.com/documentation/corefoundation/cfmutabledataref) object) to hold the index. [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzrgm) shows how.

__Listing 3-2__  Creating an index in memory

```objc
- (void) newIndexInMemory {
    NSString *name = [nameTextField stringValue];               // 1
    if ([name length] == 0) name = nil;

    SKIndexType type = kSKIndexInverted;                        // 2

    indexObject = [[NSMutableData alloc] initWithCapacity: 0];  // 3

    mySKIndex = SKIndexCreateWithMutableData (                  // 4
                    (CFMutableDataRef) indexObject,
                    (CFStringRef)      name,
                    (SKIndexType)      type,
                    (CFDictionaryRef)  NULL
                );
}
```

Here is how this code works:

1. Gets the optional index name, if provided, and saves it in an NSString object. If there's no index name, uses `nil`.
2. Defines the index type, in this case specifying an inverted index.
3. Creates a mutable data object to hold the new memory-based index.
4. Creates the new, empty, memory-based index using the supplied mutable data object, name, and type. Returns a Search Kit index object. In this simple example, the code creates an index without specifying a text analysis properties dictionary. See [Specifying Text Analysis Properties](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzu) for more information on using a text analysis properties dictionary.

To instead create an index in a file, see [Creating a File-Based Index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzv).

To work with an already-existing file-based index (one that existed before your application launched), or to work with one that you have explicitly closed, your application must first open it. Once open, a file-based Search Kit index can be searched or updated.

Memory-based indexes can be opened in a read-only mode as well as in a read/write mode. See [Opening a Memory-Based Index for Searching Only](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzw) and [Opening a Memory-Based Index for Searching or Updating](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzx).

__Listing 3-3__  Opening a file-based index for searching or updating

```objc
- (void) openIndex {
    NSString *path = [pathTextField stringValue];      // 1
    NSURL *url = [NSURL fileURLWithPath:path];         // 2

    NSString *name = [nameTextField stringValue];      // 3
    if ([name length] == 0) name = nil;

    // open the specified index
   mySKIndex = SKIndexOpenWithURL (                    // 4
                   (CFURLRef) url,
                   (CFStringRef) name,
                   true
                );
}
```

Here's how this code works:

1. Gets the file-system path for the existing file-based index and converts it to an NSString object.
2. Converts the path NSString object to an NSURL object.
3. Gets the index name, if provided, for the existing file-based index and saves it as an NSString object. If there's no index name, uses `nil`.
4. Opens the file-based index and returns a Search Kit index object.

To work with an already-existing memory-based index that your application has explicitly closed, your application must first open it.

This task describes how to open a memory-based index for searching only. To open a memory-based index for searching or updating, see [Opening a Memory-Based Index for Searching or Updating](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzx).

__Listing 3-4__  Opening a memory-based index for searching only

```objc
- (void) openIndexInMemoryReadOnly {
    mySKIndex = SKIndexOpenWithData (
                   (CFDataRef)   indexObject,
                   (CFStringRef) nil
               );
}
```

Here's how this code works:

Your application provides a previously-created mutable data object to the `SKIndexOpenWithData` function, which then returns a read-only Search Kit index object. The index name is optional and in this example is specified as `nil`. To open a memory-based index for searching and updating, see [Opening a Memory-Based Index for Searching or Updating](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzx). For information on creating a mutable data object, see [Creating an Index in Memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzt).

To work with an already-existing memory-based index that your application has explicitly closed, your application must first open it.

This task describes how to open a memory-based index for searching or updating. To open a memory-based index for searching only, see [Opening a Memory-Based Index for Searching Only](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzw).

__Listing 3-5__  Opening a memory-based index for searching or updating

```objc
- (void) openIndexInMemoryReadWrite {
    mySKIndex = SKIndexOpenWithMutableData (
                   (CFMutableDataRef) indexObject,
                   (CFStringRef)      nil
                );
}
```

Here's how this code works:

Your application provides a previously-created mutable data object to the `SKIndexOpenWithMutableData` function, which then returns a read/write Search Kit index object. The index name is optional and in this example is specified as `nil`. To open a memory-based index for searching only, see [Opening a Memory-Based Index for Searching Only](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzw). For information on creating a mutable data object, see [Creating an Index in Memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzt).

A Search Kit index, as a Core Foundation object, can be closed by passing the index object to the `CFRelease` function. Alternatively, your application can use the `SKIndexClose` function as shown here.

__Listing 3-6__  Closing an index

```objc
- (void) closeIndex {
    if (mySKIndex) {
        SKIndexClose (mySKIndex);
        mySKIndex = nil;
    }
}
```


Your application specifies an index's text analysis properties at the time of index creation. This task illustrates setting some of the available properties including minimum term length, stopwords, and customized term characters while creating a new file-based index.

__Listing 3-7__  Specifying text analysis properties

```objc
- (void) newIndexWithPropertiesInFile {
    NSString *path = [pathTextField stringValue];                // 1
    NSURL *url = [NSURL fileURLWithPath: path];                  // 2

    NSString *name = [nameTextField stringValue];                // 3
    if ([name length] == 0) name = nil;

    SKIndexType type = kSKIndexInverted;                         // 4

    NSNumber *minTermLength = [NSNumber numberWithInt: (int) 3]; // 5

    NSSet *stopwords = [NSSet setWithObjects:                    // 6
                            @"all",
                            @"and",
                            @"its",
                            @"it's",
                            @"the",
                            nil
                        ];

        NSDictionary *properties =                               // 7
        [NSDictionary dictionaryWithObjectsAndKeys:
            @"", @"kSKStartTermChars",   // additional starting-characters for terms
            @"-_@.'", @"kSKTermChars",   // additional characters within terms
            @"", @"kSKEndTermChars",     // additional ending-characters for terms
            minTermLength, @"kSKMinTermLength",
            stopwords, @"kSKStopWords",
            nil
        ];

    mySKIndex = SKIndexCreateWithURL(                            // 8
        (CFURLRef) url,
        (CFStringRef) name,
        (SKIndexType) type,
        (CFDictionaryRef) properties
    );
}
```

Here's how this code works:

1. Gets the file-system path for a new file-based index and converts it to an NSString object.
2. Converts the NSString object to an NSURL object.
3. Gets the optional index name, if provided, and saves it in an NSString object. If there's no index name, uses `nil`.
4. Defines the index type, in this case specifying an inverted index.
5. Specifies the minimum term length as a NSNumber object.
6. Specifies a list of stopwords as an NSSet object.
7. Specifies the text analysis properties dictionary, including minimum term length, stopwords, and additional term character specifications.
8. Creates the new, empty, file-based index using the specified URL, name, type, and text analysis properties. Returns a Search Kit index object.

Loading the Spotlight text importers is a single-step process that applications typically perform at launch time.

__Listing 3-8__  Loading the Spotlight text importers

```objc
- (void) loadImporters {
    SKLoadDefaultExtractorPlugIns ();
}
```


To add a file-based document to an index your application simply supplies the index object and a document URL object. You can optionally provide a MIME type hint, as described in _[Search Kit Reference](https://developer.apple.com/documentation/coreservices/search_kit)_. Finally, you specify the document as replaceable or not.

__Listing 3-9__  Adding a file-based document to an index

```objc
- (void) addDoc {
    NSString *path = [myFilePathTextField stringValue];  // 1
    NSURL *url = [NSURL fileURLWithPath: path];          // 2
    SKDocumentRef doc = SKDocumentCreateWithURL (        // 3
                            (CFURLRef) url
                        );

    Boolean added = SKIndexAddDocument (                 // 5
        (SKIndexRef) mySKIndex,
        (SKDocumentRef) doc,
        (CFStringRef) NULL,    // optional MIME type hint
        (Boolean) true         // replaceable
    );
}
```

How this code works:

1. Gets the file-system path for the document to be added to an index. Converts the path string to an NSString object.
2. Converts the NSString object to an NSURL object.
3. Creates a document URL object from the NSURL object.
4. Adds the document identified by the document URL object, along with its text, to the specified Search Kit index.

To index a folder of documents, your application makes use of other Cocoa frameworks. This task illustrates how to descend recursively into a folder structure.

__Listing 3-10__  Adding a folder of file-based documents to an index

```objc
- (void) addDocsInFolder {
    NSString *path = [myFilePathTextField stringValue];    // 1

    NSDirectoryEnumerator *dirEnumerator =                 // 2
        [[NSFileManager defaultManager] enumeratorAtPath: path];

    NSString *item;
    while ((item = [dirEnumerator nextObject]) != nil) {   // 3
        NSString *fullPath =                               // 4
            [path stringByAppendingPathComponent: item];
        if (!fullPath) continue;

        NSURL *url =                                       // 5
            [NSURL fileURLWithPath: fullPath];
        if (!url) continue;

        SKDocumentRef doc = SKDocumentCreateWithURL (      // 6
                                (CFURLRef) url
                            );
        if (!doc) continue;

        Boolean added = SKIndexAddDocument (               // 8
            (SKIndexRef) mySKIndex,
            (SKDocumentRef) doc,
            (CFStringRef) NULL,   // optional MIME type hint
            (Boolean) true        // replaceable
        );
    }
}
```

Here's how this code works:

1. Gets the file-system path for a folder containing file-based documents. Converts the path string to an NSString object.
2. Creates an NSDirectoryEnumerator object for recursively finding all the file-based documents within the folder.
3. Steps through the enumerator, getting the path to each file-based document in the folder.
4. Converts each path to an NSString object.
5. Converts each NSString object to an NSURL object.
6. Creates a document URL object from each NSURL object.
7. Adds the document identified by the document URL object, along with its text, to the specified Search Kit index.

To add text explicitly to an index, your application gets the text, parses it as necessary, and then hands it off along with an index object to Search Kit. This example illustrates indexing text from a text field in the user interface of an application. You could just as well take text from a database record or from a remote URL, for example.

__Listing 3-11__  Adding text explicitly to an index

```objc
- (void) addDocWithText {
    NSString *path = [myFilePathTextField stringValue];  // 1
    NSURL *url = [NSURL fileURLWithPath:path];           // 2

    SKDocumentRef doc = SKDocumentCreateWithURL (        // 3
                            (CFURLRef) url
                        );

    NSString *contents = [fileContentsTextView string];  // 5
    Boolean added = SKIndexAddDocumentWithText (         // 6
                        mySKIndex,
                        doc,
                        (CFStringRef) contents,
                        (Boolean) true     // replaceable
                    );
}
```

Here's how this code works:

1. Gets the file-system path for the document to be added to an index. Converts the path string to an NSString object.
2. Converts the NSString object to an NSURL object.
3. Creates a document URL object from the NSURL object.
4. Gets textual content from a user-interface text field and converts it to an NSString object.
5. Adds the document URL object along with the specified text to the specified Search Kit index. The text is associated in the index to the document URL object such that queries that match terms in the text will return the document URL object.

To reindex a document that has changed, simply replace it in the index. Do this by calling the `SKIndexAddDocumentWithText` or `SKIndexAddDocument` function, as appropriate, with the _inCanReplace_ parameter set to a `true` value. This example assumes that the document involved is a local, file-based document and so uses the `SKIndexAddDocument` function.

__Listing 3-12__  Updating an index when a document changes

```objc
- (void) replaceChangedDoc: (id) sender {
    NSString *path = [myFilePathTextField stringValue];   // 1
    NSURL *url = [NSURL fileURLWithPath:path];
    SKDocumentRef doc = SKDocumentCreateWithURL (
                            (CFURLRef) url
                        );

    Boolean replaced = SKIndexAddDocument (               // 2
                        mySKIndex,
                        doc,
                        NULL,
                        true
                    );
}
```

1. Gets the file-system path for the replacement document. Converts the path string to an NSString object.]
2. Replaces the document identified by the document URL object, along with its text, in the specified Search Kit index.

To reindex a document that has moved, or moved and changed, perform these three steps:

1. Remove the old document with the `SKIndexRemoveDocument` function.
2. Remove the old text (if desired, or if the index is significantly fragmented) with the `SKIndexCompact` function.
3. Add the changed document and its text to the index.

Compacting the index during this process removes any orphaned terms. However, the `SKIndexCompact` function can be expensive in terms of performance. Apple recommends that you do not call it every time a document is modified or deleted, but only when an index is significantly fragmented (bloated with unused text).

To check for bloat you can take advantage of the way Search Kit allocates document IDs. It does so starting at 1 and without reusing previously allocated IDs for an index. Simply compare the highest document ID, found with the `SKIndexGetMaximumDocumentID` function, with the current document count, found with the `SKIndexGetDocumentCount` function.

The following simple example illustrates compacting without checking for index bloat.

__Listing 3-13__  Updating an index when a document moves or moves and changes

```objc
- (void) replaceDoc: (id) sender {
//..........................................................................
// remove a specified document from an index
    NSString *path = [myFilePathTextField stringValue]; // 1
    NSURL *url = [NSURL fileURLWithPath: path];         // 2

    SKDocumentRef doc = SKDocumentCreateWithURL (       // 3
                            (CFURLRef) url
                        );

    Boolean removed = SKIndexRemoveDocument (           // 5
                          mySKIndex,
                          doc
                       );
//..........................................................................
// compact the index to remove the terms associated with the removed document
    SKIndexCompact (mySKIndex);                         // 6
//..........................................................................
// add the document and its terms back to the index
    NSString *path = [myFilePathTextField stringValue]; // 7
    NSURL *url = [NSURL fileURLWithPath:path];
    SKDocumentRef doc = SKDocumentCreateWithURL (
                            (CFURLRef) url
                        );

    Boolean added = SKIndexAddDocument (                // 8
                        mySKIndex,
                        doc,
                        NULL,
                        true
                    );
}
```

Here's how this code works:

1. Gets the file-system path for the document to be removed from an index. Converts the path string to an NSString object.
2. Converts the NSString object to an NSURL object.
3. Creates a document URL object from the NSURL object.
4. Removes the document URL object from the specified index.
5. Compacts the index to remove the terms associated with the removed document.
6. Gets the file-system path for the replacement document. Converts the path string to an NSString object.
7. Adds the replacement document identified by the document URL object, along with its text, to the specified Search Kit index.

This section describes each of the sub-tasks important to query-based searching and then assembles them in the task titled [A Complete Search Method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzy). Briefly, the steps are:

- Specify the maximum number of hits to return; this is simply defining a constant.
- Set up the search options.
- Get the user's query.
- Create an asynchronous search object.
- Request hits from the search object.
- Convert the hits into document locations and displays the results.

Your application can use similarity-based searching instead of query-based searching by turning on the `kSKSearchOptionFindSimilar` flag when creating a search object. In this case, use the content of an example document, or a portion of an example document, as the query string.

When your application creates a search object it can specify a variety of search options. Each option is simply a binary flag for the _inSearchOptions_ parameter of the [SKSearchCreate](https://developer.apple.com/documentation/coreservices/1443079-sksearchcreate) function.

__Listing 3-14__  Setting up search options

```
SKSearchOptions options = kSKSearchOptionDefault;    // 1

if ([searchOptionNoRelevance intValue])              // 2
    options |= kSKSearchOptionNoRelevanceScores;
if ([searchOptionSpaceIsOR intValue])                // 3
    options |= kSKSearchOptionSpaceMeansOR;
if ([searchOptionSpaceFindSimilar intValue])         // 4
    options |= kSKSearchOptionFindSimilar;
```

Here's how this code works:

1. Specifies use of the default set of search options.
2. If the user has specified that searches should not consider relevance, adds that option.
3. If the user has specified that spaces should indicate a logical `OR` in a query, adds that option.
4. If the user has specified similarity searching instead of query-based searching, adds that option.

This task illustrates the simple step of creating an NSString object from a user's query.

__Listing 3-15__  Getting a user's query

```
NSString *query = [mySearchField stringValue];
```


Your application creates a search object by supplying an index object, an NSString object representing the user's query, and a set of option flags that determine the searching behavior.

__Listing 3-16__  Creating an asynchronous search object

```
SKSearchRef search = SKSearchCreate (            // 1
                         mySKIndex,
                         (CFStringRef) query,
                         options
                     );
```

This code creates a search object based on the user's query and the specified search options, targeting the specified Search Kit index.

To retrieve matches from an asynchronous search object, your application sets up arrays to hold the results and then requests the results. You can use a loop to keep requesting additional hits while there are more to be had, as illustrated in this task and in [A Complete Search Method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzy).

The result of a hit is a lightweight document identifier. The next task, [Getting Document Locations and Displaying Results](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzz), illustrates converting the document identifiers to document locations as represented by document URL objects.

__Listing 3-17__  Getting matches from a search object

```
while (more) {
    SKDocumentID    foundDocIDs [kSearchMax];         // 1
    float           foundScores [kSearchMax];         // 2
    float *scores;                                    // 3
    Boolean unranked =                                // 4
        options & kSKSearchOptionNoRelevanceScores;

    if (unranked) {                                   // 5
        scores = NULL;
    } else {
        scores = foundScores;
    }

    CFIndex foundCount = 0;                           // 6
    more = SKSearchFindMatches (                      // 7
              search,
              kSearchMax,
              foundDocIDs,
              scores,
              1,    // maximum time before function returns, in seconds
              &foundCount
          );
    // display or accumulate results here

    totalCount += foundCount;                         // 8
}
```

Here's how this code works:

1. Sets up an array to hold document identifiers resulting from hits during the search.
2. Sets up an array to hold relevance scores.
3. Sets up a pointer to the relevance scores array.
4. Creates a Boolean flag specifying whether or not relevance scores should be reported.
5. Uses the relevance flag to define the _outScoresArray_ parameter for the `SKSearchFindMatches` function.
6. Initializes the found count to 0.
7. Queries the search object. The `SKSearchFindMatches` function places hits in the _foundDocIDs_ array, relevance scores in the _scores_ array, and a Boolean value indicating whether there are more results to be had (`TRUE`) or not (`FALSE`).
8. Accumulates the number of new matches into the total number of matches.

To obtain results that are meaningful to a user, you convert each of the document identifiers, provided by the search object as hits, to a document location in the form of a document URL object. This task illustrates a simple logging of results—including document ID, document URL, and relevance score if applicable—to a text field.

In this code excerpt, and in the complete example shown in [A Complete Search Method](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzy), the code simply displays results as they're found. Using other Cocoa frameworks, you may want to, instead, accumulate results and present them in a single list sorted by relevance and perhaps dynamically updated.

__Listing 3-18__  Getting document locations and displaying results

```
SKDocumentRef   foundDocRefs [kSearchMax];                 // 1
SKIndexCopyDocumentRefsForDocumentIDs (                    // 2
    mySKIndex,
    (CFIndex) foundCount,
    foundDocIDs,
    foundDocRefs
);

CFIndex pos;
for (pos = 0; pos < foundCount; pos++) {                   // 3
    SKDocumentRef doc = (SKDocumentRef) foundDocRefs[pos]; // 4

    NSURL *url = SKDocumentCopyURL (doc);                  // 5

    NSString *urlStr = [url absoluteString];               // 6

    NSString *desc;
    if (unranked) {                                        // 7
        desc = [NSString stringWithFormat:
            @"---\nDocID: %d,
            URL: %@",
            (int) foundDocIDs [pos],
            urlStr];
    } else {
        desc = [NSString stringWithFormat:
            @"---\nDocID: %d,
            Score: %f,
            URL: %@",
            (int) foundDocIDs[ pos],
            foundScores [pos],
            urlStr];
    }
    [self log: desc];                                      // 8
```

Here's how this code works:

1. Sets up an array to hold document URL objects derived from the document identifiers collected in [Getting Matches From a Search Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzrga).
2. Converts the document identifiers to document URL objects. The found count and the document identifiers are from [Getting Matches From a Search Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzrfvbuqmrqgqwvgvzrga).
3. Iterates through the `foundDocRefs` array to convert document URL objects to NSString objects for display.
4. Gets the next document URL object.
5. For the current document URL object, gets the URL.
6. Converts the URL to an NSString object.
7. Formats the result information for the current hit. The information to be displayed depends on whether the search was ranked or unranked.
8. Displays the results using the applications `log:` method (not illustrated here).

This task collects the preceding code excerpts in this section and presents a complete search method. As described in the introduction to this section, your application:

- Specifies the maximum number of hits to return.
- Sets up the search options.
- Gets the user's query.
- Creates an asynchronous search object.
- Requests hits from the search object.
- Converts the hits into document locations and displays the results.

For descriptions of how this code works, refer to the preceding subtasks in this section.

__Listing 3-19__  A complete search method

```objc
//..........................................................................
// specify the maximum number of hits
#define kSearchMax 1000

- (void) search {
//..........................................................................
// set up search options
    SKSearchOptions options = kSKSearchOptionDefault;

    if ([searchOptionNoRelevance intValue]) options |= kSKSearchOptionNoRelevanceScores;
    if ([searchOptionSpaceIsOR intValue]) options |= kSKSearchOptionSpaceMeansOR;
    if ([searchOptionSpaceFindSimilar intValue]) options |= kSKSearchOptionFindSimilar;

//..........................................................................
// get the user's query
    NSString *query = [mySearchField stringValue];

//..........................................................................
// create an asynchronous search object
    SKSearchRef search = SKSearchCreate (
                             mySKIndex,
                             (CFStringRef) query,
                             options
                         );

//..........................................................................
// get matches from a search object
    Boolean more = true;
    UInt32 totalCount = 0;

    while (more) {
        SKDocumentID  foundDocIDs [kSearchMax];
        float         foundScores [kSearchMax];
        SKDocumentRef foundDocRefs [kSearchMax];

        float *scores;
        Boolean unranked = options & kSKSearchOptionNoRelevanceScores;

        if (unranked) {
            scores = NULL;
        } else {
            scores = foundScores;
        }

        CFIndex foundCount = 0;
        CFIndex pos;

        more =  SKSearchFindMatches (
                    search,
                    kSearchMax,
                    foundDocIDs,
                    scores,
                    1, // maximum time before func returns, in seconds
                    &foundCount
                );

        totalCount += foundCount;

//..........................................................................
// get document locations for matches and display results.
//     alternatively, you can collect results over iterations of this loop
//     for display later.

        SKIndexCopyDocumentRefsForDocumentIDs (
            (SKIndexRef) mySKIndex,
            (CFIndex) foundCount,
            (SKDocumentID *) foundDocIDs,
            (SKDocumentRef *) foundDocRefs
        );

        for (pos = 0; pos < foundCount; pos++) {
            SKDocumentRef doc = (SKDocumentRef) foundDocRefs[pos];
            NSURL *url = SKDocumentCopyURL (doc);
            NSString *urlStr = [url absoluteString];

            NSString *desc;

            if (unranked) {
                desc = [NSString stringWithFormat:
                        @"---\nDocID: %d, URL: %@",
                        (int) foundDocIDs[pos], urlStr];
            } else {
                desc = [NSString stringWithFormat:
                        @"---\nDocID: %d, Score: %f, URL: %@",
                        (int) foundDocIDs[pos], foundScores[pos], urlStr];
            }
            [self log: desc];
        }
    }

    NSString *desc = [NSString stringWithFormat:
                        @"\"%@\" - %d matches", query, (int) totalCount];
    [self log: desc];
}
```

For descriptions of how this code works, refer to the preceding subtasks in this section.

To search an index group in parallel you can use a separate thread for querying each search object. Alternatively, as illustrated here, you can repeatedly rotate through a set of search objects, querying one and then moving on to the next, by using the timeout option in the [SKSearchFindMatches](https://developer.apple.com/documentation/coreservices/1448608-sksearchfindmatches) function.

__Listing 3-20__  Using timeout to search an index group in parallel

```
completeCount = indexCount;                   // 1
while (completeCount) {                       // 2
    for (i = 0; i < indexCount; i++) {
        if (more [i]) {
            more [i] = SKSearchFindMatches (  // 3
                           searchObjects [i],
                           kSearchMax,
                           foundDocIDs,
                           scores,
                           timeout,
                           &foundCount
                       );

            if (!more [i]) completeCount--;   // 4
            ProcessHits (                     // 5
                searchObjects [i],
                foundDocIDs,
                scores,
                foundCount
            );
        }
    }
}
```

Here's how this code works:

1. Initializes the `completeCount` variable to the number of indexes in the group. An application using this code would have previously defined one search object per index in the group. It also would have initialized the `more` array with `true` values for each element. The `completeCount` variable holds the diminishing number of search objects that still have results available.
2. Iterates through the list of search objects, getting hits from each in turn. After the period specified by the _timeout_ parameter, moves on to the next search object. As long as hits from at least one search object are not exhausted, repeats the iteration.
3. Gets the next set of search hits for the current search object, accumulating the results in `foundDocIDs`, `scores`, and `foundCount`.
4. If no new search hits were found for the current search object, decrements the number of active search objects.
5. Calls the application-defined `ProcessHits` function to work with the new search hits.

[Next](Document%20Revision%20History.md)[Previous](Search%20Kit%20Concepts.md)

