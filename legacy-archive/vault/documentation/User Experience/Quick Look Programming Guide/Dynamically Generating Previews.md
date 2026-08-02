---
title: Quick Look Programming Guide
apple_id: TP40005020
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickLook
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Quicklook_Programming_Guide/Articles/QLDynamicGeneration.html
archived_at: '2026-07-18T02:12:36.118624Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quick Look Programming Guide](Introduction%20to%20Quick%20Look%20Programming%20Guide.md)


[Next](Saving%20Previews%20and%20Thumbnails%20in%20the%20Document.md)[Previous](Drawing%20Thumbnails%20and%20Previews%20In%20a%20Graphics%20Context.md)

# Dynamically Generating Previews

If you can readily convert a document from its native format into an appropriate Quick Look format, your generator can perform that conversion for previews of that document. Such conversion is most useful for textual Quick Look formats (HTML, RTF, and plain text), but you may also generate previews in any format supported by Quick Look; for example, if you convert a document representing a 3D model into Digital Asset Exchange (DAE) format, Quick Look can display a preview interface allowing the model to be zoomed and rotated. (Note that a graphics context remains the most efficient way to provide two-dimensional image data to Quick Look; see [Drawing Thumbnails and Previews In a Graphics Context](Drawing%20Thumbnails%20and%20Previews%20In%20a%20Graphics%20Context.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqobnknlti) for details.)

Creating Textual Representations Dynamically discusses one way to dynamically create a textual preview (in this case, RTF).

If you can generate HTML data for your preview, you can also include attachments for such items as images, CSS stylesheets, and JavaScript scripts. You can use these items to provide detailed layouts and interactivity in the Quick Look preview interface; [Generating Enriched HTML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjvfvjvomq) describes this approach.

Dynamic preview generation can be useful for document types that contain textual information in non-human-readable format. An example of this kind of document type is the localized strings format used by Xcode (see Localizing String Resources for more information). A localized strings document can be stored in binary or XML format, so a Quick Look generator can interpret these formats and generate an RTF preview that uses fonts and colors to make the document’s content easy to read. The code example in [Listing 6-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrqfvbuqmjvfvjvomy) illustrates one way to create such a preview.

The [QLPreviewRequestSetDataRepresentation](https://developer.apple.com/documentation/quicklook/1402661-qlpreviewrequestsetdatarepresent) function call is the most important part of this code. The generator provides two parameters to this function—the RTF data for the preview and a UTI constant that indicates which native Quick Look the data object contains.

__Listing 6-1__  Generating a preview in RTF format

```
OSStatus GeneratePreviewForURL(void *thisInterface, QLPreviewRequestRef preview, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef options)
{
    @autoreleasepool {

        // Load the strings dictionary from the URL
        NSDictionary *localizationDict = [NSDictionary dictionaryWithContentsOfURL:(__bridge NSURL *)url];
        if (!localizationDict) return noErr;

        // The above might have taken some time, so before proceeding make sure the user didn't cancel the request
        if (QLPreviewRequestIsCancelled(preview)) return noErr;

        // Set up for producing attributed string output
        NSDictionary *keyAttrs = @{ NSFontAttributeName : [NSFont fontWithName:@"Helvetica-Oblique" size:11.0],
                                    NSForegroundColorAttributeName : [NSColor grayColor] };
        NSDictionary *valAttrs = @{ NSFontAttributeName : [NSFont fontWithName:@"Helvetica-Bold" size:18.0] };
        NSAttributedString *newline = [[NSAttributedString alloc] initWithString:@"\n"];
        NSMutableAttributedString *output = [[NSMutableAttributedString alloc] init];

        // Iterate through pairs in the dictionary to add formatted output
        [localizationDict enumerateKeysAndObjectsUsingBlock:^(id key, id val, BOOL *stop) {
            NSAttributedString *keyString = [[NSAttributedString alloc] initWithString:key attributes:keyAttrs];
            NSAttributedString *valString = [[NSAttributedString alloc] initWithString:val attributes:valAttrs];
            [output appendAttributedString:valString];
            [output appendAttributedString:newline];
            [output appendAttributedString:keyString];
            [output appendAttributedString:newline];
            [output appendAttributedString:newline];
        }];

        // Get RTF representation of the attributed string
        NSData *rtfData = [output RTFFromRange:NSMakeRange(0, output.length) documentAttributes:nil];

        // Pass preview data to QuickLook
        QLPreviewRequestSetDataRepresentation(preview,
                                              (__bridge CFDataRef)rtfData,
                                              kUTTypeRTF,
                                              NULL);
    }
    return noErr;
}
```


A generally useful but slightly more complex approach to generating a preview dynamically is to create HTML. This approach is ideally suited for applications that aren’t primarily textual or graphical in nature, such as applications whose document user interface is a combination of text and graphics, or applications that display their document data in a user interface consisting of table views, text and form fields, labeled checkboxes, and so on.

You can also use this approach to convert a document stored in one or more non-human-readable formats for a more user-friendly preview display. The code example in Listing 6-2 illustrates such usage by using Foundation classes to read a [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file and produce a formatted representation for preview. It also creates the properties dictionary to be passed back to Quick Look in the call to [QLPreviewRequestSetDataRepresentation](https://developer.apple.com/documentation/quicklook/1402661-qlpreviewrequestsetdatarepresent); the properties in this dictionary define the HTML data and the attachments associated with that data.

__Listing 6-2__  Generating a preview composed of HTML data plus an attachment

```
OSStatus GeneratePreviewForURL(void *thisInterface, QLPreviewRequestRef preview, CFURLRef url, CFStringRef contentTypeUTI, CFDictionaryRef options)
{
    @autoreleasepool {

        // Load the property list from the URL
        NSURL *nsurl = (__bridge NSURL *)url;
        NSData *data = [NSData dataWithContentsOfURL:nsurl];
        if (!data) return noErr;
        id plist = [NSPropertyListSerialization propertyListWithData:data options:NSPropertyListImmutable format:NULL error:nil];
        if (!plist) return noErr;

        // The above might have taken some time, so before proceeding make sure the user didn't cancel the request
        if (QLPreviewRequestIsCancelled(preview)) return noErr;

        // Set up the object that creates the HTML preview
        HTMLPreviewBuilder *builder = [[HTMLPreviewBuilder alloc] init];
        builder.title = [nsurl lastPathComponent];
        builder.stylesheet = [NSURL URLWithString:@"cid:plistStylesheet.css"];

        // Generate a preview for this plist and retrieve it as a string
        // (Begin recursive preview generation by wrapping the plist's top level object in a dictionary)
        NSString *html = [builder previewForDictionary:@{ @"Root" : plist }];

        // Load a CSS stylesheet to attach to the HTML
        NSBundle *bundle = [NSBundle bundleForClass:[HTMLPreviewBuilder class]];
        NSURL *cssFile = [bundle URLForResource:@"plistStylesheet" withExtension:@"css"];
        NSData *cssData = [NSData dataWithContentsOfURL:cssFile];

        // Put metadata and attachment in a dictionary
        NSDictionary *properties = @{ // properties for the HTML data
                                     (__bridge NSString *)kQLPreviewPropertyTextEncodingNameKey : @"UTF-8",
                                     (__bridge NSString *)kQLPreviewPropertyMIMETypeKey : @"text/html",
                                     // properties for attaching the CSS stylesheet
                                     (__bridge NSString *)kQLPreviewPropertyAttachmentsKey : @{
                                             @"plistStylesheet.css" : @{
                                                     (__bridge NSString *)kQLPreviewPropertyMIMETypeKey : @"text/css",
                                                     (__bridge NSString *)kQLPreviewPropertyAttachmentDataKey: cssData,
                                                     },
                                             },
                                     };

        // Pass preview data and metadata/attachment dictionary to QuickLook
        QLPreviewRequestSetDataRepresentation(preview,
                                              (__bridge CFDataRef)[html dataUsingEncoding:NSUTF8StringEncoding],
                                              kUTTypeHTML,
                                              (__bridge CFDictionaryRef)properties);
    }
    return noErr;
}
```

There are a few things worthy of special notice in Listing 6-2:

- The `properties` dictionary contains the HTML encoding and HTML MIME type (`kQLPreviewPropertyTextEncodingNameKey` and `kQLPreviewPropertyMIMETypeKey`) and any attachment subdictionaries.
- The HTML references the CSS stylesheet attachment using the URL scheme `cid:`_identifier_. The identifier is always used as the key for a dictionary containing attachment data which is included in the `properties` dictionary.
- There is one attachment subdictionary; it contains the MIME type of the CSS stylesheet attachment and the stylesheet data (accessed with `kQLPreviewPropertyMIMETypeKey` and `kQLPreviewPropertyAttachmentDataKey`).

When the generator calls `QLPreviewRequestSetDataRepresentation` it passes in the HTML data (in the specified encoding), the properties dictionary, and the UTI constant identifying HTML content. With the HTML and the properties dictionary set up in this way, WebKit can load the HTML and, when it parses it, load the attachments into the web view.

[Next](Saving%20Previews%20and%20Thumbnails%20in%20the%20Document.md)[Previous](Drawing%20Thumbnails%20and%20Previews%20In%20a%20Graphics%20Context.md)

