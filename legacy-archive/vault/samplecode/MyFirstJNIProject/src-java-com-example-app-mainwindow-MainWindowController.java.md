---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_mainwindow_MainWindowController_java.html
archived_at: '2026-07-18T03:16:36.115313Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-MenuBarBuilder.java.md)[Previous](src-java-com-example-app-mainwindow-MainWindowBuilder.java.md)

# src/java/com/example/app/mainwindow/MainWindowController.java

```
//     File: MainWindowController.java
// Abstract: Controller for the main app window, manages the display of the currently selected person.
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

package com.example.app.mainwindow;

import java.awt.event.*;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;

import com.example.app.*;
import com.example.app.addressbook.*;

/**
 * Controls the main window which shows the currently selected person.
 * 
 * Unlike most applications, once the main window is closed a quit
 * is requested, and all the controllers are disposed, and the app should
 * exit organically.
 * 
 * Swing will automatically terminate the process if there are no more
 * windows open, no background threads running, and no more events left
 * to process in the event queue.
 */
public class MainWindowController {
    final ApplicationController app;

    SelectedPersonTableModel selectedPersonTableModel;
    JFrame mainWindow;
    Action closeWindowAction;

    public MainWindowController(final ApplicationController appController) {
        this.app = appController;
    }

    public void start() {
        selectedPersonTableModel = new SelectedPersonTableModel();
        app.getAddressBookController().addPersonSelectionListener(selectedPersonTableModel);

        closeWindowAction = app.getLocalizer().new LocalizedAction("mainwindow.close", "Close", "W") {
            public void actionPerformed(final ActionEvent e) {
                final boolean windowShouldClose = requestMainWindowClose();
                if (!windowShouldClose) return;
                closeWindow();
            }
        };

        mainWindow = MainWindowBuilder.createMainWindow(this);
        mainWindow.pack();
        mainWindow.addComponentListener(new ComponentAdapter() {
            public void componentHidden(final ComponentEvent e) {
                app.getActions().quit.actionPerformed(null);
            }
        });

        bringMainWindowToFront();
    }

    public void bringMainWindowToFront() {
        mainWindow.setVisible(true);
        mainWindow.toFront();
    }

    boolean requestMainWindowClose() {
        // should the main window close?

        return true;
    }

    void closeWindow() {
        mainWindow.setVisible(false);
    }

    public void dispose() {
        closeWindow();
        mainWindow.dispose();
        app.getAddressBookController().removePersonSelectionListener(selectedPersonTableModel);
    }

    // JTable model which listens for the "currently selected person"
    class SelectedPersonTableModel extends DefaultTableModel implements PersonSelectionListener {
        Person selectedPerson;

        public void personSelected(final Object source, final Person person) {
            this.selectedPerson = person;
            fireTableDataChanged();
        }

        @Override
        public Object getValueAt(final int row, final int column) {
            if (column != 1) {
                final Localizer loc = app.getLocalizer();
                switch (row) {
                    case 0: return loc.getText("person.name", "Name");
                    case 1: return loc.getText("person.email", "Email");
                    case 2: return loc.getText("person.number", "Phone");
                    case 3: return loc.getText("person.chat", "Chat");
    //              case 4: return "UID";
                }
            } else if (selectedPerson != null) {
                switch (row) {
                    case 0: return selectedPerson.getFullName();
                    case 1: return selectedPerson.getEmail();
                    case 2: return selectedPerson.getPhone();
                    case 3: return selectedPerson.getChat();
    //              case 4: return selectedPerson.getUID();
                }
            }
            return "";
        }

        @Override
        public int getColumnCount() {
            return 2;
        }

        @Override
        public int getRowCount() {
            return 4;
        }

        @Override
        public boolean isCellEditable(final int row, final int column) {
            return false;
        }
    }
}
```

[Next](src-java-com-example-app-MenuBarBuilder.java.md)[Previous](src-java-com-example-app-mainwindow-MainWindowBuilder.java.md)

