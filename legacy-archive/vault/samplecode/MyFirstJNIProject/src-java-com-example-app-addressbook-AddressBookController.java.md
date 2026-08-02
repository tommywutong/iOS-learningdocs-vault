---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_addressbook_AddressBookController_java.html
archived_at: '2026-07-18T03:16:35.745739Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-addressbook-AddressBookPaletteBuilder.java.md)[Previous](src-java-com-example-app-Actions.java.md)

# src/java/com/example/app/addressbook/AddressBookController.java

```
//     File: AddressBookController.java
// Abstract: Central controller for access and display of the NativeAddressBook.
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

import java.awt.Window;
import java.util.*;

import javax.swing.table.DefaultTableModel;

import com.example.app.ApplicationController;

/**
 * Controls the "currently selected person" and the palette window which
 * the user changes it with. Creates the native address book, fetches people
 * from it, sorts them, filters them, and presents them.
 */
public class AddressBookController {
    final ApplicationController app;
    final PersonSelectionListenerList personSelectionListeners = new PersonSelectionListenerList();
    final List<Person> people = new ArrayList<Person>();

    NativeAddressBook addressBook;
    Window palette;

    PeopleTableModel model;
    Comparator<Person> sort = Person.SORT_BY_FIRST;
    String filter;

    public AddressBookController(final ApplicationController appController) {
        this.app = appController;
    }

    public void start() {
        addressBook = new NativeAddressBook();
        model = new PeopleTableModel();

        final Person me = addressBook.getMe();
        personSelectionListeners.personSelected(this, me);
    }

    public void dispose() {
        if (palette == null) return;
        palette.setVisible(false);
        palette.dispose();
    }

    public void showAddressBookPalette() {
        if (palette == null) {
            palette = AddressBookPaletteBuilder.createPaletteWindow(this);
            palette.setLocationRelativeTo(null); // center palette

            updatePeopleList();
        }

        palette.setVisible(true);
        palette.toFront();
    }

    public void editSelectedPerson() {
        addressBook.editPerson(personSelectionListeners.getSelectedPerson());
    }

    void hideAddressBookWindow() {
        if (palette == null) return;
        palette.setVisible(false);
    }

    public void addPersonSelectionListener(final PersonSelectionListener listener) {
        personSelectionListeners.addPersonSelectionListener(listener);
    }

    public void removePersonSelectionListener(final PersonSelectionListener listener) {
        personSelectionListeners.removePersonSelectionListener(listener);
    }

    Comparator<Person> getSort() {
        return sort;
    }

    void setSort(final Comparator<Person> sort) {
        this.sort = sort;
        updatePeopleList();
    }

    void setFilter(final String text) {
        filter = text.toLowerCase(); // filtering all lower case
        updatePeopleList();
    }

    void updatePeopleList() {
        people.clear();
        final List<Person> everyone = addressBook.getEveryone();

        if (filter == null) {
            people.addAll(everyone);
        } else {
            for (final Person person : everyone) {
                final String text = person.getFullSearchText();
                if (text.indexOf(filter) != -1) {
                    people.add(person);
                }
            }
        }

        Collections.sort(people, sort);
        model.fireTableDataChanged();
    }

    class PeopleTableModel extends DefaultTableModel {
        @Override
        public int getColumnCount() {
            return 3;
        }

        @Override
        public int getRowCount() {
            return people.size();
        }

        @Override
        public String getColumnName(final int col) {
            switch (col) {
                case 0: return app.getLocalizer().getText("address.palette.column.name", "Name");
                case 1: return app.getLocalizer().getText("address.palette.column.email", "Email");
                case 2: return app.getLocalizer().getText("address.palette.column.chat", "Chat");
            }
            return "";
        }

        @Override
        public Object getValueAt(final int row, final int col) {
            final Person person = people.get(row);
            switch (col) {
                case 0: return person.getFullName();
                case 1: return person.getEmail();
                case 2: return person.getChat();
            }
            return "";
        }

        @Override
        public boolean isCellEditable(final int row, final int column) {
            return false;
        }
    }
}
```

[Next](src-java-com-example-app-addressbook-AddressBookPaletteBuilder.java.md)[Previous](src-java-com-example-app-Actions.java.md)

