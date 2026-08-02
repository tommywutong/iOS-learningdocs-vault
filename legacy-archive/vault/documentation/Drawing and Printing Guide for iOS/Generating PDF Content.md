---
title: Drawing and Printing Guide for iOS
apple_id: TP40010156
resource_type: Guide
platform: watchOS|tvOS|iOS
topic: Graphics & Animation
technology: UIKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/GeneratingPDF/GeneratingPDF.html
archived_at: '2026-07-15T04:56:08.538422Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Drawing and Printing Guide for iOS](About%20Drawing%20and%20Printing%20in%20iOS.md)


[Next](Printing.md)[Previous](Drawing%20and%20Creating%20Images.md)

# Generating PDF Content

The UIKit framework provides a set of functions for generating PDF content using native drawing code. These functions let you create a [graphics context](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/DrawingModel.html#//apple_ref/doc/uid/TP40009071-CH9) that targets a PDF file or PDF data object. You can then create one or more PDF pages and draw into those pages using the same UIKit and Core Graphics drawing routines you use when drawing to the screen. When you are done, what you are left with is a PDF version of what you drew.

The overall drawing process is similar to the process for creating any other image (described in [Drawing and Creating Images](Drawing%20and%20Creating%20Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjtfvjvomi)). It consists of the following steps:

1. Create a PDF context and push it onto the graphics stack (as described in [Creating and Configuring the PDF Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjqfvjvomy)).
2. Create a page (as described in [Drawing PDF Pages](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjqfvjvoni)).
3. Use UIKit or Core Graphics routines to draw the content of the page.
4. Add links if needed (as described in [Creating Links Within Your PDF Content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjqfvjvony)).
5. Repeat steps 2, 3, and 4 as needed.
6. End the PDF context (as described in [Creating and Configuring the PDF Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjqfvjvomy)) to pop the context from the graphics stack and, depending on how the context was created, either write the resulting data to the specified PDF file or store it into the specified [NSMutableData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSMutableData) object.

The following sections describe the PDF creation process in more detail using a simple example. For information about the functions you use to create PDF content, see _UIKit Function Reference_.

You create a PDF graphics context using either the [UIGraphicsBeginPDFContextToData](https://developer.apple.com/documentation/uikit/1623931-uigraphicsbeginpdfcontexttodata) or [UIGraphicsBeginPDFContextToFile](https://developer.apple.com/documentation/uikit/1623927-uigraphicsbeginpdfcontexttofile) function. These functions create the graphics context and associate it with a destination for the PDF data. For the `UIGraphicsBeginPDFContextToData` function, the destination is an `NSMutableData` object that you provide. And for the `UIGraphicsBeginPDFContextToFile` function, the destination is a file in your app’s home directory.

PDF documents organize their content using a page-based structure. This structure imposes two restrictions on any drawing you do:

- There must be an open page before you issue any drawing commands.
- You must specify the size of each page.

The functions you use to create a PDF graphics context allow you to specify a default page size but they do not automatically open a page. After creating your context, you must explicitly open a new page using either the [UIGraphicsBeginPDFPage](https://developer.apple.com/documentation/uikit/1623917-uigraphicsbeginpdfpage) or [UIGraphicsBeginPDFPageWithInfo](https://developer.apple.com/documentation/uikit/1623915-uigraphicsbeginpdfpagewithinfo) function. And each time you want to create a new page, you must call one of these functions again to mark the start of the new page. The `UIGraphicsBeginPDFPage` function creates a page using the default size, while the `UIGraphicsBeginPDFPageWithInfo` function lets you customize the page size and other page attributes.

When you are done drawing, you close the PDF graphics context by calling the [UIGraphicsEndPDFContext](https://developer.apple.com/documentation/uikit/1623929-uigraphicsendpdfcontext). This function closes the last page and writes the PDF content to the file or data object you specified at creation time. This function also removes the PDF context from the graphics context stack.

Listing 4-1 shows the processing loop used by an app to create a PDF file from the text in a text view. Aside from three function calls to configure and manage the PDF context, most of the code is related to drawing the desired content. The `textView` member variable points to the `UITextView` object containing the desired text. The app uses the Core Text framework (and more specifically a [CTFramesetterRef](https://developer.apple.com/documentation/coretext/ctframesetterref) data type) to handle the text layout and management on successive pages. The implementations for the custom `renderPageWithTextRange:andFramesetter:` and `drawPageNumber:` methods are shown in [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjwfvbuqmjqfvjvonq).

__Listing 4-1__  Creating a new PDF file

```objc
- (IBAction)savePDFFile:(id)sender
{
    // Prepare the text using a Core Text Framesetter.
    CFAttributedStringRef currentText = CFAttributedStringCreate(NULL, (CFStringRef)textView.text, NULL);
    if (currentText) {
        CTFramesetterRef framesetter = CTFramesetterCreateWithAttributedString(currentText);
        if (framesetter) {

            NSString *pdfFileName = [self getPDFFileName];
            // Create the PDF context using the default page size of 612 x 792.
            UIGraphicsBeginPDFContextToFile(pdfFileName, CGRectZero, nil);

            CFRange currentRange = CFRangeMake(0, 0);
            NSInteger currentPage = 0;
            BOOL done = NO;

            do {
                // Mark the beginning of a new page.
                UIGraphicsBeginPDFPageWithInfo(CGRectMake(0, 0, 612, 792), nil);

                // Draw a page number at the bottom of each page.
                currentPage++;
                [self drawPageNumber:currentPage];

                // Render the current page and update the current range to
                // point to the beginning of the next page.
                currentRange = [self renderPageWithTextRange:currentRange andFramesetter:framesetter];

                // If we're at the end of the text, exit the loop.
                if (currentRange.location == CFAttributedStringGetLength((CFAttributedStringRef)currentText))
                    done = YES;
            } while (!done);

            // Close the PDF context and write the contents out.
            UIGraphicsEndPDFContext();

            // Release the framewetter.
            CFRelease(framesetter);

        } else {
            NSLog(@"Could not create the framesetter needed to lay out the atrributed string.");
        }
        // Release the attributed string.
        CFRelease(currentText);
    } else {
            NSLog(@"Could not create the attributed string for the framesetter");
    }
}
```


All PDF drawing must be done in the context of a page. Every PDF document has at least one page and many may have multiple pages. You specify the start of a new page by calling the [UIGraphicsBeginPDFPage](https://developer.apple.com/documentation/uikit/1623917-uigraphicsbeginpdfpage) or [UIGraphicsBeginPDFPageWithInfo](https://developer.apple.com/documentation/uikit/1623915-uigraphicsbeginpdfpagewithinfo) function. These functions close the previous page (if one was open), create a new page, and prepare it for drawing. The `UIGraphicsBeginPDFPage` creates the new page using the default size while the `UIGraphicsBeginPDFPageWithInfo` function lets you customize the page size or customize other aspects of the PDF page.

After you create a page, all of your subsequent drawing commands are captured by the PDF graphics context and translated into PDF commands. You can draw anything you want in the page, including text, vector shapes, and images just as you would in your app’s custom views. The drawing commands you issue are captured by the PDF context and translated into PDF data. Placement of content on the the page is completely up to you but must take place within the bounding rectangle of the page.

Listing 4-2 shows two custom methods used to draw content inside a PDF page. The `renderPageWithTextRange:andFramesetter:` method uses Core Text to create a text frame that fits the page and then lay out some text inside that frame. After laying out the text, it returns an updated range that reflects the end of the current page and the beginning of the next page. The `drawPageNumber:` method uses the [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) drawing capabilities to draw a page number string at the bottom of each PDF page.

__Listing 4-2__  Drawing page-based content

```objc
// Use Core Text to draw the text in a frame on the page.
- (CFRange)renderPage:(NSInteger)pageNum withTextRange:(CFRange)currentRange
                 andFramesetter:(CTFramesetterRef)framesetter
{
   // Get the graphics context.
   CGContextRef    currentContext = UIGraphicsGetCurrentContext();

   // Put the text matrix into a known state. This ensures
   // that no old scaling factors are left in place.
   CGContextSetTextMatrix(currentContext, CGAffineTransformIdentity);

   // Create a path object to enclose the text. Use 72 point
   // margins all around the text.
   CGRect    frameRect = CGRectMake(72, 72, 468, 648);
   CGMutablePathRef framePath = CGPathCreateMutable();
   CGPathAddRect(framePath, NULL, frameRect);

   // Get the frame that will do the rendering.
   // The currentRange variable specifies only the starting point. The framesetter
   // lays out as much text as will fit into the frame.
   CTFrameRef frameRef = CTFramesetterCreateFrame(framesetter, currentRange, framePath, NULL);
   CGPathRelease(framePath);

   // Core Text draws from the bottom-left corner up, so flip
   // the current transform prior to drawing.
   CGContextTranslateCTM(currentContext, 0, 792);
   CGContextScaleCTM(currentContext, 1.0, -1.0);

   // Draw the frame.
   CTFrameDraw(frameRef, currentContext);

   // Update the current range based on what was drawn.
   currentRange = CTFrameGetVisibleStringRange(frameRef);
   currentRange.location += currentRange.length;
   currentRange.length = 0;
   CFRelease(frameRef);

   return currentRange;
}

- (void)drawPageNumber:(NSInteger)pageNum
{
   NSString *pageString = [NSString stringWithFormat:@"Page %d", pageNum];
   UIFont *theFont = [UIFont systemFontOfSize:12];
   CGSize maxSize = CGSizeMake(612, 72);

   CGSize pageStringSize = [pageString sizeWithFont:theFont
                                       constrainedToSize:maxSize
                                       lineBreakMode:UILineBreakModeClip];
   CGRect stringRect = CGRectMake(((612.0 - pageStringSize.width) / 2.0),
                                  720.0 + ((72.0 - pageStringSize.height) / 2.0),
                                  pageStringSize.width,
                                  pageStringSize.height);

   [pageString drawInRect:stringRect withFont:theFont];
}
```


Besides drawing content, you can also include links that take the user to another page in the same PDF file or to an external URL. To create a single link, you must add a source rectangle and a link destination to your PDF pages. One of the attributes of the link destination is a string that serves as the unique identifier for that link. To create a link to a specific destination, you specify the unique identifier for that destination when creating the source rectangle.

To add a new link destination to your PDF content, you use the [UIGraphicsAddPDFContextDestinationAtPoint](https://developer.apple.com/documentation/uikit/1623911-uigraphicsaddpdfcontextdestinati) function. This function associates a named destination with a specific point on the current page. When you want to link to that destination point, you use [UIGraphicsSetPDFContextDestinationForRect](https://developer.apple.com/documentation/uikit/1623925-uigraphicssetpdfcontextdestinati) function to specify the source rectangle for the link. Figure 4-1 shows the relationship between these two function calls when applied to the pages of your PDF documents. Tapping on the rectangle surrounding the “see Chapter 1” text takes the user to the corresponding destination point, which is located at the top of Chapter 1.

__Figure 4-1__  Creating a link destination and jump point

!

In addition to creating links within a document, you can also use the [UIGraphicsSetPDFContextURLForRect](https://developer.apple.com/documentation/uikit/1623916-uigraphicssetpdfcontexturlforrec) function to create links to content located outside of the document. When using this function to create links, you specify the target URL and the source rectangle on the current page.

[Next](Printing.md)[Previous](Drawing%20and%20Creating%20Images.md)

