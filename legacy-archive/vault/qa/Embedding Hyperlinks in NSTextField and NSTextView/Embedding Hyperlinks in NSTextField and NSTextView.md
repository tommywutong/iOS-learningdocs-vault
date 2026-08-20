---
title: Embedding Hyperlinks in NSTextField and NSTextView
apple_id: DTS10004085
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2012-01-05'
source_url: https://developer.apple.com/library/archive/qa/qa1487/_index.html
archived_at: '2026-07-18T02:31:25.044605Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1487

# Embedding Hyperlinks in NSTextField and NSTextView

## Q:  How do I embed a hyperlink inside an NSTextField or NSTextView?

A: You can embed a hyperlink using an `NSAttributedString`. The resultant attributed string will contain the url, style and color for display.

__Figure 1__  An example illustration of an NSTextField with a hyperlink.

!

An easy way to factor this in your application is to add a "category" to the NSAttributedString class. By adding an additional class method to this category, you allow other classes to benefit from this extended feature.

__Listing 1__  Adding a category to NSAttributedString.

```objc
@interface NSAttributedString (Hyperlink)
    +(id)hyperlinkFromString:(NSString*)inString withURL:(NSURL*)aURL;
@end

@implementation NSAttributedString (Hyperlink)
+(id)hyperlinkFromString:(NSString*)inString withURL:(NSURL*)aURL
{
    NSMutableAttributedString* attrString = [[NSMutableAttributedString alloc] initWithString: inString];
    NSRange range = NSMakeRange(0, [attrString length]);

    [attrString beginEditing];
    [attrString addAttribute:NSLinkAttributeName value:[aURL absoluteString] range:range];

    // make the text appear in blue
    [attrString addAttribute:NSForegroundColorAttributeName value:[NSColor blueColor] range:range];

    // next make the text appear with an underline
    [attrString addAttribute:
            NSUnderlineStyleAttributeName value:[NSNumber numberWithInt:NSSingleUnderlineStyle] range:range];

    [attrString endEditing];

    return [attrString autorelease];
}
@end
```


__Listing 2__  Creating a hyperlink attributed string inside an NSTextField.

```objc
-(void)setHyperlinkWithTextField:(NSTextField*)inTextField
{
    // both are needed, otherwise hyperlink won't accept mousedown
    [inTextField setAllowsEditingTextAttributes: YES];
    [inTextField setSelectable: YES];

    NSURL* url = [NSURL URLWithString:@"http://www.apple.com"];

    NSMutableAttributedString* string = [[NSMutableAttributedString alloc] init];
    [string appendAttributedString: [NSAttributedString hyperlinkFromString:@"Apple Computer" withURL:url]];

    // set the attributed string to the NSTextField
    [inTextField setAttributedStringValue: string];

    [string release];
}
```

As you can see, `setHyperlinkWithTextField:` can reside in your class, which can be called from your class's `-awakeFromNib` or NSDocument's `-windowControllerDidLoadNib:`, for example.

__Listing 3__  Creating a hyperlink attributed string inside an NSTextView.

```objc
-(void)setHyperlinkWithTextView:(NSTextView*)inTextView
{
    // create the attributed string
    NSMutableAttributedString *string = [[NSMutableAttributedString alloc] init];

    // create the url and use it for our attributed string
    NSURL* url = [NSURL URLWithString: @"http://www.apple.com"];
    [string appendAttributedString:[NSAttributedString hyperlinkFromString:@"Apple Computer" withURL:url]];

    // apply it to the NSTextView's text storage
    [[inTextView textStorage] setAttributedString: string];

    [string release];
}
```

Note that Listing 3 sets the attributed string a little differently for NSTextView. You must set the text using the `NSTextStorage` object. NSTextStorage is a subclass of NSAttributedString that is the backing store for an NSTextView object.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-01-05 | Removed leaks in two code snippets. |
| 2006-10-02 | New document that shows how a Cocoa app can embed a hyperlink inside both NSTextField and NSTextView using NSAttributedString. |

