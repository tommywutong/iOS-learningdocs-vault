---
title: PhotoSearch
apple_id: DTS10003994
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoSearch/Listings/SearchQuery_m.html
archived_at: '2026-07-18T03:18:55.156194Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoSearch](PhotoSearch.md)


[Next](CaseInsensitivePredicateTemplate.h.md)[Previous](CaseInsensitivePredicateTemplate.m.md)

# SearchQuery.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  Data model for a photo search query. 
 */

#import "SearchQuery.h"

NSString *SearchQueryChildrenDidChangeNotification = @"SearchQueryChildrenDidChangeNotification";

@interface SearchQuery ()

@property (strong) NSMetadataQuery *query;
@property (strong) NSArray *children;

@end


#pragma mark -

@implementation SearchQuery

- (instancetype)init {
    return [self initWithSearchPredicate:nil title:@"" scopeURL:nil];
}

- (instancetype)initWithSearchPredicate:(NSPredicate *)searchPredicate title:(NSString *)title scopeURL:(NSURL *)url {

    self = [super init];
    if (self != nil) {
        _title = title;
        _query = [[NSMetadataQuery alloc] init];
        _searchURL = url;

        // We want the items in the query to automatically be sorted by the file system name;
        // this way, we don't have to do any special sorting
        self.query.sortDescriptors = @[[[NSSortDescriptor alloc] initWithKey:(id)kMDItemFSName ascending:YES]];
        self.query.predicate = searchPredicate;

        // Use KVO to watch the results of the query
        [self.query addObserver:self forKeyPath:@"results" options:NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld context:nil];
        self.query.delegate = self;
        [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(queryNote:) name:nil object:self.query];

        // define the scope/where the search will take placce
        self.query.searchScopes = (url != nil) ? @[url] : nil;

        [self.query startQuery];
    }
    return self;    
}

- (void)dealloc {

    [[NSNotificationCenter defaultCenter] removeObserver:self];    
    [self.query removeObserver:self forKeyPath:@"results"];
}

- (void)sendChildrenDidChangeNote {

    [[NSNotificationCenter defaultCenter] postNotificationName:SearchQueryChildrenDidChangeNotification object:self];
}

- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context {

    // Delegate the KVO notification by sending a children changed note.
    // We could check the keyPath, but there is no need, since we only observe one value.
    //
    _children = self.query.results;
    [self sendChildrenDidChangeNote];
}

#pragma NSMetadataQuery Delegate

- (id)metadataQuery:(NSMetadataQuery *)query replacementObjectForResultObject:(NSMetadataItem *)result {

    // We keep our own search item for the result in order to maintian state (image, thumbnail, title, etc)
    return [[SearchItem alloc] initWithItem:result];
}

- (void)queryNote:(NSNotification *)note {

    // The NSMetadataQuery will send back a note when updates are happening.
    // By looking at the [note name], we can tell what is happening
    //
    if ([note.name isEqualToString:NSMetadataQueryDidFinishGatheringNotification]) {
        // At this point, the query will be done. You may recieve an update later on.
        if (self.children.count == 0) {
            SearchItem *emptyItem = [[SearchItem alloc] initWithItem:nil];
            [emptyItem setTitle:NSLocalizedString(@"No results", @"Text to display when there are no results")];
            _children = @[emptyItem];
            [self sendChildrenDidChangeNote];
        }        
    }
}

@end
```

[Next](CaseInsensitivePredicateTemplate.h.md)[Previous](CaseInsensitivePredicateTemplate.m.md)

