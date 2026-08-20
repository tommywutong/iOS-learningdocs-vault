---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_Localizer_java.html
archived_at: '2026-07-18T03:16:35.427818Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-mainwindow-MainWindowBuilder.java.md)[Previous](src-java-com-example-app-ApplicationController.java.md)

# src/java/com/example/app/Localizer.java

```
//     File: Localizer.java
// Abstract: Stub implementation of a class that vends localized resources.
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

import java.awt.*;
import java.awt.image.BufferedImage;

import javax.swing.*;

/**
 * Placeholder class for localization support. Also useful for changing keyboard
 * shortcuts or menu names based on platform as well as language (Meta-W vs. Alt-F4
 * for close, Meta-R vs. F5 for refresh, etc). This class should be expanded to load
 * localized resources via ResourceBundles or other mechanisms of your choosing.
 */
public class Localizer {
    final ApplicationController controller;

    public Localizer(final ApplicationController controller) {
        this.controller = controller;
    }

    public String getText(final String key, final String fallback) {
        // get regionalized strings here, returning fallbacks for this example
        return fallback;
    }

    public KeyStroke getKeyStroke(final String key, final String fallback) {
        // get platform and region-specific keystrokes here, returning platform-split fallbacks for this example
        if (fallback == null) return null;
        final String prefix = controller.getPlatform().getShortcutKey();
        return KeyStroke.getKeyStroke(prefix + " " + fallback);
    }

    public Image getIcon(final String key) {
        // for this example, only returning an icon for the main window, and a blank icon on non-Mac platforms
        if (!"mainwindow.icon".equals(key)) return null;
        if (!controller.getPlatform().isMac()) return new BufferedImage(32, 32, BufferedImage.TYPE_INT_ARGB);

        // using NSImage:// syntax to access AppKit named images
        // see the named images section for more constants at
        // http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/nsimage_Class/Reference/Reference.html
        return Toolkit.getDefaultToolkit().getImage("NSImage://NSEveryone");
    }

    /*
     * helper action class to make creating fully localized actions easier
     * see usage in Actions.java
     */
    public abstract class LocalizedAction extends AbstractAction {
        public LocalizedAction(final String key, final String text, final String shortcut) {
            putValue(Action.NAME, getText(key + ".text", text));
            if (shortcut != null) {
                putValue(Action.ACCELERATOR_KEY, getKeyStroke(key + ".keystroke", shortcut));
            }
            putValue(Action.SMALL_ICON, getIcon(key + ".icon"));
        }
    }
}
```

[Next](src-java-com-example-app-mainwindow-MainWindowBuilder.java.md)[Previous](src-java-com-example-app-ApplicationController.java.md)

