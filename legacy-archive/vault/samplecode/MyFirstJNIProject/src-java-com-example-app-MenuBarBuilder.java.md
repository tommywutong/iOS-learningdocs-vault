---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_MenuBarBuilder_java.html
archived_at: '2026-07-18T03:16:35.578400Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-OSXAppAdapter.java.md)[Previous](src-java-com-example-app-mainwindow-MainWindowController.java.md)

# src/java/com/example/app/MenuBarBuilder.java

```
//     File: MenuBarBuilder.java
// Abstract: Centralized builder for menus, creates a consistent set of menu items across frames.
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

import javax.swing.*;

/**
 * Creates a consistent menu bar experience across both windows.
 * 
 * Since the only differentiation between this sample's two windows is the close
 * action, this one class can be responsible for assembling the entire menu bar.
 * 
 * Certain menu items are not added on the Mac because they are expected to be
 * handled by the OSXAppAdapter installing an EAWT ApplicationListener.
 */
public class MenuBarBuilder {
    public static JMenuBar createMenuBar(final ApplicationController app, final Action closeAction) {
        final JMenuBar menuBar = new JMenuBar();

        menuBar.add(createFileMenu(app, closeAction));
        menuBar.add(createEditMenu(app));
        menuBar.add(createHelpMenu(app));

        return menuBar;
    }

    static JMenu createFileMenu(final ApplicationController app, final Action closeAction) {
        final JMenu menu = new JMenu(app.getLocalizer().getText("app.file.menu", "File"));

        menu.add(new JMenuItem(app.getActions().openFile));
        menu.add(new JMenuItem(closeAction != null ? closeAction : app.getActions().close));

        if (app.getPlatform().usesFileMenuForQuit()) {
            menu.addSeparator();
            menu.add(new JMenuItem(app.getActions().quit));
        }

        return menu;
    }

    static JMenu createEditMenu(final ApplicationController app) {
        final JMenu menu = new JMenu(app.getLocalizer().getText("app.edit.menu", "Edit"));

        menu.add(new JMenuItem(app.getActions().cut));
        menu.add(new JMenuItem(app.getActions().copy));
        menu.add(new JMenuItem(app.getActions().paste));
        menu.add(new JMenuItem(app.getActions().selectAll));
        if (app.getPlatform().usesEditMenuForPreferences()) {
            menu.addSeparator();
            menu.add(new JMenuItem(app.getActions().preferences));
        }

        return menu;
    }

    static JMenu createHelpMenu(final ApplicationController app) {
        final JMenu menu = new JMenu(app.getLocalizer().getText("app.help.menu", "Help"));

        if (app.getPlatform().usesHelpMenuForAbout()) {
            menu.add(new JMenuItem(app.getActions().about));
            menu.addSeparator();
        }
        menu.add(new JMenuItem(app.getActions().help));

        return menu;
    }
}
```

[Next](src-java-com-example-app-OSXAppAdapter.java.md)[Previous](src-java-com-example-app-mainwindow-MainWindowController.java.md)

