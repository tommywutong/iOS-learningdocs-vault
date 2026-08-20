---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_OSXAppAdapter_java.html
archived_at: '2026-07-18T03:16:35.629893Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-Platform.java.md)[Previous](src-java-com-example-app-MenuBarBuilder.java.md)

# src/java/com/example/app/OSXAppAdapter.java

```
//     File: OSXAppAdapter.java
// Abstract: Adapter class for the Mac OS X eAWT event handlers.
//  Version: 2.1
// 
// Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
// Inc. ("Apple") in consideration of your agreement to the following
// terms, and your use, installation, modification or redistribution of
// this Apple software constitutes acceptance of these terms.  If you do
// not agree with these terms, please do not use, install, modify or
// redistribute this Apple software.
// 
// In consideration of your agreement to abide by the following terms, and
// subject to these terms, Apple grants you a personal, non-exclusive
// license, under Apple's copyrights in this original Apple software (the
// "Apple Software"), to use, reproduce, modify and redistribute the Apple
// Software, with or without modifications, in source and/or binary forms;
// provided that if you redistribute the Apple Software in its entirety and
// without modifications, you must retain this notice and the following
// text and disclaimers in all such redistributions of the Apple Software.
// Neither the name, trademarks, service marks or logos of Apple Inc. may
// be used to endorse or promote products derived from the Apple Software
// without specific prior written permission from Apple.  Except as
// expressly stated in this notice, no other rights or licenses, express or
// implied, are granted by Apple herein, including but not limited to any
// patent rights that may be infringed by your derivative works or by other
// works in which the Apple Software may be incorporated.
// 
// The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
// MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
// THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
// FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
// OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
// 
// IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
// OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
// MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
// AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
// STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
// 
// Copyright (C) 2011 Apple Inc. All Rights Reserved.
// 

package com.example.app;

import java.awt.event.ActionEvent;
import java.io.File;
import java.util.List;

import com.apple.eawt.*;
import com.apple.eawt.AppEvent.*;

/**
 * Helper class for Mac OS X, which integrates the ApplicationController
 * functions with the native About, Preferences, and Quit menus in the
 * Mac OS X application menu. Also hooks up the open-file action.
 */
public class OSXAppAdapter {
    static void installAdapterForController(final ApplicationController app) {
        // if not on a Mac, don't load the EAWT application
        if (!app.getPlatform().isMac()) return;

        final Application macApp = Application.getApplication();
        final Actions actions = app.getActions();

        macApp.setDefaultMenuBar(MenuBarBuilder.createMenuBar(app, null));

        // link the About action to the EAWT About menu
/* uncomment to suppress the default About handler
        macApp.setAboutHandler(new AboutHandler() {
            public void handleAbout(final AboutEvent e) {
                actions.about.actionPerformed(createActionEventFrom(e.getSource()));
            }
        });
*/

        // link the Preferences action to the EAWT Preferences menu
/* uncomment to suppress the default Preferences handler
        macApp.setPreferencesHandler(new PreferencesHandler() {
            public void handlePreferences(final PreferencesEvent e) {
                actions.preferences.actionPerformed(createActionEventFrom(e.getSource()));
            }
        });
*/

        // open any files claimed by the App's Info.plist
        macApp.setOpenFileHandler(new OpenFilesHandler() {
            public void openFiles(final OpenFilesEvent e) {
                final List<File> files = e.getFiles();
                for (final File file : files) {
                    app.openFile(file);
                }
            }
        });

        // ask the app if now is a good time to quit
        macApp.setQuitHandler(new QuitHandler() {
            public void handleQuitRequestWith(final QuitEvent e, final QuitResponse response) {
                if (app.requestQuit()) {
                    response.performQuit();
                } else {
                    response.cancelQuit();
                }
            }
        });
    }

    static ActionEvent createActionEventFrom(final Object source) {
        return new ActionEvent(source, ActionEvent.ACTION_PERFORMED, null);
    }
}
```

[Next](src-java-com-example-app-Platform.java.md)[Previous](src-java-com-example-app-MenuBarBuilder.java.md)

