---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_addressbook_AddressBookPaletteBuilder_java.html
archived_at: '2026-07-18T03:16:35.809921Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-addressbook-NativeAddressBook.java.md)[Previous](src-java-com-example-app-addressbook-AddressBookController.java.md)

# src/java/com/example/app/addressbook/AddressBookPaletteBuilder.java

```
//     File: AddressBookPaletteBuilder.java
// Abstract: UI factory class for the address book palette window.
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

package com.example.app.addressbook;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.Comparator;

import javax.swing.*;
import javax.swing.border.*;
import javax.swing.event.*;
import javax.swing.table.DefaultTableCellRenderer;

import com.example.app.*;

/**
 * Creates the UI for the AddressBook palette window.
 */
public class AddressBookPaletteBuilder {
    // create the top level window
    public static JFrame createPaletteWindow(final AddressBookController controller) {
        final Localizer loc = controller.app.getLocalizer();

        final JFrame palette = new JFrame();
        palette.setTitle(controller.app.getLocalizer().getText("address.palette.title", "Contacts"));
        palette.setDefaultCloseOperation(WindowConstants.HIDE_ON_CLOSE);

        // give the window palette behavior on Mac OS X
        palette.getRootPane().putClientProperty("Window.style", "small");
        palette.setAlwaysOnTop(true);

        // add the content
        palette.setJMenuBar(createMenuBar(controller));
        palette.add(createToolbar(controller, loc), BorderLayout.NORTH);
        palette.add(createContentPanel(controller, loc), BorderLayout.CENTER);

        palette.setSize(360, 420);
        return palette;
    }

    private static JMenuBar createMenuBar(final AddressBookController controller) {
        final Action closeAction = controller.app.getLocalizer().new LocalizedAction("address.palette.menu.close", "Close", "W") {
            public void actionPerformed(final ActionEvent e) {
                controller.hideAddressBookWindow();
            }
        };

        return MenuBarBuilder.createMenuBar(controller.app, closeAction);
    }

    static JToolBar createToolbar(final AddressBookController controller, final Localizer loc) {
        final JToolBar toolBar = new JToolBar();
        toolBar.setFloatable(false);

        toolBar.add(createSorters(controller, loc));
        toolBar.add(Box.createGlue());
        toolBar.add(createSearchField(controller));

        return toolBar;
    }

    // creates the first/last sort order button pair
    static Component createSorters(final AddressBookController controller, final Localizer loc) {
        final JPanel panel = new JPanel(new BorderLayout());
        final ButtonGroup group = new ButtonGroup();

        final JToggleButton sortByFirstButton = createSortButton(controller, Person.SORT_BY_FIRST, "first");
        sortByFirstButton.setText(loc.getText("address.palette.sort.first", "First"));
        panel.add(sortByFirstButton, BorderLayout.WEST);
        group.add(sortByFirstButton);

        final JToggleButton sortByLastButton = createSortButton(controller, Person.SORT_BY_LAST, "last");
        sortByLastButton.setText(loc.getText("address.palette.sort.last", "Last"));
        panel.add(sortByLastButton, BorderLayout.EAST);
        group.add(sortByLastButton);

        panel.setMaximumSize(panel.getPreferredSize());
        return panel;
    }

    // creates an individual sort button
    static JToggleButton createSortButton(final AddressBookController controller, final Comparator<Person> mySort, final String position) {
        final JToggleButton sortButton = new JToggleButton(new AbstractAction() {
            public void actionPerformed(final ActionEvent e) {
                controller.setSort(mySort);
            }
        });
        sortButton.setSelected(controller.getSort() == mySort);
        sortButton.setFocusable(false);

        // gives the buttons a paired appearance in Aqua
        sortButton.putClientProperty("JButton.buttonType", "segmented");
        sortButton.putClientProperty("JButton.segmentPosition", position);
        return sortButton;
    }

    static Component createSearchField(final AddressBookController controller) {
        final JTextField searchField = new JTextField(6);
        searchField.putClientProperty("JTextField.variant", "search"); // makes the textfield round in Aqua
        searchField.setMaximumSize(searchField.getPreferredSize()); // prevents the textfield from stretching

        // triggers the "live search" on every modification to the textfield, including
        // copy/paste, complex input events, and not just keystrokes
        searchField.getDocument().addDocumentListener(new DocumentListener() {
            public void changedUpdate(final DocumentEvent e) {
                controller.setFilter(searchField.getText());
            }

            public void insertUpdate(final DocumentEvent e) {
                controller.setFilter(searchField.getText());
            }

            public void removeUpdate(final DocumentEvent e) {
                controller.setFilter(searchField.getText());
            }
        });

        return searchField;
    }

    static Component createContentPanel(final AddressBookController controller, final Localizer loc) {
        final JTable addressTable = createAddressTable(controller);
        final JScrollPane scrollPane = new JScrollPane(addressTable, ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS, ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        scrollPane.setBorder(BorderFactory.createEmptyBorder()); // fits the content right up to the edge of the window
        return scrollPane;
    }

    static JTable createAddressTable(final AddressBookController controller) {
        final JTable addressTable = new JTable(controller.model); // hook up the controller's model to this table

        // only allow a single row to be selected, and tell all interested parties when the selected person changes 
        addressTable.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        addressTable.getSelectionModel().addListSelectionListener(new ListSelectionListener() {
            public void valueChanged(final ListSelectionEvent e) {
                final int index = addressTable.getSelectedRow();
                final Person person = index < 0 ? null : controller.people.get(index);
                controller.personSelectionListeners.personSelected(addressTable, person);
            }
        });

        final Font currentFont = addressTable.getFont();
        addressTable.setFont(currentFont.deriveFont(currentFont.getSize2D() - 1.0f));
        addressTable.setShowGrid(false);
        addressTable.setIntercellSpacing(new Dimension(0, 1));

        // install a custom renderer indent slightly, and show alternating rows in Aqua
        addressTable.setDefaultRenderer(Object.class, new DefaultTableCellRenderer() {
            Border indent = new EmptyBorder(0, 3, 0, 0);
            Border even = UIManager.getBorder("List.evenRowBackgroundPainter");
            Border odd = UIManager.getBorder("List.oddRowBackgroundPainter");
            Border current;

            @Override
            public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {
                Component c = super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
                current = row % 2 == 1 ? even : odd;
                setBorder(indent);
                return c;
            }

            @Override
            protected void paintComponent(Graphics g) {
                // paint the background painter first, then the rest of the component
                if (current != null) current.paintBorder(addressTable, g, 0, 0, getWidth(), getHeight());
                super.paintComponent(g);
            }
        });

        return addressTable;
    }
}
```

[Next](src-java-com-example-app-addressbook-NativeAddressBook.java.md)[Previous](src-java-com-example-app-addressbook-AddressBookController.java.md)

