---
title: 'Open the previous document on application startup | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/open-previous-document-on-application.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:3decac9ef719a434'
translated: false
---

> 原文：[Open the previous document on application startup | Cocoa with Love](https://www.cocoawithlove.com/2008/05/open-previous-document-on-application.html)　·　Cocoa with Love (Matt Gallagher)

Setting up your application to open the most recent document on startup is easier than you might think. Here's a quick solution with a some code you can plug straight into your app.

## Recent instead of Untitled

If the user is likely to edit the same document over multiple sessions of the application, automatically opening the last edited document when your app starts up is a helpful option to offer.

To make this easier for us, Mac OS X automatically remembers the last ten documents opened.

We are left with three steps to make this happen:

- Prevent the default "Untitled" document opening
- Open the most recent document as reported by the shared NSDocumentController
- Allow "Untitled" documents to open after startup

## All in the application delegate

The application's delegate is the appropriate place to do this work, most of which will occur in the delegate method applicationShouldOpenUntitledFile:.

Normally, this method returns YES. Even if we want the most recent document to open at startup, we will want this method to return YES after startup.

But we can't directly ask NSApplication if it is starting up, so we must keep a flag applicationHasStarted that should be initialized to NO in the delegate's constructor and set to YES in applicationDidFinishLaunching:. In the code example below, I assume you've already set up this behavior and I don't show it explicitly.

So, inside the body of applicationShouldOpenUntitledFile:, if applicationHasStarted is NO, we ask the shared NSDocumentController for the most recent document, get the URL of this document and open it, returning NO from applicationShouldOpenUntitledFile: to prevent the untitled document appearing.

## Solution

```objc
- (BOOL)applicationShouldOpenUntitledFile:(NSApplication *)sender
{
    // On startup, when asked to open an untitled file, open the last opened
    // file instead
    if (!applicationHasStarted)
    {
        // Get the recent documents
        NSDocumentController *controller =
            [NSDocumentController sharedDocumentController];
        NSArray *documents = [controller recentDocumentURLs];
        
        // If there is a recent document, try to open it.
        if ([documents count] > 0)
        {
            NSError *error = nil;
            [controller
                openDocumentWithContentsOfURL:[documents objectAtIndex:0]
                display:YES error:&error];
            
            // If there was no error, then prevent untitled from appearing.
            if (error == nil)
            {
                return NO;
            }
        }
    }
    
    return YES;
}
```
