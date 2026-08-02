---
title: PredicateEditorSample
apple_id: DTS10004138
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-03-15'
source_url: https://developer.apple.com/library/archive/samplecode/PredicateEditorSample/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:19:31.463247Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PredicateEditorSample](PredicateEditorSample.md)


[Next](main.m.md)[Previous](PredicateEditorSample.md)

# ReadMe.txt

```
PredicateEditorSample

"PredicateEditorSample" is a Cocoa application that demonstrates how to use the NSPredicateEditor class.  The NSPredicateEditor class is a subclass of NSRuleEditor that is specialized for editing NSPredicate objects.  This sample is intended to show how to use the many different features and aspects of this control and leverages Spotlight to search your Address Book.

It shows how to manage this control inside your window along with an NSTableView, build Spotlight friendly queries based on NSPredicate and NSCompountPredicate, build search results based on NSMetadataQuery object.


Sample Requirements
The supplied Xcode project was created using Xcode v3.2 or later running under Mac OS X 10.6.x or later. Editing the nib files requires Interface Builder 3.0.


Using the Sample
Simply build and run the sample using Xcode.  Enter query information pertaining to your Address Book.  The application will display matches in its table view.
Note that this sample uses Interface Builder 3.0 to build the NSPredicateEditorRowTemplates that make up the control's interface.

AddressBook searches are achieved by specifically requesting the "kind" of data to search via the kMDItemKind key constant.  This is the metadata attribute key that tells Spotlight to search for address book data only.  Together along with the other predicates from the NSPredicateEditor class we form a "compound predicate" and start the query.  The code snippet below found in this sample shows how this is done:

// always search for items in the Address Book
NSPredicate* addrBookPredicate = [NSPredicate predicateWithFormat:@"(kMDItemKind = 'Address Book Person Data')"];
predicate = [NSCompoundPredicate andPredicateWithSubpredicates:[NSArray arrayWithObjects:addrBookPredicate, predicate, nil]];

[query setPredicate: predicate];
[query startQuery];


Changes from Previous Versions
1.0 - First Release
1.1 - Upgraded to support 10.6, now builds 3-way Universal (ppc, i386, x86_64).


Feedback and Bug Reports
Please send all feedback about this sample to 
<http://developer.apple.com/contact/feedback.html>.

Please submit any bug reports about this sample to
<http://developer.apple.com/bugreporter>

Copyright (C) 2006-2010, Apple Inc.
```

[Next](main.m.md)[Previous](PredicateEditorSample.md)

