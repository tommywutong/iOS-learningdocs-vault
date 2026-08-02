---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_mainwindow_MainWindowBuilder_java.html
archived_at: '2026-07-18T03:16:36.056867Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-mainwindow-MainWindowController.java.md)[Previous](src-java-com-example-app-Localizer.java.md)

# src/java/com/example/app/mainwindow/MainWindowBuilder.java

```
//     File: MainWindowBuilder.java
// Abstract: UI factory class which creates the main app window, shows the currently selected person.
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

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.border.*;
import javax.swing.table.*;

import com.example.app.*;

/**
 * Creates a primary window to show the current contact and a button
 * to open the AddressBook palette. Does not need to subclass JFrame,
 * or any other JComponents because it only constructs the UI, and 
 * does not need to override any default Swing behaviors.
 */
public class MainWindowBuilder {
    public static JFrame createMainWindow(final MainWindowController controller) {
        final JFrame frame = new JFrame();
        frame.setTitle(controller.app.getLocalizer().getText("mainwindow.title", "Example Java App"));

        // need to request to close from the controller
        frame.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(final WindowEvent e) {
                controller.closeWindowAction.actionPerformed(new ActionEvent(e.getSource(), ActionEvent.ACTION_PERFORMED, null));
            }
        });

        // add the contents to the frame
        frame.setJMenuBar(createMenuBar(controller));
        frame.add(createToolbar(controller));
        frame.add(createContentPanel(controller));

        return frame;
    }

    static JMenuBar createMenuBar(final MainWindowController controller) {
        return MenuBarBuilder.createMenuBar(controller.app, controller.closeWindowAction);
    }

    static JToolBar createToolbar(final MainWindowController controller) {
        final JToolBar toolBar = new JToolBar();

        // add tool bar items here

        return toolBar;
    }

    static JPanel createContentPanel(final MainWindowController controller) {
        final JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(new EmptyBorder(6, 6, 6, 6));

        panel.add(createAddressPanel(controller), BorderLayout.CENTER);
        panel.add(createAddressBrowserButton(controller), BorderLayout.SOUTH);
        return panel;
    }

    static JPanel createAddressPanel(final MainWindowController controller) {
        final JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(BorderFactory.createTitledBorder(controller.app.getLocalizer().getText("mainwindow.selectedperson.label", "Selected Person")));

        // make a JTable that looks like part of the window background
        // since it does not go into a JScrollPane, it doesn't get any headers
        final JTable personTable = new JTable(controller.selectedPersonTableModel);
        personTable.setIntercellSpacing(new Dimension(15, 1));
        personTable.setBackground(new Color(0, 0, 0, 0)); // clear
        personTable.setOpaque(false); // force full repaint
        personTable.setShowGrid(false);
        personTable.setEnabled(false); // disallow focusing into cells

        final TableColumnModel columnModel = personTable.getTableHeader().getColumnModel();

        // right align the label column by subclassing the default renderer
        columnModel.getColumn(0).setCellRenderer(new DefaultTableCellRenderer() {
            final Font boldFont = personTable.getFont().deriveFont(Font.BOLD);
            @Override
            public Component getTableCellRendererComponent(final JTable table, final Object value, final boolean isSelected, final boolean hasFocus, final int row, final int column) {
                setHorizontalAlignment(SwingConstants.TRAILING);
                final Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                c.setFont(boldFont); // have to set font after calling super, since that resets the font
                return c;
            }
        });

        // make the value column wider
        columnModel.getColumn(1).setMinWidth(210);

        panel.add(personTable, BorderLayout.CENTER);
        panel.add(createDecorationIcon(controller), BorderLayout.WEST);

        return panel;
    }

    static JLabel createDecorationIcon(final MainWindowController controller) {
        final Image image = controller.app.getLocalizer().getIcon("mainwindow.icon");

        final JLabel label = new JLabel(new ImageIcon(image));
        label.setBorder(new EmptyBorder(16, 16, 16, 16));
        label.setVerticalAlignment(SwingConstants.TOP);
        return label;
    }

    static JPanel createAddressBrowserButton(final MainWindowController controller) {
        final JPanel panel = new JPanel(new BorderLayout());

        // create the edit button
        final JButton editButton = new JButton(controller.app.getActions().editSelectedPerson);
        panel.add(editButton, BorderLayout.WEST);

        // create the toggle button
        final JButton addressBookPaletteButton = new JButton(controller.app.getActions().showContactsPicker);
        panel.add(addressBookPaletteButton, BorderLayout.EAST);

        // invoking later, because the new button isn't actually inside its
        // top level window until this function and its callers return
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                // makes button default "return" key responder, adds a pulsing effect in Aqua
                SwingUtilities.getRootPane(addressBookPaletteButton).setDefaultButton(addressBookPaletteButton);
            }
        });

        return panel;
    }
}
```

[Next](src-java-com-example-app-mainwindow-MainWindowController.java.md)[Previous](src-java-com-example-app-Localizer.java.md)

