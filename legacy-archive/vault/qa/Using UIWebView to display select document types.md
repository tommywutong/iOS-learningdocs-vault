---
title: Using UIWebView to display select document types
apple_id: DTS40008749
resource_type: QA
platform: iOS
topic: null
technology: UIKit
published: '2009-08-25'
source_url: https://developer.apple.com/library/archive/qa/qa1630/_index.html
archived_at: '2026-07-18T02:33:02.504104Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1630

# Using UIWebView to display select document types

## Q:  How do I display iWork, Office, or other document types in my iPhone OS Application?

A: How do I display iWork, Office, or other document types in my iPhone OS Application?

In addition to HTML content, UIWebView can display specific document types.

iPhone OS 2.2.1 supports the following document types:

- Excel (.xls)
- Keynote (.key.zip)
- Numbers (.numbers.zip)
- Pages (.pages.zip)
- PDF (.pdf)
- Powerpoint (.ppt)
- Word (.doc)

Keynote, Numbers and Pages documents must be created with iWork '06 or iWork '08. iWork '06 and iWork '08 documents are document packages and must be ZIP compressed for UIWebView to recognize them. You must retain both extensions in the file name, such as presentation.key.zip, spreadsheet.numbers.zip or paper.pages.zip. iWork '09 documents are not supported on iPhone OS 2.2.1.

iPhone OS 3.0 supports these additional document types:

- Rich Text Format (.rtf)
- Rich Text Format Directory (.rtfd.zip)
- Keynote '09 (.key)
- Numbers '09 (.numbers)
- Pages '09 (.pages)

iWork '09 documents do not use a package format and must not be ZIP compressed.

To display supported documents in a UIWebView, create an NSURL as a file URL with the path to the document. Listing 1 demonstrates a method that uses a UIWebView to load a document from your application bundle.

__Listing 1__  Loading a document into a UIWebView.

```objc
-(void)loadDocument:(NSString*)documentName inView:(UIWebView*)webView {     NSString *path = [[NSBundle mainBundle] pathForResource:documentName ofType:nil];     NSURL *url = [NSURL fileURLWithPath:path];     NSURLRequest *request = [NSURLRequest requestWithURL:url];     [webView loadRequest:request]; }  // Calling -loadDocument:inView: [self loadDocument:@"mydocument.rtfd.zip" inView:self.myWebview];
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-08-25 | Updated for iPhone OS 3.0. |
| 2009-04-21 | New document that describes how you can use a UIWebView to display select document types in your application |

