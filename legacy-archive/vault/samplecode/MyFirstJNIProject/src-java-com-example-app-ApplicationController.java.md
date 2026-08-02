---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_ApplicationController_java.html
archived_at: '2026-07-18T03:16:35.346299Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-Localizer.java.md)[Previous](src-java-com-example-app-addressbook-PersonSelectionListener.java.md)

# src/java/com/example/app/ApplicationController.java

```
//     File: ApplicationController.java
// Abstract: Central controller of the app.
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

import java.io.File;

import javax.swing.UIManager;
import javax.swing.border.Border;

import com.example.app.addressbook.*;
import com.example.app.mainwindow.MainWindowController;

/**
 * Central controller of the application, holds shared resources, and is
 * the arbiter of what the app can and cannot do at any moment.
 * 
 * This example delegates to two controllers: one for the main window,
 * and the other for the address book palette window. These two windows
 * share localized content, common actions, and similar menu bars.
 * 
 * Larger applications should delegate to sub-controllers which manage
 * more specific resources and its related UI. Document-based apps
 * should create a new sub-controller for each open document that manages
 * the document life cycle (unsaved changes, data model, toolbars, etc).
 */
public class ApplicationController {
    Platform platform;
    Localizer localization;
    Actions actions;

    MainWindowController mainWindowController;
    AddressBookController addressBookController;

    // called on the main() thread
    public void init() {
        platform = new Platform(this);
        localization = new Localizer(this);
        actions = new Actions(this);
        addressBookController = new AddressBookController(this);
        mainWindowController = new MainWindowController(this);

        // ensures the edit button is only enabled if there is a selected person
        addressBookController.addPersonSelectionListener(new PersonSelectionListener() {
            public void personSelected(final Object source, final Person person) {
                actions.editSelectedPerson.setEnabled(person != null);
            }
        });
    }

    // called on the Swing Event Dispatch Thread (EDT)
    public void start(final String[] args) {
        initUIDefaults();

        actions.start();
        addressBookController.start();
        mainWindowController.start();
    }

    void initUIDefaults() {
        // install Mac-specific menu and event handlers
        OSXAppAdapter.installAdapterForController(this);

        // make all new titled borders Aqua-style
        final Border aquaBorder = UIManager.getBorder("TitledBorder.aquaVariant");
        if (aquaBorder != null) UIManager.put("TitledBorder.border", aquaBorder);
    }

    public Platform getPlatform() {
        return platform;
    }

    public Localizer getLocalizer() {
        return localization;
    }

    public Actions getActions() {
        return actions;
    }

    public AddressBookController getAddressBookController() {
        return addressBookController;
    }

    void openFile(final File file) {
        // open file here, for a document based application
    }

    void showAboutBox() {
        // show an about window
    }

    void showPreferences() {
        // show a preferences window
    }

    void showHelp() {
        // show a help window
    }

    boolean requestQuit() {
        // determine if now is a good time to quit

        // Document-based apps should poll the controllers for all
        // open documents, to see if they have unsaved changed, and put
        // up the appropriate prompts.

        return true;
    }

    void doQuit() {
        // closing and disposing the last frame causes the app to exit organically
        addressBookController.dispose();
        mainWindowController.dispose();
        actions.dispose();
    }
}
```

[Next](src-java-com-example-app-Localizer.java.md)[Previous](src-java-com-example-app-addressbook-PersonSelectionListener.java.md)

