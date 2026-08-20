---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_Actions_java.html
archived_at: '2026-07-18T03:16:35.249850Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-addressbook-AddressBookController.java.md)[Previous](MyFirstJNIProject.md)

# src/java/com/example/app/Actions.java

```
//     File: Actions.java
// Abstract: Centralized location for global app actions and their enabled states.
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
import java.awt.event.ActionEvent;
import java.beans.*;
import java.io.File;

import javax.swing.*;
import javax.swing.text.*;

/**
 * Actions can be placed inside of JButtons, JMenus, and also invoked programmatically.
 * Any action which is enabled or disabled will update all of its dependent JComponents.
 * 
 * These Cut, Copy, Paste and Select All actions have special machinery that keeps their enabled
 * state in sync with the current focus owner. This implementation only supports JTextComponents.
 * 
 * Larger applications should likely have Actions that are specific to each
 * of their controllers.
 */
public class Actions implements PropertyChangeListener {
    public final Action openFile;
    public final Action close;
    public final Action about;
    public final Action preferences;
    public final Action quit;
    public final Action help;

    public final Action editSelectedPerson;
    public final Action showContactsPicker;

    public final LocalizedTextAction cut;
    public final LocalizedTextAction copy;
    public final LocalizedTextAction paste;
    public final LocalizedTextAction selectAll;

    LocalizedTextAction[] textFieldActions;
    JTextComponent currentTextComponent;

    public Actions(final ApplicationController app) {
        final Localizer loc = app.getLocalizer();

        openFile = loc.new LocalizedAction("app.open", "Open...", "O") {
            public void actionPerformed(final ActionEvent e) {
                final Frame[] frames = Frame.getFrames();
                if (frames == null || frames.length == 0) return;
                final FileDialog openFileDialog = new FileDialog(frames[0]);
                openFileDialog.setVisible(true);
                final String file = openFileDialog.getFile();
                if (file == null) return;
                app.openFile(new File(file));
            }
        };

        // used on non-Mac OS X platforms
        about = loc.new LocalizedAction("app.about", "About...", null) {
            public void actionPerformed(final ActionEvent e) {
                app.showAboutBox();
            }
        };

        preferences = loc.new LocalizedAction("app.preferences", "Preferences...", null) {
            public void actionPerformed(final ActionEvent e) {
                app.showPreferences();
            }
        };

        quit = loc.new LocalizedAction("app.exit", "Exit", null) {
            public void actionPerformed(final ActionEvent e) {
                final boolean shouldQuit = app.requestQuit();
                if (shouldQuit) app.doQuit();
            }
        };

        help = loc.new LocalizedAction("app.help", "Help", "/") {
            public void actionPerformed(final ActionEvent e) {
                app.showHelp();
            }
        };

        close = loc.new LocalizedAction("app.close", "Close", "W") {
            public void actionPerformed(final ActionEvent e) {
                // nothing to close by default
            }
        };
        close.setEnabled(false);

        cut = new LocalizedTextAction("app.cut", "Cut", "X", DefaultEditorKit.cutAction, loc);
        copy = new LocalizedTextAction("app.copy", "Copy", "C", DefaultEditorKit.copyAction, loc);
        paste = new LocalizedTextAction("app.paste", "Paste", "V", DefaultEditorKit.pasteAction, loc);
        selectAll = new LocalizedTextAction("app.selectAll", "Select All", "A", DefaultEditorKit.selectAllAction, loc);

        textFieldActions = new LocalizedTextAction[] {
            cut, copy, paste, selectAll
        };

        editSelectedPerson = loc.new LocalizedAction("main_window.edit_selected_person", "Edit", null) {
            public void actionPerformed(final ActionEvent e) {
                app.addressBookController.editSelectedPerson();
            }
        };
        editSelectedPerson.setEnabled(false); // start off disabled, will re-enable when a person is selected

        showContactsPicker = loc.new LocalizedAction("main_window.show_contacts_picker", "Show Contacts", null) {
            public void actionPerformed(final ActionEvent e) {
                app.getAddressBookController().showAddressBookPalette();
            }
        };
    }

    void start() {
        KeyboardFocusManager.getCurrentKeyboardFocusManager().addPropertyChangeListener(this);
    }

    void dispose() {
        KeyboardFocusManager.getCurrentKeyboardFocusManager().removePropertyChangeListener(this);
    }

    public void propertyChange(final PropertyChangeEvent evt) {
        // check if this is a focus owner event
        final String changedPropertyName = evt.getPropertyName();
        if (!"permanentFocusOwner".equals(changedPropertyName)) return;

        // check if this is a text component
        final Object newFocusOwner = evt.getNewValue();
        if (newFocusOwner instanceof JTextComponent) {
            currentTextComponent = (JTextComponent)newFocusOwner;
            syncTextFieldActionStateToCurrentComponent();
            return;
        }

        // if not, disable our actions
        for (final Action textFieldAction : textFieldActions) {
            textFieldAction.setEnabled(false);
        }
        currentTextComponent = null;
    }

    // cycle though our text actions, and set them to the enabled state of the actions installed on the current text component
    private void syncTextFieldActionStateToCurrentComponent() {
        final ActionMap actionMap = currentTextComponent.getActionMap();
        for (final LocalizedTextAction textFieldAction : textFieldActions) {
            final Action installedAction = actionMap.get(textFieldAction.delegatedActionID);
            textFieldAction.setEnabled(installedAction == null ? false : installedAction.isEnabled());
        }
    }

    // sends the fired ActionEvent to a specific action of the current text component
    void performTextAction(final ActionEvent e, final String actionID) {
        if (currentTextComponent == null) return;

        final Action targetAction = currentTextComponent.getActionMap().get(actionID);
        if (targetAction == null) return;

        targetAction.actionPerformed(e);
    }

    // helper class that relays events to JTextComponents
    class LocalizedTextAction extends Localizer.LocalizedAction {
        String delegatedActionID;

        LocalizedTextAction(final String key, final String text, final String shortcut, final String delegatedActionID, final Localizer loc) {
            loc.super(key, text, shortcut);
            this.delegatedActionID = delegatedActionID;
        }

        public void actionPerformed(final ActionEvent e) {
            performTextAction(e, delegatedActionID);
        }
    }
}
```

[Next](src-java-com-example-app-addressbook-AddressBookController.java.md)[Previous](MyFirstJNIProject.md)

