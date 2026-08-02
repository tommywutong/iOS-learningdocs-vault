---
title: Common mistakes with delegation in Cocoa
apple_id: DTS10004461
resource_type: QA
platform: macOS
topic: General
technology: null
published: '2008-02-27'
source_url: https://developer.apple.com/library/archive/qa/qa1554/_index.html
archived_at: '2026-07-18T02:32:18.064488Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1554

# Common mistakes with delegation in Cocoa

## Q:  One of the delegate methods in my Cocoa application isn't being invoked. What is probably wrong?

A: One of the delegate methods in my Cocoa application isn't being invoked. What is probably wrong?

When a delegate message isn't being received as you intended, it is usually a sign of one of two things, either:

1. the method selectors don't match, often because of capitialization or a missing colon, or
2. the delegate outlet has not been set or is simply set to the wrong object.

To illustrate further, let's say that you want to handle attempts by the user to close the window `myWindow` in your application. When the user clicks on the close box, the window object will send the equivalent of  `[delegate respondsToSelector:@selector(windowShouldClose:)]` to see if it should even send the delegate message. If the receiver is `nil`, or the `respondsToSelector:` test returns `NO`, the delegate message will not be sent.

__Verify that the method signatures match__

Be sure you've implemented the right method. It is not uncommon for a method selector like -`windowShouldClose:` to either be misspelled (e.g. -`windowShoulfClose:`), miscapitalized (e.g. -`windowShouldclose`:) or be missing the colon (-`windowShouldClose`). These all describe a different method, and the runtime test will fail.

Perhaps the safest habit to develop is to simply always cut and paste the method selector. In earlier releases of Mac OS X you can find the delegate methods on the Class Reference page. In more recent releases, you'll also find delegate methods grouped together as an informal protocol (a category on NSObject). For example, the window delegate methods are declared in `NSWindow.h` in the `NSObject(NSWindowDelegate)` category.

__Ensure that the delegate is set properly__

Even if you've implemented the correct method, it can be easy to overlook assigning the delegate object. Sometimes a connection may have become disconnected in the nib file or be made to the wrong object. So be sure to check and make sure that the instance variable (most often an `IBOutlet` named `delegate`) is connected correctly in Interface Builder, or alternatively, that the appropriate accessor method is being used to set the instance variable at runtime.

__Listing 1__  If you don't, or can't, assign a delegate in Interface Builder, you can set it in code.

```objc
- (void) awakeFromNib {     [[NSFontManager sharedManager] setDelegate:self]; }
```

Prior to release, consider the use of assertions to ensure connections were established correctly.

__Listing 2__  Use of NSAssert() during debugging to test for a delegate connection.

|  |
| --- |
| ``` #if ! defined(NDEBUG)

  - (void) awakeFromNib {     // let's make sure that connection in Interface Builder was made, and made to us     NSAssert([myWindow delegate] == self, @"You forgot to connect the window delegate.!");
    // ... }  #endif ``` |

__Delegates and memory management__

Note that delegating objects keep a weak reference to their delegates. In other words, delegates are not retained by the objects they respond to: they are free to come and go at any time. When using garbage collection, this weak reference means you don't need to do anything about this relationship when the delegate is collected. However, when using retain counting it is essential to explicitly clear this relationship when the object is deallocated.

__Listing 3__  When not under garbage-collection, a delegate must clear itself before deallocation.

```objc
- (void) dealloc {     // unhook ourselves so the window won't try to message us in the future     [myWindow setDelegate:nil];     [super dealloc]; }
```

__For More Information__

See the [Cocoa documentation](https://developer.apple.com/documentation/Cocoa/index.html#//apple_ref/doc/uid/TP30000440-TP30000416) for more on [Delegates and Data Sources](https://developer.apple.com/documentation/Cocoa/Conceptual/CocoaFundamentals/CommunicatingWithObjects/chapter_6_section_4.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-02-27 | New document that the two most common errors that lead to a delegate method not being received. |

