---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/SaveAndLoad.html
archived_at: '2026-07-15T07:14:54.268731Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Modifying%20the%20Current%20Selection.md)[Previous](Enabling%20Editing.md)

# Saving and Loading Web Content

After the user edits the content of a WebView, you need some way to access the modified document. In a Cocoa document-based application, you typically allow the user to save and load the document.

For example, in the MiniBrowser application located in `/Developer/Examples/WebKit`, you would implement MyDocument’s [dataRepresentationOfType:](https://developer.apple.com/documentation/appkit/nsdocument/1515081-datarepresentationoftype) method to return an NSData representation of the HTML source. Then implement MyDocument’s [loadDataRepresentation:ofType:](https://developer.apple.com/documentation/appkit/nsdocument/1515046-loaddatarepresentation) method to transform an NSData representation to HTML source and load it into the WebView. Follow these steps to add saving and loading to the MiniBrowser application.

1. First add a variable and accessors to MyDocument to store the HTML source. Modify `MyDocument.h` as follows and implement the corresponding accessor methods in `MyDocument.m`:

```objc
@interface MyDocument : NSDocument
{
    ...
    // Editing Support
    NSString *_source;
}
...
// Editing Support
- (NSString *)source;
- (void)setSource:(NSString *)webContent;
@end
```
2. Next, implement MyDocument’s `dataRepresentationOfType:` method to get the HTML source from the DOM, set the `_source` instance variable, and convert it to an NSData object as follows:

```objc
- (NSData *)dataRepresentationOfType:(NSString *)aType
{
    if (![aType isEqualToString:HTMLDocumentType])
        return nil;

    [self setSource:[(DOMHTMLElement *)[[[webView mainFrame] DOMDocument] documentElement] outerHTML]];
    return [[self source] dataUsingEncoding:NSISOLatin1StringEncoding];
}
```
3. Then implement MyDocument’s `loadDataRepresentation:ofType:` method to transform the NSData object to HTML source as follows:

```objc
- (BOOL)loadDataRepresentation:(NSData *)data ofType:(NSString *)aType
{
    if (![aType isEqualToString:HTMLDocumentType])
        return NO;

    [self setSource:[[NSString alloc] initWithData:data encoding:NSISOLatin1StringEncoding]];
    [[webView mainFrame] loadHTMLString:[self source] baseURL:nil];

    return YES;
}
```

[Next](Modifying%20the%20Current%20Selection.md)[Previous](Enabling%20Editing.md)

