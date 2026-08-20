---
title: How do I add annotations to my IMKit Input Method
apple_id: DTS40009583
resource_type: QA
platform: macOS
topic: User Experience
technology: InputMethodKit
published: '2010-03-03'
source_url: https://developer.apple.com/library/archive/qa/qa1644/_index.html
archived_at: '2026-07-18T02:33:10.151612Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1644

# How do I add annotations to my IMKit Input Method

## Q:  How do I add annotations to my IMKit Input Method?

A: How do I add annotations to my IMKit Input Method?

Candidate annotations are used to provide additional information to the user about a selected candidate in the Input Method candidate window. Annotations are optional and not required for an Input Method, however they can be very helpful in providing additional information about the selected candidate to the user. An example of how this could look during a user's edit session is shown in Figure 1.

__Figure 1__  Example annotation for candidate window.

!

To add this functionality to your Input Method, you will need to create and cache annotation strings for candidates, and display these annotations when requested.

You will want to create and cache a list of annotation strings for specific candidates in your Input Method itself. If you are using `IMKCandidates` to display your candidate window and display the annotation strings, keep in mind that `IMKCandidiates` does not actually track and cache associations between candidates and annotations for you.

How you cache the annotation information is up to you. One possible approach would be to cache a `NSDictionary` where the key is the candidate `NSString` and the value is the `NSAttributedString` annotation string when your IM's `candidates` method is called. Then, when your IM's `candidateSelectionChanged` method is called, you can look up the given candidate string to find the appropriate annotation string, if any.

__Listing 1__  Creating annotation cache.

```
// *** In your class header:  @interface MyInputController : IMKInputController {      // ...     // The rest of your input controller definition, omitted from this snippet.     // ....      // Dictionary that maps candidate string to annotation string for candidates window     NSDictionary *annotationDictionary;  }  @end  // *** In your class implementation:  - (NSArray*)candidates:(id)sender {     NSMutableArray *theCandidates = [NSMutableArray array];      // ...     // Build theCandidates array of candidate NSStrings from converted text input. This depends on      // how you implement your IM and is beyond the scope of this code snippet.     // ...      if (annotationDictionary == nil) {         // Create NSMutableArray of NSAttributedStrings based on our candidate strings         NSMutableArray *annotationStrings = [NSMutableArray array];          for (NSString *candidateString in theCandidates) {             // Determine an appropriate annotation string for the candidate. Again, how this             // is determined is up to your IM to implement, and is beyond the scope of this snippet.             [annotationStrings addObject:[self annotationForCandidateString:candidateString]];         }         // Create the instance-owned dictionary that maps candidate strings to annotations         annotationDictionary = [NSDictionary dictionaryWithObjects:annotationStrings forKeys:theCandidates];     }      return theCandidates;  }
```


If your Input Method uses the `IMKCandidates` class to display candidates, you can also make use of `IMKCandidates` to display annotations. Your Input Method will get called when the user changes the selected candidate via `candidateSelectionChanged`. At this point you will need to determine if the newly selected candidate has an annotation string to display, and if so, display it via a call to `IMKCandidates:showAnnotation`, as shown in Listing 2.

__Listing 2__  Displaying annotations.

```objc
- (void)candidateSelectionChanged:(NSAttributedString*)candidateString {     // ...     // Change marked text for candidate as necessary     // ...      // Determine if the selected candidate string has an annotation. It is up to your IM to     // come up with this. If we continue from the first code snippet, we can use the      // annotationDictionary to look up an annotationString.      extern IMKCandidates *candidates;      NSAttributedString *annotationString = [annotationDictionary objectForKey:candidateString];     if (annotationString != nil) {         [candidates showAnnotation:annotationString];      } }
```

Please note that the annotation string is represented by a `NSAttributedString`, and as such, can contain text from RTF or HTML data sources if needed. See the _[Attributed String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/AttributedStrings.html#//apple_ref/doc/uid/10000036)_ for more details.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-03-03 | New document that describes the steps needed to add and display annotation strings for candidates for an IMKit Input Method |

