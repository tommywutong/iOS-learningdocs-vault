---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_addressbook_NativeAddressBook_java.html
archived_at: '2026-07-18T03:16:35.881603Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-addressbook-Person.java.md)[Previous](src-java-com-example-app-addressbook-AddressBookPaletteBuilder.java.md)

# src/java/com/example/app/addressbook/NativeAddressBook.java

```
//     File: NativeAddressBook.java
// Abstract: Accesses the native address book, and vends Person objects.
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

import java.util.*;

/**
 * Abstraction for the Mac OS X AddressBook API
 * 
 * Creates a copy of contacts from the address book, and vends Person
 * objects. Uses JNI to obtain simple List, Map, String, and Number
 * representations of ABPerson properties.
 */
public class NativeAddressBook {
    static {
        // ensure native JNI library is loaded
        System.loadLibrary("AddressBook");
    }

    // JNI method which obtains the UID of the "me" card in Address Book.app
    private static native String nativeGetMyUID();

    // JNI method that fetches the list of everyone as a list of maps
    private static native List<Map<String,?>> nativeGetAddressBookContacts();

    private static native void nativeEditContact(final String uid);

    List<Person> everyone;

    public List<Person> getEveryone() {
        if (everyone != null) return everyone;

        final List<Map<String, ?>> rawContacts = nativeGetAddressBookContacts();
        final List<Person> people = new ArrayList<Person>();
        for (final Map<String, ?> rawContact : rawContacts) {
            final Person person = new Person(rawContact);
            if ("".equals(person.getFullName())) continue; // strip out the nameless
            people.add(person);
        }

        return everyone = Collections.unmodifiableList(people);
    }

    public Person getMe() {
        final String myUID = nativeGetMyUID();
        if (myUID == null) return null;

        final List<Person> people = getEveryone();
        for (final Person person : people) {
            if (myUID.equals(person.getUID())) return person;
        }

        return null;
    }

    public void editPerson(final Person person) {
        if (person == null) throw new NullPointerException("Cannot edit a null person");

        final String uid = person.getUID();
        if (uid == null) throw new NullPointerException("Cannot edit a person with a null UID");

        nativeEditContact(uid);
    }
}
```

[Next](src-java-com-example-app-addressbook-Person.java.md)[Previous](src-java-com-example-app-addressbook-AddressBookPaletteBuilder.java.md)

