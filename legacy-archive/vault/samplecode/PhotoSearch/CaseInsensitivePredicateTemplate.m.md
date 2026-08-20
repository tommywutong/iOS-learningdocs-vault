---
title: PhotoSearch
apple_id: DTS10003994
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2015-12-03'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoSearch/Listings/CaseInsensitivePredicateTemplate_m.html
archived_at: '2026-07-18T03:18:54.634860Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoSearch](PhotoSearch.md)


[Next](SearchQuery.m.md)[Previous](MainWindowController.m.md)

# CaseInsensitivePredicateTemplate.m

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  CaseInsensitivePredicateTemplate is a subclass of 
   NSPredicateEditorRowTemplate that will generate case insensitive 
   comparison predicates; it can be used as the custom subclass of an 
   NSPredicateEditorRowTemplate in Interface Builder. 
 */

#import "CaseInsensitivePredicateTemplate.h"

@implementation CaseInsensitivePredicateTemplate

- (NSPredicate *)predicateWithSubpredicates:(NSArray *)subpredicates {

    // we only make NSComparisonPredicates
    NSComparisonPredicate *predicate = (NSComparisonPredicate *)[super predicateWithSubpredicates:subpredicates];

    // construct an identical predicate, but add the NSCaseInsensitivePredicateOption flag
    return [NSComparisonPredicate predicateWithLeftExpression:predicate.leftExpression
                                              rightExpression:predicate.rightExpression
                                                     modifier:predicate.comparisonPredicateModifier
                                                         type:predicate.predicateOperatorType
                                                      options:predicate.options | NSCaseInsensitivePredicateOption];
}

@end
```

[Next](SearchQuery.m.md)[Previous](MainWindowController.m.md)

